import io

def getCreds():
    creds = []
    with open('core/creds.txt', 'r') as credsFile:
        temp = credsFile.read()
    temp = temp.replace(' ', '').split('\n')
    for item in temp:
        creds.append(item[item.find(':')+1:])
    return creds