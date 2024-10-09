'''
https://www.codewars.com/kata/5c3f31c2460e9b4020780aa2

DESCRIPTION:

Return the nth term of the Recamán's sequence.

a(0) = 0;

        a(n-1) - n, if this value is positive and not yet in the sequence
      /
a(n) <
      \
        a(n-1) + n, otherwise

input range: 0 – 30 000
'''

def recaman(n):
    
    if n == 0: return 0
    
    sequence = [0] * (n + 1)
    used = set([0])
    
    for i in range(1, n + 1):
        candidate = sequence[i - 1] - i
        if candidate > 0 and candidate not in used:
            sequence[i] = candidate
        else:
            candidate = sequence[i - 1] + i
            sequence[i] = candidate
        used.add(candidate)
    
    return sequence[n]