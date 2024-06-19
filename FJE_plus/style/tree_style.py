from .strategy import Strategy  # 导入Strategy类

class TreeStyle(Strategy):
    """
    树形样式类，用于绘制树结构的树形表示。
    继承自Strategy类。
    """

    def draw(self, iterator, icon_family):
        """
        绘制树结构数据，使用指定的图标族渲染节点。
        
        参数:
        iterator (iterator): JSON 数据的迭代器。
        icon_family (IconFamily): 包含容器图标和叶子图标的图标族。
        """
        def _print_tree(iterator):
            """
            递归函数，用于打印树结构数据的每个节点。
            
            参数:
            iterator (iterator): 树结构数据的迭代器。
            """
            for parent, current, is_lasts in iterator:
                if parent is None:
                    _print_tree(iterator)  # 递归调用_print_tree函数处理子节点
                else:
                    # 根据当前节点是否为列表类型，选择对应的图标
                    icon = icon_family.get_leaf_icon() if not isinstance(current, list) else icon_family.get_container_icon()
                    parent_prefix = ""
                    connector = "└── " if is_lasts[-1] else "├── "
                    # 根据is_lasts列表中的布尔值判断当前行是否是最后一行
                    for is_last in is_lasts[:-1]:
                        parent_prefix += "    " if is_last else "│   "
                    # 根据节点类型打印不同格式的输出
                    if current is not None and not isinstance(current, list):
                        print(parent_prefix + connector + f"{icon} {parent}: {current}")
                    else:
                        print(parent_prefix + connector + f"{icon} {parent}")

        _print_tree(iterator)  # 调用内部函数_print_tree开始打印树形结构
