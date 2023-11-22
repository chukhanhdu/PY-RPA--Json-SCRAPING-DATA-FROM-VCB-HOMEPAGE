import json

data = {
    "スコア一覧": [
        {
            "科目": "英語",
            "得点": 80,
            "評価": "優"
        },
        {
            "科目": "数学",
            "得点": 70,
            "評価": "良"
        }
    ]
}

for sub in data["スコア一覧"]:
    monhoc = sub["科目"]
    diemso = sub["得点"]
    danhgia=sub["評価"]
    print(f"科目: {monhoc}")

