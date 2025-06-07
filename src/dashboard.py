import streamlit as st
import pandas as pd
from src.sheet_reader import load_workout_data

def render_dashboard():
    df = load_workout_data()
    st.title("📊 NeoFit Dashboard")

    if df.empty:
        st.warning("No workouts logged yet.")
        return

    df["Date"] = pd.to_datetime(df["Date"])

    # 1. Frequency
    freq = df["Date"].dt.to_period("W").value_counts().sort_index()
    st.subheader("Workout Frequency (Last 4 Weeks)")
    st.bar_chart(freq)

    # 2. Body Focus Distribution
    st.subheader("Body Focus Distribution")
    st.bar_chart(df["Body Focus"].value_counts())

    # 3. Intensity
    st.subheader("Intensity Over Time")
    st.line_chart(df.set_index("Date")["Intensity (1–5)"])

    # 4. Duration
    st.subheader("Session Duration Over Time")
    df["Duration (min)"] = pd.to_numeric(df["Duration (min)"], errors="coerce")
    st.line_chart(df.set_index("Date")["Duration (min)"])
