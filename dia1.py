PATH = "./input.txt"
NUMEROS = ["1","2","3","4","5","6","7","8","9","0"]
DIGITOS = ["one","two","three","four","five","six","seven","eight","nine"]
DIGITOS2 = [z[::-1] for z in DIGITOS]

def valor(s):
    res = ""
    f1 = False
    for i in range(len(s)):
        if s[i] in NUMEROS:
            res += s[i]
            break
        
        for j in range(9):
            if s[i:i+len(DIGITOS[j])] == DIGITOS[j]:
                res += NUMEROS[j]
                f1 = True
                break
        if(f1):break
    
    s = s[::-1]
    f1 = False

    for i in range(len(s)):
        if s[i] in NUMEROS:
            res += s[i]
            break

        for j in range(9):
            if s[i:i+len(DIGITOS2[j])] == DIGITOS2[j]:
                res += NUMEROS[j]
                f1 = True
                break
        if(f1):break
    
    return int(res)

with open(PATH,"r") as arq:
    cnt = 0
    for line in arq:
        cnt += valor(line)
    
print(cnt)
