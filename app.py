from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# 允許跨網域請求 (CORS)，方便本地端的 HTML 檔案調用此 API
CORS(app)

# 模擬 2026 年真實市場數據（包含價格、螢幕大小、銷量、2026排名、規格）
MONITORS_DATA = [
    {
        "id": 1,
        "name": "LG UltraGear 27GR95QE",
        "brand": "LG",
        "size": 27,
        "price": 26900,
        "sales": 1450,
        "rank_2026": 1,
        "system_score": 98,
        "resolution": "2K QHD",
        "refresh_rate": "240Hz",
        "panel": "OLED"
    },
    {
        "id": 2,
        "name": "SAMSUNG Odyssey Odyssey G7",
        "brand": "SAMSUNG",
        "size": 32,
        "price": 18900,
        "sales": 1820,
        "rank_2026": 2,
        "system_score": 95,
        "resolution": "2K QHD",
        "refresh_rate": "240Hz",
        "panel": "VA 曲面"
    },
    {
        "id": 3,
        "name": "ASUS ROG Swift PG32UCDM",
        "brand": "ASUS",
        "size": 32,
        "price": 42900,
        "sales": 680,
        "rank_2026": 3,
        "system_score": 97,
        "resolution": "4K UHD",
        "refresh_rate": "240Hz",
        "panel": "QD-OLED"
    },
    {
        "id": 4,
        "name": "BenQ Mobiuz EX2710Q",
        "brand": "BenQ",
        "size": 27,
        "price": 8988,
        "sales": 2300,
        "rank_2026": 4,
        "system_score": 89,
        "resolution": "2K QHD",
        "refresh_rate": "165Hz",
        "panel": "IPS"
    },
    {
        "id": 5,
        "name": "GIGABYTE M34WQ",
        "brand": "GIGABYTE",
        "size": 34,
        "price": 12990,
        "sales": 1100,
        "rank_2026": 5,
        "system_score": 91,
        "resolution": "UWQHD",
        "refresh_rate": "144Hz",
        "panel": "IPS 帶魚屏"
    },
    {
        "id": 6,
        "name": "MSI G244F E2",
        "brand": "MSI",
        "size": 24,
        "price": 3990,
        "sales": 3400,
        "rank_2026": 6,
        "system_score": 85,
        "resolution": "FHD",
        "refresh_rate": "180Hz",
        "panel": "Rapid IPS"
    }
]

@app.route('/api/monitors', methods=['GET'])
def get_monitors():
    # 獲取前端傳過來的篩選參數
    size_filter = request.args.get('size', 'all')
    sort_by = request.args.get('sort', 'rank')
    
    filtered_data = MONITORS_DATA.copy()
    
    # 1. 執行螢幕大小尺寸篩選
    if size_filter != 'all':
        if size_filter == '34':
            filtered_data = [m for m in filtered_data if m['size'] >= 34]
        else:
            filtered_data = [m for m in filtered_data if m['size'] == int(size_filter)]
            
    # 2. 執行動態排序（價格、銷量、排名、評分）
    if sort_by == 'rank':
        filtered_data.sort(key=lambda x: x['rank_2026'])
    elif sort_by == 'price_asc':
        filtered_data.sort(key=lambda x: x['price'])
    elif sort_by == 'price_desc':
        filtered_data.sort(key=lambda x: x['price'], reverse=True)
    elif sort_by == 'sales':
        filtered_data.sort(key=lambda x: x['sales'], reverse=True)
    elif sort_by == 'score':
        filtered_data.sort(key=lambda x: x['system_score'], reverse=True)
        
    return jsonify(filtered_data)

if __name__ == '__main__':
    # 啟動本地端 Flask 伺服器，預設埠號為 5000
    app.run(debug=True, port=5000)
