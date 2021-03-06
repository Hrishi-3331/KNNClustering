# Enemy  Localization considering Error in Angle detection using clustering Algorithms

>Nikhil Gaikwad<br />
 Hrishikesh Ugale<br />
_Visvesvaraya National Institute of Technology, Nagpur_

## Simulation of KNN Clustering for Localization

### Instructions for creating Simulation Environment

1. Install Python 3.7.0 and pip 18.0 in your PC.
2. Clone the repository to directory of your PC.

>_Users may also prefer to create a virtual environment to run simulator_

### Instructions to use simulator:

1. Run the main.py file
1. Terminal will ask for following inputs:
    1. Number of Soldiers
    1. Number of Enemies
    1. Number of frames to be analyzed.
1. After entering above inputs hit enter. Wait for terminal to display "Simulation complete"
1. In plots directory, open MapX.html in browser to view results. MapX denotes results for Xth frame. For example Map0.html shows localization results for 0th frame, Map1.html for 1st frame and so on. Open only those many maps as you have entered as input to number of frames to be analyzed.


>_Location of Battlefield used in Simulation:_<br />
VNIT Sports Ground <br />
Latitude: 21.1288441<br />
Longitude: 79.0535207<br />

## Simulator Details:

#### Red dots - Soldier Locations
#### Black dots - True enemy locations
#### Blue Circles - Localization results for that frame.

![Readme Doc KNN](https://user-images.githubusercontent.com/43084197/79428925-79259a80-7fe4-11ea-95bc-11b08a1fdab9.png)