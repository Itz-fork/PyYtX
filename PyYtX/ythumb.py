# Copyright (c) 2021 Itz-fork
# Part of PyYt Project

import logging
from urllib.parse import urlparse, parse_qs

logger = logging.getLogger(__name__)

class PyYtX:
    def get_thumb(url=None):
        url = url
        if url is None:
            logging.error("Url Isn't Provided")
        # Getting Video Id from given Url
        logging.info("Getting Video ID From Url")
        Yt_Vid_Id = PyYtX.extract_video_id(url)
        if Yt_Vid_Id is None:
            logging.error("Given Url is not a Youtube Url")
        else:
            max_thumb = f"https://img.youtube.com/vi/{Yt_Vid_Id}/maxresdefault.jpg"
            standered_thumb = f"https://img.youtube.com/vi/{Yt_Vid_Id}/sddefault.jpg"
            return max_thumb, standered_thumb
    
    def extract_video_id(url):
        query = urlparse(url)
        try:
            if query.hostname == 'youtu.be': return query.path[1:]
            if query.hostname in {'www.youtube.com', 'youtube.com'}:
                if query.path == '/watch': return parse_qs(query.query)['v'][0]
                if query.path[:7] == '/watch/': return query.path.split('/')[1]
                if query.path[:7] == '/embed/': return query.path.split('/')[2]
                if query.path[:3] == '/v/': return query.path.split('/')[2]
        except:
            return None