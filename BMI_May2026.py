import streamlit as st
import google.genai as genai

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("BMI Calculator with AI Nutritionist")

# Input fields for height and weight
ht = st.slider("Enter your height in meters:", min_value=1.0, max_value=2.5, step=0.01)
wt = st.slider("Enter your weight in kilograms:", min_value=1.0, max_value=300.0, step=0.1)
gender = st.selectbox("Select your gender:", ["Male", "Female"])

# Calculate BMI
bmi = wt / (ht ** 2)
st.write(f"Your BMI is: {bmi:.2f}")

prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, and BMI as {bmi}"

# Generate content from Gemini
if st.button("Take Ai Advice"):
    response = client.models.generate_content(model="gemini-2.5-flash",contents= prompt)
    st.write(response.text)
