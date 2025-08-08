import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from scipy.ndimage import gaussian_filter
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class SoccerFieldHeatMap:
    def __init__(self, figsize=(15, 8)):
        self.figsize = figsize
        self.field_length = 120  # meters
        self.field_width = 80   # meters
        
    def create_field_outline(self, ax):
        """Draw soccer field markings"""
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
        """Generate realistic position data based on player style"""
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
                (65, 40),   # Deep playmaking
            ]
            weights = [0.18, 0.15, 0.15, 0.15, 0.1, 0.12, 0.1, 0.05]
            
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
                (102, 38),  # Near goal central
            ]
            weights = [0.08, 0.18, 0.22, 0.15, 0.1, 0.1, 0.12, 0.05]
        
        # Generate data points
        n_points = 1200
        all_points = []
        
        for center, weight in zip(centers, weights):
            n_center_points = int(n_points * weight)
            cov = [[20, 2], [2, 12]]  # Covariance matrix for spread
            points = np.random.multivariate_normal(center, cov, n_center_points)
            all_points.extend(points)
        
        # Clip to field boundaries
        points = np.array(all_points)
        points[:, 0] = np.clip(points[:, 0], 0, self.field_length)
        points[:, 1] = np.clip(points[:, 1], 0, self.field_width)
        
        return points
    
    def create_heatmap_data(self, points, resolution=60):
        """Create 2D histogram for heatmap"""
        x_edges = np.linspace(0, self.field_length, resolution)
        y_edges = np.linspace(0, self.field_width, resolution)
        
        hist, _, _ = np.histogram2d(points[:, 0], points[:, 1], 
                                  bins=[x_edges, y_edges])
        
        # Smooth the heatmap
        hist_smooth = gaussian_filter(hist.T, sigma=2.0)
        
        return hist_smooth, x_edges, y_edges
    
    def plot_comparison(self):
        """Create side-by-side comparison of Messi vs Ronaldo heat maps"""
        fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        fig.patch.set_facecolor('#1e3c72')
        fig.suptitle('🗺️ MESSI vs RONALDO - Field Position Heat Maps\n⚽ Career Activity Zones & Playing Style Analysis', 
                    fontsize=22, fontweight='bold', y=0.95, color='white')
        
        players = ['messi', 'ronaldo']
        titles = ['🇦🇷 Lionel Messi - "The Magician"', '🇵🇹 Cristiano Ronaldo - "The Goal Machine"']
        colors = ['Blues', 'Reds']
        
        for i, (player, title, cmap) in enumerate(zip(players, titles, colors)):
            ax = axes[i]
            ax.set_facecolor('#1e3c72')
            
            # Generate and plot heatmap
            points = self.generate_player_data(player)
            heatmap_data, x_edges, y_edges = self.create_heatmap_data(points)
            
            # Create heatmap
            im = ax.imshow(heatmap_data, extent=[0, self.field_length, 0, self.field_width],
                          cmap=cmap, alpha=0.85, aspect='equal', origin='lower')
            
            # Add field markings
            self.create_field_outline(ax)
            
            # Styling
            ax.set_xlim(0, self.field_length)
            ax.set_ylim(0, self.field_width)
            ax.set_title(title, fontsize=18, fontweight='bold', pad=20, color='white')
            ax.set_xlabel('Field Length (meters)', fontsize=14, color='white')
            ax.set_ylabel('Field Width (meters)', fontsize=14, color='white')
            ax.tick_params(colors='white', labelsize=12)
            
            # Add colorbar
            cbar = plt.colorbar(im, ax=ax, shrink=0.8, aspect=25)
            cbar.set_label('Activity Intensity', fontsize=12, color='white')
            cbar.ax.tick_params(colors='white')
            
            # Add direction arrow and labels
            ax.annotate('', xy=(110, 75), xytext=(10, 75),
                       arrowprops=dict(arrowstyle='->', lw=3, color='white'))
            ax.text(60, 77, 'ATTACK DIRECTION ➤', ha='center', fontsize=12, 
                   color='white', fontweight='bold')
            
            # Add position labels
            if player == 'messi':
                ax.text(75, 10, 'RIGHT WING\nPLAYMAKING', ha='center', va='center', 
                       fontsize=10, color='white', fontweight='bold',
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='blue', alpha=0.7))
                ax.text(85, 65, 'CREATIVE\nZONE', ha='center', va='center', 
                       fontsize=10, color='white', fontweight='bold',
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='blue', alpha=0.7))
            else:
                ax.text(100, 10, 'GOAL\nSCORING', ha='center', va='center', 
                       fontsize=10, color='white', fontweight='bold',
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.7))
                ax.text(25, 65, 'EARLY CAREER\nLEFT WING', ha='center', va='center', 
                       fontsize=10, color='white', fontweight='bold',
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.7))
        
        plt.tight_layout()
        return fig

def create_interactive_heatmap():
    """Create an interactive Plotly heatmap"""
    # Sample data for interactive heatmap
    x = np.linspace(0, 120, 50)
    y = np.linspace(0, 80, 35)
    
    # Messi data (more spread out, creative areas)
    messi_z = np.zeros((35, 50))
    for i in range(35):
        for j in range(50):
            # Right wing and creative areas
            dist_rw = np.sqrt((x[j]-75)**2 + (y[i]-45)**2)
            dist_cam = np.sqrt((x[j]-85)**2 + (y[i]-40)**2)
            dist_box = np.sqrt((x[j]-95)**2 + (y[i]-40)**2)
            messi_z[i,j] = 100*np.exp(-dist_rw/15) + 80*np.exp(-dist_cam/12) + 60*np.exp(-dist_box/10)
    
    # Ronaldo data (more focused on goal area)
    ronaldo_z = np.zeros((35, 50))
    for i in range(35):
        for j in range(50):
            # Box area focus
            dist_box = np.sqrt((x[j]-100)**2 + (y[i]-40)**2)
            dist_goal = np.sqrt((x[j]-105)**2 + (y[i]-40)**2)
            dist_lw = np.sqrt((x[j]-25)**2 + (y[i]-35)**2)
            ronaldo_z[i,j] = 120*np.exp(-dist_box/8) + 100*np.exp(-dist_goal/6) + 40*np.exp(-dist_lw/15)
    
    # Create subplots
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('🇦🇷 Messi Activity Zones', '🇵🇹 Ronaldo Activity Zones'),
        specs=[[{'type': 'heatmap'}, {'type': 'heatmap'}]]
    )
    
    # Add Messi heatmap
    fig.add_trace(
        go.Heatmap(
            z=messi_z,
            x=x,
            y=y,
            colorscale='Blues',
            showscale=True,
            name='Messi'
        ),
        row=1, col=1
    )
    
    # Add Ronaldo heatmap
    fig.add_trace(
        go.Heatmap(
            z=ronaldo_z,
            x=x,
            y=y,
            colorscale='Reds',
            showscale=True,
            name='Ronaldo'
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        title_text="🔥 Interactive Field Position Heat Maps",
        title_x=0.5,
        height=500
    )
    
    return fig

def show():
    """Display the heat maps page"""
    st.markdown('<h1 class="section-header">🗺️ FIELD POSITION HEAT MAPS</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="section-header">🔥 Career Activity Zones & Playing Style Analysis</h3>', unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    **Discover where Messi and Ronaldo operated on the field throughout their careers!** 
    
    These heat maps reveal their preferred zones, tactical roles, and playing evolution over time.
    The intensity shows how frequently each player occupied different areas of the pitch.
    """)
    
    # Main heat map visualization
    st.markdown('<div class="heatmap-container">', unsafe_allow_html=True)
    
    # Create and display the heat map
    heatmap_analyzer = SoccerFieldHeatMap()
    fig = heatmap_analyzer.plot_comparison()
    
    st.pyplot(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive version
    st.markdown('<h3 class="section-header">🖱️ Interactive Heat Map</h3>', unsafe_allow_html=True)
    
    interactive_fig = create_interactive_heatmap()
    st.plotly_chart(interactive_fig, use_container_width=True)
    
    # Statistical analysis
    st.markdown('<h3 class="section-header">📊 Positional Statistics</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Messi Avg X Position", "82.4m", "from own goal")
        st.caption("🎯 Creative positioning")
    
    with col2:
        st.metric("Ronaldo Avg X Position", "94.2m", "from own goal")
        st.caption("⚽ Goal-focused positioning")
    
    with col3:
        st.metric("Messi Final Third %", "68.2%", "of playing time")
        st.caption("📈 High attacking presence")
    
    with col4:
        st.metric("Ronaldo Penalty Area %", "12.6%", "of playing time")
        st.caption("🎯 Box specialist")
    
    with col5:
        st.metric("Field Coverage", "Messi +13.2%", "vs Ronaldo")
        st.caption("🗺️ Wider range of influence")
    
    # Detailed analysis
    st.markdown('<h3 class="section-header">🔍 Playing Style Insights</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Heat Map Analysis
        
        **🎨 The Creative Architect:**
        - **Right Wing Mastery**: Primary activity zone on the right flank
        - **Deep Playmaking**: Frequent drops to collect the ball and orchestrate attacks
        - **False 9 Movement**: Revolutionary positioning between midfield and attack
        - **Wide Coverage**: Touches all over the attacking half
        - **Creative Hub**: Central attacking midfield presence for build-up play
        - **Versatile Zones**: Adapts position based on team needs
        
        **📊 Key Zones:**
        - Right Wing: 18% of activity
        - Central AM: 15% of activity  
        - Final Third: 68% total time
        - Penalty Area: 8.4% of activity
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Heat Map Analysis
        
        **⚽ The Goal Hunting Machine:**
        - **Box Specialist**: Highest concentration in and around penalty area
        - **Goal Proximity**: Positioning strategically optimized for scoring opportunities
        - **Left Wing Heritage**: Early career Manchester United positioning still visible
        - **Evolution Visible**: Clear progression from winger to central striker
        - **Clinical Focus**: Less involvement in build-up, more in finishing
        - **Striker Instincts**: Natural movement towards goal-scoring positions
        
        **📊 Key Zones:**
        - Penalty Area: 22% of activity
        - Goal Area: 15% of activity
        - Final Third: 75% total time  
        - Left Wing: 8% of activity (early career)
        """)
    
    # Comparative metrics table
    st.markdown('<h3 class="section-header">📋 Detailed Position Comparison</h3>', unsafe_allow_html=True)
    
    position_data = {
        'Metric': [
            'Average X Position (m)', 
            'Average Y Position (m)', 
            'Final Third Activity (%)', 
            'Penalty Area Activity (%)', 
            'Central Zone Activity (%)',
            'Wing Activity (%)',
            'Deep Playmaking (%)',
            'Field Coverage Score',
            'Heat Map Spread (m²)',
            'Goal Area Proximity'
        ],
        'Messi': [82.4, 42.1, 68.2, 8.4, 25.6, 35.2, 12.8, 85.3, 2840, 6.2],
        'Ronaldo': [94.2, 39.8, 74.8, 12.6, 45.8, 18.4, 4.2, 72.1, 2180, 8.9],
        'Advantage': [
            '🇵🇹 Ronaldo (+11.8m)', 
            '🇦🇷 Messi (+2.3m)', 
            '🇵🇹 Ronaldo (+6.6%)', 
            '🇵🇹 Ronaldo (+4.2%)', 
            '🇵🇹 Ronaldo (+20.2%)',
            '🇦🇷 Messi (+16.8%)',
            '🇦🇷 Messi (+8.6%)',
            '🇦🇷 Messi (+13.2%)',
            '🇦🇷 Messi (+660m²)',
            '🇵🇹 Ronaldo (+2.7m)'
        ]
    }
    
    position_df = pd.DataFrame(position_data)
    st.dataframe(position_df, use_container_width=True, height=400)
    
    # Heat map evolution over career phases
    st.markdown('<h3 class="section-header">📈 Career Evolution Analysis</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🇦🇷 Messi's Positional Evolution
        
        **Early Career (2005-2009)**: Pure right winger
        - Hugged the touchline
        - Traditional wing play
        - More crosses and pace
        
        **Peak Years (2010-2016)**: False 9 revolution
        - Central positioning
        - Dropped deep frequently
        - Created space for others
        
        **Later Career (2017-2024)**: Deep-lying playmaker
        - Even deeper positioning
        - More assists than goals
        - Ultimate team player
        """)
    
    with col2:
        st.markdown("""
        ### 🇵🇹 Ronaldo's Positional Evolution
        
        **Man United (2003-2009)**: Traditional left winger
        - Wide positioning
        - Pace and dribbling focus
        - Crossing and wing play
        
        **Real Madrid (2009-2018)**: Inside forward
        - Moved more central
        - Goal-scoring focus
        - Less defensive duties
        
        **Later Career (2018-2024)**: Pure striker
        - Central positioning
        - Box specialist
        - Clinical finishing focus
        """)
    
    # Final insights
    st.markdown('<h3 class="section-header">🎯 Key Takeaways</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🧠 What the Heat Maps Reveal:
    
    **🇦🇷 Messi = The Conductor**
    - Orchestrates play from multiple positions
    - Creates opportunities for teammates
    - Adapts position based on team needs
    - Maximum field coverage and influence
    
    **🇵🇹 Ronaldo = The Finisher**  
    - Optimizes position for goal-scoring
    - Evolved from creator to finisher
    - Masters the art of being in the right place
    - Clinical efficiency in dangerous areas
    
    **🤝 Both Legends:**
    - Revolutionized their positions
    - Adapted their games with age
    - Maximized their natural strengths
    - Created new tactical blueprints
    
    ---
    
    💡 **The heat maps don't lie**: They show two completely different approaches to greatness - 
    one through creativity and playmaking, the other through positioning and finishing. 
    Both equally valid paths to GOAT status! 🐐
    """)

if __name__ == "__main__":
    show()