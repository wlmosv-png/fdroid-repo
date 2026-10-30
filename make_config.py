#!/usr/bin/env python3
"""在 CI 里生成 config.yml（口令从环境变量读，不落盘到仓库）。"""
import os

PASS = os.environ['FDROID_KEYSTORE_PASS']

CFG = f"""sdk_path: {os.getcwd()}/sdk
repo_url: https://wlmosv-png.github.io/fdroid-repo/repo
repo_name: WPAForge Repo
repo_icon: icon.png
repo_description: |
  WPAForge 及同作者 Android 工具的自建 F-Droid 仓库。
  Self-hosted F-Droid repo for WPAForge and related Android tools by wlmosv-png.
archive_older: 0
keystore: repo.jks
repo_keyalias: repo
keystorepass: {PASS}
keypass: {PASS}
keydname: CN=wlmosv-png F-Droid Repo, OU=Android, O=wlmosv-png, L=Shenzhen, C=CN
make_current_version_link: false
"""

with open('config.yml', 'w') as fh:
    fh.write(CFG)
os.chmod('config.yml', 0o600)
print('config.yml 已生成（%d 字节）' % len(CFG))
