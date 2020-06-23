import json

class DoubanSpider:
    def __init__(self):
        # "https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start=0"
        # "https://movie.douban.com/j/search_subjects?type=tv&tag=美剧&sort=recommend&page_limit=20&page_start=0"
        # "https://movie.douban.com/j/search_subjects?type=tv&tag=国产剧&sort=recommend&page_limit=20&page_start=0"
        self.url_temp_list = ["https://movie.douban.com/j/search_subjects?type=tv&tag=%E8%8B%B1%E5%89%A7&sort=recommend&page_limit=20&page_start=0",
                              "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0",
                              "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"]

