import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the international career analysis page"""
    st.markdown('<h1 class="section-header">🌍 INTERNATIONAL CAREER ANALYSIS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    international_data = data['international']
    
    # Page introduction
    st.markdown("""
    **International football is where legends are truly made.** World Cups, continental championships, 
    and representing your nation on the biggest stage - this is where the GOAT debate often gets decided.
    
    Let's dive deep into how Messi and Ronaldo performed for Argentina and Portugal respectively.
    """)
    
    # Overview metrics
    st.markdown('<h3 class="section-header">🏆 International Career Overview</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.metric("Matches Played", 
                 f"Messi: {international_data.iloc[0]['matches']}", 
                 f"vs Ronaldo: {international_data.iloc[1]['matches']}")
        st.caption("🇵🇹 Ronaldo leads by 23")
    
    with col2:
        st.metric("International Goals", 
                 f"Messi: {international_data.iloc[0]['goals']}", 
                 f"vs Ronaldo: {international_data.iloc[1]['goals']}")
        st.caption("🇵🇹 Ronaldo leads by 22")
    
    with col3:
        st.metric("International Assists", 
                 f"Messi: {international_data.iloc[0]['assists']}", 
                 f"vs Ronaldo: {international_data.iloc[1]['assists']}")
        st.caption("🇦🇷 Messi leads by 13")
    
    with col4:
        st.metric("Goals per Game", 
                 f"Messi: {international_data.iloc[0]['goals']/international_data.iloc[0]['matches']:.2f}", 
                 f"vs Ronaldo: {international_data.iloc[1]['goals']/international_data.iloc[1]['matches']:.2f}")
        st.caption("🇵🇹 Ronaldo leads")
    
    with col5:
        st.metric("Major Trophies", 
                 f"Messi: {international_data.iloc[0]['trophies']}", 
                 f"vs Ronaldo: {international_data.iloc[1]['trophies']}")
        st.caption("🤝 Tied at 2 each")
    
    with col6:
        st.metric("Minutes per Goal", 
                 f"Messi: {international_data.iloc[0]['minutesPerGoal']}", 
                 f"vs Ronaldo: {international_data.iloc[1]['minutesPerGoal']}")
        st.caption("🇵🇹 Ronaldo slightly better")
    
    # International achievements breakdown
    st.markdown('<h3 class="section-header">🏅 Major Tournament Achievements</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card">
            <h3>🇦🇷 MESSI'S INTERNATIONAL HONORS</h3>
            <h4>🏆 Major Trophies (2)</h4>
            <p><strong>🥇 FIFA World Cup 2022</strong> - Captain & Best Player</p>
            <p><strong>🏆 Copa América 2021</strong> - Captain & Top Scorer</p>
            
            <h4>🥈 Runner-up Finishes</h4>
            <p>• Copa América 2007, 2015, 2016</p>
            <p>• FIFA World Cup 2014</p>
            
            <h4>🎖️ Individual Awards</h4>
            <p>• World Cup Golden Ball 2014, 2022</p>
            <p>• Copa América Best Player 2021</p>
            <p>• Olympic Gold Medal 2008</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card">
            <h3>🇵🇹 RONALDO'S INTERNATIONAL HONORS</h3>
            <h4>🏆 Major Trophies (2)</h4>
            <p><strong>🥇 UEFA Euro 2016</strong> - Captain & Leader</p>
            <p><strong>🏆 UEFA Nations League 2019</strong> - Top Scorer</p>
            
            <h4>🥈 Runner-up Finishes</h4>
            <p>• UEFA Euro 2004 (Host nation)</p>
            <p>• UEFA Euro 2012</p>
            
            <h4>🎖️ Individual Awards</h4>
            <p>• Euro 2016 Team of Tournament</p>
            <p>• Nations League Top Scorer 2019</p>
            <p>• All-time Int'l Top Scorer</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistical comparison charts
    st.markdown('<h3 class="section-header">📊 International Statistics Comparison</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals and assists comparison
        categories = ['Goals', 'Assists', 'Goals+Assists', 'Matches']
        messi_values = [108, 56, 164, 183]
        ronaldo_values = [130, 43, 173, 206]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_values,
            marker_color='#4ECDC4',
            text=messi_values,
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_values,
            marker_color='#FF6B6B',
            text=ronaldo_values,
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🎯 International Goals & Contributions",
            barmode='group',
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Efficiency radar chart
        categories_radar = ['Goals per Game', 'Assists per Game', 'Minutes per Goal', 'Tournament Impact', 'Leadership', 'Clutch Factor']
        # Normalized to 100 scale
        messi_radar = [85, 90, 88, 95, 85, 92]
        ronaldo_radar = [90, 70, 90, 85, 95, 88]
        
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
            title="⚡ International Performance Radar",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Tournament performance breakdown
    st.markdown('<h3 class="section-header">🏆 Major Tournament Performance</h3>', unsafe_allow_html=True)
    
    # Create tournament performance data
    tournament_data = {
        'Tournament': ['World Cup', 'Copa América', 'Euro Championships', 'Nations League', 'Confederations Cup'],
        'Messi Appearances': [5, 7, 0, 0, 0],
        'Messi Goals': [13, 13, 0, 0, 0],
        'Messi Trophies': [1, 1, 0, 0, 0],
        'Ronaldo Appearances': [5, 0, 6, 2, 2],
        'Ronaldo Goals': [8, 0, 14, 3, 2],
        'Ronaldo Trophies': [0, 0, 1, 1, 0]
    }
    
    tournament_df = pd.DataFrame(tournament_data)
    
    # Tournament goals comparison
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('🌍 World Cup Goals', '🏆 Continental Tournament Goals', '🎯 Tournament Appearances', '🏅 Tournament Success Rate'),
        specs=[[{"type": "bar"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "pie"}]]
    )
    
    # World Cup goals
    fig.add_trace(
        go.Bar(x=['Messi', 'Ronaldo'], y=[13, 8], name='WC Goals', marker_color=['#4ECDC4', '#FF6B6B']),
        row=1, col=1
    )
    
    # Continental tournament goals
    fig.add_trace(
        go.Bar(x=['Copa América (Messi)', 'Euro (Ronaldo)'], y=[13, 14], name='Continental Goals', marker_color=['#4ECDC4', '#FF6B6B']),
        row=1, col=2
    )
    
    # Tournament appearances
    fig.add_trace(
        go.Bar(x=['Messi', 'Ronaldo'], y=[12, 15], name='Appearances', marker_color=['#4ECDC4', '#FF6B6B']),
        row=2, col=1
    )
    
    # Success rate pie chart
    fig.add_trace(
        go.Pie(labels=['Messi Trophies', 'Messi Finals Lost'], values=[2, 4], name="Messi Success"),
        row=2, col=2
    )
    
    fig.update_layout(height=600, showlegend=False, title_text="🏆 Tournament Performance Analysis")
    st.plotly_chart(fig, use_container_width=True)
    
    # World Cup analysis
    st.markdown('<h3 class="section-header">🌍 World Cup Legacy Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's World Cup Journey
        
        **🏆 2022 Qatar - WORLD CHAMPION**
        - 7 goals, 3 assists in 7 games
        - Golden Ball winner (best player)
        - Led Argentina to first WC since 1986
        - Iconic final vs France (4-2 on penalties)
        
        **🥈 2014 Brazil - Runner-up**
        - 4 goals, 1 assist in 7 games
        - Golden Ball winner (best player)
        - Lost final to Germany (0-1)
        - Heartbreaking near-miss
        
        **📊 World Cup Stats:**
        - 5 World Cups (2006-2022)
        - 26 matches, 13 goals, 8 assists
        - 2 Golden Ball awards
        - 1 World Cup trophy (career completed)
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's World Cup Journey
        
        **🥉 2022 Qatar - Round of 16**
        - 1 goal, 2 assists in 4 games
        - Became first player to score in 5 WCs
        - Portugal eliminated by Morocco
        - Emotional farewell to World Cup dreams
        
        **🥉 2018 Russia - Round of 16**
        - 4 goals, 0 assists in 4 games
        - Hat-trick vs Spain (3-3 thriller)
        - Lost to Uruguay in Round of 16
        - Peak individual performance
        
        **📊 World Cup Stats:**
        - 5 World Cups (2006-2022)
        - 22 matches, 8 goals, 2 assists
        - Historic 5 World Cup goalscorer
        - 0 World Cup trophies (biggest regret)
        """)
    
    # International evolution timeline
    st.markdown('<h3 class="section-header">📈 International Career Evolution</h3>', unsafe_allow_html=True)
    
    # Create international timeline data
    years = list(range(2005, 2024))
    messi_int_goals = [0, 2, 6, 4, 5, 7, 12, 5, 8, 11, 5, 6, 4, 7, 9, 4, 1, 7, 8]
    ronaldo_int_goals = [2, 7, 8, 6, 5, 7, 8, 11, 5, 9, 7, 4, 3, 8, 2, 5, 14, 8, 1]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years,
        y=messi_int_goals,
        mode='lines+markers',
        name='Messi International Goals',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Messi</b><br>Year: %{x}<br>Int Goals: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=years,
        y=ronaldo_int_goals,
        mode='lines+markers',
        name='Ronaldo International Goals',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Ronaldo</b><br>Year: %{x}<br>Int Goals: %{y}<extra></extra>'
    ))
    
    # Add major tournament annotations
    fig.add_annotation(x=2022, y=8, text="🏆 Messi's WC Victory", arrowcolor="#4ECDC4", arrowwidth=2)
    fig.add_annotation(x=2016, y=14, text="🏆 Ronaldo's Euro Victory", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x=2021, y=4, text="🏆 Messi's Copa Victory", arrowcolor="#4ECDC4", arrowwidth=2)
    
    fig.update_layout(
        title="🌍 International Goals by Year Timeline",
        xaxis_title="Year",
        yaxis_title="International Goals",
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Head-to-head international comparison
    st.markdown('<h3 class="section-header">⚔️ Direct International Comparison</h3>', unsafe_allow_html=True)
    
    comparison_data = {
        'Metric': [
            'International Debut Age', 'Years in National Team', 'Total Caps', 'Total Goals', 
            'Total Assists', 'Goals per Game', 'Minutes per Goal', 'Hat-tricks',
            'Major Tournament Goals', 'Final Appearances', 'Trophies Won', 'Individual Awards'
        ],
        'Messi': [
            18, 19, 183, 108, 56, 0.59, 132, 3,
            26, 6, 2, 3
        ],
        'Ronaldo': [
            18, 20, 206, 130, 43, 0.63, 130, 10,
            22, 4, 2, 2
        ],
        'Winner': [
            '🤝 Tie', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo',
            '🇦🇷 Messi', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo',
            '🇦🇷 Messi', '🇦🇷 Messi', '🤝 Tie', '🇦🇷 Messi'
        ]
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df, use_container_width=True, height=450)
    
    # International legacy analysis
    st.markdown('<h3 class="section-header">🎭 International Legacy Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's International Legacy:
        
        **🏆 The Completion of Greatness:**
        - Finally won the World Cup in 2022 at age 35
        - Captained Argentina to Copa América 2021
        - Two Golden Ball awards at World Cups
        - Overcame multiple final heartbreaks
        
        **📊 Key Strengths:**
        - Superior playmaking (56 assists vs 43)
        - More goals in major tournaments (26 vs 22)
        - Higher assist rate per game
        - Multiple final appearances (6 vs 4)
        
        **🎯 Defining Moments:**
        - 2022 World Cup final vs France
        - 2021 Copa América breakthrough
        - 2014 World Cup Golden Ball
        - 2008 Olympic Gold Medal
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's International Legacy:
        
        **👑 The Record Breaker:**
        - All-time leading international goalscorer (130 goals)
        - First player to score in 5 World Cups
        - Led Portugal to Euro 2016 and Nations League 2019
        - 20-year international career
        
        **📊 Key Strengths:**
        - Most international goals in history
        - Higher goals per game ratio (0.63 vs 0.59)
        - More international hat-tricks (10 vs 3)
        - Greater longevity and consistency
        
        **🎯 Defining Moments:**
        - Euro 2016 final victory vs France
        - Hat-trick vs Spain at 2018 World Cup
        - Nations League 2019 triumph
        - Breaking all international records
        """)
    
    # Final international verdict
    st.markdown('<h3 class="section-header">🏁 International Career Verdict</h3>', unsafe_allow_html=True)
    
    # Calculate international scores
    messi_int_score = 0
    ronaldo_int_score = 0
    
    # Goals (Ronaldo wins)
    ronaldo_int_score += 1
    # Assists (Messi wins)  
    messi_int_score += 1
    # World Cup (Messi wins)
    messi_int_score += 2
    # Continental (Tie)
    messi_int_score += 1
    ronaldo_int_score += 1
    # Individual awards (Messi wins)
    messi_int_score += 1
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>🌍 International Career Verdict</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI: {messi_int_score} points</h3>
                <p>✅ World Cup Winner</p>
                <p>✅ More assists & playmaking</p>
                <p>✅ More tournament goals</p>
                <p>✅ More individual awards</p>
            </div>
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO: {ronaldo_int_score} points</h3>
                <p>✅ Most international goals</p>
                <p>✅ Higher goals per game</p>
                <p>✅ More hat-tricks</p>
                <p>✅ Greater longevity</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>International Winner:</strong> 🇦🇷 <strong>MESSI</strong> - The World Cup triumph tips the balance!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final thoughts
    st.markdown("""
    ---
    ### 🌟 International Career Summary
    
    **🇦🇷 Messi's international journey** is a story of perseverance and ultimate triumph. After multiple heartbreaking 
    final defeats, he finally captured the World Cup in 2022, completing his legacy. His playmaking ability and 
    leadership in major tournaments sets him apart.
    
    **🇵🇹 Ronaldo's international career** is defined by record-breaking consistency and longevity. As the all-time 
    leading international goalscorer, he's been Portugal's talisman for two decades, delivering crucial goals 
    and leading them to their first major trophies.
    
    **🏆 The Verdict:** While Ronaldo has more goals and greater longevity, Messi's World Cup victory and superior 
    tournament performances in major competitions give him the edge in international legacy.
    """)

if __name__ == "__main__":
    show()