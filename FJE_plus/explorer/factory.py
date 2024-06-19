import importlib  # 导入模块动态加载功能
from icon_family.icon import IconFamilyManager  # 导入图标族管理器
from style.tree_style import TreeStyle  # 导入树形样式类
from style.rectangle_style import RectangleStyle  # 导入矩形样式类

class StyleFactory:
    """
    样式工厂类，用于创建不同类型的样式对象。
    """
    def create_style(self, style_name):
        """
        根据样式名称创建对应的样式对象。
        
        参数:
        style_name (str): 样式名称，支持 "TreeStyle" 和 "RectangleStyle"。
        
        返回:
        Strategy: 根据样式名称创建的样式对象，可能是TreeStyle或RectangleStyle的实例。
        
        异常:
        ValueError: 如果传入未知的样式名称，则抛出异常。
        """
        if style_name == "TreeStyle":
            return TreeStyle()
        elif style_name == "RectangleStyle":
            return RectangleStyle()
        else:
            raise ValueError(f"Unknown style: {style_name}")

class IconFamilyFactory:
    """
    图标族工厂类，用于创建和管理图标族对象。
    """
    def __init__(self):
        """
        初始化图标族工厂，创建图标族管理器。
        """
        self.manager = IconFamilyManager()

    def create_icon_family(self, icon_family_name, icons):
        """
        创建并添加图标族到图标族管理器中。
        
        参数:
        icon_family_name (str): 图标族的名称。
        icons (dict): 包含 'icon_container' 和 'icon_leaf' 键的字典，表示容器和叶子图标的字符串。
        """
        self.manager.add_icon_family(icon_family_name, icons['icon_container'], icons['icon_leaf'])

    def get_icon_family(self, icon_family_name):
        """
        获取指定名称的图标族对象。
        
        参数:
        icon_family_name (str): 图标族的名称。
        
        返回:
        IconFamily or None: 如果找到则返回对应的图标族对象，否则返回None。
        """
        return self.manager.get_icon_family(icon_family_name)

    def load_icon_families(self, icon_families_config):
        """
        根据配置加载多个图标族到图标族管理器中。
        
        参数:
        icon_families_config (dict): 包含多个图标族配置的字典，键为图标族名称，值为包含 'icon_container' 和 'icon_leaf' 键的字典。
        """
        for name, icons in icon_families_config.items():
            self.create_icon_family(name, icons)

class ExplorerFactory:
    """
    资源管理器工厂类，负责创建资源管理器和加载相关资源。
    """
    def __init__(self):
        """
        初始化资源管理器工厂，创建样式工厂和图标族工厂。
        """
        self.style_factory = StyleFactory()
        self.icon_family_factory = IconFamilyFactory()

    def create_style(self, style_name):
        """
        根据样式名称创建对应的样式对象。
        
        参数:
        style_name (str): 样式名称，支持 "TreeStyle" 和 "RectangleStyle"。
        
        返回:
        Strategy: 根据样式名称创建的样式对象，可能是TreeStyle或RectangleStyle的实例。
        
        异常:
        ValueError: 如果传入未知的样式名称，则抛出异常。
        """
        return self.style_factory.create_style(style_name)

    def load_icon_families(self, icon_families_config):
        """
        根据配置加载多个图标族到图标族管理器中。
        
        参数:
        icon_families_config (dict): 包含多个图标族配置的字典，键为图标族名称，值为包含 'icon_container' 和 'icon_leaf' 键的字典。
        """
        self.icon_family_factory.load_icon_families(icon_families_config)

    def get_icon_family(self, icon_family_name):
        """
        获取指定名称的图标族对象。
        
        参数:
        icon_family_name (str): 图标族的名称。
        
        返回:
        IconFamily or None: 如果找到则返回对应的图标族对象，否则返回None。
        """
        return self.icon_family_factory.get_icon_family(icon_family_name)
