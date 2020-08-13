import json
import requests
from datetime import datetime

json_data = requests.get('https://covid19.who.int/page-data/index/page-data.json').json()

# for record in json_data["result"]["pageContext"]["rawDataSets"]["dayGroups"]:
#     print(record["data"]["rows"][1])


# print(json_data["result"]["pageContext"]["rawDataSets"]["dayGroups"][0]["data"]["rows"][0][1])

for record in json_data["result"]["pageContext"]["rawDataSets"]["dayGroups"]:
    # print(record["value"])
    # for deeprecord in record["data"]["rows"]:
    #     print(deeprecord[0])
    # print(datetime.strptime(record["value"][0:10], '%Y-%m-%d').strftime('%d/%m/%Y'))
    for deeprecord in record["data"]["rows"]:
        print(deeprecord)