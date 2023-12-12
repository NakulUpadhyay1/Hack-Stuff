file = open('input.txt','r')
a=0
c=0
while 1:

  char = file.read(1)
  if not char:
    break 

  if char=='(':
    a=a+1
  if char==')':
    a=a-1

  c=c+1
  if a==-1:
    break
  
print(a)
print(c)
file.close()

