from bs4 import BeautifulSoup
import requests
import json
import pandas as pd 

url = 'https://www.vietcombank.com.vn/KHCN/Cong-cu-tien-ich/Ty-gia'

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
table = soup.find('input',{'id':'currentDataExchange'})

data_json = table['value']
parsed_data = json.loads(data_json)

data_array = parsed_data.get("Data", [])

df = pd.DataFrame(data_array)

# print(df.to_csv('vcb.csv',encoding='utf-8-sig'))

print(df)


