#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:29:57 2024

@author: travis
"""
import requests

from bs4 import BeautifulSoup as bs


URLS = {
    "wb": ("https://datacatalog.worldbank.org/search/dataset/0037580/"
           "Global-Shipping-Traffic-Density")
}
self.url = "https://datacatalogfiles.worldbank.org/ddh-published/0037580/DR0045406/shipdensity_global.zip?versionId=2023-01-18T20:40:41.1120158Z"

class WorldBank:
    """Methods for Downloading from the world bank."""

    def __init__(self, url=URLS["wb"]):
        """Initialize WorldBank object."""
        self.url = url

    @property
    def paths(self):
        """Return paths to all datasets."""
        with requests.get(self.url) as r:
            content = r.content
        soup = bs(content)
        for a in soup.find_all('a', href=True):
            print("Found the URL:", a['href'])


if __name__ == "__main__":
    self = WorldBank()
