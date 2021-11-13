import footballPicker
import sys
import db

week = 7

def updateDatabase(week):
    tDict = {
            # "Name": [CBS_PREDICTION, [Odds], [Moneylines], "opponent", "record"], 
            "Arizona Cardinals": [0, [], [], "", ""],
            "Atlanta Falcons": [0, [], [], "", ""],
            "Carolina Panthers": [0, [], [], "", ""],
            "Chicago Bears": [0, [], [], "", ""],
            "Dallas Cowboys": [0, [], [], "", ""],
            "Detroit Lions": [0, [], [], "", ""],
            "Green Bay Packers": [0, [], [], "", ""],
            "Los Angeles Rams": [0, [], [], "", ""],
            "Minnesota Vikings": [0, [], [], "", ""],
            "New Orleans Saints": [0, [], [], "", ""],
            "New York Giants": [0, [], [], "", ""],
            "Philadelphia Eagles": [0, [], [], "", ""],
            "San Francisco 49ers": [0, [], [], "", ""],
            "Seattle Seahawks": [0, [], [], "", ""],
            "Tampa Bay Buccaneers": [0, [], [], "", ""],
            "Washington Football Team": [0, [], [], "", ""],

            "Baltimore Ravens": [0, [], [], "", ""],
            "Buffalo Bills": [0, [], [], "", ""],
            "Cincinnati Bengals": [0, [], [], "", ""],
            "Cleveland Browns": [0, [], [], "", ""] ,
            "Denver Broncos": [0, [], [], "", ""],
            "Houston Texans": [0, [], [], "", ""],
            "Indianapolis Colts": [0, [], [], "", ""],
            "Jacksonville Jaguars": [0, [], [], "", ""],
            "Kansas City Chiefs": [0, [], [], "", ""],
            "Las Vegas Raiders": [0, [], [], "", ""],
            "Los Angeles Chargers": [0, [], [], "", ""],
            "Miami Dolphins": [0, [], [], "", ""],
            "New England Patriots": [0, [], [], "", ""],
            "New York Jets": [0, [], [], "", ""],
            "Pittsburgh Steelers": [0, [], [], "", ""],
            "Tennessee Titans": [0, [], [], "", ""]
        }
    footballPicker.footballPicker(week)

def updateCBS(week):
    tDict = {
            # "Name": [CBS_PREDICTION, [Odds], [Moneylines], "opponent", "record"], 
            "Arizona Cardinals": [0, [], [], "", ""],
            "Atlanta Falcons": [0, [], [], "", ""],
            "Carolina Panthers": [0, [], [], "", ""],
            "Chicago Bears": [0, [], [], "", ""],
            "Dallas Cowboys": [0, [], [], "", ""],
            "Detroit Lions": [0, [], [], "", ""],
            "Green Bay Packers": [0, [], [], "", ""],
            "Los Angeles Rams": [0, [], [], "", ""],
            "Minnesota Vikings": [0, [], [], "", ""],
            "New Orleans Saints": [0, [], [], "", ""],
            "New York Giants": [0, [], [], "", ""],
            "Philadelphia Eagles": [0, [], [], "", ""],
            "San Francisco 49ers": [0, [], [], "", ""],
            "Seattle Seahawks": [0, [], [], "", ""],
            "Tampa Bay Buccaneers": [0, [], [], "", ""],
            "Washington Football Team": [0, [], [], "", ""],

            "Baltimore Ravens": [0, [], [], "", ""],
            "Buffalo Bills": [0, [], [], "", ""],
            "Cincinnati Bengals": [0, [], [], "", ""],
            "Cleveland Browns": [0, [], [], "", ""] ,
            "Denver Broncos": [0, [], [], "", ""],
            "Houston Texans": [0, [], [], "", ""],
            "Indianapolis Colts": [0, [], [], "", ""],
            "Jacksonville Jaguars": [0, [], [], "", ""],
            "Kansas City Chiefs": [0, [], [], "", ""],
            "Las Vegas Raiders": [0, [], [], "", ""],
            "Los Angeles Chargers": [0, [], [], "", ""],
            "Miami Dolphins": [0, [], [], "", ""],
            "New England Patriots": [0, [], [], "", ""],
            "New York Jets": [0, [], [], "", ""],
            "Pittsburgh Steelers": [0, [], [], "", ""],
            "Tennessee Titans": [0, [], [], "", ""]
        }
    footballPicker.getCBS(tDict, week)
    for i in tDict:
        data = db.find(week, i)
        data['cbs_pred'] = tDict[i][0]
        try:
            db.ins(data)
            print("CBS data updated")
        except:
            print(f'Something went wrong with team {i}')

if __name__ == "__main__":
    # gets input from cmd as FUNCTIONNAME WEEKNUMBER
    globals()[sys.argv[1]](sys.argv[2])