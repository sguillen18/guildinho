#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:39:31 2022

@author: sean.guillen
"""

to plot shots and passes for a player, the function will need the comp id,
 match id, home or away team, player name
 
match_file_name has the path to the game we want to open, just use that instead of passing both
comp and matchid

and events_file_name will bypass comp and match_id to get right to what we want

also need selected_match_id which is the events variable to normalize the data for 
plotting passes and shots
 
def plotShotsAndPasses (events_file_name, selected_match_id, select_team, player_name)