# Loan Repayment Prediction 


## 1. Title and Author

- **Project Title:** Loan Repayment Prediction 
- **Prepared for UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang**
- **Author Name:** Sai Adithya Reddy Alla
- **GitHub Profile:**
 https://github.com/adithya123344  
- **LinkedIn Profile:**
https://www.linkedin.com/in/adithya-reddy-91b477220/ 



## 2. Background
- **What is it about?**
  - ⁤My project mainly focuses on using machine learning and data analytics to predict loan repayment of a customer. ⁤⁤Financial organisations, such as banks must analyze a customer's financial history, which includes credit score, income,intention,property status, employment status, and other factors, because they handle a large volume of loan applications. ⁤⁤I want to design a system that improves the speed and efficiency of repayment of loans while minimizing human bias in decision-making.
    
- **why is it matters?**
  - **⁤Loan repayment prediction is important for various reasons: ⁤**
   - Efficiency and Speed: By automating the loan repayment process, banks could significantly decrease the time it takes to make decisions, resulting in faster application processing.
   - Consistency and Fairness: When correctly trained and modified, predictive models can make more consistent and fair decisions than human examiners, lowering the risk of bias. ⁤
   - Risk Management: Financial organizations use loan repayment algorithms to reduce risk by identifying applicants who are more likely to default. ⁤⁤Effective prediction enables lenders to manage their portfolios and avoid lending to high-risk candidates. ⁤
   - Cost savings: Automation eliminates the need for human reviews, lowering operational expenses and decreasing errors or inconsistencies that may occur during human loan evaluations. ⁤
     
- **What are your research questions?**
  - What are the key factors that influence the repaymentof a loan application?
  -  How accurately can a machine learning model predict loan repayment based on historical data?
  -  what are the challenges that will raise for predictions?
## 3. Data 

- Data sources: .https://www.kaggle.com/code/renjiabarai/loan-classification/input

- Data size: 2.23 MB

- Data shape:

  - Rows: 32586 
  - Columns: 13

- What does each row represent?
   - In this dataset, every row corresponds to an unique customer who is applying for a loan and includes information about their financial history, loan request, and current loan status.
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


  
