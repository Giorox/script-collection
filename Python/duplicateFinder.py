#!/usr/bin/python
# Script to check if there are duplicate files anywhere in the folder structure
# Usage: python duplicateFinder.py -f <Root Folder>[-h]
# -f [--folder=]  Path to folder to be searched
# -h [--help]   Displays the help message
# Author: Giovanni Fazolo Silva Rebouças
# Date: 19 November 2019
# Version: v0.0.2 (29 November 2019)
import os  # Import os.path,join and os.walk functions
import sys  # Import function to pull arguments from sys environment
import getopt  # Import functionality to parse arguments directly from choosen CLI
import time  # Import functions to deal with time
import logging  # Import logging functions


class StatusBuilder:
    def __init__(self, argv):
        # Variables to store arguments passed through the command line
        self.folderpath = ''  # Global variable used to store path to network folder once resolved
        self.IGNORED_FOLDERS = [".git", "hooks", "info", "logs", "objects", "refs", "npc"]
        self.IGNORED_EXTENSIONS = ["lua"]

        # Parsing through script call for arguments
        try:
            opts, args = getopt.getopt(argv, "f:h", ["folder=", "help"])
        except getopt.GetoptError:
            print("python duplicateFinder.py -f <Root Folder>[-h]")
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("python duplicateFinder.py -f <Root Folder>[-h]")
                sys.exit()
            elif opt in ("-f", "--folder"):
                self.folderpath = arg

        # Call function to pull network folder file structure
        baselineFSFiles = self.pullFileSysStructure()

        dupes = self.verifyPresence(baselineFSFiles)

        with open("duplicate_files.txt", "w") as result:
            result.writelines(dupes)

    def pullFileSysStructure(self):
        files = []  # Initializes list of file paths inside of network folder

        # Start walking and pulling file paths from the network folder
        logging.info("Pulling file structure from: " + str(self.folderpath))
        for r, d, f in os.walk(self.folderpath):  # r=root, d=directories, f = files
            # Else, start analyzing files inside of folder
            for filename in f:
                try:
                    extension = filename.split(".")[-1]
                except IndexError:
                    break
                finally:
                    if extension not in self.IGNORED_EXTENSIONS:
                        finalfilepath = filename.lower()
                        files.append(finalfilepath.lstrip("\"").rstrip("\"") + "\n")

        logging.info("Finished pulling network folder's file structure.")
        return files

    def verifyPresence(self, fileList):
        logging.info("Starting duplicate verification...")
        exists = {}
        duplicate = []
        # Check if a file in the network folder is in the repository
        for file in fileList:
            if file not in exists:
                exists[file] = 1
            else:
                if exists[file] == 1:
                    duplicate.append(file)
                exists[file] += 1

        return duplicate


if __name__ == "__main__":
    # Configuring logging parameters
    logging.basicConfig(filename='Git_checking_errors.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Get epoch at script start to measure elapsed time and log script start date and time
    start_time = time.time()
    logging.info("Script started at: " + str(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())))

    # Instantiate a StatusBuilder object and pass command line arguments to be treated by getopt
    builder = StatusBuilder(sys.argv[1:])

    # Log information of elapsed time at script end (This line will only execute after class' constructor finishes)
    logging.info("Script Ended - Elapsed time: %s seconds" % (time.time() - start_time))
