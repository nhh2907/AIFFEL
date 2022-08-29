path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

# p_list = path.split('\\')
# filename = p_list[-1]
# print(filename, 'is asfasdf')

filename = path[path.rfind('\\') + 1 : ]
print(filename)