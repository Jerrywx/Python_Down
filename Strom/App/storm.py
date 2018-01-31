
import sys
from enum import Enum
import urllib
from urllib.parse import quote, unquote, urlencode
# from urllib import quote

# 导入数据库管理部分
sys.path.append("../sqlManager")
# import dataManager
from dataManager import *


class MovieClass(Enum):
    Hot         = "热门"
    New         = "最新"
    Classic     = "经典"
    Play        = "可播放"
    Top         = "豆瓣高分"
    Dark        = "冷门佳片"
    Chinese     = "华语"
    America     = "欧美"
    Korean      = "韩国"
    Japan       = "日本"
    Action      = "动作"
    Comedy      = "喜剧"
    Love        = "爱情"
    Science     = "科幻"
    Suspense    = "悬疑"
    Terrify     = "恐怖"
    Cure        = "治愈"

# 程序
def main():
    print("This is Main")

    # for name in MovieClass:
    #     print(name)

    for name, member in MovieClass.__members__.items():
        print(name, '\t=>\t', member.value)

    # print(MovieClass.Sun)
    # print(MovieClass.Sat)

    # type = ["热门", "最新", "经典", "可播放", "豆瓣高分",
    #         "冷门佳片", "华语", "欧美", "韩国", "日本",
    #         "动作", "喜剧", "爱情", "科幻", "悬疑", "恐怖", "治愈"]
    #
    # for key in type:
    #     print(key + ":" + quote(key))

    # dataManager.createForm()
    # createForm()



if __name__ == '__main__':
    main()
