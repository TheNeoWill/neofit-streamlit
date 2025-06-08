from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import base64
import streamlit as st
import pandas as pd
st.write("🔍 Raw secret preview:", repr(st.secrets["google"]["service_account_b64"][:200]))
from src.sheet_reader import load_workout_data

def render_dashboard():
    st.title("📊 NeoFit Dashboard")
    df = load_workout_data()

    if df.empty:
        st.warning("No workouts logged yet.")
        return

    # Clean up
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    df["Duration (min)"] = pd.to_numeric(df["Duration (min)"]
                                         .astype(str)
                                         .str.replace("mins", "", case=False)
                                         .str.strip(), errors="coerce")

    df["Intensity (1-5)"] = pd.to_numeric(df["Intensity (1-5)"], errors="coerce")

    st.subheader("Workout Frequency (Last 4 Weeks)")
    # Format week labels like "Jun 03"
    df["Week"] = df["Date"].dt.to_period("W").apply(lambda r: r.start_time.strftime("%b %d"))
    freq = df["Week"].value_counts().sort_index()
    st.bar_chart(freq)

    st.subheader("Body Focus Distribution")
    st.bar_chart(df["Body Focus"].value_counts())

    st.subheader("Intensity Over Time")
    st.line_chart(df.set_index("Date")["Intensity (1-5)"])

    st.subheader("Session Duration Over Time")
    st.line_chart(df.set_index("Date")["Duration (min)"])
