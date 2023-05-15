def gcdEuclideanAlgorithm(a,b):
    if (b > a):
        temp = a;
        b = temp;
        a = b;
    r = a % b;
    if r == 0:
        return b;
    else:
        return gcdEuclideanAlgorithm(b,r);

def extendedEuclideanAlgorithm(a,b):
    if a == 0:
        return 0, 1
    x1, y1 = extendedEuclideanAlgorithm(b % a, a);
    x = y1 - (b // a) * x1;
    y = x1;
    return x,y;

a, b = 73433510078091009,45666020043321; 
print(gcdEuclideanAlgorithm(a,b));
print(extendedEuclideanAlgorithm(a,b));
