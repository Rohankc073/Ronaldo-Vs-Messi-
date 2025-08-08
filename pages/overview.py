import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the complete overview page for Messi vs Ronaldo"""
    st.markdown('<h1 class="section-header">⚽ THE GREATEST OF ALL TIME DEBATE</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    career_stats = data['career_stats']
    
    # Hero section with enhanced player cards
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: #1f77b4; font-size: 2.5rem;">🐐 WHO IS THE GOAT? 🐐</h2>
        <p style="font-size: 1.3rem; color: #666;">The eternal debate that has divided football fans for over 15 years</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card" style="
            background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 1rem;
        ">
            <div style="text-align: center;">
                <h2 style="margin: 0; font-size: 2rem;">🇦🇷 LIONEL MESSI</h2>
                <h3 style="margin: 0.5rem 0; opacity: 0.9;">"La Pulga" - The Magician</h3>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; text-align: left;">
                    <div><strong>Age:</strong> 37</div>
                    <div><strong>Position:</strong> RW/CF/AM</div>
                    <div><strong>Current Club:</strong> Inter Miami CF</div>
                    <div><strong>Height:</strong> 1.70m (5'7")</div>
                    <div><strong>Goals:</strong> 815</div>
                    <div><strong>Assists:</strong> 377</div>
                    <div><strong>Ballon d'Or:</strong> 8 🏆</div>
                    <div><strong>World Cups:</strong> 1 🏆</div>
                </div>
                <div style="margin-top: 1rem; font-style: italic; opacity: 0.9;">
                    "The most naturally gifted player in football history"
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card" style="
            background: linear-gradient(135deg, #FF6B6B 0%, #C44569 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 1rem;
        ">
            <div style="text-align: center;">
                <h2 style="margin: 0; font-size: 2rem;">🇵🇹 CRISTIANO RONALDO</h2>
                <h3 style="margin: 0.5rem 0; opacity: 0.9;">"CR7" - The Goal Machine</h3>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; text-align: left;">
                    <div><strong>Age:</strong> 40</div>
                    <div><strong>Position:</strong> CF/LW</div>
                    <div><strong>Current Club:</strong> Al Nassr FC</div>
                    <div><strong>Height:</strong> 1.87m (6'2")</div>
                    <div><strong>Goals:</strong> 895</div>
                    <div><strong>Assists:</strong> 236</div>
                    <div><strong>Ballon d'Or:</strong> 5 🏆</div>
                    <div><strong>European Championships:</strong> 1 🏆</div>
                </div>
                <div style="margin-top: 1rem; font-style: italic; opacity: 0.9;">
                    "The most complete and dedicated athlete in history"
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick comparison metrics with enhanced styling
    st.markdown('<h2 class="section-header">⚡ HEAD-TO-HEAD QUICK STATS</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="🥅 Total Goals", 
            value="895", 
            delta="80 more",
            help="Ronaldo: 895 vs Messi: 815 career goals"
        )
        st.markdown('<p style="text-align: center; color: #FF6B6B; font-weight: bold;">🇵🇹 Ronaldo leads</p>', unsafe_allow_html=True)
    
    with col2:
        st.metric(
            label="🎯 Total Assists", 
            value="377", 
            delta="141 more",
            help="Messi: 377 vs Ronaldo: 236 career assists"
        )
        st.markdown('<p style="text-align: center; color: #4ECDC4; font-weight: bold;">🇦🇷 Messi leads</p>', unsafe_allow_html=True)
    
    with col3:
        st.metric(
            label="🏆 Ballon d'Or", 
            value="8", 
            delta="3 more",
            help="Messi: 8 vs Ronaldo: 5 Ballon d'Or awards"
        )
        st.markdown('<p style="text-align: center; color: #4ECDC4; font-weight: bold;">🇦🇷 Messi leads</p>', unsafe_allow_html=True)
    
    with col4:
        st.metric(
            label="🏅 Team Trophies", 
            value="44", 
            delta="9 more",
            help="Messi: 44 vs Ronaldo: 35 total team trophies"
        )
        st.markdown('<p style="text-align: center; color: #4ECDC4; font-weight: bold;">🇦🇷 Messi leads</p>', unsafe_allow_html=True)
    
    with col5:
        st.metric(
            label="⚽ Goals per 90min", 
            value="0.79", 
            delta="0.05 more",
            help="Messi: 0.79 vs Ronaldo: 0.74 goals per 90 minutes"
        )
        st.markdown('<p style="text-align: center; color: #4ECDC4; font-weight: bold;">🇦🇷 Messi leads</p>', unsafe_allow_html=True)
    
    # Enhanced Career Highlights
    st.markdown('<h2 class="section-header">🌟 CAREER HIGHLIGHTS & ACHIEVEMENTS</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(78, 205, 196, 0.1) 0%, rgba(68, 160, 141, 0.1) 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid #4ECDC4;
            margin-bottom: 1rem;
        ">
            <h3 style="color: #4ECDC4; margin-top: 0;">🇦🇷 Messi's Greatest Achievements</h3>
            <ul style="line-height: 1.8;">
                <li>🏆 <strong>World Cup Winner 2022</strong> - Completed football's holy grail</li>
                <li>🥇 <strong>Record 8 Ballon d'Or Awards</strong> - Most in history</li>
                <li>⚽ <strong>91 Goals in 2012</strong> - Unbreakable calendar year record</li>
                <li>🎯 <strong>Most Assists in History (377)</strong> - Ultimate playmaker</li>
                <li>🏟️ <strong>Barcelona Legend</strong> - 672 goals in 778 games</li>
                <li>📊 <strong>Most Goals + Assists (1,192)</strong> - Complete player</li>
                <li>🌟 <strong>4 Consecutive Ballon d'Or</strong> - 2009-2012 dominance</li>
                <li>🥇 <strong>World Cup Golden Ball (2)</strong> - 2014 & 2022</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(255, 107, 107, 0.1) 0%, rgba(196, 69, 105, 0.1) 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid #FF6B6B;
            margin-bottom: 1rem;
        ">
            <h3 style="color: #FF6B6B; margin-top: 0;">🇵🇹 Ronaldo's Greatest Achievements</h3>
            <ul style="line-height: 1.8;">
                <li>⚽ <strong>Most Goals in History (895+)</strong> - All-time top scorer</li>
                <li>🏆 <strong>5 Champions League Titles</strong> - Mr. Champions League</li>
                <li>🌍 <strong>Success in 4 Major Leagues</strong> - Premier, La Liga, Serie A, Saudi</li>
                <li>💪 <strong>Incredible Longevity</strong> - Elite performance at 40</li>
                <li>🎯 <strong>130+ International Goals</strong> - All-time international record</li>
                <li>👑 <strong>Euro 2016 Winner</strong> - Led Portugal to first major trophy</li>
                <li>🔥 <strong>7 CL Top Scorer Awards</strong> - Big game specialist</li>
                <li>🏃‍♂️ <strong>1,200+ Career Games</strong> - Ultimate professional</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced Career Statistics Visualization
    st.markdown('<h2 class="section-header">📊 COMPREHENSIVE CAREER STATISTICS</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals and Assists comparison
        fig = go.Figure()
        categories = ['Career Goals', 'Career Assists', 'Total G+A', 'Goals per 90min', 'Assists per 90min']
        messi_values = [815, 377, 1192, 0.79, 0.33]
        ronaldo_values = [895, 236, 1131, 0.74, 0.20]
        
        fig.add_trace(go.Bar(
            name='Messi',
            x=categories,
            y=messi_values,
            marker_color='#4ECDC4',
            text=[f'{val}' for val in messi_values],
            textposition='auto',
            hovertemplate='<b>Messi</b><br>%{x}: %{y}<extra></extra>'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=categories,
            y=ronaldo_values,
            marker_color='#FF6B6B',
            text=[f'{val}' for val in ronaldo_values],
            textposition='auto',
            hovertemplate='<b>Ronaldo</b><br>%{x}: %{y}<extra></extra>'
        ))
        
        fig.update_layout(
            title="⚽ Goals & Assists Breakdown",
            barmode='group',
            height=450,
            template='plotly_white',
            showlegend=True,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Performance radar chart
        categories = ['Goal Scoring', 'Playmaking', 'Dribbling', 'Shot Power', 'Consistency', 'Big Game Performance']
        messi_values = [95, 100, 100, 85, 98, 92]
        ronaldo_values = [100, 75, 88, 100, 95, 100]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_values,
            theta=categories,
            fill='toself',
            name='Messi',
            fillcolor='rgba(78, 205, 196, 0.3)',
            line=dict(color='#4ECDC4', width=3)
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_values,
            theta=categories,
            fill='toself',
            name='Ronaldo',
            fillcolor='rgba(255, 107, 107, 0.3)',
            line=dict(color='#FF6B6B', width=3)
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    ticksuffix='%'
                )
            ),
            showlegend=True,
            title="🎯 Performance Attributes Radar",
            height=450
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Season Goals Timeline with Enhanced Features
    st.markdown('<h2 class="section-header">📈 GOALS BY SEASON TIMELINE (2005-2023)</h2>', unsafe_allow_html=True)
    
    # Enhanced season data
    years = list(range(2005, 2024))
    messi_goals = [6, 17, 16, 38, 47, 60, 73, 60, 41, 58, 54, 51, 45, 51, 36, 31, 38, 30, 21]
    ronaldo_goals = [9, 20, 42, 33, 40, 55, 60, 51, 61, 48, 44, 42, 37, 28, 31, 36, 29, 24, 14]
    
    fig = go.Figure()
    
    # Add Messi line
    fig.add_trace(go.Scatter(
        x=years,
        y=messi_goals,
        mode='lines+markers',
        name='Messi Goals',
        line=dict(color='#4ECDC4', width=4),
        marker=dict(size=10, line=dict(width=2, color='white')),
        hovertemplate='<b>Messi</b><br>Season: %{x}<br>Goals: %{y}<extra></extra>'
    ))
    
    # Add Ronaldo line
    fig.add_trace(go.Scatter(
        x=years,
        y=ronaldo_goals,
        mode='lines+markers',
        name='Ronaldo Goals',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=10, line=dict(width=2, color='white')),
        hovertemplate='<b>Ronaldo</b><br>Season: %{x}<br>Goals: %{y}<extra></extra>'
    ))
    
    # Add peak annotations
    fig.add_annotation(
        x=2012, y=73,
        text="🔥 Messi's Historic Peak<br>73 Goals (91 calendar year)",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#4ECDC4",
        arrowwidth=3,
        bgcolor="rgba(78, 205, 196, 0.8)",
        bordercolor="#4ECDC4",
        borderwidth=2,
        font=dict(color="white", size=12)
    )
    
    fig.add_annotation(
        x=2014, y=61,
        text="⚡ Ronaldo's Golden Era<br>61 Goals + CL Winner",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#FF6B6B",
        arrowwidth=3,
        bgcolor="rgba(255, 107, 107, 0.8)",
        bordercolor="#FF6B6B",
        borderwidth=2,
        font=dict(color="white", size=12)
    )
    
    # Add career phases
    fig.add_vrect(x0=2008, x1=2012, fillcolor="rgba(78, 205, 196, 0.1)", 
                  annotation_text="Messi Era 1", annotation_position="top left")
    fig.add_vrect(x0=2013, x1=2018, fillcolor="rgba(255, 107, 107, 0.1)", 
                  annotation_text="Ronaldo Peak", annotation_position="top right")
    
    fig.update_layout(
        title="⚽ Season Goals Timeline - The Evolution of Greatness",
        xaxis_title="Season",
        yaxis_title="Goals Scored",
        height=600,
        template='plotly_white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(x=0.02, y=0.98)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Trophy Comparison
    st.markdown('<h2 class="section-header">🏆 TROPHY CABINET COMPARISON</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Club trophies
        club_trophies = {
            'Trophy Type': ['League Titles', 'Champions League', 'Domestic Cups', 'Other Club Trophies'],
            'Messi': [12, 4, 7, 15],
            'Ronaldo': [7, 5, 4, 12]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=club_trophies['Trophy Type'],
            y=club_trophies['Messi'],
            marker_color='#4ECDC4',
            text=club_trophies['Messi'],
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=club_trophies['Trophy Type'],
            y=club_trophies['Ronaldo'],
            marker_color='#FF6B6B',
            text=club_trophies['Ronaldo'],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🏟️ Club Trophies",
            barmode='group',
            height=400,
            template='plotly_white',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # International achievements
        international_data = {
            'Category': ['World Cup', 'Continental Cup', 'Other International'],
            'Messi': [1, 1, 2],  # WC 2022, Copa 2021, Olympics + U20 WC
            'Ronaldo': [0, 2, 1]  # Euro 2016, Nations League 2019, Euro runner-up
        }
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=international_data['Category'],
            y=international_data['Messi'],
            marker_color='#4ECDC4',
            text=international_data['Messi'],
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=international_data['Category'],
            y=international_data['Ronaldo'],
            marker_color='#FF6B6B',
            text=international_data['Ronaldo'],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🌍 International Trophies",
            barmode='group',
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Individual awards pie chart
        individual_awards = {
            'Award': ['Ballon d\'Or', 'Golden Boot', 'FIFA Best', 'Other Major'],
            'Messi': [8, 6, 3, 15],
            'Ronaldo': [5, 4, 2, 12]
        }
        
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type':'pie'}, {'type':'pie'}]],
            subplot_titles=['🇦🇷 Messi Awards', '🇵🇹 Ronaldo Awards']
        )
        
        fig.add_trace(go.Pie(
            labels=individual_awards['Award'],
            values=individual_awards['Messi'],
            marker_colors=['#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'],
            hovertemplate='<b>%{label}</b><br>Awards: %{value}<extra></extra>'
        ), row=1, col=1)
        
        fig.add_trace(go.Pie(
            labels=individual_awards['Award'],
            values=individual_awards['Ronaldo'],
            marker_colors=['#FF6B6B', '#FF9999', '#FD79A8', '#FDCB6E'],
            hovertemplate='<b>%{label}</b><br>Awards: %{value}<extra></extra>'
        ), row=1, col=2)
        
        fig.update_layout(height=400, title_text="🏅 Individual Awards Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    # Enhanced Fun Facts Section
    st.markdown('<h2 class="section-header">🎯 MIND-BLOWING STATISTICS & RECORDS</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        ">
            <h3 style="margin-top: 0;">🔢 Combined Legacy</h3>
            <ul style="line-height: 1.6;">
                <li>• <strong>1,710+ goals</strong> scored together</li>
                <li>• <strong>613+ assists</strong> combined</li>
                <li>• <strong>13 Ballon d'Or</strong> awards</li>
                <li>• <strong>79+ trophies</strong> won</li>
                <li>• <strong>2,274+ matches</strong> played</li>
                <li>• <strong>€2+ billion</strong> combined value</li>
                <li>• <strong>15+ years</strong> of dominance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        ">
            <h3 style="margin-top: 0;">⚔️ El Clasico Battles</h3>
            <ul style="line-height: 1.6;">
                <li>• Faced each other <strong>36 times</strong></li>
                <li>• Messi: <strong>26 goals</strong> vs Real Madrid</li>
                <li>• Ronaldo: <strong>18 goals</strong> vs Barcelona</li>
                <li>• Created football's <strong>greatest rivalry</strong></li>
                <li>• Combined <strong>44 Clasico goals</strong></li>
                <li>• <strong>9 years</strong> of direct competition</li>
                <li>• Both scored in <strong>same Clasico</strong> 8 times</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        ">
            <h3 style="margin-top: 0;">🌟 Global Impact</h3>
            <ul style="line-height: 1.6;">
                <li>• Defined an entire <strong>generation</strong></li>
                <li>• <strong>1 billion+</strong> combined followers</li>
                <li>• Elevated each other's <strong>performance</strong></li>
                <li>• Made football more <strong>global</strong></li>
                <li>• Inspired <strong>millions</strong> of kids</li>
                <li>• <strong>$10+ billion</strong> economic impact</li>
                <li>• Transcended <strong>sport itself</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Age Analysis
    st.markdown('<h2 class="section-header">⏰ PERFORMANCE BY AGE ANALYSIS</h2>', unsafe_allow_html=True)
    
    # Create age performance data
    ages = list(range(18, 41))
    messi_goals_by_age = [6, 17, 16, 38, 47, 60, 73, 60, 41, 58, 54, 51, 45, 51, 36, 31, 38, 30, 21, 16, 11, 8, 3]
    ronaldo_goals_by_age = [5, 9, 20, 42, 33, 40, 55, 60, 51, 61, 48, 44, 42, 37, 28, 31, 36, 29, 24, 14, 8, 5, 2]
    
    # Pad lists to same length
    while len(messi_goals_by_age) < len(ages):
        messi_goals_by_age.append(0)
    while len(ronaldo_goals_by_age) < len(ages):
        ronaldo_goals_by_age.append(0)
    
    # Trim lists to same length as ages
    messi_goals_by_age = messi_goals_by_age[:len(ages)]
    ronaldo_goals_by_age = ronaldo_goals_by_age[:len(ages)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ages,
        y=messi_goals_by_age,
        mode='lines+markers',
        name='Messi',
        line=dict(color='#4ECDC4', width=3),
        fill='tonexty',
        fillcolor='rgba(78, 205, 196, 0.1)'
    ))
    fig.add_trace(go.Scatter(
        x=ages,
        y=ronaldo_goals_by_age,
        mode='lines+markers',
        name='Ronaldo',
        line=dict(color='#FF6B6B', width=3),
        fill='tozeroy',
        fillcolor='rgba(255, 107, 107, 0.1)'
    ))
    
    # Add career phase annotations
    fig.add_annotation(x=22, y=max(messi_goals_by_age), text="🌟 Peak Years", showarrow=False)
    fig.add_annotation(x=35, y=20, text="👑 Veteran Excellence", showarrow=False)
    
    fig.update_layout(
        title="⏰ Goals by Age - Longevity Analysis",
        xaxis_title="Age",
        yaxis_title="Goals per Season",
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Final Verdict Section
    st.markdown('<h2 class="section-header">🏁 THE GOAT DEBATE SUMMARY</h2>', unsafe_allow_html=True)
    
    # Create two columns for final comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(78, 205, 196, 0.15) 0%, rgba(68, 160, 141, 0.15) 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 3px solid #4ECDC4;
        ">
            <h3 style="color: #4ECDC4; text-align: center;">🇦🇷 THE CASE FOR MESSI</h3>
            <div style="text-align: center; margin: 1rem 0;">
                <div style="font-size: 3rem;">🐐</div>
                <h4>Natural Genius</h4>
            </div>
            <ul style="line-height: 1.8;">
                <li>✅ <strong>Record 8 Ballon d'Or</strong> awards</li>
                <li>✅ <strong>World Cup Winner</strong> - completed football</li>
                <li>✅ <strong>Most assists in history</strong></li>
                <li>✅ <strong>Higher goals per 90 minutes</strong></li>
                <li>✅ <strong>More team trophies</strong> (44 vs 35)</li>
                <li>✅ <strong>4 consecutive Ballon d'Or</strong></li>
                <li>✅ <strong>91 goals in calendar year</strong></li>
                <li>✅ <strong>More complete player</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(255, 107, 107, 0.15) 0%, rgba(196, 69, 105, 0.15) 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 3px solid #FF6B6B;
        ">
            <h3 style="color: #FF6B6B; text-align: center;">🇵🇹 THE CASE FOR RONALDO</h3>
            <div style="text-align: center; margin: 1rem 0;">
                <div style="font-size: 3rem;">🔥</div>
                <h4>Ultimate Professional</h4>
            </div>
            <ul style="line-height: 1.8;">
                <li>✅ <strong>Most goals in history</strong> (895+)</li>
                <li>✅ <strong>Success in 4 major leagues</strong></li>
                <li>✅ <strong>Incredible longevity</strong> - elite at 40</li>
                <li>✅ <strong>More Champions League</strong> titles (5 vs 4)</li>
                <li>✅ <strong>International top scorer</strong> (130+ goals)</li>
                <li>✅ <strong>7 CL top scorer awards</strong></li>
                <li>✅ <strong>Big game mentality</strong></li>
                <li>✅ <strong>Athletic perfection</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Final verdict with interactive elements
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    ">
        <h2 style="margin-top: 0; font-size: 2.5rem;">🏆 THE ETERNAL DEBATE</h2>
        <div style="font-size: 4rem; margin: 1rem 0;">🐐 vs 🔥</div>
        <p style="font-size: 1.3rem; margin-bottom: 2rem;">
            Two legends, two different styles, one incredible rivalry that elevated football to new heights.
            The debate isn't just about who's better - it's about celebrating two of the greatest athletes in human history.
        </p>
        <div style="display: flex; justify-content: space-around; margin-top: 2rem;">
            <div>
                <h4 style="margin: 0.5rem 0;">🎨 ARTISTIC GENIUS</h4>
                <p>Messi - The Magician</p>
            </div>
            <div style="font-size: 2rem;">⚔️</div>
            <div>
                <h4 style="margin: 0.5rem 0;">💪 ATHLETIC PERFECTION</h4>
                <p>Ronaldo - The Machine</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
    ---
    ### 🔍 Explore the Complete Analysis
    
    This overview just scratches the surface! Dive deeper into every aspect of this legendary rivalry:
    
    - **📊 Career Stats**: Detailed statistical breakdown and performance metrics
    - **🗺️ Heat Maps**: Advanced positioning and playing style analysis  
    - **🏅 Individual Awards**: Complete honors and recognition comparison
    - **🏁 Final Verdict**: Our comprehensive GOAT analysis with data-driven conclusions
    
    **Each page reveals new insights into what makes these players extraordinary.** 
    
    🎯 **Ready to explore every angle of the greatest debate in sports history?**
    """)
    
    # Add some fun interactive elements
    st.markdown('<h3 class="section-header">🎮 Quick GOAT Poll</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        goat_choice = st.radio(
            "Who do you think is the GOAT?",
            ["🇦🇷 Messi - The Magician", "🇵🇹 Ronaldo - The Machine", "🤝 Both are GOATs"],
            key="goat_poll"
        )
        
        if goat_choice:
            if "Messi" in goat_choice:
                st.success("🇦🇷 Team Messi! You appreciate pure footballing artistry and natural genius!")
            elif "Ronaldo" in goat_choice:
                st.success("🇵🇹 Team Ronaldo! You value dedication, athleticism, and goal-scoring prowess!")
            else:
                st.info("🤝 Diplomatic choice! Both players have indeed redefined greatness in their own unique ways!")

if __name__ == "__main__":
    show()