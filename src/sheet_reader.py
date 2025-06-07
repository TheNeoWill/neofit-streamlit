def load_workout_data():
    import gspread
    import pandas as pd
    from oauth2client.service_account import ServiceAccountCredentials
    import streamlit as st
    import json

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        json.loads(st.secrets["google"]["service_account"]),
        scope
    )
    client = gspread.authorize(credentials)

    sheet = client.open("Workout Tracker").worksheet("Workout log")
    data = sheet.get_all_records()
    return pd.DataFrame(data)
