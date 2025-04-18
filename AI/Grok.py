import requests

# Thay bằng API Key thực tế từ https://aimlapi.com/app/keys
API_KEY = "cefb7ea2d624411585ffb2ad94367061"
URL = "https://api.aimlapi.com/v1/chat/completions"  # Endpoint của AIMLAPI

# Cấu hình headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Cấu hình payload
payload = {
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # Mô hình hợp lệ
    "messages": [
        {"role": "user", "content": "Xin chào, bạn khỏe không?"}  # Có thể đổi sang tiếng Anh nếu cần
    ],
    "max_tokens": 100,
    "temperature": 0.7
}

# Gửi yêu cầu POST
response = requests.post(URL, headers=headers, json=payload)

# Xử lý phản hồi
if response.status_code in (200, 201):  # Chấp nhận cả 200 và 201
    data = response.json()
    print("Kết quả:", data["choices"][0]["message"]["content"])
else:
    print("Lỗi:", response.status_code, response.text)
    print("Chi tiết lỗi:", response.json())