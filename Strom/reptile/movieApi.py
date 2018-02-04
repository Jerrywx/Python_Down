

##################################################################################################################
#                                           豆瓣API
##################################################################################################################


# ----------------------------------------------------------- DouBan URL
# https://developers.douban.com/wiki/?title=movie_v2#reviews
# 基地址
baseApi     = "https://api.douban.com"


# ----------------------------------------------------------- 搜索
# 电影条目搜索
searchApi   = "/v2/movie/search?q={text}"
# GET /v2/movie/search?q=张艺谋 GET /v2/movie/search?tag=喜剧


# ----------------------------------------------------------- 榜单
# 正在上映
inTheaters      = "/v2/movie/in_theaters"

# 即将上映
comingSoon      = "/v2/movie/coming_soon"

# Top250
top250          = "/v2/movie/top250"

# 口碑榜
weekly          = "/v2/movie/weekly"

# 新片榜
newMovies       = "/v2/movie/new_movies"

# ----------------------------------------------------------- 电影条目

# 电影条目信息
movieInfo       = "/v2/movie/subject/{id}"
# Example: GET /v2/movie/subject/1764796

# 电影条目剧照
moviePhotos     = "/v2/movie/subject/{id}/photos"
# Example: GET /v2/movie/subject/1054395/photos


# ----------------------------------------------------------- 影人条目
# 影人条目信息
celebrity = "/v2/movie/celebrity/{id}"
# Example: GET /v2/movie/celebrity/1054395

# 影人剧照
photos  = "/v2/movie/celebrity/{id}/photos"
# Example: GET /v2/movie/celebrity/1054395/photos

# 影人作品
works = "/v2/movie/celebrity/{id}/works"
# Example: GET /v2/movie/celebrity/1054395/works


# ----------------------------------------------------------- 影集
# 影集
movieList = "https://movie.douban.com/ithil_j/activity/movie_annual{year}/widget/{tip}"
# https://movie.douban.com/ithil_j/activity/movie_annual2017/widget/3

























