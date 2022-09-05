def check_anagram(a, b):
    if a is None or b is None or len(a) != len(b):
        return "Not Anagram"
        
    counts_a = {}
    counts_b = {}
    
    for x in a:
        if x not in counts_a.keys():
            counts_a[x] = 1
        else:
            counts_a[x] += 1
        
    for x in b:
        if x not in counts_b.keys():
            counts_b[x] = 1
        else:
            counts_b[x] += 1
        
    return "Anagram" if counts_a == counts_b else "Not Anagram"

print(check_anagram("keen", "knee"))
print(check_anagram("race", "care"))
print(check_anagram("fried", "fired"))
print(check_anagram("apple", "paddle"))
print(check_anagram("first", "second"))
print(check_anagram("yo", "second"))
print(check_anagram("first", "fires"))
print(check_anagram("niche", "chien"))