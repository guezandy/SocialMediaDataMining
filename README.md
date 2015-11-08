# SocialMediaDataMining

Clustering Technique for LinkedIn Data
Practical approach to Normalization, Natural Language Processing and Clustering


Clustering LinkedIn Data:
Clustering involves taking a collection of instances and grouping them into smaller collections according to values held within the instances. Clustering in LinkedIn can be powerful to understand complex connections like you may want to cluster your LinkedIn connections by geographic region to see which region has better economic opportunities. 
When implementing clustering we have to first tackle a number of problems. First of all even if the data you receive is nicely formatted by a nice API which is usually not the case it often takes more than a little bit of effort to get the data into a form that’s suitable for analysis. 
The problem with LinkedIn data is members are allowed to enter their professional information as free text, which results in a level of unavoidable variation. For example if you want to analyze the name of companies where people work there are variations in names of the same companies for example LinkedIn Corporation, LinkedIn Inc, or just LinkedIn. 

Normalizing LinkedIn Company Names: 
In this simple script we do a simple form of normalization by focusing on variations of commonly variable parts of the Companies name. For example companies often ending in LLC can often be written without the LLC component. 

BEFORE	AFTER
Company, Inc.	Company
Company, Inc	Company
Company, LLC	Company
Company, LLP	Company
Company LLC	Company
Company Inc.	Company
Company Inc	Company

This is a key concept. These substitutions were the main ones I found from parsing through the data but there exists others that you must find in your data set to really maximize the normalization. This is great and all but there are important run time considerations that need to be taken into account. 

Parameters for runtime analysis:
A.	N= number of connections
B.	M= number of companies a connection has worked for
C.	X = number of transformed testing
Run time is determined to be (MxN) * X which is o(n^2)! Although this is usually not a problem for Linkedin data because you have a fixed number of connections usually a low N value (Typically ranging from 50-500) you can be confident your application will run. A problem could present itself if you start increasing the number of transforms to account for each and every possible variation. Thousands of transforms can prove a huge runtime problem. 

The last thing this script does it print in a pretty table the frequency of the results of any companies that have more than 2 connections working at. 
 

The same normalization technique can be done for Job Titles. Job Titles are a little more complicated because instead of removing values that complicate the data set we’re going to approach it by changing all values into a defined constant. We’re going to use the same script above but with some changes. Instead of getting the “Company” name were going to parse through “Job Title” and edit those values to see which we can normalize. The script is as follows:
 

Here our normalization is as follows:
Before	After
Sr Title	Senior Title
Jr. Title	Junior Title
Jr Title	Junior Title
CEO (Anywhere in title)	Chief Executive Officer
COO	Chief Operating Officer
CTO	Chief Financial Officer
CFO	Chief Finance Officer
VP	Vice President

Normalization results are as follows:
 

After analyzing the results I became interested in the frequency of the distribution how many of my connections did some sort of engineering or otherwise.  The figure on the right shows the frequency of tokens (words within job titles) and prints the frequency of them. Another possibly interesting analysis. 


LinkedIn Clustering Algorithm: 
 
With the Data Normalization techniques complete lets focus on how we’re going to cluster these instances. This clustering technique will give us dynamic insights on your own professional network. 

	Using our domain knowledge of the domain of Job Title we can deduce that overlap in titles is important. The following script is designed to compare the actual words in the job title and comparing them with one another using Jaccard Distance and a threshold for commonality. 
	“The Jaccard index, also known as the Jaccard similarity coefficient (originally coined coefficient de communauté by Paul Jaccard), is a statistic used for comparing thesimilarity and diversity of sample sets. The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size of the intersection divided by the size of the union of the sample sets”

	Python provides a nltk (Natural Language Toolkit) Library that contains a number of natural language processing techniques. Importing: “from nltk.metrics.distance import jaccard_distance” we have access to a DISTANCE(string, string) method that will measure similarity between the 2 words. 

	In this analysis we will analyze which connections have similar job titles and cluster groups of people by their job title.

My procedure is as follows:
1.	Setup imports and define transforms:
 
2.	Go through all our connections and create an array of all the job titles
 
3.	Normalize all the job titles using our normalization technique above
 
4.	Compare each title (title1) with every other title (title2) and find their distances (Jaccard Distance analysis)
 
5.	The smaller the Jaccard distance the more similar they are. So if the distance is less than a certain threshold (Close enough) value (Preset to 0.5) we’ll accept title1 and title2 to be clustered. 
 
6.	FLATTENING: After running steps 1-5 you’ll find that the nltk isn’t the best, and creates a lot of clusters between “empty spaces” in job titles. A bunch of useless clusters are created. To remove these we do a little hack, we just loop through all the entries and remove all clusters that have titles less than 1 value in length. 
 
7.	Create an array of all connections that fit into the cluster
 
8.	Print results in a nice legible format



