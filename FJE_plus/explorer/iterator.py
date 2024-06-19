import copy

class JsonIterator:
    """
    JSON 迭代器类，用于遍历和展开嵌套的 JSON 数据结构。
    """
    def __init__(self, data):
        """
        初始化 JSON 迭代器。
        
        参数:
        data (dict or list): 要遍历的 JSON 数据。
        """
        self.stack = [(None, data, [])]  # (parent, current, is_lasts)
    
    def __iter__(self):
        """
        返回迭代器自身，以便支持迭代协议。
        """
        return self
    
    def __next__(self):
        """
        获取迭代器的下一个元素。
        
        返回:
        tuple: 包含父节点、当前节点及其在层级中的位置信息的元组。
        
        抛出:
        StopIteration: 如果没有更多元素时抛出此异常。
        """
        while self.stack:
            parent, current, is_lasts = self.stack.pop()
            if isinstance(current, dict):
                items = list(current.items())
                # 将字典的键值对按照逆序压入栈中，并记录每个节点在当前层级中的位置
                self.stack.extend(reversed([(key, value, is_lasts + [(i == len(items) - 1)]) for i, (key, value) in enumerate(items)]))
                return parent, items, is_lasts
            elif parent is not None:
                return parent, current, is_lasts
        # 如果栈为空，表示没有更多元素可以迭代，抛出StopIteration异常
        raise StopIteration
