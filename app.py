import streamlit as st
import time
from data_logger import MultiplierLogger

st.set_page_config(page_title="Aviator Multiplier Tracker", layout="centered")

st.title("1xBet Aviator Multiplier Tracker")

logger = MultiplierLogger()

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
    st.info("Tracking multipliers...")

    multiplier = logger.simulate_next_multiplier()
    logger.log_multiplier(multiplier)

    st.write(f"Current multiplier: **{multiplier}x**")

    high_multipliers = logger.get_high_multipliers()
    st.write("### High Multipliers Log (>=100x)")
    st.table(high_multipliers)

    # Refresh page every 3 seconds to simulate live data
    time.sleep(3)
    st.experimental_rerun()
else:
    st.write("Click **Start Tracking** to begin.")