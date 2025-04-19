from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)

# Danh sách các thành phố ở Việt Nam (có thể mở rộng thêm)
VIETNAM_CITIES = [
    "Hanoi",
    "Ho Chi Minh City",
    "Da Nang",
    "HaiPhong",
    "Can Tho",
    "Hue",
    "Nha Trang",
    "Vung Tau",
    "Da Lat",
    "PhuQuoc"
    # Thêm các thành phố khác nếu bạn muốn
]

def goi_api(url_api):
    """Gọi API và trả về dữ liệu JSON."""
    try:
        phan_hoi = requests.get(url_api)
        phan_hoi.raise_for_status()
        return phan_hoi.json()
    except requests.exceptions.RequestException as loi:
        print(f"Lỗi khi gọi API: {loi}")
        return {"error": f"Lỗi khi gọi API: {loi}"}
    except json.JSONDecodeError as loi:
        print(f"Lỗi khi giải mã JSON: {loi}")
        return {"error": f"Lỗi khi giải mã JSON: {loi}"}

@app.route('/')
def hien_thi_thoi_tiet_ngau_nhien():
    khoa_api = "cf5927c60784d3d638f2e5262a0af283"  # **Nhớ thay bằng API key của bạn**
    thanh_pho_ngau_nhien = random.choice(VIETNAM_CITIES)
    url_api = f"https://api.openweathermap.org/data/2.5/weather?appid={khoa_api}&q={thanh_pho_ngau_nhien}"
    du_lieu_json = goi_api(url_api)
    return render_template('thoi_tiet.html', thoi_tiet=du_lieu_json, thanh_pho=thanh_pho_ngau_nhien)

if __name__ == '__main__':
    app.run(debug=True)