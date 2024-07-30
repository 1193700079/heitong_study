class FixedSizeList(list):
    def __init__(self, maxlen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxlen = maxlen

    def append(self, item):
        if len(self) >= self.maxlen:
            self.pop(0)  # 删除第一个元素
        super().append(item)
