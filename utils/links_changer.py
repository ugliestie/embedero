import re
import logging

logger = logging.getLogger(__name__)

class InvalidQuery(Exception):
    pass

class NotSupported(Exception):
    pass

link_pattern = re.compile(
    r"(http:\/\/|https:\/\/)?[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*(\.[a-zA-Z0-9]{1,10})((\/+)[^\/ ]*)*"
)

twitter_pattern = re.compile(
	r"(?:(?:https?):\/\/)?(?:www.)?twitter\.com\/(@?(\w){1,15})\/status\/([0-9]{19})(\?\S+)?"
)

x_pattern = re.compile(
	r"(?:(?:https?):\/\/)?(?:www.)?x\.com\/(@?(\w){1,15})\/status\/([0-9]{19})(\?\S+)?"
)

instagram_pattern = re.compile(
    r"(?:(?:https?):\/\/)(?:www\.)?instagram\.com\/(?:(?:((?:reel)|p)\/(\w+))|((stories)\/(\w+)\/\d+))(?:\/\?\S+)"
)

pinterest_pattern = re.compile(
    r"(?:https:\/\/)(?:.+)?pinterest\.com\/pin\/([0-9]+)\/?"
)

bluesky_pattern = re.compile(
    r"(?:https:\/\/)(?:.+)?bsky\.app\/profile\/(\S+)\/post\/([A-Za-z0-9]+)"
)

async def change_link(query: str):
    if re.search(link_pattern, query):
        if re.search(twitter_pattern, query):
            link = re.search(twitter_pattern, query)
            return f"fxtwitter.com/{link.group(1)}/status/{link.group(3)}"
        elif re.search(x_pattern, query):
            link = re.search(x_pattern, query)
            return f"fxtwitter.com/{link.group(1)}/status/{link.group(3)}"
        elif re.search(instagram_pattern, query):
            link = re.search(instagram_pattern, query)
            return f"fxstagram.com/{link.group(1)}/{link.group(2)}"
        elif re.search(pinterest_pattern, query):
            link = re.search(pinterest_pattern, query)
            return f"pinterestez.com/pin/{link.group(1)}"
        elif re.search(bluesky_pattern, query):
            link = re.search(bluesky_pattern, query)
            return f"boobsky.app/profile/{link.group(1)}/post/{link.group(2)}"
        else:
            raise NotSupported
    else:
        raise InvalidQuery