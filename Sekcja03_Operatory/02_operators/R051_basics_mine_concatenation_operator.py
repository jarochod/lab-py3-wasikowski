# R51. Operator konkatenacji

# operator konkatenacji

strData ="Hello " +"World"+"!"
print(strData) # Hello World!
print(strData + " and Hello again!") # Hello World! and Hello again!

listData = [1,2,3]
print(listData + [4,5,6]) # [1, 2, 3, 4, 5, 6]


tuple1=("one", "two")
tuple2=("three",)
tuple3=tuple1+tuple2
print(tuple3) # ('one', 'two', 'three')

