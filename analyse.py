import pandas as pd

DataFolder = 'Data/'
Years = ['1950-51/', '1951-52/','1952-53/', '1953-54/', '1954-55/', '1955-56/','1956-57/', '1957-58/', '1958-59/', '1959-60/', '1960-61/', '1961-62/', '1962-63/', '1963-64/', '1964-65/', '1965-66/', '1966-67/', '1967-68/', '1968-69/', '1969-70/']
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
}


def flat(lis):
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
for year in Years:
    for data in Data[year]:
        a = pd.read_csv(DataFolder + year + data)
        Teams = []
        Headers = a.columns
        for i in a['Home \ Away']:
            Teams.append(i)
    # print(a['Home \ Away']) - row
    # print(a.iloc[0]) - column
        for i in range(len(Teams)):
            HomeResults = list(a.iloc[i])
            AwayResults = list(a[Headers[i+1]])
            for i in range(len(AwayResults)):
                if type(AwayResults[i]) != float:
                    split = AwayResults[i].split('–')
                    split.insert(1, '-')
                    z = split[0]
                    y = split[2]
                    split[0], split[2] = y, z
                    for j in range(len(split)):
                        AwayResults[i] = ''.join(split)
            Results = [HomeResults, AwayResults]
            FullResults.append(Results)
            c = flat(Results)
            if type(c) == list:
                c = flat(c)
            name = c[0]
            count = 0
            for i in c:
                if count == 0:
                    pass
                else:
                    if type(i) == float:
                        pass
                    else:
                        if i[0] > i[2]:
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
                count = count + 1
            if name not in gamesplayed:
                gamesplayed[name] = count
            else:
                gamesplayed[name] = gamesplayed[name] + count

with open('writeto.txt', 'w') as f:
    for i in FullResults:
        b = flat(i)
        if type(b) == list:
            b = flat(b)
        name = b[0]
        for c in range(len(b)):
            if c != 0 :
                if type(b[c]) != float:
                    if b[c][0] > b[c][2]:
                        if name not in wincounter:
                            wincounter[name] = 2 
                        else:
                            wincounter[name] = wincounter[name] + 1
                    if b[c] not in scorecounter:
                        scorecounter[b[c]] = 1
                    else:
                        scorecounter[b[c]] = scorecounter[b[c]] + 1
    sortedwincounter = dict(sorted(wincounter.items(), key=lambda x: x[1], reverse=True))
    sortedscorecounter = dict(sorted(scorecounter.items(), key=lambda x: x[1], reverse=True))
    percentagerelativestrengths = {}
    for key in relativestrengths:
        percentagerelativestrengths[key] = ((relativestrengths[key] / gamesplayed[key]) * 100)
    sortedrelativestrengths = dict(sorted(percentagerelativestrengths.items(), key=lambda x: x[1], reverse=True))
    f.write('Club Wins \n')
    count = 0
    for d in sortedwincounter:
            f.write(str(d) + ' won ' + str(wincounter[d]) + ' matches \n')
    f.write('\n')
    f.write('Relative Strength \n')
    for d in sortedrelativestrengths:
            f.write(str(d) + ' had a relative strength of ' + str(((relativestrengths[d] / gamesplayed[d]) * 100))[:5]+ '%  \n')
    f.write('\n')
    f.write('Scores \n')
    for d in sortedscorecounter:
        if count % 2 == 0:
            f.write(str(d) + ' happend ' + str(scorecounter[d]) + ' times \n')
        count += 1
    
