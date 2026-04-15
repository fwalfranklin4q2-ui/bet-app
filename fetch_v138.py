import json
from datetime import datetime

def fetch_matches():
    return [
        {
            "id": "3005",
            "home": "阿森纳",
            "away": "葡萄牙体",
            "league": "欧冠",
            "homeOdds": 1.36,
            "drawOdds": 4.25,
            "awayOdds": 6.3,
            "note": "主稳"
        },
        {
            "id": "3006",
            "home": "拜仁",
            "away": "皇马",
            "league": "欧冠",
            "homeOdds": 1.46,
            "drawOdds": 4.85,
            "awayOdds": 4.2,
            "note": "强强对话"
        },
        {
            "id": "3007",
            "home": "弗鲁米嫩",
            "away": "里瓦达维",
            "league": "解放者杯",
            "homeOdds": 1.44,
            "drawOdds": 3.7,
            "awayOdds": 6.1,
            "note": "主胜趋势"
        }
    ]

def save():
    data = {
        "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "matches": fetch_matches()
    }

    with open("data/odds.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    save()
