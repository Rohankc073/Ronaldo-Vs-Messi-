import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def show():
    """Display season-by-season performance analysis with clutch design theme"""
    # Custom CSS for Times New Roman font
    st.markdown("""
    <style>
    .main {
        font-family: 'Times New Roman', serif;
    }
    .section-header {
        font-family: 'Times New Roman', serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.set_page_config(page_title="Season Performance", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: {RONALDO_COLOR}; font-family: 'Times New Roman', serif;">
    📅 SEASON-BY-SEASON PERFORMANCE ANALYSIS
    </h1>
    """, unsafe_allow_html=True)
    
    # Create comprehensive season data
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
    
    # Quick stats cards with custom design
    st.markdown("## 📊 Career Overview")
    
    # Custom metrics cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        messi_peak = seasons_df['Messi_Goals'].max()
        ronaldo_peak = seasons_df['Ronaldo_Goals'].max()
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">⚽</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Peak Season</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                73 vs 61
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +12</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        messi_total = seasons_df['Messi_Goals'].sum()
        ronaldo_total = seasons_df['Ronaldo_Goals'].sum()
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Total Goals</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_total} vs {ronaldo_total}
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +{ronaldo_total-messi_total}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        messi_assists = seasons_df['Messi_Assists'].sum()
        ronaldo_assists = seasons_df['Ronaldo_Assists'].sum()
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🅰️</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Total Assists</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_assists} vs {ronaldo_assists}
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +{messi_assists-ronaldo_assists}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        messi_seasons = len(seasons_df)
        ronaldo_seasons = len(seasons_df)
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid #FFD700;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">📅</div>
            <h5 style="color: #FFD700; margin: 0 0 8px 0;">Seasons</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                21 vs 21
            </div>
            <div style="
                background: #FFD700; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Equal</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        messi_trophies = seasons_df['Messi_Trophies'].sum()
        ronaldo_trophies = seasons_df['Ronaldo_Trophies'].sum()
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Trophies</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_trophies} vs {ronaldo_trophies}
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +{messi_trophies-ronaldo_trophies}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive Season Selector
    st.markdown('## 🎯 Season Explorer')
    
    selected_season = st.selectbox(
        "Select a season for detailed analysis:",
        seasons_df['Season'].tolist(),
        index=8  # Default to 2011-12 (Messi's record season)
    )
    
    # Selected Season Dashboard
    if selected_season:
        season_row = seasons_df[seasons_df['Season'] == selected_season].iloc[0]
        
        st.markdown(f'### 🔍 {selected_season} Season Dashboard')
        
        # Season comparison cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {MESSI_COLOR} 0%, #5a9bd4 100%);
                color: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
                text-align: center;
                font-family: 'Times New Roman', serif;
            ">
                <h3 style="margin: 0;">🇦🇷 MESSI ({season_row['Messi_Age']} years old)</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                    <div><strong style="font-size: 2rem;">{season_row['Messi_Goals']}</strong><br><small>Goals</small></div>
                    <div><strong style="font-size: 2rem;">{season_row['Messi_Assists']}</strong><br><small>Assists</small></div>
                    <div><strong style="font-size: 2rem;">{season_row['Messi_Apps']}</strong><br><small>Games</small></div>
                    <div><strong style="font-size: 2rem;">{season_row['Messi_Trophies']}</strong><br><small>Trophies</small></div>
                </div>
                <p style="margin: 0; opacity: 0.9; font-style: italic;">Club: {season_row['Messi_Club']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            messi_gpg = season_row['Messi_Goals']/season_row['Messi_Apps']
            ronaldo_gpg = season_row['Ronaldo_Goals']/season_row['Ronaldo_Apps']
            messi_contrib = season_row['Messi_Goals'] + season_row['Messi_Assists']
            ronaldo_contrib = season_row['Ronaldo_Goals'] + season_row['Ronaldo_Assists']
            
            st.markdown(f"""
            <div style="
                background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
                backdrop-filter: blur(20px);
                border-radius: 20px;
                padding: 25px;
                text-align: center;
                border: 2px solid #FFD700;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                font-family: 'Times New Roman', serif;
                margin: 10px 0;
            ">
                <h3 style="color: #FFD700; margin: 0 0 20px 0;">⚖️ HEAD-TO-HEAD</h3>
                <div style="margin: 15px 0;">
                    <div style="font-size: 1.1rem; margin: 10px 0;"><strong>Goals per Game:</strong></div>
                    <div style="font-size: 1.5rem; color: #FFD700;">{messi_gpg:.2f} vs {ronaldo_gpg:.2f}</div>
                </div>
                <div style="margin: 15px 0;">
                    <div style="font-size: 1.1rem; margin: 10px 0;"><strong>Total Contributions:</strong></div>
                    <div style="font-size: 1.5rem; color: #FFD700;">{messi_contrib} vs {ronaldo_contrib}</div>
                </div>
                <div style="margin: 15px 0;">
                    <div style="font-size: 1.1rem; margin: 10px 0;"><strong>Trophies:</strong></div>
                    <div style="font-size: 1.5rem; color: #FFD700;">{season_row['Messi_Trophies']} vs {season_row['Ronaldo_Trophies']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {RONALDO_COLOR} 0%, #e02525 100%);
                color: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
                text-align: center;
                font-family: 'Times New Roman', serif;
            ">
                <h3 style="margin: 0;">🇵🇹 RONALDO ({season_row['Ronaldo_Age']} years old)</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                    <div><strong style="font-size: 2rem;">{season_row['Ronaldo_Goals']}</strong><br><small>Goals</small></div>
                    <div><strong style="font-size: 2rem;">{season_row['Ronaldo_Assists']}</strong><br><small>Assists</small></div>
                    <div><strong style="font-size: 2rem;">{season_row['Ronaldo_Apps']}</strong><br><small>Games</small></div>
                    <div><strong style="font-size: 2rem;">{season_row['Ronaldo_Trophies']}</strong><br><small>Trophies</small></div>
                </div>
                <p style="margin: 0; opacity: 0.9; font-style: italic;">Club: {season_row['Ronaldo_Club']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Career Timeline
    st.markdown('## 📈 Complete Career Timeline')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals timeline
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=seasons_df['Season'],
            y=seasons_df['Messi_Goals'],
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=10),
            fill='tonexty'
        ))
        fig.add_trace(go.Scatter(
            x=seasons_df['Season'],
            y=seasons_df['Ronaldo_Goals'],
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=10),
            fill='tozeroy'
        ))
        
        fig.update_layout(
            title="⚽ Goals per Season Timeline",
            xaxis_title="Season",
            yaxis_title="Goals",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        fig.update_xaxes(tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Assists timeline
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=seasons_df['Season'],
            y=seasons_df['Messi_Assists'],
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=10)
        ))
        fig.add_trace(go.Scatter(
            x=seasons_df['Season'],
            y=seasons_df['Ronaldo_Assists'],
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="🎯 Assists per Season Timeline",
            xaxis_title="Season",
            yaxis_title="Assists",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        fig.update_xaxes(tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    # Peak Seasons Analysis
    st.markdown('## 🔥 Peak Seasons Heatmap')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi performance matrix
        performance_metrics = ['Goals', 'Assists', 'G+A', 'Goals/Game', 'Trophies']
        messi_matrix = [
            seasons_df['Messi_Goals'].tolist(),
            seasons_df['Messi_Assists'].tolist(),
            (seasons_df['Messi_Goals'] + seasons_df['Messi_Assists']).tolist(),
            (seasons_df['Messi_Goals'] / seasons_df['Messi_Apps']).tolist(),
            seasons_df['Messi_Trophies'].tolist()
        ]
        
        fig = go.Figure(data=go.Heatmap(
            z=messi_matrix,
            x=seasons_df['Season'],
            y=performance_metrics,
            colorscale='Blues',
            hoverongaps=False
        ))
        fig.update_layout(
            title="🇦🇷 Messi Performance Heatmap",
            height=400,
            xaxis_tickangle=-45,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Ronaldo performance matrix
        ronaldo_matrix = [
            seasons_df['Ronaldo_Goals'].tolist(),
            seasons_df['Ronaldo_Assists'].tolist(),
            (seasons_df['Ronaldo_Goals'] + seasons_df['Ronaldo_Assists']).tolist(),
            (seasons_df['Ronaldo_Goals'] / seasons_df['Ronaldo_Apps']).tolist(),
            seasons_df['Ronaldo_Trophies'].tolist()
        ]
        
        fig = go.Figure(data=go.Heatmap(
            z=ronaldo_matrix,
            x=seasons_df['Season'],
            y=performance_metrics,
            colorscale='Reds',
            hoverongaps=False
        ))
        fig.update_layout(
            title="🇵🇹 Ronaldo Performance Heatmap",
            height=400,
            xaxis_tickangle=-45,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Age Performance Analysis
    st.markdown('## ⏰ Performance by Age')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals by age bubble chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=seasons_df['Messi_Age'],
            y=seasons_df['Messi_Goals'],
            mode='markers',
            marker=dict(
                size=seasons_df['Messi_Assists']*2,
                sizemode='diameter',
                sizeref=2,
                color=MESSI_COLOR,
                opacity=0.7,
                line=dict(width=2, color='white')
            ),
            name='Messi',
            text=seasons_df['Season'],
            hovertemplate='<b>%{text}</b><br>Age: %{x}<br>Goals: %{y}<br>Assists: %{marker.size}<extra></extra>'
        ))
        fig.add_trace(go.Scatter(
            x=seasons_df['Ronaldo_Age'],
            y=seasons_df['Ronaldo_Goals'],
            mode='markers',
            marker=dict(
                size=seasons_df['Ronaldo_Assists']*2,
                sizemode='diameter',
                sizeref=2,
                color=RONALDO_COLOR,
                opacity=0.7,
                line=dict(width=2, color='white')
            ),
            name='Ronaldo',
            text=seasons_df['Season'],
            hovertemplate='<b>%{text}</b><br>Age: %{x}<br>Goals: %{y}<br>Assists: %{marker.size}<extra></extra>'
        ))
        fig.update_layout(
            title="⚽ Goals by Age (Bubble size = Assists)",
            xaxis_title="Age",
            yaxis_title="Goals",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Career phases performance
        early_career = seasons_df[(seasons_df['Messi_Age'] >= 16) & (seasons_df['Messi_Age'] <= 21)]
        peak_career = seasons_df[(seasons_df['Messi_Age'] >= 22) & (seasons_df['Messi_Age'] <= 30)]
        late_career = seasons_df[seasons_df['Messi_Age'] >= 31]
        
        phases = ['Early (16-21)', 'Peak (22-30)', 'Late (31+)']
        messi_avg_goals = [
            early_career['Messi_Goals'].mean(),
            peak_career['Messi_Goals'].mean(),
            late_career['Messi_Goals'].mean()
        ]
        ronaldo_avg_goals = [
            early_career['Ronaldo_Goals'].mean(),
            peak_career['Ronaldo_Goals'].mean(),
            late_career['Ronaldo_Goals'].mean()
        ]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=phases,
            y=messi_avg_goals,
            marker_color=MESSI_COLOR,
            text=[f"{x:.1f}" for x in messi_avg_goals],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=phases,
            y=ronaldo_avg_goals,
            marker_color=RONALDO_COLOR,
            text=[f"{x:.1f}" for x in ronaldo_avg_goals],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(
            title="📊 Average Goals by Career Phase",
            yaxis_title="Average Goals",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Top 5 Seasons Comparison
    st.markdown('## 🏔️ Top 5 Seasons')
    
    col1, col2 = st.columns(2)
    
    with col1:
        messi_top5 = seasons_df.nlargest(5, 'Messi_Goals')[['Season', 'Messi_Goals', 'Messi_Assists', 'Messi_Age']]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Goals',
            x=messi_top5['Season'],
            y=messi_top5['Messi_Goals'],
            marker_color=MESSI_COLOR,
            text=messi_top5['Messi_Goals'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Assists',
            x=messi_top5['Season'],
            y=messi_top5['Messi_Assists'],
            marker_color='#45B7D1',
            text=messi_top5['Messi_Assists'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(
            title="🇦🇷 Messi's Top 5 Goal Seasons",
            barmode='stack',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        ronaldo_top5 = seasons_df.nlargest(5, 'Ronaldo_Goals')[['Season', 'Ronaldo_Goals', 'Ronaldo_Assists', 'Ronaldo_Age']]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Goals',
            x=ronaldo_top5['Season'],
            y=ronaldo_top5['Ronaldo_Goals'],
            marker_color=RONALDO_COLOR,
            text=ronaldo_top5['Ronaldo_Goals'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Assists',
            x=ronaldo_top5['Season'],
            y=ronaldo_top5['Ronaldo_Assists'],
            marker_color='#FFA07A',
            text=ronaldo_top5['Ronaldo_Assists'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(
            title="🇵🇹 Ronaldo's Top 5 Goal Seasons",
            barmode='stack',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Trophy Timeline
    st.markdown('## 🏆 Trophy Timeline')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Messi Trophies',
        x=seasons_df['Season'],
        y=seasons_df['Messi_Trophies'],
        marker_color=MESSI_COLOR,
        text=seasons_df['Messi_Trophies'],
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    fig.add_trace(go.Bar(
        name='Ronaldo Trophies',
        x=seasons_df['Season'],
        y=seasons_df['Ronaldo_Trophies'],
        marker_color=RONALDO_COLOR,
        text=seasons_df['Ronaldo_Trophies'],
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    
    fig.update_layout(
        title="🏅 Trophies Won per Season",
        barmode='group',
        height=400,
        template='plotly_white',
        xaxis_tickangle=-45,
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Complete Season Statistics Table
    st.markdown('## 📋 Complete Season-by-Season Statistics')
    
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
    
    # Summary metrics with custom design
    st.markdown('## 🏁 Season Legacy Championship')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🔥</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Peak Season</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                MESSI
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">73 goals 2011-12</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">📊</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Consistency</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                RONALDO
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">14 seasons 40+ goals</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🎯</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Playmaking</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                MESSI
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">+119 more assists</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid #FFD700;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">👑</div>
            <h4 style="color: #FFD700; margin: 0 0 10px 0;">LONGEVITY KINGS</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                BOTH
            </div>
            <div style="
                background: #FFD700; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">21 epic seasons</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()