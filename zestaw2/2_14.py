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
longest=x[0]
for i in range(len(x)):
    if len(x[i])>len(longest):
        longest=x[i]

print("Najdluzszy wyraz to:",longest, ", a jego dlugosc wynosi:", len(longest))