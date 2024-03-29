## Predicting Falcon 9 First Stage Launching for Cost-Efficient Lunches and Competitive Bidding

### Description

Create the prediction model whether the Falcon 9 first stage will land successfully or not. SpaceX offers Falcon 9 rocket launches on its website at a cost of 62 million dollars, which is significantly lower than the cost of other providers that charge upward of 165 million dollars per launch. The reason behind this is that SpaceX can reuse the first stage of the rocket. Hence, predicting the successful landing of the first stage is crucial as it helps determine the cost of a launch. This information can be used by other companies who want to bid against SpaceX for a rocket launch.

#### In this project, we using going to use the programmig language: Python , SQl and a few HTML for creating Dashborad. Jupyter notebook is mainly used and Python and HTML for Interactive Dashboard. 

### Table of Contents

◆ Data Collection</br>
◆ Data Wrangling</br>
◆ Exploratory Analysis Using SQL, Pandas and Matplotlib</br>
◆ Interactive Visual Analysis using Folium and Dashboard using Plotly Dash</br>
◆ Predictive Analysis(Classification)</br>

#### Data Collection
◆ Collect the data by using the <b>request.get()</b> function from the correct API.</br>
◆ Collect the data by webscrapiing using the <b>BeautifulSoup</b>

#### Data Wrangling 
◆ Exploratory Data Analysis (EDA) to find some patterns in the data and determine </br> 　what would be the label for training supervised models by using <b>Pandas and NumPy</b>

#### Exploratory Data Analysis
◆ EDA with <b>SQL, Pandas</B></br>
◆ EDA with <b>Data Visualization</b> using <b>matplotlib and seaborn </b> 

#### Interactive Visual Analysis
◆ Visualize the Map by using <b> Folium Map </b> to explore the locations and proximities of each launch site. </br>
◆ Create an Interactive Dashboard using <b> Ploty dash and html </b> to investigate the depending on factors</br>　 such as payload mass, orbit type, etc.

#### Predictive Analysis (Classification)
　From the previous analysis, we are now sure that which independent varaiable has what effects on the dependent variables <br>
 After extracting the required variables from the dataset, we normalize the data by using <b> StandardScalar and Preprossing </b> from <b> Sklearn </b> 
 we are going to split the train and test data by using <b> train_test_split() </b> function. Then, tune the following model and parameters for each by using <b> GridSearchCV()</b> function.</br>
 ◆ Logistic Regression </br>
 ◆ Support Vector Machine </br>
 ◆ Decision Tree And </br>
 ◆ K Nearest Neighbors </br>
 From each tuned model, we are going to find the<b> best_score_ ,Accurancy socre, and Confusion Matrix</b> <br>
 By investigating the highest best_score_ and accuracy score and also the confusion matrix. We will determine which <b> MODEL WORKS THE BEST </b> for the dataset and for further unseen unknown data.
 
