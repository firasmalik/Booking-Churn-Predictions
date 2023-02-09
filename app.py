
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('clf.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'

#Streamlit ui






def prediction(no_of_adults ,no_of_children,no_of_weekend_nights,no_of_week_nights,

    required_car_parking_space,
    lead_time,
    
    arrival_year,
    arrival_month,
    arrival_date,
    
    market_segment_type,
    repeated_guest,
    
    no_of_previous_cancellations,
    no_of_previous_bookings_not_canceled,
    
    avg_price_per_room,
    no_of_special_req):
   
    prediction = classifier.predict(
    [[
    no_of_adults,
    no_of_children,

    no_of_weekend_nights,
    no_of_week_nights,

    required_car_parking_space,
    lead_time,
    
    arrival_year,
    arrival_month,
    arrival_date,
    
    market_segment_type,
    repeated_guest,
    
    no_of_previous_cancellations,
    no_of_previous_bookings_not_canceled,
    
    avg_price_per_room,
    no_of_special_req
    ]]
    )

        
    status=""

    if prediction==1:
        status+="Cancel"
    elif prediction==0:
        status+="Not Cancel"
    print(status)
    return status


  
# this is the main function in which we define our webpage
def main():
      # giving the webpage a title
    
    
      
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">ML powered Hotel bookings app
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.title("Hotel Customer Cancelation")
    st.write(""" Predict the cancellation of hotel bookings """)
    # this line allows us to display the front end aspects we have
    # defined in the above code
    
      
    no_of_adults= st.slider('No of Adults')
    no_of_children=st.slider('No of Children')

    no_of_weekend_nights= st.slider('no_of_weekend_nights')
    no_of_week_nights=st.slider('no_of_week_nights')
     
     
     
    required_car_parking_space= st.slider('required_car_parking_space')
    lead_time=st.slider('lead_time')
    
    arrival_year=st.slider('arrival_year')
    arrival_month=st.slider('rrival_month')
    arrival_date=st.slider('arrival_date')

    market_segment_type= st.slider('market_segment_type')
    repeated_guest=st.slider('repeated_guest')
    
    no_of_previous_cancellations= st.slider('no_of_previous_cancellations')
    no_of_previous_bookings_not_canceled=st.slider('no_of_previous_bookings_not_canceled')
    
    avg_price_per_room=st.slider('avg_price_per_room')
    no_of_special_req=st.slider('no_of_special_requests')
   # no_of_special_req=st.slider('no_of_special_requests')
    


    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    
    if st.button("Predict"):
        result = prediction(no_of_adults ,no_of_children,no_of_weekend_nights,no_of_week_nights,

    required_car_parking_space,
    lead_time,
    
    arrival_year,
    arrival_month,
    arrival_date,
    
    market_segment_type,
    repeated_guest,
    
    no_of_previous_cancellations,
    no_of_previous_bookings_not_canceled,
    
    avg_price_per_room,
    no_of_special_req)
    
        st.success('The customer has high probability the it will {}'.format(result))
     
if __name__=='__main__':
    main()
