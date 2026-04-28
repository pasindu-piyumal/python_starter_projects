import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

websites = [
    "apple.com",
    "facebook.com",
    "this_website_is_not_real.com",
    "newgrounds.com",
    "linkedin.com",
    "python-guide.com",
    "fastmail.com",
    "soundcloud.com",
    "whatsapp.com/hello",
    "udemy.com"
]

# Create CSV
with open("websites.csv", "w") as file:
    for i, site in enumerate(websites, start=1):
        file.write(f"{i},'{site}'\n")


def get_website(csv_path: str) -> list[str]:
    website: list[str] = []

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) < 2:
                continue

            url = row[1].strip().strip("'")  # remove quotes

            if not url.startswith(('http://', 'https://')):
                url = f'https://{url}'

            website.append(url)

    return website


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value.value == status_code:
            return f'({value.value} {value.name}) {value.phrase}'

    return 'Unknown status code'


def check_website(website: str, user_agent: str):
    try:
        response = requests.get(
            website,
            headers={'User-Agent': user_agent},
            timeout=5
        )
        print(website, get_status_description(response.status_code))

    except requests.RequestException:
        print(f'❌ Could not get information for: {website}')


def main():
    sites = get_website('websites.csv')
    user_agent = get_user_agent()

    for site in sites:
        check_website(site, user_agent)


if __name__ == '__main__':
    main()