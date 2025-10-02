import datetime
import time
import uuid

random_string = uuid.uuid4()

while True:
    date = datetime.datetime.now()
    
    print(f'{date} : {random_string}')
    
    time.sleep(2)
