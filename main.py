import json

class pos:
    def __init__(self):
         self.curent_items = []
         self.sumArry = []
         
    def LOdedata(self):
        with open("./data/data.json") as file:
            data = json.load(file)
        self.product = data.get("products",[])
        print("database lode sucss")
    def calculate(self,barcode,unit):
        for item in self.product:
            if item.get("barcode") == barcode:
                price_per = item.get("price_per_unit") #calculate the sum and total price 
                total = price_per * unit
               # self.sum +=total
                self.sumArry.append(total)
                self.curent_items = []                     #add the list for value
                self.curent_items.append(item.get("name")) #0
                self.curent_items.append(total) #1
                self.curent_items.append(unit) #2
                self.curent_items.append(item.get("unit")) #3
                self.curent_items.append(item.get("expiry_date"))
                break
            
    #this function is use to create text fils
    def make_pdf(self,number):
        filename = f"./pdf/bill{number}.txt"
        self.file = open(filename,"x")
        
    def wrirePdf(self,camand,lastPrice):
        if lastPrice is None and camand== "no":
            data_dict = { #add the curent_items for values
                     "Name": self.curent_items[0],
                      "Total": self.curent_items[1],
                      "Units":self.curent_items[2],
                      "Unit Name": self.curent_items[3],
                       "Expiry Date": self.curent_items[4],
                       
                     }
            self.file.write(f"Name =  {data_dict.get('Name')}\n") 
            self.file.write(f"Total =  {data_dict.get('Total')}\n")
            self.file.write(f"Units =  {data_dict.get('Units')}\n")
            self.file.write(f"Unit Name =  {data_dict.get('Unit Name')}\n")
            self.file.write(f"Expiry Date =  {data_dict.get('Expiry Date')}\n")
        else:
            self.file.write(f"all price = {lastPrice}\n")
            self.file.write("Mobile : 071336405") 
            
    

m1  = pos()
m1.LOdedata()
number =1
m1.make_pdf(number)
while True:
    # print("-----se super market----")
    m1.file.write("----SE SOFTWARE CREATION----\n\n\n")
    key = input("Checkout now? (yes/no): ").lower()
    if key != "yes":
        comand = "no"
        barcode = input("enter the barcode number:")
        while True:
            try:#chack the usint number is integer
                unit = int(input("enter your unit count"))
                break
            except ValueError:
                print("-----data type in not valid----")
            
        m1.calculate(barcode,unit)
        m1.wrirePdf(comand,None) #222

    else:
        m1.curent_items.clear() #clean the creant items arry
        sum = 0
        for cal in m1.sumArry:
            sum+=cal
        m1.wrirePdf("yes",sum)
        m1.sumArry.clear() #clean the arry
        number +=1
        m1.make_pdf(number)
        
        
