__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil
from zipfile import ZipFile


def main():
    # 1
    print(clean_cache())
    
    # 2
    print(cache_zip(zip_file_path, cache_dir_path))
    
    # 3  
    cached_files()
    
    # 4 
    x = cached_files() 
    print(find_password(x))


current_dir = os.getcwd()
cache_dir_path = current_dir +"/files/cache"
zip_file_path = current_dir + "/files/data.zip"    

def clean_cache():
    if os.path.exists(cache_dir_path):
        shutil.rmtree(cache_dir_path)
    if not os.path.exists(cache_dir_path):
        os.mkdir(cache_dir_path)
    return ('cache is empty')

def cache_zip(zip_file_path, cache_dir_path): 
    with ZipFile(zip_file_path, 'r') as zipobj:
        zipobj.extractall(cache_dir_path)
    return ('file is unzipped in cache folder')

def cached_files():
    absoluut = os.path.abspath(cache_dir_path)
    obj = os.scandir(absoluut)
    cached_files = []
    for entry in obj:
        path = os.path.join(absoluut, entry) 
        if entry.is_file():
            cached_files.append(path)       
    return cached_files     

def find_password(file_paths):
    for files in file_paths:
        with open(files, "r") as f:
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    password = line[line.find(' ') +1:].strip()
                    
    return password
            
        
if __name__ == '__main__': 
    main()
  

    
    
    


    
    
    
    
    
    
  


