import sys
import logging

import requests

from django.core.cache import cache


DEFAULT_USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21'

def slurp_url(url, use_cache=False, timeout=5, user_agent=None):
    def _slurp_url(url):
        resp = requests.get(url,
                            headers={'User-Agent': user_agent or DEFAULT_USER_AGENT},
                            timeout=timeout)
        if resp.status_code == 200:
            return resp.text
        else:
            logging.error('Unexpected status ({status}) for ({url})'.format(url=url, status=resp.status_code))
            return None

    cache_key = 'slurp_url:' + url
    if use_cache == True:
        cached_content = cache.get(cache_key)
        if cached_content is not None:
            return cached_content

    content = _slurp_url(url)

    if use_cache == True and content is not None:
        cache.set(cache_key, content)

    return content


if __name__ == "__main__":
    sys.stdout.write(slurp_url(sys.argv[1], False).encode('utf-8'))

