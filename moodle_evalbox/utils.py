from re import compile, sub


def clean_html_text(html: str) -> str:
    cleanr = compile("<.*?>")
    cleantext = sub(cleanr, "", html)
    return cleantext