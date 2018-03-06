annual_salary = input("Please input your annual salary: ")
annual_salary = float(annual_salary)
#total_cost = input("Please input the total cost: ")
#semi_annual_raise = input("Please input semi annual raise as a decimal: ")
current_savings = 0
semi_annual_raise = .07
total_cost = 1000000
r = 0.04
i = 1

portion_down_payment = .25 * total_cost
portion_down_payment = round(portion_down_payment, 2)

"""
for j in range (5):
        current_savings += current_savings*r/12     
        current_savings = round(current_savings, 2)
        current_savings += monthly_add
        current_savings = round(current_savings, 2)

        print current_savings, i
        i += 1
while (portion_down_payment > current_savings):
    print i, " is the current month"
    annual_salary += annual_salary * semi_annual_raise
    monthly_add = annual_salary/12 * portion_saved
    for j in range (6):
        current_savings += current_savings*r/12     
        current_savings = round(current_savings, 2)

        current_savings += monthly_add
        current_savings = round(current_savings, 2)

        print current_savings, i
        
        if portion_down_payment <= current_savings:
            print (portion_down_payment, current_savings)
            break
        i += 1
print("Number of months: ", i)
"""
minimum = float(1)
maximum = float(10000)
bisection = float(5000)
cycleNumbers = 1

while ((current_savings > portion_down_payment + 100) or (current_savings < portion_down_payment - 100)):
    if annual_salary*3 < portion_down_payment:
        print('This will not work')
        break
    print(minimum, maximum, bisection)
    current_savings = 0
    monthly_add = annual_salary/12 * (bisection / 10000) 
    for j in range(36):
        current_savings += current_savings*r/12
        current_savings += monthly_add
    print(current_savings, i)
    if current_savings < portion_down_payment - 100:
        minimum = bisection
        
        print('Moved the minimum to the middle...')
    else:
        maximum = bisection
        print('Moved the maximum to the middle...')
    print("current_savings: ", current_savings)
    print("goal           : ", portion_down_payment)
    bisection = (maximum+minimum)/2
    a = input(" ")
    cycleNumbers += 1
print (bisection/10000)
print (cycleNumbers)


