# Team Name: Un1fy
Members:
- Gautam Jethwani

## Patient Matching

## Set up instructions
1. Download all required libraries using the following commands
    ```
    pip install numpy
    pip install keras
    pip install editdistance
    ```
    as well as any other missing libraries that may be flagged as compile time errors
2. Replace `data.csv` with the desired training data. The current `data.csv` has the sample data given for the challenge. IMPORTANT: this file name is hardcoded so it has to be named `data.csv`. 
3. Place the input data in a file called `input.csv` with the patient data you would like to group. This is the unclassified input data. IMPORTANT: this file name is also hardcoded so it has to be named `input.csv`. 

## Proof of Concept Steps
1. To parse the input file, run `python3 prepare.py`. This generates a file called `nn.csv`
2. To train the neural network using `nn.csv`, run `python3 nn.py`
3. To feed data from `input.csv` to the trained network and group patients, run `python3 predict.py`. This should spit out a file called `result.txt` with each line being a group. It will be formatted like this: `{group_id}: {array of patient IDs}`

## Contact info
gdjethwa@usc.edu
Devpost submission: https://devpost.com/software/un1fy