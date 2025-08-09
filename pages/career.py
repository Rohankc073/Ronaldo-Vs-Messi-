import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the visual career statistics page"""
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
    
    st.markdown('<h1 class="section-header">📊 CAREER STATISTICS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    career_stats = data['career_stats']
    season_goals = data['season_goals']
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'  # Argentina Blue
    RONALDO_COLOR = '#FF2D2D'  # Portugal Red
    
    # Simple and clean CSS for metrics design
    st.markdown("""
    <style>
    .metric-card {
        background: rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 10px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .metric-card:hover {
        background: rgba(255,255,255,0.12);
        transform: translateY(-2px);
    }
    
    .metric-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
        display: block;
    }
    
    .metric-title {
        font-family: 'Times New Roman', serif;
        font-size: 1rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 15px;
        color: #f0f0f0;
    }
    
    .metric-values {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }
    
    .player-value {
        flex: 1;
        text-align: center;
    }
    
    .player-name {
        font-size: 0.8rem;
        font-weight: bold;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .messi-name { color: #75AADB; }
    .ronaldo-name { color: #FF2D2D; }
    
    .value-number {
        font-size: 1.8rem;
        font-weight: 900;
        font-family: 'Times New Roman', serif;
    }
    
    .vs-separator {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.6;
        margin: 0 10px;
    }
    
    .advantage-badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        font-family: 'Times New Roman', serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .messi-advantage {
        background: #75AADB;
        color: white;
    }
    
    .ronaldo-advantage {
        background: #FF2D2D;
        color: white;
    }
    
    .tie-advantage {
        background: #FFD700;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Big Numbers Dashboard with simple design
    col1, col2, col3, col4, col5 = st.columns(5)
    
    metrics_data = [
        {
            "icon": "🥅",
            "title": "Goals",
            "messi_value": "815",
            "ronaldo_value": "895",
            "advantage": "ronaldo",
            "advantage_text": "Ronaldo leads by 80"
        },
        {
            "icon": "🎯", 
            "title": "Assists",
            "messi_value": "377",
            "ronaldo_value": "236", 
            "advantage": "messi",
            "advantage_text": "Messi leads by 141"
        },
        {
            "icon": "⚽",
            "title": "G+A",
            "messi_value": "1,192",
            "ronaldo_value": "1,131",
            "advantage": "messi", 
            "advantage_text": "Messi leads by 61"
        },
        {
            "icon": "🎮",
            "title": "Games",
            "messi_value": "1,069",
            "ronaldo_value": "1,205",
            "advantage": "ronaldo",
            "advantage_text": "Ronaldo played 136 more"
        },
        {
            "icon": "📈",
            "title": "Efficiency",
            "messi_value": "0.76",
            "ronaldo_value": "0.74", 
            "advantage": "messi",
            "advantage_text": "Messi more efficient"
        }
    ]
    
    columns = [col1, col2, col3, col4, col5]
    
    for i, (col, metric) in enumerate(zip(columns, metrics_data)):
        with col:
            advantage_class = f"{metric['advantage']}-advantage"
            
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-icon">{metric['icon']}</span>
                <div class="metric-title">{metric['title']}</div>
                <div class="metric-values">
                    <div class="player-value">
                        <div class="player-name messi-name">Messi</div>
                        <div class="value-number">{metric['messi_value']}</div>
                    </div>
                    <div class="vs-separator">VS</div>
                    <div class="player-value">
                        <div class="player-name ronaldo-name">Ronaldo</div>
                        <div class="value-number">{metric['ronaldo_value']}</div>
                    </div>
                </div>
                <div class="advantage-badge {advantage_class}">
                    {metric['advantage_text']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Main comparison charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals and Assists comparison
        categories = ['Goals', 'Assists', 'G+A', 'Goals/90', 'Assists/90']
        messi_stats = [815, 377, 1192, 0.76, 0.35]
        ronaldo_stats = [895, 236, 1131, 0.74, 0.20]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='🇦🇷 Messi',
            x=categories,
            y=messi_stats,
            marker_color=MESSI_COLOR,
            text=messi_stats,
            textposition='auto',
            textfont=dict(size=14, color='white', family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='🇵🇹 Ronaldo',
            x=categories,
            y=ronaldo_stats,
            marker_color=RONALDO_COLOR,
            text=ronaldo_stats,
            textposition='auto',
            textfont=dict(size=14, color='white', family='Times New Roman')
        ))
        
        fig.update_layout(
            title="⚽ Career Production",
            barmode='group',
            height=400,
            template='plotly_white',
            showlegend=True,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Efficiency radar chart
        categories_radar = ['Goals/90', 'Assists/90', 'Shot%', 'Conversion', 'Dribbles', 'Chances']
        messi_radar = [76, 35, 45, 18, 95, 85]
        ronaldo_radar = [74, 20, 43, 15, 45, 92]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_radar,
            theta=categories_radar,
            fill='toself',
            name='🇦🇷 Messi',
            fillcolor=f'rgba(117, 170, 219, 0.4)',  # Argentina Blue with transparency
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_radar,
            theta=categories_radar,
            fill='toself',
            name='🇵🇹 Ronaldo',
            fillcolor=f'rgba(255, 45, 45, 0.4)',  # Portugal Red with transparency
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title="⚡ Performance Radar",
            height=400,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Season Goals Timeline - Enhanced
    st.markdown("### 📈 GOALS BY SEASON")
    
    years = list(range(2005, 2024))
    messi_goals = [6, 17, 16, 38, 47, 60, 73, 60, 41, 58, 54, 51, 45, 51, 36, 31, 38, 30, 21]
    ronaldo_goals = [9, 20, 42, 33, 40, 55, 60, 51, 61, 48, 44, 42, 37, 28, 31, 36, 29, 24, 14]
    
    fig = go.Figure()
    
    # Add area fill for better visual impact
    fig.add_trace(go.Scatter(
        x=years,
        y=messi_goals,
        mode='lines+markers',
        name='🇦🇷 Messi',
        line=dict(color=MESSI_COLOR, width=4),
        fill='tonexty',
        fillcolor='rgba(117, 170, 219, 0.3)',
        marker=dict(size=10, line=dict(width=2, color='white')),
        hovertemplate='<b>Messi</b><br>%{x}: %{y} goals<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=ronaldo_goals,
        mode='lines+markers',
        name='🇵🇹 Ronaldo',
        line=dict(color=RONALDO_COLOR, width=4),
        fill='tozeroy',
        fillcolor='rgba(255, 45, 45, 0.3)',
        marker=dict(size=10, line=dict(width=2, color='white')),
        hovertemplate='<b>Ronaldo</b><br>%{x}: %{y} goals<extra></extra>'
    ))
    
    # Add milestone markers
    fig.add_annotation(x=2012, y=73, text="🏆", showarrow=False, font=dict(size=25))
    fig.add_annotation(x=2014, y=61, text="👑", showarrow=False, font=dict(size=25))
    fig.add_annotation(x=2022, y=21, text="🌟", showarrow=False, font=dict(size=25))
    
    fig.update_layout(
        title="⚽ Season Goals Evolution",
        height=500,
        template='plotly_white',
        hovermode='x unified',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Skills Comparison - Visual Grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Goal Types
        goal_types = ['Total', 'Headers', 'Weak Foot', 'Outside Box', 'Penalties']
        messi_goals_breakdown = [815, 26, 118, 89, 103]
        ronaldo_goals_breakdown = [895, 145, 312, 156, 140]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=goal_types,
            x=messi_goals_breakdown,
            name='🇦🇷 Messi',
            orientation='h',
            marker_color=MESSI_COLOR,
            text=messi_goals_breakdown,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            y=goal_types,
            x=ronaldo_goals_breakdown,
            name='🇵🇹 Ronaldo',
            orientation='h',
            marker_color=RONALDO_COLOR,
            text=ronaldo_goals_breakdown,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🎯 Goal Types",
            barmode='group',
            height=400,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Creative Stats
        creative_stats = ['Assists', 'Key Passes', 'Chances', 'Dribbles', 'Through Balls']
        messi_creative = [377, 95, 85, 95, 78]
        ronaldo_creative = [236, 65, 70, 45, 42]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_creative,
            theta=creative_stats,
            fill='toself',
            name='🇦🇷 Messi',
            fillcolor='rgba(117, 170, 219, 0.5)',
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_creative,
            theta=creative_stats,
            fill='toself',
            name='🇵🇹 Ronaldo',
            fillcolor='rgba(255, 45, 45, 0.5)',
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        
        fig.update_layout(
            title="🎨 Creativity",
            polar=dict(radialaxis=dict(range=[0, 100])),
            height=400,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Efficiency Metrics
        efficiency_categories = ['Conversion %', 'Accuracy %', 'Success %']
        messi_efficiency = [17.8, 45.2, 77.8]
        ronaldo_efficiency = [15.2, 42.8, 84.3]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=efficiency_categories,
            y=messi_efficiency,
            name='🇦🇷 Messi',
            marker_color=MESSI_COLOR,
            text=[f'{x}%' for x in messi_efficiency],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            x=efficiency_categories,
            y=ronaldo_efficiency,
            name='🇵🇹 Ronaldo',
            marker_color=RONALDO_COLOR,
            text=[f'{x}%' for x in ronaldo_efficiency],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="📊 Efficiency %",
            height=400,
            yaxis=dict(range=[0, 100]),
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Age Performance Analysis
    st.markdown("### ⏰ PERFORMANCE BY AGE")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Age vs Goals
        age_ranges = ['18-23', '24-29', '30-35', '36-40']
        messi_age_goals = [28.5, 52.3, 41.2, 18.7]
        ronaldo_age_goals = [31.2, 48.6, 38.4, 24.5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=age_ranges,
            y=messi_age_goals,
            mode='lines+markers',
            name='🇦🇷 Messi',
            line=dict(color=MESSI_COLOR, width=5),
            marker=dict(size=15)
        ))
        fig.add_trace(go.Scatter(
            x=age_ranges,
            y=ronaldo_age_goals,
            mode='lines+markers',
            name='🇵🇹 Ronaldo',
            line=dict(color=RONALDO_COLOR, width=5),
            marker=dict(size=15)
        ))
        
        fig.update_layout(
            title="📈 Goals by Age Range",
            height=400,
            yaxis_title="Goals per Season",
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Milestone Ages
        milestones = [100, 200, 300, 400, 500, 600, 700, 800]
        messi_ages = [20.1, 22.4, 24.2, 25.8, 27.6, 29.9, 32.1, 35.2]
        ronaldo_ages = [21.3, 23.8, 25.9, 27.4, 28.7, 30.8, 33.2, 36.1]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=messi_ages,
            y=milestones,
            mode='lines+markers',
            name='🇦🇷 Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=12)
        ))
        fig.add_trace(go.Scatter(
            x=ronaldo_ages,
            y=milestones,
            mode='lines+markers',
            name='🇵🇹 Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=12)
        ))
        
        fig.update_layout(
            title="⏱️ Age at Milestones",
            height=400,
            xaxis_title="Age",
            yaxis_title="Goals",
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Head-to-Head Visual Summary
    st.markdown("### 🏆 HEAD-TO-HEAD SUMMARY")
    
    # Create comparison scorecard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Messi wins
        messi_wins = ['Assists', 'G+A', 'Goals/90', 'Dribbles', 'Key Passes', 'Shot%']
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=messi_wins,
            x=[1] * len(messi_wins),
            orientation='h',
            marker_color=MESSI_COLOR,
            text=['✅'] * len(messi_wins),
            textposition='auto',
            textfont=dict(size=20, family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🇦🇷 Messi Leads",
            height=300,
            showlegend=False,
            xaxis=dict(visible=False),
            yaxis=dict(title=""),
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Tied categories
        tied_categories = ['Hat-tricks', 'Free Kicks', 'Big Games']
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=tied_categories,
            x=[1] * len(tied_categories),
            orientation='h',
            marker_color='#FFA500',
            text=['🤝'] * len(tied_categories),
            textposition='auto',
            textfont=dict(size=20, family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🤝 Close/Tied",
            height=300,
            showlegend=False,
            xaxis=dict(visible=False),
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Ronaldo wins
        ronaldo_wins = ['Total Goals', 'Headers', 'Weak Foot', 'Penalties', 'Longevity', 'Outside Box']
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=ronaldo_wins,
            x=[1] * len(ronaldo_wins),
            orientation='h',
            marker_color=RONALDO_COLOR,
            text=['✅'] * len(ronaldo_wins),
            textposition='auto',
            textfont=dict(size=20, family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🇵🇹 Ronaldo Leads",
            height=300,
            showlegend=False,
            xaxis=dict(visible=False),
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Final Visual Verdict
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Score visualization
        categories = ['Goals', 'Creativity', 'Efficiency', 'Longevity', 'Versatility']
        messi_scores = [90, 100, 95, 85, 88]
        ronaldo_scores = [100, 75, 85, 100, 95]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_scores,
            theta=categories,
            fill='toself',
            name='🇦🇷 Messi',
            fillcolor='rgba(117, 170, 219, 0.6)',
            line=dict(color=MESSI_COLOR, width=4)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_scores,
            theta=categories,
            fill='toself',
            name='🇵🇹 Ronaldo',
            fillcolor='rgba(255, 45, 45, 0.6)',
            line=dict(color=RONALDO_COLOR, width=4)
        ))
        
        fig.update_layout(
            title="🏆 CAREER STATS VERDICT",
            polar=dict(radialaxis=dict(range=[0, 100])),
            height=500,
            font=dict(size=14, family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    
if __name__ == "__main__":
    show()