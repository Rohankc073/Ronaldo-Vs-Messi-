import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the career statistics page"""
    st.markdown('<h1 class="section-header">📊 CAREER STATISTICS DEEP DIVE</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    career_stats = data['career_stats']
    season_goals = data['season_goals']
    
    # Overview metrics
    st.markdown('<h3 class="section-header">⚡ Career Overview Metrics</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.metric("Total Goals", 
                 f"Messi: {career_stats.iloc[0]['goals']}", 
                 f"vs Ronaldo: {career_stats.iloc[1]['goals']}")
        st.caption("🇵🇹 Ronaldo leads by 80")
    
    with col2:
        st.metric("Total Assists", 
                 f"Messi: {career_stats.iloc[0]['assists']}", 
                 f"vs Ronaldo: {career_stats.iloc[1]['assists']}")
        st.caption("🇦🇷 Messi leads by 141")
    
    with col3:
        st.metric("Goals + Assists", 
                 f"Messi: {career_stats.iloc[0]['goals'] + career_stats.iloc[0]['assists']}", 
                 f"vs Ronaldo: {career_stats.iloc[1]['goals'] + career_stats.iloc[1]['assists']}")
        st.caption("🇦🇷 Messi leads by 61")
    
    with col4:
        st.metric("Goals per 90min", 
                 f"Messi: {career_stats.iloc[0]['goalsPer90']}", 
                 f"vs Ronaldo: {career_stats.iloc[1]['goalsPer90']}")
        st.caption("🇦🇷 Messi leads slightly")
    
    with col5:
        st.metric("Assists per 90min", 
                 f"Messi: {career_stats.iloc[0]['assistsPer90']}", 
                 f"vs Ronaldo: {career_stats.iloc[1]['assistsPer90']}")
        st.caption("🇦🇷 Messi dominates")
    
    with col6:
        st.metric("Total Matches", 
                 f"Messi: {career_stats.iloc[0]['matches']}", 
                 f"vs Ronaldo: {career_stats.iloc[1]['matches']}")
        st.caption("🇵🇹 Ronaldo played 136 more")
    
    # Main comparison charts
    st.markdown('<h3 class="section-header">📈 Statistical Comparison Charts</h3>', unsafe_allow_html=True)
    
    # Goals and Assists comparison
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure()
        categories = ['Goals', 'Assists', 'Goals per 90', 'Assists per 90']
        messi_stats = [815, 377, 0.76, 0.35]
        ronaldo_stats = [895, 236, 0.74, 0.20]
        
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_stats,
            marker_color='#4ECDC4',
            text=messi_stats,
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_stats,
            marker_color='#FF6B6B',
            text=ronaldo_stats,
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🎯 Goals & Assists Comparison",
            barmode='group',
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Efficiency radar chart
        categories_radar = ['Goals per 90', 'Assists per 90', 'Shot Accuracy', 'Conversion Rate', 'Key Passes', 'Big Chances']
        messi_radar = [76, 35, 45, 18, 95, 85]
        ronaldo_radar = [74, 20, 43, 15, 65, 92]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_radar,
            theta=categories_radar,
            fill='toself',
            name='Messi',
            fillcolor='rgba(78, 205, 196, 0.3)',
            line_color='#4ECDC4'
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_radar,
            theta=categories_radar,
            fill='toself',
            name='Ronaldo',
            fillcolor='rgba(255, 107, 107, 0.3)',
            line_color='#FF6B6B'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="⚡ Efficiency Radar Chart",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Season by season analysis
    st.markdown('<h3 class="section-header">📅 Season-by-Season Performance</h3>', unsafe_allow_html=True)
    
    # Goals timeline
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=season_goals['year'],
        y=season_goals['messiGoals'],
        mode='lines+markers',
        name='Messi Goals',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Messi</b><br>Year: %{x}<br>Goals: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=season_goals['year'],
        y=season_goals['ronaldoGoals'],
        mode='lines+markers',
        name='Ronaldo Goals',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Ronaldo</b><br>Year: %{x}<br>Goals: %{y}<extra></extra>'
    ))
    
    # Add peak annotations
    fig.add_annotation(
        x=2012, y=73,
        text="🏆 Messi's Legendary<br>91 Goals in 2012",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#4ECDC4",
        arrowwidth=2,
        bgcolor="white",
        bordercolor="#4ECDC4",
        borderwidth=2
    )
    fig.add_annotation(
        x=2014, y=61,
        text="👑 Ronaldo's Peak<br>CL & Ballon d'Or",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#FF6B6B",
        arrowwidth=2,
        bgcolor="white",
        bordercolor="#FF6B6B",
        borderwidth=2
    )
    
    fig.update_layout(
        title="🎯 Goals Per Season Timeline (2005-2023)",
        xaxis_title="Season",
        yaxis_title="Goals Scored",
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Advanced statistics
    st.markdown('<h3 class="section-header">🔬 Advanced Statistics</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goal scoring efficiency
        efficiency_data = pd.DataFrame({
            'Player': ['Messi', 'Ronaldo'],
            'Conversion Rate': [17.8, 15.2],
            'Goals per 90': [0.76, 0.74],
            'Minutes per Goal': [118, 121]
        })
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Conversion Rate (%)',
            x=efficiency_data['Player'],
            y=efficiency_data['Conversion Rate'],
            marker_color=['#4ECDC4', '#FF6B6B'],
            text=efficiency_data['Conversion Rate'],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🎯 Goal Scoring Efficiency",
            yaxis_title="Conversion Rate (%)",
            height=300,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Assists comparison
        assists_data = pd.DataFrame({
            'Player': ['Messi', 'Ronaldo'],
            'Total Assists': [377, 236],
            'Assists per 90': [0.35, 0.20]
        })
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Total Assists',
            x=assists_data['Player'],
            y=assists_data['Total Assists'],
            marker_color=['#4ECDC4', '#FF6B6B'],
            text=assists_data['Total Assists'],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🎨 Playmaking Statistics",
            yaxis_title="Total Assists",
            height=300,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Skills comparison
        skills_data = pd.DataFrame({
            'Skill': ['Dribbles Completed', 'Key Passes', 'Chances Created', 'Shot Accuracy %', 'Penalty Conversion %'],
            'Messi': [2847, 4521, 3254, 45.2, 77.8],
            'Ronaldo': [1456, 2847, 2108, 42.8, 84.3]
        })
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            y=skills_data['Skill'],
            x=skills_data['Messi'],
            orientation='h',
            marker_color='#4ECDC4',
            text=skills_data['Messi'],
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            y=skills_data['Skill'],
            x=skills_data['Ronaldo'],
            orientation='h',
            marker_color='#FF6B6B',
            text=skills_data['Ronaldo'],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🛠️ Technical Skills Comparison",
            barmode='group',
            height=500,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Peak seasons analysis
    st.markdown('<h3 class="section-header">🏔️ Peak Seasons Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🇦🇷 Messi's Best Seasons</h4>
            <p><strong>2011-12:</strong> 73 goals, 91 calendar year record</p>
            <p><strong>2009-10:</strong> 47 goals, first true peak</p>
            <p><strong>2015-16:</strong> 58 goals, treble winner</p>
            <p><strong>2018-19:</strong> 51 goals, individual brilliance</p>
            <hr>
            <p><strong>Peak Average:</strong> 57.3 goals per season</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>🇵🇹 Ronaldo's Best Seasons</h4>
            <p><strong>2013-14:</strong> 61 goals, La Décima winner</p>
            <p><strong>2014-15:</strong> 61 goals, consistent excellence</p>
            <p><strong>2011-12:</strong> 60 goals, peak Real Madrid form</p>
            <p><strong>2015-16:</strong> 51 goals, Champions League hero</p>
            <hr>
            <p><strong>Peak Average:</strong> 58.3 goals per season</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏆 Peak Comparison</h4>
            <p><strong>Highest Single Season:</strong></p>
            <p>🇦🇷 Messi: 73 goals (2011-12)</p>
            <p>🇵🇹 Ronaldo: 61 goals (2013-14)</p>
            <hr>
            <p><strong>Most Consistent Peak:</strong></p>
            <p>🇵🇹 Ronaldo: 4 seasons with 50+ goals</p>
            <p>🇦🇷 Messi: 6 seasons with 50+ goals</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Longevity analysis
    st.markdown('<h3 class="section-header">⏰ Longevity & Consistency</h3>', unsafe_allow_html=True)
    
    # Age performance chart
    age_data = {
        'Age Range': ['20-25', '26-30', '31-35', '36-40'],
        'Messi Goals per Season': [28.5, 52.3, 41.2, 18.7],
        'Ronaldo Goals per Season': [31.2, 48.6, 38.4, 24.5]
    }
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=age_data['Age Range'],
        y=age_data['Messi Goals per Season'],
        mode='lines+markers',
        name='Messi',
        line=dict(color='#4ECDC4', width=4),
        marker=dict(size=10)
    ))
    fig.add_trace(go.Scatter(
        x=age_data['Age Range'],
        y=age_data['Ronaldo Goals per Season'],
        mode='lines+markers',
        name='Ronaldo',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title="📈 Goals per Season by Age Range",
        xaxis_title="Age Range",
        yaxis_title="Average Goals per Season",
        height=400,
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Career milestones
    st.markdown('<h3 class="section-header">🎯 Career Milestones</h3>', unsafe_allow_html=True)
    
    milestones_data = {
        'Milestone': ['100 Goals', '200 Goals', '300 Goals', '400 Goals', '500 Goals', '600 Goals', '700 Goals', '800 Goals'],
        'Messi Age': [20.1, 22.4, 24.2, 25.8, 27.6, 29.9, 32.1, 35.2],
        'Ronaldo Age': [21.3, 23.8, 25.9, 27.4, 28.7, 30.8, 33.2, 36.1],
        'Messi Games': [147, 284, 365, 435, 520, 683, 792, 1000],
        'Ronaldo Games': [197, 301, 426, 547, 634, 778, 911, 1082]
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=milestones_data['Messi Age'],
            y=[100, 200, 300, 400, 500, 600, 700, 800],
            mode='lines+markers',
            name='Messi',
            line=dict(color='#4ECDC4', width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=milestones_data['Ronaldo Age'],
            y=[100, 200, 300, 400, 500, 600, 700, 800],
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="⏱️ Age at Goal Milestones",
            xaxis_title="Age",
            yaxis_title="Goals Scored",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=milestones_data['Messi Games'],
            y=[100, 200, 300, 400, 500, 600, 700, 800],
            mode='lines+markers',
            name='Messi',
            line=dict(color='#4ECDC4', width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=milestones_data['Ronaldo Games'],
            y=[100, 200, 300, 400, 500, 600, 700, 800],
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="🎮 Games Needed for Milestones",
            xaxis_title="Games Played",
            yaxis_title="Goals Scored",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Statistical breakdown table
    st.markdown('<h3 class="section-header">📋 Complete Statistical Breakdown</h3>', unsafe_allow_html=True)
    
    complete_stats = {
        'Statistic': [
            'Total Goals', 'Total Assists', 'Goals + Assists', 'Matches Played', 
            'Goals per Match', 'Assists per Match', 'Minutes per Goal', 'Minutes per Assist',
            'Shot Conversion %', 'Penalty Conversion %', 'Free Kick Goals', 'Hat-tricks',
            'Goals from Outside Box', 'Headed Goals', 'Weak Foot Goals', 'Dribbles per Game'
        ],
        'Messi': [
            815, 377, 1192, 1069, 0.76, 0.35, 118, 269,
            17.8, 77.8, 65, 57, 89, 26, 118, 2.7
        ],
        'Ronaldo': [
            895, 236, 1131, 1205, 0.74, 0.20, 121, 450,
            15.2, 84.3, 62, 61, 156, 145, 312, 1.2
        ],
        'Winner': [
            '🇵🇹 Ronaldo', '🇦🇷 Messi', '🇦🇷 Messi', '🇵🇹 Ronaldo',
            '🇦🇷 Messi', '🇦🇷 Messi', '🇦🇷 Messi', '🇦🇷 Messi',
            '🇦🇷 Messi', '🇵🇹 Ronaldo', '🇦🇷 Messi', '🇵🇹 Ronaldo',
            '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇦🇷 Messi'
        ]
    }
    
    stats_df = pd.DataFrame(complete_stats)
    st.dataframe(stats_df, use_container_width=True, height=600)
    
    # Key insights
    st.markdown('<h3 class="section-header">💡 Key Statistical Insights</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Statistical Strengths:
        
        **🎨 Playmaking Dominance:**
        - 141 more assists than Ronaldo
        - 75% higher assists per game ratio
        - 58% more chances created
        
        **⚡ Efficiency Master:**
        - Higher goals per game (0.76 vs 0.74)
        - Better shot conversion (17.8% vs 15.2%)
        - Fewer minutes needed per goal
        
        **🎯 Technical Excellence:**
        - 95% more dribbles completed
        - 2.7 vs 1.2 dribbles per game
        - Superior key passes per game
        
        **🏆 Peak Performance:**
        - Highest single season: 73 goals
        - Most 50+ goal seasons: 6
        - Calendar year record: 91 goals
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Statistical Strengths:
        
        **⚽ Goal Machine:**
        - 80 more career goals than Messi
        - All-time leading scorer
        - 136 more matches played
        
        **💪 Physical Dominance:**
        - 145 headed goals vs Messi's 26
        - 312 weak foot goals vs Messi's 118
        - Superior penalty conversion (84.3% vs 77.8%)
        
        **🌍 Versatility:**
        - 156 goals from outside the box
        - Success across 4 major leagues
        - More goals at international level
        
        **⏰ Longevity Legend:**
        - Playing at elite level at age 40
        - Consistent 20+ goals per season
        - Maintained pace across 2 decades
        """)
    
    # Final statistical verdict
    st.markdown('<h3 class="section-header">🏁 Statistical Verdict</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="final-verdict-card">
        <h2>📊 The Numbers Don't Lie</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI LEADS IN:</h3>
                <p>✅ Assists (377 vs 236)</p>
                <p>✅ Goals + Assists (1,192 vs 1,131)</p>
                <p>✅ Goals per Game (0.76 vs 0.74)</p>
                <p>✅ Shot Conversion (17.8% vs 15.2%)</p>
                <p>✅ Dribbles & Key Passes</p>
            </div>
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO LEADS IN:</h3>
                <p>✅ Total Goals (895 vs 815)</p>
                <p>✅ Headed Goals (145 vs 26)</p>
                <p>✅ Penalty Conversion (84.3% vs 77.8%)</p>
                <p>✅ Weak Foot Goals (312 vs 118)</p>
                <p>✅ Longevity & Consistency</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Statistical Summary:</strong> Messi excels in creativity and efficiency, 
            while Ronaldo dominates in pure goal scoring and physical attributes.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()