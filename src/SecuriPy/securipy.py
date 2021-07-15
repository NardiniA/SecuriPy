from lxml.html.clean as clean
import re

# strip all HTML tags from a string
def strip_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Removes all Scripts
def remove_script(text):
    cleaner = clean.Cleaner()
    cleaner.javascript = True
    txt = cleaner.clean_html(text)
    cleaned = strip_tags(txt)
    return cleaned

# Removes all styling
def remove_css(text):
    cleaner = clean.Cleaner()
    cleaner.style = True
    txt = cleaner.clean_html(text)
    cleaned = strip_tags(txt)
    return cleaned

# Only Allows letters and Numbers
def noSpecial(text):
    alphanumeric = ""

    for character in text:
        if character.isalnum():
            alphanumeric += character

    return alphanumeric

# Strips all attributes from a HTML tag
def strip_attrs(text):
    safe_attrs = clean.defs.safe_attrs
    cleaner = clean.Cleaner(safe_attrs_only=True, safe_attrs=frozenset())
    cleansed = cleaner.clean_html(text)
    return cleansed

# Removes all tags, scripts, css and sql from input
def strip_all(text):
    nostyle = remove_css(text)
    noscript = remove_script(nostyle)
    noattr = strip_attrs(noscript)
    nohtml = strip_tags(noattr)
    return nohtml

# Removes Css, Js, HTML
def general_strip(text):
    css = remove_css(text)
    js = remove_script(css)
    html = strip_tags(js)
    return html