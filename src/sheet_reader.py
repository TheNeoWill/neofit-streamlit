import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import json
import base64

def load_workout_data():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    key_b64 = st.secrets['google']['service_account_b64']
    key_json = base64.b64decode(key_b64).decode('utf-8')
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(key_json), scope)
    client = gspread.authorize(credentials)
    sheet = client.open('Workout Tracker').worksheet('Workout log')
    data = sheet.get_all_records()
    return pd.DataFrame(data)