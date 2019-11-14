tax_1 = 1.05
tax_2 = 1.13
tax_3 = 1.11
totalCharge = float( input(" Please enter your total price: "))
country = input (" PLease enter your country: ")
if country == "CANADA" :
    province = input(" Please enter your province: ")

if country == "USA" :
    print (" You dont have any tax")
    totalPrice = totalCharge
    print (" Total cost is %.2f dollars" % totalPrice)

if province == "ALBERTA" :
    totalPrice = totalCharge *tax_1
    print (totalPrice)
    print (" Total cost is %.2f dollars" % totalPrice)
    print ("Have a nice day")

if province == "ONTARIO" or province == "NEW BRUNSWICK" \
   or province == "NOVA SCOTIA" :
    totalPrice = totalCharge *tax_2
    print (totalPrice)
    print (" Total cost is %.2f dollars" % totalPrice)
    print ("Have a nice day")

if province == "BRITISH COLUMBIA" or province == "SASKATCHEWAN" \
   or province == "MANITOBA" or province == "QUEBEC" \
   or province == "PRINCE EDWARD ISLAND" \
   or province == "NEWFOUNDLAND AND LABRADOR" \
   or province == "NUNAVUT" or province == "YUKON" \
   or province == "NORTHWEST TERRITORIES" :
    totalPrice = totalCharge *tax_3
    print (" Total cost is %.2f dollars" % totalPrice)
    print ("Have a nice day")
    

