import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the physical attributes analysis page"""
    st.markdown('<h1 class="section-header">💪 PHYSICAL ATTRIBUTES & ATHLETICISM</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    physical_data = data['physical']
    
    # Page introduction
    st.markdown("""
    **Physical prowess in football comes in many forms.** From explosive speed to aerial dominance, from agility to 
    stamina - Messi and Ronaldo represent two completely different physical archetypes that have both achieved 
    incredible success. Let's analyze their athletic capabilities, injury records, longevity, and how they've 
    maintained peak physical condition throughout their careers.
    """)
    
    # Physical profile comparison
    st.markdown('<h3 class="section-header">🏃‍♂️ Physical Profile Comparison</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card">
            <h3>🇦🇷 MESSI'S PHYSICAL PROFILE</h3>
            <h4>📏 Basic Measurements</h4>
            <p><strong>Height:</strong> 5'7" (170 cm)</p>
            <p><strong>Weight:</strong> 159 lbs (72 kg)</p>
            <p><strong>Body Type:</strong> Compact & Agile</p>
            <p><strong>Dominant Foot:</strong> Left (99%)</p>
            
            <h4>⚡ Athletic Attributes</h4>
            <p><strong>Top Speed:</strong> 32.5 km/h</p>
            <p><strong>Acceleration:</strong> Explosive (0-30m)</p>
            <p><strong>Agility:</strong> Elite level</p>
            <p><strong>Balance:</strong> Exceptional</p>
            <p><strong>Core Strength:</strong> Outstanding</p>
            
            <h4>🎯 Key Strengths</h4>
            <p>• Low center of gravity</p>
            <p>• Superior balance & coordination</p>
            <p>• Quick change of direction</p>
            <p>• Resistance to tackles</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card">
            <h3>🇵🇹 RONALDO'S PHYSICAL PROFILE</h3>
            <h4>📏 Basic Measurements</h4>
            <p><strong>Height:</strong> 6'2" (187 cm)</p>
            <p><strong>Weight:</strong> 183 lbs (83 kg)</p>
            <p><strong>Body Type:</strong> Athletic & Powerful</p>
            <p><strong>Dominant Foot:</strong> Right (85%)</p>
            
            <h4>⚡ Athletic Attributes</h4>
            <p><strong>Top Speed:</strong> 34.6 km/h</p>
            <p><strong>Vertical Jump:</strong> 78 cm (30.7 inches)</p>
            <p><strong>Power:</strong> Elite level</p>
            <p><strong>Stamina:</strong> Exceptional</p>
            <p><strong>Aerial Ability:</strong> Outstanding</p>
            
            <h4>🎯 Key Strengths</h4>
            <p>• Superior height & reach</p>
            <p>• Incredible jumping ability</p>
            <p>• Raw speed & power</p>
            <p>• Physical intimidation</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Physical attributes radar
    st.markdown('<h3 class="section-header">📊 Physical Attributes Radar</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Overall physical radar
        categories = ['Speed', 'Strength', 'Agility', 'Stamina', 'Jumping', 'Balance']
        messi_values = [85, 75, 99, 88, 70, 99]
        ronaldo_values = [95, 95, 85, 92, 99, 82]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_values,
            theta=categories,
            fill='toself',
            name='Messi',
            fillcolor='rgba(78, 205, 196, 0.3)',
            line_color='#4ECDC4'
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_values,
            theta=categories,
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
            title="⚡ Physical Attributes Radar",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Athletic performance metrics
        metrics_data = {
            'Metric': ['Top Speed (km/h)', 'Strength Score', 'Agility Score', 'Stamina Score', 'Jump Height (cm)', 'Body Fat %'],
            'Messi': [32.5, 75, 99, 88, 40, 7.5],
            'Ronaldo': [34.6, 95, 85, 92, 78, 7.0],
            'Winner': ['🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇦🇷 Messi', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo']
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        st.dataframe(metrics_df, use_container_width=True, height=250)
        
        # Physical advantages
        st.markdown("""
        ### 🏆 Physical Advantages:
        
        **🇦🇷 Messi leads in:**
        - Agility & Balance (99/100)
        - Change of direction speed
        - Low center of gravity benefits
        - Resistance to physical challenges
        
        **🇵🇹 Ronaldo leads in:**
        - Top speed (34.6 vs 32.5 km/h)
        - Strength & Power (95/100)
        - Jumping ability (78cm vertical)
        - Overall athleticism
        """)
    
    # Speed and acceleration analysis
    st.markdown('<h3 class="section-header">🏃‍♂️ Speed & Acceleration Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Speed over distance
        distances = ['0-10m', '0-20m', '0-30m', 'Top Speed']
        messi_times = [1.8, 2.9, 4.1, 32.5]  # Times in seconds, top speed in km/h
        ronaldo_times = [1.9, 3.0, 4.0, 34.6]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=distances[:-1],
            y=messi_times[:-1],
            marker_color='#4ECDC4',
            text=messi_times[:-1],
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=distances[:-1],
            y=ronaldo_times[:-1],
            marker_color='#FF6B6B',
            text=ronaldo_times[:-1],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🏃‍♂️ Acceleration Times (seconds)",
            yaxis_title="Time (seconds)",
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Top speed comparison
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode = "gauge+number",
            value = 32.5,
            domain = {'x': [0, 0.48], 'y': [0.5, 1]},
            title = {'text': "Messi Top Speed"},
            gauge = {'axis': {'range': [None, 40]},
                     'bar': {'color': "#4ECDC4"},
                     'steps' : [{'range': [0, 25], 'color': "lightgray"},
                                {'range': [25, 35], 'color': "gray"}],
                     'threshold' : {'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75, 'value': 35}}))
        
        fig.add_trace(go.Indicator(
            mode = "gauge+number",
            value = 34.6,
            domain = {'x': [0.52, 1], 'y': [0.5, 1]},
            title = {'text': "Ronaldo Top Speed"},
            gauge = {'axis': {'range': [None, 40]},
                     'bar': {'color': "#FF6B6B"},
                     'steps' : [{'range': [0, 25], 'color': "lightgray"},
                                {'range': [25, 35], 'color': "gray"}],
                     'threshold' : {'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75, 'value': 35}}))
        
        # Add acceleration comparison
        fig.add_trace(go.Bar(
            name='Messi 0-30m',
            x=['Acceleration'],
            y=[4.1],
            marker_color='#4ECDC4',
            text=['4.1s'],
            textposition='auto',
            yaxis='y2',
            offsetgroup=1
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo 0-30m',
            x=['Acceleration'],
            y=[4.0],
            marker_color='#FF6B6B',
            text=['4.0s'],
            textposition='auto',
            yaxis='y2',
            offsetgroup=2
        ))
        
        fig.update_layout(
            height=400,
            title="⚡ Speed Comparison (km/h)",
            yaxis2=dict(title="0-30m Time (s)", overlaying="y", side="right", range=[3.5, 4.5])
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Strength and power analysis
    st.markdown('<h3 class="section-header">💪 Strength & Power Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏋️‍♂️ Raw Strength</h4>
            <p><strong>🇵🇹 Ronaldo: 95/100</strong></p>
            <p>• Bench Press: ~180 kg (396 lbs)</p>
            <p>• Squat: ~200 kg (440 lbs)</p>
            <p>• Upper body dominance</p>
            <p>• Physical intimidation factor</p>
            <hr>
            <p><strong>🇦🇷 Messi: 75/100</strong></p>
            <p>• Functional strength focus</p>
            <p>• Core strength emphasis</p>
            <p>• Lower body power</p>
            <p>• Relative strength high</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>🦘 Jumping Ability</h4>
            <p><strong>🇵🇹 Ronaldo: 99/100</strong></p>
            <p>• Vertical jump: 78 cm (30.7")</p>
            <p>• Highest header: 2.93m</p>
            <p>• Air time: 0.7 seconds</p>
            <p>• Heading accuracy: Elite</p>
            <hr>
            <p><strong>🇦🇷 Messi: 70/100</strong></p>
            <p>• Vertical jump: 40 cm (15.7")</p>
            <p>• Compensates with timing</p>
            <p>• Rarely wins aerial duels</p>
            <p>• Ground-based approach</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>⚖️ Balance & Coordination</h4>
            <p><strong>🇦🇷 Messi: 99/100</strong></p>
            <p>• Exceptional body control</p>
            <p>• Low center of gravity</p>
            <p>• Rarely loses balance</p>
            <p>• Superior coordination</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo: 82/100</strong></p>
            <p>• Good for his height</p>
            <p>• Improved over time</p>
            <p>• Occasional imbalance</p>
            <p>• Height disadvantage</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Injury record and longevity
    st.markdown('<h3 class="section-header">🏥 Injury Record & Longevity</h3>', unsafe_allow_html=True)
    
    # Create injury data
    injury_data = {
        'Category': ['Games Missed (Injury)', 'Serious Injuries', 'Muscle Injuries', 'Average Days Out', 'Games per Season', 'Injury-Free Seasons'],
        'Messi': [85, 3, 12, 18, 47, 8],
        'Ronaldo': [45, 2, 8, 12, 52, 12],
        'Advantage': ['🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo']
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Injury comparison chart
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=['Games Missed', 'Serious Injuries', 'Muscle Injuries'],
            y=[85, 3, 12],
            marker_color='#4ECDC4',
            text=[85, 3, 12],
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=['Games Missed', 'Serious Injuries', 'Muscle Injuries'],
            y=[45, 2, 8],
            marker_color='#FF6B6B',
            text=[45, 2, 8],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="🏥 Career Injury Comparison",
            barmode='group',
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Availability percentage by age
        ages = list(range(20, 40))
        messi_availability = [95, 92, 88, 85, 90, 88, 85, 82, 90, 88, 85, 80, 75, 85, 90, 88, 85, 80, 75, 70]
        ronaldo_availability = [98, 95, 92, 95, 98, 95, 98, 95, 92, 95, 98, 95, 92, 88, 90, 88, 85, 82, 80, 85]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=ages,
            y=messi_availability,
            mode='lines+markers',
            name='Messi Availability %',
            line=dict(color='#4ECDC4', width=3),
            marker=dict(size=6)
        ))
        fig.add_trace(go.Scatter(
            x=ages,
            y=ronaldo_availability,
            mode='lines+markers',
            name='Ronaldo Availability %',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=6)
        ))
        
        fig.update_layout(
            title="📈 Availability % by Age",
            xaxis_title="Age",
            yaxis_title="Availability %",
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    injury_df = pd.DataFrame(injury_data)
    st.dataframe(injury_df, use_container_width=True)
    
    # Fitness and conditioning
    st.markdown('<h3 class="section-header">🔋 Fitness & Conditioning</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Fitness Approach:
        
        **🍎 Nutrition Revolution (2014):**
        - Worked with nutritionist Giuliano Poser
        - Eliminated refined sugar and flour
        - Focus on lean proteins and vegetables
        - Dramatic improvement in stamina
        
        **🏋️‍♂️ Training Philosophy:**
        - Functional movement focus
        - Core strength emphasis
        - Agility and balance work
        - Technical skill integration
        
        **📊 Physical Evolution:**
        - Started career with frequent injuries
        - Major fitness overhaul at age 27
        - Peak physical years: 2015-2019
        - Adapted training for longevity
        
        **🎯 Key Improvements:**
        - Reduced muscle injuries by 70%
        - Increased games per season
        - Enhanced late-career stamina
        - Better injury prevention
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Fitness Obsession:
        
        **🤖 Athletic Perfectionism:**
        - Body fat: 7% (elite athlete level)
        - Muscle mass: Optimized throughout career
        - VO2 Max: Elite endurance levels
        - Recovery protocols: Industry-leading
        
        **🏋️‍♂️ Training Regime:**
        - 3-4 hours daily training
        - Strength, cardio, flexibility
        - Cold therapy and recovery
        - Strict diet and sleep schedule
        
        **📊 Physical Maintenance:**
        - Biological age: 10 years younger
        - Consistent body composition
        - Elite physical metrics at 39
        - Professional attitude to fitness
        
        **🎯 Longevity Secrets:**
        - Obsessive attention to detail
        - Constant physical monitoring
        - Adaptation of training methods
        - Mental discipline in lifestyle
        """)
    
    # Physical evolution over career
    st.markdown('<h3 class="section-header">📈 Physical Evolution Over Career</h3>', unsafe_allow_html=True)
    
    # Physical attributes over time
    career_years = ['Early Career', 'Peak Years', 'Late Career', 'Current']
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('💨 Speed Evolution', '💪 Strength Evolution', '🏃‍♂️ Stamina Evolution', '🤸‍♂️ Agility Evolution'),
        specs=[[{"type": "scatter"}, {"type": "scatter"}],
               [{"type": "scatter"}, {"type": "scatter"}]]
    )
    
    # Speed evolution
    messi_speed = [90, 95, 85, 75]
    ronaldo_speed = [85, 100, 90, 80]
    fig.add_trace(go.Scatter(x=career_years, y=messi_speed, name='Messi Speed', line_color='#4ECDC4'), row=1, col=1)
    fig.add_trace(go.Scatter(x=career_years, y=ronaldo_speed, name='Ronaldo Speed', line_color='#FF6B6B'), row=1, col=1)
    
    # Strength evolution
    messi_strength = [70, 80, 85, 75]
    ronaldo_strength = [80, 95, 100, 90]
    fig.add_trace(go.Scatter(x=career_years, y=messi_strength, name='Messi Strength', line_color='#4ECDC4', showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=career_years, y=ronaldo_strength, name='Ronaldo Strength', line_color='#FF6B6B', showlegend=False), row=1, col=2)
    
    # Stamina evolution
    messi_stamina = [75, 85, 95, 85]
    ronaldo_stamina = [90, 95, 98, 92]
    fig.add_trace(go.Scatter(x=career_years, y=messi_stamina, name='Messi Stamina', line_color='#4ECDC4', showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=career_years, y=ronaldo_stamina, name='Ronaldo Stamina', line_color='#FF6B6B', showlegend=False), row=2, col=1)
    
    # Agility evolution
    messi_agility = [95, 100, 95, 88]
    ronaldo_agility = [90, 95, 85, 75]
    fig.add_trace(go.Scatter(x=career_years, y=messi_agility, name='Messi Agility', line_color='#4ECDC4', showlegend=False), row=2, col=2)
    fig.add_trace(go.Scatter(x=career_years, y=ronaldo_agility, name='Ronaldo Agility', line_color='#FF6B6B', showlegend=False), row=2, col=2)
    
    fig.update_layout(height=600, title_text="📊 Physical Attributes Evolution")
    st.plotly_chart(fig, use_container_width=True)
    
    # Final physical verdict
    st.markdown('<h3 class="section-header">🏁 Physical Attributes Verdict</h3>', unsafe_allow_html=True)
    
    # Calculate physical scores
    ronaldo_physical_score = 95 + 95 + 99 + 92  # Speed, Strength, Jumping, Stamina
    messi_physical_score = 85 + 75 + 70 + 88 + 99 + 99  # Speed, Strength, Jumping, Stamina, Agility, Balance
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>💪 Physical Attributes Champion</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO: The Athletic Specimen</h3>
                <p>✅ Superior top speed (34.6 vs 32.5 km/h)</p>
                <p>✅ Elite strength & power (95/100)</p>
                <p>✅ Incredible jumping ability (78cm)</p>
                <p>✅ Better injury record (45 vs 85 games missed)</p>
                <p>✅ Superior longevity & availability</p>
                <p>✅ Physical intimidation factor</p>
            </div>
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI: The Agility Master</h3>
                <p>✅ Superior agility & balance (99/100)</p>
                <p>✅ Better acceleration (0-30m)</p>
                <p>✅ Exceptional body control</p>
                <p>✅ Low center of gravity advantage</p>
                <p>✅ Resistance to physical challenges</p>
                <p>✅ Functional strength for his style</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Physical Winner:</strong> 🇵🇹 <strong>RONALDO</strong> - The ultimate athletic specimen!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final analysis
    st.markdown("""
    ---
    ### 🌟 Physical Legacy Analysis
    
    **🇵🇹 Ronaldo represents the pinnacle of athletic achievement** in football. His combination of size, speed, strength, 
    and jumping ability is unmatched. His obsessive attention to fitness and conditioning has allowed him to maintain 
    elite physical performance well into his late 30s. His injury record and availability are simply exceptional.
    
    **🇦🇷 Messi showcases how technique can triumph over pure athleticism.** His incredible agility, balance, and 
    coordination have made him unstoppable despite lacking traditional physical advantages. His fitness transformation 
    in 2014 extended his career and improved his late-game impact significantly.
    
    **🏆 The Verdict:** While both players represent physical excellence in different ways, Ronaldo's superior 
    athletic metrics, injury record, and longevity give him the edge in pure physical attributes. However, Messi 
    proves that football intelligence and technical perfection can overcome physical limitations.
    
    **🤝 Combined Impact:** Together, they've shown that there are multiple paths to physical excellence in football - 
    Ronaldo through raw athleticism and Messi through optimized agility and intelligence.
    """)

if __name__ == "__main__":
    show()