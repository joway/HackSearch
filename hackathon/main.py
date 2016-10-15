from hackathon.api import APIService
from hackathon.helper import read_url_file
from utils.helpers import gen_uuid, get_full_domain

# filename = 'data/url.txt'
filename = 'data/v2ex.txt'
links = read_url_file(filename)

for link in links:
    resp = APIService.create_proj(name=get_full_domain(link), entry_url=link)
    print(resp)
