
#列表生成式 一层循环
listFor = [x  for x in range(1,11)]
listOneFor = [x * x for x in range(1,11)]
#列表生成式 两层循环
listTwoFor = [m+n for m in 'ABC' for n in 'XYZ']
print('listFor=',listFor)
print('listOneFor=',listOneFor)
print('listTwoFor=',listTwoFor)

dict = {'x':'A','y':'B','z':'C'}
for k,v in dict.items():
    print(k,'=',v)

print([k + '=' + v for k,v in dict.items()])