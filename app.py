import streamlit as st
import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier

# Title of the Streamlit app
st.title("🏏 Fantasy Cricket AI - Team Predictor")

# Load sample player data (Replace with actual dataset)
data = {
    "Player": [
        "Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah", "Hardik Pandya", "KL Rahul",
        "Steve Smith", "David Warner", "Kane Williamson", "Joe Root", "Babar Azam", "Ben Stokes",
        "Trent Boult", "Rashid Khan", "Shakib Al Hasan", "Faf du Plessis", "Quinton de Kock",
        "Andre Russell", "Glenn Maxwell"
    ],
    "Batting Avg": [58, 45, 50, 20, 35, 42, 48, 44, 52, 49, 56, 42, 18, 23, 38, 40, 39, 32, 36],
    "Bowling Avg": [0, 5, 0, 18, 25, 0, 0, 2, 0, 4, 3, 30, 22, 15, 21, 6, 2, 19, 10],
    "Strike Rate": [135, 140, 130, 90, 150, 145, 125, 135, 120, 115, 130, 140, 85, 110, 125, 128, 136, 160, 155],
    "Wickets": [0, 2, 0, 150, 75, 0, 0, 1, 0, 5, 2, 45, 210, 350, 300, 8, 12, 200, 150],
}

df = pd.DataFrame(data)

st.subheader("📊 Player Stats")
st.dataframe(df)

# Select players to form a team
st.subheader("🏏 Select Your Fantasy Team")
selected_players = st.multiselect("Choose 11 Players:", df["Player"].tolist())

if len(selected_players) == 11:
    st.success("✅ You have selected 11 players!")
else:
    st.warning("⚠ Please select exactly 11 players!")

# AI Prediction Model (Dummy Model for Now)
st.subheader("🔮 AI Match Outcome Prediction")
if st.button("Predict Result"):
    if len(selected_players) != 11:
        st.error("❌ Please select exactly 11 players to proceed!")
    else:
        # Dummy AI Model
        random_outcome = random.choice(["Win", "Lose", "Draw"])
        st.write(f"**Prediction:** Your Fantasy Team is likely to **{random_outcome}** the match! 🏆")

st.markdown("---")
st.caption("Created by Fantasy Cricket AI - Powered by Streamlit 🚀")
