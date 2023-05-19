# https://www.codewars.com/kata/585db3e8eec141ce9a00008f

# DESCRIPTION:
# In this kata, your goal is to write a function which will reverse the vowels in a string. 
# Any characters which are not vowels should remain in their original position. Here are some examples:

# "Hello!" => "Holle!"
# "Tomatoes" => "Temotaos"
# "Reverse Vowels In A String" => "RivArsI Vewols en e Streng"
# For simplicity, you can treat the letter y as a consonant, not a vowel.

# Good luck!

def reverse_vowels(s):
    
    def swap(lst, left, right):
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
        return left, right
    
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    
    left = 0
    right = len(s_list) - 1
    
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        elif s_list[left] and s_list[right] in vowels:
            left, right = swap(s_list, left, right)
    
    return "".join(s_list)

# reminds me of Shoha.