# -*- coding: utf-8 -*-
import re
import json
from bs4 import BeautifulSoup


class Parser:
    def get(self, response, page=1, domain=''):

        channel = {
            'page': page,
            'page_patten': None,
            'movies': []
        }

        soup = BeautifulSoup(response, "html.parser")
        channel['page'] = 2

        for movie in soup.select('#main-content div.block div.block-content > div.row div.global-figure > a'):
            thumb = self.get_thumb(str(movie))
            title = movie.get('data-ctn').encode('utf-8')

            movie = {
                'id': movie.get('data-ela'),
                'label': title,
                'title': title,
                'realtitle': title,
                'thumb': thumb,
                'type': None
            }

            channel['movies'].append(movie)

        return channel

    def get_page_ajax(self, response, page=2, domain=''):
        channel = {
            'page': page,
            'page_patten': None,
            'movies': []
        }

        response = json.loads(response)

        channel['page'] = response['total_page']

        for movie in response['videos_list']:
            channel['movies'].append({
                # 'id': id,
                'id': movie['_id'],
                'label': movie['title'].encode("utf-8"),
                'title': movie['title_vie'].encode("utf-8"),
                'realtitle': movie['title_origin'],
                'thumb': movie['thumb'],
                'type': movie['duration'].encode("utf-8"),
                'intro': movie['description'].encode("utf-8"),
            })

        return channel

    def get_thumb(self, style):
        return re.search('background-image:url\((.*?)\)', style).group(1)

    def get_search(self, response):

        channel = {
            'page': 1,
            'page_patten': None,
            'movies': []
        }

        data = re.search(r'__NUXT__=(.*);', response)
        if not data:
            return channel

        data = json.loads(data.group(1))['data'][0]
        for movie in data['searchData']:
            channel['movies'].append({
                # 'id': id,
                'id': movie['_id'],
                'label': movie['title'].encode("utf-8"),
                'title': movie['title_vie'].encode("utf-8"),
                'realtitle': movie['title_origin'],
                'thumb': movie['thumb'],
                'type': '',
                'intro': '',
            })


        return channel
