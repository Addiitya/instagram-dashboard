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
            transition: all 0.3s ease-in-out;
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
            transition: all 0.3s ease;
        }

        .sidebar-title {
            font-size: 1.6em;
            margin-bottom: 20px;
            color: #333;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .sidebar-text {
            font-size: 1em;
            color: #555;
            margin: 5px 0;
        }

        /* Metric Cards */
        .metric-container {
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
            margin: 15px;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .metric-container:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);
        }

        /* Chart Section */
        .chart-container {
            background: #fff;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }

        /* Images Section */
        img {
            border-radius: 12px;
            max-width: 100%;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Buttons */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .metric-container {
                width: 100%;
                margin: 10px 0;
            }
            .sidebar-title {
                font-size: 1.2em;
            }
        }

        /* Animations */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Profile Section
st.sidebar.image(
    "https://www.w3schools.com/w3images/avatar2.png", width=150  # Example profile image
)
st.sidebar.markdown("<div class='sidebar-title'>Your Profile</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-text'>Followers: 200K</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-text'>Posts: 1,542</div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Header Section with smooth animation
st.markdown("<h1 class='fade-in'>Instagram Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Visualize your Instagram performance metrics in real-time.")

# Mock Data
data = {
    "Post Type": ["Carousel", "Reels", "Static Image"],
    "Likes": [1500, 3000, 1000],
    "Comments": [200, 800, 150],
    "Shares": [100, 400, 50],
}
df = pd.DataFrame(data)

# Metrics Section with hover animation
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='metric-container'><h3>Total Followers</h3><p>200K</p><p>+2.5K</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-container'><h3>Total Likes</h3><p>1.5M</p><p>-5%</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-container'><h3>Total Comments</h3><p>800K</p><p>+12%</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-container'><h3>Total Shares</h3><p>120K</p><p>+8%</p></div>", unsafe_allow_html=True)

st.markdown("---")

# Chart Section with more dynamic visuals
st.markdown("### Engagement Metrics by Post Type")
fig = px.bar(
    df,
    x="Post Type",
    y=["Likes", "Comments", "Shares"],
    barmode="group",
    title="Engagement Breakdown",
    color_discrete_sequence=px.colors.qualitative.Bold,
    height=400
)
st.plotly_chart(fig, use_container_width=True)

# Posts Section with hover animation
st.markdown("### Popular Posts")
post_images = [
    "https://www.w3schools.com/w3images/fjords.jpg",  # Example post image 1
    "https://www.w3schools.com/w3images/mountains.jpg",  # Example post image 2
    "https://www.w3schools.com/w3images/lights.jpg",  # Example post image 3
]

col1, col2, col3 = st.columns(3)
col1.image(post_images[0], caption="Post 1")
col2.image(post_images[1], caption="Post 2")
col3.image(post_images[2], caption="Post 3")

# Insights Section with more engaging styling
st.markdown("---")
st.markdown("### Insights")
st.write("📊 **Carousel posts** generate 20% higher engagement than static posts.")
st.write("🎥 **Reels** drive 2x more comments compared to other formats.")
st.write("📈 **Engagement rates** are increasing month-over-month.")

# CTA Button with interaction animation
st.markdown("<div class='stButton'><button>Explore More Insights</button></div>", unsafe_allow_html=True)
