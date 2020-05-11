from itertools import permutations
import time

print("\nWelcome to Jumble Solver!",end="\n")
inputWord=input("Enter the jumbled word: ")
initialTime=time.time()
inputWord=inputWord.lower()

tempList=permutations(inputWord) #This returns a list of tuples
inputTempList=[]
for i in tempList:
    inputTempList.append("".join(i))
    
inputWordSet=set(inputTempList)
inputWordlist=list(inputWordSet)

myFile=open("English_Words.txt","r")
dictWordList=myFile.read().splitlines()
myFile.close()

flag=0
for i in inputWordlist:
    for j in dictWordList:
        if(i==j):
            print("\nThe correct word is",i)
            flag=1
            break
if (flag==0):
    print("\nSorry! The correct word is not in our dictionary")

finalTime=time.time()
timeDifference=finalTime-initialTime
timeDifference=round(timeDifference,3)
print("\nThe time taken to execute the program is",timeDifference,"seconds")