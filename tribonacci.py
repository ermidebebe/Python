def tribonacci(signature, n):
    tribonacci=[]
    s=0
    for i in range(n):
        if i>2:
            break
        tribonacci.append(signature[i])
    for i in range(n-3):
        for i in range(len(signature)):
            s+=signature[i]
        tribonacci.append(s)
        del signature[0]
        signature.append(s)
        s=0
    return tribonacci

print(tribonacci([1, 1, 1], 10))
