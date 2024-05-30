#include <opencv2/opencv.hpp>
#include <chrono>
#include <iostream>
#include <thread>
#include <vector>
using namespace std;

// High-pass filtering through 2D convolution
// Parallel using pThread

#define NUM_THREADS 4 // Number of threads

// Define our highpass filter kernels
cv::Mat highpass1 = (cv::Mat_<float>(3, 3) << 0, -1, 0, -1, 4, -1, 0, -1, 0);
cv::Mat highpass2 = (cv::Mat_<float>(3, 3) << -1, -1, -1, -1, 8, -1, -1, -1, -1);

// Vector of resulting video frames
vector<cv::Mat> finalVideo;

// Signal flags for pipeline tasks
vector<bool> isDataReady(NUM_THREADS, false);

// Function that enables task separation
void filterDemux(int taskID, int threadID, cv::Mat& frame, cv::Mat& resultingFrame)
{
    if (taskID == 0)
    {
        // Process the frame through the first filter
        cv::filter2D(frame, resultingFrame, -1, highpass1);

        // Signal that the data is available
        isDataReady[threadID] = true;
    }
    else if (taskID == 1)
    {
        // Wait until the thread who has task 0 to report that our data is ready and that the input frame IS NOT empty
        while (!isDataReady[threadID]);

        // Process the frame through the second filter
        cv::filter2D(frame, resultingFrame, -1, highpass2);

        // Reset to allow for next loop iteration
        isDataReady[threadID] = false;
    }
}

// Function that will be executed in each thread
void frameFiltering(int id, int start, int end)
{
    // Capture the frame of the input video file
    cv::VideoCapture capture("videos/op_video.mp4");

    // Check that we were able to open the input video
    if (!capture.isOpened())
    {
        cout << "Error opening video file" << endl;
        cout << "Killing thread - ID: " << id << endl;
        return;
    }

    cout << "Opened video in thread: " << id << endl;

    // Set the index of the frame where we want to start processing
    int caretPosition = (start > 0) ? start : 1;
    capture.set(cv::CAP_PROP_POS_FRAMES, caretPosition);

    // Iterate over every single frame of the video
    for (int frameIndex = start; frameIndex < end; frameIndex++)
    {
        // These are, in order, the original video frame, the frame after passing through highpass1 filter and the frame after passing through highpass2 filter
        cv::Mat frame, filteredFrame1, filteredFrame2;

        // Read the next frame from the video
        capture.read(frame);

        cout << "Thread: " << id << " - Converting frame " << frameIndex + 1 << " of " << end << ".\n";

        // Check if the frame is empty for some reason (encoding, reading or display errors)
        // Skip if so to prevent breaking
        if (frame.empty())
        {
            cout << "Frame " << frameIndex << " of " << end << " returned empty!!!!";
            continue;
        }

        // Instatiante pipeline threads
        thread applyFilter1, applyFilter2;

        // We can spawn a thread that will apply the first filter and the next thread will take the previous one's input
        // to then apply a second thread
        applyFilter1 = thread(filterDemux, 0, id, ref(frame), ref(filteredFrame1));
        applyFilter2 = thread(filterDemux, 1, id, ref(filteredFrame1), ref(filteredFrame2));

        // Barrier
        applyFilter1.join();
        applyFilter2.join();

        // Write the filtered frame to the vector of the final video
        finalVideo[frameIndex] = filteredFrame2;
    }

    // Release our capture
    capture.release();
}

int main() 
{
    // Instantiate an array of threads
    thread threads[NUM_THREADS];

    // Open the input file to get our metadata
    cv::VideoCapture capture("videos/coco_video.mp4");

    // Check that we were able to open the input video
    if (!capture.isOpened())
    {
        cout << "Error opening video file" << endl;
        return -1;
    }

    cout << "Loaded video\n";

    // Read the videos properties
    int frameWidth = (int)capture.get(cv::CAP_PROP_FRAME_WIDTH);
    int frameHeight = (int)capture.get(cv::CAP_PROP_FRAME_HEIGHT);
    int frameCount = (int)capture.get(cv::CAP_PROP_FRAME_COUNT);
    double fps = capture.get(cv::CAP_PROP_FPS);
    double codec = capture.get(cv::CAP_PROP_FOURCC);

    // Release the capture
    capture.release();

    // Set the size for the resulting video vector
    finalVideo.resize(frameCount);

    // Split our frame count for each thread
    int portionSize = frameCount / NUM_THREADS;

    // Get current time - start time
    auto t1 = chrono::high_resolution_clock::now();

    // Separate portions of the frames to each thread
    for (int j = 0; j < NUM_THREADS; j++)
    {
        // Calculate index sizes for each portion
        int start = j * portionSize;
        int end = start + portionSize - 1;

        // Set all remaining values to the last thread - Solves the division remainder problem
        if (j == NUM_THREADS - 1)
        {
            end = frameCount;
        }

        // Instantiate threads
        threads[j] = thread(frameFiltering, j, start, end);
    }

    // Barrier, join all threads
    for (int j = 0; j < NUM_THREADS; j++)
    {
        threads[j].join();
    }

    // Get current time - end time
    auto t2 = chrono::high_resolution_clock::now();

    // Open a VideoWrite object to write the output to file
    cv::VideoWriter writer("output/filteredVideo.mp4", codec, fps, cv::Size(frameWidth, frameHeight));
    cout << "Opening output file\n";

    if (!writer.isOpened())
    {
        cout << "Error opening output video file" << endl;
        return -1;
    }

    cout << "Opened output file. Writing to output...\n";

    // Write all frames of the resulting array to a video
    for (int i = 0; i < finalVideo.size(); i++)
    {
        writer.write(finalVideo[i]);
    }
    
    cout << "Finished writing";

    // Release the writer
    writer.release();

    // Calculate how long it took
    auto duration = chrono::duration_cast<chrono::seconds> (t2 - t1).count();

    // Report and Exit
    cout << "\nAlgorithm duration: " << duration << " (s).\n";

    return 0;
}