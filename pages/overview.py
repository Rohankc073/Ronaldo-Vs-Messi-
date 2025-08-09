import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the refined overview page for Messi vs Ronaldo with focus on visualizations"""
    st.markdown('<h1 class="section-header">⚽ THE GREATEST OF ALL TIME DEBATE</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    career_stats = data['career_stats']
    
    # Compact hero section
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: #1f77b4; font-size: 2.2rem;">🐐 WHO IS THE GOAT? 🐐</h2>
        <p style="font-size: 1.1rem; color: #666;">15+ years of legendary rivalry</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Compact player cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        ">
            <h2 style="margin: 0;">🇦🇷 LIONEL MESSI</h2>
            <p style="margin: 0.5rem 0; opacity: 0.9;">Age 37 | Inter Miami | RW/CF</p>
            <div style="display: flex; justify-content: space-around; margin: 1rem 0;">
                <div><strong>815</strong><br><small>Goals</small></div>
                <div><strong>377</strong><br><small>Assists</small></div>
                <div><strong>8</strong><br><small>Ballon d'Or</small></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #FF6B6B 0%, #C44569 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        ">
            <h2 style="margin: 0;">🇵🇹 CRISTIANO RONALDO</h2>
            <p style="margin: 0.5rem 0; opacity: 0.9;">Age 40 | Al Nassr | CF/LW</p>
            <div style="display: flex; justify-content: space-around; margin: 1rem 0;">
                <div><strong>895</strong><br><small>Goals</small></div>
                <div><strong>236</strong><br><small>Assists</small></div>
                <div><strong>5</strong><br><small>Ballon d'Or</small></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick metrics with visual indicators
    st.markdown('<h2 class="section-header">⚡ HEAD-TO-HEAD QUICK STATS</h2>', unsafe_allow_html=True)
    
    # Create a comparative metrics chart instead of separate metrics
    metrics_data = {
        'Metric': ['Goals', 'Assists', 'Ballon d\'Or', 'Team Trophies', 'Goals/90min'],
        'Messi': [815, 377, 8, 44, 0.79],
        'Ronaldo': [895, 236, 5, 35, 0.74],
        'Winner': ['Ronaldo', 'Messi', 'Messi', 'Messi', 'Messi']
    }
    
    fig = go.Figure()
    
    # Normalize values for better visualization (except for goals which are close)
    norm_messi = [815/1000, 377/400, 8/10, 44/50, 0.79/1]
    norm_ronaldo = [895/1000, 236/400, 5/10, 35/50, 0.74/1]
    
    fig.add_trace(go.Scatterpolar(
        r=norm_messi,
        theta=metrics_data['Metric'],
        fill='toself',
        name='Messi',
        fillcolor='rgba(78, 205, 196, 0.4)',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=norm_ronaldo,
        theta=metrics_data['Metric'],
        fill='toself',
        name='Ronaldo',
        fillcolor='rgba(255, 107, 107, 0.4)',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1])
        ),
        showlegend=True,
        title="🔥 Head-to-Head Performance Radar",
        height=500,
        font=dict(size=14)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Career timeline with key milestones
    st.markdown('<h2 class="section-header">📈 CAREER GOALS TIMELINE</h2>', unsafe_allow_html=True)
    
    # Enhanced season data with milestones
    years = list(range(2005, 2024))
    messi_goals = [6, 17, 16, 38, 47, 60, 73, 60, 41, 58, 54, 51, 45, 51, 36, 31, 38, 30, 21]
    ronaldo_goals = [9, 20, 42, 33, 40, 55, 60, 51, 61, 48, 44, 42, 37, 28, 31, 36, 29, 24, 14]
    
    fig = go.Figure()
    
    # Add area charts for better visual impact
    fig.add_trace(go.Scatter(
        x=years,
        y=messi_goals,
        mode='lines+markers',
        name='Messi',
        line=dict(color='#4ECDC4', width=4),
        fill='tonexty',
        fillcolor='rgba(78, 205, 196, 0.3)',
        marker=dict(size=8, line=dict(width=2, color='white')),
        hovertemplate='<b>Messi</b><br>%{x}: %{y} goals<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=ronaldo_goals,
        mode='lines+markers',
        name='Ronaldo',
        line=dict(color='#FF6B6B', width=4),
        fill='tozeroy',
        fillcolor='rgba(255, 107, 107, 0.3)',
        marker=dict(size=8, line=dict(width=2, color='white')),
        hovertemplate='<b>Ronaldo</b><br>%{x}: %{y} goals<extra></extra>'
    ))
    
    # Add milestone markers
    fig.add_annotation(x=2012, y=73, text="🏆", showarrow=False, font=dict(size=20))
    fig.add_annotation(x=2014, y=61, text="⚡", showarrow=False, font=dict(size=20))
    fig.add_annotation(x=2022, y=21, text="🌟", showarrow=False, font=dict(size=20))
    
    fig.update_layout(
        title="⚽ Goals by Season - Peak Performance Eras",
        xaxis_title="Season",
        yaxis_title="Goals",
        height=500,
        template='plotly_white',
        hovermode='x unified',
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Multi-dimensional comparison
    st.markdown('<h2 class="section-header">📊 PERFORMANCE BREAKDOWN</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals + Assists stacked bar
        categories = ['Goals', 'Assists', 'G+A Total']
        messi_vals = [815, 377, 1192]
        ronaldo_vals = [895, 236, 1131]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_vals,
            marker_color='#4ECDC4',
            text=messi_vals,
            textposition='auto',
            textfont=dict(color='white', size=14, family='Arial Black')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_vals,
            marker_color='#FF6B6B',
            text=ronaldo_vals,
            textposition='auto',
            textfont=dict(color='white', size=14, family='Arial Black')
        ))
        
        fig.update_layout(
            title="⚽ Career Production",
            barmode='group',
            height=400,
            template='plotly_white',
            showlegend=True,
            yaxis=dict(range=[0, 1300])
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Trophy distribution pie charts
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type':'pie'}, {'type':'pie'}]],
            subplot_titles=['🇦🇷 Messi (44 total)', '🇵🇹 Ronaldo (35 total)']
        )
        
        # Messi trophies
        messi_trophies = ['League (12)', 'Champions League (4)', 'Cups (7)', 'International (4)', 'Others (17)']
        messi_values = [12, 4, 7, 4, 17]
        
        fig.add_trace(go.Pie(
            labels=messi_trophies,
            values=messi_values,
            marker_colors=['#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#A8E6CF'],
            hole=0.3
        ), row=1, col=1)
        
        # Ronaldo trophies
        ronaldo_trophies = ['League (7)', 'Champions League (5)', 'Cups (4)', 'International (3)', 'Others (16)']
        ronaldo_values = [7, 5, 4, 3, 16]
        
        fig.add_trace(go.Pie(
            labels=ronaldo_trophies,
            values=ronaldo_values,
            marker_colors=['#FF6B6B', '#FF9999', '#FD79A8', '#FDCB6E', '#FFB3BA'],
            hole=0.3
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="🏆 Trophy Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    # Age performance analysis
    st.markdown('<h2 class="section-header">⏰ LONGEVITY ANALYSIS</h2>', unsafe_allow_html=True)
    
    # Age performance heatmap
    age_ranges = ['18-23', '24-29', '30-35', '36+']
    metrics = ['Goals/Season', 'Assists/Season', 'Trophies', 'Individual Awards']
    
    # Performance scores (normalized to 0-100)
    messi_performance = [
        [70, 85, 75, 60],  # Goals by age range
        [60, 90, 85, 70],  # Assists by age range  
        [80, 90, 70, 50],  # Trophies by age range
        [60, 85, 80, 75]   # Awards by age range
    ]
    
    ronaldo_performance = [
        [60, 80, 90, 40],  # Goals by age range
        [40, 60, 70, 30],  # Assists by age range
        [70, 85, 80, 30],  # Trophies by age range
        [50, 75, 85, 20]   # Awards by age range
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure(data=go.Heatmap(
            z=messi_performance,
            x=age_ranges,
            y=metrics,
            colorscale=[[0, '#E8F8F7'], [1, '#4ECDC4']],
            text=messi_performance,
            texttemplate='%{text}',
            textfont=dict(size=12, color='white'),
            hoverongaps=False
        ))
        fig.update_layout(
            title="🇦🇷 Messi Performance by Age",
            height=300,
            xaxis_title="Age Range",
            yaxis_title="Performance Metric"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = go.Figure(data=go.Heatmap(
            z=ronaldo_performance,
            x=age_ranges,
            y=metrics,
            colorscale=[[0, '#FFE5E5'], [1, '#FF6B6B']],
            text=ronaldo_performance,
            texttemplate='%{text}',
            textfont=dict(size=12, color='white'),
            hoverongaps=False
        ))
        fig.update_layout(
            title="🇵🇹 Ronaldo Performance by Age",
            height=300,
            xaxis_title="Age Range",
            yaxis_title="Performance Metric"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Interactive comparison dashboard
    st.markdown('<h2 class="section-header">🎯 QUICK FACTS DASHBOARD</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="margin: 0;">1,710+</h3>
            <p style="margin: 0;">Combined Goals</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #f093fb, #f5576c); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="margin: 0;">36</h3>
            <p style="margin: 0;">El Clasico Meetings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #4facfe, #00f2fe); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="margin: 0;">13</h3>
            <p style="margin: 0;">Ballon d'Or Awards</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #43e97b, #38f9d7); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="margin: 0;">15+</h3>
            <p style="margin: 0;">Years of Rivalry</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Final comparison with visual verdict
    st.markdown('<h2 class="section-header">🏁 THE GOAT DEBATE</h2>', unsafe_allow_html=True)
    
    # Create a scorecard visualization
    categories = ['Goals', 'Assists', 'Trophies', 'Individual Awards', 'Longevity', 'Big Games']
    messi_scores = [90, 100, 95, 100, 95, 90]
    ronaldo_scores = [100, 70, 85, 80, 100, 100]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=messi_scores,
        theta=categories,
        fill='toself',
        name='Messi',
        fillcolor='rgba(78, 205, 196, 0.5)',
        line=dict(color='#4ECDC4', width=4),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=ronaldo_scores,
        theta=categories,
        fill='toself',
        name='Ronaldo',
        fillcolor='rgba(255, 107, 107, 0.5)',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                ticksuffix='%'
            )
        ),
        showlegend=True,
        title="🐐 GOAT Scorecard - Who Wins Each Category?",
        height=600,
        font=dict(size=14)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Interactive GOAT poll
    st.markdown('<h3 class="section-header">🎮 Cast Your Vote</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        goat_choice = st.radio(
            "Who is the GOAT?",
            ["🇦🇷 Messi", "🇵🇹 Ronaldo", "🤝 Both"],
            horizontal=True,
            key="goat_poll"
        )
        
        if goat_choice:
            if "Messi" in goat_choice:
                st.success("🇦🇷 Team Messi! Natural genius and pure artistry!")
            elif "Ronaldo" in goat_choice:
                st.success("🇵🇹 Team Ronaldo! Athletic perfection and goal machine!")
            else:
                st.info("🤝 Both legends! They've elevated each other to greatness!")
    
    # Navigation prompt
    
if __name__ == "__main__":
    show()