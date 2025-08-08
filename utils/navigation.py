import streamlit as st

def create_navbar():
    """Create navigation buttons"""
    navbar_items = [
        ("🏠 Overview", "overview"),
        ("📊 Career Stats", "career"),
        ("🏆 Club Performance", "club"),
        ("🌍 International", "international"),
        ("🥇 Awards", "awards"),
        ("💪 Physical", "physical"),
        ("📱 Fame", "fame"),
        ("⚽ Leagues", "leagues"),
        ("🔥 Clutch", "clutch"),
        ("🗺️ Heat Maps", "heatmaps"),
        ("🏁 Verdict", "verdict")
    ]
    
    return navbar_items

def handle_navigation():
    """Handle navigation and return current page"""
    navbar_items = create_navbar()
    
    # Create navigation buttons in columns
    cols = st.columns(len(navbar_items))
    
    for i, (label, key) in enumerate(navbar_items):
        with cols[i]:
            if st.button(label, key=f"nav_{key}", help=f"Go to {label}"):
                st.session_state.current_page = key
                st.rerun()
    
    return st.session_state.current_page