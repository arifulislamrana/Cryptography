q = 353
primRoots = []
for i in range(2, q-1):
    distinctResult = []
    for j in range(1, q-1):
        if pow(i, j, q) in distinctResult:
            break
        if pow(i, j, q) not in distinctResult:
            distinctResult.append(pow(i, j, q))
            if j == q-2:
                primRoots.append(i)

print(primRoots)

alpha = int(input("Select a primitive root: "))

privat_Xa = 97
assert privat_Xa < q, "Xa should be less than q"
privat_Xb = 233
assert privat_Xb < q, "Xb should be less than q"

public_Ya = pow(alpha, privat_Xa, q)
public_Yb = pow(alpha, privat_Xb, q)

secret_Ka = pow(public_Yb, privat_Xa, q)
secret_Kb = pow(public_Ya, privat_Xb, q)

print(f"public of A: {public_Ya}")
print(f"secret of A: {secret_Ka}")

print(f"public of B: {public_Yb}")
print(f"secret of B: {secret_Kb}")





