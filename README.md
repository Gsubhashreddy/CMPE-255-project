# CMPE-255-project

## Project Title:  Finding Donors for Charity

## Team members: 
#### Kaushal Karinaga Shetter Raju - kaushalkr27
#### Sai Subhash Chandra Reddy Gangireddygari - Gsubhashreddy
#### Abraham Mathew - abematt
#### Sarat Kumar Kaniti - sarat458

## Dataset:
#### We are using census income dataset from openML- https://www.openml.org/search?type=data&status=active&id=4535&sort=runs

## Description:
  * We're working with data from the United States Census Bureau's income survey from 1994. The challenge we're seeking to tackle with this dataset is identifying people who earn more than $50,000. Non-profit or charitable groups can benefit from this insight. Understanding an individual's income can assist a non-profit in determining how large of a donation to request, as well as whether or not to contact out in the first place.
  * While determining an individual's general income bracket directly from public sources can be challenging, we can deduce this figure from other publicly available data such as openML.
  * This data set has 14 features such as 'age','work class','education','occupation','income' and so on. Income will be our target label and remaining columns will be features of this dataset.
  * A preliminary investigation of the dataset will determine how many individuals fit into either group, and will tell us about the percentage of these individuals making more than $50,000.
  * The Individuals are grouped into two categories - 'greater than or equal to $50K' and 'less than $50k'.

## Potential Methods:
  * The dataset is first pre-processed, with all null values found and purged, as well as noise and redundant data omitted. This process can be augmented by visualization techniques such as plots and graphs.
  * These plots will enable data preparation such as weeding out noisy, incomplete data, identifying correlations etc. We must apply an effective feature selection strategy to find the most key aspects in order to build a model that accurately predicts individuals with more than $50k income who are likely to make a donation.
  * It is often good practice to perform some type of scaling on numerical features. Applying a scaling to the data does not change the shape of each feature's distribution, however, normalization ensures that each feature is treated equally when applying supervised learning. Typically, learning algorithms expect input to be numeric, which requires that non-numeric features (called categorical variables) be converted. One popular way to convert categorical variables is by using the one-hot encoding scheme. One-hot encoding creates a "dummy" variable for each possible category of each non-numeric feature.
  * Individuals earning more than $50K will be predicted in this section. As a result, we already have income as a feature. We'll use Supervised Learning Algorithms because we have a labelled dataset.
  * Some of the supervised learning models that are currently available in scikit-learn are :
    * Gaussian Naive Bayes (GaussianNB)
    * Decision Trees
    * Ensemble Methods (Bagging, AdaBoost, Random Forest, Gradient Boosting)
    * K-Nearest Neighbors (KNeighbors)
    * Stochastic Gradient Descent Classifier (SGDC)
    * Support Vector Machines (SVM)
    * Logistic Regression
* Depending on the Pre processing and exploratory data analysis , we will be choosing the 3 appropriate methods from the above.




