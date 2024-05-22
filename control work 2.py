def count_identical_characters(apple):
    # Create a dictionary to store the frequency of each character
    char_count = {}
    
    # Iterate through each character in the word
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Count the number of characters that appear more than once
    identical_count = 0
    for count in char_count.values():
        if count > 1:
            identical_count += 1
    
    return identical_count

# Example usage
word = "apple"
print(f"The word '{word}' has {count_identical_characters(word)} identical characters.")