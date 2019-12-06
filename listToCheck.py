import json
def getList():
    returnList = []
    with open('patterns.json') as patterns:
        patternDict = json.load(patterns)
        for item in patternDict:
            returnList.append(patternDict[item])
        patterns.close()
    return returnList
