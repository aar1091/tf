nums = list(map(int, input("Ingrese números separados por coma: ").split(',')))

result = []
for i in range(len(nums)):
    prod = 1
    for j in range(len(nums)):
        if i != j:
            prod *= nums[j]
    result.append(prod)

print("Resultado:", result)