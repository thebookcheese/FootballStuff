import random

def homesortkey(e):
    return e[0]
def awaysortkey(e):
    return e[2]
def main(scorecounter, wincounter, relativestrengths):
    teams = []
    HomeWinScores = []
    AwayWinScores = []
    DrawScores = []
    for i in wincounter:
        teams.append(i)
    percentagescorecount = {
    }
    totalgamesplayed = 0
    for key in scorecounter:
        totalgamesplayed += scorecounter[key]
        if key[0] > key[2]:
            HomeWinScores.append(key)
        elif key[2] > key[0]:
            AwayWinScores.append(key)
        else:
            DrawScores.append(key)

    HomeWinScores.sort(key=homesortkey)
    AwayWinScores.sort(key=awaysortkey)

    AwayDevistatingWin = []
    AwayStrongWin = []
    AwayMediumWin = []
    AwayWeakWin = []

    HomeDevistatingWin = []
    HomeStrongWin = []
    HomeMediumWin = []
    HomeWeakWin = []
    Scores = {
        'Away' : {
            'DevistatingWin' : [],
            'StrongWin' : [],
            'MediumWin' : [],
            'WeakWin' : []
        },
        'Home' : {
            'DevistatingWin' : [],
            'StrongWin' : [],
            'MediumWin' : [],
            'WeakWin' : []
        }

    }

    ScoreProbabilies = {
        'Away' : {
            'DevistatingWin' : [],
            'StrongWin' : [],
            'MediumWin' : [],
            'WeakWin' : []
        },
        'Home' : {
            'DevistatingWin' : [],
            'StrongWin' : [],
            'MediumWin' : [],
            'WeakWin' : []
        }
    }

    for i in AwayWinScores:
        a = i.split(':')
        if (a[1] - a[0] == 1) and (a[1] == 1 or a[1] == 2):
            AwayWeakWin.append(i)
        elif a[1] - a[0] == 2 or (a[1] - a[0] == 3 and a[0] != 0):
            AwayMediumWin.append(i)
        elif (a[1] - a[0] == 3 and a[0] == 0) or (a[1]-a[0] == 4 and a[0] != 0):
            AwayStrongWin.append(i)
        else:
            AwayDevistatingWin.append(i)

        

    for i in HomeWinScores:
        a = i.split(':')
        if (a[1] - a[0] == 1) and (a[1] == 1 or a[1] == 2):
            HomeWeakWin.append(i)
            Scores['Home']['WeakWin'].append(i)
            ScoreProbabilies['Home']['WeakWin'].append(percentagescorecount[i])
        elif a[1] - a[0] == 2 or (a[1] - a[0] == 3 and a[0] != 0):
            HomeMediumWin.append(i)
            Scores['Home']['MediumWin'].append(i)
            ScoreProbabilies['Home']['MediumWin'].append(percentagescorecount[i])
        elif (a[1] - a[0] == 3 and a[0] == 0) or (a[1]-a[0] == 4 and a[0] != 0):
            HomeStrongWin.append(i)
        else:
            HomeDevistatingWin.append(i)
    for key in scorecounter:
        percentagescorecount[key] = (scorecounter[key] / totalgamesplayed) *100
    
    Home = random.choices(teams, k=1)[0]
    Away = random.choices(teams, k=1)[0]
    HomeRelativeStrength = relativestrengths[Home] + 2.5
    AwayRelativeStrength = relativestrengths[Away]
    print(f'Home: {Home}, strength: {HomeRelativeStrength}')
    print(f'Away: {Away}, strength: {AwayRelativeStrength}')
    HomeRelativeStrength = relativestrengths[Home] + 2.5
    AwayRelativeStrength = relativestrengths[Away]
    if HomeRelativeStrength > AwayRelativeStrength:
        UpsetChance = 0.5 / ((HomeRelativeStrength - AwayRelativeStrength)*1.15)
        UpsetTeam = 'Away'
    elif AwayRelativeStrength > HomeRelativeStrength:
        UpsetChance = 0.5 / ((AwayRelativeStrength - HomeRelativeStrength)*1.15)
        UpsetTeam = 'Home'

    Upset = False
    if random.uniform(0, 100) < UpsetChance:
        Upset = True
    
    strengthDifference = HomeRelativeStrength - AwayRelativeStrength

    if Upset == True:
        random.choices()


