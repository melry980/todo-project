todos = [
    {"title": "レポートを提出する", "completed": False, "priority": "高"},
    {"title": "教科書を返却する", "completed": True, "priority": "中"},
]


def show_todos():
    print("TODO一覧")
    print("状態と優先度：高・中・低／[完了]は完了済み")
    
    # 1. 未完了のTODOを表示するループ
    for todo in todos:
        if not todo["completed"]:
            print(f'- {todo["title"]} [{todo["priority"]}]')
            
    # 2. 完了したTODOを表示するループ（[完了]をつける）
    for todo in todos:
        if todo["completed"]:
            print(f'- [完了] {todo["title"]} [{todo["priority"]}]')


show_todos()