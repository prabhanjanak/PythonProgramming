# while loop to find the sum of first n numbers
endpoint = int(input("Enteer the value of n:"))
sum_of_numbers = 0
i = 0
while i <= endpoint:
    sum_of_numbers = sum_of_numbers + i
    i = i + 1
print("The sum of the first {} wwhole numbers is {}".format(endpoint, sum_of_numbers))