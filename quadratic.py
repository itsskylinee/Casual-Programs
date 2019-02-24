from math import *;

print("We support equations like ax^2+bx+c=0");
print('Let "a" be zero to get a linear equation.');
print();
a = eval(input('input coefficient "a":'));
b = eval(input('input coefficient "b":'));
c = eval(input('input coefficient "c":'));

DELTA = b*b-4*a*c;
if DELTA < 0:
    print("Your equation has no real roots!");
else:
    x1 = (0-b+sqrt(DELTA))/2/a;
    x2 = (0-b-sqrt(DELTA))/2/a;
    if delta == 0:
        print("Your equation has two real roots that are equal: %s" % x1);
    else:
        print("Your equation has two different real roots,");
        print("they are %s and %s" % (x1, x2));

