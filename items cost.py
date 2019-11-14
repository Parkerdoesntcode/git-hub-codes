deposit=input("item 1 price: ")
if float(deposit)>=50:
    Cost1=int(deposit)*0.12
    Item1=int(deposit)+Cost1
    print("the cost of item one is ${0:.2f}".format(Item1))
else:
    Cost1=int(deposit)*0.12
    Number1=int(deposit)+Cost1
    Final1=Number1+10
    print("The cost of item 1 including shipping is ${0:.2f}".format(Final1))
