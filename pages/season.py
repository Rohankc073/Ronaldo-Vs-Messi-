import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the season-by-season performance analysis page"""
    st.markdown('<h1 class="section-header">📅 SEASON-BY-SEASON PERFORMANCE</h1>', unsafe_allow_html=True)
    
    # Page introduction
    st.markdown("""
    **Track the incredible journey season by season.** From their breakthrough years to record-breaking campaigns, 
    witness how Messi and Ronaldo evolved, peaked, and maintained excellence across two decades. Every season tells 
    a story of growth, adaptation, and relentless pursuit of greatness.
    """)
    
    # Create comprehensive season data (Complete careers 2003-2024)
    seasons_data = {
        'Season': ['2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11', '2011-12', 
                  '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', 
                  '2021-22', '2022-23', '2023-24'],
        'Messi_Age': [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
        'Ronaldo_Age': [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
        'Messi_Club': ['Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 
                      'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 
                      'Barcelona', 'Barcelona', 'Barcelona', 'Barcelona', 'PSG', 'PSG', 'Inter Miami'],
        'Ronaldo_Club': ['Sporting', 'Man United', 'Man United', 'Man United', 'Man United', 'Real Madrid', 
                        'Real Madrid', 'Real Madrid', 'Real Madrid', 'Real Madrid', 'Real Madrid', 'Real Madrid', 
                        'Real Madrid', 'Real Madrid', 'Juventus', 'Juventus', 'Juventus', 'Man United', 'Al Nassr', 'Al Nassr', 'Al Nassr'],
        'Messi_Goals': [1, 1, 8, 17, 16, 38, 47, 53, 73, 60, 41, 58, 54, 37, 51, 36, 31, 38, 11, 21, 25],
        'Ronaldo_Goals': [5, 9, 12, 23, 42, 33, 40, 60, 55, 51, 61, 48, 51, 42, 44, 37, 36, 24, 18, 14, 35],
        'Messi_Assists': [1, 0, 3, 4, 13, 18, 11, 24, 29, 16, 17, 22, 23, 13, 22, 14, 25, 14, 15, 20, 18],
        'Ronaldo_Assists': [1, 4, 6, 8, 8, 12, 13, 15, 12, 16, 22, 18, 16, 8, 8, 6, 4, 3, 2, 3, 12],
        'Messi_Apps': [9, 9, 25, 36, 40, 51, 53, 55, 60, 50, 46, 57, 49, 52, 50, 44, 44, 47, 34, 41, 37],
        'Ronaldo_Apps': [31, 50, 47, 53, 49, 35, 37, 54, 55, 44, 47, 54, 48, 46, 43, 46, 44, 39, 38, 36, 45],
        'Messi_Trophies': [0, 0, 2, 1, 0, 6, 2, 3, 3, 0, 1, 2, 2, 0, 2, 0, 0, 1, 0, 2, 1],
        'Ronaldo_Trophies': [0, 1, 2, 1, 2, 0, 1, 1, 2, 1, 4, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0]
    }
    
    seasons_df = pd.DataFrame(seasons_data)
    
    # Debug section - Show data verification
    with st.expander("🔍 Data Verification (Click to expand)", expanded=False):
        st.write(f"**Total seasons in dataset:** {len(seasons_df)}")
        st.write(f"**First season:** {seasons_df['Season'].iloc[0]}")
        st.write(f"**Last season:** {seasons_df['Season'].iloc[-1]}")
        st.write(f"**Messi's last season goals:** {seasons_df['Messi_Goals'].iloc[-1]} (2023-24)")
        st.write(f"**Ronaldo's last season goals:** {seasons_df['Ronaldo_Goals'].iloc[-1]} (2023-24)")
        
        # Show last 5 seasons
        st.write("**Last 5 seasons data:**")
        st.dataframe(seasons_df[['Season', 'Messi_Goals', 'Ronaldo_Goals', 'Messi_Club', 'Ronaldo_Club']].tail())
    
    # Season selector
    st.markdown('<h3 class="section-header">🎯 Season Selector & Overview</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        selected_season = st.selectbox(
            "Select a season to analyze in detail:",
            seasons_df['Season'].tolist(),
            index=8  # Default to 2011-12 (Messi's record season)
        )
    
    # Selected season analysis
    if selected_season:
        season_row = seasons_df[seasons_df['Season'] == selected_season].iloc[0]
        
        st.markdown(f'<h3 class="section-header">🔍 {selected_season} Season Deep Dive</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="player-card messi-card">
                <h3>🇦🇷 MESSI {selected_season}</h3>
                <h4>📊 Season Statistics</h4>
                <p><strong>Age:</strong> {season_row['Messi_Age']} years old</p>
                <p><strong>Club:</strong> {season_row['Messi_Club']}</p>
                <p><strong>Goals:</strong> {season_row['Messi_Goals']}</p>
                <p><strong>Assists:</strong> {season_row['Messi_Assists']}</p>
                <p><strong>Appearances:</strong> {season_row['Messi_Apps']}</p>
                <p><strong>Goals per Game:</strong> {season_row['Messi_Goals']/season_row['Messi_Apps']:.2f}</p>
                <p><strong>Goal Contributions:</strong> {season_row['Messi_Goals'] + season_row['Messi_Assists']}</p>
                <p><strong>Trophies Won:</strong> {season_row['Messi_Trophies']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="player-card ronaldo-card">
                <h3>🇵🇹 RONALDO {selected_season}</h3>
                <h4>📊 Season Statistics</h4>
                <p><strong>Age:</strong> {season_row['Ronaldo_Age']} years old</p>
                <p><strong>Club:</strong> {season_row['Ronaldo_Club']}</p>
                <p><strong>Goals:</strong> {season_row['Ronaldo_Goals']}</p>
                <p><strong>Assists:</strong> {season_row['Ronaldo_Assists']}</p>
                <p><strong>Appearances:</strong> {season_row['Ronaldo_Apps']}</p>
                <p><strong>Goals per Game:</strong> {season_row['Ronaldo_Goals']/season_row['Ronaldo_Apps']:.2f}</p>
                <p><strong>Goal Contributions:</strong> {season_row['Ronaldo_Goals'] + season_row['Ronaldo_Assists']}</p>
                <p><strong>Trophies Won:</strong> {season_row['Ronaldo_Trophies']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Career timeline visualization
    st.markdown('<h3 class="section-header">📈 Complete Career Timeline</h3>', unsafe_allow_html=True)
    
    fig = go.Figure()
    
    # Goals timeline - Make sure we have all 21 seasons
    fig.add_trace(go.Scatter(
        x=seasons_df['Season'],
        y=seasons_df['Messi_Goals'],
        mode='lines+markers',
        name='Messi Goals',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Messi %{x}</b><br>Goals: %{y}<br>Age: %{customdata}<br>Club: %{text}<extra></extra>',
        customdata=seasons_df['Messi_Age'],
        text=seasons_df['Messi_Club']
    ))
    
    fig.add_trace(go.Scatter(
        x=seasons_df['Season'],
        y=seasons_df['Ronaldo_Goals'],
        mode='lines+markers',
        name='Ronaldo Goals',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Ronaldo %{x}</b><br>Goals: %{y}<br>Age: %{customdata}<br>Club: %{text}<extra></extra>',
        customdata=seasons_df['Ronaldo_Age'],
        text=seasons_df['Ronaldo_Club']
    ))
    
    # Add major milestones with correct season references
    fig.add_annotation(x='2011-12', y=73, text="Messi's Record<br>73 Goals", arrowcolor="#4ECDC4", arrowwidth=2)
    fig.add_annotation(x='2013-14', y=61, text="Ronaldo's Peak<br>61 Goals", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x='2008-09', y=38, text="Messi's<br>Breakthrough", arrowcolor="#4ECDC4", arrowwidth=2)
    fig.add_annotation(x='2007-08', y=42, text="Ronaldo's<br>Breakout", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x='2021-22', y=11, text="Messi to PSG", arrowcolor="#4ECDC4", arrowwidth=1)
    fig.add_annotation(x='2023-24', y=25, text="Messi to Miami", arrowcolor="#4ECDC4", arrowwidth=1)
    fig.add_annotation(x='2018-19', y=44, text="Ronaldo to Juventus", arrowcolor="#FF6B6B", arrowwidth=1)
    fig.add_annotation(x='2023-24', y=35, text="Ronaldo to Al Nassr", arrowcolor="#FF6B6B", arrowwidth=1)
    
    fig.update_layout(
        title="⚽ Goals per Season Timeline (2003-2024)",
        xaxis_title="Season",
        yaxis_title="Goals Scored",
        height=500,
        template='plotly_white',
        xaxis_tickangle=-45,
        showlegend=True,
        # Ensure x-axis shows all seasons
        xaxis=dict(
            type='category',  # Treat as categorical data
            categoryorder='array',
            categoryarray=seasons_df['Season'].tolist()  # Explicit order
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Quick verification - show recent seasons data
    st.markdown("**Recent Seasons Data (Last 5 years):**")
    recent_data = seasons_df[['Season', 'Messi_Goals', 'Ronaldo_Goals', 'Messi_Club', 'Ronaldo_Club']].tail()
    st.dataframe(recent_data, use_container_width=True)
    
    # Peak seasons analysis
    st.markdown('<h3 class="section-header">🏔️ Peak Seasons Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi's top 5 seasons
        messi_peak = seasons_df.nlargest(5, 'Messi_Goals')[['Season', 'Messi_Age', 'Messi_Goals', 'Messi_Assists', 'Messi_Trophies']]
        
        st.markdown("### 🇦🇷 Messi's Top 5 Goal-Scoring Seasons:")
        
        for idx, row in messi_peak.iterrows():
            total_contrib = row['Messi_Goals'] + row['Messi_Assists']
            st.markdown(f"""
            **{row['Season']} (Age {row['Messi_Age']})**
            - Goals: {row['Messi_Goals']} | Assists: {row['Messi_Assists']} 
            - Total Contributions: {total_contrib}
            - Trophies: {row['Messi_Trophies']}
            """)
        
        # Peak season details
        st.markdown("""
        **🎯 Peak Analysis:**
        - **Best Season**: 2011-12 (73 goals + 29 assists = 102 contributions)
        - **Most Consistent**: 2015-16 (54 goals + 23 assists)
        - **Trophy Years**: 2008-09 (6 trophies), 2015-16 (2 trophies)
        """)
    
    with col2:
        # Ronaldo's top 5 seasons
        ronaldo_peak = seasons_df.nlargest(5, 'Ronaldo_Goals')[['Season', 'Ronaldo_Age', 'Ronaldo_Goals', 'Ronaldo_Assists', 'Ronaldo_Trophies']]
        
        st.markdown("### 🇵🇹 Ronaldo's Top 5 Goal-Scoring Seasons:")
        
        for idx, row in ronaldo_peak.iterrows():
            total_contrib = row['Ronaldo_Goals'] + row['Ronaldo_Assists']
            st.markdown(f"""
            **{row['Season']} (Age {row['Ronaldo_Age']})**
            - Goals: {row['Ronaldo_Goals']} | Assists: {row['Ronaldo_Assists']}
            - Total Contributions: {total_contrib}
            - Trophies: {row['Ronaldo_Trophies']}
            """)
        
        # Peak season details
        st.markdown("""
        **🎯 Peak Analysis:**
        - **Best Season**: 2013-14 (61 goals + 22 assists = 83 contributions)
        - **Most Balanced**: 2010-11 (60 goals + 15 assists)
        - **Trophy Years**: 2013-14 (4 trophies), 2016-17 (2 trophies)
        """)
    
    # Age-based performance analysis
    st.markdown('<h3 class="section-header">⏰ Performance by Age Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals by age scatter plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=seasons_df['Messi_Age'],
            y=seasons_df['Messi_Goals'],
            mode='markers+lines',
            name='Messi',
            marker=dict(size=10, color='#4ECDC4'),
            line=dict(color='#4ECDC4', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=seasons_df['Ronaldo_Age'],
            y=seasons_df['Ronaldo_Goals'],
            mode='markers+lines',
            name='Ronaldo',
            marker=dict(size=10, color='#FF6B6B'),
            line=dict(color='#FF6B6B', width=2)
        ))
        
        fig.update_layout(
            title="⚽ Goals by Age",
            xaxis_title="Age",
            yaxis_title="Goals per Season",
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Age performance insights
        st.markdown("""
        ### 📊 Age-Based Insights:
        
        **🇦🇷 Messi's Age Progression:**
        - **Peak Years**: 24-25 (73 and 60 goals)
        - **Consistency**: 27-31 (50+ goals regularly)
        - **Late Career**: 35+ (20+ goals in different league)
        - **Longevity**: High performance across 20 years
        
        **🇵🇹 Ronaldo's Age Progression:**
        - **Early Peak**: 22 (42 goals breakthrough)
        - **Prime Years**: 28-29 (61 and 48 goals)
        - **Consistency**: 24-33 (40+ goals for 10 years)
        - **Late Career**: 38+ (35+ goals in Saudi Arabia)
        
        **🔍 Key Differences:**
        - Messi: Higher peak but earlier decline
        - Ronaldo: More consistent across ages
        - Both: Remarkable longevity at top level
        """)
    
    # Assists and playmaking evolution
    st.markdown('<h3 class="section-header">🎨 Assists & Playmaking Evolution</h3>', unsafe_allow_html=True)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=seasons_df['Season'],
        y=seasons_df['Messi_Assists'],
        mode='lines+markers',
        name='Messi Assists',
        line=dict(color='#45B7D1', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Messi %{x}</b><br>Assists: %{y}<br>Club: %{text}<extra></extra>',
        text=seasons_df['Messi_Club']
    ))
    fig.add_trace(go.Scatter(
        x=seasons_df['Season'],
        y=seasons_df['Ronaldo_Assists'],
        mode='lines+markers',
        name='Ronaldo Assists',
        line=dict(color='#FFA07A', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Ronaldo %{x}</b><br>Assists: %{y}<br>Club: %{text}<extra></extra>',
        text=seasons_df['Ronaldo_Club']
    ))
    
    # Add annotations for playmaking peaks
    fig.add_annotation(x='2011-12', y=29, text="Messi's Assist Peak<br>29 Assists", arrowcolor="#45B7D1", arrowwidth=2)
    fig.add_annotation(x='2013-14', y=22, text="Ronaldo's Assist Peak<br>22 Assists", arrowcolor="#FFA07A", arrowwidth=2)
    fig.add_annotation(x='2022-23', y=20, text="Messi PSG<br>Playmaker", arrowcolor="#45B7D1", arrowwidth=1)
    
    fig.update_layout(
        title="🎯 Assists per Season Timeline (2003-2024)",
        xaxis_title="Season",
        yaxis_title="Assists",
        height=400,
        template='plotly_white',
        xaxis_tickangle=-45,
        xaxis=dict(
            type='category',
            categoryorder='array',
            categoryarray=seasons_df['Season'].tolist()
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Career phases analysis
    st.markdown('<h3 class="section-header">📊 Career Phases Breakdown</h3>', unsafe_allow_html=True)
    
    # Define career phases
    early_career = seasons_df[(seasons_df['Messi_Age'] >= 16) & (seasons_df['Messi_Age'] <= 21)]
    peak_career = seasons_df[(seasons_df['Messi_Age'] >= 22) & (seasons_df['Messi_Age'] <= 30)]
    late_career = seasons_df[seasons_df['Messi_Age'] >= 31]
    
    phases_analysis = {
        'Phase': ['Early Career (16-21)', 'Peak Career (22-30)', 'Late Career (31+)'],
        'Messi Avg Goals': [
            early_career['Messi_Goals'].mean(),
            peak_career['Messi_Goals'].mean(),
            late_career['Messi_Goals'].mean()
        ],
        'Ronaldo Avg Goals': [
            early_career['Ronaldo_Goals'].mean(),
            peak_career['Ronaldo_Goals'].mean(),
            late_career['Ronaldo_Goals'].mean()
        ],
        'Messi Avg Assists': [
            early_career['Messi_Assists'].mean(),
            peak_career['Messi_Assists'].mean(),
            late_career['Messi_Assists'].mean()
        ],
        'Ronaldo Avg Assists': [
            early_career['Ronaldo_Assists'].mean(),
            peak_career['Ronaldo_Assists'].mean(),
            late_career['Ronaldo_Assists'].mean()
        ]
    }
    
    phases_df = pd.DataFrame(phases_analysis)
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('⚽ Average Goals by Career Phase', '🎯 Average Assists by Career Phase')
    )
    
    # Goals by phase
    fig.add_trace(
        go.Bar(x=phases_df['Phase'], y=phases_df['Messi Avg Goals'], name='Messi Goals', marker_color='#4ECDC4'),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(x=phases_df['Phase'], y=phases_df['Ronaldo Avg Goals'], name='Ronaldo Goals', marker_color='#FF6B6B'),
        row=1, col=1
    )
    
    # Assists by phase
    fig.add_trace(
        go.Bar(x=phases_df['Phase'], y=phases_df['Messi Avg Assists'], name='Messi Assists', marker_color='#45B7D1', showlegend=False),
        row=1, col=2
    )
    fig.add_trace(
        go.Bar(x=phases_df['Phase'], y=phases_df['Ronaldo Avg Assists'], name='Ronaldo Assists', marker_color='#FFA07A', showlegend=False),
        row=1, col=2
    )
    
    fig.update_layout(height=400, title_text="📊 Career Phases Performance Analysis")
    st.plotly_chart(fig, use_container_width=True)
    
    # Season statistics table
    st.markdown('<h3 class="section-header">📋 Complete Season-by-Season Statistics</h3>', unsafe_allow_html=True)
    
    # Create display dataframe
    display_df = seasons_df.copy()
    display_df['Messi G+A'] = display_df['Messi_Goals'] + display_df['Messi_Assists']
    display_df['Ronaldo G+A'] = display_df['Ronaldo_Goals'] + display_df['Ronaldo_Assists']
    display_df['Messi GPG'] = (display_df['Messi_Goals'] / display_df['Messi_Apps']).round(2)
    display_df['Ronaldo GPG'] = (display_df['Ronaldo_Goals'] / display_df['Ronaldo_Apps']).round(2)
    
    # Select columns for display
    table_df = display_df[[
        'Season', 'Messi_Age', 'Ronaldo_Age', 'Messi_Club', 'Ronaldo_Club',
        'Messi_Goals', 'Ronaldo_Goals', 'Messi_Assists', 'Ronaldo_Assists',
        'Messi G+A', 'Ronaldo G+A', 'Messi GPG', 'Ronaldo GPG', 'Messi_Trophies', 'Ronaldo_Trophies'
    ]]
    
    # Rename columns for better display
    table_df.columns = [
        'Season', 'Messi Age', 'Ronaldo Age', 'Messi Club', 'Ronaldo Club',
        'Messi Goals', 'Ronaldo Goals', 'Messi Assists', 'Ronaldo Assists',
        'Messi G+A', 'Ronaldo G+A', 'Messi G/G', 'Ronaldo G/G', 'Messi Trophies', 'Ronaldo Trophies'
    ]
    
    st.dataframe(table_df, use_container_width=True, height=600)
    
    # Season highlights and milestones
    st.markdown('<h3 class="section-header">🌟 Season Highlights & Milestones</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Season Milestones:
        
        **🏆 Record-Breaking Seasons:**
        - **2011-12**: 73 goals (All-time single season record)
        - **2011-12**: 91 calendar year goals (World record)
        - **2018-19**: 51 goals at age 31 (Late career peak)
        
        **🎯 Breakthrough Moments:**
        - **2008-09**: First 30+ goal season (38 goals)
        - **2009-10**: First 40+ goal season (47 goals)
        - **2010-11**: First 50+ goal season (53 goals)
        
        **📈 Evolution Highlights:**
        - **Early**: Gradual development (1-17 goals)
        - **Peak**: Incredible consistency (37-73 goals)
        - **Adaptation**: New leagues success (11-25 goals)
        
        **🏅 Trophy Seasons:**
        - **2008-09**: 6 trophies (Treble + more)
        - **2015-16**: Treble season
        - **2022-23**: World Cup year impact
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Season Milestones:
        
        **🏆 Record-Breaking Seasons:**
        - **2013-14**: 61 goals (Personal best)
        - **2014-15**: 61 goals (Consistency peak)
        - **2007-08**: 42 goals (Breakthrough season)
        
        **🎯 Breakthrough Moments:**
        - **2006-07**: First 20+ goal season (23 goals)
        - **2007-08**: First 40+ goal season (42 goals)
        - **2009-10**: Real Madrid adaptation (40 goals)
        
        **📈 Evolution Highlights:**
        - **Early**: Rapid development (5-42 goals)
        - **Peak**: Machine-like consistency (40-61 goals)
        - **Adaptation**: Success across leagues
        
        **🏅 Trophy Seasons:**
        - **2013-14**: 4 trophies (La Décima)
        - **2016-17**: Champions League threepeat
        - **2018-19**: Juventus adaptation
        """)
    
    # Career summary
    st.markdown('<h3 class="section-header">🏁 Season-by-Season Legacy</h3>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>📅 Two Decades of Excellence</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI'S CAREER JOURNEY</h3>
                <p><strong>21 Seasons</strong> of professional football</p>
                <p><strong>Peak:</strong> 2011-12 (73 goals, 29 assists)</p>
                <p><strong>Most Consistent:</strong> 2010-2019 decade</p>
                <p><strong>Longevity:</strong> 20+ goals at age 36</p>
                <p><strong>Adaptation:</strong> Success in 3 different leagues</p>
            </div>
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO'S CAREER JOURNEY</h3>
                <p><strong>21 Seasons</strong> of professional football</p>
                <p><strong>Peak:</strong> 2013-14 (61 goals, 22 assists)</p>
                <p><strong>Most Consistent:</strong> 2007-2018 period</p>
                <p><strong>Longevity:</strong> 35+ goals at age 38</p>
                <p><strong>Versatility:</strong> Success in 5 different leagues</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Season Legacy:</strong> 🤝 <strong>BOTH LEGENDS</strong> - Different peaks, sustained excellence!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final insights
    st.markdown("""
    ---
    ### 🌟 Season-by-Season Insights
    
    **📈 Career Trajectories:** Both players show remarkably different but equally impressive career arcs. Messi's 
    journey features a gradual rise to an incredible peak, while Ronaldo shows more consistent excellence across 
    a longer period with multiple peaks.
    
    **🏔️ Peak Performance:** Messi's 2011-12 season with 73 goals stands as potentially the greatest individual 
    season in football history. Ronaldo's peak was more sustained, with multiple 50+ goal seasons.
    
    **⏰ Longevity:** Both have maintained elite performance well into their 30s, adapting their games and proving 
    that class is permanent. Their ability to perform at the highest level across two decades is unprecedented.
    
    **🔄 Adaptation:** The season-by-season analysis shows how both players evolved their games - Messi becoming 
    more of a playmaker in later years, Ronaldo maintaining goal-scoring prowess across different leagues.
    
    **🏆 Legacy:** Together, they've defined what excellence looks like across 21 seasons, inspiring generations 
    and setting standards that may never be matched.
    """)

if __name__ == "__main__":
    show()