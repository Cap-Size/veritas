import requests
from core.auth import getCreds as getCreds
from listToCheck import getList as getList
from re import search
import io



def main():
    #These get the creds and the regex list to search
    creds = getCreds()
    listToSearch = getList()
    #This is the list of found secrets
    secretsFound = []

    #This method pulls the list of commits and cycles through them with the other sub methods below
    def getRecentCommits():
        #Where the commits urls will be stored
        totalList = []
        #The queries that will be used for the search API
        searchTerms = ['update', 'change', 'added', 'test']
        apiEndpoint = creds[0] + 'search/commits'
        theHeaders={'ACCEPT': 'application/vnd.github.cloak-preview'}
        for term in searchTerms:
            param = {'sort':'committer-date','q':term,}
            r = requests.get(url = apiEndpoint, headers = theHeaders, params = param, auth=(creds[1], creds[2]))
            for item in r.json()['items']:
                commitURL = item['url']
                if(commitURL not in totalList):
                    totalList.append(commitURL)
        for item in totalList:
            getSoleCommit(item)
    
    
    
    #This method gets the code for the individual methods and then cycles through line by line 
    #of the code to check for secrets through the testCommit method
    def getSoleCommit(commitURL):
        r = requests.get(url=commitURL, auth=(creds[1],creds[2]))
        for item in r.json()['files']:
            if(item['additions'] > 0 and 'patch' in item):
                testCommit(item['patch'])
    


    #This checks the commit code for a set of regex rules that 
    def testCommit(inCommitt):
        #skipping context line (i.e '@@ -1,3 +1,3 @@')
        #may want ot change this in the future
        for item in inCommitt.split('\n')[1]:
            if(item[0] == '+'):
                results = regexSearch(item)
                if(results[0] == True):
                    return [inCommitt, results[1]]



    def regexSearch(inline):
        for pattern in listToSearch:
            if(search(pattern, inline)):
                return[True, [pattern, inline]]
            else:
                searchMatch = [False, []]
                return [False, []]

    getRecentCommits()

if(__name__ == '__main__'):
    main()