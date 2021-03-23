m = int(input("input message : "))
k = int(input("input key : "))
num = m^k
print(num)
print(bin(num))

m = "01010011"
k = "00111000"
for i in range(len(m)):
    m[i]