import gspread
import streamlit as st
import json
from oauth2client.service_account import ServiceAccountCredentials

def write_workout_to_sheet(row_dict, spreadsheet_name="Workout Tracker", worksheet_name="Workout log"):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(st.secrets["google"]["service_account"]), scope)
    client = gspread.authorize(credentials)

    sheet = client.open(spreadsheet_name).worksheet(worksheet_name)

    row = [
        row_dict.get("Date"),
        row_dict.get("Workout Type"),
        row_dict.get("Duration (min)"),
        row_dict.get("Intensity (1–5)"),
        row_dict.get("Body Focus"),
        row_dict.get("Sets x (Reps x Lbs)"),
        row_dict.get("Notes")
    ]
    sheet.append_row(row)
