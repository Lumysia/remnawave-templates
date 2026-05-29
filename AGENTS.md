# Repository Guidance

This repository contains Remnawave subscription templates and one Remnawave subscription page JSON. Keep changes general-purpose and internationally usable; do not narrow behavior to a specific country, provider, region, or private deployment.

## Scope

- Subscription templates live in `templates/`.
- The subscription page is `subpage.json`.
- Subscription page translations live in `tools/subpage-i18n/` and are applied by `tools/localize_subpage.py`.

## Template Rules

- Preserve Remnawave injection markers such as `proxies: # LEAVE THIS LINE!`.
- Preserve sing-box Remnawave injection through selector outbound `outbounds: null`.
- Do not hard-code any country to `DIRECT`.
- `DIRECT`/Local should only cover localhost, LAN, private IPs, multicast, link-local, ULA IPv6, and private domains like `.local` or `.lan`.
- Keep `Final` proxy-first.
- Keep group/tag/rule names English.

## Subscription Page Rules

- Prefer widely used clients with strong GitHub/community recognition.
- The subscription page is for GUI clients; do not add CLI/core-only downloads as app cards.
- Do not add obscure forks unless there is a clear maintenance or platform reason.
- Do not pin release versions in download URLs.
- Use `releases/latest/download/...` only for assets with stable names across releases. If asset names include the version, use `releases/latest` instead.

## Localization

- Do not edit translated strings directly in the generated subpage unless making a one-off emergency fix.
- Edit `tools/subpage-i18n/<locale>.json`, then run `python tools/localize_subpage.py`.
- The generator writes ASCII-escaped JSON (`\uXXXX`) intentionally. This prevents UTF-8 text from becoming `?` during copy/import paths.

## Validation

Before handing off changes, verify:

- JSON files parse.
- YAML files parse.
- All subpage `svgIconKey` values exist in `svgLibrary`.
- All subpage `svgIconColor` values are accepted by Remnawave or are hex colors.
- All localized fields include every locale declared in `locales`.

## Commits

- Use Angular-style commit messages, for example `feat: add international templates` or `fix: correct subpage import links`.
