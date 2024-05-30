#include <iostream>
#include <vector>
#include <chrono>
#include <opencv2/opencv.hpp>
using namespace std;

// High-pass filtering through 2D convolution
// Sequential

// Apply the filter to the image
vector<vector<int>> convolute(vector<vector<int>> image, vector<vector<int>> filter)
{
    int filterSize = filter.size();
    int paddingSize = filterSize / 2;
    int imageWidth = image.size();
    int imageHeight = image[0].size();
    vector<vector<int>> filteredImage(imageWidth, vector<int>(imageHeight, 0));

    // Create a padded version of the image to handle boundary pixels
    vector<vector<int>> paddedImage(imageWidth + paddingSize * 2, vector<int>(imageHeight + paddingSize * 2, 0));
    for (int i = 0; i < imageWidth; ++i)
    {
        for (int j = 0; j < imageHeight; ++j)
        {
            paddedImage[i + paddingSize][j + paddingSize] = image[i][j];
        }
    }

    // Apply the filter to the image
    // First 2 loops go through the actual image
    for (int i = 0; i < imageWidth; ++i)
    {
        for (int j = 0; j < imageHeight; ++j)
        {
            // These 2 loops does the product and the equivalent sum between the filter matrix and the padded image portion matrix
            int sum = 0;
            for (int k = -paddingSize; k <= paddingSize; ++k)
            {
                for (int l = -paddingSize; l <= paddingSize; ++l)
                {
                    sum += filter[k + paddingSize][l + paddingSize] * paddedImage[i + paddingSize + k][j + paddingSize + l];
                }
            }
            filteredImage[i][j] = sum;
        }
    }

    return filteredImage;
}


// Function to print our matrices
void printMatrix(vector<vector<int>> printableMatrix)
{
    for (int i = 0; i < printableMatrix.size(); i++)
    {
        for (int j = 0; j < printableMatrix[0].size(); j++)
        {
            cout << printableMatrix[i][j] << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> convertFrameToVector(cv::Mat channel)
{
    // Convert the channel from unsigned char to integer
    cv::Mat channelInt;
    channel.convertTo(channelInt, CV_32S);

    // Convert channel to vector of vector
    vector<vector<int>> channelVec(channelInt.rows, vector<int>(channelInt.cols));

    for (int i = 0; i < channelInt.rows; ++i)
    {
        for (int j = 0; j < channelInt.cols; ++j)
        {
            channelVec[i][j] = channelInt.at<int>(i, j);
        }
    }

    return channelVec;
}

cv::Mat convertVectorToFrame(vector<vector<int>> vectorCh)
{
    // Declare our new Mat channel
    cv::Mat channel(vectorCh.size(), vectorCh[0].size(), CV_32S);

    // Convert our vector of vector to channel
    for (int i = 0; i < vectorCh.size(); ++i)
    {
        for (int j = 0; j < vectorCh[0].size(); ++j)
        {
            channel.at<int>(i, j) = vectorCh[i][j];
        }
    }

    // Convert the new Material from integer to unsigned char 
    cv::Mat channelChar;
    channel.convertTo(channelChar, CV_8U);

    return channelChar;
}

int main()
{
    // Define our high-pass filter
    vector<vector<int>> highpassFilter1 = { {0, -1, 0},
                                       {-1,  4, -1},
                                       {0, -1, 0} };

    vector<vector<int>> highpassFilter2 = { {-1, -1, -1},
                                       {-1,  8, -1},
                                       {-1, -1, -1} };

    cout << "\nFilter Matrix - H1: \n";
    printMatrix(highpassFilter1);
    cout << "\nFilter Matrix - H2: \n";
    printMatrix(highpassFilter2);

    // Open the video file
    cv::VideoCapture video("videos/coco_video.mp4");

    // Check that we were able to open the video
    if (!video.isOpened())
    {
        cout << "Error opening video file" << endl;
        return -1;
    }

    cout << "Loaded video\n";

    // Get current time - start time
    auto t1 = chrono::high_resolution_clock::now();

    // Read the videos properties
    int frameWidth = (int) video.get(cv::CAP_PROP_FRAME_WIDTH);
    int frameHeight = (int) video.get(cv::CAP_PROP_FRAME_HEIGHT);
    double fps = video.get(cv::CAP_PROP_FPS);
    int frameCount = (int)video.get(cv::CAP_PROP_FRAME_COUNT);

    // Declare the vector of Mat objects that represent the new video
    vector<cv::Mat> newVideoFrames(frameCount);

    // Iterate over all frames of the original video
    for (int frameIndex = 0; frameIndex < frameCount; frameIndex++)
    {
        //cout << "Converting frame " << frameIndex + 1 << " of " << frameCount << ".\n";
        cout << "Converting frame " << frameIndex + 1 << " of " << frameCount << ".\n";

        // Declare a frame object and read the next frame from the video
        cv::Mat frame;
        video >> frame;

        // Check if the frame is empty for some reason (encoding, reading or display errors)
        // Skip if so to prevent breaking
        if (frame.empty())
        {
            continue;
        }

        // Split the frame into color channels
        // When doing this, OpenCV converts the colorspace to BGR, which means that channels[0] is Blue,
        // channels[1] is Green and channels[2] is Red
        vector<cv::Mat> channels;
        cv::split(frame, channels);

        // A 3 dimensional vector that stores the integer representation of the filtered frames
        vector<vector<vector<int>>> filteredFrames(3, vector<vector<int>>(frame.rows, vector<int>(frame.cols)));

        // Convert our channels to vector of vector of integers
        // Apply both filters to the image and save them to the filtered frame array
        for (int i = 0; i < channels.size(); i++)
        {
            vector<vector<int>> imagem = convertFrameToVector(channels[i]);
            vector<vector<int>> imagemFiltradaH1 = convolute(imagem, highpassFilter1);
            vector<vector<int>> imagemFiltradaH2 = convolute(imagemFiltradaH1, highpassFilter2);

            filteredFrames[i] = imagemFiltradaH2;
        }
        
        // A vector of materials for our reconverted channels
        vector<cv::Mat> reconvertedChannels(3);

        // Merge all 2D vectors back into a OpenCV Frame
        // Save each NEW frame to a special vector to be put back together into a video
        for (int i = 0; i < filteredFrames.size(); i++)
        {
            reconvertedChannels[i] = convertVectorToFrame(filteredFrames[i]);
        }

        // Merge our reconverted Channels back into a frame
        cv::Mat filteredFrame;
        cv::merge(reconvertedChannels, filteredFrame);

        // Save the new frame to our array of frames that represents a new video
        newVideoFrames[frameIndex] = filteredFrame;
    }

    // Get current time - end time
    auto t2 = chrono::high_resolution_clock::now();

    // Close the input video file
    //video.release();

    // Open a VideoWrite object to write the output to file
    cv::VideoWriter writer("output/filteredVideo.mp4", video.get(cv::CAP_PROP_FOURCC), fps, cv::Size(frameWidth, frameHeight));
    cout << "Opening output file";

    if (!writer.isOpened())
    {
        cout << "Error opening output video file" << endl;
        return -1;
    }

    cout << "Output file opened. Writing...";

    // Once it's all converted, create a video out of the frame vector and show it to the user
    for (int i = 0; i < newVideoFrames.size(); i++)
    {
        writer.write(newVideoFrames[i]);
    }

    cout << "Output file written";
    //writer.release();

    // Calculate how long it took
    auto duration = chrono::duration_cast<chrono::seconds> (t2 - t1).count();

    // Report and Exit
    cout << "\nAlgorithm duration: " << duration << " (s).";

    return 0;
}