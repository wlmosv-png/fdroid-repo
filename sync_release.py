#!/usr/bin/env python3
"""从 wpaforge 拉取最新 release 的 APK 放进 repo/。"""
import json
import os
import sys
import urllib.request

UA = 'Mozilla/5.0 (compatible; fdroid-repo-sync/1.0)'
TOK = os.environ.get('GITHUB_TOKEN', '')
SRC = 'wlmosv-png/wpaforge'


def fetch(url, raw=False):
    req = urllib.request.Request(url, headers={
        'User-Agent': UA,
        'Authorization': 'Bearer ' + TOK,
        'Accept': 'application/vnd.github+json',
    })
    data = urllib.request.urlopen(req, timeout=300).read()
    return data if raw else json.loads(data.decode('utf-8'))


def main():
    rel = fetch('https://api.github.com/repos/%s/releases/latest' % SRC)
    tag = rel['tag_name'].lstrip('v')
    print('最新 release:', rel['tag_name'])
    os.makedirs('repo', exist_ok=True)
    # 清掉旧 APK，避免同一版本存在两个文件名（fdroid 会报 duplicate）
    for f in os.listdir('repo'):
        if f.endswith('.apk'):
            os.remove(os.path.join('repo', f))

    for asset in rel.get('assets', []):
        if not asset['name'].lower().endswith('.apk'):
            continue
        target = os.path.join('repo', 'WPAForge_%s.apk' % tag)
        if os.path.exists(target):
            print('已存在，跳过:', target)
            return 0
        blob = fetch(asset['browser_download_url'], raw=True)
        with open(target, 'wb') as fh:
            fh.write(blob)
        print('已下载:', target, len(blob), 'bytes')
        return 0

    print('该 release 没有 .apk 附件', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
