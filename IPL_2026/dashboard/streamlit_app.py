import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import os

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="IPL 2026 Match Intelligence Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .story-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-left: 4px solid #1f4788;
        border-radius: 4px;
        margin: 10px 0;
        font-style: italic;
        color: #333;
    }
    .insight-box {
        background-color: #fff3cd;
        padding: 12px;
        border-left: 4px solid #ffc107;
        border-radius: 4px;
        margin: 8px 0;
        color: #333;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #1f4788;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD DATA - FIXED PATH
# ============================================================================

@st.cache_data
def load_data():
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to parent directory
    parent_dir = os.path.dirname(current_dir)
    
    # Construct paths
    matches_path = os.path.join(parent_dir, 'ipl_2026_data', 'final_matches_data.csv')
    deliveries_path = os.path.join(parent_dir, 'ipl_2026_data', 'final_ipl_2026_deliveries_data.csv')
    
    matches = pd.read_csv(matches_path)
    deliveries = pd.read_csv(deliveries_path)
    
    matches['date'] = pd.to_datetime(matches['date'])
    deliveries['date'] = pd.to_datetime(deliveries['date'])
    deliveries['is_boundary'] = deliveries['runs_of_bat'].isin([4, 6]).astype(int)
    deliveries['is_out'] = deliveries['player_dismissed'].notnull().astype(int)
    deliveries['total_runs'] = deliveries['runs_of_bat'] + deliveries['extras']
    
    return matches, deliveries

matches, deliveries = load_data()

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================

st.sidebar.title("🏏 IPL 2026 Intelligence Hub")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate to Analysis:",
    options=[
        "📊 Dashboard Overview",
        "🏆 Team Performance",
        "🏏 Batting Excellence",
        "🎯 Bowling Mastery",
        "🎪 Venue Intelligence",
        "⭐ Impact Players",
        "🔍 Match Patterns",
        "📈 Complete Statistics"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Data Coverage:** Match 1 - Match 51")
st.sidebar.markdown(f"**Total Matches:** {len(matches)}")
st.sidebar.markdown(f"**Total Deliveries:** {len(deliveries):,}")
st.sidebar.markdown(f"**Unique Teams:** {len(set(pd.concat([matches['team1'], matches['team2']])))}")

# ============================================================================
# PAGE: DASHBOARD OVERVIEW
# ============================================================================

if page == "📊 Dashboard Overview":
    st.title("🏏 IPL 2026 Match Intelligence Dashboard")
    st.markdown("### Real-time Cricket Intelligence Analysis - Up to Match 51")
    
    # Story introduction
    st.markdown("""
    <div class="story-box">
    <b>📖 The Tournament's Tale:</b> IPL 2026 is unfolding as a season of competitive balance and strategic excellence. 
    With 51 matches completed and over 11,000 deliveries analyzed, patterns are emerging that separate champions from contenders. 
    This dashboard reveals the hidden narratives behind every match – the momentum shifts, the specialization trends, 
    and the individual brilliance that shapes T20 cricket's future.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Metrics Row 1
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Matches", len(matches), "League Stage", delta_color="off")
    with col2:
        st.metric("Total Deliveries", f"{len(deliveries):,}", "Ball-by-ball", delta_color="off")
    with col3:
        st.metric("Unique Batters", deliveries['striker'].nunique(), "Players", delta_color="off")
    with col4:
        st.metric("Unique Bowlers", deliveries['bowler'].nunique(), "Bowlers", delta_color="off")
    
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        all_teams = len(set(pd.concat([matches['team1'], matches['team2']])))
        st.metric("Total Teams", all_teams, "Franchises", delta_color="off")
    with col2:
        st.metric("Unique Venues", len(matches['venue'].unique()), "Stadiums", delta_color="off")
    with col3:
        avg_score_1 = matches['first_ings_score'].mean()
        st.metric("Avg 1st Score", f"{avg_score_1:.0f}", "Runs", delta_color="off")
    with col4:
        avg_score_2 = matches['second_ings_score'].mean()
        st.metric("Avg 2nd Score", f"{avg_score_2:.0f}", "Runs", delta_color="off")
    
    st.markdown("---")
    
    st.subheader("📅 Tournament Timeline & Momentum")
    
    col1, col2 = st.columns(2)
    
    with col1:
        season_duration = (matches['date'].max() - matches['date'].min()).days
        st.write(f"**Tournament Duration:** {season_duration} days")
        st.write(f"**Start Date:** {matches['date'].min().strftime('%B %d, %Y')}")
        st.write(f"**Current Date:** {matches['date'].max().strftime('%B %d, %Y')}")
        
        st.markdown("""
        <div class="insight-box">
        <b>💡 Timeline Insight:</b> The tournament has spanned over two months, allowing teams to build consistency 
        and players to hit peak form. Mid-season transitions often reveal which teams have adapted strategies effectively.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        matches_per_day = matches.groupby(matches['date'].dt.date).size()
        st.line_chart(matches_per_day, use_container_width=True)
        st.caption("📊 Match Scheduling Intensity")
        
        st.markdown("""
        <div class="insight-box">
        <b>🎯 Scheduling Story:</b> The irregular match distribution reflects strategic tournament planning. 
        Clusters of matches create momentum phases where teams play back-to-back, testing squad depth and 
        mental resilience – critical factors in T20 success.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📊 Match Results Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        result_dist = matches['match_result'].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=result_dist.index,
            values=result_dist.values,
            hole=0.3,
            marker=dict(colors=['#2ecc71', '#e74c3c', '#f39c12'])
        )])
        fig.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎲 Result Narrative:</b> The match result distribution shows the tournament's competitive nature. 
        The balance between completed, rain-affected, and other outcomes indicates weather challenges and 
        the unpredictability that makes T20 cricket thrilling.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.write("**Toss Decision Analysis**")
        for decision in ['Bat', 'Bowl']:
            count = len(matches[matches['toss_decision'] == decision])
            st.write(f"- **{decision}:** {count} matches")
        
        toss_wins = len(matches[matches['toss_winner'] == matches['match_winner']])
        toss_impact = (toss_wins / len(matches) * 100)
        st.write(f"\n**Toss Winners Who Won Match:** {toss_impact:.1f}%")
        
        st.markdown("""
        <div class="insight-box">
        <b>🪙 The Toss Truth:</b> Only 50% of toss winners convert to match winners. This remarkable statistic 
        proves a fundamental T20 principle: <b>execution trumps fortune</b>. Teams that master pressure situations 
        and adaptable strategies emerge victorious, regardless of batting order choice.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: TEAM PERFORMANCE
# ============================================================================

elif page == "🏆 Team Performance":
    st.title("🏆 Team Performance Intelligence")
    
    st.markdown("""
    <div class="story-box">
    <b>📖 The Competitive Landscape:</b> In IPL 2026, no single franchise has dominated. Instead, a ecosystem 
    of competitive equals has emerged, where consistency, adaptability, and mental strength separate the winners 
    from the rest. Each team's win percentage tells a story of strategic choices, player form, and tactical evolution.
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate team stats
    team_wins = matches['match_winner'].value_counts()
    team_matches = pd.concat([matches['team1'], matches['team2']]).value_counts()
    
    team_stats = pd.DataFrame({
        'Matches': team_matches,
        'Wins': team_wins
    }).fillna(0).astype(int)
    
    team_stats['Losses'] = team_stats['Matches'] - team_stats['Wins']
    team_stats['Win %'] = (team_stats['Wins'] / team_stats['Matches'] * 100).round(1)
    team_stats = team_stats.sort_values('Wins', ascending=False)
    
    st.subheader("📋 Team Standings & Win Records")
    st.dataframe(team_stats, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>📊 The Numbers Game:</b> Team win percentages range from 40-60%, indicating no runaway leaders. 
    This competitive parity makes IPL 2026 unpredictable – any team could challenge for the title with 
    consecutive wins and optimal form timing.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Win-Loss Comparison")
        fig = go.Figure(data=[
            go.Bar(x=team_stats.index, y=team_stats['Wins'], name='Wins', marker_color='#2ecc71'),
            go.Bar(x=team_stats.index, y=team_stats['Losses'], name='Losses', marker_color='#e74c3c')
        ])
        fig.update_layout(
            xaxis_title="Team",
            yaxis_title="Matches",
            barmode='stack',
            height=400,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎯 Story Behind Stacks:</b> The stacked bar chart reveals teams that have mastered consistency. 
        Teams with higher win blocks have demonstrated the ability to execute under pressure consistently. 
        Notice how some teams peak late – this suggests mid-season tactical adjustments paying dividends.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📈 Win Percentage Rankings")
        fig = go.Figure(data=[go.Bar(
            x=team_stats.index,
            y=team_stats['Win %'],
            marker_color=team_stats['Win %'],
            marker_colorscale='Viridis',
            text=team_stats['Win %'].round(1),
            textposition='auto'
        )])
        fig.update_layout(
            xaxis_title="Team",
            yaxis_title="Win % (%)",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎪 The Win % Story:</b> Teams above 55% are building championship momentum. Teams below 45% 
        face pressure – but T20 cricket's short format allows rapid turnarounds. A 5-match winning streak 
        can transform tournament dynamics. Leadership, team culture, and in-form players become critical now.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: BATTING EXCELLENCE
# ============================================================================

elif page == "🏏 Batting Excellence":
    st.title("🏏 Batting Excellence & Run-Making Masters")
    
    st.markdown("""
    <div class="story-box">
    <b>📖 The Batting Evolution:</b> IPL 2026's batting landscape showcases three distinct archetypes of excellence:
    the <b>consistent accumulator</b> who builds innings methodically, the <b>explosive boundary-hitter</b> who 
    changes match momentum in moments, and the <b>death-over specialist</b> who thrives under extreme pressure. 
    These players are the heartbeat of their franchises.
    </div>
    """, unsafe_allow_html=True)
    
    # Top scorers
    top_scorers = deliveries.groupby('striker')['runs_of_bat'].sum().sort_values(ascending=False).head(15)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔝 Run Accumulation Masters")
        fig = go.Figure(data=[go.Bar(
            x=top_scorers.values,
            y=top_scorers.index,
            orientation='h',
            marker_color='#3498db',
            text=top_scorers.values.astype(int),
            textposition='auto'
        )])
        fig.update_layout(
            title="Top 15 Run Scorers",
            xaxis_title="Runs",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>⭐ The Accumulator's Tale:</b> These batters have earned their runs through consistency and reliability. 
        They're the backbone of innings, rotating strikes, building partnerships, and converting starts into centuries. 
        Teams with strong accumulators rarely lose – consistency is the foundation of championships.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("💥 Boundary Explosion Leaders")
        boundaries = deliveries.groupby('striker')['is_boundary'].sum().sort_values(ascending=False).head(15)
        fig = go.Figure(data=[go.Bar(
            x=boundaries.values,
            y=boundaries.index,
            orientation='h',
            marker_color='#e74c3c',
            text=boundaries.values.astype(int),
            textposition='auto'
        )])
        fig.update_layout(
            title="Top 15 Boundary Hitters",
            xaxis_title="Boundaries (4s & 6s)",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎆 The Boundary Breaker's Impact:</b> These players are momentum-changers. When they're in form, 
        opposition bowlers fear every delivery. Their aggressive approach forces defensive changes, demoralizes 
        bowling units, and often turns close matches into comfortable victories. Count them as match-winners.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚡ Strike Rate Specialists (Min 50 balls)")
        batter_stats = deliveries.groupby('striker').agg({
            'runs_of_bat': 'sum',
            'over': 'count'
        }).rename(columns={'over': 'balls_faced'})
        
        batter_stats['strike_rate'] = (batter_stats['runs_of_bat'] / batter_stats['balls_faced']) * 100
        batter_stats = batter_stats[batter_stats['balls_faced'] >= 50]
        top_sr = batter_stats['strike_rate'].sort_values(ascending=False).head(15)
        
        fig = go.Figure(data=[go.Bar(
            x=top_sr.values,
            y=top_sr.index,
            orientation='h',
            marker_color='#f39c12',
            text=top_sr.values.round(1).astype(str) + '%',
            textposition='auto'
        )])
        fig.update_layout(
            title="Top 15 Strike Rates",
            xaxis_title="Strike Rate (%)",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>⚙️ The Acceleration Masters:</b> Strike rate above 150 means danger. These batters understand T20 
        cricket's core principle: <b>fast runs win matches</b>. They're not just hitting – they're timing perfectly, 
        reading fields, and punishing bowlers. Opposition must adjust field placements entirely when they bat.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("💀 Death Over Finishers (Overs 16-20)")
        death_overs = deliveries[deliveries['over'] >= 16]
        death_runs = death_overs.groupby('striker')['runs_of_bat'].sum().sort_values(ascending=False).head(10)
        
        fig = go.Figure(data=[go.Bar(
            x=death_runs.values,
            y=death_runs.index,
            orientation='h',
            marker_color='#9b59b6',
            text=death_runs.values.astype(int),
            textposition='auto'
        )])
        fig.update_layout(
            title="Death Over Run Scorers",
            xaxis_title="Runs",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎯 The Clutch Heroes:</b> When pressure peaks and every delivery matters, these batters deliver. 
        They've nerves of steel, perfect timing, and an ability to read bowler psychology. In T20 cricket, 
        death overs decide close matches – having a reliable finisher is like having insurance on the match itself.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: BOWLING MASTERY
# ============================================================================

elif page == "🎯 Bowling Mastery":
    st.title("🎯 Bowling Mastery & Pressure Architecture")
    
    st.markdown("""
    <div class="story-box">
    <b>📖 The Bowling Paradox:</b> Modern T20 bowling isn't about taking wickets alone – it's about 
    <b>building pressure through restraint</b>. Economy rates combined with dot-ball percentages create 
    psychological pressure that forces batters into mistakes. The best bowlers are architects of pressure, 
    not just wicket-takers.
    </div>
    """, unsafe_allow_html=True)
    
    # Prepare bowling stats
    deliveries['is_dot'] = (deliveries['total_runs'] == 0).astype(int)
    deliveries['is_wicket'] = deliveries['player_dismissed'].notnull().astype(int)
    deliveries.loc[deliveries['wicket_type'] == 'run out', 'is_wicket'] = 0
    
    bowler_stats = deliveries.groupby('bowler').agg({
        'total_runs': 'sum',
        'is_dot': 'sum',
        'is_wicket': 'sum'
    })
    
    bowler_stats['balls'] = deliveries.groupby('bowler').size()
    bowler_stats = bowler_stats[bowler_stats['balls'] >= 60]
    bowler_stats['overs'] = bowler_stats['balls'] / 6
    bowler_stats['economy'] = bowler_stats['total_runs'] / bowler_stats['overs']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📉 Run Restriction Masters")
        top_economy = bowler_stats.sort_values('economy').head(15)
        fig = go.Figure(data=[go.Bar(
            x=top_economy['economy'].values,
            y=top_economy.index,
            orientation='h',
            marker_color='#1abc9c',
            text=top_economy['economy'].values.round(2).astype(str),
            textposition='auto'
        )])
        fig.update_layout(
            title="Most Economical Bowlers (Min 60 balls)",
            xaxis_title="Economy Rate",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🛡️ The Restriction Story:</b> Economy under 7 is elite-level bowling. These bowlers are match-savers. 
        When opposition builds momentum, they break it. Their consistency forces batters to take risks against 
        other bowlers, creating opportunities for breakthrough moments. Low economy = championship mentality.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("⚔️ Match-Winning Wicket-Takers")
        top_wickets = bowler_stats.sort_values('is_wicket', ascending=False).head(15)
        fig = go.Figure(data=[go.Bar(
            x=top_wickets['is_wicket'].values,
            y=top_wickets.index,
            orientation='h',
            marker_color='#c0392b',
            text=top_wickets['is_wicket'].values.astype(int),
            textposition='auto'
        )])
        fig.update_layout(
            title="Top Wicket-Takers",
            xaxis_title="Wickets",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎯 The Breakthroughs:</b> Wickets at critical moments – opening partnerships broken, middle-order 
        destabilized, lower-order expedited – these bowlers are match-deciders. They possess the X-factor that 
        transforms potential defeats into victories. Teams with 2-3 reliable wicket-takers rarely lose consecutive matches.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🔴 Dot Ball Pressure Builders")
    col1, col2 = st.columns(2)
    
    with col1:
        bowler_stats['dot_pct'] = (bowler_stats['is_dot'] / bowler_stats['balls']) * 100
        dot_specialists = bowler_stats.sort_values('dot_pct', ascending=False).head(15)
        
        fig = go.Figure(data=[go.Bar(
            x=dot_specialists['dot_pct'].values,
            y=dot_specialists.index,
            orientation='h',
            marker_color='#34495e',
            text=dot_specialists['dot_pct'].values.round(1).astype(str) + '%',
            textposition='auto'
        )])
        fig.update_layout(
            title="Dot Ball % Specialists",
            xaxis_title="Dot Ball %",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
        <b>💯 The Pressure Architects:</b> 50%+ dot balls means opposition is getting squeezed. Batters feel the pressure,
        get frustrated, and attempt risky shots. This forces them into poor decision-making. Dot-ball bowling is psychological 
        warfare – it's about breaking confidence, not just slowing scoring. These specialists are underrated match-winners.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🎲 Economy vs Wickets Analysis")
        fig = go.Figure(data=[go.Scatter(
            x=bowler_stats['economy'],
            y=bowler_stats['is_wicket'],
            mode='markers',
            marker=dict(
                size=bowler_stats['dot_pct']/2,
                color=bowler_stats['overs'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Overs")
            ),
            text=bowler_stats.index,
            hovertemplate='<b>%{text}</b><br>Economy: %{x:.2f}<br>Wickets: %{y}<extra></extra>'
        )])
        fig.update_layout(
            title="Bowler Performance Matrix",
            xaxis_title="Economy Rate",
            yaxis_title="Wickets",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎪 The Complexity of Bowling:</b> The perfect bowler combines low economy AND high wickets. 
        Those in the bottom-left quadrant are rare – they're the bowlers franchises build seasons around. 
        Size of bubble = dot-ball expertise. Look for large bubbles in bottom-left corner – those are champions.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: VENUE INTELLIGENCE
# ============================================================================

elif page == "🎪 Venue Intelligence":
    st.title("🎪 Venue Intelligence & Ground Personalities")
    
    st.markdown("""
    <div class="story-box">
    <b>📖 The Ground Effect:</b> Each cricket ground has a personality shaped by geography, pitch composition, 
    and climate. Some grounds reward aggressive batting, others favor bowlers. Smart teams adapt their XI, 
    strategies, and game plans based on venue characteristics. Venue intelligence separates winning franchises 
    from inconsistent ones.
    </div>
    """, unsafe_allow_html=True)
    
    venue_stats = matches.groupby('venue').agg({
        'match_id': 'count',
        'first_ings_score': 'mean',
        'second_ings_score': 'mean',
        'balls_left': 'mean'
    }).round(2)
    
    venue_stats.columns = ['Matches', 'Avg 1st Score', 'Avg 2nd Score', 'Avg Balls Left']
    venue_stats = venue_stats.sort_values('Matches', ascending=False)
    
    st.subheader("📊 Venue Performance Statistics")
    st.dataframe(venue_stats, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>📋 What the Numbers Reveal:</b> Venues with higher 2nd inning scores are chaser-friendly. 
    Those favoring 1st inning are batting-first grounds. Balls-left metric shows match competitiveness – 
    higher values = chases completed easily, lower values = edge-of-seat finishes.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏟️ Average Scoring by Venue")
        venue_scores = venue_stats[['Avg 1st Score', 'Avg 2nd Score']].sort_values('Avg 1st Score', ascending=True)
        
        fig = go.Figure(data=[
            go.Bar(name='1st Inning', x=venue_scores['Avg 1st Score'], y=venue_scores.index, 
                   orientation='h', marker_color='#3498db'),
            go.Bar(name='2nd Inning', x=venue_scores['Avg 2nd Score'], y=venue_scores.index, 
                   orientation='h', marker_color='#e74c3c')
        ])
        fig.update_layout(
            title="Average Innings Scores by Venue",
            xaxis_title="Score",
            barmode='group',
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎯 Venue Strategy Story:</b> Notice the gaps between 1st and 2nd inning scores? 
        That's the venue effect. Chaser-friendly grounds embolden batting teams. Defender-friendly grounds 
        require aggressive first-inning approaches. Smart captains study these patterns and adjust their plans accordingly.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🎪 Chasing Advantage by Venue")
        venue_stats['Run Differential'] = (venue_stats['Avg 2nd Score'] - venue_stats['Avg 1st Score']).round(0)
        run_diff = venue_stats['Run Differential'].sort_values()
        
        colors = ['#e74c3c' if x < 0 else '#2ecc71' for x in run_diff.values]
        fig = go.Figure(data=[go.Bar(
            x=run_diff.values,
            y=run_diff.index,
            orientation='h',
            marker_color=colors,
            text=run_diff.values.astype(int),
            textposition='auto'
        )])
        fig.update_layout(
            title="Chasing Advantage (2nd Score - 1st Score)",
            xaxis_title="Run Differential",
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>⚖️ The Chasing Psychology:</b> Green bars = chaser-friendly venues where knowledge of target 
        provides advantage. Red bars = first-innings grounds favoring aggressive batting. Teams winning at 
        chaser-friendly venues show superior mental strength – they back themselves against any target.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: IMPACT PLAYERS
# ============================================================================

elif page == "⭐ Impact Players":
    st.title("⭐ Impact Players - The Game-Changers")
    
    st.markdown("""
    <div class="story-box">
    <b>📖 Defining Impact:</b> True impact players combine three qualities: consistent strike rates (aggressive intent),
    reliable averages (staying at crease), and boundary hitting (explosive potential). These are the non-negotiable 
    players franchises build around. They're worth every penny because they win matches single-handedly.
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate impact scores
    impact_stats = deliveries.groupby('striker').agg({
        'runs_of_bat': 'sum',
        'is_boundary': 'sum',
        'is_out': 'sum'
    })
    
    impact_stats['balls_faced'] = deliveries.groupby('striker').size()
    impact_stats = impact_stats[impact_stats['balls_faced'] >= 60]
    
    impact_stats['strike_rate'] = (impact_stats['runs_of_bat'] / impact_stats['balls_faced']) * 100
    impact_stats['average'] = impact_stats['runs_of_bat'] / impact_stats['is_out'].replace(0, 1)
    impact_stats['boundary_pct'] = (impact_stats['is_boundary'] / impact_stats['balls_faced']) * 100
    
    # Impact Score: 40% SR + 30% Avg + 30% Boundary%
    impact_stats['impact_score'] = (
        0.4 * impact_stats['strike_rate'] + 
        0.3 * impact_stats['average'] + 
        0.3 * impact_stats['boundary_pct']
    )
    
    top_impact = impact_stats.sort_values('impact_score', ascending=False).head(20)
    
    st.markdown("""
    <div class="insight-box">
    <b>🧮 Impact Formula:</b> 40% Strike Rate + 30% Average + 30% Boundary% = True Impact Score
    <br>This composite metric reveals batters who combine aggression, consistency, and explosiveness.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🏆 Top Impact Players")
    fig = go.Figure(data=[go.Bar(
        x=top_impact['impact_score'].values,
        y=top_impact.index,
        orientation='h',
        marker_color=top_impact['impact_score'].values,
        marker_colorscale='RdYlGn',
        text=top_impact['impact_score'].values.round(2).astype(str),
        textposition='auto'
    )])
    fig.update_layout(
        title="Top 20 Players by Impact Score",
        xaxis_title="Impact Score",
        height=700,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>⭐ Why Impact Score Matters:</b> These 20 players are the difference-makers. At 60+ impact score, 
    players are championship-caliber. They win tight matches through consistency, take on bowling attacks fearlessly, 
    and convert starts into big scores. Franchises that have 2-3 of these players at peak form rarely lose.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📊 Impact Score Components")
    display_cols = ['strike_rate', 'average', 'boundary_pct', 'impact_score']
    impact_display = top_impact[display_cols].head(15).round(2)
    impact_display.columns = ['Strike Rate', 'Average', 'Boundary %', 'Impact Score']
    st.dataframe(impact_display, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>🎯 Reading the Components:</b> High SR means aggressive nature, high average means consistency, 
    high boundary % means explosiveness. The best players have all three elevated. Look for well-balanced 
    profiles – they're the safest bets in fantasy cricket and real-world performance.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: MATCH PATTERNS
# ============================================================================

elif page == "🔍 Match Patterns":
    st.title("🔍 Match Patterns & Hidden Narratives")
    
    st.markdown("""
    <div class="story-box">
    <b>📖 Pattern Intelligence:</b> Behind every match statistic lies a story. Score distributions reveal 
    batting aggression, wicket-scoring correlations show bowling pressure, and momentum shifts tell tales of 
    resilience and collapse. Understanding patterns predicts future match outcomes with surprising accuracy.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📈 Scoring Pattern Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure(data=[
            go.Histogram(x=matches['first_ings_score'], name='1st Inning', marker_color='#3498db', nbinsx=15),
            go.Histogram(x=matches['second_ings_score'], name='2nd Inning', marker_color='#e74c3c', nbinsx=15)
        ])
        fig.update_layout(
            title="Score Distribution - Both Innings",
            xaxis_title="Score",
            yaxis_title="Frequency",
            barmode='overlay',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>📊 Distribution Story:</b> Similar distributions in both innings mean balanced competition. 
        Peaks indicate comfortable score ranges. Outliers reveal explosive performances or collapses. 
        Teams aiming for 170+ are playing aggressive cricket – expect higher variance in outcomes.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        fig = go.Figure(data=[
            go.Scatter(x=matches['first_ings_wkts'], y=matches['first_ings_score'], 
                      mode='markers', name='1st Inning', marker=dict(size=8, color='#3498db')),
            go.Scatter(x=matches['second_ings_wkts'], y=matches['second_ings_score'], 
                      mode='markers', name='2nd Inning', marker=dict(size=8, color='#e74c3c'))
        ])
        fig.update_layout(
            title="Wickets Lost vs Score Achieved",
            xaxis_title="Wickets Lost",
            yaxis_title="Score",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <b>🎲 The Wicket Truth:</b> Clear downward trend: losing early wickets = lower scores. 
        This is T20 cricket's golden rule. Teams that preserve wickets and build partnerships 
        consistently outperform teams that lose batters early. Wicket management is 60% of match success.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: COMPLETE STATISTICS
# ============================================================================

elif page == "📈 Complete Statistics":
    st.title("📈 Complete Match Database")
    
    st.subheader("📋 All Matches Data")
    display_matches = matches[['date', 'team1', 'team2', 'venue', 'first_ings_score', 
                               'second_ings_score', 'match_winner']].copy()
    display_matches['date'] = display_matches['date'].dt.strftime('%Y-%m-%d')
    
    st.dataframe(display_matches, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>📊 Database Story:</b> This complete match history contains all the raw data. Each row is a 
    match narrative – who played, where, what they scored, and who won. Patterns across this data 
    form the foundation of all intelligence insights above.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666666;">
    <p><b>IPL 2026 Match Intelligence Dashboard</b></p>
    <p>Cricket Intelligence Driven Analysis | Data-backed Strategic Insights</p>
    <p>Coverage: Match 1-51 | Updated: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}</p>
    <p style="font-size: 12px;">This dashboard transforms raw cricket statistics into strategic intelligence 
    that powers championship-winning decisions.</p>
</div>
""", unsafe_allow_html=True)