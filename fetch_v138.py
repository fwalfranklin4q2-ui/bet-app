import json
from datetime import datetime, timezone

def analyze_match(home_odds: float, draw_odds: float, away_odds: float) -> dict:
    # 默认输出
    recommend = "观望"
    confidence = 50
    risk = "中"
    tag = "均势"

    # 规则1：主胜超低赔
    if home_odds <= 1.50:
        recommend = "胜"
        confidence = 78
        risk = "低"
        tag = "主稳胆"

    # 规则2：客胜超低赔
    elif away_odds <= 1.50:
        recommend = "负"
        confidence = 78
        risk = "低"
        tag = "客稳胆"

    # 规则3：主队优势较明显
    elif home_odds < 1.80 and draw_odds >= 3.50:
        recommend = "胜"
        confidence = 70
        risk = "中低"
        tag = "主胜趋势"

    # 规则4：客队优势较明显
    elif away_odds < 1.80 and draw_odds >= 3.50:
        recommend = "负"
        confidence = 70
        risk = "中低"
        tag = "客胜趋势"

    # 规则5：均势危险盘
    elif 2.30 <= home_odds <= 2.80 and 2.30 <= away_odds <= 2.80:
        recommend = "放弃"
        confidence = 35
        risk = "高"
        tag = "均势危险盘"

    # 规则6：平赔异常低，防平
    elif draw_odds <= 3.00:
        recommend = "防平"
        confidence = 55
        risk = "中高"
        tag = "平局警报"

    # 规则7：主队略优
    elif home_odds < away_odds:
        recommend = "胜"
        confidence = 60
        risk = "中"
        tag = "主队略优"

    # 规则8：客队略优
    elif away_odds < home_odds:
        recommend = "负"
        confidence = 60
        risk = "中"
        tag = "客队略优"

    return {
        "recommend": recommend,
        "confidence": confidence,
        "risk": risk,
        "tag": tag
    }


def main():
    # 先用你现在的演示数据，后面你再接真实抓取
    matches = [
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

    for match in matches:
        match["analysis"] = analyze_match(
            match["homeOdds"],
            match["drawOdds"],
            match["awayOdds"]
        )

    output = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "matches": matches
    }

    with open("data/odds.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
