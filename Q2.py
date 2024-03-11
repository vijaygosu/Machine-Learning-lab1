def difference(list_):
    if len(list_) < 3:  # Check if the length of the list is less than 3
        return "range determination not possible"  # Return error message if the list has less than 3 elements
    else:
        max_ = max(list_)  
        min_ = min(list_)  
        return max_ - min_  # Return the difference between the maximum and minimum values

list_ = [5, 3, 8, 1, 0, 4]  # Sample list of numbers
difference_ = difference(list_)  
print("range:", difference_)  
