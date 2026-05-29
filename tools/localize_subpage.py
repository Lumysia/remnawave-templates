import json
import re
from pathlib import Path

SUBPAGE = Path("subpage.json")
I18N_DIR = Path("tools/subpage-i18n")

LOCALES = [
    "en", "ru", "zh", "fr", "fa", "uz", "de", "hi", "tr", "az",
    "es", "vi", "ja", "be", "uk", "pt", "pl", "id", "tk", "th",
]


def load_i18n():
    data = {}
    for locale in LOCALES:
        if locale == "en":
            continue
        path = I18N_DIR / f"{locale}.json"
        data[locale] = json.loads(path.read_text(encoding="utf-8"))
    return data


def translate(text, locale, i18n):
    if locale == "en":
        return text

    exact = i18n[locale].get("exact", {})
    if text in exact:
        return exact[text]

    templates = i18n[locale].get("templates", {})

    match = re.fullmatch(
        r"After importing the profile, select it in (.+), choose a proxy policy if needed, and enable the connection or system proxy\.",
        text,
    )
    if match:
        return templates["connect"].format(app=match.group(1))

    match = re.fullmatch(
        r"If automatic import does not work, copy the subscription link from this page and import it manually in (.+) as a remote profile or subscription URL\.",
        text,
    )
    if match:
        return templates["manual"].format(app=match.group(1))

    match = re.fullmatch(r"Install (.+) if your Android TV device supports APK sideloading\.", text)
    if match:
        return templates["install_android_tv"].format(app=match.group(1))

    if text == "Install the official sing-box Android client.":
        return templates["install"].format(app="sing-box Android")

    match = re.match(r"Install (.+?)(?:,|\.| if| from| for).+", text)
    if match:
        return templates["install"].format(app=match.group(1))

    return text


def localize(value, i18n):
    if isinstance(value, dict):
        if isinstance(value.get("en"), str):
            source = value["en"]
            for locale in LOCALES:
                value[locale] = translate(source, locale, i18n)
            for key in list(value.keys()):
                if key not in LOCALES:
                    del value[key]
        else:
            for child in value.values():
                localize(child, i18n)
    elif isinstance(value, list):
        for child in value:
            localize(child, i18n)


def validate(data):
    missing = []
    corrupted = []

    def walk(value, path=""):
        if isinstance(value, dict):
            if isinstance(value.get("en"), str):
                en = value["en"]
                for locale in LOCALES:
                    text = value.get(locale)
                    if not isinstance(text, str) or not text:
                        missing.append((path, locale))
                    if locale != "en" and "???" in text:
                        corrupted.append((path, locale, text))
            for key, child in value.items():
                walk(child, f"{path}.{key}" if path else key)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}.{index}")

    walk(data)
    if missing or corrupted:
        raise SystemExit(f"missing={missing[:5]} corrupted={corrupted[:5]}")


def main():
    i18n = load_i18n()
    data = json.loads(SUBPAGE.read_text(encoding="utf-8"))
    data["locales"] = LOCALES
    localize(data, i18n)
    validate(data)
    SUBPAGE.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
