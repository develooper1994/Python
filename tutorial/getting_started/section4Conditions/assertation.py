import math
def sqrt(a,b,c):
   assert b*b >= 4*a*c, "Cannot find square root of negative number, found %s < %s" % (b*b, 4*a*c)
   return math.sqrt(b*b - 4*a*c)

print(sqrt(10, 12, 3))
# this will cause assertion error
print(sqrt(-4, 5, -3))