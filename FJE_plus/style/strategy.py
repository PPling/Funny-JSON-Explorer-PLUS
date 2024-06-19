from abc import ABC, abstractmethod  # 导入抽象基类（ABC）和抽象方法（abstractmethod）

class Strategy(ABC):
    """
    抽象策略类，用于定义绘制策略的接口。
    继承自ABC类，表示这是一个抽象基类。
    """

    @abstractmethod
    def draw(self, iterator, icon_family):
        """
        抽象方法：绘制方法，子类必须实现该方法来定义具体的绘制策略。
        
        参数:
        iterator (iterator): 绘制所需的数据迭代器。
        icon_family (IconFamily): 包含容器图标和叶子图标的图标族对象。
        """
        pass  # 子类必须实现draw方法来定义具体的绘制逻辑
