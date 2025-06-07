import streamlit as st
from src.parser import parse_workout_input
from src.sheet_writer import write_workout_to_sheet

st.set_page_config(page_title="NeoFit Workout Logger", layout="centered")
st.title("🏋️ NeoFit Workout Logger")

with st.form("log_form"):
    body_focus = st.selectbox("Workout Type", ["Push", "Pull", "Legs", "Upper", "Lower", "Full Body", "Cardio"])
    duration = st.number_input("Duration (min)", min_value=5, max_value=180, step=5)
    intensity = st.slider("Intensity (1–5)", 1, 5, 3)
    exercises = st.text_area("Exercises (one per line)", height=150)
    notes = st.text_area("Notes", height=100)

    submitted = st.form_submit_button("📈 Log Workout")

if submitted:
    entry = {
        "body_focus": body_focus,
        "duration": duration,
        "intensity": intensity,
        "exercises": exercises,
        "notes": notes
    }
    parsed = parse_workout_input(entry)
    write_workout_to_sheet(parsed)
    st.success("✅ Workout logged successfully!")
