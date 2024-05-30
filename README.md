# Script Collection

A collection of scripts written in many different programming languages and each developed independently to perform very specific tasks (big or small). This repository was made in order to have a centralized place where scripts developed during my day-to-day activities in order to facilitate a certain task could be stored and tracked.

This repository is an amalgamation of my personal collection of scripts developed over the years aswell as the ones previously stored in the [CharliePapaPapa-Algorithms](https://github.com/Giorox/CharliePapaPapa-Algorithms) repository which held a collection of C++ scripts with comments localized in English and Brazilian Portuguese.

-----------

## Project Goal

The main goal of this repository is to have implementations of famous, useful or novelty algorithms in differente programming languages and have these be available so students, teachers, self-taught, coders, mathematicians, scientists, free-lancers and anyone else that is interested in Computer Science/Engineering can make good use of these.

## Contributions

This project started as an idea to centralize day-to-day, small scripts that extended above simple snippets but weren't big enough to be deserving of their own repositories. Contributions, fixes and suggestions are all welcome via pull-requests to this repository but be aware that they will be accepted or denied at the author's discretion with comments where applicable/necessary.

That being said, we expect a certain degree of conformity to coding standards, nomenclature, organization and overall quality favoring language-specific references where possible/available (e.g. PEP8 for Python)

-----------

## Table of Contents

### C++

- Boyer-Moore-Horspool Algorithm for text-in-text search ([Boyer-Moore-Horspool Algorithm.cpp](C++/Boyer-Moore-Horspool Algorithm.cpp))
- Karatsuba-Ofman Algorithm for fast big integer multiplication ([Karatsuba-Ofman Algorithm.cpp](C++/Karatsuba-Ofman Algorithm.cpp))
- Levenshtein Distance calculator using Dynamic Programming Techniques ([Levenshtein Distance using Dynamic Programming.cpp](C++/Levenshtein Distance using Dynamic Programming.cpp))
- Map data-structure implementation in pure C++ ([Map Implementation.cpp](C++/Map Implementation.cpp))
- Bubble Sort Algorithm ([BubbleSort.cpp](C++/BubbleSort.cpp))
- Quick Sort Algorithm ([QuickSort.cpp](C++/QuickSort.cpp))
- Selection Sort Algorithm ([SelectionSort.cpp](C++/SelectionSort.cpp))
- High-pass filtering of videos through 2-dimensional convolution in a:
  - Sequential manner ([SequentialConvolution.cpp](C++/SequentialConvolution.cpp))
  - Parallel manner using pThread library ([ParallelConvolution.cpp](C++/ParallelConvolution.cpp))

### Python

- Script to create a project and a repository to a certain BitBucket Cloud instance through BitBucket's REST API ([bitbucket_manager.py](Python/bitbucket_manager.py))
- Class decorator that can be used to develop a hybrid method (a method that can be used as static or instance method) effectively allowing method overloading in Python ([doublemethodtest.py](Python/doublemethodtest.py))
- Script that will search a folder's entire structure looking for duplicate files while providing an optional list of files (or extensions) and folders to ignore ([duplicateFinder.py](Python/duplicateFinder.py))
- Script to check if a local repository has more than one branch using the gitPython package ([checkIfMultipleBranches.py](Python/checkIfMultipleBranches.py))
- Script to commit and push to a remote repository using the gitPython package ([commitAndPushToRemote.py](Python/commitAndPushToRemote.py))
- Script to create a git respository and configure user name and user email using the gitPython package ([createRepositoryAndConfigure.py](Python/createRepositoryAndConfigure.py))
- Script to commit files to a local git repository using the gitPython package ([executeCommits.py](Python/executeCommits.py))
- Script to fetch a remote repository to a local git repository using the gitPython package ([fetchFromRemote.py](Python/fetchFromRemote.py))
- Script to pull and print information from local repository using the gitPython package ([pullRepositoryInfo.py](Python/pullRepositoryInfo.py))
- Script to pull info from different branches of a local repository using the gitPython package ([pullTagsAndBehind.py](Python/pullTagsAndBehind.py))
- Implementation of the Bisection method for root-finding of continuous functions ([bissection.py](Python/bissection.py))
- Implementation of Newton's Method (also called Newton-Raphson method) for root-finding of real-valued functions ([newton.py](Python/newton.py))
- Scripts to generated all possible states of a Tic-Tac-Toe game using:
  - Depth-first-search ([tictactoe_dfs.py](Python/tictactoe_dfs.py)); and
  - Min-max approach ([tictactoe_minmax.py](Python/tictactoe_minmax.py))
- Script to migrate Github issues between different repositories ([migrateIssuesGithub.py](Python/migrateIssuesGithub.py))
