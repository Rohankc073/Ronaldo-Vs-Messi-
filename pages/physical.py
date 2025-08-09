import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def show():
    """Display clean physical attributes analysis"""
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
    
    st.set_page_config(page_title="Physical Analysis", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: {MESSI_COLOR}; font-family: 'Times New Roman', serif;">
    💪 PHYSICAL ATTRIBUTES & ATHLETICISM
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
            <h3>The Agility Master</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                <div><strong>170cm</strong><br>Height</div>
                <div><strong>72kg</strong><br>Weight</div>
                <div><strong>32.5</strong><br>Top Speed</div>
                <div><strong>99/100</strong><br>Agility</div>
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
            <h3>The Athletic Specimen</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                <div><strong>187cm</strong><br>Height</div>
                <div><strong>83kg</strong><br>Weight</div>
                <div><strong>34.6</strong><br>Top Speed</div>
                <div><strong>78cm</strong><br>Jump Height</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Physical attributes radar
    st.markdown('## 📊 Physical Attributes Comparison')
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Radar chart
        categories = ['Speed', 'Strength', 'Agility', 'Stamina', 'Jumping', 'Balance']
        messi_values = [85, 75, 99, 88, 70, 99]
        ronaldo_values = [95, 95, 85, 92, 99, 82]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_values,
            theta=categories,
            fill='toself',
            name='Messi',
            fillcolor=f'rgba(117, 170, 219, 0.3)',
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_values,
            theta=categories,
            fill='toself',
            name='Ronaldo',
            fillcolor=f'rgba(255, 45, 45, 0.3)',
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Physical Attributes Radar",
            height=500,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Key metrics table
        metrics_data = {
            'Attribute': ['Top Speed', 'Strength', 'Agility', 'Stamina', 'Jump Height', 'Balance'],
            'Messi': [32.5, 75, 99, 88, 40, 99],
            'Ronaldo': [34.6, 95, 85, 92, 78, 82],
            'Winner': ['🇵🇹', '🇵🇹', '🇦🇷', '🇵🇹', '🇵🇹', '🇦🇷']
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        st.dataframe(metrics_df, use_container_width=True, height=350)
    
    # Speed and acceleration analysis
    st.markdown('## ⚡ Speed & Acceleration Analysis')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Acceleration comparison
        distances = ['0-10m', '0-20m', '0-30m']
        messi_times = [1.8, 2.9, 4.1]
        ronaldo_times = [1.9, 3.0, 4.0]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=distances,
            y=messi_times,
            marker_color=MESSI_COLOR,
            text=[f'{t}s' for t in messi_times],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=distances,
            y=ronaldo_times,
            marker_color=RONALDO_COLOR,
            text=[f'{t}s' for t in ronaldo_times],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Acceleration Times (Lower is Better)",
            yaxis_title="Time (seconds)",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Top speed gauges
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'indicator'}, {'type': 'indicator'}]],
            subplot_titles=['Messi Top Speed', 'Ronaldo Top Speed']
        )
        
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=32.5,
            domain={'x': [0, 0.48], 'y': [0, 1]},
            title={'text': "km/h"},
            gauge={
                'axis': {'range': [None, 40]},
                'bar': {'color': MESSI_COLOR},
                'steps': [
                    {'range': [0, 25], 'color': "lightgray"},
                    {'range': [25, 35], 'color': "gray"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 35
                }
            }
        ), row=1, col=1)
        
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=34.6,
            domain={'x': [0.52, 1], 'y': [0, 1]},
            title={'text': "km/h"},
            gauge={
                'axis': {'range': [None, 40]},
                'bar': {'color': RONALDO_COLOR},
                'steps': [
                    {'range': [0, 25], 'color': "lightgray"},
                    {'range': [25, 35], 'color': "gray"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 35
                }
            }
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="Top Speed Comparison", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    # Strength and power analysis
    st.markdown('## 💪 Strength & Power Analysis')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Raw strength comparison
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Bench Press', 'Squat', 'Overall'],
            y=[140, 160, 75],  # Messi estimates
            name='Messi',
            marker_color=MESSI_COLOR,
            text=['140kg', '160kg', '75/100'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            x=['Bench Press', 'Squat', 'Overall'],
            y=[180, 200, 95],  # Ronaldo estimates
            name='Ronaldo',
            marker_color=RONALDO_COLOR,
            text=['180kg', '200kg', '95/100'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Strength Comparison",
            yaxis_title="Weight (kg) / Score",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Jumping ability
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Messi', 'Ronaldo'],
            y=[40, 78],
            marker_color=[MESSI_COLOR, RONALDO_COLOR],
            text=['40cm', '78cm'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Vertical Jump Height",
            yaxis_title="Height (cm)",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Balance comparison
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Messi', 'Ronaldo'],
            y=[99, 82],
            marker_color=[MESSI_COLOR, RONALDO_COLOR],
            text=['99/100', '82/100'],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Balance & Coordination",
            yaxis_title="Score (0-100)",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Injury record analysis
    st.markdown('## 🏥 Injury Record & Availability')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Injury comparison
        categories = ['Games Missed', 'Serious Injuries', 'Muscle Injuries']
        messi_injuries = [85, 3, 12]
        ronaldo_injuries = [45, 2, 8]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_injuries,
            marker_color=MESSI_COLOR,
            text=messi_injuries,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_injuries,
            marker_color=RONALDO_COLOR,
            text=ronaldo_injuries,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Career Injury Comparison",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Availability by age
        ages = list(range(20, 40))
        messi_availability = [95, 92, 88, 85, 90, 88, 85, 82, 90, 88, 85, 80, 75, 85, 90, 88, 85, 80, 75, 70]
        ronaldo_availability = [98, 95, 92, 95, 98, 95, 98, 95, 92, 95, 98, 95, 92, 88, 90, 88, 85, 82, 80, 85]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=ages,
            y=messi_availability,
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=ages,
            y=ronaldo_availability,
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Availability % by Age",
            xaxis_title="Age",
            yaxis_title="Availability %",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Physical evolution over career
    st.markdown('## 📈 Physical Evolution Over Career')
    
    career_phases = ['Early Career', 'Peak Years', 'Late Career']
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Speed Evolution', 'Strength Evolution', 'Stamina Evolution', 'Agility Evolution')
    )
    
    # Speed evolution
    messi_speed = [90, 95, 85]
    ronaldo_speed = [85, 100, 90]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_speed, name='Messi Speed', 
                           line=dict(color=MESSI_COLOR, width=4), marker=dict(size=10)), row=1, col=1)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_speed, name='Ronaldo Speed', 
                           line=dict(color=RONALDO_COLOR, width=4), marker=dict(size=10)), row=1, col=1)
    
    # Strength evolution
    messi_strength = [70, 80, 85]
    ronaldo_strength = [80, 95, 100]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_strength, name='Messi Strength', 
                           line=dict(color=MESSI_COLOR, width=4), marker=dict(size=10), showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_strength, name='Ronaldo Strength', 
                           line=dict(color=RONALDO_COLOR, width=4), marker=dict(size=10), showlegend=False), row=1, col=2)
    
    # Stamina evolution
    messi_stamina = [75, 85, 95]
    ronaldo_stamina = [90, 95, 98]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_stamina, name='Messi Stamina', 
                           line=dict(color=MESSI_COLOR, width=4), marker=dict(size=10), showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_stamina, name='Ronaldo Stamina', 
                           line=dict(color=RONALDO_COLOR, width=4), marker=dict(size=10), showlegend=False), row=2, col=1)
    
    # Agility evolution
    messi_agility = [95, 100, 95]
    ronaldo_agility = [90, 95, 85]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_agility, name='Messi Agility', 
                           line=dict(color=MESSI_COLOR, width=4), marker=dict(size=10), showlegend=False), row=2, col=2)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_agility, name='Ronaldo Agility', 
                           line=dict(color=RONALDO_COLOR, width=4), marker=dict(size=10), showlegend=False), row=2, col=2)
    
    fig.update_layout(height=600, title_text="Physical Attributes Through Career Phases", 
                     template='plotly_white', font=dict(family='Times New Roman'))
    st.plotly_chart(fig, use_container_width=True)
    
    # Physical comparison metrics with custom design
    st.markdown('## 🏆 Physical Metrics Summary')
    
    # Custom metrics cards
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">💨</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Top Speed Winner</h4>
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
            ">+2.1 km/h advantage</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">💪</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Strength Winner</h4>
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
            ">+20 points advantage</div>
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
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🤸</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Agility Winner</h4>
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
            ">+14 points advantage</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏥</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Injury Record</h4>
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
            ">40 fewer games missed</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Final verdict
    st.markdown('## 🎯 Physical Attributes Verdict')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🇦🇷 Messi - The Agility Master**
        - Superior agility & balance (99/100)
        - Exceptional body control
        - Low center of gravity advantage
        - Quick change of direction
        """)
    
    with col2:
        st.markdown("""
        **🇵🇹 Ronaldo - The Athletic Specimen**
        - Superior speed & strength
        - Incredible jumping ability (78cm)
        - Better injury record
        - Elite physical conditioning
        """)
    
    st.markdown("""
    ---
    
    ### 🏁 The Final Verdict
    
    **Physical Winner: 🇵🇹 RONALDO** - The ultimate athletic specimen with superior speed, strength, 
    jumping ability, and injury record. However, Messi's agility and balance are unmatched, proving 
    that different physical attributes can lead to greatness! 🐐
    """)

if __name__ == "__main__":
    show()