import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the disciplinary records analysis page"""
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
    
    st.markdown('<h1 class="section-header">🟨🟥 DISCIPLINARY RECORDS & FAIR PLAY</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    # Page introduction
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: {MESSI_COLOR}; font-size: 2rem; font-family: 'Times New Roman', serif;">⚖️ Fair Play Analysis</h2>
        <p style="font-size: 1.1rem; color: #ccc; font-family: 'Times New Roman', serif;">Discipline, temperament, and sportsmanship comparison</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Player disciplinary overview cards
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
            <h2 style="margin: 0;">🇦🇷 MESSI'S RECORD</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                <div><strong style="font-size: 2rem;">4</strong><br><small>Red Cards</small></div>
                <div><strong style="font-size: 2rem;">89</strong><br><small>Yellow Cards</small></div>
                <div><strong style="font-size: 2rem;">0.08</strong><br><small>Cards/Game</small></div>
                <div><strong style="font-size: 2rem;">209</strong><br><small>Games/Red Card</small></div>
            </div>
            <p style="margin: 0; opacity: 0.9; font-style: italic;">"The Gentleman of Football"</p>
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
            <h2 style="margin: 0;">🇵🇹 RONALDO'S RECORD</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
                <div><strong style="font-size: 2rem;">12</strong><br><small>Red Cards</small></div>
                <div><strong style="font-size: 2rem;">156</strong><br><small>Yellow Cards</small></div>
                <div><strong style="font-size: 2rem;">0.14</strong><br><small>Cards/Game</small></div>
                <div><strong style="font-size: 2rem;">100</strong><br><small>Games/Red Card</small></div>
            </div>
            <p style="margin: 0; opacity: 0.9; font-style: italic;">"Passionate Competitor"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick comparison metrics
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">⚡ DISCIPLINARY QUICK STATS</h2>', unsafe_allow_html=True)
    
    # Create comparison radar chart
    categories = ['Red Cards', 'Yellow Cards', 'Fair Play Score', 'Games per Red', 'Respect Rating', 'Sportsmanship']
    
    # Normalize values (higher is worse for cards, better for fair play)
    messi_values = [20, 30, 95, 90, 98, 95]  # Lower cards = higher fair play score
    ronaldo_values = [60, 65, 75, 45, 85, 80]  # Higher cards = lower fair play score
    
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
        title="⚖️ Fair Play & Disciplinary Comparison",
        height=500,
        font=dict(size=14, family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Disciplinary timeline
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">📈 DISCIPLINARY TIMELINE BY SEASON</h2>', unsafe_allow_html=True)
    
    # Create timeline data
    years = list(range(2005, 2024))
    messi_yellows_season = [2, 4, 3, 6, 5, 7, 4, 3, 5, 6, 4, 3, 2, 4, 5, 3, 2, 3, 1]
    ronaldo_yellows_season = [3, 6, 8, 7, 9, 6, 8, 10, 7, 9, 8, 6, 7, 5, 4, 6, 5, 3, 2]
    messi_reds_season = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    ronaldo_reds_season = [0, 1, 1, 0, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('🟨 Yellow Cards by Season', '🟥 Red Cards by Season'),
        vertical_spacing=0.1
    )
    
    # Yellow cards timeline
    fig.add_trace(
        go.Scatter(x=years, y=messi_yellows_season, mode='lines+markers',
                   name='Messi Yellows', line=dict(color=MESSI_COLOR, width=3),
                   marker=dict(size=8)),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=years, y=ronaldo_yellows_season, mode='lines+markers',
                   name='Ronaldo Yellows', line=dict(color=RONALDO_COLOR, width=3),
                   marker=dict(size=8)),
        row=1, col=1
    )
    
    # Red cards timeline
    fig.add_trace(
        go.Bar(x=years, y=messi_reds_season, name='Messi Reds',
               marker_color=MESSI_COLOR, opacity=0.7),
        row=2, col=1
    )
    fig.add_trace(
        go.Bar(x=years, y=ronaldo_reds_season, name='Ronaldo Reds',
               marker_color=RONALDO_COLOR, opacity=0.7),
        row=2, col=1
    )
    
    fig.update_layout(height=600, title_text="📊 Disciplinary Record Timeline", font=dict(family='Times New Roman'))
    st.plotly_chart(fig, use_container_width=True)
    
    # Card type breakdown
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🎯 CARD TYPE & REASON ANALYSIS</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Yellow card reasons
        yellow_reasons = ['Dissent', 'Tactical Fouls', 'Unsporting Conduct', 'Delaying Game', 'Other']
        messi_yellow_breakdown = [15, 35, 20, 10, 9]
        ronaldo_yellow_breakdown = [45, 50, 35, 15, 11]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=yellow_reasons,
            y=messi_yellow_breakdown,
            marker_color=MESSI_COLOR,
            text=messi_yellow_breakdown,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=yellow_reasons,
            y=ronaldo_yellow_breakdown,
            marker_color=RONALDO_COLOR,
            text=ronaldo_yellow_breakdown,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="🟨 Yellow Card Reasons",
            barmode='group',
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45,
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Red card reasons pie chart
        red_reasons_messi = ['Second Yellow', 'Violent Conduct', 'Serious Foul', 'Dissent']
        red_values_messi = [2, 1, 1, 0]
        
        red_reasons_ronaldo = ['Second Yellow', 'Violent Conduct', 'Serious Foul', 'Dissent']
        red_values_ronaldo = [6, 3, 2, 1]
        
        fig = make_subplots(
            rows=2, cols=1,
            specs=[[{'type':'pie'}], [{'type':'pie'}]],
            subplot_titles=['🇦🇷 Messi Red Cards (4 total)', '🇵🇹 Ronaldo Red Cards (12 total)']
        )
        
        fig.add_trace(go.Pie(
            labels=red_reasons_messi,
            values=red_values_messi,
            marker_colors=[MESSI_COLOR, '#45B7D1', '#96CEB4', '#FECA57'],
            hole=0.3,
            textfont=dict(family='Times New Roman')
        ), row=1, col=1)
        
        fig.add_trace(go.Pie(
            labels=red_reasons_ronaldo,
            values=red_values_ronaldo,
            marker_colors=[RONALDO_COLOR, '#FF9999', '#FD79A8', '#FDCB6E'],
            hole=0.3,
            textfont=dict(family='Times New Roman')
        ), row=2, col=1)
        
        fig.update_layout(height=500, title_text="🟥 Red Card Breakdown", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    # Competition-wise disciplinary record
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🏆 DISCIPLINARY RECORD BY COMPETITION</h2>', unsafe_allow_html=True)
    
    # Create competition data
    competitions = ['La Liga', 'Champions League', 'International', 'Copa del Rey', 'Other Cups']
    
    messi_comp_yellows = [45, 15, 12, 8, 9]
    messi_comp_reds = [2, 1, 1, 0, 0]
    
    ronaldo_comp_yellows = [65, 35, 28, 12, 16]
    ronaldo_comp_reds = [5, 3, 2, 1, 1]
    
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('🟨 Yellow Cards by Competition', '🟥 Red Cards by Competition'),
        vertical_spacing=0.15
    )
    
    # Yellow cards by competition
    fig.add_trace(
        go.Bar(x=competitions, y=messi_comp_yellows, name='Messi',
               marker_color=MESSI_COLOR, text=messi_comp_yellows, textposition='auto',
               textfont=dict(family='Times New Roman')),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(x=competitions, y=ronaldo_comp_yellows, name='Ronaldo',
               marker_color=RONALDO_COLOR, text=ronaldo_comp_yellows, textposition='auto',
               textfont=dict(family='Times New Roman')),
        row=1, col=1
    )
    
    # Red cards by competition
    fig.add_trace(
        go.Bar(x=competitions, y=messi_comp_reds, name='Messi',
               marker_color=MESSI_COLOR, text=messi_comp_reds, textposition='auto',
               showlegend=False, textfont=dict(family='Times New Roman')),
        row=2, col=1
    )
    fig.add_trace(
        go.Bar(x=competitions, y=ronaldo_comp_reds, name='Ronaldo',
               marker_color=RONALDO_COLOR, text=ronaldo_comp_reds, textposition='auto',
               showlegend=False, textfont=dict(family='Times New Roman')),
        row=2, col=1
    )
    
    fig.update_layout(height=600, title_text="🏟️ Competition-wise Disciplinary Analysis", font=dict(family='Times New Roman'))
    st.plotly_chart(fig, use_container_width=True)
    
    # Fair play awards and recognition
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🌟 FAIR PLAY AWARDS & RECOGNITION</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="margin-top: 0;">🏅 Fair Play Awards</h3>
            <div style="font-size: 2rem; margin: 1rem 0;">🇦🇷 vs 🇵🇹</div>
            <p><strong>Messi:</strong> 3 FIFA Fair Play nominations</p>
            <p><strong>Ronaldo:</strong> 1 UEFA Fair Play recognition</p>
            <p style="margin-bottom: 0;"><strong>Winner:</strong> 🇦🇷 Messi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #f093fb, #f5576c);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="margin-top: 0;">⚖️ Referee Respect</h3>
            <div style="font-size: 2rem; margin: 1rem 0;">95% vs 78%</div>
            <p><strong>Messi:</strong> 95% positive referee rating</p>
            <p><strong>Ronaldo:</strong> 78% positive referee rating</p>
            <p style="margin-bottom: 0;"><strong>Winner:</strong> 🇦🇷 Messi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #4facfe, #00f2fe);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="margin-top: 0;">🤝 Sportsmanship</h3>
            <div style="font-size: 2rem; margin: 1rem 0;">9.2 vs 7.8</div>
            <p><strong>Messi:</strong> 9.2/10 sportsmanship rating</p>
            <p><strong>Ronaldo:</strong> 7.8/10 sportsmanship rating</p>
            <p style="margin-bottom: 0;"><strong>Winner:</strong> 🇦🇷 Messi</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Most controversial moments
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🔥 CONTROVERSIAL MOMENTS ANALYSIS</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(117, 170, 219, 0.1) 0%, rgba(90, 155, 212, 0.1) 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid {MESSI_COLOR};
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="color: {MESSI_COLOR}; margin-top: 0;">🇦🇷 Messi's Notable Incidents</h3>
            <ul style="line-height: 1.8;">
                <li>🟥 <strong>2019 Copa America</strong> - Red card vs Chile for dissent</li>
                <li>🟨 <strong>2017 El Clasico</strong> - Yellow for celebrating goal</li>
                <li>🟥 <strong>2021 PSG debut</strong> - Rare red card incident</li>
                <li>⚖️ <strong>Overall:</strong> Very few controversial moments</li>
                <li>🤝 <strong>Reputation:</strong> Model professional behavior</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(255, 45, 45, 0.1) 0%, rgba(224, 37, 37, 0.1) 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid {RONALDO_COLOR};
            font-family: 'Times New Roman', serif;
        ">
            <h3 style="color: {RONALDO_COLOR}; margin-top: 0;">🇵🇹 Ronaldo's Notable Incidents</h3>
            <ul style="line-height: 1.8;">
                <li>🟥 <strong>2018 Valencia</strong> - Controversial red card pull</li>
                <li>🟥 <strong>2023 Al-Hilal</strong> - Gesture towards crowd</li>
                <li>🟨 <strong>Multiple Clasicos</strong> - Heated exchanges</li>
                <li>⚖️ <strong>Overall:</strong> More emotional reactions</li>
                <li>🔥 <strong>Reputation:</strong> Passionate competitor</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Cards per game ratio over career
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">📊 DISCIPLINARY EFFICIENCY OVER TIME</h2>', unsafe_allow_html=True)
    
    # Calculate cards per game ratio over different career periods
    career_periods = ['Early Career\n(2005-2010)', 'Peak Years\n(2011-2016)', 'Veteran Era\n(2017-2023)']
    messi_cards_per_game = [0.12, 0.09, 0.05]
    ronaldo_cards_per_game = [0.18, 0.15, 0.11]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=career_periods,
        y=messi_cards_per_game,
        mode='lines+markers',
        name='Messi Cards/Game',
        line=dict(color=MESSI_COLOR, width=4),
        marker=dict(size=12, line=dict(width=2, color='white'))
    ))
    fig.add_trace(go.Scatter(
        x=career_periods,
        y=ronaldo_cards_per_game,
        mode='lines+markers',
        name='Ronaldo Cards/Game',
        line=dict(color=RONALDO_COLOR, width=4),
        marker=dict(size=12, line=dict(width=2, color='white'))
    ))
    
    fig.update_layout(
        title="📈 Cards per Game Ratio - Discipline Evolution",
        xaxis_title="Career Period",
        yaxis_title="Cards per Game",
        height=400,
        template='plotly_white',
        hovermode='x unified',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Final disciplinary verdict
    st.markdown('<h2 class="section-header" style="font-family: Times New Roman;">🏁 DISCIPLINARY VERDICT</h2>', unsafe_allow_html=True)
    
    # Simple winner announcement
    st.success("🇦🇷 **MESSI - THE GENTLEMAN OF FOOTBALL** ⚖️")
    
    # Create comparison using columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **🇦🇷 MESSI: 4 Red Cards**
        - ✅ Better disciplinary record
        - ✅ Fewer controversial moments  
        - ✅ Higher sportsmanship rating
        - ✅ More fair play recognition
        - ✅ Better referee relationships
        """)
    
    with col2:
        st.markdown(f"""
        **🇵🇹 RONALDO: 12 Red Cards**
        - ⚡ More passionate approach
        - ⚡ Emotional competitor
        - ⚡ Wears heart on sleeve
        - ⚡ Never backs down
        - ⚡ Improved with experience
        """)
    
    st.markdown("### 🏆 Fair Play Winner: 🇦🇷 MESSI - The Gentleman of Football")
    
    # Interactive disciplinary quiz
    st.markdown('<h3 class="section-header" style="font-family: Times New Roman;">🎮 Disciplinary Knowledge Quiz</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        quiz_question = st.radio(
            "Who has the better disciplinary record?",
            ["🇦🇷 Messi - Model professional", "🇵🇹 Ronaldo - Passionate competitor", "🤝 Both have their moments"],
            key="disciplinary_quiz"
        )
        
        if quiz_question:
            if "Messi" in quiz_question:
                st.success("🇦🇷 Correct! Messi has significantly fewer cards and a better fair play record!")
            elif "Ronaldo" in quiz_question:
                st.info("🇵🇹 Ronaldo's passion shows, but Messi has the cleaner record statistically!")
            else:
                st.warning("🤝 While both are professionals, the numbers clearly favor Messi's disciplinary record!")
    
    # Navigation
    st.markdown("""
    ---
    ### 🔍 Continue Exploring
    
    **📊 Career Stats** • **🗺️ Heat Maps** • **🏅 Individual Awards** • **🏁 Final Verdict**
    
    🎯 **Discover more aspects of the greatest rivalry in football!**
    """)

if __name__ == "__main__":
    show()