def commaCode(anyList):
    anyList.insert(-1, 'and')
    for i in anyList[0: -1]:
        print(i, end = ', ')
    print(anyList[-1])
    
spam = ['Roma', 'New York', 'Tokyo', 'Beijin', 'Berlin', 'Paris']
commaCode(spam)
