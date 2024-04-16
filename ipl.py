import streamlit as st
import pandas as pd

df = pd.read_csv(r"C:\Users\arsha\Downloads\cleaned.csv")

after_15 = df[df['over'] > 13]

# Initialize an empty DataFrame to store the results
columns = ['batsman_runs', 'Strike_rate', 'Average', 'value']
dff = pd.DataFrame(columns=columns)

# Iterate over unique batsmen in the filtered DataFrame
for batsman in after_15['batsman'].unique():
    kohli = after_15[after_15['batsman'] == batsman]
    scores_list = []
    outs = 0
    for match_id in kohli['id'].unique():
        match = kohli[kohli['id'] == match_id]
        full_batsman = match[(match['batsman'] == batsman)]
        count = 0
        for index, row in full_batsman.iterrows():
            if row['batsman_runs'] > 0:
                count += row['batsman_runs']
            if row['is_wicket'] == 1:
                outs += 1
        scores_list.append(count)
    total_scores = sum(scores_list)
    average = total_scores / outs if outs != 0 else total_scores
    balls = kohli['ball'].count()
    runs_scored = kohli['batsman_runs'].sum()
    strike_rate = (runs_scored / balls) * 100
    value = average + (strike_rate / 100)
    dff = pd.concat([dff, pd.DataFrame([[total_scores, strike_rate, average, value]], columns=columns)])

# Sort the DataFrame by 'batsman_runs' and 'value' columns
dff = dff.sort_values(by=['batsman_runs', 'value'], ascending=False)

# Display the results
st.table(dff)






"""
above_15 = df.loc[df['over']>14]
before_15 = df.loc[df['over']<15]
virat = above_15.loc[above_15['batsman']=="V Kohli"]
balls = virat['ball'].count()
print(balls)
count = 0
sum = 0
for x in virat['batsman_runs']:
    if (x>0):
        count = count + x
print(count)
strike_rate = (count/balls)*100
print(strike_rate)

for x in df['Season'].unique():
        list = []
        matched = df.loc[df['Season']==x]
        kohli = matched.loc[matched['batsman']=="V Kohli"]
        print(kohli['dismissal_kind'].value_counts())

for x in df['Season'].unique():
        list = []
        matched = df.loc[df['Season']==x]
        kohli = matched.loc[matched['batsman']=="V Kohli"]
        print(kohli['winner'].value_counts())


dff = pd.DataFrame(columns = ['Season','winner'],index=None)
for x in df['Season'].unique():
        list = []
        matched = df.loc[df['Season']==x]
        df2=dff
        last_row = matched.iloc[-1]
        list = [last_row['Season'],last_row['winner']]
        df2.loc[len(df2)] = list
        df2.index = [""] * len(df2)
print(df2)
print(df2['winner'].value_counts())
for x in df['Season'].unique():
        list = []
        matched = df.loc[df['Season']==x]
        print(matched['winner'].value_counts())
for x in df['Season'].unique():
        list = []
        matched = df.loc[df['Season']==x]
        print(matched['player_of_match'].value_counts())
"""       
        


#toss_importance = df.loc[df['toss_winner']==df['winner']]
#print(df.count())
#raina_df = df.loc[(df["batsman"]=="MS Dhoni") & (df['batsman_runs']==6)]
#ballsperboundary_df = df.loc[(df["batsman"]=="MS Dhoni")&(df['batsman_runs']==4)]
#total = raina_df['batsman_runs'].sum()
#print(total)
#print(raina_df['batsman_runs'].count())
#toss_decision = toss_importance.loc[toss_importance['toss_decision']=="field"]
#print(toss_decision.count())
#mostwins_in_season = df.loc[(df['date']<"2021-01-25") & (df['date']>"2020-01-25")]
#print(mostwins_in_season['winner'].value_counts())
#print(df['city'].value_counts())
#bravo_df = df.loc[(df['bowler']=="DJ Bravo") & (df['extras_type']=="wides")]
#print(bravo_df.count())
#malinga_df = df.loc[(df['bowler']=="SL Malinga") & (df['extras_type']=="wides")]
#print(malinga_df.count())
#wides_df = df.loc[df['winner']=="Kolkata Knight Riders"]
#print(wides_df['bowler'].value_counts())
#print(line.count())
#win_percentage = df.loc[(df['city']=='Chennai')]
#total_matches = win_percentage['city'].count()
#print(total_matches)
#win_select = df.loc[(df['city']=='Chennai')&(df['winner']=="Chennai Super Kings")]
#total_csk = win_select['city'].count()
#print(total_csk)
#a = (total_csk/total_matches)*100
#print(a)

#list =[]
"""for x in df['id'].unique():
    match = df.loc[df['id']==x]
    full_dhoni = match.loc[(match['batsman']=="V Kohli")]
    count =0
    for index, row in full_dhoni.iterrows():
        if(row['batsman']=="V Kohli"):
            if(row['batsman_runs']>0):
                count = count + row['batsman_runs']
    list.append(count)
print(max(list))
centuries = 0
fifties = 0
thirties = 0
for x in list:
    if(x>=100):
        centuries = centuries + 1
    if(x>=50):
        fifties = fifties + 1
    if(x>=30):
        thirties = thirties + 1
dff = pd.DataFrame(columns = ['player','centuries', 'fifties','thirties'],index=None)
dff['player']=['V Kohli']
dff['centuries']=[centuries]
dff['fifties']=[fifties]
dff['thirties']=[thirties]
print(dff.to_string(index=False))

list_totalruns = []
for x in df['Season'].unique():
    match = df.loc[df['Season']==x]
    full_dhoni = match.loc[(match['batsman']=="V Kohli")]
    count =0
    for index, row in full_dhoni.iterrows():
        if(row['batsman']=="V Kohli"):
            if(row['batsman_runs']>0):
                count = count + row['batsman_runs']
    list_totalruns.append(count)
print(list_totalruns)
dff = pd.DataFrame(columns = ['player','centuries', 'fifties','thirties','Season'],index=None)

for x in df['Season'].unique():
    list=[]
    matched = df.loc[df['Season']==x]
    
    for y in matched['id'].unique():
        

        matches = matched.loc[df['id']==y]
        full_dhoni = matches.loc[(matches['batsman']=="V Kohli")]
        count =0
        for index, row in full_dhoni.iterrows():
            if(row['batsman']=="V Kohli"):
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
    listed = ["V Kohli",centuries,fifties,thirties,x]
    dff.loc[len(dff)] = listed
    
print(dff.to_string(index=False)) 

dff = pd.DataFrame(columns = ['player','centuries', 'fifties','thirties','Season'],index=None)
avg = []
sum = 0
len = 0
average = 0
total_runs = 0
total_balls =0    
for x in df['Season'].unique():
    list=[]
    matched = df.loc[df['Season']==x]
    strikerate = []
    

    for y in matched['id'].unique():
            

        matches = matched.loc[df['id']==y]
        full_dhoni = matches.loc[(matches['batsman']=="MS Dhoni")]
        count =0
        balls_count = 0
        for index, row in full_dhoni.iterrows():
            if(row['batsman']=="MS Dhoni"):
                if(row['extras_type']!="wides"):

                    balls_count = balls_count + 1
                if(row['batsman_runs']>0):
                    count = count + row['batsman_runs']
        list.append(count)
        if(balls_count==0):
            continue
        if(balls_count!=0):
            strike_rate = (count/balls_count)*100
            strikerate.append(strike_rate)
        print(count)
        print(balls_count)
        total_runs = total_runs + count
        total_balls= total_balls + balls_count
print(total_runs)
print(total_balls)  
print((total_runs/total_balls)*100) 

avg = []
sum = 0
len = 0
average = 0
total_runs = 0
total_balls =0    
for x in df['Season'].unique():
    list=[]
    matched = df.loc[df['Season']==x]
    strikerate = []
    
    strike_rate_10_list = []
    strike_rate_after10_list=[]
    for y in matched['id'].unique():
            
        strike_rate_after10 =0
        strike_rate_10 = 0
        matches = matched.loc[df['id']==y]
        full_dhoni = matches.loc[(matches['batsman']=="MS Dhoni")]
        count =0
        balls_count = 0
        for index, row in full_dhoni.iterrows():
            if(row['batsman']=="MS Dhoni"):
                while(balls_count<=10):

                    if(row['extras_type']!="wides"):

                        balls_count = balls_count + 1
                    if(row['batsman_runs']>0):
                        count = count + row['batsman_runs']
                if(balls_count!=0):
                    strike_rate_10 = (count/balls_count)*100
                    strike_rate_10_list.append(strike_rate_10)
                balls_count = 0 
                count = 0 
                while(balls_count>10):
                    if(row['extras_type']!="wides"):

                        balls_count = balls_count + 1
                    if(row['batsman_runs']>0):
                        count = count + row['batsman_runs']
                if(balls_count!=0):

                    strike_rate_after10 = (count/balls_count)*100
                    strike_rate_after10_list.append(strike_rate_after10)
                print(strike_rate_after10)
                print(strike_rate_10)
        break
"""

                




