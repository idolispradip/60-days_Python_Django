# write a program to swap the value of two variable a and b without using a third variable use arithmatic operations to achieve this.
#we use arithmatic operations and swap the two variable a and b without using third varibale .
a= 5
b= 10
print("Before swapping:")
print("a=",a) # output =5 
print("a=", b) #output = 10

#logic
a= a+b # a= 15 , (5+10)
b= a-b # b=5, (15-10)
a=a-b  # a=10,(15-5)
print("\After swapping ")
print("a=", a) #output:10
print("b=", b) #output:5