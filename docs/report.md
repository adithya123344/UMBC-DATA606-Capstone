# Loan Default Prediction 


## 1. Title and Author

- **Project Title:** Loan Default Prediction 
- **Prepared for UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang**
- **Author Name:** Sai Adithya Reddy Alla
- **GitHub Profile:**
 https://github.com/adithya123344  
- **LinkedIn Profile:**
https://www.linkedin.com/in/adithya-reddy-91b477220/
- **Streamlit App:** https://loandefaultstatus.streamlit.app/



## 2. Background
- **What is it about?**
  - ⁤My project mainly focuses on using machine learning and data analytics to predict loan default of a customer. ⁤⁤Financial organisations, such as banks must analyze a customer's financial history, which includes credit score, income,intention,property status, employment status, and other factors, because they handle a large volume of loan applications. ⁤⁤I want to design a system that improves the speed and efficiency of repayment of loans while minimizing human bias in decision-making.
    
- **why is it matters?**
  - **⁤Loan default prediction is important for various reasons: ⁤**
   - Efficiency and Speed: By automating the loan default process, banks could significantly decrease the time it takes to make decisions, resulting in faster application processing.
   - Consistency and Fairness: When correctly trained and modified, predictive models can make more consistent and fair decisions than human examiners, lowering the risk of bias. ⁤
   - Risk Management: Financial organizations use loan default algorithms to reduce risk by identifying applicants who are more likely to default. ⁤⁤Effective prediction enables lenders to manage their portfolios and avoid lending to high-risk candidates. ⁤
   - Cost savings: Automation eliminates the need for human reviews, lowering operational expenses and decreasing errors or inconsistencies that may occur during human loan evaluations. ⁤
     
- **What are your research questions?**
  - What are the key factors that influence the default of a loan application?
  -  How accurately can a machine learning model predict loan default based on historical data?
  -  what are the challenges that will raise for predictions?
## 3. Data 

- Data sources: .https://www.kaggle.com/code/renjiabarai/loan-classification/input

- Data size: 2.23 MB

- Data shape:

  - Rows: 32586 
  - Columns: 13

- What does each row represent?
   - In this dataset, every row corresponds to an unique customer for a loan default and includes information about their financial history, loan request, and current loan status.
## Dataset Description

| Column Name            | Description                                                | Data Type   |
|------------------------|------------------------------------------------------------|-------------|
| `customer_id`           | Unique identifier for each customer                        | Float      |
| `customer_age`          | Age of the customer                                        | Integer    |
| `customer_income`       | Annual income of the customer                              | Object     |
| `home_ownership`        | Home ownership status (e.g., RENT, OWN, MORTGAGE)          | Object     |
| `employment_duration`   | Duration of employment in months                           | Float      |
| `loan_intent`           | Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL)   | Object     |
| `loan_grade`            | Grade assigned to the loan                                 | Object     |
| `loan_amnt`             | Loan amount requested                                      | Object     |
| `loan_int_rate`         | Interest rate of the loan                                  | Float      |
| `term_years`            | Loan term in years                                         | Integer    |
| `historical_default`    | Indicates if the customer has a history of default (Y/N)   | Object     |
| `cred_hist_length`      | Length of the customer's credit history in years           | Integer    |
| `Current_loan_status`   | Current status of the loan (DEFAULT, NO DEFAULT)           | Object     |

## Target Variable and Features
- **Target**:
  - `Current_loan_status` - The status of the loan, indicating whether the customer has defaulted or not.
- **Features**:
  - **Demographic Information**: `customer_age`, `home_ownership`, `employment_duration`
  - **Financial Information**: `customer_income`, `cred_hist_length`, `historical_default`
  - **Loan Information**: `loan_intent`, `loan_grade`, `loan_amnt`, `loan_int_rate`, `term_years`

## Project Outcome
#Machine learning models can be trained on this dataset to predict the following:
- Whether a customer can repay a loan.
- The probability of loan default based on the characteristics of the customer.

## Exploratory Data Analysis (EDA)
- **Cleaned the dataset by droping the null values and replacing some of the column null values with the mean values**
- **Normalised and label Encoded the object based columns and converted the datatype into Int So that prediction can be more accurate**
- **Dropped `customer_id` ,`index`,`historical default ` columns as they are not relevant**
- **Used Plotly.express for visualization**
 - In our Dataset,  customers took more Education loans compared to other
  
![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic1.png)
- Most of the customers tooks the loan are from renatal houses

![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic2.png)
- Highest loans are taken by 23 years old customers

![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic3.png)

- and Least loans for Home Improvement 

![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic4.png)
- More customer that has more defaults are from rental houses
  
![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic5.png)
- Medical Loans and Debt Consolidation loans have the most defaults

![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic6.png)
- Most of the loans taken by the cistomers are between age 23 to 30 years

![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/pic7.png)


## Model Training
- **The models used to predict the default status are** 
  - #### Random Forest Classifier
  - #### Logistic Regression
  - #### K Neighbor Classifier
  - #### Decision Tree Classifer
  - #### GaussianNB Classifier
  - #### Gradient Booster Classifier
  - #### XGB Classifer

- **Train vs test split = 80/20
- **Python packages to be used scikit-learn, Pandas,Numpy
- **The development environment used is JUPYTER NOTEBOOK ,VISUAL STUDIO CODE.

## Comparing all Models
![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/im1)
### XGB Classifier model has the highest accuracy of 91.75%
### Logistic Regression has the lowest accuracy of 67.83%
![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/im2)

## STREAMLIT WEB APP
![image](https://github.com/adithya123344/UMBC-DATA606-Capstone/blob/main/docs/images/im3)

## Future Use of Machine Learning in Loan Default Prediction!
**More Improvements**
- Enhanced Data Integration: Leveraging more diverse data sources, such as social media and transaction data, for a comprehensive borrower profile.
- Advanced Algorithms: Adoption of more sophisticated algorithms like deep learning to improve prediction accuracy.
- Real-Time Analysis: Implementation of real-time data processing to provide instant insights and decisions.
  
**Future Projects Can be implemented**
- Personalized Loan Products: Tailoring loan offerings based on predictive insights to better serve individual borrower needs.
- Fraud Detection: Using predictive models to identify and mitigate potential fraudulent activities in loan applications.
- Risk Management: Enhancing financial institutions' risk management frameworks by integrating predictive analytics.

## CONCLUSION
- Machine learning algorithms for loan default prediction can improve financial organizations' risk management. These accurate and scalable models detect high-risk borrowers, optimize lending methods, and reduce financial losses by using historical data and advanced predictive analytics.
-This study tested Logistic Regression, Random Forest, and XGBoost. The comparative analysis showed that [selected model, e.g., XGBoost] had the best precision-recall ratio, making it the ideal choice for real-world deployment.







  


  
