import streamlit as st
import json
import requests as re

st.markdown("<h1 style='text-align: center; color: #bd1111;'>CREDIT CARD FRAUD DETECTION</h1>", unsafe_allow_html=True)

st.write(" ")

#st.title("Credit Card Fraud Detection Web App")

st.image("image3.jpg")

st.write("""
## What is Credit Card Fraud?
Credit card fraud is the act of using another person’s credit card to make purchases or request cash advances without the cardholder’s knowledge or consent. These criminals may obtain the card itself through physical theft, though increasingly fraudsters are leveraging digital means to steal the credit card number and accompanying personal information to make illicit transactions.

 There is some overlap between identity theft and credit card theft. In fact, credit card theft is one of the most common forms of identity theft. In such cases, a fraudster uses an individual’s personal information, which is often stolen as part of a cyberattack or data breach, to open a new account that the victim does not know about. This activity is considered both identity fraud and credit card fraud.
""")

# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("image2.png")
st.image("image.jpg")

st.write("""
## What is Credit Card Fraud Detection?
Credit card fraud detection is the collective term for the policies, tools, methodologies, and practices that credit card companies and financial institutions take to combat identity fraud and stop fraudulent transactions.  

In recent years, as the amount of data has exploded and the number of payment card transactions has skyrocketed, credit fraud detection has become largely digitized and automated.. Most modern solutions leverage artificial intelligence (AI) and machine learning (ML) to manage data analysis, predictive modeling, decision-making, fraud alerts and remediation activity that occur when individual instances of credit card fraud are detected.  
""")
st.write("""
**This Streamlit App utilizes a Machine Learning model served as an API in order to detect fraudulent credit card transactions based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.** 

The API was built with FastAPI and can be found [here.](https://myapi-5nix.onrender.com/)

""")


st.sidebar.header('Input Features of The Transaction')

sender_name = st.sidebar.text_input("""Input Sender ID""")
receiver_name = st.sidebar.text_input("""Input Receiver ID""")
step = st.sidebar.slider("""Number of Hours it took the Transaction to complete: """)
types = st.sidebar.subheader(f"""
                 Enter Type of Transfer Made:\n\n\n\n
                 0 for 'Cash In' Transaction\n 
                 1 for 'Cash Out' Transaction\n 
                 2 for 'Debit' Transaction\n
                 3 for 'Payment' Transaction\n  
                 4 for 'Transfer' Transaction\n""")
types = st.sidebar.selectbox("",(0,1,2,3,4))
x = ''
if types == 0:
    x = 'Cash in'
if types == 1:
    x = 'Cash Out'
if types == 2:
    x = 'Debit'
if types == 3:
    x = 'Payment'
if types == 4:
    x =  'Transfer'
    
amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("""Sender Balance Before Transaction was made""",min_value=0, max_value=110000)
newbalanceorg= st.sidebar.number_input("""Sender Balance After Transaction was made""",min_value=0, max_value=110000)
oldbalancedest= st.sidebar.number_input("""Recipient Balance Before Transaction was made""",min_value=0, max_value=110000)
newbalancedest= st.sidebar.number_input("""Recipient Balance After Transaction was made""",min_value=0, max_value=110000)
isflaggedfraud = 0
if amount >= 200000:
  isflaggedfraud = 1
else:
  isflaggedfraud = 0


if st.button("Detection Result"):
    values = {
    "step": step,
    "types": types,
    "amount": amount,
    "oldbalanceorig": oldbalanceorg,
    "newbalanceorig": newbalanceorg,
    "oldbalancedest": oldbalancedest,
    "newbalancedest": newbalancedest,
    "isflaggedfraud": isflaggedfraud
    }


    st.write(f"""### These are the transaction details:\n
    Sender ID: {sender_name}
    Receiver ID: {receiver_name}
    1. Number of Hours it took to complete: {step}\n
    2. Type of Transaction: {x}\n
    3. Amount Sent: {amount}$\n
    4. Sender Balance Before Transaction: {oldbalanceorg}$\n
    5. Sender Balance After Transaction: {newbalanceorg}$\n
    6. Recepient Balance Before Transaction: {oldbalancedest}$\n
    7. Recepient Balance After Transaction: {newbalancedest}$\n
    8. System Flag Fraud Status(Transaction amount greater than $200000): {isflaggedfraud}
                """)

    res = re.post(f"https://myapi-5nix.onrender.com/predict",json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    if sender_name=='' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        st.write(f"""### The '{x}' transaction that took place between {sender_name} and {receiver_name} is {resp[0]}.""")
