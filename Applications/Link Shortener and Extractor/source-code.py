"""Simple link shortener and extractor helpers.

Provides small CLI helpers to shorten a URL using tinyurl and to expand
shortened URLs back to their original target.
"""

import pyshorteners
from urllib.request import urlopen


def link_shortener(link: str) -> None:
    shortener = pyshorteners.Shortener()
    short_link = shortener.tinyurl.short(link)

    print(f'\t[+] Real Link: {link}')
    print(f'\t[+] Shortened Link: {short_link}')


def link_opener(link: str) -> None:
    shortened_url = urlopen(link)
    real_link = shortened_url.geturl()

    print(f'\t[+] Shortened Link: {link}')
    print(f'\t[+] Real Link: {real_link}')


def main() -> None:
    """Interactive CLI: choose shorten or expand flow."""
    print("Enter your choice:")
    print(" 1. Shorten a link")
    print(" 2. Expand a shortened link to its real URL")

    choice = input("Choice (1/2): ").strip()
    if choice not in {'1', '2'}:
        print("Invalid choice. Exiting.")
        return

    link = input("Enter the link: ").strip()
    if not link:
        print("Empty link provided. Exiting.")
        return

    try:
        if choice == '1':
            link_shortener(link)
        else:
            link_opener(link)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()