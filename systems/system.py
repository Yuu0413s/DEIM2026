import numpy as np
from dataclasses import dataclass
from enum import Enum

# 定数の定義（単位：日）
DAY = 1
WEEK = 7
MONTH = 30
YEAR = 365

class ScheduleType(Enum):
    PERIODICAL = "Periodical_Rec"  # 中長期的な配置（例：月次レポート、年次更新）
    DAILY = "Daily_Rec"            # 日々の隙間時間への配置（例：ルーチン、短期課題）
    MANUAL = "Manual_Review"       # 自動化対象外（例外処理）

@dataclass
class Task:
    name: str
    interval_days: float  # n: 頻度（何日に1回発生するか）
    duration_hours: float # m: 所要時間

    # 個人の特性データなどをここに持たせることも可能
    # priority: int
    # preferred_time: str

class TaskScheduler:
    def __init__(self):
        pass

    def classify_task_strategy(self, task: Task) -> ScheduleType:
        """
        タスクの頻度(n)に基づいてスケジューリング戦略を決定する
        数式:
        - 1/month < n < 1/year -> Periodical
        - n < 1/week or n < 1/month -> Daily
        注: ここでは n を「発生間隔(日数)」として実装します。
        """
        n = task.interval_days

        # 頻度が低い（間隔が長い）：1ヶ月〜1年の間
        # 条件: 1/month < n < 1/year (記述の意図を「月1回より稀、年1回より頻繁」と解釈)
        if MONTH < n <= YEAR:
            return ScheduleType.PERIODICAL

        # 頻度が高い（間隔が短い）：週1回未満、あるいは月1回未満
        # 条件: n < 1/month ... Daily
        elif n <= MONTH:
            return ScheduleType.DAILY

        else:
            # 1年以上の間隔など
            return ScheduleType.MANUAL

    def optimize(self, task: Task):
        strategy = self.classify_task_strategy(task)

        print(f"Task: {task.name} (Interval: {task.interval_days} days, Duration: {task.duration_hours}h)")
        print(f"Selected Strategy: {strategy.value}")

        if strategy == ScheduleType.PERIODICAL:
            self._run_periodical_optimization(task)
        elif strategy == ScheduleType.DAILY:
            self._run_daily_optimization(task)
        print("-" * 30)

    def _run_periodical_optimization(self, task):
        # ここに「長期カレンダー」の空き状況と「締切」に基づくロジックを記述
        print(">> Running logic for Long-term Calendar Planning...")
        # TODO: 過去の履歴から「月初」や「月末」など傾向を抽出して配置

    def _run_daily_optimization(self, task):
        # ここに「個人の集中時間帯」や「日々の空きスロット」に基づくロジックを記述
        print(f">> Running logic for Daily Slot Optimization (Allocating {task.duration_hours} hours)...")
        # TODO: 朝型・夜型データと照らし合わせて最適な時間帯をレコメンド

# --- 実行例 ---
scheduler = TaskScheduler()

# ケース1: 年に数回のイベント（例：学期末レポート作成） -> n = 90日 (3ヶ月に1回)
task1 = Task(name="Quarterly Report", interval_days=90, duration_hours=5.0)
scheduler.optimize(task1)

# ケース2: 週次の課題（例：プログラミング課題） -> n = 7日
task2 = Task(name="Weekly Coding", interval_days=7, duration_hours=2.0)
scheduler.optimize(task2)

# ケース3: 毎日のルーチン（例：メールチェック） -> n = 1日
task3 = Task(name="Daily Email", interval_days=1, duration_hours=0.5)
scheduler.optimize(task3)