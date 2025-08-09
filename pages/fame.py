import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def show():
    """Display visual fame and global impact analysis"""
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
    
    st.set_page_config(page_title="Fame & Global Impact", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: {RONALDO_COLOR}; font-family: 'Times New Roman', serif;">
    🌟 FAME & GLOBAL IMPACT ANALYSIS
    </h1>
    """, unsafe_allow_html=True)
    
    # Quick stats cards with custom design
    st.markdown("## 📊 Global Fame Overview")
    
    # Custom metrics cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">📱</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Instagram</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                610M vs 504M
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +106M</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🎬</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">YouTube</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                57M vs 2.3M
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +55M</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">💰</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Earnings</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                $130M vs $120M
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +$10M</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
            <h5 style="color: {MESSI_COLOR}; margin: 0 0 8px 0;">Ballon d'Or</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                8 vs 5
            </div>
            <div style="
                background: {MESSI_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Messi +3</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🌍</div>
            <h5 style="color: {RONALDO_COLOR}; margin: 0 0 8px 0;">Global Reach</h5>
            <div style="font-size: 1.5rem; font-weight: 900; color: #FFD700; margin: 8px 0;">
                3.2B vs 2.8B
            </div>
            <div style="
                background: {RONALDO_COLOR}; 
                color: white; 
                padding: 6px 12px; 
                border-radius: 20px; 
                font-weight: bold;
                font-size: 0.8rem;
            ">Ronaldo +400M</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main fame comparison
    st.markdown('## 🌟 Fame & Popularity Comparison')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Social media followers bar chart
        platforms = ['Instagram', 'Facebook', 'Twitter', 'YouTube', 'TikTok']
        messi_followers = [504, 111, 44, 2.3, 34]
        ronaldo_followers = [610, 170, 108, 57, 51]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi (Millions)',
            x=platforms,
            y=messi_followers,
            marker_color=MESSI_COLOR,
            text=[f'{x}M' for x in messi_followers],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo (Millions)',
            x=platforms,
            y=ronaldo_followers,
            marker_color=RONALDO_COLOR,
            text=[f'{x}M' for x in ronaldo_followers],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Social Media Followers",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Fame radar chart
        radar_categories = ['Social Media', 'Endorsements', 'Media Coverage', 'Global Recognition', 'Brand Value']
        messi_radar = [85, 95, 90, 95, 88]
        ronaldo_radar = [98, 88, 85, 90, 92]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_radar,
            theta=radar_categories,
            fill='toself',
            name='Messi',
            fillcolor=f'rgba(117, 170, 219, 0.3)',
            line=dict(color=MESSI_COLOR, width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_radar,
            theta=radar_categories,
            fill='toself',
            name='Ronaldo',
            fillcolor=f'rgba(255, 45, 45, 0.3)',
            line=dict(color=RONALDO_COLOR, width=3)
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Fame & Influence Radar",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Endorsements and brand value
    st.markdown('## 💰 Brand Value & Endorsements')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Annual earnings breakdown
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'pie'}, {'type': 'pie'}]],
            subplot_titles=['Messi: $130M Annual', 'Ronaldo: $120M Annual']
        )
        
        fig.add_trace(go.Pie(
            labels=['Salary', 'Endorsements', 'Investments'],
            values=[75, 45, 10],
            marker_colors=[MESSI_COLOR, '#45B7D1', '#96CEB4'],
            name='Messi',
            textfont=dict(family='Times New Roman')
        ), row=1, col=1)
        
        fig.add_trace(go.Pie(
            labels=['Salary', 'Endorsements', 'Investments'],
            values=[70, 40, 10],
            marker_colors=[RONALDO_COLOR, '#FF9999', '#FD79A8'],
            name='Ronaldo',
            textfont=dict(family='Times New Roman')
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="Annual Earnings Breakdown", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Major endorsement deals
        brands = ['Adidas', 'Nike', 'Pepsi', 'Mastercard', 'Other']
        messi_deals = [25, 0, 4, 3, 13]
        ronaldo_deals = [0, 20, 0, 0, 20]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=brands,
            y=messi_deals,
            marker_color=MESSI_COLOR,
            text=[f'${x}M' for x in messi_deals],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=brands,
            y=ronaldo_deals,
            marker_color=RONALDO_COLOR,
            text=[f'${x}M' for x in ronaldo_deals],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Major Endorsement Deals (Annual)",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Career earnings timeline
        years = list(range(2010, 2024))
        messi_earnings = [25, 32, 41, 45, 52, 64, 73, 80, 92, 104, 110, 126, 130, 130]
        ronaldo_earnings = [30, 38, 44, 50, 58, 67, 79, 88, 95, 105, 115, 125, 120, 120]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=messi_earnings,
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=10)
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=ronaldo_earnings,
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Annual Earnings Over Time",
            xaxis_title="Year",
            yaxis_title="Earnings (Millions USD)",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Global impact and recognition
    st.markdown('## 🌍 Global Impact & Recognition')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Awards and recognition
        award_types = ['Individual', 'Team', 'Special', 'Honorary']
        messi_awards = [95, 47, 15, 8]
        ronaldo_awards = [85, 52, 12, 6]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=award_types,
            y=messi_awards,
            mode='lines+markers+text',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=15),
            text=messi_awards,
            textposition='top center',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Scatter(
            x=award_types,
            y=ronaldo_awards,
            mode='lines+markers+text',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=15),
            text=ronaldo_awards,
            textposition='top center',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Awards & Recognition Count",
            yaxis_title="Number of Awards",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Media coverage and search trends
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'pie'}, {'type': 'pie'}]],
            subplot_titles=['Google Searches (Billions)', 'Media Mentions (Millions)']
        )
        
        fig.add_trace(go.Pie(
            labels=['Messi', 'Ronaldo'],
            values=[2.8, 3.2],
            marker_colors=[MESSI_COLOR, RONALDO_COLOR],
            name='Searches',
            textfont=dict(family='Times New Roman')
        ), row=1, col=1)
        
        fig.add_trace(go.Pie(
            labels=['Messi', 'Ronaldo'],
            values=[145, 142],
            marker_colors=[MESSI_COLOR, RONALDO_COLOR],
            name='Media',
            textfont=dict(family='Times New Roman')
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="Digital Presence", font=dict(family='Times New Roman'))
        st.plotly_chart(fig, use_container_width=True)
    
    # Social media engagement analysis
    st.markdown('## 📱 Social Media Engagement')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Engagement rates by platform
        platforms = ['Instagram', 'Facebook', 'Twitter', 'YouTube']
        messi_engagement = [12.5, 8.2, 15.3, 25.1]
        ronaldo_engagement = [15.8, 9.1, 18.7, 28.4]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=platforms,
            y=messi_engagement,
            marker_color=MESSI_COLOR,
            text=[f'{x}%' for x in messi_engagement],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=platforms,
            y=ronaldo_engagement,
            marker_color=RONALDO_COLOR,
            text=[f'{x}%' for x in ronaldo_engagement],
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Engagement Rate by Platform",
            barmode='group',
            height=400,
            template='plotly_white',
            yaxis_title="Engagement Rate (%)",
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Social media growth timeline
        years = list(range(2015, 2024))
        messi_total_followers = [50, 85, 120, 160, 220, 290, 380, 450, 504]
        ronaldo_total_followers = [80, 130, 180, 240, 320, 420, 520, 580, 610]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=messi_total_followers,
            mode='lines+markers',
            name='Messi',
            line=dict(color=MESSI_COLOR, width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=ronaldo_total_followers,
            mode='lines+markers',
            name='Ronaldo',
            line=dict(color=RONALDO_COLOR, width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Social Media Growth (Instagram)",
            xaxis_title="Year",
            yaxis_title="Followers (Millions)",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Fame influence heatmap
    st.markdown('## 🔥 Global Influence Heatmap')
    
    regions = ['Europe', 'South America', 'North America', 'Asia', 'Africa', 'Middle East']
    players = ['Messi', 'Ronaldo']
    influence_matrix = [
        [85, 95, 75, 80, 70, 65],  # Messi
        [90, 70, 80, 85, 75, 90]   # Ronaldo
    ]
    
    fig = go.Figure(data=go.Heatmap(
        z=influence_matrix,
        x=regions,
        y=players,
        colorscale='RdYlBu_r',
        text=influence_matrix,
        texttemplate="%{text}",
        textfont={"size": 20, "family": "Times New Roman"},
        hoverongaps=False
    ))
    
    fig.update_layout(
        title="Global Influence by Region (Higher = More Popular)",
        height=350,
        template='plotly_white',
        font=dict(family='Times New Roman')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Final comparison charts
    st.markdown('## 🏆 Fame Championship')
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Overall fame scores
        categories = ['Social Media', 'Endorsements', 'Recognition', 'Global Reach', 'Brand Value', 'Media Coverage']
        messi_scores = [85, 95, 95, 90, 88, 90]
        ronaldo_scores = [98, 88, 85, 95, 92, 85]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_scores,
            marker_color=MESSI_COLOR,
            text=messi_scores,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_scores,
            marker_color=RONALDO_COLOR,
            text=ronaldo_scores,
            textposition='auto',
            textfont=dict(family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Overall Fame Comparison",
            barmode='group',
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Winner pie chart
        winners = ['Ronaldo Wins', 'Messi Wins']
        win_counts = [4, 2]  # Ronaldo wins 4 categories, Messi wins 2
        
        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=winners,
            values=win_counts,
            marker_colors=[RONALDO_COLOR, MESSI_COLOR],
            textinfo='label+percent',
            textfont=dict(size=16, family='Times New Roman')
        ))
        
        fig.update_layout(
            title="Category Winners",
            height=400,
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Summary metrics with custom design
    st.markdown('## 🌟 Fame Championship Results')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">📱</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Social Media King</h4>
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
            ">+200M followers</div>
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
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🏆</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Award Champion</h4>
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
            ">8 Ballon d'Or</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🌍</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Global Reach</h4>
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
            ">3.2B reach</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
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
            margin: 10px 0;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">👑</div>
            <h4 style="color: #FFD700; margin: 0 0 10px 0;">FAME CHAMPION</h4>
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
            ">4/6 categories</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()