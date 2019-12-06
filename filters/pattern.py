#This method finds patterns within text, it can find the following:
#Repeating:     'aaaa'
#Ascending:     'abcd'
#Decending:     'dcba'
#NOTE:          Recommended character threshold is 4

def pattern(suspect):
    differences = ''
    for i in range(len(suspect) - 1):
        test = str(abs(ord(suspect[i]) - ord(suspect[i + 1])))
        if(test == '1' or test == '0'):
            differences += 1
        else:
            differences += 0
        
    if('111' in differences):
        return True
    else:
        return False