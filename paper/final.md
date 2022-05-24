| Title        | Date           | Author |
| :-------------: |:-------------:| :-----:|
| Finding Donors for Charity | May 2022 | Team#7, Sarat Kumar Kaniti, Sai Subhash Chandra Reddy Gangireddygari, Kaushal Karinaga Shetter Raju, Abraham Mathew |

## ABSTRACT
  The census is a unique, wide-ranging activity that occurs once every ten years across the country. The goal is to collect data on the general public in order to offer a complete and accurate image of the country's population, including housing conditions, demographic, social, and economic features. Age, gender, place of origin, marital status, housing conditions, marriage, education, and employment are among the data collected. The purpose of this machine learning research is to estimate whether or not a person earns more than $50,000 per year based on their demographics. Several classification strategies are investigated, with the Adaboost classification model providing the best prediction result.

## INTRODUCTION
   The income of the citizens has a significant impact on a country's economic well-being. Many business and public sector choices are dependent on Census data. The democratic form of governance relies heavily on census data, which has a significant impact on the economy. The government distributes federal cash to different states and localities using census-related data. Not just for the reasons stated above, but also for post-census population estimates and predictions, economic and social scientific research, and a variety of other uses. As a result, the significance of this data and its accurate forecasts is obvious to us. Many crucial judgments have always been based on data. When an assumption is supported by facts and figures, the odds of being wrong and making poor judgments are reduced.

   We're using data from a 1994 income survey conducted by the US Census Bureau. With this dataset, we want to solve the problem of identifying persons who make more than $50,000. This information can be useful to non-profit or philanthropic organizations. Understanding an individual's income can assist a non-profit in determining how large of a donation to request, as well as whether or not to contact out in the first place.

### A. Dataset
   We are using census income dataset from openML- https://www.openml.org/search?type=data&status=active&id=4535&sort=runs . The data is collected by the United States Census Bureau's income survey. It contains about 32561 rows and 15 features.
 
 | Feature Name        | Type           | Decsription |
| :-------------: |:-------------:| :-----:|
|Age |	Numerical|	The age of an individual, this ranges from 17 to 90.|
|Workclass	|Categorical	|The class of work to which an individual belongs.|
|Fnlwgt	|Numerical	|The weight assigned to the combination of features (an estimate of how many people belong to this set of combination)|
|Education	|Categorical	|Highest level of education|
|Education_num|	Numerical|	Number of years for which education was taken|
|Marital_Status|	Categorical|	Represents the category assigned on the basis of marriage status of a person|
|Occupation	|Categorical	|Profession of a person|
|Relationship|	Categorical|	Relation of the person in his family|
|Race|	Categorical|	Origin background of a person|
|Sex|	Categorical	|Gender of a person|
|Capital_gain|	Numerical|	Capital gained by a person|
|Capital_loss|	Numerical|	Loss of capital for a person|
|Hours_per_week|	Numerical	|Number of hours for which an individual works per week|
|Native_Country	|Categorical|	Country to which a person belongs|
|Income	|Numerical|	Income| 

### B.	Exploratory Data Analysis
#### Data Preprocessing
* We import necessary libraries for the current project. Importing refers to allowing a Python file or a Python module to access the script from another Python file or module. We can only use functions and properties our program can access.
* All the standard libraries like numpy, pandas, matplotlib, and seaborn are imported in this step. We use numpy for linear algebra operations, pandas for using data frames, matplotlib, and seaborn for plotting graphs. The dataset is imported using the pandas command read_csv()
* We use the describe method to check for the description of the dataframe. The describe() method returns description of the data in the Data Frame. If the Data Frame contains numerical data, the description contains this information for each column: count - The number of not-empty values. mean - The average (mean) value.
* Now, to check the first 5 rows of the data frame we use df.head()
* We draw a correlation matrix to check the correlation between each pair of variables. This helps us in further analyzing which features are important, and which are not.
* From the correlation heatmap, we can see that the dependent feature ‘income’ is highly correlated with age, numbers of years of education, capital gain, and the number of hours per week. 
* From the correlation matrix, we observe that income has 34% correlation with ‘Education_num’, 23% correlation with ‘hours_per_week’ and ‘age’, and 22% correlation with ‘Capital_gain’. The correlations are moderate.

#### Cleaning Data
*	We have the missing Values in our data set for the columns workclass, occupation and native_country. So instead of removing the rows with missing values we are going to replace them, with the mean/mode. Hence, we replace ‘?’ is ‘Workclass’ column by ‘Private’, ‘Occupation’ column by ‘Prof-speciality’ and ‘Native_country’ by ‘United_States’.
*	We logically combined the data to reduce the number of categories in the features.
*	We can keep Never-worked and Without-pay into one category. Also Group State-gov, Local-gov into Government. Add Self-emp-not-inc into ‘Private’ category We combine all the columns relevant to schools in ‘School’ category, Let’s keep ‘Doctorate’ and ‘Prof school’ in a single category ‘Doctorate’, ‘Assoc-acdm’ and ‘Assoc-voc’ in one category ‘Assoc’, and ‘HS-Grad’ and ‘Some-college’ in one category ‘College’.
*	Marital status: We combine ‘Divorced’, ‘Married-spouse-absent’, ‘Separated’, ‘Widowed’ and ‘Married-AF-Spouse’ to one category and name it as ‘No spouse’.
*	Relationship Column: We combine ‘Not-in-family’, ‘Own-child’, ‘Unmarried’ and ‘Other-relative’ columns to a single category looking at the distributions, and name is as ‘Other’.
*	Race column :We combine the categories ‘Amer-Indian-Eskimo’ and ‘Other’ to ‘Others’ category, since they have similar distributions.
*	We used label encoder to normalize the labels and to transform categorical columns to numerical. Since majority of the classification models need input as ‘int/float’, and do not work on ‘string’ data, we encode our categorical columns using ‘Label Encoder’

#### Scaling Data
*	The next step is to bring the data to a common scale, since there are certain columns with very small values and some columns with high values. This process is important as values on a similar scale allow the model to learn better.
*	We use standard scaler for this process .
*	StandardScaler follows Standard Normal Distribution (SND). Therefore, it makes mean = 0 and scales the data to unit variance.

#### Data Visualizations
### Age Column
*	We checked for null values in the age column and found that it has no null values in it. Distplot here is used to visualize the parametric distribution of the age variable.
*	Our data has a right skewness, with most of the ages lying between 20 and 50. As people get older, the number continues to decrease.
*	In this dataset, the greatest number of people are young, white, male, high school graduates with 9 to 10 years of education, and work 40 hours per week.
 ![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/Age.png "Age Distribution Plot")

 ### Workclass column
*	We used value_counts() function to get a series containing counts of unique values in work class column.
*	We used seaborn. countplot() method  to show the counts of observations in each categorical bin using bars.
*	When we look at the unique values for workclass, we notice that there are seven different sorts of values, as well as some missing values denoted by a '?'. Null values account for 1836, or around 5% of the data.
*	We see that most people work in the 'Private' sector. We also notice something intriguing here: the values that are lacking 'Workclass' are also missing 'Occupation'.


![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/work%20class.png "Work Class Plot")

### Education Column
* we checked for its unique values and found that there are 16 different categories in the 'Education' column. 
* Most of these categories fall within the 'School' category (different classes are divided into multiple categories). 
* There are no missing values in this column, and most persons have a 'HS-grad' education level, followed by 'Some-college' and 'Bachelors'.

![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/education_level.png "Education Level Plot")

### From Now, Let's see all the features against the target column which is Income
### Race vs Income
* In this count plot, we realize that the Whites are large in number in the category of >50K while others being the least. 
* Asians and Blacks have nearly equal population in this category whereas American Indian eskimos dont have any people in >50k income category


![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/race_vs_inc.png "Race Vs Income Plot")

### Work class vs Income
* We found that people of private sector have a lot of population >50K. Ratio of people earning more than 50K is higher in case Workclass is ‘Self-emp-inc’.

![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/work_class_vs_inc.png "WorkClass Vs Income Plot")

### Education level vs Income
* People with bachelor’s degree have the highest income (>50K) and people with HS-grad have the highest income (<=50K). 
* People with education level as ‘Masters/Doctorate/Prof-school’ have higher ratios of >50K earning, than <=50K. Bachelors degree also has around 10:7 ratio of <=50K : >50K.

![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/eduLev_vs_inc.png "EducationLevel Vs Income Plot")

### Relationship vs Income
* Husband earns the most when compared to other relationships.
* Based on the scatterplot of age, hours per week, and income, we can see that to make more than 50K(Dollars), a person must be at least 30 years old, or he/she should work at least 60 hours per week.

![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/rel_vs_inc.png "RelationshipLevel Vs Income Plot")

## C. Analysis from EDA
* If a person's race is 'White'/'Asian-pac-islander,' he or she has a good likelihood of earning more than 50K(Dollars).
* Males are more likely than females to earn more than 50K(Dollars).* * 
* Number of People earning more than 50K is high in private sector when compared to Others. If Workclass is 'Self-emp-inc,' the percentage of those earning more than 50K(Dollars) is greater.
* People with a 'Masters/Doctorate/Prof-school' education have a larger ratio of >50K earning than those with a '=50K' education. The ratio of =50K: >50K for bachelor's degrees is roughly 10:7.
* If the relationship status is 'Husband/Wife,' the odds of earning more than 50K(Dollars) are considerable.
* Based on the scatterplot of age, hours per week, and income, we can see that to make more than 50K(Dollars), a person must be at least 30 years old or he/she should work at least 60 hours per week.

### D.	Feature Selection
*	The curse of multicollinearity and the problem of overfitting can be solved by performing Feature Selection. The feature importances can be easily found by using the ExtraTreesClassifier.
*	We found that some features are least important and contribute nothing to prediction. As a result, we dropped all of them.
### E.	Oversampling:
*	The dependent feature ‘Income’ is highly imbalanced as 75.92% values have income less than 50k and 24.08% values have income more than 50k. This needs to be fixed as it results in a low F1 score. As we have a small dataset we can perform Oversampling using a technique like RandomOverSampler.
### F.	Methods for fitting data into classification Models:
*	The dataset is then split into X which contains all the independent features and Y which contains the dependent feature ‘Income’
*	We split our dataset into train and test sets to evaluate how well our machine learning model performs. The train set is used to fit the model, the statistics of the train set are known. The second set is called the test data set, this set is solely used for predictions.
*	Here we are splitting the training and the testing data sets in the ratio of 80:20

## METHODS
### Random Forest Classifier
   Random forest is a Supervised learning algorithm that is used for both classification and regression. Since our project comes under classification, we thought this would be a great choice to start with. It is a type of bagging ensemble algorithm, which creates multiple decision trees simultaneously trying to learn from the dataset independent of one another. The final prediction is selected using majority voting.
  
  Random forests are very flexible and give high accuracy as it overcomes the problem of overfitting by combining the results of multiple decision trees. Even for large datasets, random forests give a good performance. They also give good accuracy if our dataset has many missing values. But random forests are more complex and computationally intensive than decision trees resulting in a time-consuming model building process. They are also harder to interpret and less intuitive than a decision tree.
  
 ![Alt-text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/RandomForestClassifier.jpg)
  
  This algorithm has some important parameters like max_depth, max_features, n_estimators, and min_sample_leaf. The number of trees which can be used to build the model is defined by n_estimators. Max_features determine the maximum number of features the random forest can use in an individual tree. The maximum depth of the decision trees is given by the parameter max_depth. The minimum number of samples required at a leaf node is given by min_sample_leaf.
#### Model Evaluation:
  In this step, we will evaluate our model using accuracy_score as a metric. Accuracy is the ratio of correct predicted values over the total predicted values. It tells us how accurate our prediction is. We will tune the hyperparameters of our random forest classifier using RandomizedSearchCV which finds the best hyperparameters by searching randomly avoiding unnecessary computation. We will try to find the best values for ‘n_estimators’ and ‘max_depth’. This method gives an accuracy of ***84.48*** after tuning its hyperparameters. We have taken the classification report and it is as follows:

![Alt-text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/randomclassification_report.png)
 
### Logistic Regression
  Logistic regression is a classification algorithm, used when the value of the target variable is categorical in nature. Logistic regression is most commonly used when the data in question has binary output, so when it belongs to one class or another, or is either a 0 or 1. Classification tasks have discrete categories, unlike regressions tasks. Here, by the idea of using a regression model to solve the classification problem, we rationally raise a question of whether we can draw a hypothesis function to fit to the binary dataset. The answer is that we will have to use a type of function, different from linear functions,  called a logistic function, or a sigmoid function.
  
  The sigmoid function/logistic function is a function that resembles an “S” shaped curve when plotted on a graph. It takes values between 0 and 1 and “squishes” them towards the margins at the top and bottom, labeling them as 0 or 1.The goal of classification with the dataset it to predict whether or not an income is likely to be greater than or less than or equal to 50k. There are only two categories this makes the classification task perfect for logistic regression.
  
 #### Model Evaluation:
  Now that we have prepped the data, we can feed it into the logistic regression classifier. First, we imported the logistic regression algorithm from Scikit-learn. Now we created an instance of the classifier and fit it to the training data. We created the predictions by running the classifier on the test dataset.
  Finally, we checked to see how the classifier performed by importing some metrics and checking the predicted values against the actual values. This model is evaluated based on its accuracy score. The accuracy of this model is ***83.86***. We have taken the classification and it is as follows.
  
![Alt-text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/logistic_regression.png)



## COMPARISONS

## CONCLUSION

