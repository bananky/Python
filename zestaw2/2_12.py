line = '\tLorem ipsum dolor sit amet,\n' \
       'consectetur adipiscing elit,\n' \
       'sed do eiusmod tempor incididunt\n' \
       'ut labore et dolore magna aliqua.\n' \
       '\tUt enim ad minim veniam, quis nostrud\n' \
       'exercitation ullamco laboris nisi\n' \
       'ut aliquip ex ea commodo consequat.\n' \
       '\tDuis aute irure dolor in reprehenderit\n' \
       'in voluptate velit esse cillum dolore eu\n' \
       'fugiat nulla pariatur.'

x=line.split()
print(x)
n=[]
for i in range(len(x)):
       word=x[i]
       n.append(word[0])

print(n)
word=''.join(n)
print(word)

n=[]
for i in range(len(x)):
       word=x[i]
       n.append(word[len(word)-1])
word=''.join(n)
print(word)