import re
import logging

logger = logging.getLogger(__name__)

twitter_pattern = re.compile(
	r"((https?):\/\/)?(www.)?(twitter)\.com(\/@?(\w){1,15})\/status\/[0-9]{19}\?"
)

x_pattern = re.compile(
	r"((https?):\/\/)?(www.)?(x)\.com(\/@?(\w){1,15})\/status\/[0-9]{19}\?"
)

instagram_pattern = re.compile(
    r"https?:\/\/(?:www\.)?instagram\.com\/(?:(?:((?:reels)|p)\/(\w+))|((stories)\/(\w+)\/\d+))"
)

pinterest_pattern = re.compile(
    r"pinterest\.com\/pin\/[0-9]+"
)

"""
sorry this is for me lol

example_pattern = re.compile(
    r""
)
"""

async def change_link(query: str):
    if re.search(twitter_pattern, query):
        return re.search(twitter_pattern, query).string.replace('twitter.com', 'fxtwitter.com')
    elif re.search(x_pattern, query):
        return re.search(x_pattern, query).string.replace('x.com', 'fxtwitter.com')
    elif re.search(instagram_pattern, query):
        return re.search(instagram_pattern, query).string.replace('instagram.com', 'fxstagram.com')
    elif re.search(pinterest_pattern, query):
        return re.search(pinterest_pattern, query).string.replace('pinterest.com', 'pinterestez.com')
    else:
        raise Exception("None of supported links")