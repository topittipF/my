def count_identical_characters(apple):
    char_count = {}
    
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    identical_count = 0
    for count in char_count.values():
        if count > 1:
            identical_count += 1
    
    return identical_count

word = "apple"
print(f"The word '{word}' has {count_identical_characters(word)} identical characters.") 