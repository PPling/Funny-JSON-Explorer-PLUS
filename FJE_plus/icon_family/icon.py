class IconFamily:
    def __init__(self, name, container, leaf):
        """
        初始化图标族对象。
        
        参数:
        name (str): 图标族的名称。
        container (str): 容器图标的表示字符串。
        leaf (str): 叶子图标的表示字符串。
        """
        self.name = name
        self.container = container
        self.leaf = leaf

    def get_container_icon(self):
        """
        获取容器图标。
        
        返回:
        str: 容器图标的表示字符串。
        """
        return self.container

    def get_leaf_icon(self):
        """
        获取叶子图标。
        
        返回:
        str: 叶子图标的表示字符串。
        """
        return self.leaf

class IconFamilyManager:
    def __init__(self):
        """
        初始化图标族管理器。
        """
        self.icon_families = {}

    def add_icon_family(self, name, container, leaf):
        """
        添加图标族到管理器中。
        
        参数:
        name (str): 图标族的名称。
        container (str): 容器图标的表示字符串。
        leaf (str): 叶子图标的表示字符串。
        """
        self.icon_families[name] = IconFamily(name, container, leaf)

    def get_icon_family(self, name):
        """
        根据名称获取指定的图标族。
        
        参数:
        name (str): 图标族的名称。
        
        返回:
        IconFamily or None: 如果找到则返回对应的图标族对象，否则返回None。
        """
        return self.icon_families.get(name, None)

    def get_all_icon_families(self):
        """
        获取所有已添加的图标族。
        
        返回:
        dict: 包含所有图标族对象的字典，键为图标族名称，值为IconFamily对象。
        """
        return self.icon_families
