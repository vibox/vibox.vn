# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class Parser:
    def get(self, response, page):

        channel = {
            'page': page,
            'page_patten': None,
            'movies': []
        }

        soup = BeautifulSoup(response, "html.parser")
        # get total page
        next_page = soup.select_one('a.more-btn.yellow-btn.btn-nav')
        print("*********************** Get pages ")
        if next_page is not None:
            channel['page'] = int(page)+1

        for movie in soup.select('div.flex-wrap-movielist > a.movie-item'):

            title = movie.select_one('div.title-in h6').text.strip()
            try:
                type = movie.select_one('div.badget-eps').text.strip()
            except:
                type = "HD"

            label = "[%s] %s" % (type, title)
            thumb = movie.select_one('div.mv-img').get('data-original')

            channel['movies'].append({
                'id': movie.get('href'),
                'label': label.encode("utf-8"),
                'title': title.encode("utf-8"),
                'realtitle': title.encode("utf-8"),
                'thumb': thumb,
                'type': type.encode("utf-8"),
            })

        return channel