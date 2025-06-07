import re
from datetime import datetime

def parse_workout_input(user_input: str):
    result = {
        "Date": datetime.today().strftime("%Y-%m-%d"),
        "Workout Type": "Strength",
        "Duration (min)": "",
        "Intensity (1–5)": "",
        "Body Focus": "",
        "Sets x (Reps x Lbs)": "",
        "Notes": ""
    }

    # Normalize input
    lines = user_input.get("exercises", "").splitlines()
    flat = " ".join(lines)

    # Body Focus
    match_focus = re.search(r'workout\s*:\s*(\w+)', flat, re.IGNORECASE)
    if match_focus:
        result["Body Focus"] = match_focus.group(1).capitalize()

    # Duration
    match_duration = re.search(r'duration\s*:\s*(\d+)', flat, re.IGNORECASE)
    if match_duration:
        result["Duration (min)"] = match_duration.group(1)

    # Intensity
    match_intensity = re.search(r'intensity\s*:\s*([1-5])', flat, re.IGNORECASE)
    if match_intensity:
        result["Intensity (1–5)"] = int(match_intensity.group(1))
    else:
        result["Intensity (1–5)"] = 3  # default

    # Exercises
    exercises = []
    for line in lines:
        if "-" in line and "@" in line:
            cleaned = line.replace("-", "").strip()
            exercises.append(cleaned)
        elif "exercises:" in line.lower():
            exercise_inline = re.findall(r'(\w[\w\s]+?\d+x\d+@[\d]+lbs)', line)
            exercises.extend(exercise_inline)
    if exercises:
        result["Sets x (Reps x Lbs)"] = "\n".join(f"- {e}" for e in exercises)

    # Notes
    notes_match = re.search(r'notes\s*:\s*(.*)', flat, re.IGNORECASE)
    if notes_match:
        result["Notes"] = notes_match.group(1).strip()
    else:
        result["Notes"] = user_input

    return result


