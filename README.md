# Election_Analysis 


## Project Overview

Tom, a Colorado Board of Elections employee requested my help in completing an election audit of a recent local congressional election, and asked for me to complete the following tasks:

	1. Calculate the total number of votes cast. 
	2. Get a complete list of candidates who received votes. 
	3. Calculate the total number of votes each candidate received. 
	4. Calculate the percentage of votes each candidate won. 
	5. Determine the winner of the election based on popular vote. 

## Resources

**Data Source:** election_results.csv

**Software:** Python 3.9.7, Visual Studio Code 1.63.2

## Summary

The results of the election analysis are as follows:
* There were a toal of **369,711** votes cast in the election.
* The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
* The candidate results were:
	- Charles Casper Stockham received **_23.0%_** of the vote and _85,213_ number of votes.
	- Diana DeGette received **_73.8%_** of the vote and _272,892_ number of votes.
	- Raymon Anthony Doane received **_3.1%_** of the vote and _11,606_ number of votes.
  
         The **winner** of the election was:

    **Diana DeGette**, who received **272,892** number of votes, **73.8%** of the total votes cast in the election.
    
## Challenge Overview

The Colorado Board of Elections then requested further help regarding the election audit, and asked for me to write a script that would compile the following information:

	-The voter turnout for each county
	-The percentage of votes from each county out of the total count
	-The county with the highest turnout

## Challenge Audit Results

The results of the challenge analysis were as follows:
* **Jefferson County**
	- **_10.5%_** of the overall vote
	- **_38,855_** total votes
* **Denver County**
	- **_82.8%_** of the overall vote
	- **_306,055_** total votes
* **Arapahoe County**
	- **_6.7%_** of the overall vote
	- **_11,606_** total votes
* **_Denver County_** had the largest turnout

## Challenge Summary
	
The code that I helped write for this challenge is easily applied to any of the election board's local, regional, or even state races that they oversee or are involved with. For example, the code can be re-written to replace the word "county" in the analysis returned with any applicable sub-region in an election, i.e. city ward for a mayoral election, specific areas for a school board election, etc. It could also easily be applied to federal elections in a similar manner. 
