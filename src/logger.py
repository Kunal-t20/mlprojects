import logging
import os
from datetime import datetime

# Create Unique Log File Name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Define Folder to Store Log File
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE) #os.getcwd() → gives current folder (like D:/Codes/MLPROJECTS),
                                                    #'logs' → means all logs will be saved inside a folder called logs
#Create That Folder (If Not Exists)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#Setup the Logging Format and File
'''Where to save logs → in LOG_FILE_PATH

How logs should look → using the format

Which level of logs to record → here INFO and above

'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,

    )

