
def gener_geomet_prog(a, r, n):
    result = []
    for i in range(n):
        result.append(a * pow(r, i))
    return result

print(gener_geomet_prog(2, 3, 10))
