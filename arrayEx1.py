
expense = [
    ['January',2200],['February',2350],['March',2600],
    ['April',2130],['May',2190]]

#answer 1
print(expense[1][1]-expense[0][1])

#answer 2
total_expense=0
for i in range(3):
    total_expense+=expense[i][1]
print(total_expense)

#answer 3
for i in range(len(expense)):
    if expense[i][1]==2000:
        print('Yes, 2000 dollars was spent in the month ',
        expense[i][0])

#answer 4
expense.insert(5,['June',1980])

#answer 5
expense[3][1]-=200


