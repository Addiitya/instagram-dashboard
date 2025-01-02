
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Instagram Dashboard", layout="wide")

# Embed CSS for custom styling
st.markdown(
    """
    <style>
        /* General styling */
        body {
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
        }

        h1, h2, h3 {
            color: #333;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #eaeaea;
        }

        /* Metric styling */
        div[data-testid="metric-container"] {
            background-color: #ffffff;
            border: 1px solid #eaeaea;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            color: #000000; /* Make all metric text black */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        div[data-testid="stMetricValue"] {
            color: #000000 !important; /* Ensure metric value is black */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Profile Section
st.sidebar.image("https://via.placeholder.com/150", width=150)
st.sidebar.markdown("### Your Profile")
st.sidebar.markdown("**Followers:** 200K")
st.sidebar.markdown("**Posts:** 1,542")
st.sidebar.markdown("---")

# Header Section
st.markdown("## Instagram Dashboard")
st.markdown("Visualize your Instagram performance metrics in real-time.")

# Metrics Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Followers", value="200K", delta="2.5K")
with col2:
    st.metric(label="Total Likes", value="1.5M", delta="-5%")
with col3:
    st.metric(label="Total Comments", value="800K", delta="+12%")
with col4:
    st.metric(label="Total Shares", value="120K", delta="+8%")

st.markdown("---")

# Mock Data
data = {
    "Post Type": ["Carousel", "Reels", "Static Image"],
    "Likes": [1500, 3000, 1000],
    "Comments": [200, 800, 150],
    "Shares": [100, 400, 50],
}

df = pd.DataFrame(data)

# Chart Section
st.markdown("### Engagement Metrics by Post Type")
fig = px.bar(
    df,
    x="Post Type",
    y=["Likes", "Comments", "Shares"],
    barmode="group",
    title="Engagement Breakdown",
    color_discrete_sequence=px.colors.qualitative.Bold,
)
st.plotly_chart(fig, use_container_width=True)

# Posts Section
st.markdown("### Popular Posts")
post_images = [
    "https://via.placeholder.com/300x300?text=Post+1",
    "https://via.placeholder.com/300x300?text=Post+2",
    "https://via.placeholder.com/300x300?text=Post+3",
]

col1, col2, col3 = st.columns(3)
col1.image(post_images[0], caption="Post 1")
col2.image(post_images[1], caption="Post 2")
col3.image(post_images[2], caption="Post 3")

# Insights Section
st.markdown("---")
st.markdown("### Insights")
st.write("📊 **Carousel posts** generate 20% higher engagement than static posts.")
st.write("🎥 **Reels** drive 2x more comments compared to other formats.")
st.write("📈 **Engagement rates** are increasing month-over-month.")
