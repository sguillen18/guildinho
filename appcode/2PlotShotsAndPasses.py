#Make a shot map and a pass map using Statsbomb data
#Set match id in match_id_required.
#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np
import json

#Draw the pitch
from FCPython import createPitch
#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','black')


#ID for Barcelona vs Osasuna in La Liga
match_id_required = 68318
home_team_required ="Barcelona"
away_team_required ="Osasuna"

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
file_name=str(match_id_required)+'.json'

#Load in all match events 
with open('open-data-master/data/events/'+file_name) as data_file:
        #print mypath+'events'+file
        data=json.load(data_file)

#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

# #A dataframe of lineups
# lineups = df.loc[df['type_name'] == 'Starting XI'].set_index('id')

# #Print Lineups
# for i,startinglineup in lineups.iterrows():
#         eleven=startinglineup['tactics_lineup']
#         print(eleven)

#A dataframe of passes
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

#Plot the passes for the home team (barcelona)
for i,singlepass in passes.iterrows():
        x=singlepass['location'][0]
        y=singlepass['location'][1]
        passingplayer=singlepass['player_name']
        xe=singlepass['pass_end_location'][0]
        ye=singlepass['pass_end_location'][1]
        
        
        
        team_name=home_team_required
        circleSize=0.5
        if "Lionel Andrés Messi Cuccittini" in passingplayer:
            #printedplayer=passingplayer
            passCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")
            endpassCircle=plt.Circle((xe, pitchWidthY-ye),circleSize,color="red")
            
            passline=plt.arrow(x, pitchWidthY-y, xe-x, -(ye-y), color="gray")
            #ax.arrow(x,pitchWidthY-y,xe-x,pitchWidthY-ye)
            #plot pass direction
            ax.add_patch(passCircle)
            ax.add_patch(passline)
        

#A dataframe of shots
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
    
#Plot the shots
for i,shot in shots.iterrows():
    x=shot['location'][0]
    y=shot['location'][1]
    
    shootingplayer=shot['player_name']
    goal=shot['shot_outcome_name']=='Goal'
    team_name=shot['team_name']
    
    circleSize=np.sqrt(shot['shot_statsbomb_xg'])*7
    
    if "Lionel Andrés Messi Cuccittini" in shootingplayer:
        printedplayer=shootingplayer
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            plt.text((x+1),pitchWidthY-y+1,shot['player_name'])
            ax.add_patch(shotCircle)
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")     
            shotCircle.set_alpha(.3)
            ax.add_patch(shotCircle)
        

    # if (team_name==home_team_required):
    #     if goal:
    #         shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
    #         plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
    #     else:
    #         shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
    #         shotCircle.set_alpha(.2)
    # elif (team_name==away_team_required):
    #     if goal:
    #         shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
    #         plt.text((pitchLengthX-x+1),y+1,shot['player_name']) 
    #     else:
    #         shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")      
    #         shotCircle.set_alpha(.2)
    
    

finalplayer=printedplayer.split()
plt.text(1,75,finalplayer[0] + ' ' +finalplayer[2] + ' shots and passes',color="black") 
     
fig.set_size_inches(10, 7)
#fig.savefig('Output/shots.pdf', dpi=100) 
plt.show()

#Exercise: 
#1, Create a dataframe of passes which contains all the passes in the match
#2, Plot the start point of every Barcelona pass. Attacking left to right.
#3, Plot only passes made by Xavi
#4, Plot arrows to show where the passes were

