import requests
import time
import random


def create_zabbix_data_type_0_entry():
    entry_data = {
        'clock': time.time(),  # Replace with your actual clock value
        'host_name': 'demohost',  # Replace with your actual host_name
        'item_id': random.randint(1, 10000000),  # Replace with your actual item_id value
        'item_name': "demoname",  # Replace with your actual item_name
        'ns': random.randint(0,255),  # Replace with your actual ns value
        'value': random.randint(0, 255),  # Replace with your actual value value
        'data_type': random.randint(0,4)  # Replace with your actual data_type value
    }
    url = 'http://127.0.0.1:8000/zabbix/api/datatype0/'
    response = requests.post(url, data=entry_data)
    print(response.status_code)
    

    


if __name__ == '__main__':
        create_zabbix_data_type_0_entry()       
