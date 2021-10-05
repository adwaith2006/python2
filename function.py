def countWordsFromFile():
    filename=input("ENTER THE FILE NAME")
    file=open(filename,"r")

    numberOfWords=0

    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+ len(words)
    
    print("NUMBER OF WORDS:")
    print(numberOfWords)

countWordsFromFile()
