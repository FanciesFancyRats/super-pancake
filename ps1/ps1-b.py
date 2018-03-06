annual_salary = input("Please input your annual salary: ")
portion_saved = input("Please input your portion saved: ")
total_cost = input("Please input the total cost: ")
semi_annual_raise = input("Please input semi annual raise as a decimal: ")
current_savings = 0
monthly_add = annual_salary/12 * portion_saved

r = 0.04
i = 1
portion_down_payment = .25 * total_cost
portion_down_payment = round(portion_down_payment, 2)
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

