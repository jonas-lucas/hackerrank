# ginortS

s: str = input()

# My Answer:
# print(''.join(list(
#   sorted(
#       sorted(
#           sorted(
#               sorted(list(s)), 
#               key=str.isupper
#           ), 
#           key=lambda x: x.isdigit() and int(x) % 2 == 1
#       ), 
#       key=lambda x: x.isdigit() and int(x) % 2 == 0
#   )
# )))

# My Another Answer:

print(''.join(list(sorted(list(s), key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit() and int(x) % 2 == 1, x.isupper(), x)))))