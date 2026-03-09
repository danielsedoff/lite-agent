import urllib.parse as urlparse
from urllib.parse import urlencode

def generate_url(user_input: str):
    url = "http://duckduckgo.com/?ia=web&origin=funnel_home_website"
    params = {'q':user_input}

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)

    return(urlparse.urlunparse(url_parts))

if __name__ == "__main__":
    print("usage: url = generate_url('QUERY')")
