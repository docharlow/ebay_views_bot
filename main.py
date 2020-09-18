import argparse
import requests
import time

header = '''
    ________                         _                      __          __ 
   / ____/ /_  ____ ___  __   _   __(_)__ _      _______   / /_  ____  / /_
  / __/ / __ \/ __ `/ / / /  | | / / / _ \ | /| / / ___/  / __ \/ __ \/ __/
 / /___/ /_/ / /_/ / /_/ /   | |/ / /  __/ |/ |/ (__  )  / /_/ / /_/ / /_  
/_____/_.___/\__,_/\__, /    |___/_/\___/|__/|__/____/  /_.___/\____/\__/  
   v1.5.0         /____/   By NIZAR BAMIDA                              
'''

def view_listing(item_id,view_count):
    try:
        
        print("\nSending views....\n")
        url = "https://www.ebay.com/itm/"+item_id
        start_time = time.time()
        for i in range(int(view_count)):
            requests.get(url)
        view_time = float(time.time() - start_time)
        print("Done,for "+ str(item_id) +", viewed "+view_count+" times, and "+"it took "+ str(view_time)+" sec")
    except :
        pass
    
def view_multi_listing(file_loc,view_count):
    try:
        file1 = open(file_loc, 'r') 
        ids = file1.readlines()
        file1.close()
    except:
        print("File not Found")
    start_time = time.time()
    count=0
    for id in ids :
        count += 1 
        try:
            print("\nSending views....\n")
            url = "https://www.ebay.com/itm/"+str(id)
            start_time2 = time.time()
            for i in range(int(view_count)):
                requests.get(url)
            view_time2 =  float(time.time() - start_time)
            print("Done,for "+str(id.rstrip('\n'))+", viewed "+view_count+" times, and "+"it took "+ str(view_time2)+" sec")
        except:
            pass
    view_time = float(time.time() - start_time)
    print("\nTask complete for "+ str(count)+" items in "+ str(view_time) + " s ")
        

print(header)
print("\n=========================================")
print("Please select a mode. ")
print("Single product : 1")
print("Multi products : 2 \n")
print("=========================================")
choice = input("mode :")
if choice == "1":
    view_count = input("How many views you want:")
    item_id = input("enter you item id :")
    view_listing(item_id,view_count)
elif choice == "2" :
    view_count = input("How many views you want for each item :")
    file_loc = input("you list location:")
    view_multi_listing(file_loc,view_count)
else:
    print("Invalid input !!")
    
    
    


    
    
        
