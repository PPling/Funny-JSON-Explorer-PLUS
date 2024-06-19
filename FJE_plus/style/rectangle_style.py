from .strategy import Strategy  # 导入Strategy策略类

class RectangleStyle(Strategy):
    """
    矩形样式类，用于绘制树结构的矩形表示。
    继承自Strategy类，实现了绘制矩形样式树结构的方法。
    """

    def draw(self, iterator, icon_family):
        """
        绘制树结构数据，使用指定的图标族渲染节点。
        
        参数:
        iterator (iterator): JSON 数据的迭代器。
        icon_family (IconFamily): 包含容器图标和叶子图标的图标族。
        """
        def _print_tree(iterator, is_first=False):
            """
            递归函数，用于打印树结构数据的每个节点。
            
            参数:
            iterator (iterator): 树结构数据的迭代器。
            is_first (bool): 是否为第一个节点，影响连接符和前缀的输出格式。
            """
            for parent, current, is_lasts in iterator:
                if parent is None:
                    _print_tree(iterator, True)  # 递归调用_print_tree函数处理子节点，第一个节点特殊处理
                else:
                    # 根据节点位置确定连接符和前缀
                    if is_first:
                        connector = "┌─"
                        next_prefix = "|   "
                        end_str = "┐"
                        is_first = False
                    elif is_lasts.count(True) == len(is_lasts) and not isinstance(current, list):
                        connector = "└─"
                        next_prefix = "    "
                        end_str = "┘"
                    else:
                        connector = "├─"
                        next_prefix = "|   "
                        end_str = "┤"
                    
                    # 根据is_lasts列表中的布尔值生成父节点前缀
                    parent_prefix = "│   " * (len(is_lasts) - 1)
                    if is_lasts.count(True) == len(is_lasts) and not isinstance(current, list):
                        parent_prefix = "└───" * (len(is_lasts) - 1)
                    
                    # 根据节点类型打印不同格式的输出
                    if isinstance(current, list):
                        print(parent_prefix + connector + f" {icon_family.get_container_icon()} {parent} " + "─" * (40 - len(parent_prefix) - len(connector) - len(parent) - 1) + end_str)
                    else:
                        if current is not None:
                            print(parent_prefix + connector + f" {icon_family.get_leaf_icon()} {parent} : {current} " + "─" * (40 - len(parent_prefix) - len(connector) - len(parent) - len(current) - 4) + end_str)
                        else:
                            print(parent_prefix + connector + f" {icon_family.get_leaf_icon()} {parent} " + "─" * (40 - len(parent_prefix) - len(connector) - len(parent) - 1) + end_str)

        _print_tree(iterator)  # 调用内部函数_print_tree开始打印矩形样式的树形结构
