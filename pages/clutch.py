import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the clutch performance analysis page"""
    st.markdown('<h1 class="section-header">🔥 CLUTCH PERFORMANCE ANALYSIS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    clutch_data = data['clutch']
    
    # Page introduction
    st.markdown("""
    **When the pressure is on, legends are made.** Clutch performance separates the great from the greatest. 
    In finals, decisive moments, penalty shootouts, and last-minute scenarios - how do Messi and Ronaldo respond? 
    Let's analyze their performance when it matters most, in the biggest games and most crucial moments of their careers.
    """)
    
    # Clutch metrics overview
    st.markdown('<h3 class="section-header">⚡ Clutch Metrics Overview</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Final Goals", "26", "4 more")
        st.caption("🇦🇷 Messi leads")
        st.write("**Messi:** 26 goals in finals")
        st.write("**Ronaldo:** 22 goals in finals")
    
    with col2:
        st.metric("Last Minute Goals", "31", "8 more")
        st.caption("🇵🇹 Ronaldo leads")
        st.write("**Ronaldo:** 31 decisive goals")
        st.write("**Messi:** 23 last-minute goals")
    
    with col3:
        st.metric("Penalty Shootouts", "7", "3 more")
        st.caption("🇵🇹 Ronaldo leads")
        st.write("**Ronaldo:** 7 successful shootouts")
        st.write("**Messi:** 4 successful shootouts")
    
    with col4:
        st.metric("Big Game Goals", "95", "6 more")
        st.caption("🇵🇹 Ronaldo leads")
        st.write("**Ronaldo:** 95 crucial goals")
        st.write("**Messi:** 89 big game goals")
    
    with col5:
        st.metric("Champions League Finals", "5", "1 more")
        st.caption("🇵🇹 Ronaldo leads")
        st.write("**Ronaldo:** 5 CL final wins")
        st.write("**Messi:** 4 CL final wins")
    
    # Clutch performance breakdown
    st.markdown('<h3 class="section-header">🏆 Clutch Performance Breakdown</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Clutch categories comparison
        clutch_categories = ['Final Goals', 'Penalty Shootout Goals', 'Last Minute Goals', 'Hat-tricks in Finals', 'Big Game Goals']
        messi_clutch = [26, 4, 23, 2, 89]
        ronaldo_clutch = [22, 7, 31, 3, 95]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=clutch_categories,
            y=messi_clutch,
            marker_color='#4ECDC4',
            text=messi_clutch,
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=clutch_categories,
            y=ronaldo_clutch,
            marker_color='#FF6B6B',
            text=ronaldo_clutch,
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🔥 Clutch Performance Categories",
            barmode='group',
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Clutch performance radar
        categories_radar = ['Finals Performance', 'Penalty Pressure', 'Last Minute Impact', 'Big Game Mentality', 'Decisive Moments', 'Mental Strength']
        messi_radar = [90, 75, 85, 88, 92, 85]
        ronaldo_radar = [85, 95, 95, 95, 90, 98]
        
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
            title="🔥 Clutch Performance Radar",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Finals performance analysis
    st.markdown('<h3 class="section-header">🏆 Finals Performance Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card">
            <h3>🇦🇷 MESSI'S FINALS RECORD</h3>
            <h4>🏆 Major Finals</h4>
            <p><strong>Finals Played:</strong> 10</p>
            <p><strong>Finals Won:</strong> 7</p>
            <p><strong>Win Rate:</strong> 70%</p>
            <p><strong>Goals in Finals:</strong> 26</p>
            <p><strong>Assists in Finals:</strong> 15</p>
            
            <h4>🌟 Iconic Finals</h4>
            <p>• 2022 World Cup Final vs France</p>
            <p>• 2021 Copa América Final vs Brazil</p>
            <p>• 2015 Champions League Final vs Juventus</p>
            <p>• 2011 Champions League Final vs Man United</p>
            
            <h4>💔 Heartbreaks</h4>
            <p>• 2014 World Cup Final vs Germany</p>
            <p>• 2016 Copa América Final vs Chile (Penalties)</p>
            <p>• 2015 Copa América Final vs Chile</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card">
            <h3>🇵🇹 RONALDO'S FINALS RECORD</h3>
            <h4>🏆 Major Finals</h4>
            <p><strong>Finals Played:</strong> 9</p>
            <p><strong>Finals Won:</strong> 7</p>
            <p><strong>Win Rate:</strong> 78%</p>
            <p><strong>Goals in Finals:</strong> 22</p>
            <p><strong>Assists in Finals:</strong> 8</p>
            
            <h4>🌟 Iconic Finals</h4>
            <p>• 2016 Euro Final vs France (Injured early)</p>
            <p>• 2014 Champions League Final vs Atlético</p>
            <p>• 2017 Champions League Final vs Juventus</p>
            <p>• 2018 Champions League Final vs Liverpool</p>
            
            <h4>💔 Heartbreaks</h4>
            <p>• 2004 Euro Final vs Greece</p>
            <p>• 2012 Euro Final vs Spain</p>
            <p>• No World Cup Final appearance</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Big moments breakdown
    st.markdown('<h3 class="section-header">⚡ Defining Clutch Moments</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🎯 Penalty Pressure</h4>
            <p><strong>🇵🇹 Ronaldo: Superior</strong></p>
            <p>• Penalty conversion: 84.3%</p>
            <p>• Shootout success: 7 wins</p>
            <p>• Never missed crucial penalty</p>
            <p>• Ice-cold under pressure</p>
            <hr>
            <p><strong>🇦🇷 Messi: Good but vulnerable</strong></p>
            <p>• Penalty conversion: 77.8%</p>
            <p>• Shootout success: 4 wins</p>
            <p>• Notable misses in big moments</p>
            <p>• 2022 WC redemption story</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>⏰ Last Minute Magic</h4>
            <p><strong>🇵🇹 Ronaldo: Mr. Clutch</strong></p>
            <p>• 31 last-minute goals</p>
            <p>• Famous for late winners</p>
            <p>• Thrives under pressure</p>
            <p>• "Siuuuu" celebration master</p>
            <hr>
            <p><strong>🇦🇷 Messi: Quiet brilliance</strong></p>
            <p>• 23 last-minute goals</p>
            <p>• More subtle clutch moments</p>
            <p>• Creates winning assists</p>
            <p>• 91st minute vs Iran (2014 WC)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏆 Champions League Clutch</h4>
            <p><strong>🇵🇹 Ronaldo: Mr. Champions League</strong></p>
            <p>• 140 CL goals (Record)</p>
            <p>• 17 knockout goals in 2016-17</p>
            <p>• 5 CL titles</p>
            <p>• Ultimate big game player</p>
            <hr>
            <p><strong>🇦🇷 Messi: Barcelona legend</strong></p>
            <p>• 129 CL goals</p>
            <p>• 4 CL titles</p>
            <p>• Dominated with Barcelona</p>
            <p>• PSG disappointment</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Clutch moments timeline
    st.markdown('<h3 class="section-header">📅 Career Clutch Moments Timeline</h3>', unsafe_allow_html=True)
    
    # Create clutch moments data
    clutch_moments = {
        'Year': [2006, 2008, 2009, 2011, 2014, 2015, 2016, 2017, 2018, 2019, 2021, 2022, 2023],
        'Messi_Moment': ['CL Debut Goal', 'Olympics Gold', 'First CL Win', 'CL Final Goal', 'WC Final Loss', 'CL Final Win', 'Copa Final Loss', 'CL Comeback PSG', 'WC Round of 16', 'Copa Semifinal', 'Copa Final Win', 'WC Final Win', 'Leagues Cup'],
        'Ronaldo_Moment': ['World Cup Debut', 'Euro 2008', 'Real Madrid Move', 'CL Semifinal', 'La Décima Win', 'CL Semifinal', 'Euro Final Win', 'CL Final Win', 'Bicycle Kick', 'Nations League', 'Euro Top Scorer', 'World Cup Record', 'Al Nassr Impact'],
        'Messi_Impact': [6, 7, 9, 8, 5, 9, 4, 7, 6, 8, 10, 10, 7],
        'Ronaldo_Impact': [6, 7, 8, 9, 10, 9, 8, 9, 10, 8, 8, 7, 7]
    }
    
    clutch_df = pd.DataFrame(clutch_moments)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=clutch_df['Year'],
        y=clutch_df['Messi_Impact'],
        mode='lines+markers',
        name='Messi Clutch Impact',
        line=dict(color='#4ECDC4', width=4),
        marker=dict(size=10),
        text=clutch_df['Messi_Moment'],
        hovertemplate='<b>Messi %{x}</b><br>Impact: %{y}/10<br>Moment: %{text}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=clutch_df['Year'],
        y=clutch_df['Ronaldo_Impact'],
        mode='lines+markers',
        name='Ronaldo Clutch Impact',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=10),
        text=clutch_df['Ronaldo_Moment'],
        hovertemplate='<b>Ronaldo %{x}</b><br>Impact: %{y}/10<br>Moment: %{text}<extra></extra>'
    ))
    
    # Add major annotations
    fig.add_annotation(x=2022, y=10, text="Messi's World Cup<br>Ultimate Clutch", arrowcolor="#4ECDC4", arrowwidth=2)
    fig.add_annotation(x=2018, y=10, text="Ronaldo's Bicycle Kick<br>vs Juventus", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x=2014, y=10, text="La Décima<br>Ronaldo delivers", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x=2021, y=10, text="Messi's Copa<br>Breakthrough", arrowcolor="#4ECDC4", arrowwidth=2)
    
    fig.update_layout(
        title="🔥 Career Clutch Moments Impact Timeline",
        xaxis_title="Year",
        yaxis_title="Clutch Impact Score (1-10)",
        height=500,
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Pressure situations analysis
    st.markdown('<h3 class="section-header">😰 Pressure Situations Analysis</h3>', unsafe_allow_html=True)
    
    pressure_data = {
        'Situation': ['Penalty Kicks', 'Free Kicks in Finals', 'Injury Time Goals', 'Comeback Contributions', 'Title Deciders', 'Derby Goals'],
        'Messi': [77.8, 12, 23, 45, 18, 26],
        'Ronaldo': [84.3, 8, 31, 52, 22, 18],
        'Description': ['Success rate %', 'Goals scored', 'Goals + assists', 'Goals + assists', 'Decisive goals', 'Clasico + Derby goals'],
        'Winner': ['🇵🇹 Ronaldo', '🇦🇷 Messi', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇦🇷 Messi']
    }
    
    pressure_df = pd.DataFrame(pressure_data)
    st.dataframe(pressure_df, use_container_width=True, height=300)
    
    # Mental strength comparison
    st.markdown('<h3 class="section-header">🧠 Mental Strength & Resilience</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Mental Journey:
        
        **🌱 Early Struggles:**
        - Multiple final defeats (2007, 2014, 2015, 2016)
        - Argentina retirement consideration (2016)
        - Pressure of expectations
        - "Choker" narrative unfairly applied
        
        **🔄 Resilience & Growth:**
        - Returned from international retirement
        - Learned from penalty shootout failures
        - Developed mental toughness with age
        - 2021-2022 redemption arc
        
        **👑 Ultimate Vindication:**
        - 2021 Copa América breakthrough
        - 2022 World Cup triumph
        - Penalty shootout success vs Netherlands
        - Final vs France performance
        
        **🎯 Mental Strengths:**
        - Incredible consistency under pressure
        - Ability to create magic in big moments
        - Team-first mentality in crucial games
        - Grew stronger from early failures
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Mental Fortress:
        
        **🧱 Unbreakable Confidence:**
        - Never doubts his ability
        - Thrives under pressure from day one
        - "I am the best" mentality
        - Converts pressure into motivation
        
        **🎯 Clutch Gene:**
        - Born for big moments
        - Higher performance in crucial games
        - Penalty specialist under pressure
        - Last-minute goal machine
        
        **🏆 Championship Mentality:**
        - 5 Champions League titles
        - Delivers when team needs him most
        - Never intimidated by occasion
        - Elevates game in finals
        
        **💪 Mental Advantages:**
        - Superior penalty conversion under pressure
        - More last-minute decisive goals
        - Better in knockout competitions
        - Thrives on being the main man
        """)
    
    # Clutch statistics breakdown
    st.markdown('<h3 class="section-header">📊 Advanced Clutch Statistics</h3>', unsafe_allow_html=True)
    
    advanced_clutch = {
        'Metric': [
            'Goals in Finals', 'Assists in Finals', 'Finals Win Rate (%)', 'Penalty Shootout Record',
            'Last Minute Winners', 'Comeback Goals', 'Goals vs Top 6 Teams', 'Champions League KO Goals',
            'Goals when Team Behind', 'Goals in Title Deciders', 'El Clasico/Derby Goals', 'Goals under Pressure Rating'
        ],
        'Messi': [26, 15, 70, '4W-3L', 23, 34, 67, 49, 45, 18, 26, 88],
        'Ronaldo': [22, 8, 78, '7W-2L', 31, 41, 72, 67, 52, 22, 18, 94],
        'Winner': [
            '🇦🇷 Messi', '🇦🇷 Messi', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo',
            '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo',
            '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇦🇷 Messi', '🇵🇹 Ronaldo'
        ]
    }
    
    advanced_df = pd.DataFrame(advanced_clutch)
    st.dataframe(advanced_df, use_container_width=True, height=450)
    
    # Final clutch verdict
    st.markdown('<h3 class="section-header">🏁 Clutch Performance Verdict</h3>', unsafe_allow_html=True)
    
    # Calculate clutch scores
    ronaldo_clutch_score = 9  # Wins 8 out of 12 categories
    messi_clutch_score = 4   # Wins 4 out of 12 categories
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>🔥 Clutch Performance Champion</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO: Mr. Clutch</h3>
                <p>✅ Better penalty conversion (84.3% vs 77.8%)</p>
                <p>✅ More penalty shootout wins (7 vs 4)</p>
                <p>✅ More last-minute goals (31 vs 23)</p>
                <p>✅ Higher finals win rate (78% vs 70%)</p>
                <p>✅ More Champions League knockout goals</p>
                <p>✅ Superior pressure situation rating (94 vs 88)</p>
                <p>✅ More goals when team needs them most</p>
            </div>
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI: Finals Specialist</h3>
                <p>✅ More goals in finals (26 vs 22)</p>
                <p>✅ More assists in finals (15 vs 8)</p>
                <p>✅ Better in El Clasico (26 vs 18 goals)</p>
                <p>✅ World Cup final heroics (2022)</p>
                <p>✅ Ultimate redemption story</p>
                <p>✅ Clutch playmaker in big games</p>
                <p>✅ Creates moments of pure magic</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Clutch Winner:</strong> 🇵🇹 <strong>RONALDO</strong> - The ultimate pressure performer!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final analysis
    st.markdown("""
    ---
    ### 🌟 Clutch Performance Legacy
    
    **🇵🇹 Ronaldo embodies clutch performance** like no athlete in any sport. His ability to raise his game when 
    the stakes are highest is legendary. From penalty spots to last-minute winners, from Champions League knockouts 
    to international tournaments - he consistently delivers when his team needs him most. His mental strength and 
    self-belief are unmatched.
    
    **🇦🇷 Messi's clutch story is one of growth and ultimate redemption.** While he faced criticism for early final 
    defeats, his journey to clutch greatness culminated in the 2022 World Cup - the ultimate pressure performance. 
    His ability to create magic in crucial moments and his final-specific goal record show different but equally 
    valuable clutch qualities.
    
    **🏆 The Verdict:** Ronaldo wins the clutch category through superior penalty performance, more last-minute 
    winners, and better knockout competition records. However, Messi's 2022 World Cup performance and overall 
    finals goal record show that both players have delivered in the biggest moments.
    
    **🔥 Combined Legacy:** Together, they've produced some of the most clutch performances in football history, 
    proving that true greatness is measured not just by talent, but by the ability to deliver when everything 
    is on the line. Both have ice in their veins, just expressed differently.
    
    **🎯 Final Truth:** In clutch moments, you want either player on your team. Ronaldo for penalties and last-minute 
    drama, Messi for magical moments and finals excellence. Both are clutch legends in their own right.
    """)

if __name__ == "__main__":
    show()