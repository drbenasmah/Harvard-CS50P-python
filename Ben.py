'''for i in [0,1,2]:
  print("can't stop! Won't stop!")
  '''

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    
for _ in range(n):
    print("can't stop! Won't stop!")