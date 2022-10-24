# standardizeStats.py - Uses Z Scores ((Obs  - Mean) / St Dev.) to standardize any of the different statistics scraped

from nba_api.stats.endpoints import leaguedashteamstats
import statistics
from getStats import getStatsForTeam
import time
from customHeaders import customHeaders

# Finds league mean for the entered basic or advanced statistic (statType = 'Base' or 'Advanced')
# 리그 수치의 중앙값(Mean)을 구함
def basicOrAdvancedStatMean(startDate, endDate, stat,statType = 'Base', season='2018-19'):

    time.sleep(.2)
    # Gets list of dictionaries with stats for every team
    allTeamsInfo = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='Per100Possessions',
                                                           measure_type_detailed_defense=statType,
                                                           date_from_nullable=startDate,
                                                           date_to_nullable=endDate,
                                                           season=season,
                                                           headers=customHeaders,
                                                           timeout=120)
    allTeamsDict = allTeamsInfo.get_normalized_dict()
    '''
    {'LeagueDashTeamStats': [
        {
            'TEAM_ID': 1610612737, 
            'TEAM_NAME': 'Atlanta Hawks', 
            'GP': 65, 
            'W': 35, 
            'L': 30, 
            'W_PCT': 0.538, 
            'MIN': 48.8, 
            'FGM': 40.5, 
            'FGA': 87.6, 
            'FG_PCT': 0.462, 
            'FG3M': 12.5, 
            'FG3A': 33.8, 
            'FG3_PCT': 0.37, 
            'FTM': 20.0, 
            'FTA': 24.6, 
            'FT_PCT': 0.811, 
            'OREB': 10.7, 
            'DREB': 34.9, 
            'REB': 45.7, 
            'AST': 24.0, 
            'TOV': 13.5, 
            'STL': 7.0, 
            'BLK': 4.7, 
            'BLKA': 5.1, 
            'PF': 19.6, 
            'PFD': 20.1, 
            'PTS': 113.4, 
            'PLUS_MINUS': 1.2, 
            'GP_RANK': 1, 
            'W_RANK': 10, 
            'L_RANK': 12, 
            'W_PCT_RANK': 12, 
            'MIN_RANK': 9, 
            'FGM_RANK': 20, 
            'FGA_RANK': 19, 
            'FG_PCT_RANK': 20, 
            'FG3M_RANK': 16, 
            'FG3A_RANK': 17, 
            'FG3_PCT_RANK': 14, 
            'FTM_RANK': 1, 
            'FTA_RANK': 4, 
            'FT_PCT_RANK': 5, 
            'OREB_RANK': 5, 
            'DREB_RANK': 10, 
            'REB_RANK': 5, 
            'AST_RANK': 20, 
            'TOV_RANK': 12, 
            'STL_RANK': 23, 
            'BLK_RANK': 17, 
            'BLKA_RANK': 21, 
            'PF_RANK': 19, 
            'PFD_RANK': 8, 
            'PTS_RANK': 10, 
            'PLUS_MINUS_RANK': 12, 
            'CFID': 10, 
            'CFPARAMS': 'Atlanta Hawks'
            }
    '''
    allTeamsList = allTeamsDict['LeagueDashTeamStats']

    specificStatAllTeams = []
    for i in range(len(allTeamsList)):  # Loops through and appends specific stat to new list until every team's stat has been added
        specificStatAllTeams.append(allTeamsList[i][stat])
    mean = statistics.mean(specificStatAllTeams)  # Finds mean of stat
    return mean


# Finds league standard deviation for the entered basic or advanced statistic (statType = 'Base' or 'Advanced')
# 리그의 표준편차
def basicOrAdvancedStatStandardDeviation(startDate, endDate, stat,statType = 'Base', season='2018-19'):

    time.sleep(.2)
    # Gets list of dictionaries with stats for every team
    allTeamsInfo = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='Per100Possessions',
                                                           measure_type_detailed_defense=statType,
                                                           date_from_nullable=startDate,
                                                           date_to_nullable=endDate,
                                                           season=season,
                                                           headers=customHeaders,
                                                           timeout=120
                                                           )
    allTeamsDict = allTeamsInfo.get_normalized_dict()
    allTeamsList = allTeamsDict['LeagueDashTeamStats']

    specificStatAllTeams = []
    for i in range(len(allTeamsList)):  # Loops and appends specific stat to new list until every team's stat has been added
        specificStatAllTeams.append(allTeamsList[i][stat])

    standardDeviation = statistics.stdev(specificStatAllTeams)  # Finds standard deviation of stat
    return standardDeviation


# Returns a standardized version of each data point via the z-score method
# Z-Score (Obs-M)/StDev
def basicOrAdvancedStatZScore(observedStat, mean, standardDeviation):

    zScore = (observedStat-mean)/standardDeviation  # Calculation for z-score

    return(zScore)
