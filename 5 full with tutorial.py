from bs4 import BeautifulSoup # nhập bộ thư viện BeautifulSoup để parser trang web
import requests # nhập bộ thư viện requests để lấy thông tin từ web

# CRAW DỮ LIỆU TỪ TRANG WEB CAFEBIZ
# 

#========================= LẤY THÔNG TIN TỪ WEB ============================
# lấy nội dung web ( dạng bit)
web_page = requests.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
# lấy nội dung web ( dạng content)
web_content= web_page.content
# chuyển nội dung web dưới dạng beautiful soup có thể đọc được
page = BeautifulSoup(web_content,"html.parser")
# Tìm cụ thể thông tin trên bảng với tags là các table data (td) và attributes là class có tên b_r_c
table_data= page.find_all("td",attrs={"class":"b_r_c"})
# Bởi vì in ra cái đầu tiên nó éo liên quan nên mình xóa đi bằng cách dùng hàm pop(vị trí muốn xóa)
table_data.pop(0)
#print(table_data) 

# Thông tin trong trang web dưới dạng HTML. Vì vậy chúng ta cần sử dụng (BS) Beautiful Soup
# BS được dùng để chui vào cây HTML và lọc lấy thông tin cần thiết

#========================= XỬ LÝ TỪNG THẺ TABLE DATA SANG DẠNG CHỮ TEXT ==========================


i=0 # không có tác dụng gì, ngoài việc là bộ đếm, để hiển thị dữ liệu ra ngoài được rõ hơn
array = [] # array là mảng chứa dữ liệu ở các table data đã được lọc file text
for data in table_data: # duyệt toàn bộ mảng
    if i<len(table_data): # nếu index vẫn nhỏ hơn mảng dữ liệu thì ta cứ tăng i
        data=data.get_text().strip() #get_text() hiểu là chỉ lọc chữ, loại bỏ kí tự lạ, strip là loại bỏ khoảng trống phía sau và trước
        if data == "": # nếu ô craw dữ liệu mà không có dữ liệu, ta ghi là không có 
            data= "deo co"
        print("%s) "%i+data) # in ra toàn bộ dữ liệu + có đánh số
        i+=1
        array.append(data) #thêm vào mảng kết quả trả về

# từ các mảng kết quả trả về, để in ra excel ta cần ngắt mảng
#========================= NGẮT DÃY KẾT QUẢ THÀNH CÁC LIST CON ==========================
list = [array[i:i+6] for i in range (0,len(array),6)] # duyệt mảng cứ 6 phần tử một thì tạo một mảng mới có vị trí từ i đến i+6
#print(list) in ra kết quả để kiểm tra xem có đúng hay không

#========================= iN TOÀN BỘ RA FILE EXCEL ==========================
import pyexcel # nhập thư viện pyexcel để in dữ liệu ra
import pyexcel.ext.xlsx # nhập bộ mở rộng của thư viện, mục đích để in được file xlsx
sheet = pyexcel.Sheet(list) 
sheet.save_as("cafebiz.xlsx")
