import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Instagram Dashboard", layout="wide")

# Embed advanced CSS for Instagram-like styling
st.markdown(
    """
    <style>
        /* Global Styling */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background-color: #fafafa;
            color: #333;
        }
        h1, h2, h3 {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #2C3E50;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #fff;
            width: 300px;
            border-right: 2px solid #eaeaea;
            box-shadow: 4px 0px 6px rgba(0, 0, 0, 0.1);
            padding: 30px 15px;
        }

        .sidebar-title {
            font-size: 1.6em;
            margin-bottom: 20px;
            color: #333;
            font-weight: bold;
        }

        .metric-container {
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
            margin: 15px;
        }

        img {
            border-radius: 12px;
            max-width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Profile Section
st.sidebar.image(
    "https://www.w3schools.com/w3images/avatar2.png", width=150
)
st.sidebar.markdown("<div class='sidebar-title'>Your Profile</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-text'>Followers: 200K</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-text'>Posts: 1,542</div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Header Section
st.markdown("<h1>Instagram Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Visualize your Instagram performance metrics in real-time.")

# Mock Data for Engagement Metrics
data = {
    "Post Type": ["Carousel", "Reels", "Static Image"],
    "Likes": [1500, 3000, 1000],
    "Comments": [200, 800, 150],
    "Shares": [100, 400, 50],
}
df = pd.DataFrame(data)

# Metrics Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Followers", "200K", "+2.5K")
with col2:
    st.metric("Total Likes", "1.5M", "-5%")
with col3:
    st.metric("Total Comments", "800K", "+12%")
with col4:
    st.metric("Total Shares", "120K", "+8%")

st.markdown("---")

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
st.plotly_chart(fig)

# Posts Section with Popular Posts
st.markdown("### Popular Posts")
post_images = [
    "https://www.w3schools.com/w3images/fjords.jpg",
    "https://www.w3schools.com/w3images/mountains.jpg",
    "https://www.w3schools.com/w3images/lights.jpg",
]

col1, col2, col3 = st.columns(3)
col1.image(post_images[0], caption="Post 1")
col2.image(post_images[1], caption="Post 2")
col3.image(post_images[2], caption="Post 3")

# Insights Section
st.markdown("---")
st.markdown("### Insights")
insights = [
    "📊 **Carousel posts** generate higher engagement than static posts.",
    "🎥 **Reels** drive more comments compared to other formats.",
    "📈 **Engagement rates** are increasing month-over-month."
]
for insight in insights:
    st.write(insight)

# Call-To-Action Button
if st.button('Explore More Insights'):
    st.write("Redirecting to detailed insights... (This would link to another page or section)")

