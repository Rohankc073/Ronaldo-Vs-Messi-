import pandas as pd
import streamlit as st

@st.cache_data
def load_all_data():
    """Load all data for the GOAT analysis with error handling"""
    
    try:
        # Achievements data
        achievements = pd.DataFrame({
            'category': ['Ballon d\'Or', 'Golden Boot', 'Champions League Top Scorer', 'FIFA Best', 'UEFA Player of Year', 'Liga MVP', 'World Cup Golden Ball'],
            'messi': [8, 6, 6, 3, 3, 6, 1],
            'ronaldo': [5, 4, 7, 2, 3, 2, 0]
        })

        # Career stats
        career_stats = pd.DataFrame({
            'player': ['Messi', 'Ronaldo'],
            'goals': [815, 895],
            'assists': [377, 236],
            'matches': [1069, 1205],
            'trophies': [44, 35],
            'ballonDors': [8, 5],
            'goalsPer90': [0.76, 0.74],
            'assistsPer90': [0.35, 0.20],
            'conversionRate': [17.8, 15.2],
            'shotAccuracy': [45.2, 42.8],
            'penaltyConversion': [77.8, 84.3],
            'dribblesCompleted': [2847, 1456],
            'keyPasses': [4521, 2847],
            'chancesCreated': [3254, 2108],
            'teamTrophies': [44, 35],
            'individualAwards': [47, 34]
        })

        # Club goals data
        club_goals = pd.DataFrame({
            'club': ['Barcelona', 'PSG', 'Inter Miami', 'Man United', 'Real Madrid', 'Juventus', 'Al Nassr', 'Sporting CP'],
            'messi': [672, 32, 25, 0, 0, 0, 0, 0],
            'ronaldo': [0, 0, 0, 145, 451, 101, 68, 5]
        })

        # International performance
        international = pd.DataFrame({
            'player': ['Messi', 'Ronaldo'],
            'country': ['Argentina', 'Portugal'],
            'matches': [183, 206],
            'goals': [108, 130],
            'assists': [56, 43],
            'trophies': [2, 2],
            'minutesPerGoal': [132, 130]
        })

        # Fame/Social media data
        fame = pd.DataFrame({
            'player': ['Messi', 'Ronaldo'],
            'instagramFollowers': [500000000, 615000000],
            'facebookFollowers': [115000000, 170000000],
            'twitterFollowers': [46000000, 110000000],
            'youtubeSubscribers': [2500000, 55000000],
            'googleSearchVolume': [45000000, 67000000],
            'sponsorshipIncomeUSD': [55000000, 70000000],
            'merchSalesUSD': [125000000, 185000000],
            'globalFanBaseM': [450, 520],
            'influenceRank': [2.1, 1.8]
        })

        # League stats
        league_stats = pd.DataFrame({
            'league': ['La Liga', 'Premier League', 'Serie A', 'Ligue 1', 'MLS', 'Saudi Pro League'],
            'messiGoals': [474, 0, 0, 16, 11, 0],
            'ronaldoGoals': [311, 103, 81, 0, 0, 35],
            'messiApps': [520, 0, 0, 67, 14, 0],
            'ronaldoApps': [292, 236, 98, 0, 0, 42]
        })

        # Physical attributes
        physical = pd.DataFrame({
            'player': ['Messi', 'Ronaldo'],
            'topSpeed_kmh': [32.5, 34.6],
            'strength_score': [75, 95],
            'stamina_score': [88, 92],
            'agility_score': [99, 85]
        })

        # Tactical attributes
        tactical = pd.DataFrame({
            'attribute': ['Vision', 'Passing', 'Dribbling', 'Finishing', 'Positioning', 'Aerial Ability'],
            'messi': [98.5, 97.8, 99.2, 95.4, 94.6, 72.3],
            'ronaldo': [88.7, 85.2, 89.4, 97.8, 96.5, 98.1]
        })

        # Clutch performance
        clutch = pd.DataFrame({
            'category': ['Final Goals', 'Penalty Shootout Goals', 'Last Minute Goals', 'Hat-tricks in Finals', 'Big Game Goals'],
            'messi': [26, 4, 23, 2, 89],
            'ronaldo': [22, 7, 31, 3, 95]
        })

        # Season by season goals (complete careers 2005-2023)
        years = list(range(2005, 2024))
        messi_goals_by_year = [1, 8, 17, 16, 38, 47, 53, 73, 60, 41, 58, 54, 37, 51, 36, 31, 38, 11, 21]
        ronaldo_goals_by_year = [9, 12, 23, 42, 33, 40, 60, 55, 51, 61, 48, 51, 42, 44, 37, 36, 24, 18, 35]
        
        season_goals = pd.DataFrame({
            'year': years,
            'messiGoals': messi_goals_by_year,
            'ronaldoGoals': ronaldo_goals_by_year,
            'messiAssists': [a//2 for a in messi_goals_by_year],
            'ronaldoAssists': [a//3 for a in ronaldo_goals_by_year]
        })

        data_dict = {
            'achievements': achievements,
            'career_stats': career_stats,
            'club_goals': club_goals,
            'international': international,
            'fame': fame,
            'league_stats': league_stats,
            'physical': physical,
            'tactical': tactical,
            'clutch': clutch,
            'season_goals': season_goals
        }
        
        # Log successful data loading
        st.sidebar.success(f"✅ Data loaded: {len(data_dict)} datasets")
        
        return data_dict
        
    except Exception as e:
        st.sidebar.error(f"❌ Error loading data: {e}")
        # Return minimal fallback data
        return {
            'career_stats': pd.DataFrame({
                'player': ['Messi', 'Ronaldo'],
                'goals': [815, 895],
                'assists': [377, 236]
            }),
            'season_goals': pd.DataFrame({
                'year': [2020, 2021, 2022, 2023],
                'messiGoals': [25, 30, 35, 40],
                'ronaldoGoals': [30, 35, 25, 20]
            })
        }