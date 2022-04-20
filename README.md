# CMPE-255-project

## Team members: 
###### Kaushal Karinaga Shetter Raju - kaushalkr27
###### Sai Subhash Chandra Reddy Gangireddygari - Gsubhashreddy
###### Abraham Mathew - abematt
###### Sarat Kumar Kaniti - sarat458

## Data:
###### We are using a 120 years dataset from Kaggle - https://www.kaggle.com/code/duttadebadri/analysing-the-olympics-for-last-120-yrs/data?select=athlete_events.csv

## Description:
###### After considerable analysis into a number of datasets, 120 Years of Olympic Games is being examined for representation. Its dataset has a range of benefits, including the fact that it is a large-scale dataset that spans the years 1896 to 2016. Last but not least, the Olympic Games dataset is seen to be worthwhile analysing in terms of visual representation and user experience.  A data set from Kaggle was chosen to solve the main question, which consists of two unique tables, athlete events, and event regions.
###### The problems being solved can be a multitude of problems.  Which countries are the most dominant? How has involvement evolved? Which countries have the most medals in various disciplines? What is the ratio of female/male Olympic attendees?. What factors of an athlete influence the success rate of a country.

## Potential Methods:
###### The dataset is first pre-processed, with all null values found and purged, as well as noise and redundant data omitted. This process can be augmented by visualization techniques such as plots and graphs. These plots will enable data preparation such as weeding out noisy, incomplete data, identifying correlations etc. We must apply an effective feature selection strategy to find the most key aspects in order to build a model that accurately predicts medal performance in the coming Olympic games. The embedded feature selection model will use the package that includes the wrapper function rfcv() to pretrain a Random Forest and omit the least important variables in order to employ the most suited strategy. This will assist make the decision tree more relevant and based on the target variables in the long run. This will help speed up the computing process. Random Forest Classification was used to train the dataset since it is a simple way to measure the relative relevance of each feature on the prediction. When a node is split, the best feature from a random group of features is found, resulting in an improved model than when a model selects the most relevant feature.




