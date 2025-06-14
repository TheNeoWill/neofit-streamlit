import streamlit as st
from src.parser import parse_workout_input
from src.sheet_writer import write_workout_to_sheet
from src.dashboard import render_dashboard

st.set_page_config(page_title="NeoFit Workout Logger", layout="centered")

st.title("🏋️ NeoFit Workout Logger")

page = st.sidebar.radio("🧭 Navigation", ["Log Workout", "Dashboard"])

def render_log_form():
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

        submitted = st.form_submit_button("📈 Log Workout")

        if submitted:
            user_input = {
                "body_focus": body_focus,
                "duration": duration,
                "intensity": intensity,
                "exercises": exercises,
                "notes": notes
            }
            parsed = parse_workout_input(user_input)
            write_workout_to_sheet(parsed)
            st.success("✅ Workout logged!")

if page == "Dashboard":
    try:
        render_dashboard()
    except Exception as e:
        st.error(f"Error loading dashboard: {e}")
else:
    render_log_form()

