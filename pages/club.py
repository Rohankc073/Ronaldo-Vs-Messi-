import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the club performance analysis page"""
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
    
    st.markdown('<h1 class="section-header">🏆 CLUB PERFORMANCE ANALYSIS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    club_data = data['club_goals']
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    # Brief introduction
    st.markdown("**Club football legends: Analyzing Messi and Ronaldo's performances across different clubs and leagues.**")
    
    # Career Overview Cards - More Visual, Less Text
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🏟️ Career Overview</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi career timeline visualization
        messi_clubs = ['Barcelona', 'PSG', 'Inter Miami']
        messi_years = [18, 2, 2]
        messi_goals = [672, 32, 25]
        
        fig = go.Figure(go.Pie(
            labels=messi_clubs,
            values=messi_goals,
            hole=0.6,
            marker_colors=['#004D98', RONALDO_COLOR, '#FF69B4'],
            title="🇦🇷 Messi's Career Goals Distribution",
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(height=400, showlegend=True, font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
        
        # Quick stats
        st.markdown("""
        **🔵 Barcelona:** 672 goals, 303 assists, 34 trophies  
        **🔴 PSG:** 32 goals, 35 assists, 2 trophies  
        **🩷 Miami:** 25+ goals, 15+ assists, 1 trophy
        """)
    
    with col2:
        # Ronaldo career timeline visualization
        ronaldo_clubs = ['Man United', 'Real Madrid', 'Juventus', 'Al Nassr']
        ronaldo_goals = [145, 451, 101, 68]
        
        fig = go.Figure(go.Pie(
            labels=ronaldo_clubs,
            values=ronaldo_goals,
            hole=0.6,
            marker_colors=[RONALDO_COLOR, '#FFFFFF', '#000000', '#FFD700'],
            title="🇵🇹 Ronaldo's Career Goals Distribution",
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(height=400, showlegend=True, font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
        
        # Quick stats
        st.markdown("""
        **🔴 Man United:** 145 goals, 64 assists, 9 trophies  
        **⚪ Real Madrid:** 451 goals, 131 assists, 16 trophies  
        **⚫ Juventus:** 101 goals, 22 assists, 5 trophies  
        **🟡 Al Nassr:** 68+ goals, 18+ assists, 0 trophies
        """)
    
    # Goals per Game Comparison by Club
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">⚽ Goals per Game by Club</h3>', unsafe_allow_html=True)
    
    clubs = ['Barcelona', 'PSG', 'Miami', 'Man United', 'Real Madrid', 'Juventus', 'Al Nassr']
    messi_gpg = [0.86, 0.43, 0.74, 0, 0, 0, 0]
    ronaldo_gpg = [0, 0, 0, 0.42, 1.03, 0.75, 0.92]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=clubs,
        y=messi_gpg,
        mode='markers+lines',
        name='Messi',
        marker=dict(size=15, color=MESSI_COLOR),
        line=dict(width=3, color=MESSI_COLOR)
    ))
    fig.add_trace(go.Scatter(
        x=clubs,
        y=ronaldo_gpg,
        mode='markers+lines',
        name='Ronaldo',
        marker=dict(size=15, color=RONALDO_COLOR),
        line=dict(width=3, color=RONALDO_COLOR)
    ))
    fig.update_layout(
        title="🎯 Goals per Game Comparison",
        yaxis_title="Goals per Game",
        height=400,
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Radar Chart - Club Performance Metrics
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🕸️ Performance Radar</h3>', unsafe_allow_html=True)
    
    categories = ['Goals per Game', 'Trophies per Year', 'Adaptability', 'Longevity', 'Peak Performance', 'Consistency']
    
    messi_values = [9, 8, 7, 10, 10, 9]
    ronaldo_values = [8, 7, 10, 8, 9, 9]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=messi_values,
        theta=categories,
        fill='toself',
        name='Messi',
        line_color=MESSI_COLOR,
        fillcolor=f'rgba(117, 170, 219, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=ronaldo_values,
        theta=categories,
        fill='toself',
        name='Ronaldo',
        line_color=RONALDO_COLOR,
        fillcolor=f'rgba(255, 45, 45, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        title="🎯 Club Performance Comparison",
        height=500,
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Goals Timeline with Club Changes
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">📈 Career Goals Timeline</h3>', unsafe_allow_html=True)
    
    seasons = list(range(2004, 2024))
    messi_goals = [6, 8, 17, 16, 38, 47, 60, 73, 60, 41, 58, 54, 45, 51, 36, 31, 30, 35, 16, 21]
    ronaldo_goals = [6, 9, 23, 42, 33, 40, 60, 55, 51, 61, 48, 50, 44, 42, 28, 37, 31, 29, 24, 14]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=seasons,
        y=messi_goals,
        mode='lines+markers',
        name='Messi',
        line=dict(color=MESSI_COLOR, width=4),
        marker=dict(size=8, color=MESSI_COLOR),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=seasons,
        y=ronaldo_goals,
        mode='lines+markers',
        name='Ronaldo',
        line=dict(color=RONALDO_COLOR, width=4),
        marker=dict(size=8, color=RONALDO_COLOR),
        fill='tozeroy'
    ))
    
    # Add transfer annotations
    fig.add_vline(x=2009, line_dash="dash", line_color=RONALDO_COLOR, annotation_text="Ronaldo → Real", 
                  annotation=dict(font=dict(family='Times New Roman')))
    fig.add_vline(x=2018, line_dash="dash", line_color=RONALDO_COLOR, annotation_text="Ronaldo → Juventus",
                  annotation=dict(font=dict(family='Times New Roman')))
    fig.add_vline(x=2021, line_dash="dash", line_color=MESSI_COLOR, annotation_text="Messi → PSG",
                  annotation=dict(font=dict(family='Times New Roman')))
    fig.add_vline(x=2023, line_dash="dash", line_color=MESSI_COLOR, annotation_text="Messi → Miami",
                  annotation=dict(font=dict(family='Times New Roman')))
    
    fig.update_layout(
        title="⚽ Goals per Season with Club Changes",
        xaxis_title="Season",
        yaxis_title="Goals",
        height=500,
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Champions League Performance
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🏆 Champions League Stats</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 5,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "CL Titles"},
            gauge = {'axis': {'range': [None, 6]},
                     'bar': {'color': RONALDO_COLOR},
                     'steps': [{'range': [0, 3], 'color': "lightgray"},
                               {'range': [3, 6], 'color': "gray"}],
                     'threshold': {'line': {'color': "red", 'width': 4},
                                   'thickness': 0.75, 'value': 5}}
        ))
        fig.update_layout(height=250, title="🇵🇹 Ronaldo", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 4,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "CL Titles"},
            gauge = {'axis': {'range': [None, 6]},
                     'bar': {'color': MESSI_COLOR},
                     'steps': [{'range': [0, 3], 'color': "lightgray"},
                               {'range': [3, 6], 'color': "gray"}],
                     'threshold': {'line': {'color': "blue", 'width': 4},
                                   'thickness': 0.75, 'value': 4}}
        ))
        fig.update_layout(height=250, title="🇦🇷 Messi", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 140,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "CL Goals"},
            gauge = {'axis': {'range': [None, 150]},
                     'bar': {'color': RONALDO_COLOR},
                     'steps': [{'range': [0, 100], 'color': "lightgray"},
                               {'range': [100, 150], 'color': "gray"}],
                     'threshold': {'line': {'color': "red", 'width': 4},
                                   'thickness': 0.75, 'value': 140}}
        ))
        fig.update_layout(height=250, title="🇵🇹 Ronaldo", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 129,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "CL Goals"},
            gauge = {'axis': {'range': [None, 150]},
                     'bar': {'color': MESSI_COLOR},
                     'steps': [{'range': [0, 100], 'color': "lightgray"},
                               {'range': [100, 150], 'color': "gray"}],
                     'threshold': {'line': {'color': "blue", 'width': 4},
                                   'thickness': 0.75, 'value': 129}}
        ))
        fig.update_layout(height=250, title="🇦🇷 Messi", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    # Trophies Comparison
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🏅 Trophy Comparison</h3>', unsafe_allow_html=True)
    
    trophy_types = ['League Titles', 'Champions League', 'Domestic Cups', 'Super Cups', 'Club World Cup']
    messi_trophies = [12, 4, 7, 8, 3]
    ronaldo_trophies = [7, 5, 4, 4, 4]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Messi',
        x=trophy_types,
        y=messi_trophies,
        marker_color=MESSI_COLOR,
        text=messi_trophies,
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    fig.add_trace(go.Bar(
        name='Ronaldo',
        x=trophy_types,
        y=ronaldo_trophies,
        marker_color=RONALDO_COLOR,
        text=ronaldo_trophies,
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    
    fig.update_layout(
        title="🏆 Club Trophies by Category",
        barmode='group',
        height=400,
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Club Performance Heatmap
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🔥 Performance Heatmap</h3>', unsafe_allow_html=True)
    
    performance_data = {
        'Club': ['Barcelona', 'PSG', 'Inter Miami', 'Man United', 'Real Madrid', 'Juventus', 'Al Nassr'],
        'Goals per Game': [0.86, 0.43, 0.74, 0.42, 1.03, 0.75, 0.92],
        'Assists per Game': [0.39, 0.47, 0.44, 0.18, 0.30, 0.16, 0.24],
        'Trophies per Year': [1.89, 1.00, 0.50, 1.50, 1.78, 1.67, 0.00],
        'Impact Rating': [10, 6, 9, 7, 10, 8, 7]
    }
    
    df = pd.DataFrame(performance_data)
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=[df['Goals per Game'], df['Assists per Game'], df['Trophies per Year'], df['Impact Rating']],
        x=df['Club'],
        y=['Goals/Game', 'Assists/Game', 'Trophies/Year', 'Impact'],
        colorscale='RdYlBu_r',
        text=[[f"{val:.2f}" for val in df['Goals per Game']],
              [f"{val:.2f}" for val in df['Assists per Game']],
              [f"{val:.2f}" for val in df['Trophies per Year']],
              [f"{val}" for val in df['Impact Rating']]],
        texttemplate="%{text}",
        textfont={"size":12, "family": "Times New Roman"}
    ))
    
    fig.update_layout(
        title="🌡️ Club Performance Heatmap",
        height=400,
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Adaptation Score Visualization
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🔄 Adaptation vs Loyalty</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Loyalty vs Adaptability scatter
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=[9], y=[7],
            mode='markers+text',
            marker=dict(size=50, color=MESSI_COLOR),
            text=['Messi'],
            textposition='middle center',
            name='Messi',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Scatter(
            x=[7], y=[10],
            mode='markers+text',
            marker=dict(size=50, color=RONALDO_COLOR),
            text=['Ronaldo'],
            textposition='middle center',
            name='Ronaldo',
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(
            title="Loyalty vs Adaptability",
            xaxis_title="Loyalty Score",
            yaxis_title="Adaptability Score",
            height=400,
            xaxis=dict(range=[5, 11]),
            yaxis=dict(range=[5, 11]),
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # League success comparison
        leagues = ['Premier League', 'La Liga', 'Serie A', 'Ligue 1', 'MLS', 'Saudi Pro League']
        messi_success = [0, 10, 0, 6, 9, 0]
        ronaldo_success = [8, 9, 8, 0, 0, 7]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=leagues,
            y=messi_success,
            marker_color=MESSI_COLOR,
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=leagues,
            y=ronaldo_success,
            marker_color=RONALDO_COLOR,
            textfont=dict(family='Times New Roman')
        ))
        fig.update_layout(
            title="League Success Rating",
            barmode='group',
            height=400,
            xaxis_tickangle=-45,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Final Verdict with custom design
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🏁 Final Verdict</h3>', unsafe_allow_html=True)
    
    # Custom metrics cards
    col1, col2, col3 = st.columns(3)
    
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">⚽</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Peak Goals/Game</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                1.03
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">Ronaldo (Real Madrid)</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏆</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Most Club Goals</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                672
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">Messi (Barcelona)</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🌍</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Leagues Conquered</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                4
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">Ronaldo</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    **🏆 Club Verdict:** Both legends excel differently - Messi dominates through loyalty and peak performance, 
    while Ronaldo conquers through adaptability and versatility across leagues.
    """)

if __name__ == "__main__":
    show()