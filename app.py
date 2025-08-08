import streamlit as st
from pages import (
    overview, career_stats, club_performance, international, 
    awards, physical, fame, leagues, clutch, heatmaps, verdict
)
from utils.styling import apply_custom_css
from utils.navigation import create_navbar, handle_navigation

# Page configuration
st.set_page_config(
    page_title="🐐 GOAT Analysis: Messi vs Ronaldo",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
apply_custom_css()

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'overview'

# Main header
st.markdown('<h1 class="main-header">🐐 THE ULTIMATE GOAT DEBATE 🐐</h1>', unsafe_allow_html=True)

# Create and handle navigation
current_page = handle_navigation()

# Page routing
page_functions = {
    'overview': overview.show,
    'career': career_stats.show,
    'club': club_performance.show,
    'international': international.show,
    'awards': awards.show,
    'physical': physical.show,
    'fame': fame.show,
    'leagues': leagues.show,
    'clutch': clutch.show,
    'heatmaps': heatmaps.show,
    'verdict': verdict.show
}

# Display the selected page
if current_page in page_functions:
    page_functions[current_page]()
else:
    st.error("Page not found!")

# Footer
st.markdown("---")
st.markdown("### 🐐 About This Analysis")
st.markdown("Comprehensive comparison using real career statistics and performance metrics.")
st.markdown("**Data Sources**: Official club records, FIFA, UEFA, and statistical databases")
st.markdown("**Last Updated**: 2024")