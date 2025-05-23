import streamlit as st
import time
from data_logger import MultiplierLogger
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Aviator Multiplier Tracker", layout="centered")

st.title("1xBet Aviator Multiplier Tracker")

logger = MultiplierLogger()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"**Current Time:** {current_time}")

if 'start' not in st.session_state:
    st.session_state.start = False

def start_tracking():
    st.session_state.start = True

def stop_tracking():
    st.session_state.start = False

col1, col2 = st.columns(2)
with col1:
    if st.button("Start Tracking") and not st.session_state.start:
        start_tracking()
with col2:
    if st.button("Stop Tracking") and st.session_state.start:
        stop_tracking()

if st.session_state.start:
    st.success("Tracking multipliers...")

    multiplier = logger.simulate_next_multiplier()
    logger.log_multiplier(multiplier)

    st.metric(label="Current Multiplier", value=f"{multiplier}x")

    df = logger.get_dataframe()
    logger.save_to_csv(df)

    # Filters
    st.write("### Filter Log")
    min_val = st.slider("Minimum Multiplier", 1, 1000, 100)
    filtered_df = df[df["multiplier"] >= min_val]

    st.write(f"### Multiplier Log (>= {min_val}x)")
    st.dataframe(filtered_df, use_container_width=True)

    # Graph
    st.write("### Multiplier Timeline")
    st.line_chart(filtered_df.set_index("timestamp")["multiplier"])

    time.sleep(3)
    st.experimental_rerun()
else:
    st.info("Click **Start Tracking** to simulate multiplier tracking.")
