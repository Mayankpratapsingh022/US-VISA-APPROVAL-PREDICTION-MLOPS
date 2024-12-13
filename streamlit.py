import streamlit as st
import requests

# Base URL of the FastAPI endpoint
API_URL = "http://localhost:8000/predict"

st.title("US Visa Prediction")

# Form inputs
with st.form("visa_form"):
    st.header("Visa Application Form")

    # Continent
    continent = st.selectbox(
        "Continent",
        options=["Asia", "Africa", "North America", "Europe", "South America", "Oceania"],
        help="Select the continent"
    )

    # Education of Employee
    education_of_employee = st.selectbox(
        "Education of Employee",
        options=["High School", "Master's", "Bachelor's", "Doctorate"],
        help="Select the highest level of education"
    )

    # Has Job Experience
    has_job_experience = st.selectbox(
        "Has Job Experience",
        options=["Y", "N"],
        help="Does the employee have job experience?"
    )

    # Requires Job Training
    requires_job_training = st.selectbox(
        "Requires Job Training",
        options=["Y", "N"],
        help="Does the job require training?"
    )

    # Number of Employees
    no_of_employees = st.number_input(
        "Number of Employees",
        min_value=14500,
        max_value=40000,
        value=20000,
        step=500,
        help="Enter the number of employees in the company"
    )

    # Region of Employment
    region_of_employment = st.selectbox(
        "Region of Employment",
        options=["West", "Northeast", "South", "Midwest", "Island"],
        help="Select the employment region"
    )

    # Prevailing Wage
    prevailing_wage = st.number_input(
        "Prevailing Wage",
        min_value=600.0,
        max_value=70000.0,
        value=7000.0,
        step=100.0,
        help="Enter the prevailing wage"
    )

    # Unit of Wage
    unit_of_wage = st.selectbox(
        "Unit of Wage",
        options=["Hour", "Year", "Week", "Month"],
        help="Select the contract tenure unit"
    )

    # Full Time Position
    full_time_position = st.selectbox(
        "Full Time Position",
        options=["Y", "N"],
        help="Is it a full-time position?"
    )

    # Company Age
    company_age = st.number_input(
        "Age of the Company",
        min_value=15,
        max_value=180,
        value=50,
        step=5,
        help="Enter the age of the company"
    )

    # Submit button
    submit_button = st.form_submit_button(label="Predict Visa Status")

# API call on form submission
if submit_button:
    # Prepare the data payload
    payload = {
        "continent": continent,
        "education_of_employee": education_of_employee,
        "has_job_experience": has_job_experience,
        "requires_job_training": requires_job_training,
        "no_of_employees": no_of_employees,
        "region_of_employment": region_of_employment,
        "prevailing_wage": prevailing_wage,
        "unit_of_wage": unit_of_wage,
        "full_time_position": full_time_position,
        "company_age": company_age,
    }

    try:
        # Make the POST request to the FastAPI endpoint
        response = requests.post(API_URL, json=payload)
        response_data = response.json()

        if response.status_code == 200 and response_data.get("status", False):
            st.success(f"Prediction: {response_data['prediction']}")
        else:
            st.error(f"Error: {response_data.get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Error connecting to the API: {str(e)}")
