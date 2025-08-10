import streamlit as st
import plotly.graph_objects as go
import sys
import os


# Add the pages directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))

# Import page modules with error handling
def safe_import(module_name):
    try:
        return __import__(module_name)
    except ImportError:
        return None

# Import your page modules
overview = safe_import('overview')
career = safe_import('career')
awards = safe_import('awards')
disciplinary_statistics = safe_import('disciplinary_statistics')

heatmap = safe_import('heatmap')
verdict = safe_import('verdict')
club = safe_import('club')
clutch = safe_import('clutch')
fame = safe_import('fame')
international = safe_import('international')
physical = safe_import('physical')
season = safe_import('season')

def main():
    """Main dashboard application with beautiful navbar"""
    
    # Page configuration
    st.set_page_config(
        page_title="GOAT Debate: Messi vs Ronaldo",
        page_icon="⚽",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state - DEFAULT TO OVERVIEW
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'overview'
    
    # Enhanced CSS for compact, clean styling
    st.markdown("""
    <style>
    /* Hide Streamlit elements and remove top spacing */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    section[data-testid="stSidebarNav"] {display: none;}
    .css-1d391kg {display: none;}
    
    /* Remove top padding/margin from main container */
    .main > div {
        padding-top: 0rem !important;
    }
    
    .block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    
    /* Remove space above header */
    .stApp > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Compact hero section - no top margin */
    .hero-section {
        background: linear-gradient(135deg, #0f4c75 0%, #3282b8 100%);
        padding: 1.5rem 0;
        margin: 0 -1rem 2rem -1rem;
        position: relative;
        border-bottom: 3px solid #FFD700;
    }
    
    .hero-content {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 2rem;
        text-align: center;
    }
    
    /* Compact main title */
    .main-title {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0 0 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        letter-spacing: 1px;
    }
    
    .subtitle {
        color: #FFD700;
        font-size: 1rem;
        margin: 0;
        font-weight: 500;
        letter-spacing: 1px;
    }
    
    .comparison-title {
        color: #2c3e50;
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: none;
        position: relative;
        z-index: 1;
    }
    
    .comparison-title::after {
        content: '🔥';
        margin-left: 10px;
        animation: flame 1.5s ease-in-out infinite alternate;
    }
    
    @keyframes flame {
        from { transform: scale(1) rotate(-2deg); }
        to { transform: scale(1.1) rotate(2deg); }
    }
    
    /* Enhanced player comparison */
    .player-comparison {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }
    
    .player-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 2rem;
        min-width: 280px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        border: 3px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .player-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, transparent, currentColor, transparent);
        transform: translateX(-100%);
        transition: transform 0.6s ease;
    }
    
    .player-card:hover::before {
        transform: translateX(100%);
    }
    
    .player-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0,0,0,0.25);
    }
    
    .player-card.messi {
        
        color: #4ECDC4;
    }
    
    .player-card.ronaldo {
        
        color: #FF6B6B;
    }
    
    .player-header {
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    .player-name {
        font-size: 1.4rem;
        font-weight: 800;
        color: #2c3e50;
        margin: 0.5rem 0;
        background: linear-gradient(45deg, currentColor, #2c3e50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .player-flag {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        display: block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .player-stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        border: 2px solid #dee2e6;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s ease;
    }
    
                //A
    .stat-card:hover::before {
        left: 100%;
    }
    
    .stat-card:hover {
        transform: translateY(-3px);
        border-color: currentColor;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        display: block;
        font-size: 1.3rem;
        font-weight: 800;
        color: #2c3e50;
        margin-bottom: 0.3rem;
        position: relative;
        z-index: 1;
    }
    
    .stat-label {
        font-size: 0.75rem;
        color: #6c757d;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 600;
        position: relative;
        z-index: 1;
    }
    
    .vs-divider {
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 80px;
    }
    
    .vs-text {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #4ECDC4, #FF6B6B, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        animation: pulse 2s ease-in-out infinite;
        position: relative;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    /* Enhanced navigation buttons */
    .stButton > button {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%) !important;
        color: #2c3e50 !important;
        border: 2px solid #e9ecef !important;
        border-radius: 12px !important;
        padding: 0.8rem 1rem !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        height: 55px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        position: relative !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(145deg, #4ECDC4 0%, #44A08D 100%) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(78, 205, 196, 0.4) !important;
        border-color: #4ECDC4 !important;
    }
    
    .stButton > button:focus,
    .stButton > button:active {
        background: linear-gradient(145deg, #FF6B6B 0%, #C44569 100%) !important;
        color: white !important;
        border-color: #FF6B6B !important;
        box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .player-comparison {
            flex-direction: column;
            gap: 1rem;
        }
        
        .player-card {
            min-width: 250px;
        }
        
        .vs-text {
            font-size: 2rem;
        }
        
        .stButton > button {
            height: 45px !important;
            font-size: 0.85rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Render the beautiful navbar
    render_enhanced_navbar()
    
    # Content area wrapper
    st.markdown('<div style="max-width: 1400px; margin: 0 auto; padding: 0 2rem;">', unsafe_allow_html=True)
    
    # Route to the appropriate page
    route_page()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_enhanced_navbar():
    """Render compact header and navbar with enhanced comparison sections"""
    
    # Compact hero section - simple and clean
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="main-title">🏆 THE GOAT DEBATE 🐐</h1>
            <p class="subtitle">Messi vs Ronaldo • The Greatest Rivalry</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Comparison Section - NO CONTAINER
    st.markdown('<h2 class="comparison-title">Quick Comparison</h2>', unsafe_allow_html=True)
    
    # Create columns for the comparison
    col1, col2, col3 = st.columns([3, 1, 3])
    
    with col1:
        st.markdown("""
        <div class="player-card messi">
            <div class="player-header">
                <span class="player-flag">🇦🇷</span>
                <div class="player-name">Lionel Messi</div>
            </div>
            <div class="player-stats-grid">
                <div class="stat-card">
                    <span class="stat-number">815</span>
                    <span class="stat-label">Goals</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">377</span>
                    <span class="stat-label">Assists</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">8</span>
                    <span class="stat-label">Ballon d'Or</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="vs-divider">
            <div class="vs-text">VS</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="player-card ronaldo">
            <div class="player-header">
                <span class="player-flag">🇵🇹</span>
                <div class="player-name">Cristiano Ronaldo</div>
            </div>
            <div class="player-stats-grid">
                <div class="stat-card">
                    <span class="stat-number">895</span>
                    <span class="stat-label">Goals</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">236</span>
                    <span class="stat-label">Assists</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">5</span>
                    <span class="stat-label">Ballon d'Or</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation section - clean and organized
    st.markdown("### 🧭 Explore the Debate")
    
    # Navigation buttons
    nav_items = [
        ('overview', 'Overview'),
        ('career', 'Career Stats'),
        ('awards', 'Awards'),
        ('disciplinary', 'Fair Play'),
        ('heatmap', 'Heat Maps'),
        ('physical', 'Physical'),
        ('clutch', 'Clutch'),
        ('international', 'International'),
        ('club', 'Clubs'),
        ('fame', 'Fame'),
        ('season', 'Seasons'),
        ('verdict', 'Final Verdict')
    ]
    
    # Create columns for navigation buttons
    cols = st.columns(6)
    
    for i, (page_key, page_label) in enumerate(nav_items):
        col_index = i % 6
        with cols[col_index]:
            if st.button(page_label, key=f"nav_{page_key}", use_container_width=True):
                st.session_state.current_page = page_key
                st.rerun()

def route_page():
    """Route to the appropriate page"""
    page = st.session_state.current_page
    
    try:
        if page == 'overview' and overview:
            overview.show()
        elif page == 'career' and career:
            career.show()
        elif page == 'awards' and awards:
            awards.show()
        elif page == 'disciplinary' and disciplinary_statistics:
            disciplinary_statistics.show()
        elif page == 'heatmap' and heatmap:
            st.write("Loading heatmap page...")  # DEBUG
            heatmap.show()
        elif page == 'physical' and physical:
            physical.show()
        elif page == 'clutch' and clutch:
            clutch.show()
        elif page == 'international' and international:
            international.show()
        elif page == 'club' and club:
            club.show()
        elif page == 'fame' and fame:
            fame.show()
        elif page == 'season' and season:
            season.show()
        elif page == 'verdict' and verdict:
            verdict.show()
        else:
            # Fallback to overview if page not found
            if overview:
                overview.show()
            else:
                show_page_not_found(page)
            
    except Exception as e:
        st.error(f"Error loading {page} page: {str(e)}")
        st.info("Make sure the page file exists and has a 'show()' function.")
        
        # Show overview as fallback
        if overview:
            st.info("Showing Overview page as fallback...")
            overview.show()

def show_page_not_found(page_name):
    """Show a not found message"""
    st.error(f"Page '{page_name}' not found or not properly configured.")
    st.info(f"Please make sure `pages/{page_name}.py` exists and has a `show()` function.")

if __name__ == "__main__":
    main()