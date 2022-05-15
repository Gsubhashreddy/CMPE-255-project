## Introduction
    In this project, we are going to predict whether a person’s income is above 50k or below 50k using various features like age, education, and occupation. The dataset we are going to use is the adult census income dataset which contains about 32561 rows and 15 features.
Mentioned below are the details of the features provided to us, which we will be feeding to our classification model to train it.
    1. Age — The age of an individual, this ranges from 17 to 90.
    2. Workclass — The class of work to which an individual belongs.
    3. Fnlwgt — The weight assigned to the combination of features (an estimate of how many people belong to this set of combination)
    4. Education — Highest level of education
    5. Education_num — Number of years for which education was taken
    6. Marital_Status — Represents the category assigned on the basis of marriage status of a person
    7. Occupation — Profession of a person
    8. Relationship — Relation of the person in his family
    9. Race — Origin background of a person
    10. Sex — Gender of a person
    11. Capital_gain — Capital gained by a person
    12. Capital_loss — Loss of capital for a person
    13. Hours_per_week — Number of hours for which an individual works per week
    14. Native_Country — Country to which a person belongs
  Output:
     Income — The target variable, which predicts if the income is higher or lower than 50K$.



## Method 1: Random Forest Classifier
### Introduction:

  * Random forest is a Supervised learning algorithm that is used for both classification and regression. Since our project comes under classification, we thought this would be a great choice to start with.
  
  * It is a type of bagging ensemble algorithm, which creates multiple decision trees simultaneously trying to learn from the dataset independent of one another. The final prediction is selected using majority voting.
  
  * Random forests are very flexible and give high accuracy as it overcomes the problem of overfitting by combining the results of multiple decision trees. Even for large datasets, random forests give a good performance. 
  
  * They also give good accuracy if our dataset has many missing values. But random forests are more complex and computationally intensive than decision trees resulting in a time-consuming model building process. 
  
  * They are also harder to interpret and less intuitive than a decision tree.

    ![Alt text](https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/RandomForestClassifier.jpg "Random Forest Classifier")
  
  * This algorithm has some important parameters like max_depth, max_features, n_estimators, and min_sample_leaf. The number of trees which can be used to build the model is defined by n_estimators. 
  
  * Max_features determine the maximum number of features the random forest can use in an individual tree. The maximum depth of the decision trees is given by the parameter max_depth. The minimum number of samples required at a leaf node is given by min_sample_leaf.
 
### Model Evaluation:

 * In this step, we will evaluate our model using accuracy_score as a metric. Accuracy is the ratio of correct predicted values over the total predicted values. It tells us how accurate our prediction is.
 
 * **Hyperparameter Tuning**: We will tune the hyperparameters of our random forest classifier using RandomizedSearchCV which finds the best hyperparameters by searching randomly avoiding unnecessary computation. We will try to find the best values for ‘n_estimators’ and ‘max_depth’.

### Output:
 * This method gives an accuracy of 84.48 after tuning its hyperparameters. 
 
 * We have taken the classification report and it is as follows:   
 
   ![Alt text]( https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/RFC_Output.jpg "Random Forest Classifier")


## Method 2: 

## Method 3:

## Conclusion:

### AUC ROC curve:

 * AUC — ROC curve is a performance measurement for the classification problems at various threshold settings. ROC is a probability curve and AUC represents the degree or measure of separability. It tells how much the model is capable of distinguishing between classes. Higher the AUC, the better the model is at predicting 0’s as 0’s and 1’s as 1’s.
 
 * The area under the ROC curve represents the ability of our model to predict correct values, and the curve that we got is quite a good score.
 
 * A comparative study of the above models with respect to accuracy, precision, recall, ROC score is computed together for better decision.
 
 * From the table above, ada boost gives the best accuracy and ROC score.

   ![Alt text]( https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/Summary_Table.png "Random Forest Classifier")
   
 * All the ROC curvers are shown below
 
   ![Alt text]( https://github.com/kaushalkr27/CMPE-255-project/blob/main/images/ROC_Summary.png "Random Forest Classifier")

  * Ada boost covers the maximum area and hence is a better model.



 


