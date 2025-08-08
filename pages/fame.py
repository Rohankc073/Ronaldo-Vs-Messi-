import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from utils.data_loader import load_all_data

def show():
    """Display the fame and global impact analysis page"""
    st.markdown('<h1 class="section-header">📱 FAME & GLOBAL IMPACT</h1>', unsafe_allow_html=True)
    
    # Load data
    data = load_all_data()
    fame_data = data['fame']
    
    # Page introduction
    st.markdown("""
    **Beyond football, Messi and Ronaldo are global superstars.** Their influence extends far beyond the pitch, 
    reaching billions through social media, sponsorships, and cultural impact. They've transcended sport to become 
    household names worldwide. Let's analyze their fame, brand value, social media dominance, and global reach.
    """)
    
    # Social media overview
    st.markdown('<h3 class="section-header">📱 Social Media Empire</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Instagram", "615M", "115M more")
        st.caption("🇵🇹 Ronaldo dominates")
        st.write("**Ronaldo:** Most followed person")
        st.write("**Messi:** 500M+ followers")
    
    with col2:
        st.metric("Facebook", "170M", "55M more")
        st.caption("🇵🇹 Ronaldo leads")
        st.write("**Ronaldo:** 170M likes")
        st.write("**Messi:** 115M likes")
    
    with col3:
        st.metric("Twitter/X", "110M", "64M more")
        st.caption("🇵🇹 Ronaldo ahead")
        st.write("**Ronaldo:** 110M followers")
        st.write("**Messi:** 46M followers")
    
    with col4:
        st.metric("YouTube", "55M", "52.5M more")
        st.caption("🇵🇹 Ronaldo massive lead")
        st.write("**Ronaldo:** Own channel success")
        st.write("**Messi:** 2.5M subscribers")
    
    with col5:
        st.metric("Total Followers", "950M", "235M more")
        st.caption("🇵🇹 Ronaldo's social empire")
        st.write("**Combined:** 1.66B followers")
        st.write("**Overlap:** ~300M estimated")
    
    # Social media platform breakdown
    st.markdown('<h3 class="section-header">📊 Social Media Platform Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Social media followers comparison
        platforms = ['Instagram', 'Facebook', 'Twitter/X', 'YouTube', 'TikTok']
        messi_followers = [500, 115, 46, 2.5, 35]  # in millions
        ronaldo_followers = [615, 170, 110, 55, 45]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Messi',
            x=platforms,
            y=messi_followers,
            marker_color='#4ECDC4',
            text=[f"{x}M" for x in messi_followers],
            textposition='auto'
        ))
        fig.add_trace(go.Bar(
            name='Ronaldo',
            x=platforms,
            y=ronaldo_followers,
            marker_color='#FF6B6B',
            text=[f"{x}M" for x in ronaldo_followers],
            textposition='auto'
        ))
        
        fig.update_layout(
            title="📱 Social Media Followers (Millions)",
            barmode='group',
            height=400,
            template='plotly_white',
            yaxis_title="Followers (Millions)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Engagement rates and platform dominance
        engagement_data = {
            'Platform': ['Instagram', 'Facebook', 'Twitter', 'YouTube', 'Overall'],
            'Messi Engagement %': [3.2, 2.8, 4.1, 8.5, 3.5],
            'Ronaldo Engagement %': [2.8, 2.4, 3.2, 12.2, 3.8],
            'Messi Reach': ['High', 'Medium', 'High', 'Low', 'High'],
            'Ronaldo Reach': ['Massive', 'High', 'High', 'Medium', 'Massive']
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=engagement_data['Platform'],
            y=engagement_data['Messi Engagement %'],
            mode='lines+markers',
            name='Messi Engagement %',
            line=dict(color='#4ECDC4', width=3),
            marker=dict(size=10)
        ))
        fig.add_trace(go.Scatter(
            x=engagement_data['Platform'],
            y=engagement_data['Ronaldo Engagement %'],
            mode='lines+markers',
            name='Ronaldo Engagement %',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="📈 Engagement Rates by Platform",
            yaxis_title="Engagement Rate (%)",
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        engagement_df = pd.DataFrame(engagement_data)
        st.dataframe(engagement_df, use_container_width=True)
    
    # Brand value and commercial impact
    st.markdown('<h3 class="section-header">💰 Brand Value & Commercial Impact</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="player-card messi-card">
            <h3>🇦🇷 MESSI'S BRAND EMPIRE</h3>
            <h4>💰 Financial Portfolio</h4>
            <p><strong>Annual Earnings:</strong> $130M (2023)</p>
            <p><strong>Lifetime Adidas Deal:</strong> $1B+</p>
            <p><strong>PSG Salary:</strong> €30M + bonuses</p>
            <p><strong>Miami Deal:</strong> $50-60M/year</p>
            
            <h4>🤝 Major Sponsorships</h4>
            <p>• Adidas (Lifetime partner)</p>
            <p>• Apple TV+ (MLS partnership)</p>
            <p>• Mastercard (Global ambassador)</p>
            <p>• Pepsi (Long-term partner)</p>
            <p>• Budweiser (World Cup campaigns)</p>
            
            <h4>📊 Brand Metrics</h4>
            <p><strong>Brand Value:</strong> $600M+</p>
            <p><strong>Search Volume:</strong> 45M monthly</p>
            <p><strong>Merchandise Sales:</strong> $125M</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="player-card ronaldo-card">
            <h3>🇵🇹 RONALDO'S BRAND EMPIRE</h3>
            <h4>💰 Financial Portfolio</h4>
            <p><strong>Annual Earnings:</strong> $136M (2023)</p>
            <p><strong>Lifetime Nike Deal:</strong> $1B+</p>
            <p><strong>Al Nassr Salary:</strong> €200M/year</p>
            <p><strong>Business Ventures:</strong> Multiple investments</p>
            
            <h4>🤝 Major Sponsorships</h4>
            <p>• Nike (Lifetime partner)</p>
            <p>• Clear Shampoo (Global face)</p>
            <p>• Herbalife (Nutrition partner)</p>
            <p>• Tag Heuer (Luxury watches)</p>
            <p>• Coca-Cola (Long-term deals)</p>
            
            <h4>📊 Brand Metrics</h4>
            <p><strong>Brand Value:</strong> $700M+</p>
            <p><strong>Search Volume:</strong> 67M monthly</p>
            <p><strong>Merchandise Sales:</strong> $185M</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Global search trends and popularity
    st.markdown('<h3 class="section-header">🌍 Global Search Trends & Popularity</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Google search volume by region
        regions = ['Europe', 'South America', 'North America', 'Asia', 'Africa', 'Oceania']
        messi_search = [85, 95, 70, 60, 75, 80]
        ronaldo_search = [90, 80, 85, 95, 90, 85]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=messi_search,
            theta=regions,
            fill='toself',
            name='Messi Popularity',
            fillcolor='rgba(78, 205, 196, 0.3)',
            line_color='#4ECDC4'
        ))
        fig.add_trace(go.Scatterpolar(
            r=ronaldo_search,
            theta=regions,
            fill='toself',
            name='Ronaldo Popularity',
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
            title="🌍 Global Popularity by Region",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Search trends over time (2019-2024)
        years = ['2019', '2020', '2021', '2022', '2023', '2024']
        messi_trends = [75, 70, 80, 95, 90, 85]  # 2022 World Cup spike
        ronaldo_trends = [85, 80, 75, 70, 75, 70]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=messi_trends,
            mode='lines+markers',
            name='Messi Search Interest',
            line=dict(color='#4ECDC4', width=4),
            marker=dict(size=10)
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=ronaldo_trends,
            mode='lines+markers',
            name='Ronaldo Search Interest',
            line=dict(color='#FF6B6B', width=4),
            marker=dict(size=10)
        ))
        
        # Add World Cup annotation
        fig.add_annotation(
            x='2022', y=95,
            text="World Cup 2022<br>Messi Peak",
            showarrow=True,
            arrowcolor="#4ECDC4",
            arrowwidth=2
        )
        
        fig.update_layout(
            title="📈 Global Search Trends (2019-2024)",
            xaxis_title="Year",
            yaxis_title="Search Interest Index",
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Cultural impact and influence
    st.markdown('<h3 class="section-header">🎭 Cultural Impact & Influence</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="comparison-card">
            <h4>🎬 Media & Entertainment</h4>
            <p><strong>🇦🇷 Messi:</strong></p>
            <p>• Netflix documentary series</p>
            <p>• Apple TV+ partnership</p>
            <p>• Multiple biographical films</p>
            <p>• Children's book character</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo:</strong></p>
            <p>• Netflix documentary series</p>
            <p>• Multiple reality shows</p>
            <p>• Autobiography bestseller</p>
            <p>• Fashion and lifestyle content</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-card">
            <h4>🏛️ Cultural Recognition</h4>
            <p><strong>🇦🇷 Messi:</strong></p>
            <p>• Argentine national hero</p>
            <p>• Barcelona city icon</p>
            <p>• UNESCO Goodwill Ambassador</p>
            <p>• Time 100 Most Influential</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo:</strong></p>
            <p>• Portuguese national symbol</p>
            <p>• Madeira airport renamed after him</p>
            <p>• Museum dedicated to his career</p>
            <p>• Order of Merit recipient</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="comparison-card">
            <h4>🌟 Global Influence</h4>
            <p><strong>🇦🇷 Messi:</strong></p>
            <p>• MLS transformation impact</p>
            <p>• Youth football inspiration</p>
            <p>• Humble icon representation</p>
            <p>• Technical excellence symbol</p>
            <hr>
            <p><strong>🇵🇹 Ronaldo:</strong></p>
            <p>• Fitness and dedication icon</p>
            <p>• Business empire inspiration</p>
            <p>• Saudi Arabia ambassador</p>
            <p>• Athletic perfection symbol</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Business ventures and investments
    st.markdown('<h3 class="section-header">🏢 Business Ventures & Investments</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Messi's business portfolio
        st.markdown("""
        ### 🇦🇷 Messi's Business Portfolio:
        
        **🏢 Major Investments:**
        - Play Time (Sports tech startup)
        - Kin + Carta (Digital transformation)
        - Davis Cup (Tennis investment)
        - Real estate investments
        
        **👕 Fashion & Lifestyle:**
        - The Messi Store (Official merchandise)
        - Adidas Messi collection
        - Limited edition collaborations
        - Luxury watch partnerships
        
        **🍽️ Hospitality:**
        - Hincha restaurant chain
        - Food and beverage investments
        - Hospitality ventures in Miami
        
        **📚 Media & Content:**
        - Production company interests
        - Documentary projects
        - Educational content initiatives
        """)
    
    with col2:
        # Ronaldo's business empire
        st.markdown("""
        ### 🇵🇹 Ronaldo's Business Empire:
        
        **🏢 Major Ventures:**
        - CR7 brand empire (fashion, fragrance)
        - Pestana CR7 hotel chain (7 locations)
        - Hair transplant clinics
        - Fitness center investments
        
        **👕 Fashion & Lifestyle:**
        - CR7 underwear line
        - CR7 footwear collection
        - CR7 fragrances
        - Luxury lifestyle products
        
        **🍽️ Hospitality:**
        - Pestana CR7 hotels (Lisbon, Madrid, NY)
        - Restaurant investments
        - Luxury hospitality ventures
        
        **📱 Digital & Tech:**
        - Social media empire monetization
        - NFT and digital collectibles
        - E-commerce platforms
        """)
    
    # Fame metrics comparison
    st.markdown('<h3 class="section-header">📊 Fame Metrics Comparison</h3>', unsafe_allow_html=True)
    
    fame_metrics = {
        'Metric': [
            'Social Media Followers (Total)', 'Google Search Volume (Monthly)', 'Brand Value (USD)', 
            'Annual Earnings (USD)', 'Merchandise Sales (USD)', 'Global Fan Base (Millions)',
            'Sponsorship Income (USD)', 'Media Mentions (Daily)', 'Influence Rank (Global)',
            'Cultural Impact Score', 'Business Ventures', 'Documentary Features'
        ],
        'Messi': [
            '715M', '45M', '$600M', '$130M', '$125M', '450M',
            '$55M', '15K', '2.1', '95/100', '8', '12'
        ],
        'Ronaldo': [
            '950M', '67M', '$700M', '$136M', '$185M', '520M',
            '$70M', '18K', '1.8', '92/100', '15', '18'
        ],
        'Winner': [
            '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo',
            '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo', '🇦🇷 Messi', '🇵🇹 Ronaldo', '🇵🇹 Ronaldo'
        ]
    }
    
    fame_df = pd.DataFrame(fame_metrics)
    st.dataframe(fame_df, use_container_width=True, height=450)
    
    # Social media growth over time
    st.markdown('<h3 class="section-header">📈 Social Media Growth Timeline</h3>', unsafe_allow_html=True)
    
    # Social media growth data (2015-2024)
    social_years = list(range(2015, 2025))
    messi_ig_growth = [50, 75, 100, 130, 165, 200, 250, 350, 450, 500]  # Instagram millions
    ronaldo_ig_growth = [45, 80, 120, 150, 200, 280, 350, 450, 550, 615]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=social_years,
        y=messi_ig_growth,
        mode='lines+markers',
        name='Messi Instagram',
        line=dict(color='#4ECDC4', width=4),
        marker=dict(size=8)
    ))
    fig.add_trace(go.Scatter(
        x=social_years,
        y=ronaldo_ig_growth,
        mode='lines+markers',
        name='Ronaldo Instagram',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=8)
    ))
    
    # Add milestone annotations
    fig.add_annotation(x=2018, y=150, text="Ronaldo becomes<br>most followed athlete", arrowcolor="#FF6B6B")
    fig.add_annotation(x=2022, y=450, text="Messi World Cup<br>boost", arrowcolor="#4ECDC4")
    fig.add_annotation(x=2024, y=615, text="Ronaldo: Most followed<br>person on Instagram", arrowcolor="#FF6B6B")
    
    fig.update_layout(
        title="📱 Instagram Followers Growth (2015-2024)",
        xaxis_title="Year",
        yaxis_title="Followers (Millions)",
        height=500,
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Most viral moments
    st.markdown('<h3 class="section-header">🔥 Most Viral Moments & Posts</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Most Viral Moments:
        
        **📱 Social Media Records:**
        1. **World Cup Trophy Post (2022)**
           - 75M+ likes on Instagram
           - Most-liked sports post ever
           - 20M+ shares across platforms
        
        2. **Miami Debut Announcement**
           - 50M+ likes in 24 hours
           - MLS follower surge
           - Global news coverage
        
        3. **Ballon d'Or #8 Post**
           - 40M+ likes
           - Record-breaking engagement
           - Viral celebration videos
        
        4. **Family Moments**
           - Wife and kids posts
           - 20-30M regular likes
           - Authentic content appreciation
        
        **🎯 Viral Impact:**
        - Consistent 15-25M likes per post
        - High engagement rates
        - Authentic content strategy
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Most Viral Moments:
        
        **📱 Social Media Records:**
        1. **Return to Manchester United**
           - 60M+ likes across platforms
           - Transfer announcement viral
           - Global trending topic
        
        2. **Al Nassr Signing**
           - 45M+ likes
           - Saudi football spotlight
           - Massive Middle East engagement
        
        3. **Euro 2016 Celebration**
           - 35M+ likes
           - Emotional victory moment
           - Portuguese pride viral
        
        4. **Training & Lifestyle Content**
           - Consistent 8-15M likes
           - Fitness inspiration posts
           - Luxury lifestyle content
        
        **🎯 Viral Impact:**
        - Highest follower count globally
        - Consistent content output
        - Lifestyle brand integration
        """)
    
    # Fame evolution by career phase
    st.markdown('<h3 class="section-header">📊 Fame Evolution by Career Phase</h3>', unsafe_allow_html=True)
    
    career_phases = ['Early Career\n(2003-2008)', 'Rise to Fame\n(2009-2012)', 'Peak Rivalry\n(2013-2018)', 'Legacy Phase\n(2019-2024)']
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('📱 Social Media Following', '💰 Brand Value Growth', '🌍 Global Recognition', '📺 Media Coverage'),
        specs=[[{"type": "scatter"}, {"type": "scatter"}],
               [{"type": "scatter"}, {"type": "scatter"}]]
    )
    
    # Social media following
    messi_social = [0, 20, 60, 90]
    ronaldo_social = [0, 25, 70, 95]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_social, name='Messi Social', line_color='#4ECDC4'), row=1, col=1)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_social, name='Ronaldo Social', line_color='#FF6B6B'), row=1, col=1)
    
    # Brand value
    messi_brand = [10, 40, 80, 95]
    ronaldo_brand = [15, 50, 90, 100]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_brand, name='Messi Brand', line_color='#4ECDC4', showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_brand, name='Ronaldo Brand', line_color='#FF6B6B', showlegend=False), row=1, col=2)
    
    # Global recognition
    messi_recognition = [30, 70, 95, 100]
    ronaldo_recognition = [25, 75, 95, 98]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_recognition, name='Messi Recognition', line_color='#4ECDC4', showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_recognition, name='Ronaldo Recognition', line_color='#FF6B6B', showlegend=False), row=2, col=1)
    
    # Media coverage
    messi_media = [20, 60, 90, 95]
    ronaldo_media = [25, 70, 95, 92]
    fig.add_trace(go.Scatter(x=career_phases, y=messi_media, name='Messi Media', line_color='#4ECDC4', showlegend=False), row=2, col=2)
    fig.add_trace(go.Scatter(x=career_phases, y=ronaldo_media, name='Ronaldo Media', line_color='#FF6B6B', showlegend=False), row=2, col=2)
    
    fig.update_layout(height=600, title_text="📈 Fame Evolution Across Career Phases")
    st.plotly_chart(fig, use_container_width=True)
    
    # Final fame verdict
    st.markdown('<h3 class="section-header">🏁 Fame & Global Impact Verdict</h3>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="final-verdict-card">
        <h2>📱 Global Fame Champion</h2>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3>🇵🇹 RONALDO: The Social Media King</h3>
                <p>✅ Most followed person on Instagram (615M)</p>
                <p>✅ Highest total social media following (950M)</p>
                <p>✅ Superior brand value ($700M vs $600M)</p>
                <p>✅ Higher annual earnings ($136M vs $130M)</p>
                <p>✅ More business ventures (15 vs 8)</p>
                <p>✅ Greater merchandise sales ($185M vs $125M)</p>
                <p>✅ Higher global influence rank (1.8 vs 2.1)</p>
            </div>
            <div style="text-align: center;">
                <h3>🇦🇷 MESSI: The Cultural Icon</h3>
                <p>✅ Higher cultural impact score (95 vs 92)</p>
                <p>✅ Most-liked sports post ever (75M)</p>
                <p>✅ UNESCO Goodwill Ambassador</p>
                <p>✅ More authentic engagement style</p>
                <p>✅ Strong regional dominance (South America)</p>
                <p>✅ Apple TV+ global partnership</p>
                <p>✅ World Cup viral moment peak</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            <strong>Fame Winner:</strong> 🇵🇹 <strong>RONALDO</strong> - The ultimate global superstar!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final analysis
    st.markdown("""
    ---
    ### 🌟 Global Fame & Impact Legacy
    
    **🇵🇹 Ronaldo has mastered the art of global fame** like no athlete before him. His 950M+ social media followers, 
    superior brand value, and extensive business empire make him the most commercially successful footballer ever. 
    His ability to monetize his fame across multiple platforms and ventures is unmatched.
    
    **🇦🇷 Messi represents authentic cultural impact** over pure commercial success. While his numbers are slightly 
    lower, his cultural influence runs deeper, especially in South America and among football purists. His World Cup 
    victory created the most viral sports moment in history.
    
    **🏆 The Verdict:** Ronaldo wins the fame category through sheer scale and commercial dominance. However, both 
    players have transcended sport to become global cultural phenomena, inspiring billions and redefining what 
    athlete fame means in the digital age.
    
    **📊 Combined Legacy:** Together, they command 1.66+ billion social media followers, making them the most 
    followed athletes in history. Their combined influence has globalised football like never before, reaching 
    every corner of the planet and inspiring countless future stars.
    
    **🌍 Global Impact:** Both have used their platforms for philanthropy, social causes, and inspiring the next 
    generation, proving that with great fame comes great responsibility - and both have delivered magnificently.
    """)

if __name__ == "__main__":
    show()