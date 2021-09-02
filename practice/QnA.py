# 問答程式 > 選擇題

# 引用方式 有兩種
from question import Question # 從 question.py 只 import Question 這個 class
# import question # 從 question.py import 整個 question.py 的內容

# 設計選擇題列表
test = [
    "1 + 3 = ?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色?\n(a) 綠色\n(b) 黃色\n(c) 紅色\n\n"
]

# 引用 Question 這個 class 傳入必要資訊 問題描述 與 答案 兩個必須參數 存入 questions list 內
questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
    ]

# 定義答題程式
def run_test(questions): # 定義必要參數 questions
    score = 0 # score 從 0 起算
    for question in questions: 
        # 從 questions list 依序讀取 在 line 15 傳給 Question 這個類別必要的資料
        answer = input(question.description) 
        # 賦值 answer 來接受 input 並傳給 question.py 的 description 屬性
        if answer == question.answer: 
            # 如果 input 的值 等於 question.py 的 answer 屬性在 line 15 接收到的值
            score += 1 # 分數 由原本 + 1
    print("你得到" + str(score) + "分, 共" + str(len(questions)) + "題")
    # 印出所得分數

run_test(questions) # 執行答題程式