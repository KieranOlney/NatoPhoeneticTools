import string
from datetime import datetime

def main():
    rawSavefileName = "natoPhoenetic.txt"
    logSaveFileName = "natoPhoeneticLog.txt"
    textInput = readFromFile(rawSavefileName)
    convertTime = datetime.now()
    convertedText = convertToPhoenetic(textInput)
    print(convertedText)
    saveToFile(rawSavefileName,convertedText)
    convertTime = convertTime.strftime("%d/%m/%Y %H:%M:%S")
    logText = "The Text '"+textInput+"' Was Converted to NATO Phoenetics at "+convertTime+"\n"
    appendToFile(logSaveFileName,logText)
    return

def convertToPhoenetic(stringToConvert):
    natoAlphabet = {'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett','K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee','Z':'Zulu'}
    convertedString = ""
    stringToConvert = stringToConvert.upper()
    for char in stringToConvert:
        if char == " ":
            continue
        elif char in string.punctuation:
            convertedString += " "
            convertedString += char
        elif char in natoAlphabet:
            convertedString += " "
            convertedString += natoAlphabet[char]
        else:
            print("Sorry I did not recognise a character in this string. Please enter a String using only the English Alphabet and Punctuation, without numbers or accented letters.")
            return convertedString
    convertedString = convertedString[1:]
    return convertedString

def readFromFile(fileName):
    readFile = open(fileName,"r")
    fileText = readFile.read()
    readFile.close()
    return fileText

def saveToFile(fileName,saveText):
    writeFile = open(fileName,"w")
    writeFile.write(saveText)
    writeFile.close()
    if readFromFile(fileName) == saveText:
        return True
    else:
        return False

def appendToFile(fileName,saveText):
    writeFile = open(fileName,"a")
    writeFile.write(saveText)
    writeFile.close()
    return

main()