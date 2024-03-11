def countpairs(list_, pairsum):
    pairs = 0  
    for i in range(len(list_)):  
        for j in range(i + 1, len(list_)):  
            if list_[i] + list_[j] == pairsum:  # Check if the sum of the current pair equals the given sum
                pairs += 1  
    return pairs  # Return the count of pairs with the given sum

list_ = [2, 7, 4, 1, 3, 6]  # Sample list of numbers
pairsum = 10  # Sum to find pairs for
count = countpairs(list_, pairsum)  
print("No of pairs with sum =", pairsum, "is", count)  
