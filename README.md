# Zomato-Restaurant-Recommendation-System
Introduction:

This is a minor project based on "Recommendation Systems".Recommender systems are the systems that are designed to recommend things to the user based on many different factors. Companies like Netflix, Amazon, etc. use recommender systems to help their users to identify the correct product or movies for them. 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Keywords:<br/>

#Data Preprocessing<br/>
#Text Preprocessing<br/>
#Content Based Filtering<br/>
#Tf-idf Vectorization<br/>
#Cosine Similarity

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dataset Description:<br/>

The dataset used for analyzing is the "Zomato Restaurant Dataset" of Bangalore taken from Kaggle.The link for the dataset is https://www.kaggle.com/himanshupoddar/zomato-bangalore-restaurants?select=zomato.csv .<br/>
It consists of about 51717 rows and 17 columns. After preprocessing,the columns were reduced to 14 and then final recommendation makes use of only 4 columns.
Some important features of the dataset are :<br/>
 name :name of the restaurant<br/>
 cuisines: cuisines offered by the restaurant<br/>
 rate:contains the overall rating of the restaurant out of 5<br/>
 mean rating: average rating of the restaurant<br/>
 cost: cost of various dishes offered by the restaurant 
 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Important Libraries and Modules:<br/>

Numpy<br/>
Pandas<br/>
sklearn<br/>
seaborn<br/>
matplotlib.pyplot

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Functionality:</br>

Input:User will input a restaurant name.<br/>
Output:10 similar kinds of restaurants to the one entered by the user.<br/>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Methodolgy:<br/>

The reviews column is majorly used for coming up with the recommendation.Firstly,the important words,after removing the stop words , are converted into vectors. This process is known af Tf-idf(Term frequency-Inverse Document Frequency) Vectorization. Then , cosine similarity function is used to calculate the extent of similarity between these vectors.The more the value of cosine similarity,the more similar the reviews are. Thus, restaurants having similar kinds of reviews are recommended by the machine as the final output.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
