#This method calculates the shannon entropy of a string
#IN     string  (potential secret)
#OUT    float   (shannon entropy)

import math
from collections import Counter

def entropy(s):
    threshold = 3.0
    p, lns = Counter(s), float(len(s))
    return (threshold < -sum( count/lns * math.log(count/lns, 2) for count in p.values()))
