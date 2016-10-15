from hackathon.api import APIService
from hackathon.helper import read_url_file
from utils.helpers import gen_uuid

filename = 'data/url.txt'
links = read_url_file(filename)

for link in links:
    resp = APIService.create_proj(name=gen_uuid(), entry_url=link)
    print(resp)
