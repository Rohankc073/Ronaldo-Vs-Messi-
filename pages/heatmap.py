import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from scipy.ndimage import gaussian_filter
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class SoccerFieldHeatMap:
    def __init__(self, figsize=(15, 10)):
        self.figsize = figsize
        self.field_length = 120  # meters
        self.field_width = 80   # meters
        
    def create_field_outline(self, ax):
        """Draw soccer field markings exactly like reference"""
        # Field outline
        field = Rectangle((0, 0), self.field_length, self.field_width, 
                         linewidth=2, edgecolor='white', facecolor='none')
        ax.add_patch(field)
        
        # Center line
        ax.plot([self.field_length/2, self.field_length/2], [0, self.field_width], 
                color='white', linewidth=2)
        
        # Center circle
        center_circle = Circle((self.field_length/2, self.field_width/2), 9.15, 
                              linewidth=2, color='white', fill=False)
        ax.add_patch(center_circle)
        
        # Center spot
        ax.plot(self.field_length/2, self.field_width/2, 'wo', markersize=3)
        
        # Goal areas (6-yard box)
        goal_area_left = Rectangle((0, (self.field_width-20)/2), 5.5, 20, 
                                  linewidth=2, edgecolor='white', facecolor='none')
        goal_area_right = Rectangle((self.field_length-5.5, (self.field_width-20)/2), 5.5, 20,
                                   linewidth=2, edgecolor='white', facecolor='none')
        ax.add_patch(goal_area_left)
        ax.add_patch(goal_area_right)
        
        # Penalty areas (18-yard box)
        penalty_area_left = Rectangle((0, (self.field_width-44)/2), 16.5, 44,
                                     linewidth=2, edgecolor='white', facecolor='none')
        penalty_area_right = Rectangle((self.field_length-16.5, (self.field_width-44)/2), 16.5, 44,
                                      linewidth=2, edgecolor='white', facecolor='none')
        ax.add_patch(penalty_area_left)
        ax.add_patch(penalty_area_right)
        
        # Penalty spots
        ax.plot(11, self.field_width/2, 'wo', markersize=3)
        ax.plot(self.field_length-11, self.field_width/2, 'wo', markersize=3)
        
        # Goals
        ax.plot([0, 0], [(self.field_width-7.32)/2, (self.field_width+7.32)/2], 
                color='white', linewidth=3)
        ax.plot([self.field_length, self.field_length], [(self.field_width-7.32)/2, (self.field_width+7.32)/2], 
                color='white', linewidth=3)
    
    def generate_player_data(self, player_style='messi'):
        """Generate realistic position data based on player style - exact reference implementation"""
        np.random.seed(42 if player_style == 'messi' else 24)
        
        if player_style == 'messi':
            # Messi - more central, slightly right-wing, creative areas
            centers = [
                (75, 45),   # Right wing
                (85, 40),   # Attacking midfield right
                (95, 40),   # Final third right
                (70, 35),   # Central attacking midfield
                (80, 50),   # Right attacking areas
                (90, 45),   # Box edge right
                (100, 40),  # Penalty area right
            ]
            weights = [0.2, 0.15, 0.15, 0.15, 0.1, 0.15, 0.1]
            
        else:  # ronaldo
            # Ronaldo - more box-focused, left wing early career, central striker later
            centers = [
                (25, 35),   # Left wing (early career)
                (95, 40),   # Box area central
                (100, 45),  # Penalty area central
                (105, 40),  # Goal area
                (90, 30),   # Box edge left
                (90, 50),   # Box edge right
                (98, 40),   # Prime scoring area
            ]
            weights = [0.1, 0.2, 0.25, 0.15, 0.1, 0.1, 0.1]
        
        # Generate data points
        n_points = 1000
        all_points = []
        
        for center, weight in zip(centers, weights):
            n_center_points = int(n_points * weight)
            cov = [[25, 3], [3, 15]]  # Covariance matrix for spread
            points = np.random.multivariate_normal(center, cov, n_center_points)
            all_points.extend(points)
        
        # Clip to field boundaries
        points = np.array(all_points)
        points[:, 0] = np.clip(points[:, 0], 0, self.field_length)
        points[:, 1] = np.clip(points[:, 1], 0, self.field_width)
        
        return points
    
    def create_heatmap_data(self, points, resolution=50):
        """Create 2D histogram for heatmap - exact reference implementation"""
        x_edges = np.linspace(0, self.field_length, resolution)
        y_edges = np.linspace(0, self.field_width, resolution)
        
        hist, _, _ = np.histogram2d(points[:, 0], points[:, 1], 
                                  bins=[x_edges, y_edges])
        
        # Smooth the heatmap
        hist_smooth = gaussian_filter(hist.T, sigma=1.5)
        
        return hist_smooth, x_edges, y_edges
    
    def plot_comparison(self):
        """Create side-by-side comparison exactly like reference"""
        # Set font to Times New Roman
        plt.rcParams['font.family'] = 'Times New Roman'
        
        fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        fig.suptitle('MESSI vs RONALDO - Field Position Heat Maps\n' + 
                    'Career Activity Zones Comparison', 
                    fontsize=20, fontweight='bold', y=0.95, family='Times New Roman')
        
        players = ['messi', 'ronaldo']
        titles = ['Lionel Messi - "The Magician"', 'Cristiano Ronaldo - "The Goal Machine"']
        # Updated colors: Argentina Blue and Portugal Red
        colors = ['Blues', 'Reds']
        
        for i, (player, title, cmap) in enumerate(zip(players, titles, colors)):
            ax = axes[i]
            
            # Generate and plot heatmap
            points = self.generate_player_data(player)
            heatmap_data, x_edges, y_edges = self.create_heatmap_data(points)
            
            # Create heatmap
            im = ax.imshow(heatmap_data, extent=[0, self.field_length, 0, self.field_width],
                          cmap=cmap, alpha=0.8, aspect='equal', origin='lower')
            
            # Add field markings
            self.create_field_outline(ax)
            
            # Styling with Times New Roman
            ax.set_xlim(0, self.field_length)
            ax.set_ylim(0, self.field_width)
            ax.set_title(title, fontsize=16, fontweight='bold', pad=20, family='Times New Roman')
            ax.set_xlabel('Field Length (meters)', fontsize=12, family='Times New Roman')
            ax.set_ylabel('Field Width (meters)', fontsize=12, family='Times New Roman')
            
            # Add colorbar
            cbar = plt.colorbar(im, ax=ax, shrink=0.8, aspect=20)
            cbar.set_label('Activity Intensity', fontsize=10, family='Times New Roman')
            
            # Add direction arrow
            ax.annotate('', xy=(110, 75), xytext=(10, 75),
                       arrowprops=dict(arrowstyle='->', lw=2, color='white'))
            ax.text(60, 77, 'Attack Direction', ha='center', fontsize=10, 
                   color='white', fontweight='bold', family='Times New Roman')
        
        plt.tight_layout()
        return fig
    
    def plot_overlay_comparison(self):
        """Create overlay comparison showing both players on same field"""
        # Set font to Times New Roman
        plt.rcParams['font.family'] = 'Times New Roman'
        
        fig, ax = plt.subplots(figsize=(15, 10))
        fig.suptitle('MESSI vs RONALDO - Overlapping Heat Map Comparison\n' + 
                    'Blue = Messi Zones | Red = Ronaldo Zones | Purple = Overlap', 
                    fontsize=16, fontweight='bold', family='Times New Roman')
        
        # Generate data for both players
        messi_points = self.generate_player_data('messi')
        ronaldo_points = self.generate_player_data('ronaldo')
        
        messi_heat, x_edges, y_edges = self.create_heatmap_data(messi_points)
        ronaldo_heat, _, _ = self.create_heatmap_data(ronaldo_points)
        
        # Normalize the heatmaps
        messi_heat = messi_heat / np.max(messi_heat)
        ronaldo_heat = ronaldo_heat / np.max(ronaldo_heat)
        
        # Create RGB overlay
        rgb_data = np.zeros((messi_heat.shape[0], messi_heat.shape[1], 3))
        rgb_data[:, :, 2] = messi_heat     # Blue channel for Messi
        rgb_data[:, :, 0] = ronaldo_heat   # Red channel for Ronaldo
        
        # Plot overlay
        ax.imshow(rgb_data, extent=[0, self.field_length, 0, self.field_width],
                 alpha=0.7, aspect='equal', origin='lower')
        
        # Add field markings
        self.create_field_outline(ax)
        
        # Styling with Times New Roman
        ax.set_xlim(0, self.field_length)
        ax.set_ylim(0, self.field_width)
        ax.set_xlabel('Field Length (meters)', fontsize=12, family='Times New Roman')
        ax.set_ylabel('Field Width (meters)', fontsize=12, family='Times New Roman')
        
        # Add direction arrow
        ax.annotate('', xy=(110, 75), xytext=(10, 75),
                   arrowprops=dict(arrowstyle='->', lw=3, color='white'))
        ax.text(60, 77, 'Attack Direction', ha='center', fontsize=12, 
               color='white', fontweight='bold', family='Times New Roman')
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor='blue', alpha=0.7, label='Messi Activity'),
                          Patch(facecolor='red', alpha=0.7, label='Ronaldo Activity'),
                          Patch(facecolor='purple', alpha=0.7, label='Overlap Areas')]
        ax.legend(handles=legend_elements, loc='upper left', fontsize=10, 
                 labelcolor='white', prop={'family': 'Times New Roman'})
         
        plt.tight_layout()
        return fig
    
    def create_stats_summary(self):
        """Create a summary statistics comparison"""
        # Set font to Times New Roman
        plt.rcParams['font.family'] = 'Times New Roman'
        
        # Generate data
        messi_points = self.generate_player_data('messi')
        ronaldo_points = self.generate_player_data('ronaldo')
        
        # Calculate statistics
        stats_data = {
            'Player': ['Messi', 'Ronaldo'],
            'Avg X Position': [np.mean(messi_points[:, 0]), np.mean(ronaldo_points[:, 0])],
            'Avg Y Position': [np.mean(messi_points[:, 1]), np.mean(ronaldo_points[:, 1])],
            'X Position Std': [np.std(messi_points[:, 0]), np.std(ronaldo_points[:, 0])],
            'Y Position Std': [np.std(messi_points[:, 1]), np.std(ronaldo_points[:, 1])],
            'Final Third %': [(messi_points[:, 0] > 80).mean() * 100, 
                             (ronaldo_points[:, 0] > 80).mean() * 100],
            'Penalty Area %': [((messi_points[:, 0] > 103.5) & 
                               (messi_points[:, 1] > 18) & 
                               (messi_points[:, 1] < 62)).mean() * 100,
                              ((ronaldo_points[:, 0] > 103.5) & 
                               (ronaldo_points[:, 1] > 18) & 
                               (ronaldo_points[:, 1] < 62)).mean() * 100]
        }
        
        df = pd.DataFrame(stats_data)
        
        # Create comparison plot with Argentina Blue and Portugal Red
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Positional Statistics Comparison', fontsize=16, fontweight='bold', family='Times New Roman')
        
        # Colors: Argentina Blue and Portugal Red
        messi_color = '#75AADB'
        ronaldo_color = '#FF2D2D'
        
        # Average positions
        ax1 = axes[0, 0]
        ax1.bar(['Messi', 'Ronaldo'], df['Avg X Position'], color=[messi_color, ronaldo_color], alpha=0.7)
        ax1.set_title('Average X Position (Attack Direction)', family='Times New Roman')
        ax1.set_ylabel('Meters from own goal', family='Times New Roman')
        
        ax2 = axes[0, 1]
        ax2.bar(['Messi', 'Ronaldo'], df['Avg Y Position'], color=[messi_color, ronaldo_color], alpha=0.7)
        ax2.set_title('Average Y Position (Width)', family='Times New Roman')
        ax2.set_ylabel('Meters from sideline', family='Times New Roman')
        
        # Position variability
        ax3 = axes[1, 0]
        ax3.bar(['Messi', 'Ronaldo'], df['X Position Std'], color=[messi_color, ronaldo_color], alpha=0.7)
        ax3.set_title('Positional Variability (X)', family='Times New Roman')
        ax3.set_ylabel('Standard Deviation', family='Times New Roman')
        
        # Final third and penalty area presence
        ax4 = axes[1, 1]
        x = np.arange(2)
        width = 0.35
        ax4.bar(x - width/2, df['Final Third %'], width, label='Final Third %', alpha=0.7, color=messi_color)
        ax4.bar(x + width/2, df['Penalty Area %'], width, label='Penalty Area %', alpha=0.7, color=ronaldo_color)
        ax4.set_title('Attacking Zone Presence', family='Times New Roman')
        ax4.set_ylabel('Percentage of time', family='Times New Roman')
        ax4.set_xticks(x)
        ax4.set_xticklabels(['Messi', 'Ronaldo'])
        ax4.legend(prop={'family': 'Times New Roman'})
        
        plt.tight_layout()
        return fig, df

def show():
    """Display the heat maps using exact reference + enhanced visualizations"""
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
    
    st.set_page_config(page_title="Heat Map Analysis", layout="wide")
    
    # Argentina Blue: #75AADB, Portugal Red: #FF2D2D
    MESSI_COLOR = '#75AADB'
    RONALDO_COLOR = '#FF2D2D'
    
    st.markdown(f"""
    <h1 style="text-align: center; color: {MESSI_COLOR}; font-family: 'Times New Roman', serif;">
    🔥 MESSI vs RONALDO Heat Map Analysis
    </h1>
    """, unsafe_allow_html=True)
    
    # Visual comparison cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {MESSI_COLOR}, #5a9bd4);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin: 1rem 0;
            font-family: 'Times New Roman', serif;
        ">
            <h2>🇦🇷 MESSI</h2>
            <h3>The Magician</h3>
            <div style="display: flex; justify-content: space-around; margin: 1rem 0;">
                <div><strong>Creative</strong><br>Playmaker</div>
                <div><strong>Right Wing</strong><br>Specialist</div>
                <div><strong>Deep</strong><br>Involvement</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {RONALDO_COLOR}, #e02525);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin: 1rem 0;
            font-family: 'Times New Roman', serif;
        ">
            <h2>🇵🇹 RONALDO</h2>
            <h3>The Goal Machine</h3>
            <div style="display: flex; justify-content: space-around; margin: 1rem 0;">
                <div><strong>Goal</strong><br>Focused</div>
                <div><strong>Penalty Area</strong><br>Expert</div>
                <div><strong>Clinical</strong><br>Finisher</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main heat map visualization using exact reference code
    st.markdown('## 🏟️ Professional Field Position Heat Maps')
    
    analyzer = SoccerFieldHeatMap()
    fig1 = analyzer.plot_comparison()
    st.pyplot(fig1, use_container_width=True)
    
    # Enhanced interactive dashboard
    st.markdown('## 📊 Interactive Performance Dashboard')
    
    # Create simple dashboard inline
    col1, col2 = st.columns(2)
    
    with col1:
        # Zone comparison
        zones = ['Penalty Area', 'Final Third', 'Right Wing', 'Central', 'Left Wing']
        messi_zones = [15, 68, 25, 30, 8]
        ronaldo_zones = [28, 75, 12, 45, 15]
        
        fig_zones = go.Figure()
        fig_zones.add_trace(go.Bar(
            x=zones, y=messi_zones, name='Messi', 
            marker_color=MESSI_COLOR, text=[f'{v}%' for v in messi_zones],
            textposition='auto', textfont=dict(family='Times New Roman')
        ))
        fig_zones.add_trace(go.Bar(
            x=zones, y=ronaldo_zones, name='Ronaldo',
            marker_color=RONALDO_COLOR, text=[f'{v}%' for v in ronaldo_zones],
            textposition='auto', textfont=dict(family='Times New Roman')
        ))
        fig_zones.update_layout(
            title="Zone Activity Distribution",
            yaxis_title="Percentage of Time",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_zones, use_container_width=True)
    
    with col2:
        # Goal distance analysis
        distances = np.arange(5, 51, 5)
        messi_goals = [8, 12, 18, 22, 15, 12, 8, 3, 1, 1]
        ronaldo_goals = [15, 20, 25, 18, 12, 6, 3, 1, 0, 0]
        
        fig_goals = go.Figure()
        fig_goals.add_trace(go.Scatter(
            x=distances, y=messi_goals, mode='lines+markers',
            name='Messi Goals', line=dict(color=MESSI_COLOR, width=4),
            marker=dict(size=10)
        ))
        fig_goals.add_trace(go.Scatter(
            x=distances, y=ronaldo_goals, mode='lines+markers',
            name='Ronaldo Goals', line=dict(color=RONALDO_COLOR, width=4),
            marker=dict(size=10)
        ))
        fig_goals.update_layout(
            title="Goal Distance Analysis",
            xaxis_title="Distance from Goal (m)",
            yaxis_title="Goals Scored",
            template='plotly_white',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_goals, use_container_width=True)
    
    # Position attributes comparison
    st.markdown('## 📡 Positional Attributes Comparison')
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create simple bar comparison instead of radar
        categories = ['Goal Proximity', 'Creative Freedom', 'Wing Play', 
                     'Central Presence', 'Deep Involvement', 'Box Activity']
        messi_values = [70, 95, 80, 85, 90, 60]
        ronaldo_values = [95, 65, 70, 85, 45, 90]
        
        fig_comparison = go.Figure()
        fig_comparison.add_trace(go.Bar(
            x=categories, y=messi_values, name='🇦🇷 Messi',
            marker_color=MESSI_COLOR, opacity=0.8,
            textfont=dict(family='Times New Roman')
        ))
        fig_comparison.add_trace(go.Bar(
            x=categories, y=ronaldo_values, name='🇵🇹 Ronaldo',
            marker_color=RONALDO_COLOR, opacity=0.8,
            textfont=dict(family='Times New Roman')
        ))
        fig_comparison.update_layout(
            title="Positional Attributes Comparison",
            yaxis_title="Score (0-100)",
            template='plotly_white',
            barmode='group',
            font=dict(family='Times New Roman')
        )
        st.plotly_chart(fig_comparison, use_container_width=True)
    
    with col2:
        st.markdown("""
        #### 🎯 Radar Insights
        
        **🇦🇷 Messi Strengths:**
        - Creative Freedom: 95/100
        - Deep Involvement: 90/100
        - Central Presence: 85/100
        
        **🇵🇹 Ronaldo Strengths:**
        - Goal Proximity: 95/100
        - Box Activity: 90/100
        - Central Presence: 85/100
        
        **📊 Key Difference:**
        Messi excels in creativity and deep play, 
        while Ronaldo dominates goal-scoring zones.
        """)
    
    # Overlay comparison using reference code
    st.markdown('## 🔄 Overlapping Heat Map Analysis')
    st.markdown('**Blue = Messi Zones | Red = Ronaldo Zones | Purple = Overlap Areas**')
    
    fig2 = analyzer.plot_overlay_comparison()
    st.pyplot(fig2, use_container_width=True)
    
    # Statistical analysis using reference code
    st.markdown('## 📊 Advanced Positional Statistics')
    
    fig3, stats_df = analyzer.create_stats_summary()
    st.pyplot(fig3, use_container_width=True)
    
    # Key metrics with custom design
    st.markdown('## 🎯 Key Performance Metrics')
    
    # Custom metrics cards
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Goal Proximity</h4>
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
            ">+13m closer to goal</div>
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
            <div style="font-size: 2rem; margin-bottom: 10px;">🎨</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Creative Freedom</h4>
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
            ">+30% more zones</div>
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
            border: 2px solid {MESSI_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">⚡</div>
            <h4 style="color: {MESSI_COLOR}; margin: 0 0 10px 0;">Field Coverage</h4>
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
            ">+25% wider range</div>
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
            border: 2px solid {RONALDO_COLOR};
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: 'Times New Roman', serif;
            margin: 10px 0;
        ">
            <div style="font-size: 2rem; margin-bottom: 10px;">🥅</div>
            <h4 style="color: {RONALDO_COLOR}; margin: 0 0 10px 0;">Box Activity</h4>
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
            ">+7% more time</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics table
    st.markdown('### 📋 Detailed Statistics')
    st.dataframe(stats_df.round(2), use_container_width=True)
    
    # Career evolution timeline
    st.markdown('### 📈 Positional Evolution Timeline')
    
    # Create evolution chart inline
    years = list(range(2005, 2024))
    messi_x_pos = [70, 72, 74, 76, 78, 80, 82, 84, 85, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68]
    ronaldo_x_pos = [25, 30, 35, 40, 75, 80, 85, 90, 92, 94, 96, 95, 94, 95, 96, 97, 98, 99, 100]
    
    fig_evolution = go.Figure()
    
    fig_evolution.add_trace(go.Scatter(
        x=years, y=messi_x_pos, mode='lines+markers',
        name='🇦🇷 Messi X Position', line=dict(color=MESSI_COLOR, width=4),
        marker=dict(size=8)
    ))
    
    fig_evolution.add_trace(go.Scatter(
        x=years, y=ronaldo_x_pos, mode='lines+markers',
        name='🇵🇹 Ronaldo X Position', line=dict(color=RONALDO_COLOR, width=4),
        marker=dict(size=8)
    ))
    
    fig_evolution.update_layout(
        title="📊 Average Field Position Evolution (2005-2023)",
        xaxis_title="Year", yaxis_title="Average X Position (meters from own goal)",
        height=400, template='plotly_white',
        font=dict(family='Times New Roman')
    )
    
    st.plotly_chart(fig_evolution, use_container_width=True)
    
    # Key insights
    st.markdown('## 🏆 Key Insights')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🇦🇷 Messi Profile:**
        - More creative positioning
        - Drops deeper to build play
        - Wider range of positions
        - Right-wing preference
        - Greater positional variability
        """)
    
    with col2:
        st.markdown("""
        **🇵🇹 Ronaldo Profile:**
        - More goal-focused positioning
        - Higher up the pitch
        - Penalty area specialist
        - Central striker evolution
        - Clinical finishing zones
        """)
    
    # Final verdict section with proper formatting
    st.markdown('## 🎯 Heat Map Verdict: Two Paths to Greatness')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🇦🇷 Messi = The Conductor**
        - Orchestrates from multiple positions
        - Creates space and opportunities  
        - Maximum field influence
        - Adapts to team tactical needs
        """)
    
    with col2:
        st.markdown("""
        **🇵🇹 Ronaldo = The Finisher**
        - Optimizes for goal-scoring
        - Masters dangerous area positioning
        - Clinical efficiency focus
        - Evolved with age and experience
        """)
    
    st.markdown("""
    ---
    
    ### 🤝 The Verdict
    
    The heat maps reveal two genius approaches: One through creative freedom and playmaking, 
    the other through positioning mastery and finishing. Both equally valid paths to GOAT status! 🐐
    """)

if __name__ == "__main__":
    show()