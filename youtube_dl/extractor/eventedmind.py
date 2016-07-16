# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor


class EventedMindIE(InfoExtractor):
    _VALID_URL = r'https://www\.eventedmind\.com/classes/(?P<id>[\w\d-]+)$'
    _TEST = {
        'url': 'http://yourextractor.com/watch/42',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'Video title goes here',
            'thumbnail': 're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
	video_id = self._match_id(url)

	webpage = self._download_webpage(url, video_id)
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')
        print "Title of Class: %s" % title




        return {
            # 'id': video_id,
            # 'title': title,
            # 'description': self._og_search_description(webpage),
            # 'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
