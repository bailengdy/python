## 1️⃣ 同类型 key：int / str / tuple
# 例子 1：int key
print("----------------Example 1----------------")
d = {}
d[1] = "one"
d[1] = "uno"   # 覆盖前面的值
print(d)       # {1: 'uno'}
# 这里 1 == 1，hash(1) == hash(1)，所以只能有一个 key=1。

# 例子 2：str key（字符串）
print("----------------Example 2----------------")
d = {}
d["AAPL"] = 1
d["AAPL"] = 2
print(d)  # {'AAPL': 2}
# 同理，"AAPL" == "AAPL"，hash 也一样 → 覆盖。

# 例子 3：tuple key（常见用法：坐标、pair）
print("----------------Example 3----------------")
d = {}
d[(1, 2)] = "point A"
d[(1, 2)] = "point B"
print(d)        # {(1, 2): 'point B'}
print((1, 2) == (1, 2))      # True
print(hash((1, 2)) == hash((1, 2)))  # True
# 只要元组内部元素都可 hash，整个 tuple 就是合法 key。

## 2️⃣ 不同类型 key：相等就会“撞车”的情况
# 例子 4：1 和 1.0
print("----------------Example 4----------------")
print(1 == 1.0)             # True
print(hash(1), hash(1.0))   # 在 CPython 里是一样的
d = {}
d[1] = "int one"
d[1.0] = "float one"
print(d)  # {1: 'float one'} 或 {1.0: 'float one'}，但只有一个 key
# In Python, 1 and 1.0 compare equal and have the same hash,
# so they cannot coexist as distinct keys in a dict.

# 例子 5：True 和 1
print("----------------Example 5----------------")
print(True == 1)           # True
print(hash(True), hash(1)) # 一样
d = {}
d[True] = "bool true"
d[1] = "int one"
print(d)  # {True: 'int one'} 或 {1: 'int one'}，但只有一个 key
# 因为 bool 是 int 的子类：
isinstance(True, int)  # True
# 所以 True 和 1 做 key 实际上会“挤在一起”。

## 3️⃣ 不同类型 key：不相等，就可以共存
# 例子 6：1 和 "1"
print("----------------Example 6----------------")
print(1 == "1")     # False
d = {}
d[1] = "int one"
d["1"] = "string one"
print(d)
# {1: 'int one', '1': 'string one'}

# 例子 7：tuple vs str
print("----------------Example 7----------------")
print((1, 2) == "1,2")   # False
d = {}
d[(1, 2)] = "tuple key"
d["1,2"] = "string key"
print(d)
# {(1, 2): 'tuple key', '1,2': 'string key'}

## 4️⃣ 自定义对象作为 key（eq + hash）
# 例子 8：两个不同对象但逻辑上当作同一个 key
print("----------------Example 8----------------")
class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol
    def __eq__(self, other):
        if not isinstance(other, Ticker):
            return False
        return self.symbol == other.symbol
    def __hash__(self):
        return hash(self.symbol)
a = Ticker("AAPL")
b = Ticker("AAPL")
print(a == b)              # True
print(hash(a) == hash(b))  # True
d = {}
d[a] = "apple stock"
d[b] = "overwritten"
print(len(d))  # 1
