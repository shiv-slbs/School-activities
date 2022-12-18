
t=0#variable to calculate the t value.

p=1#variable to calculate the p.

n=input("Enter the n to check for special n: ")#take the n from the user.

for x in n:#for loop  to read the n.

  t=t+int(x)#calculate the t.

  p=p*int(x)#clculate the p.

if((p+t)==int(n)):#check that the n is special or not.

   print("The  is a special number")

else:

   print("The not is not a special number")
