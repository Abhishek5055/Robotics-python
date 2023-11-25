import random
l1=['a','b','c','d']
l2=input("Enter names:").split()
l2.extend(l1)
l2.append('f')
print(l2)
l3=random.choice(l2)
print(l3)