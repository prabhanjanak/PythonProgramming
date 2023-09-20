m1=float(input("Enter 1st marks :"))
m2=float(input("Enter 2nd marks :"))
m3=float(input("Enter 3rd marks :"))
minimum=min(m1,m2,m3)
best_of_two=(m1+m2+m3)-minimum
avg=best_of_two/2
print("Avg. of Best of two marks is:",avg)