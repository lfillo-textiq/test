import os
import stat
import sys
import shutil
import urllib.request
from github import Github

GITHUB_PAT = os.getenv("GITHUB_PAT")
BARTENDER = "bartender"
ASSET_DST_MAP = {
    "bartender": "/usr/local/bin",
    "prod.config": "/usr/local/etc",
    "dev.config": "/usr/local/etc"
}

class ReleaseAsset:
    """ Class for storing release assets, their destination, and download url"""
    def __init__(self, name, url):
        self.name = name
        self.dst = ASSET_DST_MAP[self.name]
        self.url = url

def main():
    """Downloads and installs the latest bartender release assets"""
    if GITHUB_PAT is None:
        sys.exit("Error: GITHUB_PAT environment variable not found")
    g = Github(GITHUB_PAT)
    repo = g.get_repo("textiq/Bartender")
    rel = repo.get_latest_release()
    assets = rel.get_assets()
    rel_assets = []
    for a in assets:
        if a.name in ASSET_DST_MAP.keys():
            rel_assets.append(ReleaseAsset(a.name, a.url))
    for rel_asset in rel_assets:
        req = urllib.request.Request(rel_asset.url)
        req.add_header("Authorization", "token {}".format(GITHUB_PAT))
        req.add_header("Accept", "application/octet-stream")
        with urllib.request.urlopen(req) as response, open(rel_asset.name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            dst = os.path.join(rel_asset.dst, rel_asset.name)
            shutil.move(rel_asset.name, dst)
            st = os.stat(dst)
            if rel_asset.name == BARTENDER:
                os.chmod(dst, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print("bartender {} successfully installed!".format(rel.tag_name))
if __name__ == "__main__":
    main()
