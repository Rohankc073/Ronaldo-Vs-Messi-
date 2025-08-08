import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the individual awards analysis page"""
    st.markdown('<h1 class="section-header">🥇 INDIVIDUAL AWARDS & HONORS</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    achievements_data = data['achievements']
    
    # Page introduction
    st.markdown("""
    **Individual awards tell the story of personal excellence.** From Ballon d'Or to Golden Boots, from FIFA Best to 
    league MVPs - these honors recognize the finest individual performances in football. Let's explore how Messi and 
    Ronaldo stack up in terms of personal accolades and recognition from peers, media, and fans worldwide.
    """)
    
    # Major Awards Overview
    st.markdown('<h3 class="section-header">🏆 Major Individual Awards Overview</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Ballon d'Or", "8", "3 more")
        st.caption("🇦🇷 Messi dominates")
        st.write("**Messi:** 2009, 2010, 2011, 2012, 2015, 2019, 2021, 2023")
        st.write("**Ronaldo:** 2008, 2013, 2014, 2016, 2017")
    
    with col2:
        st.metric("FIFA Best", "3", "1 more")
        st.caption("🇦🇷 Messi leads")
        st.write("**Messi:** 2019, 2022, 2023")
        st.write("**Ronaldo:** 2016, 2017")
    
    with col3:
        st.metric("Golden Boot", "6", "2 more")
        st.caption("🇦🇷 Messi leads")
        st.write("**Messi:** 2010, 2012, 2013, 2017, 2018, 2019")
        st.write("**Ronaldo:** 2008, 2011, 2014, 2015")
    
    with col4:
        st.metric("UEFA Player", "3", "tied")
        st.caption("🤝 Tied")
        st.write("**Messi:** 2011, 2015, 2019")
        st.write("**Ronaldo:** 2014, 2016, 2017")
    
    with col5:
        st.metric("Liga MVP", "6", "4 more")
        st.caption("🇦🇷 Messi dominates")
        st.write("**Messi:** Multiple La Liga MVPs")
        st.write("**Ronaldo:** 2 La Liga MVPs")
    
    # Ballon d'Or timeline
    st.markdown('<h3 class="section-header">🥇 Ballon d\'Or Timeline & Era Dominance</h3>', unsafe_allow_html=True)
    
    # Create Ballon d'Or timeline data
    ballon_years = list(range(2007, 2024))
    ballon_winners = []
    for year in ballon_years:
        if year in [2009, 2010, 2011, 2012, 2015, 2019, 2021, 2023]:
            ballon_winners.append('Messi')
        elif year in [2008, 2013, 2014, 2016, 2017]:
            ballon_winners.append('Ronaldo')
        elif year == 2007:
            ballon_winners.append('Kaká')
        elif year == 2018:
            ballon_winners.append('Modrić')
        elif year == 2020:
            ballon_winners.append('Cancelled')
        elif year == 2022:
            ballon_winners.append('Benzema')
        else:
            ballon_winners.append('Other')
    
    # Create timeline visualization
    fig = go.Figure()
    
    for i, (year, winner) in enumerate(zip(ballon_years, ballon_winners)):
        if winner == 'Messi':
            color = '#4ECDC4'
            symbol = 'star'
        elif winner == 'Ronaldo':
            color = '#FF6B6B'
            symbol = 'star'
        else:
            color = 'lightgray'
            symbol = 'circle'
        
        fig.add_trace(go.Scatter(
            x=[year],
            y=[1],
            mode='markers',
            marker=dict(size=20, color=color, symbol=symbol),
            name=winner,
            showlegend=False,
            text=f"{year}<br>{winner}",
            hovertemplate='%{text}<extra></extra>'
        ))
    
    # Add era annotations
    fig.add_annotation(x=2010.5, y=1.2, text="Messi Era 1<br>(4 consecutive)", showarrow=True, arrowcolor="#4ECDC4")
    fig.add_annotation(x=2014.5, y=0.8, text="Ronaldo Peak<br>(2 of 3)", showarrow=True, arrowcolor="#FF6B6B")
    fig.add_annotation(x=2022, y=1.2, text="Messi Era 2<br>(2 recent)", showarrow=True, arrowcolor="#4ECDC4")
    
    fig.update_layout(
        title="🥇 Ballon d'Or Timeline (2007-2023)",
        xaxis_title="Year",
        yaxis=dict(visible=False),
        height=300,
        template='plotly_white',
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Major awards comparison
    st.markdown('<h3 class="section-header">📊 Major Awards Comparison</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Main awards bar chart
        awards_categories = ['Ballon d\'Or', 'FIFA Best', 'Golden Boot', 'UEFA Player', 'World Cup Golden Ball']
        messi_awards = [8, 3, 6, 3, 1]
        ronaldo_awards = [5, 2, 4, 3, 0]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=awards_categories,
            y=messi_awards,
            marker_color='#4ECDC4',
            text=messi_awards,
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=awards_categories,
            y=ronaldo_awards,
            marker_color='#FF6B6B',
            text=ronaldo_awards,
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🏆 Major Individual Awards",
            barmode='group',
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Awards by decade
        decades_data = {
            'Decade': ['2000s', '2010s', '2020s'],
            'Messi Ballon d\'Or': [1, 5, 2],
            'Ronaldo Ballon d\'Or': [1, 4, 0],
            'Messi Major Awards': [2, 15, 8],
            'Ronaldo Major Awards': [3, 12, 2]
        }
        
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('🥇 Ballon d\'Or by Decade', '🏆 Major Awards by Decade'),
            vertical_spacing=0.15
        )
        
        # Ballon d'Or by decade
        fig.add_trace(
            go.Bar(x=decades_data['Decade'], y=decades_data['Messi Ballon d\'Or'], 
                   name='Messi', marker_color='#4ECDC4'),
            row=1, col=1
        )
        fig.add_trace(
            go.Bar(x=decades_data['Decade'], y=decades_data['Ronaldo Ballon d\'Or'], 
                   name='Ronaldo', marker_color='#FF6B6B'),
            row=1, col=1
        )
        
        # Major awards by decade
        fig.add_trace(
            go.Bar(x=decades_data['Decade'], y=decades_data['Messi Major Awards'], 
                   name='Messi', marker_color='#4ECDC4', showlegend=False),
            row=2, col=1
        )
        fig.add_trace(
            go.Bar(x=decades_data['Decade'], y=decades_data['Ronaldo Major Awards'], 
                   name='Ronaldo', marker_color='#FF6B6B', showlegend=False),
            row=2, col=1
        )
        
        fig.update_layout(height=500, title_text="📈 Awards by Decade Analysis")
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed awards breakdown
    st.markdown('<h3 class="section-header">📋 Complete Awards Breakdown</h3>', unsafe_allow_html=True)
    
    # Create comprehensive awards data
    comprehensive_awards = {
        'Award Category': [
            'Ballon d\'Or', 'FIFA Best Player', 'Golden Boot', 'UEFA Player of Year', 
            'World Cup Golden Ball', 'Champions League Top Scorer', 'Liga MVP',
            'Laureus Sportsman', 'Globe Soccer Player', 'IFFHS Player',
            'FIFPro World XI', 'UEFA Team of Year', 'World Soccer Player',
            'Onze d\'Or', 'Goal.com Player', 'ESPN Player'
        ],
        'Messi': [8, 3, 6, 3, 1, 6, 6, 2, 7, 6, 17, 16, 3, 2, 4, 3],
        'Ronaldo': [5, 2, 4, 3, 0, 7, 2, 2, 6, 5, 15, 14, 2, 1, 3, 2],
        'Description': [
            'Most prestigious individual award',
            'FIFA\'s top player award (since 2016)',
            'Europe\'s top goalscorer award',
            'UEFA\'s best player in Europe',
            'World Cup best player award',
            'Champions League top scorer',
            'League Most Valuable Player',
            'Laureus World Sportsman',
            'Globe Soccer best player',
            'IFFHS World\'s Best Player',
            'FIFA/FIFPro World XI selections',
            'UEFA Team of the Year inclusions',
            'World Soccer Magazine Player',
            'French magazine Onze d\'Or',
            'Goal.com Player of Year',
            'ESPN Player of the Year'
        ]
    }
    
    awards_df = pd.DataFrame(comprehensive_awards)
    st.dataframe(awards_df, use_container_width=True, height=600)
    
    # Awards by competition level
    st.markdown('<h3 class="section-header">🌍 Awards by Competition Level</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🌍 International Awards</h4>
            <p><strong>🇦🇷 Messi:</strong></p>
            <p>• World Cup Golden Ball (2014, 2022)</p>
            <p>• Copa América Best Player (2021)</p>
            <p>• Olympic Gold Medal (2008)</p>
            <p>• U-20 World Cup Golden Ball (2005)</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo:</strong></p>
            <p>• Euro Team of Tournament (2016)</p>
            <p>• Nations League Top Scorer (2019)</p>
            <p>• Euro Top Scorer (2021)</p>
            <p>• World Cup Top Scorer candidate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏆 Club Competition Awards</h4>
            <p><strong>🇦🇷 Messi:</strong></p>
            <p>• 6 Champions League Top Scorers</p>
            <p>• 6 La Liga MVP awards</p>
            <p>• 3 UEFA Best Player in Europe</p>
            <p>• Multiple Club Player of Year</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo:</strong></p>
            <p>• 7 Champions League Top Scorers</p>
            <p>• 2 La Liga MVP awards</p>
            <p>• 3 UEFA Best Player in Europe</p>
            <p>• Multiple league top scorers</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>🌟 Global Recognition Awards</h4>
            <p><strong>🇦🇷 Messi:</strong></p>
            <p>• 17 FIFPro World XI selections</p>
            <p>• 2 Laureus Sportsman awards</p>
            <p>• 7 Globe Soccer Player awards</p>
            <p>• Time 100 Most Influential</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo:</strong></p>
            <p>• 15 FIFPro World XI selections</p>
            <p>• 2 Laureus Sportsman awards</p>
            <p>• 6 Globe Soccer Player awards</p>
            <p>• Multiple global recognition</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Awards timeline evolution
    st.markdown('<h3 class="section-header">📈 Awards Evolution Timeline</h3>', unsafe_allow_html=True)
    
    # Create awards timeline
    years_timeline = list(range(2005, 2024))
    messi_annual_awards = [1, 2, 1, 3, 4, 6, 5, 7, 3, 4, 5, 3, 4, 2, 3, 4, 2, 3, 5]
    ronaldo_annual_awards = [0, 1, 2, 4, 2, 3, 4, 2, 6, 5, 4, 3, 3, 2, 1, 2, 1, 1, 1]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years_timeline,
        y=messi_annual_awards,
        mode='lines+markers',
        name='Messi Annual Awards',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Messi</b><br>Year: %{x}<br>Awards: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=years_timeline,
        y=ronaldo_annual_awards,
        mode='lines+markers',
        name='Ronaldo Annual Awards',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Ronaldo</b><br>Year: %{x}<br>Awards: %{y}<extra></extra>'
    ))
    
    # Add peak annotations
    fig.add_annotation(x=2012, y=7, text="Messi's Record Year<br>7 Major Awards", arrowcolor="#4ECDC4", arrowwidth=2)
    fig.add_annotation(x=2014, y=6, text="Ronaldo's Peak<br>6 Major Awards", arrowcolor="#FF6B6B", arrowwidth=2)
    fig.add_annotation(x=2023, y=5, text="Messi's Renaissance<br>5 Major Awards", arrowcolor="#4ECDC4", arrowwidth=2)
    
    fig.update_layout(
        title="🏆 Annual Major Awards Timeline (2005-2023)",
        xaxis_title="Year",
        yaxis_title="Major Awards Won",
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Age-based awards analysis
    st.markdown('<h3 class="section-header">⏰ Awards by Age Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi age groups
        messi_age_groups = {
            'Age Group': ['18-23', '24-29', '30-35', '36+'],
            'Ballon d\'Or': [1, 4, 2, 1],
            'Major Awards': [5, 18, 12, 6],
            'Peak Years': ['2009', '2010-2015', '2019-2021', '2023']
        }
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Ballon d\'Or',
            x=messi_age_groups['Age Group'],
            y=messi_age_groups['Ballon d\'Or'],
            marker_color='#4ECDC4',
            text=messi_age_groups['Ballon d\'Or'],
            textposition='auto'
        ))
        fig.add_trace(go.Scatter(
            name='Total Major Awards',
            x=messi_age_groups['Age Group'],
            y=messi_age_groups['Major Awards'],
            mode='lines+markers',
            marker_color='#45B7D1',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="🇦🇷 Messi's Awards by Age",
            yaxis=dict(title="Ballon d'Or", side="left"),
            yaxis2=dict(title="Total Major Awards", side="right", overlaying="y"),
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Ronaldo age groups
        ronaldo_age_groups = {
            'Age Group': ['18-23', '24-29', '30-35', '36+'],
            'Ballon d\'Or': [1, 2, 2, 0],
            'Major Awards': [3, 12, 15, 3],
            'Peak Years': ['2008', '2013-2014', '2016-2017', '2021+']
        }
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Ballon d\'Or',
            x=ronaldo_age_groups['Age Group'],
            y=ronaldo_age_groups['Ballon d\'Or'],
            marker_color='#FF6B6B',
            text=ronaldo_age_groups['Ballon d\'Or'],
            textposition='auto'
        ))
        fig.add_trace(go.Scatter(
            name='Total Major Awards',
            x=ronaldo_age_groups['Age Group'],
            y=ronaldo_age_groups['Major Awards'],
            mode='lines+markers',
            marker_color='#FF9999',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="🇵🇹 Ronaldo's Awards by Age",
            yaxis=dict(title="Ballon d'Or", side="left"),
            yaxis2=dict(title="Total Major Awards", side="right", overlaying="y"),
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Awards voting analysis
    st.markdown('<h3 class="section-header">🗳️ Ballon d\'Or Voting Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🥇 Ballon d'Or Wins
        **🇦🇷 Messi: 8 wins**
        - 2009: First win at 22
        - 2010-2012: Historic 4 consecutive
        - 2015: Barcelona treble year
        - 2019: 6th Ballon d'Or
        - 2021: Copa América triumph
        - 2023: World Cup winner
        
        **🇵🇹 Ronaldo: 5 wins**
        - 2008: Manchester United peak
        - 2013: Real Madrid arrival
        - 2014: La Décima year
        - 2016: Euro 2016 champion
        - 2017: Champions League hero
        """)
    
    with col2:
        st.markdown("""
        ### 🥈 Runner-up Finishes
        **🇦🇷 Messi: 6 times**
        - 2008, 2013, 2014, 2016, 2017, 2020
        - Often lost to Ronaldo
        - Incredible consistency
        
        **🇵🇹 Ronaldo: 6 times**
        - 2007, 2009, 2011, 2012, 2015, 2018
        - Often lost to Messi
        - Equal consistency
        
        **Combined dominance:**
        - 13 wins between them
        - 12 runner-up finishes
        - 15-year duopoly (2008-2023*)
        """)
    
    with col3:
        st.markdown("""
        ### 📊 Voting Statistics
        **🇦🇷 Messi averages:**
        - 8 wins in 16 eligible years
        - 50% win rate since 2008
        - Youngest 4-time winner
        - Oldest winner (36 in 2023)
        
        **🇵🇹 Ronaldo averages:**
        - 5 wins in 16 eligible years
        - 31% win rate since 2008
        - Most nominations (16)
        - Consistent top-3 finishes
        
        **🤝 Shared records:**
        - Only players with 5+ wins
        - Most top-3 finishes ever
        """)
    
    # Final awards verdict
    st.markdown('<h3 class="section-header">🏁 Individual Awards Verdict</h3>', unsafe_allow_html=True)
    
    # Calculate awards scores
    messi_awards_score = 8 + 3 + 6 + 3 + 1  # Major awards
    ronaldo_awards_score = 5 + 2 + 4 + 3 + 0  # Major awards
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>🥇 Individual Awards Champion</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI: {messi_awards_score} Major Awards</h3>
                <p>✅ 8 Ballon d'Or (Record)</p>
                <p>✅ 6 Golden Boots (Record)</p>
                <p>✅ 3 FIFA Best Player</p>
                <p>✅ World Cup Golden Ball</p>
                <p>✅ More league MVP awards</p>
            </div>
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO: {ronaldo_awards_score} Major Awards</h3>
                <p>✅ 5 Ballon d'Or (2nd most ever)</p>
                <p>✅ 7 Champions League top scorer</p>
                <p>✅ Equal UEFA Player awards (3)</p>
                <p>✅ Consistent excellence (16 years)</p>
                <p>✅ More CL individual honors</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Awards Winner:</strong> 🇦🇷 <strong>MESSI</strong> - Record 8 Ballon d'Or tips the scales!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final analysis
    st.markdown("""
    ---
    ### 🌟 Individual Awards Legacy
    
    **🇦🇷 Messi's awards collection** represents the pinnacle of individual recognition in football. His record 8 Ballon d'Or 
    awards, including 4 consecutive wins and a remarkable comeback at age 36, showcase sustained excellence across different 
    eras. His 6 Golden Boots and World Cup Golden Ball cement his status as the most decorated individual player.
    
    **🇵🇹 Ronaldo's awards cabinet** demonstrates incredible consistency and longevity. His 5 Ballon d'Or awards span nearly 
    a decade, and his 7 Champions League top scorer awards highlight his big-game mentality. His ability to maintain 
    elite-level recognition across 4 different leagues is unmatched.
    
    **🏆 The Verdict:** While both players have dominated individual awards like no others in football history, 
    Messi's record-breaking 8 Ballon d'Or awards and superior collection of major individual honors give him 
    the edge in this category. However, both players have redefined what individual excellence means in football.
    
    **📊 Combined Legacy:** Together, they've won 13 of the last 16 Ballon d'Or awards (2008-2023), completely 
    dominating the most prestigious individual award in sports for over 15 years.
    """)

if __name__ == "__main__":
    show()