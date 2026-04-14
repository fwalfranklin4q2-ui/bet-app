import json
from datetime import datetime

def fetch_mock_data():
    return [
        {
            "id": "2006",
            "home": "博卡青年",
            "away": "巴塞罗那",
            "league": "解放者杯",
            "homeOdds": 1.26,
            "drawOdds": 4.40,
            "awayOdds": 9.30,
            "note": "稳胆"
        },
        {
            "id": "2007",
            "home": "基多大学",
            "away": "米拉索尔",
            "league": "解放者杯",
            "homeOdds": 1.69,
            "drawOdds": 3.40,
            "awayOdds": 4.10,
            "note": "次稳"
        }
    ]

def main():
    output = {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "matches": fetch_mock_data()
    }

    with open("data/odds.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("odds.json 已更新")

if __name__ == "__main__":
    main()
