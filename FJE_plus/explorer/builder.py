from .explorer import FunnyJsonExplorer  # 导入FunnyJsonExplorer类

class ExplorerBuilder:
    """
    资源管理器构建器类，用于构建具有特定样式和图标族的 FunnyJsonExplorer 对象。
    """
    def __init__(self, factory):
        """
        初始化资源管理器构建器。
        
        参数:
        factory (ExplorerFactory): 资源管理器工厂对象，用于创建样式和图标族。
        """
        self.factory = factory

    def build(self, style_name, icon_family_name):
        """
        构建具有特定样式和图标族的 FunnyJsonExplorer 对象。
        
        参数:
        style_name (str): 样式名称，用于指定 JSON 数据展示的样式。
        icon_family_name (str): 图标族名称，用于指定 JSON 数据展示时的图标样式。
        
        返回:
        FunnyJsonExplorer: 构建的 FunnyJsonExplorer 对象，用于展示 JSON 数据。
        
        异常:
        ValueError: 如果未找到指定的图标族名称，则抛出异常。
        """
        style = self.factory.create_style(style_name)
        icon_family = self.factory.get_icon_family(icon_family_name)
        if not icon_family:
            raise ValueError(f"Icon family '{icon_family_name}' not found.")
        return FunnyJsonExplorer(style, icon_family)
