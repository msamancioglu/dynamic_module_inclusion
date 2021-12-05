import importlib
import sys
from datetime import datetime

def magic_module(path:str):
    try:
        mod = importlib.import_module(f"magic_files.{path}")
        return mod               
    except ModuleNotFoundError:        
        return None   

if __name__ == "__main__":    
    if magic_module(sys.argv[1]) is not None:
        start = datetime.now()
        ret = magic_module(sys.argv[1]).run()
        print(ret)
        end = datetime.now()
        print(end - start)
    