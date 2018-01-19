
class Movie:
    title       = ""    # 名字
    actors      = []    # 主演列表
    director    = []    # 导演列表
    duration    = ""    # 时长
    rate        = 0.0   # 豆瓣评分
    region      = ""    # 产地
    release     = ""    # 上映年份
    cover       = ""    # 电影封面
    trailer     = ""    # 相关视频地址
    threadUrl   = ""    # 豆瓣链接地址


    def __str__(self):
        return self.title +"\n" \
                + self.duration + "\n" \
                + self.region + "\n" \
                + self.release + "\n\n\n"



# data-actors="章子怡 / 黄晓明 / 张震"
# data-director="李芳芳"
# data-dstat-areaid="70_1"
# data-dstat-mode="click,expose"
# data-dstat-viewport=".screening-bd"
# data-dstat-watch=".ui-slide-content"
# data-duration="138分钟"
# data-enough="true"
# data-intro=""
# data-rate="7.4"
# data-rater="99901"
# data-region="中国大陆"
# data-release="2018"
# data-star="40"
# data-ticket="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F71946%3F_v_%3Dyes%26merCode%3D1000011"
# data-title="无问西东"
# data-trailer="https://movie.douban.com/subject/6874741/trailer">

