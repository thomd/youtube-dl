# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor


class EventedMindIE(InfoExtractor):
    _VALID_URL = r'https://www\.eventedmind\.com/classes/(?P<id>[\w\d-]+)$'
    _TEST = {
        'url': 'https://www.eventedmind.com/classes/oauth-from-scratch-98a98727',
        'info_dict': {
            'id': 'oauth-from-scratch-98a98727',
            'title': 'OAuth From Scratch'
        },
        'playlist_count': 6
    }

    def _real_extract(self, url):
        playlist_id = self._match_id(url)

        webpage = self._download_webpage(url, playlist_id)
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')
        description = self._html_search_regex(r'<p>(.*?)\s</p>', webpage, 'description', fatal=False)
        links = re.findall(r'<li class="item video-item class-item">\s*?<a href="([^"]+)">', webpage)
        urls = map(lambda link: 'https://www.eventedmind.com' + re.sub(r'classes/[^/]+', 'items', link) + '/media.mp4', links)
        entries = [self.url_result(u) for u in urls]

        return {
            '_type': 'playlist',
            'id': playlist_id,
            'title': title,
            'description': description,
            'entries': entries,
        }
