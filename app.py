import streamlit as st
import requests

# Title and description
st.title("AI Models: Classification, Sentiment, Summary, Labeling")
st.write("Choose a model and input data to get the desired result.")

# Model selection
model_choice = st.selectbox(
    "Which model would you like to use?",
    ("Classification", "Sentiment Analysis", "Summary", "Labeling")
)

# Input section for user data
input_data = st.text_input("Enter your input data")

# If Classification is selected, ask for classes input
if model_choice == "Classification":
    classes = st.text_input("Enter the list of classes (comma-separated)")

# Function to send a request to the FastAPI backend
def get_prediction(model, input_data, classes=None):
    if model == "Classification":
        api_url = "http://localhost:8000/classification"
        data = {
            'chat': input_data,
            'classes': [cls.strip() for cls in classes.split(',')]
        }
    elif model == "Sentiment Analysis":
        api_url = "http://localhost:8000/sentiment"
        data = {'chat': input_data}
    elif model == "Summary":
        api_url = "http://localhost:8000/summary"
        data = {'chat': input_data}
    elif model == "Labeling":
        api_url = "http://localhost:8000/label"
        data = {'chat': input_data}

    # Make the POST request
    response = requests.post(api_url, json=data)
    return response.json()

# When the user clicks the Predict button
if st.button("Predict"):
    if input_data:
        if model_choice == "Classification" and not classes:
            st.write("Please enter classes for classification.")
        else:
            result = get_prediction(model_choice, input_data, classes if model_choice == "Classification" else None)
            st.write(f"{model_choice} Output:", result)
    else:
        st.write("Please enter input data.")

