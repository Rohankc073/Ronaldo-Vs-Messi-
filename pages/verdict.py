import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the final verdict page"""
    st.markdown('<h1 class="section-header">🏁 THE FINAL VERDICT</h1>', unsafe_allow_html=True)
    
    # GOAT Score calculation with comprehensive categories
    st.markdown('<h3 class="section-header">🐐 Comprehensive GOAT Analysis</h3>', unsafe_allow_html=True)
    
    # Enhanced scoring system with more categories
    categories = [
        'Goal Scoring Ability', 'Playmaking & Assists', 'Club Trophies', 'Individual Awards', 
        'International Success', 'Longevity & Consistency', 'Technical Skills', 
        'Physical Attributes', 'Big Game Performance', 'Global Impact & Legacy',
        'Versatility', 'Peak Performance', 'Clutch Factor', 'Team Leadership'
    ]
    
    # Detailed scoring (out of 10) - carefully balanced based on career achievements
    messi_scores = [8.9, 9.9, 9.4, 10.0, 9.6, 8.8, 9.8, 7.4, 9.3, 9.5, 9.2, 9.8, 9.0, 9.1]
    ronaldo_scores = [9.8, 7.3, 8.8, 8.7, 8.8, 9.8, 8.7, 9.6, 9.7, 9.7, 9.6, 9.2, 9.5, 9.3]
    
    # Calculate weighted scores (some categories matter more)
    weights = [1.3, 1.2, 1.1, 1.2, 1.4, 1.0, 1.1, 0.8, 1.3, 1.0, 0.9, 1.1, 1.2, 1.0]
    
    messi_weighted = sum(m * w for m, w in zip(messi_scores, weights))
    ronaldo_weighted = sum(r * w for r, w in zip(ronaldo_scores, weights))
    
    # Main comparison visualization
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Comprehensive radar chart
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_scores,
            theta=categories,
            fill='toself',
            name='Messi',
            fillcolor='rgba(78, 205, 196, 0.4)',
            line=dict(color='#4ECDC4', width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_scores,
            theta=categories,
            fill='toself',
            name='Ronaldo',
            fillcolor='rgba(255, 107, 107, 0.4)',
            line=dict(color='#FF6B6B', width=3)
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10],
                    tickmode='linear',
                    tick0=0,
                    dtick=2
                )),
            title="🏆 Ultimate GOAT Score Comparison (1-10 Scale)",
            height=700,
            showlegend=True,
            font_size=12
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Score summary
        st.markdown("### 📊 Final Scores")
        
        messi_total = sum(messi_scores)
        ronaldo_total = sum(ronaldo_scores)
        
        st.metric("Messi Total", f"{messi_total:.1f}/140", f"{messi_total - ronaldo_total:+.1f}")
        st.metric("Ronaldo Total", f"{ronaldo_total:.1f}/140", "")
        st.metric("Weighted Score", f"Messi: {messi_weighted:.1f}", f"vs Ronaldo: {ronaldo_weighted:.1f}")
        
        # Category wins
        messi_wins = sum(1 for m, r in zip(messi_scores, ronaldo_scores) if m > r)
        ronaldo_wins = sum(1 for m, r in zip(messi_scores, ronaldo_scores) if r > m)
        ties = sum(1 for m, r in zip(messi_scores, ronaldo_scores) if abs(m - r) < 0.1)
        
        st.markdown("### 🏆 Category Breakdown")
        st.metric("Messi Wins", f"{messi_wins}/14", "")
        st.metric("Ronaldo Wins", f"{ronaldo_wins}/14", "")
        st.metric("Close Contests", f"{ties}/14", "")
        
        # Performance indicators
        st.markdown("### ⚡ Performance")
        if messi_total > ronaldo_total:
            st.success("🇦🇷 Messi Leading")
        else:
            st.error("🇵🇹 Ronaldo Leading")
        
        margin = abs(messi_total - ronaldo_total)
        if margin < 2:
            st.info("🤝 Extremely Close!")
        elif margin < 5:
            st.warning("⚖️ Close Contest")
        else:
            st.info("📊 Clear Leader")
    
    # Determine the winner
    if messi_total > ronaldo_total:
        winner = "LIONEL MESSI"
        winner_emoji = "🇦🇷"
        winner_desc = "The Magician from Argentina claims the crown!"
        winner_color = "#4ECDC4"
        margin = messi_total - ronaldo_total
    else:
        winner = "CRISTIANO RONALDO"
        winner_emoji = "🇵🇹"
        winner_desc = "The Portuguese phenomenon takes the throne!"
        winner_color = "#FF6B6B"
        margin = ronaldo_total - messi_total
    
    # Final verdict announcement
    st.markdown('<h3 class="section-header">👑 THE ULTIMATE VERDICT</h3>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h1 style="font-size: 3rem; margin-bottom: 1rem;">{winner_emoji} THE GOAT IS...</h1>
        <h2 style="font-size: 4rem; font-weight: bold; margin: 1rem 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{winner}</h2>
        <h3 style="font-size: 1.8rem; opacity: 0.9; margin-bottom: 2rem;">{winner_desc}</h3>
        
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h4 style="font-size: 2.5rem; margin: 0; color: #4ECDC4;">{messi_total:.1f}</h4>
                <p style="margin: 0; font-size: 1.2rem;">🇦🇷 Messi Score</p>
            </div>
            <div style="font-size: 3rem; opacity: 0.7; align-self: center;">VS</div>
            <div style="text-align: center;">
                <h4 style="font-size: 2.5rem; margin: 0; color: #FF6B6B;">{ronaldo_total:.1f}</h4>
                <p style="margin: 0; font-size: 1.2rem;">🇵🇹 Ronaldo Score</p>
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 10px; margin: 2rem 0;">
            <p style="font-size: 1.3rem; margin: 0;"><strong>Victory Margin:</strong> {margin:.1f} points</p>
            <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Weighted Score: {messi_weighted:.1f} vs {ronaldo_weighted:.1f}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Detailed category breakdown
    st.markdown('<h3 class="section-header">📋 Detailed Category Analysis</h3>', unsafe_allow_html=True)
    
    category_analysis = pd.DataFrame({
        'Category': categories,
        'Messi Score': messi_scores,
        'Ronaldo Score': ronaldo_scores,
        'Winner': ['🇦🇷 Messi' if m > r else '🇵🇹 Ronaldo' if r > m else '🤝 Tie' 
                  for m, r in zip(messi_scores, ronaldo_scores)],
        'Margin': [abs(m - r) for m, r in zip(messi_scores, ronaldo_scores)],
        'Weight': weights,
        'Weighted Messi': [m * w for m, w in zip(messi_scores, weights)],
        'Weighted Ronaldo': [r * w for r, w in zip(ronaldo_scores, weights)]
    })
    
    # Format the dataframe for better display
    category_analysis['Messi Score'] = category_analysis['Messi Score'].round(1)
    category_analysis['Ronaldo Score'] = category_analysis['Ronaldo Score'].round(1)
    category_analysis['Margin'] = category_analysis['Margin'].round(1)
    category_analysis['Weighted Messi'] = category_analysis['Weighted Messi'].round(1)
    category_analysis['Weighted Ronaldo'] = category_analysis['Weighted Ronaldo'].round(1)
    
    st.dataframe(category_analysis, use_container_width=True, height=500)
    
    # Key strengths analysis
    st.markdown('<h3 class="section-header">💪 Strength Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Dominant Categories:
        
        **🎨 Playmaking & Assists (9.9/10)**
        - Unmatched vision and creativity
        - 377 career assists vs Ronaldo's 236
        - Natural playmaker instincts
        
        **🏆 Individual Awards (10.0/10)**
        - Record 8 Ballon d'Or awards
        - Most individual accolades in history
        - Consistent recognition of excellence
        
        **🛠️ Technical Skills (9.8/10)**
        - Close ball control mastery
        - Dribbling perfection
        - Left foot magic
        
        **🌟 Peak Performance (9.8/10)**
        - 91 goals in calendar year 2012
        - Multiple 50+ goal seasons
        - Sustained excellence at peak
        
        **🌍 International Success (9.6/10)**
        - World Cup 2022 champion
        - Copa América winner
        - Completed his legacy
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Dominant Categories:
        
        **⚽ Goal Scoring Ability (9.8/10)**
        - All-time leading scorer (895+ goals)
        - Clinical finishing ability
        - Goal machine mentality
        
        **⏰ Longevity & Consistency (9.8/10)**
        - Elite performance at age 40
        - 20+ year career at top level
        - Incredible physical maintenance
        
        **🔥 Big Game Performance (9.7/10)**
        - Champions League king
        - Clutch moments specialist
        - Rises to biggest occasions
        
        **🌎 Global Impact & Legacy (9.7/10)**
        - Massive social media following
        - Global brand recognition
        - Inspiring millions worldwide
        
        **💪 Physical Attributes (9.6/10)**
        - Athletic perfection
        - Aerial dominance
        - Speed and strength combo
        
        **🎯 Versatility (9.6/10)**
        - Success in 4 major leagues
        - Adapted game with age
        - Multiple playing positions
        """)
    
    # The beautiful debate
    st.markdown('<h3 class="section-header">🎭 The Beautiful Truth</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
        <h3 style="text-align: center; color: #2c3e50;">🤝 Beyond the Numbers</h3>
        
        <div style="display: flex; justify-content: space-between; margin: 2rem 0;">
            <div style="flex: 1; padding: 0 1rem;">
                <h4 style="color: #4ECDC4;">🇦🇷 The Messi Magic:</h4>
                <ul>
                    <li><strong>Artist of Football:</strong> Makes the impossible look effortless</li>
                    <li><strong>Team Elevator:</strong> Makes everyone around him better</li>
                    <li><strong>Clutch Creator:</strong> Delivers when team needs him most</li>
                    <li><strong>Humble Genius:</strong> Lets football do the talking</li>
                    <li><strong>Complete Player:</strong> Goals, assists, dribbles, passes</li>
                </ul>
            </div>
            
            <div style="flex: 1; padding: 0 1rem;">
                <h4 style="color: #FF6B6B;">🇵🇹 The Ronaldo Machine:</h4>
                <ul>
                    <li><strong>Goal Scoring Machine:</strong> Built to score from anywhere</li>
                    <li><strong>Mental Fortress:</strong> Unbreakable confidence and will</li>
                    <li><strong>Physical Specimen:</strong> Athletic perfection maintained</li>
                    <li><strong>Clutch Performer:</strong> Delivers in biggest moments</li>
                    <li><strong>Longevity King:</strong> Elite level across 2 decades</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Final philosophical thoughts
    st.markdown('<h3 class="section-header">🌟 The Ultimate Truth</h3>', unsafe_allow_html=True)
    
    st.markdown(f"""
    ### 🐐 The GOAT Verdict: **{winner}**
    
    **But here's the real truth...**
    
    Both Messi and Ronaldo represent the absolute pinnacle of human achievement in football. 
    They've pushed each other to heights that seemed impossible, creating a rivalry that has 
    elevated the beautiful game itself.
    
    **🇦🇷 Messi** wins this analysis by **{margin:.1f} points**, primarily due to his:
    - Unmatched playmaking abilities
    - Record-breaking individual awards  
    - World Cup triumph completing his legacy
    - Technical perfection and artistry
    
    **🇵🇹 Ronaldo** remains incredibly close, excelling in:
    - Pure goal-scoring supremacy
    - Incredible longevity and consistency
    - Big game clutch performances
    - Physical dominance and versatility
    
    ---
    
    ### 🎭 The Beautiful Reality
    
    **The real winners?** Every football fan who witnessed this golden era. 
    We may never see anything like this again. Two players, from different planets, 
    who redefined what's possible in football.
    
    **Whether you believe in Messi's magic or Ronaldo's machine-like precision, 
    one thing is certain: We are blessed to have witnessed the two greatest players 
    in football history competing at the same time.**
    
    **🐐 + 🐐 = The Greatest Era in Football History** ⚽
    
    ---
    
    *"In the end, football wins. In the end, we all win."* 🌟
    """)
    
    # Interactive poll (for fun)
    st.markdown('<h3 class="section-header">🗳️ Your Vote</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🇦🇷 Vote for Messi", key="vote_messi"):
            st.success("🐐 You voted for Messi!")
            st.balloons()
    
    with col2:
        if st.button("🇵🇹 Vote for Ronaldo", key="vote_ronaldo"):
            st.success("🐐 You voted for Ronaldo!")
            st.balloons()
    
    with col3:
        if st.button("🤝 Both are GOATs", key="vote_both"):
            st.success("🐐🐐 Wise choice!")
            st.balloons()

if __name__ == "__main__":
    show()