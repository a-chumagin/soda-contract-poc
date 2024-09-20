import streamlit as st
import pandas as pd
import json, os

def load_data(folder_path):
    filenames = os.listdir(folder_path)
    query_params = st.query_params
    if query_params == {}:
        selected_filename = st.selectbox('Select a file', filenames)
    else:
        selected_filename = st.query_params.file

    file_name = os.path.join(folder_path, selected_filename)
    with open(file_name, "r") as f:
        data = json.load(f, strict=False)
    return pd.json_normalize(data), selected_filename

def calculate_time_running(start_time, end_time):
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)
    return (end_time - start_time).total_seconds()

def get_outcomes(checks, outcome):
  all_checks = []
  for check in checks:
    if check['outcome'] == outcome:
      all_checks.append({
        'Name': check['name'],
        'Table name': check['table'],
        'Outcome': check['outcome'],
        'Diagnostics': check['diagnostics'],
        'Description': get_description_value(check)
      })
  return pd.DataFrame(all_checks)

def get_description_value(check):
  description_value = check['resourceAttributes'][0]['value'] if check['resourceAttributes'] else 'N/A'
  return description_value

def display_report(df, selected_filename):
    st.markdown(f"[share](/?file={selected_filename})")
    checks = df['checks'][0]
    failed_checks = get_outcomes(checks, 'fail')
    passed_checks = get_outcomes(checks, 'pass')
    df['checks'] = df['checks'].astype(str)
    st.write(f"Definition Name: {df['definitionName'][0]}")
    st.write(f"Default data source:  {df['defaultDataSource'][0]}")

    time_running = calculate_time_running(df['scanStartTimestamp'][0], df['scanEndTimestamp'][0])
    st.write(f"Time running, sec: {time_running}")

    st.write(f"Checks count: {len(checks)}")
    st.write('Number of failed checks:', len(failed_checks))
    st.write('Number of passed checks:', len(passed_checks))

    st.write('Passed checks:')
    st.table(passed_checks)

    st.write('Failed checks:')
    st.table(failed_checks)

    st.write('Logs:')
    st.write(df['logs'][0])

# Call the function to display the report
folder_path = './data/results'
df,selected_filename  = load_data(folder_path)
display_report(df, selected_filename)