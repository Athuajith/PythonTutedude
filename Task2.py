list=[]

for i in range(1,11):
    list.append(i)
first_five=list[:5]
rev_first_five=first_five[::-1]
print(f"Original list:{list}")
print(f"Extracted fist five elements:{first_five}")
print(f"Reversed extracted five elements:{rev_first_five}")
