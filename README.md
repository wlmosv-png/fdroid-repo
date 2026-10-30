# WPAForge F-Droid Repository

自建 F-Droid 仓库（索引 v1/v2 均由独立密钥签名）。
Self-hosted F-Droid repository for WPAForge and related Android tools by wlmosv-png.

## 仓库地址

```
https://wlmosv-png.github.io/fdroid-repo/repo
```

**签名指纹（SHA-256）**：

```
31 96 60 50 C7 86 8C C0 60 A5 50 1A 5D 66 43 7E 59 FF 24 75 20 F1 6E DE 02 53 13 22 EF 79 84 10
```

## 在 F-Droid 客户端中添加

设置 → 仓库（Repositories）→ 添加仓库 → 地址填上面的 URL。
指纹会由客户端自动校验证书，无需手动输入。

## 在 Obtainium 中添加

添加应用时，来源填上面的仓库地址即可。

## 收录的应用

| 应用 | 说明 | 源码 |
|---|---|---|
| **WPAForge** | Android Wi-Fi 网络审计工具（需 Root，Android 8.0+，Apache-2.0） | https://github.com/wlmosv-png/wpaforge |

## 说明

- `config.yml` 与仓库签名密钥**不在此仓库中**（仅本地保留），因此本仓库只包含公开的索引与 APK。
- 索引由 `fdroid update` 生成。发布新版后重新运行该命令并推送即可。
