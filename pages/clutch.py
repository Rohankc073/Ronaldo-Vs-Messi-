import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def show():
    """Display visual clutch performance analysis"""
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
    
    st.set_page_config(page_title="Clutch Performance", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: {RONALDO_COLOR}; font-family: 'Times New Roman', serif;">
    🔥 CLUTCH PERFORMANCE ANALYSIS
    </h1>
    """, unsafe_allow_html=True)
    
    # Quick stats cards with custom design
    st.markdown("## 📊 Clutch Performance Overview")
    
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
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Final Goals</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                26 vs 22
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +4</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">⏰</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Last Minute</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                31 vs 23
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +8</div>
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Penalties</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                84% vs 78%
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +6%</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🏅</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Big Games</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                95 vs 89
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +6</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">CL Finals</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                5 vs 4
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +1</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main clutch comparison
    st.markdown('## 🔥 Clutch Performance Comparison')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Clutch categories bar chart
        categories = ['Final Goals', 'Penalty Goals', 'Last Minute', 'Big Games', 'Comebacks']
        messi_stats = [26, 7, 23, 89, 45]
        ronaldo_stats = [22, 15, 31, 95, 52]
        
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
            title="Clutch Performance Categories",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Clutch radar chart
        radar_categories = ['Finals', 'Penalties', 'Last Minute', 'Big Games', 'Mental Strength']
        messi_radar = [90, 75, 85, 88, 85]
        ronaldo_radar = [85, 95, 95, 95, 98]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_radar,
            theta=radar_categories,
            fill='toself',
            name='Messi',
            fillcolor=f'rgba(117, 170, 219, 0.3)',
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_radar,
            theta=radar_categories,
            fill='toself',
            name='Ronaldo',
            fillcolor=f'rgba(255, 45, 45, 0.3)',
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Clutch Performance Radar",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Finals performance visualization
    st.markdown('## 🏆 Finals Performance')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Combined win rate comparison
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'pie'}, {'type': 'pie'}]],
            subplot_titles=['Messi: 70% Win Rate', 'Ronaldo: 78% Win Rate']
        )
        
        fig.add_trace(go.Pie(
            labels=['Wins', 'Losses'],
            values=[7, 3],
            marker_colors=[MESSI_COLOR, '#E8E8E8'],
            name='Messi',
            textfont=dict(family='Times New Roman')
        ), row=1, col=1)
        
        fig.add_trace(go.Pie(
            labels=['Wins', 'Losses'],
            values=[7, 2],
            marker_colors=[RONALDO_COLOR, '#E8E8E8'],
            name='Ronaldo',
            textfont=dict(family='Times New Roman')
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="Finals Win Rate", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Goals in finals by competition
        competitions = ['World Cup', 'Continental', 'Champions League', 'Domestic']
        messi_final_goals = [2, 8, 14, 2]
        ronaldo_final_goals = [0, 6, 12, 4]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=competitions,
            y=messi_final_goals,
            marker_color=MESSI_COLOR,
            text=messi_final_goals,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=competitions,
            y=ronaldo_final_goals,
            marker_color=RONALDO_COLOR,
            text=ronaldo_final_goals,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Final Goals by Competition",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Finals timeline
        years = [2006, 2009, 2011, 2014, 2015, 2016, 2017, 2018, 2021, 2022]
        messi_finals = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
        ronaldo_finals = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=np.cumsum(messi_finals),
            mode='lines+markers',
            name='Messi Finals Won',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=10)
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=np.cumsum(ronaldo_finals),
            mode='lines+markers',
            name='Ronaldo Finals Won',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Finals Won Over Time",
            xaxis_title="Year",
            yaxis_title="Cumulative Finals Won",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Penalty analysis
    st.markdown('## 🎯 Penalty Performance')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Penalty conversion rates
        situations = ['Regular', 'Shootout', 'Crucial', 'Finals']
        messi_penalty = [81, 60, 70, 75]
        ronaldo_penalty = [84, 85, 90, 88]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=situations,
            y=messi_penalty,
            mode='lines+markers+text',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=15),
            text=[f'{x}%' for x in messi_penalty],
            textposition='top center',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Scatter(
            x=situations,
            y=ronaldo_penalty,
            mode='lines+markers+text',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=15),
            text=[f'{x}%' for x in ronaldo_penalty],
            textposition='top center',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Penalty Conversion by Situation",
            yaxis_title="Success Rate %",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Penalty shootout records
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'pie'}, {'type': 'pie'}]],
            subplot_titles=['Messi Shootouts (4W-3L)', 'Ronaldo Shootouts (7W-2L)']
        )
        
        fig.add_trace(go.Pie(
            labels=['Wins', 'Losses'],
            values=[4, 3],
            marker_colors=[MESSI_COLOR, '#E8E8E8'],
            name='Messi',
            textfont=dict(family='Times New Roman')
        ), row=1, col=1)
        
        fig.add_trace(go.Pie(
            labels=['Wins', 'Losses'],
            values=[7, 2],
            marker_colors=[RONALDO_COLOR, '#E8E8E8'],
            name='Ronaldo',
            textfont=dict(family='Times New Roman')
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="Penalty Shootout Records", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    # Last minute and clutch timeline
    st.markdown('## ⏰ Last Minute & Career Trends')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Last minute goals by competition
        competitions = ['Champions League', 'League', 'International', 'Cups']
        messi_lastmin = [8, 12, 2, 1]
        ronaldo_lastmin = [12, 15, 3, 1]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=competitions,
            y=messi_lastmin,
            marker_color=MESSI_COLOR,
            text=messi_lastmin,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=competitions,
            y=ronaldo_lastmin,
            marker_color=RONALDO_COLOR,
            text=ronaldo_lastmin,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Last Minute Goals by Competition",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Clutch performance timeline
        years = list(range(2005, 2024))
        messi_clutch_trend = [6, 7, 8, 9, 7, 8, 5, 9, 8, 6, 7, 8, 9, 4, 7, 8, 10, 10, 7]
        ronaldo_clutch_trend = [7, 8, 8, 9, 10, 9, 8, 9, 10, 8, 9, 7, 8, 6, 7, 8, 7, 6, 7]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=messi_clutch_trend,
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=ronaldo_clutch_trend,
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Clutch Performance Over Career",
            xaxis_title="Year",
            yaxis_title="Clutch Rating (1-10)",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Pressure situations heatmap
    st.markdown('## 🌡️ Pressure Performance Heatmap')
    
    situations = ['Penalties', 'Free Kicks', 'Last Minute', 'Comebacks', 'Derby Games', 'Finals']
    players = ['Messi', 'Ronaldo']
    performance_matrix = [
        [78, 85, 85, 90, 95, 90],  # Messi
        [84, 80, 95, 95, 80, 85]   # Ronaldo
    ]
    
    fig = go.Figure(data=go.Heatmap(
        z=performance_matrix,
        x=situations,
        y=players,
        colorscale='RdYlBu_r',
        text=performance_matrix,
        texttemplate="%{text}",
        textfont={"size": 20, "family": "Times New Roman"},
        hoverongaps=False
    ))
    
    fig.update_layout(
        title="Clutch Performance Heatmap (Higher = Better)",
        height=350,
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Final comparison charts
    st.markdown('## 🏆 Final Comparison')
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Overall clutch scores
        categories = ['Penalties', 'Last Minute', 'Finals', 'Big Games', 'Mental Strength', 'Comebacks']
        messi_scores = [75, 85, 90, 88, 85, 90]
        ronaldo_scores = [95, 95, 85, 95, 98, 95]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_scores,
            marker_color=MESSI_COLOR,
            text=messi_scores,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_scores,
            marker_color=RONALDO_COLOR,
            text=ronaldo_scores,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Overall Clutch Comparison",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Winner pie chart
        winners = ['Ronaldo Wins', 'Messi Wins']
        win_counts = [5, 1]  # Ronaldo wins 5 categories, Messi wins 1
        
        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=winners,
            values=win_counts,
            marker_colors=[RONALDO_COLOR, MESSI_COLOR],
            textinfo='label+percent',
            textfont=dict(size=16, family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Category Winners",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Summary metrics with custom design
    st.markdown('## 🎯 Clutch Performance Summary')
    
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🎯</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Penalty Winner</h4>
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
            ">+20 points</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">⚡</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Last Minute Winner</h4>
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
            ">+10 points</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏆</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Finals Winner</h4>
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
            ">+5 points</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🔥</div>
            <h4 style="color: #FFD700; margin: 0 0 10px 0;">CLUTCH CHAMPION</h4>
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
            ">5/6 categories</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()