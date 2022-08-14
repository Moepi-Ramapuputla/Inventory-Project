class Shoes:#main class

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):

        print(f"The cost for {self.product} is  R{self.cost}")

    def get_quanty(self):
        print(f"The quantity for {self.product} is  {self.quantity} goods")

    def __str__(self):
        return (f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}")
        

shoe_objects_list = []

def read_shoes_data():

    while True:
        try:
            file = open(f'inventory.txt', 'r')
            string_file = file.read()
            onesplit_List = string_file.replace("\n",",").split(",")
          
            a = 0
            b = 1
            c = 2
            d = 3
            e = 4
            while(a < len(onesplit_List)):
                shoe_objects_list.append(Shoes(onesplit_List[a],onesplit_List[b],onesplit_List[c],onesplit_List[d],onesplit_List[e]).__str__())
                a += 5
                b += 5
                c += 5
                d += 5
                e += 5
            
            print("Successful the file inventory.txt has been opened and read the data from the file !")
            print("Also created shoesobject and appended this object into the shoes list")


            break
        
        except FileNotFoundError as error:
            print("File location not found.Try again.\n")
        
def capture_shoes ():
    #get user input
    country = input("Country:")
    code =  input("Code:")
    product = input("Product:")
    cost =  input("Cost:")
    quantity = input("Quantity:")

    #creating object from shoe class
    new_shoe = Shoes(country,code,product,cost,quantity)

    #append shoe list
    shoe_objects_list.append(new_shoe.__str__())
    shoe_objects_list.append(Shoes("Spain","F23132","Max","1000","100").__str__())
       
def view_all():
    print(f"All the detials about items available : \n")
    print("Country,Code,Product,Cost,Quantity")
    x = 0

    while(x < len(shoe_objects_list)):
        print(shoe_objects_list[x])
        x += 1
        
def re_stock():

    join_List = ",".join(shoe_objects_list)
    onesplit_List = join_List.split(",")

    # Create a list to store all quantities
    lowest_list = []
    i = 4

    while(i < len(onesplit_List)):
        # 4th index is the product and every +5 is for next product
        lowest_list.append(int(onesplit_List[i]))
        i += 5

    # Find the lowest of list
    lowest_quantity = min(lowest_list)

    # Find index of quatity the go back 2 spaces to get product name
    index_lowest = onesplit_List.index(str(lowest_quantity))
    product_name_lowest = int(index_lowest)-2

    print(f"{onesplit_List[product_name_lowest]} have the lowest quantity at {lowest_quantity}.")

    add_quantity = int(input(f"How much do you want to add to the quantity of {onesplit_List[product_name_lowest]}:"))

    after_add = lowest_quantity + add_quantity
    # update the index amount
    
    onesplit_List[index_lowest]= after_add 
    print(f"The updated quantity is now {onesplit_List[index_lowest]} for {onesplit_List[product_name_lowest]} ")

    with open("inventory.txt", "r") as f: 
        # remove old line with outdated inform
        lines = f.readlines()
        with open("inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != f"{onesplit_List[index_lowest-4]},{onesplit_List[index_lowest-3]},{onesplit_List[index_lowest-2]},{onesplit_List[index_lowest-1]},{lowest_quantity}":
                    f.write(line)

    #add updates line
    f = open("inventory.txt", "a")
    f.write("\n")
    f.write(f"{onesplit_List[index_lowest-4]},{onesplit_List[index_lowest-3]},{onesplit_List[index_lowest-2]},{onesplit_List[index_lowest-1]},{after_add}")
    f.close()

def seach_shoe():
    shoe_code = input("Please enter shoe code to search:")

    # checks if code matches to codes in the list
    matches = []

    for match in shoe_objects_list:
        if shoe_code in match:
            matches.append(match)
            
    print(matches)

def value_per_item():
    
    join_List = ",".join(shoe_objects_list)
    onesplit_List = join_List.split(",")

    i = 2
    j = 3
    k = 4
    while(i < len(onesplit_List)):
        value_item = int(onesplit_List[j]) * int(onesplit_List[k])
        print(f"{onesplit_List[i]} value:R{value_item}\n")
        i += 5
        j += 5
        k += 5
        
def highest_qty():
    join_List = ",".join(shoe_objects_list)
    onesplit_List = join_List.split(",")

    # Create a list to store all quantities 
    highest_list = []
    i = 4

    while(i < len(onesplit_List)):
        highest_list.append(int(onesplit_List[i]))
        i += 5

    # Find the highest of list
    highest_quantity = max(highest_list)

    # Find index of quatity the go back 2 spaces to get product name
    index_highest = onesplit_List.index(str(highest_quantity)) 
    product_name_highest = int(index_highest)-2

    print(f"{onesplit_List[product_name_highest]} have the highest quantity at {highest_quantity} thus will be on sale")
   
def main():
    menu = ""
    
    while (menu != "d") or (menu != "c") or (menu != "va") or (menu != "rs") or (menu != "s")or (menu != "v")or (menu != "h") or (menu != "g"):
        menu = input('''Select one of the following Options below:
d - Read Shoes Data
c - Capture Shoes
va - View all 
rs - Re-Stock
s - Search Shoe
v - Value Per Item
h - Highest Quantity
g- Get Cost and Quantity

e - Exit
: ''').lower()

        if menu == 'd':

                #calling function
                read_shoes_data()

        elif menu == 'c':

                capture_shoes ()
            
        elif menu == 'va':

                view_all()
            
        elif menu == 'rs':

                re_stock()

        elif menu == 's':
            
                seach_shoe()
            
            
        elif menu == 'v':
            
                value_per_item()

        elif menu == 'h':
            
                highest_qty()

        elif menu == 'g':
            
                #get cost
                new_shoe = Shoes("Spain","F23132","Max","1000","100")
                new_shoe.get_cost()
                new_shoe.get_quanty()
                
        elif menu == 'e':
               print('Goodbye!!!')
               exit()

        else:
                print("You have made a wrong choice, Please Try again\n")
                
main()

    





