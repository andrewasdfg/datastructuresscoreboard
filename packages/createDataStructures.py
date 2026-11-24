from .getData import getList
from datetime import date
from .player import Player

class TrieNode:
    def __init__(self):
        #child nodes
        self.children: dict[str, "TrieNode"] = {}
        #is this the end of a word?
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isEnd = True

    def search(self, word: str) -> bool:
        currentNode = self.findNode(word)
        return currentNode is not None and currentNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None

    def findNode(self, prefix: str) -> TrieNode | None:
        currentNode = self.root
        for char in prefix:
            if char not in currentNode.children:
                return None
            currentNode = currentNode.children[char]
        return currentNode
    
def getPlayersSortedByHighscore(players):
    n = len(players)
    for i in range(n - 1):
        minIdx = i
        for j in range(i + 1, n):
            if players[j].highscore < players[minIdx].highscore:
                minIdx = j

        players[i], players[minIdx] = players[minIdx], players[i]
    #print(players)
    return players

def createNameTree():
    players = getList()
    nameTree = Trie()
    n = len(players)
    for i in range(n - 1):
        nameTree.insert(players[i].username)
    return nameTree

#All of this is for adding onto the data
def addEntry(scoreboard: list, names: Trie, username: str, highscore: float, playhours: float, dateadded: date):
    if not isinstance(names, Trie):
        raise TypeError(f"Expected a Trie object, got {type(names)}")
    if not isinstance(scoreboard, list):
        raise TypeError(f"Expected a list, got {type(scoreboard)}")
    currentPlayer = Player("",0,0,"")
    username = username.lstrip()
    username = username.capitalize()
    username = username.partition(" ")[0]
    highscore = round(highscore, -1)
    if (highscore <= 9):
        raise ValueError("highscore must be at least 10")
    playhours = round(playhours, 1)
    if (playhours <= 0):
        raise ValueError("playhours must be at least 0.1")
    dateString = ""
    if dateadded.month < 10:
        datestring = f"0{dateadded.month}"
    else:
        datestring = f"{dateadded.month}"
    if dateadded.day < 10:
        datestring = datestring + f"/0{dateadded.day}"
    else:
        datestring = datestring + f"/{dateadded.day}"
        datestring = datestring + f"/{dateadded.year}"
    username = nameCheck(names, username)
    currentPlayer.username = username
    currentPlayer.highscore = highscore
    currentPlayer.playhours = playhours
    currentPlayer.dateadded = dateString
    scoreboard.append(currentPlayer)
    scoreboard = getPlayersSortedByHighscore(scoreboard) #sorts the list again. idk.
    names.insert(currentPlayer.username)

def nameCheck(names: Trie, name: str):
    keepChecking = True
    nameNthClone = ""
    while(keepChecking):
        if names.search(f"{name}{nameNthClone}") == False:
            keepChecking = False
        else:
            if (nameNthClone == ""):
                nameNthClone = 2
            else:
                nameNthClone = nameNthClone + 1
    return f"{name}{nameNthClone}"