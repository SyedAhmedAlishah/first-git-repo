Languages = ['korean is here', 'Urdu', 'English', 'Punjabi', 'Japanese']
print(Languages[4])
print(Languages[0].split(" "))
Numbers=[1, 2, 3, 4, 6]
Name=['ahmed', 'Ali', 'Shah']

Languages.extend(Numbers)
print(Languages)

Languages.remove(1)
print(Languages)

Languages.clear()
print(Languages)

Languages = ['korean is here', 'Urdu', 'Urdu', 'English', 'Punjabi', 'Japanese']
Languages.append(Name)
print(Languages)
print(Languages[5][2])

print(Languages.index('Urdu'))

string = Languages.copy()
print(string)

print(Languages.count('Urdu'))

Roll_NO=[355, 356, 350, 360]
Roll_NO.insert(1,352)
print(Roll_NO)

Roll_NO.pop()
print(Roll_NO)

Roll_NO.sort()
print(Roll_NO)

Roll_NO.reverse()
print(Roll_NO)

