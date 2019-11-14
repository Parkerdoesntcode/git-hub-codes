animal1 = ("dog")
animal2 = ("bird")
animal3 = ("lizard")

print ("Look at all the animals ['" + animal1 + ",'" + "'" + animal2 + ",'" + "'" + animal3 + "']")
anint = input("Enter the name of an animal: ")

if anint == animal1 or anint == animal2 or anint == animal3:
    print("1 instance of " + anint + " removed from list.")
else:
    print("1 instance of " + anint + " appended to list.")

if anint == ("Quit") or anint == ("quit"):
    print ("Goodbye")

if anint == animal1:
    print("Look at all the animals ['" + animal2 + ",'" + "'" + animal3 + "']")

if anint == animal2:
    print("Look at all the animals ['" + animal1 + ",'" + "'" + animal3 + "']")

if anint == animal3:
    print("Look at all the animals ['" + animal1 + ",'" + "'" + animal2 + "']")

if anint != animal1 and anint != animal2 and anint != animal3 and anint != "quit" and anint != "Quit":
    print("Look at all the animals ['" + animal1 + ",'" + "'" + animal2 + ",'" + "'" + animal3 + ",'" + "'" + anint + "']")



