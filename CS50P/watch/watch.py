import re
import sys
def main():
    s='<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    print(parse(s))


def parse(html):
    # Updated pattern to match any YouTube embed URL in the src attribute of an iframe
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'

    # Search for the pattern in the HTML input
    match = re.search(pattern, html)

    # If a match is found, format the shorter YouTube URL with youtu.be and return it
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    # If no match, return None
    return None



if __name__ == "__main__":
    main()
