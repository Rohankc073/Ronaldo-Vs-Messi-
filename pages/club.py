import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the club performance analysis page"""
    st.markdown('<h1 class="section-header">🏆 CLUB PERFORMANCE ANALYSIS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    club_data = data['club_goals']
    
    # Page introduction
    st.markdown("""
    **Club football is where both legends built their reputations.** From Barcelona's tiki-taka to Real Madrid's 
    galáctico style, from Manchester United's counter-attacks to Juventus' tactical discipline - let's analyze 
    how Messi and Ronaldo performed across different clubs, leagues, and playing styles.
    """)
    
    # Club career overview
    st.markdown('<h3 class="section-header">🏟️ Club Career Overview</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card">
            <h3>🇦🇷 MESSI'S CLUB JOURNEY</h3>
            <h4>🔵 FC Barcelona (2003-2021)</h4>
            <p><strong>672 goals</strong> in 778 appearances</p>
            <p><strong>303 assists</strong> | <strong>34 trophies</strong></p>
            <p>La Liga's all-time top scorer</p>
            
            <h4>🔴 Paris Saint-Germain (2021-2023)</h4>
            <p><strong>32 goals</strong> in 75 appearances</p>
            <p><strong>35 assists</strong> | <strong>2 trophies</strong></p>
            <p>Adaptation period in new league</p>
            
            <h4>🩷 Inter Miami (2023-present)</h4>
            <p><strong>25+ goals</strong> in 30+ appearances</p>
            <p><strong>15+ assists</strong> | <strong>1 trophy</strong></p>
            <p>MLS revolution and Leagues Cup winner</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card">
            <h3>🇵🇹 RONALDO'S CLUB JOURNEY</h3>
            <h4>🔴 Manchester United (2003-2009, 2021-2022)</h4>
            <p><strong>145 goals</strong> in 346 appearances</p>
            <p><strong>64 assists</strong> | <strong>9 trophies</strong></p>
            <p>From winger to superstar</p>
            
            <h4>⚪ Real Madrid (2009-2018)</h4>
            <p><strong>451 goals</strong> in 438 appearances</p>
            <p><strong>131 assists</strong> | <strong>16 trophies</strong></p>
            <p>Galáctico era and Champions League king</p>
            
            <h4>⚫ Juventus (2018-2021)</h4>
            <p><strong>101 goals</strong> in 134 appearances</p>
            <p><strong>22 assists</strong> | <strong>5 trophies</strong></p>
            <p>Serie A domination</p>
            
            <h4>🟡 Al Nassr (2023-present)</h4>
            <p><strong>68+ goals</strong> in 70+ appearances</p>
            <p><strong>18+ assists</strong> | <strong>0 trophies</strong></p>
            <p>Saudi Arabian adventure</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Club goals comparison
    st.markdown('<h3 class="section-header">⚽ Goals by Club Comparison</h3>', unsafe_allow_html=True)
    
    # Prepare club data for visualization
    clubs = ['Barcelona', 'PSG', 'Inter Miami', 'Man United', 'Real Madrid', 'Juventus', 'Al Nassr', 'Sporting CP']
    messi_goals = [672, 32, 25, 0, 0, 0, 0, 0]
    ronaldo_goals = [0, 0, 0, 145, 451, 101, 68, 5]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Messi',
        x=clubs,
        y=messi_goals,
        marker_color='#4ECDC4',
        text=messi_goals,
        textposition='auto'
    ))
    fig.add_trace(go.Bar(
        name='Ronaldo',
        x=clubs,
        y=ronaldo_goals,
        marker_color='#FF6B6B',
        text=ronaldo_goals,
        textposition='auto'
    ))
    
    fig.update_layout(
        title="🎯 Career Goals by Club",
        barmode='group',
        height=500,
        template='plotly_white',
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed club statistics
    st.markdown('<h3 class="section-header">📊 Detailed Club Statistics</h3>', unsafe_allow_html=True)
    
    # Create detailed club data
    detailed_club_data = {
        'Club': ['Barcelona', 'PSG', 'Inter Miami', 'Man United (Total)', 'Real Madrid', 'Juventus', 'Al Nassr'],
        'Player': ['Messi', 'Messi', 'Messi', 'Ronaldo', 'Ronaldo', 'Ronaldo', 'Ronaldo'],
        'Years': ['2003-2021', '2021-2023', '2023-present', '2003-09, 21-22', '2009-2018', '2018-2021', '2023-present'],
        'Games': [778, 75, 34, 346, 438, 134, 74],
        'Goals': [672, 32, 25, 145, 451, 101, 68],
        'Assists': [303, 35, 15, 64, 131, 22, 18],
        'Goals per Game': [0.86, 0.43, 0.74, 0.42, 1.03, 0.75, 0.92],
        'Trophies': [34, 2, 1, 9, 16, 5, 0]
    }
    
    club_df = pd.DataFrame(detailed_club_data)
    st.dataframe(club_df, use_container_width=True, height=350)
    
    # Peak club performances
    st.markdown('<h3 class="section-header">🏔️ Peak Club Performances</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi's best seasons at Barcelona
        messi_seasons = {
            'Season': ['2011-12', '2009-10', '2018-19', '2015-16', '2012-13'],
            'Goals': [73, 47, 51, 41, 60],
            'Assists': [29, 11, 22, 23, 16],
            'Trophies': [3, 2, 0, 2, 0]
        }
        
        messi_df = pd.DataFrame(messi_seasons)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Goals',
            x=messi_df['Season'],
            y=messi_df['Goals'],
            marker_color='#4ECDC4',
            yaxis='y'
        ))
        fig.add_trace(go.Scatter(
            name='Assists',
            x=messi_df['Season'],
            y=messi_df['Assists'],
            mode='lines+markers',
            marker_color='#45B7D1',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="🇦🇷 Messi's Best Barcelona Seasons",
            yaxis=dict(title="Goals", side="left"),
            yaxis2=dict(title="Assists", side="right", overlaying="y"),
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Ronaldo's best seasons at Real Madrid
        ronaldo_seasons = {
            'Season': ['2013-14', '2014-15', '2011-12', '2015-16', '2017-18'],
            'Goals': [61, 61, 60, 51, 44],
            'Assists': [22, 18, 15, 16, 8],
            'Trophies': [4, 0, 1, 1, 3]
        }
        
        ronaldo_df = pd.DataFrame(ronaldo_seasons)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Goals',
            x=ronaldo_df['Season'],
            y=ronaldo_df['Goals'],
            marker_color='#FF6B6B',
            yaxis='y'
        ))
        fig.add_trace(go.Scatter(
            name='Assists',
            x=ronaldo_df['Season'],
            y=ronaldo_df['Assists'],
            mode='lines+markers',
            marker_color='#FF9999',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="🇵🇹 Ronaldo's Best Real Madrid Seasons",
            yaxis=dict(title="Goals", side="left"),
            yaxis2=dict(title="Assists", side="right", overlaying="y"),
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Champions League club performance
    st.markdown('<h3 class="section-header">🏆 Champions League Club Performance</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Champions League Titles", "5", "")
        st.caption("🇵🇹 Ronaldo leads")
        st.write("**Ronaldo:** 1 (United), 4 (Real Madrid)")
        st.write("**Messi:** 4 (Barcelona)")
    
    with col2:
        st.metric("CL Goals", "140", "vs 129")
        st.caption("🇵🇹 Ronaldo leads by 11")
        st.write("**Ronaldo:** 140 goals in 183 games")
        st.write("**Messi:** 129 goals in 163 games")
    
    with col3:
        st.metric("CL Goals per Game", "0.79", "vs 0.76")
        st.caption("🇦🇷 Messi slightly higher")
        st.write("**Messi:** 0.79 goals per game")
        st.write("**Ronaldo:** 0.76 goals per game")
    
    # Club adaptation analysis
    st.markdown('<h3 class="section-header">🔄 Club Adaptation Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Club Adaptations:
        
        **🔵 Barcelona (2003-2021) - Perfect Fit**
        - Grew up in La Masia academy
        - Perfect tactical fit with tiki-taka
        - All-time club legend status
        - 86% career goals at one club
        
        **🔴 PSG (2021-2023) - Adjustment Period**
        - Different league and style
        - More playmaker role, fewer goals
        - Strong assist numbers (35 in 75 games)
        - Champions League disappointments
        
        **🩷 Inter Miami (2023-present) - Renaissance**
        - Immediate impact in MLS
        - Leading team transformation
        - Perfect role as player-leader
        - Leagues Cup triumph in debut
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Club Adaptations:
        
        **🔴 Manchester United - Development**
        - From raw talent to superstar
        - Learned work ethic and professionalism
        - First Ballon d'Or at United
        - Return stint less successful
        
        **⚪ Real Madrid - Peak Years**
        - Goal machine optimization
        - 1.03 goals per game average
        - 4 Champions League titles
        - Greatest individual club period
        
        **⚫ Juventus - New Challenge**
        - Proved Serie A adaptability
        - Consistent 100+ goals in 3 years
        - Team trophies but CL disappointment
        
        **🟡 Al Nassr - Legacy Building**
        - Global football ambassador
        - Goal scoring continues at 39
        - New market development
        """)
    
    # Club trophies breakdown
    st.markdown('<h3 class="section-header">🏅 Club Trophies Breakdown</h3>', unsafe_allow_html=True)
    
    # Create trophies data
    trophies_data = {
        'Trophy Type': ['League Titles', 'Champions League', 'Domestic Cups', 'Super Cups', 'Club World Cup'],
        'Messi Total': [12, 4, 7, 8, 3],
        'Ronaldo Total': [7, 5, 4, 4, 4],
        'Messi Clubs': ['La Liga (10), Ligue 1 (2)', 'Barcelona (4)', 'Copa del Rey (7)', 'Various (8)', 'Barcelona (3)'],
        'Ronaldo Clubs': ['PL (3), La Liga (2), Serie A (2)', 'United (1), Real (4)', 'Various (4)', 'Various (4)', 'Real (4)']
    }
    
    trophies_df = pd.DataFrame(trophies_data)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Messi',
        x=trophies_data['Trophy Type'],
        y=trophies_data['Messi Total'],
        marker_color='#4ECDC4',
        text=trophies_data['Messi Total'],
        textposition='auto'
    ))
    fig.add_trace(go.Bar(
        name='Ronaldo',
        x=trophies_data['Trophy Type'],
        y=trophies_data['Ronaldo Total'],
        marker_color='#FF6B6B',
        text=trophies_data['Ronaldo Total'],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="🏆 Club Trophies by Category",
        barmode='group',
        height=400,
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(trophies_df, use_container_width=True)
    
    # Goals per season across clubs
    st.markdown('<h3 class="section-header">📈 Goals per Season Across Clubs</h3>', unsafe_allow_html=True)
    
    # Create season timeline with club colors
    seasons = list(range(2004, 2024))
    messi_goals_timeline = [6, 8, 17, 16, 38, 47, 60, 73, 60, 41, 58, 54, 45, 51, 36, 31, 30, 35, 16, 21]
    ronaldo_goals_timeline = [6, 9, 23, 42, 33, 40, 60, 55, 51, 61, 48, 50, 44, 42, 28, 37, 31, 29, 24, 14]
    
    # Club periods for coloring
    messi_clubs = ['Barcelona']*18 + ['PSG']*2
    ronaldo_clubs = ['United']*6 + ['Real Madrid']*9 + ['Juventus']*3 + ['United']*1 + ['Al Nassr']*1
    
    fig = go.Figure()
    
    # Messi timeline with club coloring
    colors_messi = ['#004D98' if club == 'Barcelona' else '#FF0000' if club == 'PSG' else '#FF69B4' for club in messi_clubs]
    fig.add_trace(go.Scatter(
        x=seasons,
        y=messi_goals_timeline,
        mode='lines+markers',
        name='Messi',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=8, color=colors_messi),
        hovertemplate='<b>Messi</b><br>Season: %{x}<br>Goals: %{y}<br>Club: %{text}<extra></extra>',
        text=messi_clubs
    ))
    
    # Ronaldo timeline with club coloring  
    colors_ronaldo = ['#FF0000' if club == 'United' else '#FFFFFF' if club == 'Real Madrid' else '#000000' if club == 'Juventus' else '#FFD700' for club in ronaldo_clubs]
    fig.add_trace(go.Scatter(
        x=seasons,
        y=ronaldo_goals_timeline,
        mode='lines+markers',
        name='Ronaldo',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=8, color=colors_ronaldo, line=dict(width=1, color='black')),
        hovertemplate='<b>Ronaldo</b><br>Season: %{x}<br>Goals: %{y}<br>Club: %{text}<extra></extra>',
        text=ronaldo_clubs
    ))
    
    # Add club transfer annotations
    fig.add_annotation(x=2021, y=35, text="Messi → PSG", arrowcolor="#4ECDC4", arrowwidth=2)
    fig.add_annotation(x=2009, y=40, text="Ronaldo → Real", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x=2018, y=28, text="Ronaldo → Juventus", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x=2023, y=21, text="Messi → Miami", arrowcolor="#4ECDC4", arrowwidth=2)
    
    fig.update_layout(
        title="⚽ Goals per Season Timeline with Club Changes",
        xaxis_title="Season",
        yaxis_title="Goals Scored",
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Club loyalty vs versatility analysis
    st.markdown('<h3 class="section-header">❤️ Club Loyalty vs Versatility</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏆 Club Loyalty Score</h4>
            <p><strong>🇦🇷 Messi: 9/10</strong></p>
            <p>• 18 years at Barcelona</p>
            <p>• 86% of career goals at one club</p>
            <p>• Grew from academy to legend</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo: 7/10</strong></p>
            <p>• Multiple successful moves</p>
            <p>• Adapted to different cultures</p>
            <p>• No single club dominance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>🌍 Versatility Score</h4>
            <p><strong>🇵🇹 Ronaldo: 10/10</strong></p>
            <p>• 4 different leagues</p>
            <p>• Proved adaptability everywhere</p>
            <p>• Success across different styles</p>
            <hr>
            <p><strong>🇦🇷 Messi: 7/10</strong></p>
            <p>• Struggled initially at PSG</p>
            <p>• Excellent at Inter Miami</p>
            <p>• Barcelona system perfectly suited</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>🎯 Club Impact Score</h4>
            <p><strong>🇦🇷 Messi: 10/10</strong></p>
            <p>• Transformed Barcelona style</p>
            <p>• Immediate Miami revolution</p>
            <p>• Tiki-taka perfectionist</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo: 9/10</strong></p>
            <p>• Galáctico era at Real Madrid</p>
            <p>• Consistent high standards</p>
            <p>• Goal machine wherever he goes</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Final club performance verdict
    st.markdown('<h3 class="section-header">🏁 Club Performance Verdict</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="final-verdict-card">
        <h2>🏟️ Club Performance Summary</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI'S STRENGTHS</h3>
                <p>✅ Higher goals per game at peak (0.86)</p>
                <p>✅ More assists across all clubs</p>
                <p>✅ Greater club loyalty (Barcelona)</p>
                <p>✅ More league titles (12 vs 7)</p>
                <p>✅ Perfect tactical fit at Barcelona</p>
            </div>
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO'S STRENGTHS</h3>
                <p>✅ More Champions League titles (5 vs 4)</p>
                <p>✅ Success in 4 different leagues</p>
                <p>✅ Greater adaptability and versatility</p>
                <p>✅ Consistent across all clubs</p>
                <p>✅ More Club World Cups (4 vs 3)</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Club Verdict:</strong> 🤝 <strong>DRAW</strong> - Different styles of excellence!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final analysis
    st.markdown("""
    ---
    ### 🌟 Club Career Analysis
    
    **🇦🇷 Messi's club career** represents the pinnacle of loyalty and single-club excellence. His 18-year Barcelona 
    journey from La Masia graduate to global icon is unmatched. While his PSG period showed adaptation challenges, 
    his Miami revival proves his magic transcends leagues.
    
    **🇵🇹 Ronaldo's club career** showcases incredible versatility and adaptability. From Manchester United's 
    developing star to Real Madrid's galáctico, from Juventus' tactical discipline to Al Nassr's global ambassador - 
    he's proven himself in every environment.
    
    **🏆 The Verdict:** This is where individual preferences matter. Do you value loyalty and single-club mastery 
    (Messi) or versatility and multi-league conquest (Ronaldo)? Both approaches to club football are equally valid 
    paths to greatness.
    """)

if __name__ == "__main__":
    show()