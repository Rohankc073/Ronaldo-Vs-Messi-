import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def show():
    """Display visual international career analysis"""
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
    
    st.set_page_config(page_title="International Career", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: {MESSI_COLOR}; font-family: 'Times New Roman', serif;">
    🌍 INTERNATIONAL CAREER ANALYSIS
    </h1>
    """, unsafe_allow_html=True)
    
    # Quick comparison cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {MESSI_COLOR}, #5a9bd4);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin: 1rem 0;
            font-family: 'Times New Roman', serif;
        ">
            <h2>🇦🇷 MESSI</h2>
            <h3>World Cup Champion</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                <div><strong>183</strong><br>Matches</div>
                <div><strong>108</strong><br>Goals</div>
                <div><strong>56</strong><br>Assists</div>
                <div><strong>2</strong><br>Trophies</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {RONALDO_COLOR}, #e02525);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin: 1rem 0;
            font-family: 'Times New Roman', serif;
        ">
            <h2>🇵🇹 RONALDO</h2>
            <h3>Record Goal Scorer</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                <div><strong>206</strong><br>Matches</div>
                <div><strong>130</strong><br>Goals</div>
                <div><strong>43</strong><br>Assists</div>
                <div><strong>2</strong><br>Trophies</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Key metrics with custom design
    st.markdown("## 📊 International Performance Overview")
    
    # Custom metrics cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🥅</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Total Goals</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                130 vs 108
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +22</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Assists</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                56 vs 43
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +13</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
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
            <div style="font-size: 2rem; margin-bottom: 10px;">⚽</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Goals/Game</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                0.63 vs 0.59
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +0.04</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
            <h5 style="color: #FFD700; margin: 0 0 8px 0;">Major Trophies</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                2 vs 2
            </div>
            <div style="
                background: #FFD700; 
                color: #333; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Tied</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🌍</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">World Cup</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                1 vs 0
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +1</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main comparison charts
    st.markdown('## 📊 International Performance Comparison')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals and assists comparison
        categories = ['Goals', 'Assists', 'Matches', 'Hat-tricks']
        messi_stats = [108, 56, 183, 3]
        ronaldo_stats = [130, 43, 206, 10]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_stats,
            marker_color=MESSI_COLOR,
            text=messi_stats,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_stats,
            marker_color=RONALDO_COLOR,
            text=ronaldo_stats,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="International Statistics",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Performance radar chart
        categories = ['Goals/Game', 'Assists/Game', 'Tournament Impact', 'Leadership', 'Clutch Factor']
        messi_radar = [85, 90, 95, 85, 92]
        ronaldo_radar = [90, 70, 85, 95, 88]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_radar,
            theta=categories,
            fill='toself',
            name='Messi',
            fillcolor=f'rgba(117, 170, 219, 0.3)',
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_radar,
            theta=categories,
            fill='toself',
            name='Ronaldo',
            fillcolor=f'rgba(255, 45, 45, 0.3)',
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Performance Radar",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Tournament performance
    st.markdown('## 🏆 Tournament Performance')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # World Cup performance
        wc_categories = ['Goals', 'Assists', 'Matches', 'Tournaments']
        messi_wc = [13, 8, 26, 5]
        ronaldo_wc = [8, 2, 22, 5]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=wc_categories,
            y=messi_wc,
            marker_color=MESSI_COLOR,
            text=messi_wc,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=wc_categories,
            y=ronaldo_wc,
            marker_color=RONALDO_COLOR,
            text=ronaldo_wc,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="World Cup Performance",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Continental tournaments
        continental_stats = ['Copa América (Messi)', 'Euro (Ronaldo)']
        goals = [13, 14]
        tournaments = [7, 6]
        
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=['Continental Goals', 'Continental Tournaments']
        )
        
        fig.add_trace(go.Bar(
            x=continental_stats,
            y=goals,
            marker_color=[MESSI_COLOR, RONALDO_COLOR],
            text=goals,
            textposition='auto',
            name='Goals',
            textfont=dict(family='Times New Roman')
        ), row=1, col=1)
        
        fig.add_trace(go.Bar(
            x=continental_stats,
            y=tournaments,
            marker_color=[MESSI_COLOR, RONALDO_COLOR],
            text=tournaments,
            textposition='auto',
            name='Tournaments',
            textfont=dict(family='Times New Roman')
        ), row=2, col=1)
        
        fig.update_layout(
            title="Continental Performance",
            height=400,
            template='plotly_white',
            showlegend=False,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Trophy comparison
        trophies = ['World Cup', 'Copa América', 'Euro', 'Nations League']
        messi_trophies = [1, 1, 0, 0]
        ronaldo_trophies = [0, 0, 1, 1]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=trophies,
            y=messi_trophies,
            marker_color=MESSI_COLOR,
            text=messi_trophies,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=trophies,
            y=ronaldo_trophies,
            marker_color=RONALDO_COLOR,
            text=ronaldo_trophies,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Major Trophies Won",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Career timeline
    st.markdown('## 📈 International Career Timeline')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals by year
        years = list(range(2005, 2024))
        messi_goals = [0, 2, 6, 4, 5, 7, 12, 5, 8, 11, 5, 6, 4, 7, 9, 4, 1, 7, 8]
        ronaldo_goals = [2, 7, 8, 6, 5, 7, 8, 11, 5, 9, 7, 4, 3, 8, 2, 5, 14, 8, 1]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=messi_goals,
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=ronaldo_goals,
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=3),
            marker=dict(size=8)
        ))
        
        # Add trophy annotations
        fig.add_annotation(x=2022, y=8, text="🏆 WC Win", arrowcolor=MESSI_COLOR, font=dict(family='Times New Roman'))
        fig.add_annotation(x=2016, y=14, text="🏆 Euro Win", arrowcolor=RONALDO_COLOR, font=dict(family='Times New Roman'))
        fig.add_annotation(x=2021, y=4, text="🏆 Copa Win", arrowcolor=MESSI_COLOR, font=dict(family='Times New Roman'))
        
        fig.update_layout(
            title="International Goals by Year",
            xaxis_title="Year",
            yaxis_title="Goals",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Cumulative career stats
        years_career = [2005, 2010, 2015, 2020, 2023]
        messi_cumulative = [6, 17, 45, 70, 108]
        ronaldo_cumulative = [9, 26, 55, 99, 130]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years_career,
            y=messi_cumulative,
            mode='lines+markers',
            name='Messi Career Goals',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=12),
            fill='tonexty'
        ))
        fig.add_trace(go.Scatter(
            x=years_career,
            y=ronaldo_cumulative,
            mode='lines+markers',
            name='Ronaldo Career Goals',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=12)
        ))
        
        fig.update_layout(
            title="Cumulative International Goals",
            xaxis_title="Year",
            yaxis_title="Total Goals",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Efficiency analysis
    st.markdown('## ⚡ Efficiency Analysis')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals per game by tournament
        tournaments = ['World Cup', 'Continental', 'Qualifiers', 'Friendlies']
        messi_gpg = [0.50, 0.65, 0.72, 0.45]
        ronaldo_gpg = [0.36, 0.70, 0.78, 0.52]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=tournaments,
            y=messi_gpg,
            mode='lines+markers+text',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=15),
            text=[f'{x:.2f}' for x in messi_gpg],
            textposition='top center',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Scatter(
            x=tournaments,
            y=ronaldo_gpg,
            mode='lines+markers+text',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=15),
            text=[f'{x:.2f}' for x in ronaldo_gpg],
            textposition='top center',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Goals per Game by Tournament Type",
            yaxis_title="Goals per Game",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Age performance
        age_groups = ['Under 25', '25-30', '30-35', 'Over 35']
        messi_age_goals = [25, 45, 28, 10]
        ronaldo_age_goals = [28, 52, 35, 15]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=age_groups,
            y=messi_age_goals,
            marker_color=MESSI_COLOR,
            text=messi_age_goals,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=age_groups,
            y=ronaldo_age_goals,
            marker_color=RONALDO_COLOR,
            text=ronaldo_age_goals,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Goals by Age Group",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Head-to-head comparison table
    st.markdown('## 📋 Complete International Comparison')
    
    comparison_data = {
        'Metric': ['Debut Age', 'Career Years', 'Total Caps', 'Goals', 'Assists', 'Goals/Game', 
                  'Hat-tricks', 'Major Tournament Goals', 'Finals', 'Trophies', 'Individual Awards'],
        'Messi': [18, 19, 183, 108, 56, 0.59, 3, 26, 6, 2, 3],
        'Ronaldo': [18, 20, 206, 130, 43, 0.63, 10, 22, 4, 2, 2],
        'Winner': ['🤝', '🇵🇹', '🇵🇹', '🇵🇹', '🇦🇷', '🇵🇹', '🇵🇹', '🇦🇷', '🇦🇷', '🤝', '🇦🇷']
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df, use_container_width=True, height=400)
    
    # Final verdict visualization
    st.markdown('## 🏆 International Career Verdict')
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Category winners
        categories = ['Goals', 'Assists', 'Efficiency', 'World Cup', 'Tournaments', 'Individual Awards']
        messi_wins = [0, 1, 0, 1, 1, 1]  # 4 categories
        ronaldo_wins = [1, 0, 1, 0, 0, 0]  # 2 categories
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi Wins',
            x=categories,
            y=messi_wins,
            marker_color=MESSI_COLOR,
            text=['❌', '✅', '❌', '✅', '✅', '✅'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo Wins',
            x=categories,
            y=ronaldo_wins,
            marker_color=RONALDO_COLOR,
            text=['✅', '❌', '✅', '❌', '❌', '❌'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Category Winners",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Overall winner pie
        winners = ['Messi Advantages', 'Ronaldo Advantages']
        win_counts = [4, 2]
        
        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=winners,
            values=win_counts,
            marker_colors=[MESSI_COLOR, RONALDO_COLOR],
            textinfo='label+percent',
            textfont=dict(size=16, family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Overall Advantage",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Summary metrics with custom design
    st.markdown('## 🎯 International Career Summary')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🥅</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Goal Scorer</h4>
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
            ">+22 goals</div>
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
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🌍</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">World Cup</h4>
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
            ">1 trophy</div>
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
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Playmaker</h4>
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
            ">+13 assists</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏆</div>
            <h4 style="color: #FFD700; margin: 0 0 10px 0;">INTERNATIONAL WINNER</h4>
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
            ">4/6 categories</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()