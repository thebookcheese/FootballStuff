import penaltyblog as pb
import random
fb = pb.scrapers.FootballData('ENG Premier League', '2019-2020')
df = fb.get_fixtures()

clf = pb.models.DixonColesGoalModel(df["goals_home"], df["goals_away"], df["team_home"], df["team_away"])
clf.fit()
results = {}
def predict():
    probs = clf.predict("Arsenal", "Chelsea")
    a = random.random()
    if a > probs.home_win:
        homeCloseness = a - probs.home_win
    else:
        homeCloseness = probs.home_win - a

    if a > probs.away_win:
        awayCloseness = a - probs.away_win
    else:
        awayCloseness = probs.away_win - a

    if a > probs.draw:
        drawCloseness = a - probs.draw
    else:
        drawCloseness = probs.draw - a

    if homeCloseness < awayCloseness and homeCloseness < drawCloseness:
        print('is home win')
        homeGoals = round(random.uniform(probs.home_goal_expectation - 1, probs.home_goal_expectation + 1)[0])
        awayGoals = round(random.uniform(probs.away_goal_expectation - 1, probs.home_goal_expectation)[0])
        while awayGoals >= homeGoals:
            awayGoals = round(random.uniform(probs.away_goal_expectation - 1, probs.home_goal_expectation)[0])
        score = str(homeGoals) + ':' + str(awayGoals)
        print(score)
    elif awayCloseness < homeCloseness and awayCloseness < drawCloseness:
        print('is away win')
        awayGoals = round(random.uniform(probs.away_goal_expectation - 1, probs.away_goal_expectation + 1)[0])
        homeGoals = round(random.uniform(probs.home_goal_expectation - 1, probs.away_goal_expectation)[0])
        while homeGoals >= awayGoals:
            homeGoals = round(random.uniform(probs.away_goal_expectation - 1, probs.home_goal_expectation)[0])
        score = str(homeGoals) + ':' + str(awayGoals)
        print(score)
    elif drawCloseness < homeCloseness and drawCloseness < awayCloseness:
        print('is draw')
        score = str(round(probs.home_goal_expectation[0])) + ':' + str(round(probs.home_goal_expectation[0]))
        print(score)

    if score not in results:
        results[score] = 1
    elif score in results:
        results[score] = results[score] + 1

for i in range(400):
    predict()

sortedresults = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)) # sort relative team strength
with open('otherwriteto.txt', 'w') as f: 
    for key in sortedresults:
        percent = str((sortedresults[key]/400)*100)
        f.write(f'{key} happen {sortedresults[key]} times or {percent[:4]}% (out of 400) \n')