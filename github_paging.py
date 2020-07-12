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


def main():
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Authorization": f"bearer {token}"
    }
    
    query = """query {
  viewer {
    name
    repositories (first: 2) {
      pageInfo {
        endCursor
        hasNextPage
      }
      nodes {
        name
      }
    }
  }
}
"""
    data = {
        "query": query, # json.dumps(query),
        "variables": {}
    }
    
    response = requests.post("https://api.github.com/graphql", headers=headers, data=json.dumps(data))
    print("===========================================================")
    print("--- data ---")
    pprint(data)
    print("--- request body ---")
    pprint(response.request.body)
    print("--- Response ---")
    pprint(response.text)

if __name__ == "__main__":
    main()
