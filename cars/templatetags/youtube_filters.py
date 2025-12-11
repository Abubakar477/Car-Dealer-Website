from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(link):
    """
    Converts a YouTube watch link to embed format.
    """
    pattern = r'(?:v=|be/|embed/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, link)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return ''
