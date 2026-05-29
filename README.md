# Remnawave Templates

International, proxy-first Remnawave subscription templates and a curated subscription page.

## Files

- `templates/xray.json`
- `templates/mihomo.yaml`
- `templates/stash.yaml`
- `templates/singbox.json`
- `templates/clash.yaml`
- `subpage-00000000-0000-0000-0000-000000000000.json`

## Notes

- Recommended order: Mihomo > Stash > Singbox > Clash legacy.
- No country is hard-coded to `DIRECT`; regional groups are user-selectable buckets.
- Unknown traffic falls through to proxy-first `Final`.
- The subscription page keeps widely used GUI clients and uses direct GitHub download links only when latest assets have stable names.

## Client Coverage

- Mihomo: Clash Verge Rev, FlClash, Clash Meta for Android, Clash Mi, Mihomo Party, ClashX Meta, Karing, NekoBox for Android.
- Stash: Stash.
- Singbox: sing-box GUI clients, Hiddify, Karing.
- Xray: v2rayN, v2rayNG, Shadowrocket, Streisand.
- Clash legacy: fallback for older Clash-compatible GUI clients only.

## Localization

Edit `tools/subpage-i18n/<locale>.json`, then run:

```bash
python tools/localize_subpage.py
```

The generated subpage is ASCII-escaped JSON to avoid broken non-ASCII text during import.
