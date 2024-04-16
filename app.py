
#importing the libraries used for analytics
import streamlit as st
from streamlit import *
import pandas as pd
import numpy as np
from PIL import Image
#Title of the project
st.title("IPL Analytics")
image = Image.open(r"C:\Users\arsha\Downloads\ipl-2024-venue.webp")
st.image(image)
st.markdown("The Indian Premier League (IPL) is a professional Twenty20 cricket league played in India")

#Loading the data from csv files to make dataframes with them 
# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Season wise winners"])

if page == "Home":
    st.subheader("Objective:")
    st.write("The Indian Premier League (IPL), also known as the TATA IPL for sponsorship reasons, is a men's Twenty20 (T20) cricket league held annually in India. Founded by the BCCI in 2007, the league features ten city-based franchise teams. The IPL usually takes place during the summer, between March and May each year. It has an exclusive window in the ICC Future Tours Programme, resulting in fewer international cricket tours occurring during the IPL seasons")
    st.subheader("Content:")
    st.write("The Streamlit dashboard for IPL cricket analysis provides an immersive experience for enthusiasts keen on exploring the intricacies of one of the world's most popular cricket leagues. By leveraging comprehensive match data spanning multiple seasons, the dashboard offers insights into team dynamics, player performances, and match outcomes. Users can delve into season-wise winners, analyze individual player statistics, and track dismissal types to gain a deeper understanding of the game. With interactive visualizations and customizable filters, the dashboard empowers users to uncover trends, compare player performances, and derive actionable insights, enhancing their enjoyment and understanding of IPL cricket.")

def load_data():
    data=pd.read_csv(r"C:\Users\arsha\Downloads\IPL Matches 2008-2020.csv")
    return data
matches_df=load_data()
def load_data():
    data1=pd.read_csv(r"C:\Users\arsha\Downloads\cleaned.csv")
    return data1
ball2ball_df=load_data()
#Season_wise_winners
#from the original matches dataframe using the winner of the last row in every season we got the season_winner.
st.title("Season Wise winners")
df2 = pd.DataFrame(columns = ['Season','winner'],index=None)
for x in matches_df['Season'].unique():
        list = []
        matched = matches_df.loc[matches_df['Season']==x]
        
        last_row = matched.iloc[-1]
        list = [last_row['Season'],last_row['winner']]
        df2.loc[len(df2)] = list
        df2.index = [""] * len(df2)
st.write(df2)
import streamlit as st

# Title of the project
import streamlit as st

# Title of the project
st.title("IPL Analytics")

# Auction information dictionary
auction_info = {
    "2008": "MS Dhoni secured the highest bid for the 2008 season, with an amount of ₹6 crore.",
    "2009": "Kevin Pietersen was the highest-bid player, with a bid of USD 12.5 cr for the Royal Challengers Bangalore.",
    "2010": "Gautam Gambhir fetched the highest bid of USD 2.40 million for the Kolkata Knight Riders.",
    "2011": "Kieron Pollard and Shane Bond both received the highest bid of USD 0.75 million for the Mumbai Indians and Kolkata Knight Riders, respectively.",
    "2012": "Ravindra Jadeja was the most expensive player, with a bid of USD 2.00 million for the Chennai Super Kings.",
    "2013": "Glenn Maxwell secured a bid of USD 1.00 million from the Mumbai Indians.",
    "2014": "Yuvraj Singh was the highest-bid player, with a bid of ₹14.00 crore for the Royal Challengers Bangalore.",
    "2015": "Yuvraj Singh continued his streak, fetching a bid of ₹16.00 crore for the Delhi Daredevils now Delhi Capitals.",
    "2016": "Shane Watson received the highest bid of ₹9.50 crore for the Royal Challengers Bangalore.",
    "2017": "Ben Stokes was the most expensive player, with a bid of ₹14.50 crore for the Rising Pune Supergiant.",
    "2018": "Ben Stokes again topped the charts, securing a bid of ₹12.50 crore for the Rajasthan Royals.",
    "2019": "Varun Chakravarthy and Jaydev Unadkat shared the highest bid of ₹8.40 crore for the Kings XI Punjab and Rajasthan Royals, respectively.",
    "2020": "Pat Cummins became the most expensive player, with a bid of ₹15.5 crore for the Kolkata Knight Riders.",
    "2021": "Chris Morris set a new record, fetching a whopping bid of ₹16.25 crore from the Rajasthan Royals.",
    "2022": "Ishan Kishan emerged as the top player, with a bid of ₹15.25 crore for the Mumbai Indians."
}

# Streamlit app
st.title("Indian Premier League Auction History")

# Create a selectbox to choose a year
selected_year = st.selectbox("Select a year", auction_info.keys())

# Display the auction information for the selected year
st.write(auction_info[selected_year])

#which team won how many times , it is calculated using the same dataframe used for previous stat
st.title("Which Team won Most Titles?")
st.write(df2['winner'].value_counts())
#the winning count of the teams in each individiual season , where season can be selected in the drop down.
st.title("The winning count of the teams in each individiual season")
select11 = st.selectbox('season',matches_df['Season'].unique())
for x in matches_df['Season'].unique():
    list = []
    matched = matches_df.loc[matches_df['Season']==select11]
st.write(matched['winner'].value_counts())
#Dataframe conrtaining the details of winning data of a particular team from the drop down
select = st.selectbox('Select a Team',matches_df['winner'].unique())
team_data = matches_df[matches_df['winner'] == select]
new = team_data[['toss_winner','toss_decision','winner', 'player_of_match','result_margin']].copy()
st.subheader('Toss-win relational dataframe')
if st.button('individual team wins dataframe'):
    new.index = [""] * len(new)
    #the above statement is to remove the unnecessary index at the begining
    st.write(new)
bar_data = team_data[:30]
st.subheader('winning margin ')
#Bar Chart
st.bar_chart(bar_data['result_margin'])
#line chart
df = pd.DataFrame(matches_df[:200], columns = ["result_margin"])
st.line_chart(df)
#Man_of _the_match count of individual player in all seasons
st.title("Man_of _the_match of individual player")
select5 = st.selectbox('player',matches_df['player_of_match'].unique())
man_of_match = matches_df.loc[matches_df['player_of_match']==select5]
st.write(str(man_of_match['player_of_match'].count()))
#Man_of_the_match winners per season 
st.title("Man_of_the_match Winners")
select12 = st.selectbox('season_wise',matches_df['Season'].unique())
for x in matches_df['Season'].unique():
    list = []
    matched = matches_df.loc[matches_df['Season']==select12]
st.write(matched['player_of_match'].value_counts())
#totsl man_of_the_match winners dataframe together
st.title("Total_Man_of _the_match awards")
st.write(matches_df['player_of_match'].value_counts())
#win percentage of teams with respect to ground
st.title("win% in a city")
select6 = st.selectbox('city',matches_df['city'].unique())
select7 = st.selectbox('team',matches_df['winner'].unique())
win_percentage = matches_df.loc[(matches_df['city']==select6)&((matches_df['team1']==select7)|(matches_df['team2']==select7))]
total_matches = win_percentage['city'].count()
win_select = win_percentage.loc[(win_percentage['winner']==select7)&(matches_df['city']==select6)]
total_wins = win_select['city'].count()

a = (total_wins/total_matches)*100
st.write(a)
# one on one stats , if we select a batsman and a bowler , we can get the results of no.of sixes ,fours ,total_runs and wickets against the particular bowler 
st.title("select batsman and bowler for ONE-ONE Stats")
select1 = st.selectbox('Select a batsman',ball2ball_df['batsman'].unique())
select2 = st.selectbox('Select a bowler',ball2ball_df['bowler'].unique())
#get the state selected in the selectbox
raina_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select1) & (ball2ball_df['bowler']==select2)]
wickets_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select1) & (ball2ball_df['bowler']==select2) & (ball2ball_df['is_wicket']==1)]
total = raina_df['batsman_runs'].sum()
sixes_df = raina_df.loc[raina_df['batsman_runs']==6]
shepherd = select2
fours_df = raina_df.loc[raina_df['batsman_runs']==4]
string_in_string = "sixes hit against {}.".format(shepherd)
#st.write(string_in_string)
sixes = sixes_df['batsman_runs'].count()
#st.button(label=string_in_string, key=None, help=None)
st.title("ONE_ONE stats")

import plotly.graph_objects as go

fig1 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = sixes,
    mode = "gauge+number",
    title = {'text': string_in_string},
    
    gauge = {'axis': {'range': [None, 20]},
             'steps' : [
                 {'range': [0, 10], 'color': "lightgray"},
                 {'range': [10, 15], 'color': "gray"}]
             }))
if st.button('Sixes Indicator'):
    st.write(fig1)

string_in_string = "fours hit against {}.".format(shepherd)
fours = fours_df['batsman_runs'].count()
fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = fours,
    mode = "gauge+number",
    title = {'text': string_in_string},
    
    gauge = {'axis': {'range': [None, 20]},
             'steps' : [
                 {'range': [0, 10], 'color': "lightgray"},
                 {'range': [10, 15], 'color': "gray"}]
             }))
if st.button('Fours Indicator'):
    st.write(fig2)
#st.write(string_in_string)
#st.write(fours_df['batsman_runs'].count())
shepherd = select2
string_in_string = "total runs scored against {}.".format(shepherd)
fig3 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = total,
    mode = "gauge+number",
    title = {'text': string_in_string},
    
    gauge = {'axis': {'range': [None, 200]},
             'steps' : [
                 {'range': [0, 100], 'color': "lightgray"},
                 {'range': [100, 150], 'color': "gray"}]
             }))
if st.button('Total_runs Indicator'):
    st.write(fig3)
string_in_string = "outs against {}.".format(shepherd)
wickets = wickets_df['batsman_runs'].count()
fig4 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = wickets,
    mode = "gauge+number",
    title = {'text': string_in_string},
    
    gauge = {'axis': {'range': [None, 20]},
             'steps' : [
                 {'range': [0, 10], 'color': "lightgray"},
                 {'range': [10, 15], 'color': "gray"}]
             }))
if st.button('Wickets Indicator'):
    st.write(fig4)
#Boundary count of a individual player in all seasons combined .
st.title("Boundary Count")
select3 = st.selectbox('Select batsman',ball2ball_df['batsman'].unique())
ballsperboundary1_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select3)&(ball2ball_df['batsman_runs']==6)]
ballsperboundary2_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select3)&(ball2ball_df['batsman_runs']==4)]
shepherd1 = select3
string_in_string = "total boundaries scored by {}.".format(shepherd1)
boundaries = ballsperboundary1_df['batsman_runs'].count() + ballsperboundary2_df['batsman_runs'].count()
st.title(string_in_string)
st.write(str(boundaries))
#No.of balls that a batsman take for scoring a boundary .
st.title("Balls per boundary")
select4 = st.selectbox('batsman',ball2ball_df['batsman'].unique())
individual = ball2ball_df.loc[ball2ball_df['batsman']==select4]
count = 0
sum = 0
list = []
for x in individual['batsman_runs']:
    if (x<4):
        count = count + 1
    if(x>=4):
        list.append(count)
        sum = sum + count
        count = 0
avg_balls_for_boundary = sum/len(list)
if st.button("balls per boundary"):
    st.write(str(avg_balls_for_boundary))
import plotly.graph_objects as go
#Total_runs scored by a batsman in the IPL 
st.title("Total Runs in IPL")
select8 = st.selectbox('Total Runs in IPL',ball2ball_df['batsman'].unique())
if st.button("total runs"):
    individual_total = ball2ball_df.loc[ball2ball_df['batsman']==select8]
    count = 0
    sum = 0
    for x in individual_total['batsman_runs']:
        if (x>0):
                count = count + x
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = count,
        mode = "gauge+number",
        title = {'text': "Runs_in_IPL"},
        
        gauge = {'axis': {'range': [None, 6000]},
                'steps' : [
                    {'range': [0, 250], 'color': "lightgray"},
                    {'range': [250, 400], 'color': "gray"}],
                }))
    st.write(fig)
#Batting stats per season ( centuries , fifties , thirties per season )
st.title("batting stats dataframe in all seasons")
select9 = st.selectbox('batsman_stats',ball2ball_df['batsman'].unique())
dff = pd.DataFrame(columns = ['player','centuries', 'fifties','thirties','Season'],index=None)
if st.button("batting_stats_dataframe"):
    for x in ball2ball_df['Season'].unique():
        list=[]
        matched = ball2ball_df.loc[ball2ball_df['Season']==x]
        for y in matched['id'].unique():
            matches = matched.loc[ball2ball_df['id']==y]
            full_dhoni = matches.loc[(matches['batsman']==select9)]
            count =0
            for index, row in full_dhoni.iterrows():
                if(row['batsman']==select9):
                    if(row['batsman_runs']>0):
                        count = count + row['batsman_runs']
            list.append(count)
        centuries = 0
        fifties = 0
        thirties = 0
        for z in list:
            if(z>=100):
                centuries = centuries + 1
            if(z>=50):
                fifties = fifties + 1
            if(z>=30):
                thirties = thirties + 1
        dff1 = pd.DataFrame(columns = ['player','centuries', 'fifties','thirties','Season'],index=None)
        listed = [select9,centuries,fifties,thirties,x]
        dff.loc[len(dff)] = listed
        dff.index = [""] * len(dff)
    st.write(dff)
#Bowling stats per season dataframe for individual bowler
st.title("bowling stats dataframe in all seasons")
select10 = st.selectbox('bowler stats',ball2ball_df['bowler'].unique())
if st.button("bowling_stats_dataframe"):
    dff = pd.DataFrame(columns = ['player','total_wickets', 'five_wicket_hauls','three_wicket_hauls','Season'],index=None)
    for x in ball2ball_df['Season'].unique():
        list=[]
        matched = ball2ball_df.loc[ball2ball_df['Season']==x]
        for y in matched['id'].unique():
            matches = matched.loc[ball2ball_df['id']==y]
            full_dhoni = matches.loc[(matches['bowler']==select10)]
            count =0
            for index, row in full_dhoni.iterrows():
                if(row['bowler']==select10):
                    if((row['is_wicket']==1)and(row['dismissal_kind']!="run out")):
                        count = count + 1
            list.append(count)
        total_wickets = 0
        five_wicket_hauls = 0
        three_wicket_hauls = 0
        total_wickets_count = 0
        for z in list:
            total_wickets_count = total_wickets_count+z
            if(z>=5):
                five_wicket_hauls = five_wicket_hauls + 1
            if(z>=3):
                three_wicket_hauls = three_wicket_hauls + 1
        total_wickets = total_wickets_count
        dff1 = pd.DataFrame(columns = ['player','centuries', 'fifties','thirties','Season'],index=None)
        listed = [select10,total_wickets,five_wicket_hauls,three_wicket_hauls,x]
        dff.loc[len(dff)] = listed
        dff.index = [""] * len(dff)
    st.write(dff)
#dismissal types for a batsman in a season and also total dismissals (types_count)
st.title("dismissal_types")
select13 = st.selectbox('batsman_dismissals',ball2ball_df['batsman'].unique())
select14 = st.selectbox('season_wise_dismissals',matches_df['Season'].unique())
for x in ball2ball_df['Season'].unique():
        list = []
        matched = ball2ball_df.loc[ball2ball_df['Season']==select14]
        kohli = matched.loc[matched['batsman']==select13]
if st.button("dismissal_types"):
    st.write(kohli['dismissal_kind'].value_counts())    
st.title("total_dismissals")
select15 = st.selectbox('batsman_dismissals_total',ball2ball_df['batsman'].unique())

dismissals = ball2ball_df.loc[ball2ball_df['batsman']==select15]
if st.button("total_dismissals"):
    st.write(dismissals['dismissal_kind'].value_counts()) 
st.title("Bowler_type of dismissals")
select16 = st.selectbox('bowler_dismissals_total',ball2ball_df['bowler'].unique())

dismissals = ball2ball_df.loc[ball2ball_df['bowler']==select16]
if st.button("Bowler_type of dismissals"):
    st.write(dismissals['dismissal_kind'].value_counts()) 
select17 = st.selectbox('batsman_dismissals_by bowler',ball2ball_df['batsman'].unique())  
dismissals = ball2ball_df.loc[(ball2ball_df['batsman']==select17)&(ball2ball_df['is_wicket']==1)]
if st.button("batsman_dismissals_by bowler"):
    st.write(dismissals['bowler'].value_counts()) 
#Average of a batsman
st.title("Average of the batsman")
select18 = st.selectbox('average_of_batsman',ball2ball_df['batsman'].unique())  
individual_total = ball2ball_df.loc[ball2ball_df['batsman']==select18]
wickets = ball2ball_df.loc[(ball2ball_df['player_dismissed']==select18)]
count = 0
sum = 0
for x in individual_total['batsman_runs']:
    if (x>0):
        count = count + x
for x in wickets['is_wicket']:
    if(x==1):
        sum = sum + 1
average = count/sum
st.write(average)
#strike_rate of a batsman after particular number of overs
# Note - there are total 20 overs but the count starts from 0.1,0.2 so it ends with 19.5,19.6 , so for selecting above 15 overs , we must select >13 because 13.6 is 14th over .
st.title("strike_rate after no.of overs")
select19 = st.selectbox('strike_rate after 15 overs for a batsman',ball2ball_df['batsman'].unique())
select20 = st.selectbox('over_of _match',ball2ball_df['over'].unique())
above_15 = ball2ball_df.loc[ball2ball_df['over']>select20]
before_15 = ball2ball_df.loc[ball2ball_df['over']<select20]
virat = above_15.loc[above_15['batsman']==select19]
balls = virat['ball'].count()

count = 0
sum = 0
for x in virat['batsman_runs']:
    if (x>0):
        count = count + x

strike_rate = (count/balls)*100
st.write(strike_rate)
st.title("Stats for batsman after 15 overs including their value")
st.markdown("value is calculated as average + strike_rate/100 for every player after 15 overs  {v=average+(strike_rate/100)} ")
dff = pd.DataFrame(columns = ['batsman','batsman_runs','Strike_rate','Average','value'],index=None)
select21 = st.selectbox('',ball2ball_df['batsman'].unique())
after_15 = ball2ball_df.loc[ball2ball_df['over']>13]
kohli = after_15.loc[after_15['batsman']==select21]
scores_list=[]
outs =0
for x in kohli['id'].unique():
    match = kohli.loc[kohli['id']==x]
    full_dhoni = match.loc[(match['batsman']==select21)]
    count =0
    sum = 0
    for index, row in full_dhoni.iterrows():
        if(row['batsman']==select21):
            sum = sum + 1
            if(row['batsman_runs']>0):
                count = count + row['batsman_runs']
            if(row['is_wicket']==1):
                outs = outs + 1
    scores_list.append(count)  
total_scores= 0
for x in scores_list:
    total_scores = total_scores + x
if(outs!=0):
    average = total_scores/outs
if(outs==0):
    average = total_scores
balls = kohli['ball'].count()
count = 0
sum = 0
for x in kohli['batsman_runs']:
    if (x>0):
        count = count + x
strike_rate = (count/balls)*100
Value = average + ((strike_rate)/100) 
listed = [select21,total_scores,strike_rate,average,Value]
dff.loc[len(dff)] = listed
dff.index = [""] * len(dff)
if st.button("Value after 15 overs"):
    st.write(dff)







