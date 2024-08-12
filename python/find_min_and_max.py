'''
Description:

Implement a function that returns the minimal and the maximal value of a list (in this order).
'''

def get_min_max(seq): 
    return min(seq), max(seq)

def get_min_max(seq): 
    
    srtd = sorted(seq)
    
    return (srtd[0], srtd[-1])