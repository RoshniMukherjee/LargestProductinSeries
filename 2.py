def find_largest_product(N, series):
    largest_product = 0
    
    # Iterate through each consecutive set of N digits in the series
    for i in range(len(series) - N + 1):
        current_product = 1
        current_subseries = series[i:i + N]
        
        # Calculate the product of digits in the current subseries
        for digit in current_subseries:
            current_product *= int(digit)
        
        # Update the largest product if the current product is greater
        if current_product > largest_product:
            largest_product = current_product
    
    return largest_product

# Example usage:
N = int(input("Enter the length of consecutive digits: "))
series = input("Enter the series of digits: ")
largest_product = find_largest_product(N, series)
print("Largest product of size", N, "in the series is:", largest_product)
