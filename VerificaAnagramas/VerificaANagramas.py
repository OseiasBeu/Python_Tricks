from collections import Counter
def is_anagram(str1, str2):
     return Counter(str1) == Counter(str2)
  
def is_anagram(str1, str2): 
    return sorted(str1) == sorted(str2) 
  
print(is_anagram('roma', 'amor'))
print(is_anagram('regalia', 'alegria')) 