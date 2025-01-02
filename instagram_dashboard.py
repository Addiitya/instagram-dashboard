import streamlit as st
from langflow import Flow, DataStaxQueryNode, GPTNode, PlotlyChartNode
from langflow.nodes.llm import LLMNode
from langflow.utils import load_yaml
import pandas as pd
import plotly.express as px
import requests
import time
import logging
import json

# --- Configuration ---
try:
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f) 
except FileNotFoundError:
    st.error("config.yaml not found. Please create a config.yaml file with your credentials.")
    st.stop()

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

# --- Langflow Flow ---

def build_flow(post_type):
    """
    Constructs the Langflow workflow for the given post type.

    Args:
        post_type: The type of post (e.g., "carousel", "reel", "image")

    Returns:
        The constructed Langflow Flow object.
    """
    flow = Flow()

    # DataStax Query Node
    data_stax_node = DataStaxQueryNode(
        config=config["datastax"], 
        query=f"SELECT post_type, AVG(likes), AVG(comments), AVG(shares) FROM social_media_posts WHERE post_type = '{post_type}' GROUP BY post_type"
    )
    flow.add_node(data_stax_node)

    # GPT Node
    gpt_node = GPTNode(
        model_name="text-davinci-003", 
        prompt_template="""
        Given the following data: 
        {data}

        Generate concise and informative insights about the engagement of this post type. 
        Focus on comparisons and key takeaways. 
        """
    )
    flow.add_node(gpt_node)

    # Connect nodes
    flow.connect(data_stax_node, gpt_node, input_key="data")

    return flow

# --- Streamlit App ---

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
    fig = px.line(df_follower_activity, x="Hour", y="Followers", title="Follower Activity by Hour")
    st.plotly_chart(fig)

elif st.session_state.page == "Content":
    st.header("Content")
    st.subheader("Engagement by Post Type")
    post_types = ["carousel", "reel", "image"] 
    for post_type in post_types:
        try:
            flow = build_flow(post_type)
            result = flow.run()
            st.write(f"**{post_type}**: {result['gpt_output']}")
        except Exception as e:
            st.error(f"Error processing {post_type}: {e}")
            logging.error(f"Error processing {post_type}: {e}") 

elif st.session_state.page == "Activity":
    st.header("Activity")
    # Fetch recent activity data (replace with actual API call)
    recent_activity_data = fetch_recent_activity() 
    if recent_activity_data:
        # Example: Display recent posts (replace with actual data handling)
        st.subheader("Recent Posts")
        for post in recent_activity_data['posts']:
            st.write(f"- {post['text']}") 
    else:
        st.warning("Failed to fetch recent activity data.")

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
        logging.error(f"Error fetching top countries: {e}")
        return None

# --- Example: Fetching Recent Activity (Replace with actual API call) ---
def fetch_recent_activity():
    try:
        # Replace with actual API endpoint and authentication
        response = requests.get("https://api.instagram.com/v1/your_data_endpoint", 
                                headers={"Authorization": f"Bearer {YOUR_ACCESS_TOKEN}"}) 
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data['data']  # Adjust based on the API response structure
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching recent activity: {e}")
        logging.error(f"Error fetching recent activity: {e}")
        return None

# --- Run App ---

if __name__ == "__main__":
    if st.button("Refresh Data"):
        # Fetch and update data from sources (e.g., API calls)
        pass