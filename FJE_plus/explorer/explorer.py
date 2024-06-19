from .iterator import JsonIterator  # 导入JsonIterator迭代器类

class FunnyJsonExplorer:
    """
    有趣的 JSON 浏览器类，用于展示 JSON 数据。
    """
    def __init__(self, style, icon_family):
        """
        初始化 JSON 浏览器。
        
        参数:
        style (Strategy): 样式对象，用于定义数据展示的样式。
        icon_family (IconFamily): 图标族对象，包含用于展示节点的图标。
        """
        self.style = style
        self.icon_family = icon_family

    def show(self, data):
        """
        展示 JSON 数据。
        
        参数:
        data (dict or list): 要展示的 JSON 数据。
        """
        iterator = JsonIterator(data)
        self.style.draw(iterator, self.icon_family)
