from bs4 import BeautifulSoup
import requests
import re
web_content = requests.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').content
page = BeautifulSoup(web_content,"html.parser")
table_data= page.find_all("td",attrs={"class":"b_r_c"})
table_data.pop(0)
#print(table_data)
i=0
for data in table_data:
    if i<len(table_data):
        data=data.get_text().strip()
        if data == "":
            data= "deo co"
        print("%s) "%i+data)
        i+=1

