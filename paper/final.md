| Title        | Date           | Author |
| :-------------: |:-------------:| :-----:|
| Finding Donors for Charity | May 2022 | Team#7, Sarat Kumar Kaniti, Sai Subhash Chandra Reddy Gangireddygari, Kaushal Karinaga Shetter Raju, Abraham Mathew |

## Abstract
   #### The census is a unique, wide-ranging activity that occurs once every ten years across the country. The goal is to collect data on the general public in order to offer a complete and accurate image of the country's population, including housing conditions, demographic, social, and economic features. Age, gender, place of origin, marital status, housing conditions, marriage, education, and employment are among the data collected. The purpose of this machine learning research is to estimate whether or not a person earns more than $50,000 per year based on their demographics. Several classification strategies are investigated, with the Adaboost classification model providing the best prediction result.

## Introduction
   The income of the citizens has a significant impact on a country's economic well-being.
   
   Many business and public sector choices are dependent on Census data. The democratic form of governance relies heavily on census data, which has a significant impact on the economy. The government distributes federal cash to different states and localities using census-related data.
   
Not just for the reasons stated above, but also for post-census population estimates and predictions, economic and social scientific research, and a variety of other uses. As a result, the significance of this data and its accurate forecasts is obvious to us.
Many crucial judgments have always been based on data. When an assumption is supported by facts and figures, the odds of being wrong and making poor judgments are reduced.

We're using data from a 1994 income survey conducted by the US Census Bureau. With this dataset, we want to solve the problem of identifying persons who make more than $50,000. This information can be useful to non-profit or philanthropic organizations. Understanding an individual's income can assist a non-profit in determining how large of a donation to request, as well as whether or not to contact out in the first place.

### Dataset
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



