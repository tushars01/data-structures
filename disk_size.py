#implementing Disk usage of my system

import os

def disk_size(path):

    total_immediate_size = os.path.getsize(path)
    #print("immediate_size = " + str(total_immediate_size))
    if os.path.isdir(path):
        #print(os.listdir(path))
        for file in os.listdir(path):
            abs_path = os.path.join(path, file)
            #print(abs_path)
            total_immediate_size += disk_size(abs_path)
            print(str(total_immediate_size) + ': ' +str(abs_path))
        return total_immediate_size
    else:
        return total_immediate_size
    #'file or folder not found or inaccesible'

#path = __file__
path = r'C:/Users/Tushar/Desktop/'
print(disk_size(path)/(1024**2))
        
            
            
            
    
