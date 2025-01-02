import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import time
import requests

# --- Sample Data (Replace with API Data) ---
# ... (Sample data for interactions, views, followers as before) ...

# --- Styling ---
st.set_page_config(page_title="Instagram Insights", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #181818; /* Dark background */
        }
        .st-h1 {
            color: #fff;
        }
        .st-h2 {
            color: #fff;
        }
        .st-text {
            color: #fff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Navigation ---

if 'page' not in st.session_state:
    st.session_state.page = "Overview"

pages = ["Overview", "Audience", "Content", "Activity"]
selected_page = st.sidebar.selectbox("Select Page", pages)
st.session_state.page = selected_page

# --- Dashboard Layout ---

if st.session_state.page == "Overview":
    st.header("Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Account Reached", "1,771")
        st.metric("Impressions", "5,685")  # Replace with actual data
    with col2:
        st.metric("Profile Visits", 399)
        st.metric("Website Clicks", 10)  # Replace with actual data

elif st.session_state.page == "Audience":
    st.header("Audience")
    st.subheader("Top Countries")
    # ... (Code to fetch and display top countries) ...
    st.subheader("Most Active Times")
    fig = px.line(df_follower_activity, x="Hour", y="Followers", title="Follower Activity by Hour")
    st.plotly_chart(fig)

elif st.session_state.page == "Content":
    st.header("Content")
    st.subheader("Interactions by Content Type")
    fig = px.bar(df_interactions, x="Content Type", y="Interactions", title="Interactions by Content Type")
    st.plotly_chart(fig)
    st.subheader("Views by Content Type")
    fig = px.bar(df_views, x="Content Type", y="Views", title="Views by Content Type")
    st.plotly_chart(fig)

elif st.session_state.page == "Activity":
    st.header("Activity")
    # ... (Code to display recent activity - posts, stories, reels) ...

# --- Placeholder for Data Fetching (Replace with API Calls) ---

# --- Example: Fetching Top Countries (Replace with actual API call) ---
# (Note: This is a simplified example)
def fetch_top_countries():
    try:
        response = requests.get("https://api.example.com/top_countries")  # Replace with actual API endpoint
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching top countries: {e}")
        return None

# --- End of App ---