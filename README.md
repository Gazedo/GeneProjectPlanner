##Ball Python breeding Calculator
###Goal Create a modular software suite that has a variety of priorities.
1. Predict outcomes of a pairing
2.	Use predicts to calculate backwards from target animal to choose possible paths to take
3.	Automatically choose best path from knowledge of current collection based on least time
4.	Update path based on current state (age/weight/eating habits) of collection
5.	Browser based UI with backend to be hosted on web server (local or remote)

###Modules
#####Main
Deals with overall decisions and interacts with GUI

#####Database
Stores information of genes.

-	Name
-	Dominance
-	Description

Split Banana into banana-male and banana-female

Able to update with additions or deletions. Possibly stored with mysql or a simple text file read into a dictionary at start up.

#####Predictor
Handles the pairing calculations. Uses Matrices to calculate percentages of pairings based on parents. Can also work from children to show all possible parent pairings to produce that animal. Should show 2 per possibility, male gene A with female gene B and male gene B with female gene A in order to check against some special characteristics.

-	Detect if being run as a function or stand alone
-	Function, grab the inputs or ask for them
-	Double check inputs are in matrix form, if not put them in
-	return result

In order to calculate the result the program has to understand how the genes interact.

#####Current Collection
A database or an imported csv with gene names, physical status of animal and sex

#####Planner
Takes current collection information and calculates possible paths to a specific animal.

#####Plan updater
This module compares to current collection. Saves complete plan with all possibilities and current state of the plan. It will also interact with saved plans to update them based on newly born animals, unexpected purchases, deaths, or weight changes (allows to remove an animal from the plan temporarily and recalculate)

###Project plan
#####Milestone 1
* Go over software ideas with Billie for feedback
* Research various databases and choose backend along with verify that Python is an appropriate language to use for this* Establish test database and use it to test the Predictor module against for pairing

#####Milestone 2
* Implement planner by itself working from various start points, including partial database and full + Check that it fails gracefully by notifying of failed calculation and asking for instructions or new gene

#####Milestone 3
* Implement the Current Collection Database with Plan Updater

#####Milestone 4
* Design and implement browser based gui

#####Milestone 5
* Decide on marketing path

###Possible Issues
Male/Female issue with planner gayness.

-	IE Generation 1 pair produces all female of required gene, cannot pair back to mother.

Check if Predictor needs to be aware of genders

Check for Gene interaction
