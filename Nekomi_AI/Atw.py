class NekoNum:
    def __init__(self, data):
        # 入力検証
        if not all(isinstance(row, list) for row in data):
            raise ValueError("All rows must be lists")
        if len(set(len(row) for row in data)) > 1:
            raise ValueError("All rows must have the same length")
        
        self.data = data

    def shape(self):
        if not self.data or not self.data[0]:
            return (0, 0)  # 空の行列に対応
        return len(self.data), len(self.data[0])  # 2Dの例

    def sum(self):
        return sum(map(sum, self.data))

    def transpose(self):
        return [list(row) for row in zip(*self.data)]
