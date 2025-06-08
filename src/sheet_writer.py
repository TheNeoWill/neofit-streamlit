import base64
import json
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def write_workout_to_sheet(row_dict, spreadsheet_name="Workout Tracker", worksheet_name="Workout log"):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Decode base64 service account JSON
    key_json = base64.b64decode(st.secrets["google"]["service_account_b64"]).decode("utf-8")
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(key_json), scope)

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
    sheet.append_row([str(x) if x is not None else "" for x in row])
