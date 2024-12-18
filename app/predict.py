import streamlit as st
import pickle
import numpy as np
back="""
<style>
[data-testid='stAPPViewContainer]{
background-image:url("bank.jpeg");
background-size:cover;
}
.st-key-red button{
    background-color:red;
}
</style>
"""
st.markdown(back,unsafe_allow_html=True)


def loading_model():
    with open('app/saved_model.pkl','rb') as file:
        load_model=pickle.load(file)
    return load_model

data=loading_model()




def show_predict():
    st.title("LOAN DEFAULT PREDICTION")
    st.write("""### *Fill out the form to predict your default status*""")

show_predict()
st.sidebar.write("""#### Click on pictures for more Details""")
st.sidebar.markdown(
    """
    <a href='https://money.howstuffworks.com/personal-finance/debt-management/personal-loan-mistakes.htm' target='_blank'>
        <img src='https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL2xvYW4tcGVyc29uYWwuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo4Mjh9LCJ0b0Zvcm1hdCI6ImF2aWYifX0=' width='500'>
    </a>
    Taking Out a Personal Loan? Some Mistakes to Avoid
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <a href='https://www.iifl.com/blogs/business-loan/what-happens-when-you-default-on-loan-payments' target='_blank'>
        <img src='data:image/png;base64,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' width='500'>
    </a>
    What Happens When You Default On Loan Payments?
    """,
    unsafe_allow_html=True
)

house_ownership=['RENT','OWN','MORTGAGE','OTHER']
loan_intent=['EDUCATION','MEDICAL','PERSONAL','DEBTCONSOLIDATION','HOMEIMPROVEMENT']
loan_grade=['A','B','C','D','E']

loanamount=st.number_input("Enter the Loan Amount", min_value=1000, max_value=100000, value=10000,)
income = st.number_input("Enter your Income", min_value=0, max_value=1000000, value=5000)
intrest=st.number_input("Enter the Intrest Rate",min_value=0.0,max_value=30.0, value=0.0)
HouseOwnership=st.selectbox("House Ownership",house_ownership)
loanintent=st.selectbox("Intent of the Loan",loan_intent)
grade=st.selectbox("Grade",loan_grade)
employment=st.slider("Employment Duration",0,50,1)
term=st.slider("Loan Term Years",0,20,2)
credithistory=st.number_input("Enter credit history length",min_value=0,max_value=50, value=0)
house_ownership_dict = {"RENT": 0, "OWN": 1, "MORTGAGE": 2,"OTHER":3}
loan_intent_dict = {"EDUCATION": 0, "MEDICAL": 1, "PERSONAL": 2, "DEBTCONSOLIDATION": 3, "HOMEIMPROVEMENT": 4}
grade_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}




HouseOwnership = house_ownership_dict[HouseOwnership]

loanintent = loan_intent_dict[loanintent]
grade = grade_dict[grade]

result=st.button('Predict the Status',key="red")
st.subheader("Prediction Results")
if result:
    x=np.array([[income,HouseOwnership,employment,loanintent,grade,loanamount,intrest,term,credithistory]])
    x=x.astype(float)

    status=data.predict(x)
    if status==0:
        st.success("This loan is unlikely to default.")
    else:
        st.error("This loan is likely to default.")
