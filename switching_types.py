#num is automatically converted to a float (num which was an integer, but converted to a float
num = 42
pi = 3.142
num = 42/pi
print(num)

x = 10
y = 3
z = x / y
print(z)

#how can we predict when python3 will automatically convert integers and floats to strings?

count = 443
#converted integer to a string for the concatetnation to work
print("unused port: " + str(count))

