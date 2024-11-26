class NekoNum:
    def __init__(self, data):
        self.data = data

    def shape(self):
        return len(self.data), len(self.data[0])  # 2Dの例

    def sum(self):
        return sum(sum(row) for row in self.data)

    def transpose(self):
        return [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
