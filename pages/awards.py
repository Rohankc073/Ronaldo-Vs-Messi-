import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the visual awards analysis page"""
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .awards-summary-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        border: 2px solid rgba(255,255,255,0.2);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .awards-summary-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.8s;
    }
    
    .awards-summary-card:hover::before {
        left: 100%;
    }
    
    .champion-badge {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #333;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .comparison-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin: 30px 0;
    }
    
    .player-awards-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
    }
    
    .player-awards-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .messi-card {
        border-left: 5px solid #75AADB;
    }
    
    .ronaldo-card {
        border-left: 5px solid #FF2D2D;
    }
    
    .award-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .award-item:last-child {
        border-bottom: none;
    }
    
    .award-count {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 5px 12px;
        border-radius: 15px;
        font-weight: bold;
        min-width: 40px;
        text-align: center;
    }
    
    .final-verdict {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 40px;
        text-align: center;
        margin: 40px 0;
        position: relative;
        overflow: hidden;
    }
    
    .trophy-icon {
        font-size: 4rem;
        margin: 20px 0;
        animation: rotate 3s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="section-header">🏅 INDIVIDUAL AWARDS & ACHIEVEMENTS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    
    # Page introduction
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: #75AADB; font-size: 2rem; font-family: 'Times New Roman', serif;">🏆 Individual Excellence Analysis</h2>
        <p style="font-size: 1.1rem; color: #ccc; font-family: 'Times New Roman', serif;">Awards, recognitions, and individual achievements comparison</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    # Player awards overview cards
    col1, col2 = st.columns(2)
    
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
            <h2 style="margin: 0;">🇦🇷 MESSI'S AWARDS</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                <div><strong style="font-size: 2rem;">8</strong><br><small>Ballon d'Or</small></div>
                <div><strong style="font-size: 2rem;">3</strong><br><small>FIFA Best</small></div>
                <div><strong style="font-size: 2rem;">6</strong><br><small>Golden Boot</small></div>
                <div><strong style="font-size: 2rem;">21</strong><br><small>Major Awards</small></div>
            </div>
            <p style="margin: 0; opacity: 0.9; font-style: italic;">"The Award King"</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
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
            <h2 style="margin: 0;">🇵🇹 RONALDO'S AWARDS</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                <div><strong style="font-size: 2rem;">5</strong><br><small>Ballon d'Or</small></div>
                <div><strong style="font-size: 2rem;">2</strong><br><small>FIFA Best</small></div>
                <div><strong style="font-size: 2rem;">4</strong><br><small>Golden Boot</small></div>
                <div><strong style="font-size: 2rem;">17</strong><br><small>Major Awards</small></div>
            </div>
            <p style="margin: 0; opacity: 0.9; font-style: italic;">"Global Icon"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick comparison metrics
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">⚡ AWARDS QUICK STATS</h2>', unsafe_allow_html=True)
    
    # Create comparison radar chart
    categories = ['Ballon d\'Or', 'FIFA Awards', 'Golden Boots', 'League Awards', 'International Recognition', 'Legacy Score']
    
    # Normalize values (higher is better for awards)
    messi_values = [100, 90, 95, 85, 90, 98]  # Messi's strengths
    ronaldo_values = [75, 80, 85, 90, 95, 85]  # Ronaldo's strengths
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=messi_values,
        theta=categories,
        fill='toself',
        name='Messi',
        fillcolor=f'rgba(117, 170, 219, 0.4)',
        line=dict(color=MESSI_COLOR, width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=ronaldo_values,
        theta=categories,
        fill='toself',
        name='Ronaldo',
        fillcolor=f'rgba(255, 45, 45, 0.4)',
        line=dict(color=RONALDO_COLOR, width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=True,
        title="🏆 Awards & Recognition Comparison",
        height=500,
        font=dict(size=14, family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Ballon d'Or Timeline
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🥇 BALLON D\'OR TIMELINE</h2>', unsafe_allow_html=True)
    
    # Create enhanced timeline
    years = list(range(2007, 2024))
    winners = []
    colors = []
    hover_texts = []
    
    # Define winners for each year
    ballon_dor_data = {
        2007: ('Kaká', '#9B59B6', '🇧🇷 Kaká'),
        2008: ('Ronaldo', RONALDO_COLOR, '🇵🇹 Cristiano Ronaldo'),
        2009: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2010: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2011: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2012: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2013: ('Ronaldo', RONALDO_COLOR, '🇵🇹 Cristiano Ronaldo'),
        2014: ('Ronaldo', RONALDO_COLOR, '🇵🇹 Cristiano Ronaldo'),
        2015: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2016: ('Ronaldo', RONALDO_COLOR, '🇵🇹 Cristiano Ronaldo'),
        2017: ('Ronaldo', RONALDO_COLOR, '🇵🇹 Cristiano Ronaldo'),
        2018: ('Modrić', '#FFD700', '🇭🇷 Luka Modrić'),
        2019: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2020: ('Cancelled', '#95A5A6', '❌ Cancelled (COVID-19)'),
        2021: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi'),
        2022: ('Benzema', '#E67E22', '🇫🇷 Karim Benzema'),
        2023: ('Messi', MESSI_COLOR, '🇦🇷 Lionel Messi')
    }
    
    for year in years:
        if year in ballon_dor_data:
            winner_info = ballon_dor_data[year]
            winners.append(winner_info[0])
            colors.append(winner_info[1])
            hover_texts.append(winner_info[2])
    
    fig = go.Figure()
    
    # Add timeline line
    fig.add_trace(go.Scatter(
        x=years,
        y=[1] * len(years),
        mode='lines',
        line=dict(color='rgba(100, 100, 100, 0.3)', width=3),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add timeline points
    for i, (year, winner, color, hover_text) in enumerate(zip(years, winners, colors, hover_texts)):
        symbol = 'star' if 'Messi' in winner else 'diamond' if 'Ronaldo' in winner else 'circle'
        size = 35 if winner in ['Messi', 'Ronaldo'] else 30
        
        fig.add_trace(go.Scatter(
            x=[year],
            y=[1],
            mode='markers',
            marker=dict(
                size=size, 
                color=color, 
                symbol=symbol,
                line=dict(width=3, color='white'),
                opacity=0.9
            ),
            name=winner,
            showlegend=False,
            hovertemplate=f'<b>{year}</b><br>{hover_text}<br><extra></extra>'
        ))
    
    # Add era highlights
    fig.add_shape(
        type="rect", 
        x0=2008.5, y0=0.7, x1=2012.5, y1=1.3,
        fillcolor=f"rgba(117, 170, 219, 0.2)", 
        line=dict(width=2, color=MESSI_COLOR, dash='dot')
    )
    fig.add_shape(
        type="rect", 
        x0=2012.5, y0=0.7, x1=2017.5, y1=1.3,
        fillcolor=f"rgba(255, 45, 45, 0.2)", 
        line=dict(width=2, color=RONALDO_COLOR, dash='dot')
    )
    
    # Enhanced annotations
    fig.add_annotation(
        x=2010.5, y=1.5, 
        text="<b>Messi Era 1</b><br>4 consecutive wins", 
        showarrow=True,
        arrowhead=2,
        arrowcolor=MESSI_COLOR,
        font=dict(size=12, color=MESSI_COLOR, family='Times New Roman'),
        bgcolor=f"rgba(117, 170, 219, 0.1)",
        bordercolor=MESSI_COLOR,
        borderwidth=1
    )
    fig.add_annotation(
        x=2015, y=0.5, 
        text="<b>Ronaldo Peak</b><br>4 out of 5 years", 
        showarrow=True,
        arrowhead=2,
        arrowcolor=RONALDO_COLOR,
        font=dict(size=12, color=RONALDO_COLOR, family='Times New Roman'),
        bgcolor=f"rgba(255, 45, 45, 0.1)",
        bordercolor=RONALDO_COLOR,
        borderwidth=1
    )
    fig.add_annotation(
        x=2021, y=1.5, 
        text="<b>Messi Era 2</b><br>Record 8th Ballon d'Or", 
        showarrow=True,
        arrowhead=2,
        arrowcolor=MESSI_COLOR,
        font=dict(size=12, color=MESSI_COLOR, family='Times New Roman'),
        bgcolor=f"rgba(117, 170, 219, 0.1)",
        bordercolor=MESSI_COLOR,
        borderwidth=1
    )
    
    fig.update_layout(
        title="🏆 Ballon d'Or Winners (2007-2023)",
        height=400,
        yaxis=dict(visible=False, range=[0.3, 1.7]),
        xaxis=dict(
            title="Year",
            showgrid=True,
            gridcolor='rgba(200, 200, 200, 0.3)',
            dtick=1
        ),
        template='plotly_white',
        hovermode='closest',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Awards breakdown by category
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🎯 AWARDS BREAKDOWN BY CATEGORY</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Major individual awards
        awards = ['Ballon d\'Or', 'FIFA Best', 'Golden Boot', 'UEFA Player', 'World Cup Golden Ball']
        messi_counts = [8, 3, 6, 3, 1]
        ronaldo_counts = [5, 2, 4, 3, 0]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=awards,
            y=messi_counts,
            marker_color=MESSI_COLOR,
            text=messi_counts,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=awards,
            y=ronaldo_counts,
            marker_color=RONALDO_COLOR,
            text=ronaldo_counts,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🏆 Major Individual Awards",
            barmode='group',
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Awards by decade pie chart
        decades = ['2000s', '2010s', '2020s']
        messi_decade_awards = [2, 15, 4]  # Including all major awards
        
        fig = go.Figure(data=[go.Pie(
            labels=decades,
            values=messi_decade_awards,
            hole=0.4,
            marker_colors=['#96CEB4', MESSI_COLOR, '#45B7D1'],
            textinfo='label+percent+value',
            textfont=dict(family='Times New Roman')
        )])
        
        fig.update_layout(
            title="🇦🇷 Messi Awards by Decade",
            height=400,
            annotations=[dict(
                text='21<br>Total', 
                x=0.5, y=0.5, 
                font=dict(size=20, color='#2C3E50', family='Times New Roman'), 
                showarrow=False
            )],
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # League vs International awards
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🏟️ LEAGUE VS INTERNATIONAL AWARDS</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # League awards
        league_awards = ['La Liga MVP', 'Premier League POTY', 'Serie A MVP', 'League Top Scorer']
        messi_league = [6, 0, 0, 8]
        ronaldo_league = [2, 2, 2, 7]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=league_awards,
            x=messi_league,
            name='Messi',
            orientation='h',
            marker_color=MESSI_COLOR,
            text=messi_league,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            y=league_awards,
            x=ronaldo_league,
            name='Ronaldo',
            orientation='h',
            marker_color=RONALDO_COLOR,
            text=ronaldo_league,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🏟️ League Awards",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="margin-top: 0;">🌍 International Recognition</h3>
            <div style="font-size: 2rem; margin: 1rem 0;">🇦🇷 vs 🇵🇹</div>
            <p><strong>Messi:</strong> World Cup Winner 2022</p>
            <p><strong>Ronaldo:</strong> Euro Winner 2016</p>
            <p><strong>World Cup Golden Ball:</strong> Messi ✅</p>
            <p style="margin-bottom: 0;"><strong>Winner:</strong> 🇦🇷 Messi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #f093fb, #f5576c);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="margin-top: 0;">🏅 Lifetime Achievement</h3>
            <div style="font-size: 2rem; margin: 1rem 0;">📊 Legacy Score</div>
            <p><strong>Messi:</strong> 9.8/10 legacy rating</p>
            <p><strong>Ronaldo:</strong> 9.5/10 legacy rating</p>
            <p><strong>Most Awards:</strong> Messi ✅</p>
            <p style="margin-bottom: 0;"><strong>Winner:</strong> 🇦🇷 Messi</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Awards timeline evolution
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">📈 AWARDS EVOLUTION OVER TIME</h2>', unsafe_allow_html=True)
    
    # Career awards progression
    years_career = list(range(2005, 2024))
    messi_cumulative_awards = [0, 1, 2, 3, 5, 8, 10, 12, 14, 16, 17, 18, 19, 20, 21, 21, 21, 21, 21]
    ronaldo_cumulative_awards = [0, 1, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 17, 17, 17, 17, 17, 17, 17]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years_career,
        y=messi_cumulative_awards,
        mode='lines+markers',
        name='Messi Cumulative Awards',
        line=dict(color=MESSI_COLOR, width=4),
        marker=dict(size=8, line=dict(width=2, color='white')),
        fill='tonexty'
    ))
    fig.add_trace(go.Scatter(
        x=years_career,
        y=ronaldo_cumulative_awards,
        mode='lines+markers',
        name='Ronaldo Cumulative Awards',
        line=dict(color=RONALDO_COLOR, width=4),
        marker=dict(size=8, line=dict(width=2, color='white')),
        fill='tozeroy'
    ))
    
    fig.update_layout(
        title="📈 Cumulative Major Awards Over Career",
        xaxis_title="Year",
        yaxis_title="Total Major Awards",
        height=400,
        template='plotly_white',
        hovermode='x unified',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # NEW IMPROVED FINAL AWARDS VERDICT - Using Streamlit native components
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🏁 AWARDS VERDICT</h2>', unsafe_allow_html=True)
    
    # Modern Awards Summary Cards using simple Streamlit styling
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); border-radius: 20px; padding: 25px; border-left: 5px solid {MESSI_COLOR}; font-family: 'Times New Roman', serif;">
                <h3 style="color: {MESSI_COLOR}; text-align: center; margin-bottom: 20px;">🇦🇷 MESSI - THE AWARDS KING</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Use metrics for clean display
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("🏆 Ballon d'Or Awards")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">8</span>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("🌟 FIFA Best Player")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">3</span>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("👑 Golden Boot Awards")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">6</span>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("🌍 World Cup Golden Ball")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">1</span>', unsafe_allow_html=True)
            
            st.divider()
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown("**🎯 Total Major Awards**")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, {MESSI_COLOR}, #5a9bd4); color: white; padding: 8px 15px; border-radius: 15px; font-weight: bold; font-size: 1.2rem;">21</span>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); border-radius: 20px; padding: 25px; border-left: 5px solid {RONALDO_COLOR}; font-family: 'Times New Roman', serif;">
                <h3 style="color: {RONALDO_COLOR}; text-align: center; margin-bottom: 20px;">🇵🇹 RONALDO - THE GLOBAL ICON</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Use metrics for clean display
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("🏆 Ballon d'Or Awards")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">5</span>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("🌟 FIFA Best Player")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">2</span>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("👑 Golden Boot Awards")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">4</span>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write("🌍 Multi-League Success")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold;">3</span>', unsafe_allow_html=True)
            
            st.divider()
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown("**🎯 Total Major Awards**")
            with col_b:
                st.markdown(f'<span style="background: linear-gradient(45deg, {RONALDO_COLOR}, #e02525); color: white; padding: 8px 15px; border-radius: 15px; font-weight: bold; font-size: 1.2rem;">17</span>', unsafe_allow_html=True)
    
    # Final Verdict Card - Custom designed winner section
    st.markdown("---")
    
    # Champion Announcement with custom styling
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {MESSI_COLOR} 0%, #5a9bd4 100%);
        color: white;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 30px 0;
        font-family: 'Times New Roman', serif;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    ">
        <div style="font-size: 3rem; margin-bottom: 10px;">🏆</div>
        <h2 style="font-size: 2rem; margin: 0 0 20px 0;">AWARDS CHAMPION</h2>
        <div style="
            background: linear-gradient(45deg, #FFD700, #FFA500);
            color: #333;
            padding: 15px 30px;
            border-radius: 50px;
            font-weight: bold;
            font-size: 1.3rem;
            display: inline-block;
            box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4);
        ">
            🇦🇷 LIONEL MESSI - THE MOST DECORATED PLAYER
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom Statistics Cards
    st.markdown("""
    <div style="margin: 30px 0;">
        <h3 style="text-align: center; font-family: 'Times New Roman', serif; margin-bottom: 25px; color: #FFD700;">
            📊 MESSI'S DECISIVE ADVANTAGES
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create three custom metric cards
    col1, col2, col3 = st.columns(3)
    
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
            transition: transform 0.3s ease;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏆</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 15px 0;">Ballon d'Or Dominance</h4>
            <div style="
                font-size: 3rem; 
                font-weight: 900; 
                color: #FFD700; 
                margin: 10px 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            ">+3</div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                margin-top: 10px;
            ">8 vs 5 Awards</div>
            <p style="margin-top: 15px; opacity: 0.9; font-size: 0.9rem;">Record-breaking supremacy</p>
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
            border: 2px solid #FFD700;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">👑</div>
            <h4 style="color: #FFD700; margin: 0 0 15px 0;">Golden Boot Excellence</h4>
            <div style="
                font-size: 3rem; 
                font-weight: 900; 
                color: #FFD700; 
                margin: 10px 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            ">+2</div>
            <div style="
                background: #FFD700; 
                color: #333; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                margin-top: 10px;
            ">6 vs 4 Awards</div>
            <p style="margin-top: 15px; opacity: 0.9; font-size: 0.9rem;">Scoring championship leader</p>
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
            border: 2px solid #FF6B35;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🎯</div>
            <h4 style="color: #FF6B35; margin: 0 0 15px 0;">Total Awards Mastery</h4>
            <div style="
                font-size: 3rem; 
                font-weight: 900; 
                color: #FFD700; 
                margin: 10px 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            ">+4</div>
            <div style="
                background: #FF6B35; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                margin-top: 10px;
            ">21 vs 17 Awards</div>
            <p style="margin-top: 15px; opacity: 0.9; font-size: 0.9rem;">Most decorated player ever</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key advantages
    st.info("""
    🎯 **Key Advantages:**
    - ✅ Most Ballon d'Or awards in history
    - ✅ World Cup Golden Ball winner  
    - ✅ Highest individual recognition rate
    - ✅ Most consistent award winner
    """)
    
    st.markdown("""
    **Conclusion:** Messi's record-breaking 8 Ballon d'Or awards and 21 total major individual honors 
    cement his status as the most decorated player in football history.
    """)
    
    # Interactive awards quiz
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🎮 Awards Knowledge Quiz</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        quiz_question = st.radio(
            "Who has won more Ballon d'Or awards?",
            ["🇦🇷 Messi with 8 awards", "🇵🇹 Ronaldo with 5 awards", "🤝 They're tied"],
            key="awards_quiz"
        )
        
        if quiz_question:
            if "Messi" in quiz_question:
                st.success("🇦🇷 Correct! Messi has a record-breaking 8 Ballon d'Or awards!")
            elif "Ronaldo" in quiz_question:
                st.info("🇵🇹 Ronaldo has 5, but Messi leads with 8 Ballon d'Or awards!")
            else:
                st.warning("🤝 Not quite! Messi clearly leads 8-5 in Ballon d'Or awards!")
    
    # Navigation
    st.markdown("""
    ---
    ### 🔍 Continue Exploring
    
    **📊 Career Stats** • **🗺️ Heat Maps** • **🟨🟥 Disciplinary Records** • **🏁 Final Verdict**
    
    🎯 **Discover more aspects of the greatest rivalry in football!**
    """)

if __name__ == "__main__":
    show()