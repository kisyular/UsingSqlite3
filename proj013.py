import  sqlite3

conn =sqlite3.connect("database.sqlite")

def addScore():
    nameString = raw_input("What is your name? ")
    scoreString = raw_input ("What is your score? ")
    matchesPlayed = raw_input("How many Matches did you play? ")
    matchesPlayed = str(matchesPlayed)
    score = str(scoreString)
    conn.execute('insert into entries (name, score, matches) VALUES (?,?, ?)', [nameString, score, matchesPlayed])
    conn.commit()


def leaderBoardPrint():
    print ("********** proj012 ***********")
    results = conn.execute('select *from entries order by score desc')
    for tuple in results:
        print tuple[0] + "\t" + str(tuple[1]) + "\t" + str(tuple[2])

def showLeaderBoard():
    print ("********** proj012 ***********")
    results = conn.execute('select *from entries order by name asc')
    for tuple in results:
        print tuple[0] + "\t" + str(tuple[1]) + "\t" + str(tuple[2])
def showMatchesBoard():
    print ("********** proj012 ***********")
    results = conn.execute('select *from entries order by matches desc')
    for tuple in results:
        print tuple[0] + "\t" + str(tuple[1]) + "\t" + str(tuple[2])

def deletedRecord():
    nameString = raw_input("Which record(name) do you want to delete? ")
    conn.execute('delete from entries where name=?', [nameString])
    conn.commit()
def deletedByScore():
    scoreString = raw_input("enter the minimum score you want to delete? ")
    scoreString = str(scoreString)
    conn.execute('delete from entries where score < ?', [scoreString])
    conn.commit()

while (True):
    print
    print
    print ("What would you like to do? ")
    print ("1. Add a new record.")
    print ("2. Remove a record")
    print ("3. Show Score board - sort by score (high to low)")
    print ("4. Show Score board - sort by name (A to Z)")
    print ("5. Show Score board - sort by matches played")
    print ("6. Delete record by score")
    print ("x. quit")
    choice = raw_input("Your choice ")

    if (choice == "1"):
        addScore()
    elif (choice == "2"):
        deletedRecord()
    elif (choice == "3"):
        leaderBoardPrint()
    elif (choice == "4"):
        showLeaderBoard()
    elif (choice == "5"):
        showMatchesBoard()
    elif (choice == "6"):
        deletedByScore()
    elif (choice == "x"):
        break
    else:
        print ("Undefined choice")