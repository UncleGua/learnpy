def yesornot(a):
 a=str(a)
 if a[::]==a[::-1]:
    return True
 else:
    return False
print(list(filter(yesornot,[i for i in range(1,200)])))



