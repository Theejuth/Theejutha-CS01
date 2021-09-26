NumTotal = []
for i in range(5):
    Data = int(input("Enter your data : "))
    NumTotal += [Data]
NumTotal.sort()
print ("Min =",NumTotal[0])
print ("Max =",NumTotal[4])