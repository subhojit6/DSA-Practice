class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1

        while self.stack and price > self.stack[-1][0]:
            previous_price, previous_span = self.stack.pop()
            span += previous_span
            
        self.stack.append((price, span))

        return span
        
obj = StockSpanner()
param_1 = obj.next(100)
print(param_1)