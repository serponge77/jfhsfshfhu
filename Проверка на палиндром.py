def palindrom(a):
    if a == a[::-1]:
        return True
    else:
        return False
print(palindrom('лепсспел'))
