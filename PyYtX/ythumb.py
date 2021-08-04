# Copyright (c) 2021 Itz-fork
# Part of PyYt Project

import os
import logging
import wget

from urllib.parse import urlparse, parse_qs

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class PyYtX:
    def get_thumb(url=None, download=False, path=None):
        url = url
        download = download
        if url is None:
            logging.error("Url Isn't Provided")
        # Getting Video Id from given Url
        logging.info("Getting Video ID From Url")
        Yt_Vid_Id = PyYtX.extract_video_id(url)
        if Yt_Vid_Id is None:
            logging.error("Given Url is not a Youtube Video Url")
            return
        try:
            # Video Urls
            max_thumb = f"https://img.youtube.com/vi/{Yt_Vid_Id}/maxresdefault.jpg"
            standered_thumb = f"https://img.youtube.com/vi/{Yt_Vid_Id}/sddefault.jpg"
            # Now processing url
            if download is False:
                return max_thumb, standered_thumb
            elif download is True:
                urls = [max_thumb, standered_thumb]
                PyYtX.download_thumbs(urls, path)
                return max_thumb, standered_thumb
        except Exception as e:
            logging.error(e)
    
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
    
    def download_thumbs(urls, path=None):
        pyytx_urls = urls
        # File Path
        if path is not None:
            path = path
        else:
            path = "pyytx_img"
        if not os.path.isdir(path):
            os.makedirs(path)
        pyytx_path = path
        for imgu in pyytx_urls:
            wget.download(imgu, out=pyytx_path)
        logging.info("Download Finished")
