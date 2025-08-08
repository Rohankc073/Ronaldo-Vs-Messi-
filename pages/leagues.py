import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the leagues and competitions analysis page"""
    st.markdown('<h1 class="section-header">⚽ LEAGUES & COMPETITIONS MASTERY</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    league_data = data['league_stats']
    
    # Page introduction
    st.markdown("""
    **League mastery showcases adaptability and consistency.** How players perform across different leagues, 
    playing styles, and competitive environments reveals their true versatility. Messi dominated La Liga for 
    nearly two decades, while Ronaldo conquered four different top leagues. Let's analyze their league-specific 
    performances, records, and impact across competitions.
    """)
    
    # League overview
    st.markdown('<h3 class="section-header">🏟️ League Career Overview</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card">
            <h3>🇦🇷 MESSI'S LEAGUE JOURNEY</h3>
            <h4>🇪🇸 La Liga (2004-2021) - 17 seasons</h4>
            <p><strong>474 goals</strong> in 520 appearances</p>
            <p><strong>192 assists</strong> | <strong>0.91 G/G</strong></p>
            <p><strong>10 League titles</strong> | <strong>6 Golden Boots</strong></p>
            <p>All-time La Liga top scorer</p>
            
            <h4>🇫🇷 Ligue 1 (2021-2023) - 2 seasons</h4>
            <p><strong>16 goals</strong> in 67 appearances</p>
            <p><strong>35 assists</strong> | <strong>0.24 G/G</strong></p>
            <p><strong>2 League titles</strong> | Adaptation period</p>
            <p>Focus shifted to playmaking</p>
            
            <h4>🇺🇸 MLS (2023-present) - Current</h4>
            <p><strong>11+ goals</strong> in 14+ appearances</p>
            <p><strong>15+ assists</strong> | <strong>0.79 G/G</strong></p>
            <p><strong>1 Leagues Cup</strong> | Immediate impact</p>
            <p>Revolutionizing American soccer</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card">
            <h3>🇵🇹 RONALDO'S LEAGUE CONQUEST</h3>
            <h4>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League (2003-2009, 2021-2022)</h4>
            <p><strong>103 goals</strong> in 236 appearances</p>
            <p><strong>64 assists</strong> | <strong>0.44 G/G</strong></p>
            <p><strong>3 League titles</strong> | <strong>1 Golden Boot</strong></p>
            <p>From winger to superstar</p>
            
            <h4>🇪🇸 La Liga (2009-2018) - 9 seasons</h4>
            <p><strong>311 goals</strong> in 292 appearances</p>
            <p><strong>95 assists</strong> | <strong>1.07 G/G</strong></p>
            <p><strong>2 League titles</strong> | <strong>3 Golden Boots</strong></p>
            <p>Peak goal-scoring machine</p>
            
            <h4>🇮🇹 Serie A (2018-2021) - 3 seasons</h4>
            <p><strong>81 goals</strong> in 98 appearances</p>
            <p><strong>22 assists</strong> | <strong>0.83 G/G</strong></p>
            <p><strong>2 League titles</strong> | Tactical mastery</p>
            <p>Proved adaptability again</p>
            
            <h4>🇸🇦 Saudi Pro League (2023-present)</h4>
            <p><strong>35+ goals</strong> in 42+ appearances</p>
            <p><strong>18+ assists</strong> | <strong>0.83 G/G</strong></p>
            <p><strong>0 League titles</strong> | Global ambassador</p>
            <p>Elevating Middle East football</p>
        </div>
        """, unsafe_allow_html=True)
    
    # League goals comparison
    st.markdown('<h3 class="section-header">⚽ Goals by League Comparison</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals by league bar chart
        leagues = ['La Liga', 'Premier League', 'Serie A', 'Ligue 1', 'MLS', 'Saudi Pro League']
        messi_goals = [474, 0, 0, 16, 11, 0]
        ronaldo_goals = [311, 103, 81, 0, 0, 35]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=leagues,
            y=messi_goals,
            marker_color='#4ECDC4',
            text=messi_goals,
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=leagues,
            y=ronaldo_goals,
            marker_color='#FF6B6B',
            text=ronaldo_goals,
            textposition='auto'
        ))
        
        fig.update_layout(
            title="⚽ Goals by League",
            barmode='group',
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Goals per game by league
        leagues_gpg = ['La Liga', 'Premier League', 'Serie A', 'Ligue 1', 'MLS', 'Saudi Pro']
        messi_gpg = [0.91, 0, 0, 0.24, 0.79, 0]
        ronaldo_gpg = [1.07, 0.44, 0.83, 0, 0, 0.83]
        
        # Filter out zeros for cleaner visualization
        messi_leagues = [l for l, g in zip(leagues_gpg, messi_gpg) if g > 0]
        messi_gpg_filtered = [g for g in messi_gpg if g > 0]
        ronaldo_leagues = [l for l, g in zip(leagues_gpg, ronaldo_gpg) if g > 0]
        ronaldo_gpg_filtered = [g for g in ronaldo_gpg if g > 0]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=messi_leagues,
            y=messi_gpg_filtered,
            mode='lines+markers',
            name='Messi Goals/Game',
            line=dict(color='#4ECDC4', width=4),
            marker=dict(size=10)
        ))
        fig.add_trace(go.Scatter(
            x=ronaldo_leagues,
            y=ronaldo_gpg_filtered,
            mode='lines+markers',
            name='Ronaldo Goals/Game',
            line=dict(color='#FF6B6B', width=4),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="📈 Goals per Game by League",
            yaxis_title="Goals per Game",
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # League statistics detailed table
    st.markdown('<h3 class="section-header">📊 Detailed League Statistics</h3>', unsafe_allow_html=True)
    
    league_detailed = {
        'League': ['La Liga', 'Premier League', 'Serie A', 'Ligue 1', 'MLS', 'Saudi Pro League'],
        'Player': ['Both', 'Ronaldo Only', 'Ronaldo Only', 'Messi Only', 'Messi Only', 'Ronaldo Only'],
        'Messi Goals': [474, 0, 0, 16, 11, 0],
        'Ronaldo Goals': [311, 103, 81, 0, 0, 35],
        'Messi Apps': [520, 0, 0, 67, 14, 0],
        'Ronaldo Apps': [292, 236, 98, 0, 0, 42],
        'Messi G/G': [0.91, 0, 0, 0.24, 0.79, 0],
        'Ronaldo G/G': [1.07, 0.44, 0.83, 0, 0, 0.83],
        'Messi Titles': [10, 0, 0, 2, 0, 0],
        'Ronaldo Titles': [2, 3, 2, 0, 0, 0]
    }
    
    league_df = pd.DataFrame(league_detailed)
    st.dataframe(league_df, use_container_width=True, height=350)
    
    # League dominance analysis
    st.markdown('<h3 class="section-header">👑 League Dominance Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🇪🇸 La Liga Mastery</h4>
            <p><strong>🇦🇷 Messi: Absolute King</strong></p>
            <p>• 474 goals in 17 seasons</p>
            <p>• 10 league titles (record)</p>
            <p>• 6 Golden Boots in La Liga</p>
            <p>• All-time top scorer</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo: Elite Competitor</strong></p>
            <p>• 311 goals in 9 seasons</p>
            <p>• 2 league titles</p>
            <p>• 3 Golden Boots</p>
            <p>• 1.07 goals per game (better rate)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League Impact</h4>
            <p><strong>🇵🇹 Ronaldo: Only Player</strong></p>
            <p>• 103 goals in 236 appearances</p>
            <p>• 3 league titles with United</p>
            <p>• 1 Golden Boot (2007-08)</p>
            <p>• Two different spells</p>
            <hr>
            <p><strong>🇦🇷 Messi: Never Played</strong></p>
            <p>• 0 Premier League experience</p>
            <p>• Always wondered "what if"</p>
            <p>• Barcelona loyalty prevented move</p>
            <p>• PL remains unconquered</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>🌍 League Versatility</h4>
            <p><strong>🇵🇹 Ronaldo: 4 Leagues</strong></p>
            <p>• Premier League ✅</p>
            <p>• La Liga ✅</p>
            <p>• Serie A ✅</p>
            <p>• Saudi Pro League ✅</p>
            <hr>
            <p><strong>🇦🇷 Messi: 3 Leagues</strong></p>
            <p>• La Liga ✅ (Dominated)</p>
            <p>• Ligue 1 ✅ (Adapted)</p>
            <p>• MLS ✅ (Revolutionizing)</p>
            <p>• Fewer but deeper impact</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Seasonal performance analysis
    st.markdown('<h3 class="section-header">📈 Peak Seasonal Performances by League</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi's best seasons by league
        st.markdown("""
        ### 🇦🇷 Messi's Peak League Seasons:
        
        **🇪🇸 La Liga Peak Seasons:**
        - **2011-12**: 50 goals, 14 assists (Record)
        - **2012-13**: 46 goals, 12 assists
        - **2009-10**: 34 goals, 11 assists
        - **2018-19**: 36 goals, 13 assists (Age 31)
        
        **🇫🇷 Ligue 1 Performance:**
        - **2021-22**: 6 goals, 14 assists (Playmaker)
        - **2022-23**: 16 goals, 16 assists (Balanced)
        
        **🇺🇸 MLS Impact:**
        - **2023**: 11 goals, 15 assists in 14 games
        - Immediate transformation of Inter Miami
        - Leagues Cup winner in debut season
        
        **📊 Key Insights:**
        - Peak was La Liga 2011-12
        - Adapted role in Ligue 1
        - Instant impact in MLS
        """)
    
    with col2:
        # Ronaldo's best seasons by league
        st.markdown("""
        ### 🇵🇹 Ronaldo's Peak League Seasons:
        
        **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League Peak:**
        - **2007-08**: 31 goals, 6 assists (Breakthrough)
        - **2006-07**: 17 goals, 13 assists
        - **2021-22**: 18 goals, 3 assists (Return)
        
        **🇪🇸 La Liga Peak Seasons:**
        - **2014-15**: 48 goals, 16 assists (Peak)
        - **2011-12**: 46 goals, 12 assists
        - **2013-14**: 51 goals, 13 assists
        
        **🇮🇹 Serie A Excellence:**
        - **2019-20**: 31 goals, 5 assists
        - **2020-21**: 29 goals, 3 assists
        - Consistent 25+ goals each season
        
        **🇸🇦 Saudi Pro League:**
        - **2023-24**: 35+ goals in debut season
        - Immediate league transformation
        
        **📊 Key Insights:**
        - Peak was La Liga 2014-15
        - Consistent across all leagues
        - Adaptability champion
        """)
    
    # League records and achievements
    st.markdown('<h3 class="section-header">🏆 League Records & Achievements</h3>', unsafe_allow_html=True)
    
    # Create records comparison
    records_data = {
        'Record Category': [
            'Most Goals in Single League', 'Most League Titles', 'Most Golden Boots in League',
            'Highest Goals per Game (League)', 'Most Assists in Single League', 'Most League Appearances',
            'Youngest League Top Scorer', 'Oldest League Top Scorer', 'Most Hat-tricks in League',
            'Most League Rivalries Won', 'League MVP Awards', 'League Top Scorer Awards'
        ],
        'Messi': [
            '474 (La Liga)', '10 (La Liga)', '6 (La Liga)',
            '0.91 (La Liga)', '192 (La Liga)', '520 (La Liga)',
            '22 (La Liga)', '34 (La Liga)', '36 (La Liga)',
            '26 (El Clasico)', '6 (La Liga)', '8 (La Liga)'
        ],
        'Ronaldo': [
            '311 (La Liga)', '3 (Premier League)', '3 (La Liga)',
            '1.07 (La Liga)', '95 (La Liga)', '292 (La Liga)',
            '21 (Premier League)', '37 (Serie A)', '34 (La Liga)',
            '18 (El Clasico)', '2 (La Liga)', '7 (Multiple)'
        ],
        'Winner': [
            '🇦🇷 Messi', '🇦🇷 Messi', '🇦🇷 Messi',
            '🇵🇹 Ronaldo', '🇦🇷 Messi', '🇦🇷 Messi',
            '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇦🇷 Messi',
            '🇦🇷 Messi', '🇦🇷 Messi', '🇦🇷 Messi'
        ]
    }
    
    records_df = pd.DataFrame(records_data)
    st.dataframe(records_df, use_container_width=True, height=450)
    
    # League adaptation analysis
    st.markdown('<h3 class="section-header">🔄 League Adaptation Analysis</h3>', unsafe_allow_html=True)
    
    # Adaptation timeline
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('🎯 Goal Scoring Adaptation', '🎨 Playmaking Evolution', '⚡ Performance Consistency', '🏆 Success Rate by League'),
        specs=[[{"type": "scatter"}, {"type": "scatter"}],
               [{"type": "bar"}, {"type": "bar"}]]
    )
    
    # Goal scoring adaptation (first season in each league)
    leagues_adapt = ['La Liga', 'Premier League', 'Serie A', 'Ligue 1', 'MLS', 'Saudi Pro']
    messi_first_season = [0.3, 0, 0, 0.24, 0.79, 0]  # Goals per game in first season
    ronaldo_first_season = [0.3, 0.26, 0.61, 0, 0, 0.83]
    
    # Filter non-zero values
    messi_adapt_leagues = [l for l, g in zip(leagues_adapt, messi_first_season) if g > 0]
    messi_adapt_values = [g for g in messi_first_season if g > 0]
    ronaldo_adapt_leagues = [l for l, g in zip(leagues_adapt, ronaldo_first_season) if g > 0]
    ronaldo_adapt_values = [g for g in ronaldo_first_season if g > 0]
    
    fig.add_trace(go.Scatter(x=messi_adapt_leagues, y=messi_adapt_values, name='Messi Adaptation', line_color='#4ECDC4'), row=1, col=1)
    fig.add_trace(go.Scatter(x=ronaldo_adapt_leagues, y=ronaldo_adapt_values, name='Ronaldo Adaptation', line_color='#FF6B6B'), row=1, col=1)
    
    # Playmaking evolution (assists per season)
    messi_assists_evolution = [0.37, 0, 0, 0.52, 1.07, 0]
    ronaldo_assists_evolution = [0.33, 0.27, 0.22, 0, 0, 0.43]
    
    messi_assist_leagues = [l for l, a in zip(leagues_adapt, messi_assists_evolution) if a > 0]
    messi_assist_values = [a for a in messi_assists_evolution if a > 0]
    ronaldo_assist_leagues = [l for l, a in zip(leagues_adapt, ronaldo_assists_evolution) if a > 0]
    ronaldo_assist_values = [a for a in ronaldo_assists_evolution if a > 0]
    
    fig.add_trace(go.Scatter(x=messi_assist_leagues, y=messi_assist_values, name='Messi Assists/Game', line_color='#4ECDC4', showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=ronaldo_assist_leagues, y=ronaldo_assist_values, name='Ronaldo Assists/Game', line_color='#FF6B6B', showlegend=False), row=1, col=2)
    
    # Performance consistency (average goals per season)
    messi_consistency = [27.9, 0, 0, 8, 11, 0]
    ronaldo_consistency = [34.6, 17.2, 27, 0, 0, 35]
    
    messi_consist_leagues = [l for l, c in zip(leagues_adapt, messi_consistency) if c > 0]
    messi_consist_values = [c for c in messi_consistency if c > 0]
    ronaldo_consist_leagues = [l for l, c in zip(leagues_adapt, ronaldo_consistency) if c > 0]
    ronaldo_consist_values = [c for c in ronaldo_consistency if c > 0]
    
    fig.add_trace(go.Bar(x=messi_consist_leagues, y=messi_consist_values, name='Messi Avg Goals/Season', marker_color='#4ECDC4', showlegend=False), row=2, col=1)
    fig.add_trace(go.Bar(x=ronaldo_consist_leagues, y=ronaldo_consist_values, name='Ronaldo Avg Goals/Season', marker_color='#FF6B6B', showlegend=False), row=2, col=1)
    
    # Success rate (titles won / seasons played)
    messi_success_rate = [58.8, 0, 0, 100, 0, 0]  # Percentage
    ronaldo_success_rate = [22.2, 50, 66.7, 0, 0, 0]
    
    messi_success_leagues = [l for l, s in zip(leagues_adapt, messi_success_rate) if s > 0]
    messi_success_values = [s for s in messi_success_rate if s > 0]
    ronaldo_success_leagues = [l for l, s in zip(leagues_adapt, ronaldo_success_rate) if s > 0]
    ronaldo_success_values = [s for s in ronaldo_success_rate if s > 0]
    
    fig.add_trace(go.Bar(x=messi_success_leagues, y=messi_success_values, name='Messi Success Rate', marker_color='#4ECDC4', showlegend=False), row=2, col=2)
    fig.add_trace(go.Bar(x=ronaldo_success_leagues, y=ronaldo_success_values, name='Ronaldo Success Rate', marker_color='#FF6B6B', showlegend=False), row=2, col=2)
    
    fig.update_layout(height=600, title_text="📊 League Performance Analysis")
    st.plotly_chart(fig, use_container_width=True)
    
    # League style adaptation
    st.markdown('<h3 class="section-header">🎭 Playing Style by League</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's League Adaptations:
        
        **🇪🇸 La Liga (Perfect Fit):**
        - Technical league suited his style
        - Tiki-taka system optimization
        - False 9 revolution
        - Consistent 30+ goals per season
        
        **🇫🇷 Ligue 1 (Playmaker Role):**
        - Adapted to deeper position
        - Focus on assists over goals
        - Learning new tactical systems
        - PSG's creative hub
        
        **🇺🇸 MLS (Instant Impact):**
        - Perfect role as player-leader
        - Combination of goals and assists
        - Elevated entire league profile
        - Tactical freedom to roam
        
        **📊 Key Insight:**
        Messi adapts by changing his role rather than his style, becoming more of a playmaker in leagues where pure goal-scoring is harder.
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's League Conquests:
        
        **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League (Physical Development):**
        - From skillful winger to complete player
        - Learned physicality and pace
        - Developed aerial ability
        - Built elite mentality
        
        **🇪🇸 La Liga (Goal Machine Mode):**
        - Optimized for pure goal-scoring
        - Best goals-per-game ratio (1.07)
        - Clinical finishing perfection
        - Big game specialist
        
        **🇮🇹 Serie A (Tactical Master):**
        - Adapted to defensive league
        - Maintained high goal output
        - Proved tactical intelligence
        - Leadership role
        
        **🇸🇦 Saudi Pro League (Global Ambassador):**
        - Elevating league standard
        - Maintaining elite output
        - Cultural bridge builder
        
        **📊 Key Insight:**
        Ronaldo adapts by maximizing his physical and technical attributes for each league's specific demands while maintaining his core strengths.
        """)
    
    # Final leagues verdict
    st.markdown('<h3 class="section-header">🏁 League Mastery Verdict</h3>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>⚽ League Mastery Champion</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO: The League Conqueror</h3>
                <p>✅ Success in 4 different leagues</p>
                <p>✅ Proved adaptability across continents</p>
                <p>✅ Consistent performance in all leagues</p>
                <p>✅ Higher goals per game in La Liga (1.07)</p>
                <p>✅ Premier League proven (only one)</p>
                <p>✅ Versatility across playing styles</p>
                <p>✅ Global football ambassador</p>
            </div>
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI: The League Dominator</h3>
                <p>✅ Absolute La Liga king (474 goals)</p>
                <p>✅ More league titles (12 vs 7)</p>
                <p>✅ More league records and achievements</p>
                <p>✅ 6 Golden Boots in single league</p>
                <p>✅ Deeper impact where he played</p>
                <p>✅ Instant MLS transformation</p>
                <p>✅ Perfect adaptation in Ligue 1</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>League Winner:</strong> 🇵🇹 <strong>RONALDO</strong> - The ultimate league versatility champion!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final analysis
    st.markdown("""
    ---
    ### 🌟 League Mastery Legacy
    
    **🇵🇹 Ronaldo's league career represents the pinnacle of versatility** in modern football. His ability to 
    adapt and excel in four completely different leagues - from the physicality of the Premier League to the 
    tactical discipline of Serie A - is unmatched. He's proven that elite talent can transcend playing styles, 
    cultures, and tactical systems.
    
    **🇦🇷 Messi's league mastery shows the power of perfect synergy** between player and system. His dominance 
    in La Liga is absolute and likely unmatched, while his adaptations in Ligue 1 and MLS show he can succeed 
    anywhere when given the right role. His impact goes beyond numbers - he transforms entire leagues.
    
    **🏆 The Verdict:** Ronaldo wins this category through sheer breadth of league conquest and adaptability. 
    However, Messi's depth of dominance in La Liga and transformative impact wherever he goes shows that 
    there are different paths to league mastery.
    
    **🌍 Combined Impact:** Together, they've elevated every league they've touched, bringing global attention 
    to La Liga, inspiring a generation in the Premier League, revolutionizing expectations in Serie A and MLS, 
    and showcasing football's universal appeal across all continents.
    """)

if __name__ == "__main__":
    show()