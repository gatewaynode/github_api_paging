#!./env/bin/python3

"""
Module Docstring
"""

import settings
import os
import json
import requests
from pprint import pprint

__author__ = "Gatewaynode"
__version__ = "0.1.0"
__license__ = "MIT"


def github_request(marker = ""):
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Authorization": f"bearer {token}"
    }
    if marker:
      request_params = f"first: 5, after: \"{marker}\""
    else:
      request_params = "first: 5"
    query = f"""query {{
  viewer {{
    name
    repositories ({request_params}) {{
      pageInfo {{
        endCursor
        hasNextPage
      }}
      nodes {{
        url
      }}
    }}
  }}
}}
"""
    data = {
        "query": query,
        "variables": {}
    }
    
    response = requests.post("https://api.github.com/graphql", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
      send_me_home = json.loads(response.text)
      if "data" in send_me_home:
        return send_me_home
      else:
        pprint(send_me_home)
        exit(1)
    else:
      pprint(response)
      exit(1)


def main():
  repos = []
  marker = ""
  has_next = True
  while has_next:
    response = github_request(marker)
    has_next = response["data"]["viewer"]["repositories"]["pageInfo"]["hasNextPage"]
    marker = response["data"]["viewer"]["repositories"]["pageInfo"]["endCursor"]
    repos += response["data"]["viewer"]["repositories"]["nodes"]
  
  pprint(repos)
  

if __name__ == "__main__":
    main()
