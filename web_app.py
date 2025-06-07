import streamlit as st
from src.parser import parse_workout_input
from src.sheet_writer import write_workout_to_sheet

st.markdown("## 🏋️ NeoFit Logger")
st.caption("Log your training with speed and structure. No fluff. No tap-dancing.")
st.markdown("---")

with st.form("log_form"):
    st.header("📝 Log a New Workout")

    # Section 1: Focus + grouping
    st.caption("Workout Type and Focus")
    body_focus = st.selectbox("Body Focus", ["Push", "Pull", "Legs", "Upper", "Lower", "Full Body", "Cardio"])

    # Section 2: Duration + Intensity side-by-side
    st.caption("Session Details")
    col1, col2 = st.columns(2)
    with col1:
        duration = st.number_input("Duration (min)", min_value=5, max_value=180, step=5)
    with col2:
        intensity = st.slider("Intensity (1–5)", 1, 5, 3)

    # Section 3: Exercises
    st.caption("Exercises (one per line)")
    exercises = st.text_area("ex. Barbell Bench Press 5x10 @120lbs", height=150)

    # Section 4: Notes
    st.caption("Any notes?")
    notes = st.text_area("Optional notes", height=80)

    # Submit
    submitted = st.form_submit_button("Log this workout 🏋")

if submitted:
    entry = {
        "body_focus": body_focus,
        "duration": duration,
        "intensity": intensity,
        "exercises": exercises,
        "notes": notes
    }
    parsed = parse_workout_input(entry)
    with st.spinner("Writing to your sheet..."):
    write_workout_to_sheet(parsed)
    st.success("✅ lock and loaded!")
