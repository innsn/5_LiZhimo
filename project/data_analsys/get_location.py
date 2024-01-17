import json
import pandas as pd
import requests

data = pd.read_csv("D:/计算机大三上/大数据分析实践/project/CN-Reanalysis201301/201301/CN-Reanalysis-daily-2013010100.csv")

key = "c7317dd02d5b2c06ff11d30362bbbf38"
total = []
for item1,item2 in data[[' lat',' lon']][:5].values:
    # print(item1)
    location = str(item2) + ','+ str(item1)
    url = "https://restapi.amap.com/v3/geocode/regeo?output&location=" + location + "&key="+key+"&radius=1000&extensions=all"
    r = requests.get(url)

    print(r.text)
    t = r.text
    js = json.loads(t)
    locations = {'lat':[],'lon':[],'city':[],'province':[],'district':[]}
    locations['lat'].append(item1)
    locations['lon'].append(item2)
    locations['city'].append(js['regeocode']['addressComponent']['city'])
    locations['province'].append(js['regeocode']['addressComponent']['province'])
    locations['district'].append(js['regeocode']['addressComponent']['district'])

with open('./data.json','w') as file:
    json.dump(locations,file)