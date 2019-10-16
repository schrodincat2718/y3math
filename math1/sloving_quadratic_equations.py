#Please key in the coefficient of x^2, x, and constant in 3 lines
import math

a = int(input())
b = int(input())
c = int(input())

if (b*b - 4*a*c < 0):
	print("No real roots")
if (b*b - 4*a*c == 0):
	print(-b/(2*a))
if (b*b - 4*a*c > 0):
	print((-b+math.sqrt(b*b-4*a*c))/(2*a))
	print(' ')
	print((-b-math.sqrt(b*b-4*a*c))/(2*a))
