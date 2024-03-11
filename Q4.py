def max_occur(string):
    count = {}  
    for char in string:  # Iterate through each character
        count[char] = count.get(char, 0) + 1  

    max_char = max(count, key=count.get)  # Find the character with the maximum count
    max_count = count[max_char]  # Get the count of the maximum occurring character

    return max_char, max_count

string = "hippopotamus"  # Sample string
char, count = max_occur(string)   
print("the most occurring character is ", char, " with count", count)  
