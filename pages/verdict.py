import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    """Display the final verdict with clutch design theme"""
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
    
    st.set_page_config(page_title="Final Verdict", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: #FFD700; font-family: 'Times New Roman', serif;">
    🏁 THE FINAL VERDICT
    </h1>
    """, unsafe_allow_html=True)
    
    # Enhanced scoring system
    categories = [
        'Goal Scoring', 'Playmaking', 'Club Trophies', 'Individual Awards', 
        'International Success', 'Longevity', 'Technical Skills', 
        'Physical Attributes', 'Big Game Performance', 'Global Impact',
        'Versatility', 'Peak Performance', 'Clutch Factor', 'Leadership'
    ]
    
    # Scoring data
    messi_scores = [8.9, 9.9, 9.4, 10.0, 9.6, 8.8, 9.8, 7.4, 9.3, 9.5, 9.2, 9.8, 9.0, 9.1]
    ronaldo_scores = [9.8, 7.3, 8.8, 8.7, 8.8, 9.8, 8.7, 9.6, 9.7, 9.7, 9.6, 9.2, 9.5, 9.3]
    weights = [1.3, 1.2, 1.1, 1.2, 1.4, 1.0, 1.1, 0.8, 1.3, 1.0, 0.9, 1.1, 1.2, 1.0]
    
    # Calculate totals
    messi_total = sum(messi_scores)
    ronaldo_total = sum(ronaldo_scores)
    messi_weighted = sum(m * w for m, w in zip(messi_scores, weights))
    ronaldo_weighted = sum(r * w for r, w in zip(ronaldo_scores, weights))
    
    # Quick overview cards
    st.markdown("## 📊 GOAT Competition Overview")
    
    # Custom metrics cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    messi_wins = sum(1 for m, r in zip(messi_scores, ronaldo_scores) if m > r)
    ronaldo_wins = sum(1 for m, r in zip(messi_scores, ronaldo_scores) if r > m)
    
    with col1:
        st.markdown(f"""
        <div style="
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Categories Won</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_wins} vs {ronaldo_wins}
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +{ronaldo_wins-messi_wins}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Total Score</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_total:.1f} vs {ronaldo_total:.1f}
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +{messi_total-ronaldo_total:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">⚖️</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Weighted Score</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_weighted:.1f} vs {ronaldo_weighted:.1f}
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +{messi_weighted-ronaldo_weighted:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        messi_avg = np.mean(messi_scores)
        ronaldo_avg = np.mean(ronaldo_scores)
        st.markdown(f"""
        <div style="
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">📈</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Average Score</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_avg:.1f} vs {ronaldo_avg:.1f}
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +{messi_avg-ronaldo_avg:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        messi_peak = max(messi_scores)
        ronaldo_peak = max(ronaldo_scores)
        st.markdown(f"""
        <div style="
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🔥</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Peak Score</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                {messi_peak:.1f} vs {ronaldo_peak:.1f}
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +{messi_peak-ronaldo_peak:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main comprehensive radar chart
    st.markdown('## 📊 Comprehensive GOAT Analysis')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Radar chart
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=messi_scores,
            theta=categories,
            fill='toself',
            name='Messi',
            fillcolor=f'rgba(117, 170, 219, 0.3)',
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=ronaldo_scores,
            theta=categories,
            fill='toself',
            name='Ronaldo',
            fillcolor=f'rgba(255, 45, 45, 0.3)',
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            height=500,
            showlegend=True,
            title="GOAT Performance Radar",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with col2:
        # Category winners visualization
        winners = []
        colors = []
        for m, r in zip(messi_scores, ronaldo_scores):
            if m > r:
                winners.append('Messi')
                colors.append(MESSI_COLOR)
            elif r > m:
                winners.append('Ronaldo')
                colors.append(RONALDO_COLOR)
            else:
                winners.append('Tie')
                colors.append('#FFCE56')
        
        fig_winners = go.Figure(data=[
            go.Bar(x=categories, y=[1]*len(categories), 
                   marker_color=colors, text=winners, textposition='inside',
                   textfont=dict(color='white', size=10, family='Times New Roman'))
        ])
        fig_winners.update_layout(
            height=500,
            xaxis_tickangle=-45,
            showlegend=False,
            yaxis=dict(visible=False),
            title="Category Winners",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_winners, use_container_width=True)
    
    # Head-to-head score comparison
    st.markdown('## ⚖️ Head-to-Head Score Comparison')
    
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        name='🇦🇷 Messi',
        x=categories,
        y=messi_scores,
        marker_color=MESSI_COLOR,
        text=messi_scores,
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    fig_comparison.add_trace(go.Bar(
        name='🇵🇹 Ronaldo',
        x=categories,
        y=ronaldo_scores,
        marker_color=RONALDO_COLOR,
        text=ronaldo_scores,
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    
    fig_comparison.update_layout(
        barmode='group',
        height=500,
        xaxis_tickangle=-45,
        yaxis_title="Score (0-10)",
        yaxis=dict(range=[0, 11]),
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Performance heatmap
    st.markdown('## 🌡️ Performance Intensity Heatmap')
    
    heatmap_data = pd.DataFrame({
        'Category': categories,
        'Messi': messi_scores,
        'Ronaldo': ronaldo_scores
    }).set_index('Category').T
    
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=[messi_scores, ronaldo_scores],
        x=categories,
        y=['Messi', 'Ronaldo'],
        colorscale='RdYlBu_r',
        text=[messi_scores, ronaldo_scores],
        texttemplate="%{text:.1f}",
        textfont={"size": 12, "family": "Times New Roman"},
        hoverongaps=False
    ))
    
    fig_heatmap.update_layout(
        title="Performance Intensity by Category (Higher = Better)",
        height=300,
        xaxis_tickangle=-45,
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Why Messi wins despite fewer categories
    st.markdown('## 🤔 Why Messi Wins Despite Ronaldo Having More Categories?')
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(45deg, {RONALDO_COLOR}, {MESSI_COLOR});
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        color: white;
        font-family: 'Times New Roman', serif;
    ">
        <h3>🎯 It's Not Just About Category Count - It's About IMPORTANCE!</h3>
        <p style="font-size: 1.2rem; margin: 0;">Some categories matter more in defining the GOAT than others</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Raw category count
        fig_count = go.Figure(data=[
            go.Bar(x=['🇦🇷 Messi', '🇵🇹 Ronaldo'], 
                   y=[messi_wins, ronaldo_wins],
                   marker_color=[MESSI_COLOR, RONALDO_COLOR],
                   text=[f"{messi_wins} categories", f"{ronaldo_wins} categories"],
                   textposition='outside',
                   textfont=dict(family='Times New Roman'))
        ])
        fig_count.update_layout(
            height=400,
            yaxis_title="Categories Won",
            showlegend=False,
            title="Ronaldo Wins More Categories",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_count, use_container_width=True)
        
        st.markdown(f"""
        <div style="
            background: rgba(255, 45, 45, 0.1);
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid {RONALDO_COLOR};
            font-family: 'Times New Roman', serif;
        ">
            <p style="margin: 0; text-align: center;"><strong>🇵🇹 Ronaldo: {ronaldo_wins} categories</strong></p>
            <p style="margin: 0; text-align: center;"><strong>🇦🇷 Messi: {messi_wins} categories</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Weighted score
        fig_weighted = go.Figure(data=[
            go.Bar(x=['🇦🇷 Messi', '🇵🇹 Ronaldo'], 
                   y=[messi_weighted, ronaldo_weighted],
                   marker_color=[MESSI_COLOR, RONALDO_COLOR],
                   text=[f"{messi_weighted:.1f} points", f"{ronaldo_weighted:.1f} points"],
                   textposition='outside',
                   textfont=dict(family='Times New Roman'))
        ])
        fig_weighted.update_layout(
            height=400,
            yaxis_title="Weighted Score",
            showlegend=False,
            title="Messi Wins in Weighted Score",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_weighted, use_container_width=True)
        
        st.markdown(f"""
        <div style="
            background: rgba(117, 170, 219, 0.1);
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid {MESSI_COLOR};
            font-family: 'Times New Roman', serif;
        ">
            <p style="margin: 0; text-align: center;"><strong>🇦🇷 Messi: {messi_weighted:.1f} points</strong></p>
            <p style="margin: 0; text-align: center;"><strong>🇵🇹 Ronaldo: {ronaldo_weighted:.1f} points</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # High-impact categories analysis
    st.markdown('## 🎯 High-Impact Categories Analysis')
    
    high_impact_indices = [i for i, w in enumerate(weights) if w >= 1.2]
    high_impact_categories = [categories[i] for i in high_impact_indices]
    high_impact_messi = [messi_scores[i] for i in high_impact_indices]
    high_impact_ronaldo = [ronaldo_scores[i] for i in high_impact_indices]
    high_impact_weights = [weights[i] for i in high_impact_indices]
    
    fig_high_impact = go.Figure()
    fig_high_impact.add_trace(go.Bar(
        name='🇦🇷 Messi (High Impact)',
        x=high_impact_categories,
        y=high_impact_messi,
        marker_color=MESSI_COLOR,
        text=[f"{score:.1f}" for score in high_impact_messi],
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    fig_high_impact.add_trace(go.Bar(
        name='🇵🇹 Ronaldo (High Impact)',
        x=high_impact_categories,
        y=high_impact_ronaldo,
        marker_color=RONALDO_COLOR,
        text=[f"{score:.1f}" for score in high_impact_ronaldo],
        textposition='auto',
        textfont=dict(family='Times New Roman')
    ))
    
    # Add weight indicators
    for i, (cat, weight) in enumerate(zip(high_impact_categories, high_impact_weights)):
        fig_high_impact.add_annotation(
            x=i,
            y=10.5,
            text=f"Weight: {weight}x",
            showarrow=False,
            font=dict(size=10, color='orange', family='Times New Roman'),
            bgcolor='rgba(255,165,0,0.2)',
            bordercolor='orange'
        )
    
    fig_high_impact.update_layout(
        barmode='group',
        height=400,
        xaxis_tickangle=-45,
        yaxis_title="Score (0-10)",
        yaxis=dict(range=[0, 11]),
        title="Categories That Matter Most (Weight ≥ 1.2x)",
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig_high_impact, use_container_width=True)
    
    # Key insight
    messi_high_impact_wins = sum(1 for m, r in zip(high_impact_messi, high_impact_ronaldo) if m > r)
    total_high_impact = len(high_impact_categories)
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #FFD700, #FFA500);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        color: white;
        font-family: 'Times New Roman', serif;
    ">
        <h3>💡 The Key Insight</h3>
        <p style="font-size: 1.3rem; margin: 1rem 0;"><strong>In High-Impact Categories:</strong></p>
        <div style="display: flex; justify-content: space-around; margin: 1rem 0;">
            <div>
                <h2 style="margin: 0;">{messi_high_impact_wins}</h2>
                <p style="margin: 0;">🇦🇷 Messi Wins</p>
            </div>
            <div style="font-size: 2rem;">VS</div>
            <div>
                <h2 style="margin: 0;">{total_high_impact - messi_high_impact_wins}</h2>
                <p style="margin: 0;">🇵🇹 Ronaldo Wins</p>
            </div>
        </div>
        <p style="font-size: 1.1rem; margin: 1rem 0; font-style: italic;">
            🏆 Messi dominates the categories that define GOAT status!<br>
            📊 Quality beats quantity in the GOAT debate
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final Score Dashboard
    st.markdown('## 🎯 Final Score Dashboard')
    
    # Determine winner
    if messi_total > ronaldo_total:
        winner = "LIONEL MESSI"
        winner_emoji = "🇦🇷"
        winner_color = MESSI_COLOR
    else:
        winner = "CRISTIANO RONALDO"
        winner_emoji = "🇵🇹" 
        winner_color = RONALDO_COLOR
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {MESSI_COLOR}, #5a9bd4);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-family: 'Times New Roman', serif;
        ">
            <h2>🇦🇷 MESSI</h2>
            <h1 style="font-size: 3rem; margin: 1rem 0;">{messi_total:.1f}</h1>
            <p>Total Score</p>
            <h2 style="margin-top: 1rem;">{messi_weighted:.1f}</h2>
            <p>Weighted Score</p>
            <div style="margin-top: 1rem; font-size: 0.9rem;">
                <strong>Categories Won: {messi_wins}</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {winner_color}, #333);
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin: 2rem 0;
            font-family: 'Times New Roman', serif;
        ">
            <h1 style="font-size: 2rem; margin-bottom: 1rem;">👑 THE GOAT IS...</h1>
            <h1 style="font-size: 4rem; margin: 1rem 0; text-shadow: 3px 3px 6px rgba(0,0,0,0.5);">{winner_emoji}</h1>
            <h2 style="font-size: 2.5rem; font-weight: bold; margin: 1rem 0;">{winner}</h2>
            <p style="font-size: 1.3rem; opacity: 0.9;">Victory Margin: {abs(messi_total - ronaldo_total):.1f} points</p>
            <p style="font-size: 1.1rem; opacity: 0.8;">Weighted Margin: {abs(messi_weighted - ronaldo_weighted):.1f} points</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {RONALDO_COLOR}, #e02525);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-family: 'Times New Roman', serif;
        ">
            <h2>🇵🇹 RONALDO</h2>
            <h1 style="font-size: 3rem; margin: 1rem 0;">{ronaldo_total:.1f}</h1>
            <p>Total Score</p>
            <h2 style="margin-top: 1rem;">{ronaldo_weighted:.1f}</h2>
            <p>Weighted Score</p>
            <div style="margin-top: 1rem; font-size: 0.9rem;">
                <strong>Categories Won: {ronaldo_wins}</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Victory breakdown
    st.markdown('## 🏆 Victory Breakdown Analysis')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Score differences by category
        differences = [m - r for m, r in zip(messi_scores, ronaldo_scores)]
        colors = [MESSI_COLOR if diff > 0 else RONALDO_COLOR for diff in differences]
        
        fig_diff = go.Figure(data=[
            go.Bar(x=categories, y=differences, marker_color=colors, 
                   text=[f"{diff:+.1f}" for diff in differences], 
                   textposition='outside',
                   textfont=dict(family='Times New Roman'))
        ])
        fig_diff.update_layout(
            height=400,
            xaxis_tickangle=-45,
            yaxis_title="Score Difference (Messi - Ronaldo)",
            showlegend=False,
            yaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='black'),
            title="Score Differences by Category",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_diff, use_container_width=True)
    
    with col2:
        # Category dominance pie chart
        fig_donut = go.Figure(data=[go.Pie(
            labels=['🇦🇷 Messi Wins', '🇵🇹 Ronaldo Wins'],
            values=[messi_wins, ronaldo_wins],
            hole=.6,
            marker_colors=[MESSI_COLOR, RONALDO_COLOR],
            textfont=dict(family='Times New Roman')
        )])
        fig_donut.update_layout(
            height=400,
            title="Category Dominance",
            annotations=[dict(text=f"{messi_wins} vs {ronaldo_wins}", x=0.5, y=0.5, 
                             font_size=20, showarrow=False, 
                             font=dict(family='Times New Roman'))],
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_donut, use_container_width=True)
    
    # Interactive voting
    st.markdown('## 🗳️ Cast Your Vote')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🇦🇷 Vote Messi", key="vote_messi", use_container_width=True):
            st.success("🐐 Team Messi!")
            st.balloons()
    
    with col2:
        if st.button("🤝 Both GOATs", key="vote_both", use_container_width=True):
            st.success("🐐🐐 Diplomatic choice!")
            st.balloons()
    
    with col3:
        if st.button("🇵🇹 Vote Ronaldo", key="vote_ronaldo", use_container_width=True):
            st.success("🐐 Team Ronaldo!")
            st.balloons()
    
    # Summary statistics
    st.markdown('## 📊 Final Statistics Summary')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="
            border-radius: 25px;
            padding: 25px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏅</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Excellence</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                MESSI
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">Higher avg & peak</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            border-radius: 25px;
            padding: 25px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">📊</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Breadth</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                RONALDO
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">More categories</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            border-radius: 25px;
            padding: 25px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🎯</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Impact</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                MESSI
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">Key categories</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="
            border-radius: 25px;
            padding: 25px;
            text-align: center;
            border: 2px solid #FFD700;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">👑</div>
            <h4 style="color: #FFD700; margin: 0 0 10px 0;">WINNER</h4>
            <div style="font-size: 2rem; font-weight: 900; color: #FFD700; margin: 10px 0;">
                MESSI
            </div>
            <div style="
                background: #FFD700; 
                color: white; 
                padding: 8px 16px; 
                border-radius: 25px; 
                font-weight: bold;
                font-size: 0.9rem;
            ">The GOAT</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick stats table
    stats_data = pd.DataFrame({
        'Metric': ['Categories Won', 'Total Score', 'Weighted Score', 'Average Score', 'Peak Score', 'Consistency (Std Dev)'],
        'Messi': [
            messi_wins, 
            f"{messi_total:.1f}", 
            f"{messi_weighted:.1f}", 
            f"{np.mean(messi_scores):.1f}", 
            f"{max(messi_scores):.1f}", 
            f"{np.std(messi_scores):.2f}"
        ],
        'Ronaldo': [
            ronaldo_wins, 
            f"{ronaldo_total:.1f}", 
            f"{ronaldo_weighted:.1f}", 
            f"{np.mean(ronaldo_scores):.1f}", 
            f"{max(ronaldo_scores):.1f}", 
            f"{np.std(ronaldo_scores):.2f}"
        ]
    })
    
    st.dataframe(stats_data, use_container_width=True, hide_index=True)
    
    # Closing message
    st.markdown(f"""
    <div style="
        background: linear-gradient(45deg, {RONALDO_COLOR}, {MESSI_COLOR});
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        color: white;
        font-family: 'Times New Roman', serif;
    ">
        <h3>🌟 The Greatest Era in Football History</h3>
        <p style="font-size: 1.2rem; margin: 1rem 0;">
            Whether {winner} or not, we witnessed two legends push each other to impossible heights. 
            <br><strong>Football wins. We all win.</strong> ⚽
        </p>
        <p style="font-size: 1rem; margin: 1rem 0; opacity: 0.9;">
            The debate will continue forever, and that's what makes it beautiful. 🐐
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()