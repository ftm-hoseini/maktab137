from api_client import fetch_data
from data_processor import process_and_save
my_list = fetch_data("https://jsonplaceholder.typicode.com/users")
for i in my_list:
    print(i)

process_and_save(my_list)
