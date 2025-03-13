import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("fantasy_cricket_data.csv")

data = load_data()

# Streamlit UI
st.title("Fantasy Cricket AI Predictor 🏏")
st.write("Select your players and predict the best team!")

# Show available players
st.subheader("Available Players")
st.dataframe(data[['Player of the Match', 'Runs Scored', 'Wickets Taken', 'Fantasy Points']])

# Feature selection for ML model
features = data[['Runs Scored', 'Wickets Taken']]
labels = np.where(data['Fantasy Points'] > 100, 1, 0)  # 1 = Good player, 0 = Average player

# Train AI model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(features, labels)

# User input for prediction
st.subheader("Predict Your Team's Performance")
runs = st.number_input("Enter Expected Runs of Player", min_value=0, max_value=200, value=50)
wickets = st.number_input("Enter Expected Wickets of Player", min_value=0, max_value=10, value=2)

# Make prediction
if st.button("Predict Player Performance"):
    prediction = model.predict([[runs, wickets]])
    if prediction[0] == 1:
        st.success("This player is a **Great Choice!** ✅")
    else:
        st.warning("This player might not be the best option. ❌")
