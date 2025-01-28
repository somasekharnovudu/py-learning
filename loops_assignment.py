names = ['john', 'micheal', 'jackson', 'jeffery', 'bentley',
         'rolls', 'astin', 'ferrari', 'chevron', 'cheyron', 'veron']

for name in names:
    name_length = len(name)
    print('===== name length is ' + str(name_length))
    if name_length > 5:
        print('==== big name ' + name)
    if 'n' in name or 'N' in name:
        print('====== name which has n is ' + name)

while (len(names) > 0):
    names.pop()
else:
    print('===== loop emptied')

print(names)
