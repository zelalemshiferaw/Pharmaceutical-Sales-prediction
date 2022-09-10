
import streamlit as st
import pandas as pd
import sys


sys.path.insert(0, '../scripts')


def app():
    st.title("Explanatory Data Analysis")

    distribution_option = st.selectbox(
        'Distribution of',
        ('Promotion on train and test data', 'Promotion Interval', 'School Holiday on Train Data', 'State Holiday on Train Data', 'Promotion on Train Data'))

    if distribution_option == 'Promotion on train and test data':
        st.header("Distribution of Promotion on train and test data")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/comparepromodistribution.png')
    elif distribution_option == 'Promotion Interval':
        st.header("Distribution of Promotion Interval")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/distributionofpromointerval.png')
    elif distribution_option == 'School Holiday on Train Data':
        st.subheader("School Holiday")
        st.image('./images/distributionofschoolholiday.png')
    elif distribution_option == 'State Holiday on Train Data':
        st.subheader("State Holiday")
        st.image('./images/distributionofstateholiday.png')
    elif distribution_option == 'Promotion on Train Data':
        st.subheader("Promotion")
        st.image('./images/distributionoftrainpromo.png')

    compare_option = st.selectbox(
        'Comaprison of sales and custromer By',
        ('schoolholiday', 'stateholiday', 'assortment', 'Day Of Week', 'Store Type', 'Month', 'Count'))

    if compare_option == 'schoolholiday':
        st.subheader("School Hoiday")
        st.image('./images/schoolholidayvssalesandcustomer.png')
    elif compare_option == 'stateholiday':
        st.subheader("State Hoiday")
        st.image('./images/stateholidayvssalesandcustomer.png')
    elif compare_option == 'assortment':
        st.subheader("Assortment")
        st.image('./images/assortmentvssalesandcustomer.png')
    elif compare_option == 'Day Of Week':
        st.subheader("Day of Week")
        st.image('./images/dayofweekvssalesandcustomer.png')
    elif compare_option == 'Store Type':
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Sales")
            st.image('./images/salesbystoretype.png')

        with col2:
            st.subheader("Customers")
            st.image('./images/customerbystoretype.png')
    elif compare_option == 'Month':
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Sales")
            st.image('./images/salesforeachmonth.png')

        with col2:
            st.subheader("Customers")
            st.image('./images/customersofeachmonth.png')

    elif compare_option == 'Count':
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Sales Count")
            st.image('./images/distributionofsales.png')

        with col2:
            st.subheader("Customer Count")
            st.image('./images/distributionofcustomers.png')

    correlation_option = st.selectbox(
        'Correlation Views',
        ('sales vs customer', 'sales vs competition distance', 'promotion vs customer', '10 choosen variables'))

    if correlation_option == 'sales vs customer':
        st.subheader("Correlation of Customer and Sales")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/correlationsalesandcustomer.png')
    elif correlation_option == 'promotion vs customer':
        st.subheader("Correlation of Customer and Promo")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/correlationpromoandcustomer.png')
    elif correlation_option == 'sales vs competition distance':
        st.subheader("Correlation of Sales And Competition distance")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/correlationsalesanddistance.png')
    else:
        st.subheader("Correlation of 10 Selected Variables")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/correlationtraindata.png')

    st.header("Christmass sales of 2014/15")
    # st.subheader("Impact on Customer Based on Day of Week")
    st.image('./images/christmasssales.png')

    col1, col2 = st.columns(2)

    with col1:
        st.header("Sales of store that open all weekdays")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/openstoresallweekdays.png')

    with col2:
        st.header("Sales of store that do not open all weekdays")
        # st.subheader("Impact on Customer Based on Day of Week")
        st.image('./images/notopenstoreallweekdays.png')

    st.header("Sales When Store and Open")
    # st.subheader("Impact on Customer Based on Day of Week")
    st.image('./images/storeopenclosecustomerbehaviour.png')

    st.header("Assortment vs sales")
    # st.subheader("Impact on Customer Based on Day of Week")
    st.image('./images/assortmentvssales.png')