from packages import createDataStructures
from packages import getData
from packages import guiBuilder
from datetime import date

def main():
    scoreboard = createDataStructures.getPlayersSortedByHighscore(getData.getList())
    nameTrie = createDataStructures.createNameTree()
    andrew = "Andrew"
    createDataStructures.addEntry(scoreboard, nameTrie, "Andrew", 7500, 6.8, date(2009,8,6))
    andrew = createDataStructures.nameCheck(nameTrie, andrew)
    print(andrew)
    

if __name__ == "__main__":
    main()