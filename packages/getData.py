import pandas as pd
from datetime import date
from .player import Player

def getCSV():
    return pd.read_csv("players.csv")

def getList():
    playerData = getCSV()
    playerData = sanitizeDates(playerData)
    playerData = sanitizeScores(playerData)
    playerData = sanitizePlayhours(playerData)
    playerData = sanitizeUsername(playerData)
    #print(playerData.dtypes)
    #printEachLine(playerData)
    return createList(playerData)

def printEachLine(df):
    for row in df.itertuples():
        print(f"{row.username} {row.highscore} {row.playhours} {row.dateadded}")

def sanitizeDates(df):
    df["dateadded"] = pd.to_datetime(df["dateadded"], format="mixed", errors="coerce")
    today = pd.Timestamp.today().normalize()
    df = df[df["dateadded"] <= today]
    return df

def sanitizeScores(df):
    df["highscore"] = df["highscore"].round(-1)
    df = df[df["highscore"] > 0]
    return df

def sanitizePlayhours(df):
    df["playhours"] = df["playhours"].round(1)
    df = df[df["playhours"] > 0]
    return df

def sanitizeUsername(df):
    df["username"] = df["username"].str.lstrip()
    df["username"] = df["username"].str.capitalize()
    df["username"] = df["username"].str.partition(" ")[0]
    df = df[df["username"] != ""]
    df = df.dropna()
    return df

def createList(df):
    players = []
    for row in df.itertuples():
        currentPlayer = Player("",0,0,"")

        currentPlayer.username = row.username
        currentPlayer.highscore = row.highscore
        currentPlayer.playhours = row.playhours
        
        datestring = f"{row.dateadded.month}"
        if row.dateadded.month < 10:
            datestring = f"0{row.dateadded.month}"
        else:
            datestring = f"{row.dateadded.month}"
        if row.dateadded.day < 10:
            datestring = datestring + f"/0{row.dateadded.day}"
        else:
            datestring = datestring + f"/{row.dateadded.day}"
        datestring = datestring + f"/{row.dateadded.year}"

        currentPlayer.dateadded = datestring

        players.append(currentPlayer)
    return players