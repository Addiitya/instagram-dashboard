import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import time

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
    # Fetch top countries data (replace with actual API call)
    top_countries_data = fetch_top_countries() 
    if top_countries_data:
        # Example: Create a bar chart to visualize top countries
        df_top_countries = pd.DataFrame(top_countries_data) 
        fig = px.bar(df_top_countries, x='country', y='count', title="Top Countries")
        st.plotly_chart(fig)
    else:
        st.warning("Failed to fetch top countries data.")
    st.subheader("Most Active Times")
    # Sample follower activity data
    follower_activity_data = {
        "Hour": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "Followers": [140, 149, 160, 125, 41, 32, 101, 140, 140, 120, 110, 90, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    }
    df_follower_activity = pd.DataFrame(follower_activity_data)
    fig = px.line(df_follower_activity, x="Hour", y="Followers", title="Follower Activity by Hour")
    st.plotly_chart(fig)

elif st.session_state.page == "Content":
    st.header("Content")
    st.subheader("Interactions by Content Type")
    # Sample interaction data
    interaction_data = {
        "Content Type": ["Reels", "Stories", "Posts"],
        "Interactions": [54.5, 40.9, 4.5]
    }
    df_interactions = pd.DataFrame(interaction_data)
    fig = px.bar(df_interactions, x="Content Type", y="Interactions", title="Interactions by Content Type")
    st.plotly_chart(fig)
    st.subheader("Views by Content Type")
    # Sample view data
    view_data = {
        "Content Type": ["Stories", "Posts", "Reels"],
        "Views": [87.0, 7.7, 5.4]
    }
    df_views = pd.DataFrame(view_data)
    fig = px.bar(df_views, x="Content Type", y="Views", title="Views by Content Type")
    st.plotly_chart(fig)

elif st.session_state.page == "Activity":
    st.header("Activity")
    # Sample recent activity data
    recent_activity_data = [
        {"text": "Post 1"},
        {"text": "Post 2"},
        {"text": "Post 3"}
    ]
    st.subheader("Recent Posts")
    for post in recent_activity_data:
        st.write(f"- {post['text']}")

# --- Placeholder for Data Fetching (Replace with API Calls) ---

# --- Example: Fetching Top Countries (Replace with actual API call) ---
def fetch_top_countries():
    try:
        # Replace with actual API endpoint and authentication
        response = requests.get("https://api.instagram.com/v1/your_data_endpoint", 
                                headers={"Authorization": f"Bearer {YOUR_ACCESS_TOKEN}"}) 
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data['data']  # Adjust based on the API response structure
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching top countries: {e}")
        return None

# --- Run App ---

if __name__ == "__main__":
    if st.button("Refresh Data"):
        # Fetch and update data from sources (e.g., API calls)
        pass