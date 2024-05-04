import requests
import concurrent.futures
from auctions import validate_and_print_auction


API_URL = "https://api.hypixel.net/skyblock/auctions"
MOST_RECENT_PAGES = 2


def run():
    print("Initializing...")
    print("Press Ctrl+C to stop the program\n")

    # Fetch initial response to get total pages count
    initial_response = fetch_url(API_URL)
    total_pages_count = int(initial_response["totalPages"])

    # Fetch all pages of auctions
    fetch_pages(total_pages_count)
    while True:
        # Fetch most recent pages of auctions
        fetch_pages(MOST_RECENT_PAGES)


def fetch_pages(page_count):
    try:
        urls = []
        for i in range(page_count):
            urls.append(f'{API_URL}?page={i}')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(fetch_url, url) for url in urls]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                
                if result is not None and result["success"]:
                    for auction in result["auctions"]:
                        validate_and_print_auction(auction)

    except KeyboardInterrupt:
        print("Program stopped by user, exiting...")
        exit()


def fetch_url(url):
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição para {url}: {e}')
        return None

run()
