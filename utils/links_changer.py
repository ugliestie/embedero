import re
import logging

logger = logging.getLogger(__name__)

class InvalidQuery(Exception):
    pass

class NotSupported(Exception):
    pass

link_pattern = re.compile(
    r"^(http:\/\/|https:\/\/)?[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*(\.[a-zA-Z0-9]{1,10})((\/+)[^\/ ]*)*$"
)

twitter_pattern = re.compile(
	r"(?:(?:https?):\/\/)?(?:www.)?(?:twitter|x)\.com\/(@?(\w){1,15})\/status\/([0-9]{19})(\?\S+)?"
)

instagram_pattern = re.compile(
    r"(?:(?:https?):\/\/)?(?:www.)?instagram\.com\S*?\/(p|reel)\/(\w{11})\/?"
)

pinterest_pattern = re.compile(
    r"(?:https:\/\/)(?:.+)?pinterest\.com\/pin\/([0-9]+)\/?"
)

bluesky_pattern = re.compile(
    r"(?:https:\/\/)(?:.+)?bsky\.app\/profile\/(\S+)\/post\/([A-Za-z0-9]+)"
)

tiktok_pattern = re.compile(
    r"(?:(?:https?):\/\/)?(?:m|www|vm)?\.?tiktok\.com\/((?:.*\b(?:(?:usr|v|embed|user|video)\/|\?shareId=|\&item_id=)(\d+))|\w+)/?"
)

async def change_link(query: str):
    if re.search(link_pattern, query):
        if re.search(twitter_pattern, query):
            return re.sub(twitter_pattern, r"fxtwitter.com/\g<1>/status/\g<3>", query)
        elif re.search(tiktok_pattern, query):
            return re.sub(tiktok_pattern, r"kktiktok.com/\g<1>/\g<2>", query)
        elif re.search(instagram_pattern, query):
            return re.sub(instagram_pattern, r"uuinstagram.com/\g<1>/\g<2>", query)
        elif re.search(pinterest_pattern, query):
            return re.sub(pinterest_pattern, r"pinterestez.com/pin/\g<1>", query)
        elif re.search(bluesky_pattern, query):
            return re.sub(bluesky_pattern, r"boobsky.app/profile/\g<1>/post/\g<2>", query)
        else:
            raise NotSupported
    else:
        raise InvalidQuery