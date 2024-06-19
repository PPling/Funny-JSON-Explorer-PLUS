import json
import argparse
from explorer.builder import ExplorerBuilder
from explorer.factory import ExplorerFactory

def main():
    """
    主程序函数，用于解析命令行参数并展示JSON数据。

    命令行参数:
    - -f, --file: 要探索的JSON文件路径（必选参数）。
    - -s, --style: 要使用的样式名称，从配置文件中的'styles'选项中选择（必选参数）。
    - -i, --icon: 要使用的图标族名称，从配置文件中的'icon_families'选项中选择（必选参数）。
    """
    # 读取并加载配置文件config.json
    with open('config.json', encoding='utf-8') as config_file:
        config = json.load(config_file)

    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    
    # 添加命令行参数：要探索的JSON文件路径，必选参数
    parser.add_argument('-f', '--file', required=True, help='JSON file to explore')
    
    # 添加命令行参数：要使用的样式名称，必选参数，选项限定为配置文件中'styles'字典的键
    parser.add_argument('-s', '--style', required=True, choices=config['styles'].keys(), help='Style to use')
    
    # 添加命令行参数：要使用的图标族名称，必选参数，选项限定为配置文件中'icon_families'字典的键
    parser.add_argument('-i', '--icon', required=True, choices=config['icon_families'].keys(), help='Icon family to use')
    
    # 解析命令行参数
    args = parser.parse_args()

    # 打开并加载指定的JSON文件
    with open(args.file, encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # 创建ExplorerFactory实例
    factory = ExplorerFactory()
    
    # 创建ExplorerBuilder实例，传入ExplorerFactory实例作为构建器的参数
    builder = ExplorerBuilder(factory)
    
    # 使用ExplorerFactory加载配置文件中的图标族配置信息
    factory.load_icon_families(config['icon_families'])
    
    # 根据命令行参数中选定的样式名称获取实际样式名称
    style_name = config['styles'][args.style]
    
    # 获取命令行参数中选定的图标族名称
    icon_family_name = args.icon
    
    # 使用Builder根据样式名称和图标族名称构建Explorer实例
    explorer = builder.build(style_name, icon_family_name)
    
    # 使用构建好的Explorer实例展示指定的JSON数据
    explorer.show(data)

if __name__ == "__main__":
    main()
