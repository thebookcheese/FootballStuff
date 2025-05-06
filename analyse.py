import pandas as pd
import matchsim

DataFolder = 'Data/' # Folder Starters
Data = {
    '1950-51/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1951-52/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
     '1952-53/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1953-54/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1954-55/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1955-56/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1956-57/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1957-58/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_north_results.csv',
        'third_division_south_results.csv'
    ],
    '1958-59/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1959-60/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1960-61/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1961-62/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1962-63/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
     '1963-64/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1964-65/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1965-66/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1966-67/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1967-68/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
     '1968-69/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1969-70/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1970-71/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1971-72/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1972-73/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1973-74/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
     '1974-75/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
       '1975-76/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
        '1976-77/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],    
    '1977-78/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1978-79/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
     '1979-80/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1980-81/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1981-82/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
       '1982-83/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'

    ],
    '1983-84/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
     '1984-85/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1985-86/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
      '1986-87/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
        '1987-88/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1988-89/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
    '1989-90/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
     '1990-91/': [
        'first_division_results.csv',
        'second_division_results.csv',
        'third_division_results.csv',
        'fourth_division_results.csv'
    ],
}
Years = []

for count in range(len(Data)):
    Years.append((f'{count + 1950}') + '-' + (f'{(count + 51) % 100}') + '/') # create years
    if (count + 51) % 100 < 10:
        Years[-1] = (f'{count + 1950}') + '-' + (f'0{(count + 51) % 100}') + '/'

print(Years)

def flat(lis): # flattens 2 dimentional list e.g [[2,3],[4,5], 16]] to [2, 3, 4, 5, 16]
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList


pd.options.display.max_rows = 9999
wincounter = {}
scorecounter = {}
relativestrengths = {}
gamesplayed = {}
FullResults = []
for year in Years: # iterate through the years
    for data in Data[year]: # iterate through the files in the year
        a = pd.read_csv(DataFolder + year + data) # read the csv file
        Teams = [] # teams list
        Headers = a.columns # columns of teams
        for i in a['Home \ Away']: # iterate through teams row
            Teams.append(i)
    # print(a['Home \ Away']) - row
    # print(a.iloc[0]) - column
        for i in range(len(Teams)): # for length of teams
            HomeResults = list(a.iloc[i])
            AwayResults = list(a[Headers[i+1]])
            for i in range(len(AwayResults)):
                if type(AwayResults[i]) != float:
                    if AwayResults[i][0] != AwayResults[i][2]:
                        split = AwayResults[i].split('–') #reverse the away results
                        split.insert(1, '-')
                        z = split[0]
                        y = split[2]
                        split[0], split[2] = y, z
                        for j in range(len(split)):
                            AwayResults[i] = ''.join(split)
            Results = [HomeResults, AwayResults] # combine lists
            FullResults.append(Results) # add to full results
            c = flat(Results) # flatten list
            if type(c) == list:
                c = flat(c) # flatten again if 3d
            name = c[0] # name of team
            count = 0
            for i in c: # iterate through the flattened list
                if count == 0:
                    pass
                else:
                    if type(i) == float:
                        pass
                    else:
                        if i[0] > i[2]: # if win for team
                            #add the relative strengths
                            if name not in relativestrengths:
                                if data == 'first_division_results.csv':
                                    relativestrengths[name] = 1
                                elif data == 'second_division_results.csv':
                                    relativestrengths[name] = 0.5
                                elif data == 'third_division_north_results.csv' or data == 'third_division_south_results.csv':
                                    relativestrengths[name] = 0.25
                                elif data == 'fourth_division_results.csv':
                                    relativestrengths[name] = 0.125
                            else:
                                if data == 'first_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 1
                                elif data == 'second_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 0.5
                                elif data == 'third_division_north_results.csv' or data == 'third_division_south_results.csv' or data == 'third_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 0.25
                                elif data == 'fourth_division_results.csv': 
                                    relativestrengths[name] = relativestrengths[name] + 0.125
                        if i[0] == i[2]: # if draw
                            #add the relative strengths
                            if name not in relativestrengths:
                                if data == 'first_division_results.csv':
                                    relativestrengths[name] = 0.5
                                elif data == 'second_division_results.csv':
                                    relativestrengths[name] = 0.25
                                elif data == 'third_division_north_results.csv' or data == 'third_division_south_results.csv' or data == 'third_division_results.csv':
                                    relativestrengths[name] = 0.125
                                elif data == 'fourth_division_results.csv':
                                    relativestrengths[name] = 0.0625
                            else:
                                if data == 'first_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 0.5
                                elif data == 'second_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 0.25
                                elif data == 'third_division_north_results.csv' or data == 'third_division_south_results.csv' or data == 'third_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 0.125
                                elif data == 'fourth_division_results.csv':
                                    relativestrengths[name] = relativestrengths[name] + 0.0625
                count = count + 1
            if name not in gamesplayed:
                gamesplayed[name] = count
            else:
                gamesplayed[name] = gamesplayed[name] + count # increase game played

with open('writeto.txt', 'w') as f: # open file to write stats to
    for i in FullResults:
        b = flat(i) # flatten list
        if type(b) == list:
            b = flat(b)
        name = b[0] # name of team
        for c in range(len(b)): # go over the results
            if c != 0 :
                if type(b[c]) != float:
                    if b[c][0] > b[c][2]: #if win
                        if name not in wincounter:
                            wincounter[name] = 1 # add name to win counter
                        else:
                            wincounter[name] = wincounter[name] + 1 # increase win
                        if b[c][0] != b[c][2]:
                            split = b[c].split('-')
                        else:
                            split = b[c]
                        if len(split) == 2:
                            split.insert(1, '–')
                            z = split[0]
                            y = split[2]
                            split[0], split[2] = y, z
                            for j in range(len(split)):
                                Toappend = ''.join(split)
                        else:
                            Toappend = split[0]
                        if Toappend not in scorecounter:
                                scorecounter[Toappend] = 1#add score to score counter
                        else:
                            scorecounter[Toappend] = scorecounter[Toappend] + 1 #increase count of score
                    elif b[c][0] == b[c][2]:
                        if b[c] not in scorecounter:
                            scorecounter[b[c]] = 0.5
                        else:
                            scorecounter[b[c]] = scorecounter[b[c]] + 0.5
    sortedwincounter = dict(sorted(wincounter.items(), key=lambda x: x[1], reverse=True)) # sort wins
    sortedscorecounter = dict(sorted(scorecounter.items(), key=lambda x: x[1], reverse=True)) # sort scores
    percentagerelativestrengths = {}
    for key in relativestrengths:
        percentagerelativestrengths[key] = ((relativestrengths[key] / gamesplayed[key]) * 100) # relative team strength
    sortedrelativestrengths = dict(sorted(percentagerelativestrengths.items(), key=lambda x: x[1], reverse=True)) # sort relative team strength
    f.write('Club Wins \n')
    count = 0
    for d in sortedwincounter:
            f.write(str(d) + ' won ' + str(wincounter[d]) + ' matches \n') # write wins per team to file
    f.write('\n')
    f.write('Relative Strength \n')
    for d in sortedrelativestrengths:
            f.write(str(d) + ' had a relative strength of ' + str(((relativestrengths[d] / gamesplayed[d]) * 100))[:5]+ '%  \n') # write relative strength of teams to file
    f.write('\n')
    f.write('Scores \n')
    for d in sortedscorecounter:
        f.write(str(d) + ' happend ' + str(int(scorecounter[d])) + ' times \n') # write scores to file
    f.close()
    
matchsim.main(sortedscorecounter, sortedwincounter, sortedrelativestrengths)