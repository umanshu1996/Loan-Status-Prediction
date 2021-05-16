import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('loan_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Education, ApplicantIncome,CoapplicantIncome, LoanAmount, Credit_History,Property_Area):   
 
    # Pre-processing user input    
    if Education == "Graduate":
        Education = 0
    else:
        Education = 1
 
    if Property_Area == "rural":
        Property_Area = 0
    elif Property_Area == "semiurban":
        Property_Area = 1
    else:
        Property_Area = 2
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Education, ApplicantIncome,CoapplicantIncome, LoanAmount, Credit_History,Property_Area]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("http://www.businessnewsdaily.com/images/i/000/010/326/original/business-loan.jpg?1450474727")
    }
   
    </style>
    """,
    unsafe_allow_html=True
)
    
    
      
    # following lines create boxes in which user can enter data required to make prediction 
    Education = st.selectbox('Education',("Graduate","Ungraduate"))
    Property_Area = st.selectbox('Property Area',("rural","semiurban","urban")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    CoapplicantIncome = st.number_input("Coapplicants monthly income")
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Education, ApplicantIncome,CoapplicantIncome, LoanAmount, Credit_History,Property_Area) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()