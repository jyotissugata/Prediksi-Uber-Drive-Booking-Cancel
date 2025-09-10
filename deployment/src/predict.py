# import libraries
import streamlit as st
import pandas as pd
import pickle

def run():

    with open('./model_akhir.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    st.title("Predict Booking Cancel")

    # pembuatan form
    with st.form('booking_data'):
        st.write('## Isi Dengan Data Booking')

        date = st.date_input('Date:', value=pd.to_datetime('2024-11-29'))
        time = st.time_input('Time:', value=pd.to_datetime('18:01:39').time())
        booking_id = st.text_input('Booking ID:', placeholder="CNR1326809", value='CNR1326809')
        booking_status = st.selectbox('Booking Status:', options=['No Driver Found', 'Complete', 'Incomplete', 'Cancelled by Driver', 'Cancelled by Customer'], placeholder='Incomplete', index=1)
        customer_id = st.text_input('Customer ID:', placeholder="CID4604802", value='CID4604802')
        vehicle_type = st.selectbox('Vehicle Type:', options=['eBike', 'Go Sedan', 'Auto', 'Premier Sedan', 'Bike', 'Go Mini', 'Uber XL'], placeholder='Go Sedan', index=0)
        pickup_location = st.text_input('Pickup Location:', placeholder="Shastri Nagar", value='Shastri Nagar')
        drop_location = st.text_input('Drop Location:', placeholder="Gurgaon Sector 56", value='Gurgaon Sector 56')
        avg_vtat = st.number_input('Avg VTAT:', min_value=2.0, max_value=20.0, value=4.9, step=0.1, format="%.1f")
        avg_ctat = st.number_input('Avg CTAT:', min_value=10.0 , max_value=45.0, value=14.0, step=0.1, format="%.1f")
        cancelled_rides_by_customer = st.checkbox('Cancelled Rides by Customer', value=False)
        reason_for_cancelling_by_customer = st.selectbox('Reason for cancelling by Customer:', options=['Driver is not moving towards pickup location', 'Driver asked to cancel', 'AC is not working', 'Change of plans', 'Wrong Address'], placeholder='No Reason', index=0)
        cancelled_rides_by_driver = st.checkbox('Cancelled Rides by Driver', value=False)
        driver_cancellation_reason = st.selectbox('Driver Cancellation Reason:', options=['Personal & Car related issues', 'Customer related issue', 'More than permitted people in there', 'The customer was coughing/sick'], placeholder='No Reason', index=0)
        incomplete_rides = st.checkbox('Incomplete Rides', value=False)
        incomplete_rides_reason = st.selectbox('Incomplete Rides Reason:', options=['Vehicle Breakdown', 'Other Issue', 'Customer Demand'], placeholder='No Reason', index=0)
        booking_value = st.number_input('Booking Value:', min_value=50.0, max_value=4277.0, value=237.0, step=1.0, format="%.1f")
        ride_distance = st.number_input('Ride Distance:', min_value=1.0, max_value=50.0, value=5.73, step=0.01, format="%.2f")
        driver_ratings = st.number_input('Driver Ratings:', min_value=0.0, max_value=5.0, value=0.0, step=0.1, format="%.1f")
        customer_rating = st.number_input('Customer Rating:', min_value=0.0, max_value=5.0, value=0.0, step=0.1, format="%.1f")
        payment_method = st.selectbox('Payment Method:', options=['UPI', 'Debit Card', 'Cash', 'Uber Wallet', 'Credit Card'], placeholder='UPI', index=0)

        predict = st.form_submit_button('Predict')

    data_inf = {
        'Date': date,
        'Time': time,
        'Booking ID': booking_id,
        'Booking Status': booking_status,
        'Customer ID': customer_id,
        'Vehicle Type': vehicle_type,
        'Pickup Location': pickup_location,
        'Drop Location': drop_location,
        'Avg VTAT': avg_vtat,
        'Avg CTAT': avg_ctat,
        'Cancelled Rides by Customer': 1 if cancelled_rides_by_customer else None,
        'Reason for cancelling by Customer': reason_for_cancelling_by_customer,
        'Cancelled Rides by Driver':  1 if cancelled_rides_by_driver else None,
        'Driver Cancellation Reason': driver_cancellation_reason,
        'Incomplete Rides':  1 if incomplete_rides else None,
        'Incomplete Rides Reason': incomplete_rides_reason,
        'Booking Value': booking_value,
        'Ride Distance': ride_distance,
        'Driver Ratings': driver_ratings,
        'Customer Rating': customer_rating,
        'Payment Method': payment_method,
    }

    if (predict):
        data = pd.DataFrame([data_inf])
        st.dataframe(data.T, width=400, height=400)
        prediction = model.predict(data)
        st.write(f'## Cancel Booking: {bool(prediction[0])}')

if __name__ == '__main__':
    run()