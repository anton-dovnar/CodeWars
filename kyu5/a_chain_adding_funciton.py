class ChainAddition(int):
    def __call__(self, value):
        return ChainAddition(self + value)

add = ChainAddition
