import requests
import json

def goi_va_phan_tich_api(url_api):
    """
    Gọi một API và phân tích kết quả trả về theo định dạng JSON.

    Tham số:
        url_api (str): URL của API cần gọi.

    Trả về:
        dict hoặc None: Một dictionary Python chứa dữ liệu đã phân tích (nếu thành công),
                     hoặc None nếu có lỗi.
    """
    try:
        # Thực hiện yêu cầu GET đến API
        phan_hoi = requests.get(url_api)

        # Kiểm tra trạng thái của phản hồi
        phan_hoi.raise_for_status()  # Báo lỗi cho các mã trạng thái HTTP có lỗi

        # Chuyển đổi dữ liệu JSON nhận được thành dictionary Python
        du_lieu = phan_hoi.json()

        print("Dữ liệu JSON nhận được:")
        print(json.dumps(du_lieu, indent=4, ensure_ascii=False))

        # Tiến hành phân tích dữ liệu tại đây (ví dụ cụ thể bên dưới)
        ket_qua_phan_tich = phan_tich_du_lieu_thoi_tiet(du_lieu)
        return ket_qua_phan_tich

    except requests.exceptions.RequestException as loi:
        print(f"Lỗi khi gọi API: {loi}")
        return None
    except json.JSONDecodeError as loi:
        print(f"Lỗi khi giải mã JSON: {loi}")
        return None

def phan_tich_du_lieu_thoi_tiet(du_lieu_thoi_tiet):
    """
    Phân tích dữ liệu thời tiết từ API OpenWeatherMap.

    Tham số:
        du_lieu_thoi_tiet (dict): Dictionary chứa dữ liệu thời tiết.

    Trả về:
        dict hoặc None: Dictionary chứa thông tin thời tiết đã phân tích,
                     hoặc None nếu dữ liệu không hợp lệ.
    """
    if du_lieu_thoi_tiet and du_lieu_thoi_tiet.get("cod") != "404":
        du_lieu_chinh = du_lieu_thoi_tiet.get("main")
        thong_tin_thoi_tiet = du_lieu_thoi_tiet.get("weather")

        if du_lieu_chinh and thong_tin_thoi_tiet and len(thong_tin_thoi_tiet) > 0:
            nhiet_do = du_lieu_chinh.get("temp")
            do_am = du_lieu_chinh.get("humidity")
            mo_ta = thong_tin_thoi_tiet[0].get("description")

            if nhiet_do is not None and do_am is not None and mo_ta:
                return {
                    "nhiet_do": f"{nhiet_do - 273.15:.2f} °C",
                    "do_am": f"{do_am}%",
                    "mo_ta": mo_ta
                }
            else:
                print("Dữ liệu thời tiết không đầy đủ.")
                return None
        else:
            print("Không tìm thấy thông tin thời tiết chi tiết.")
            return None
    else:
        print("Không tìm thấy thông tin thời tiết cho thành phố này.")
        return None

if __name__ == "__main__":
    # Thay thế bằng API key của bạn và tên thành phố mong muốn
    khoa_api = "cf5927c60784d3d638f2e5262a0af283"
    ten_thanh_pho = "Ho Chi Minh City"
    url_co_so = "https://api.openweathermap.org/data/2.5/weather?"
    url_api = url_co_so + "appid=" + khoa_api + "&q=" + ten_thanh_pho

    ket_qua = goi_va_phan_tich_api(url_api)

    if ket_qua:
        print("\nKết quả phân tích:")
        for ten, gia_tri in ket_qua.items():
            print(f"{ten.capitalize()}: {gia_tri}")