# PuzzlePal

Do you play `Connections`, the popular word puzzle in the `New York Times`?
If so, have you ever wished that instead of a shuffle, you could do a sort?
That is, drag and drop the cells until you see patterns.

You could write the words out on PostIts, or you could code up a widget to help out.
I chose the latter, mostly because I needed practice in Python.
I also wanted to explore cross platform GUIs.
Everytime I felt one of my tools at work needed GUI, I never really had time to learn how to make one.
I finally got a break from my work schedule, and roughed out this very basic tool.

# To Build and Run

## Pre-requisites

>_I didn't record what I did at the time, so I forget which libraries I had to install._
_I will eventually make a clean environment and walk through this again, logging all actions._

- Python 3.9

## Building
Python is an interpreted language, so there is no need for a build phase.
Actually, I just checked and there is some just in time processing of the code before execution, so maybe [Python is a compiled language](https://eddieantonio.ca/blog/2023/10/25/python-is-a-compiled-language/).

## Running

1. Start playing [NYT Connections](https://www.nytimes.com/games/connections) in your browser.
1. Take a screen capture of the 4x4 grid to a file.
1. Open a terminal
1. Run `connections-splitter.py`
1. ```bash
   (base) alexodonnell@Alexs-MBP ~ % python3 ./Projects/GitHub/PuzzlePal/code/connections-splitter.py
   ```
1. Use the file selector to open screen capture
1. You may now drag and drop tiles OR use the shuffle button
   - Drag and drop does not yet have animation or coloration to help, trust that it will swap the source and destination
   - Shuffle will randomize the tile order
   - The grid is broken into 16 tiles, each 1/4 of the height and width of the original capture rather than smart border detection.
  
# Known issues

- No visual feedback of a selected tile
- No visual feedback for dragging
- Tile split is based on quartering height and width, not line detection.
