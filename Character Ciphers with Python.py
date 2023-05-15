def gcd(x,y):
    if x > y:
        small = y;
    else:
        small = x;
    for i in range(1,small+1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i;
    return gcd;

def encrypt(plaintext, a, b):
    if gcd(a,b) == 1:
        encrypted = "";
        for i in plaintext:
            if i.isalpha():
                if i.isupper():
                    temp = ord(i) - 65;
                    temp = (temp * a + b) % 26 + 65;
                    encrypted += chr(temp);
                else: 
                    temp = ord(i) - 97;
                    temp = (temp * a + b) % 26 + 97;
                    encrypted += chr(temp);
            else:
                encrypted += i;
        return encrypted;
    else:
        return("warning");

def decrypt(ciphertext, a, b):
    if gcd(a,b) == 1:
        inv = 0;
        for i in range(26):
            if (a * i) % 26 == 1:
                inv = i;
        decrypted = "";
        for i in ciphertext:
            if i.isalpha():
                if i.isupper():
                    temp = ord(i) - 65;
                    temp = inv * (temp - b) % 26 + 65;
                    decrypted += chr(temp);
                else:
                    temp = ord(i) - 97;
                    temp = inv * (temp - b) % 26 + 97;
                    decrypted += chr(temp); 
            else:
                decrypted += i;
        return decrypted;
    else:
        return("warning");

print(decrypt("Ve zdl tuh tqrhgo edu oyh Qvdmdbz du oyh LR Yvroduz HDN, zdl fvmm uhnhvih tg hjtvm rotovgb fyhuh od uhaduo edu oyh jtph-la hctj.  Oyh jtph-la hctjr tuh Euvktz", 23, 19))
