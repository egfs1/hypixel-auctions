import requests
import concurrent.futures
from auctions import validate_and_print_auction
from utils import API_URL, MOST_RECENT_PAGES

session = requests.Session()

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
        # Create a list of URLs to fetch
        urls = []
        for i in range(page_count):
            urls.append(f'{API_URL}?page={i}')

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as fetch_executor, concurrent.futures.ThreadPoolExecutor(max_workers=50) as process_executor:
            # Fetch all URLs concurrently
            fetch_futures = [fetch_executor.submit(fetch_url, url) for url in urls]
            process_futures = []
            
            # Process fetched auctions concurrently
            for future in concurrent.futures.as_completed(fetch_futures):
                result = future.result()
                if result is not None and result["success"]:
                    for auction in result["auctions"]:
                        process_futures.append(process_executor.submit(validate_and_print_auction, auction))

            # Wait for all auctions to be processed
            for future in concurrent.futures.as_completed(process_futures):
                future.result()

    except KeyboardInterrupt:
        print("Program stopped by user, exiting...")
        exit()


def fetch_url(url):
    try:
        response = session.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {url} = {e}")
        return None

run()