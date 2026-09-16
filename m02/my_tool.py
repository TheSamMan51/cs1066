### Scrape, save, and plot Google Trends data

import csv
import re
from pathlib import Path

from trends_scraper import get_driver, scrape_interest_data
from trends_plot import main as plot_data


def get_plot_filename(query):
    """Build a filesystem-safe plot filename from the search term."""
    stem = re.sub(r'[^A-Za-z0-9]+', '_', query).strip('_').lower() or 'trends'
    return Path(f'{stem}.png')


def resolve_plot_filename(output_file):
    while output_file.exists():
        choice = input(
            f"Plot file already exists: {output_file}. "
            "Overwrite it or enter a different filename? [o/d]: "
        ).strip().lower()

        if choice in ('o', 'overwrite'):
            return output_file
        if choice in ('d', 'different'):
            output_file = Path(input("Enter a different plot filename: ").strip())
            if not output_file.name:
                print("A filename is required.")
        else:
            print("Please choose overwrite or different filename.")

    return output_file


def main():
    # Build the URL for Google Trends. This is the page we'll scrape.
    date_range = "now%207-d"
    geo = "US"
    query = input("Enter a search term or phrase: ")
    output_file = resolve_plot_filename(get_plot_filename(query))

    site = "https://trends.google.com/trends/explore"
    url = f"{site}?date={date_range}&geo={geo}&q={query}&hl=en"

    # Build a driver for a browser
    driver = get_driver()

    # Scrape the interest data
    interest_data = scrape_interest_data(driver, url)

    # Save data to a CSV file
    fname = 'scraped_data.csv'
    with open(fname, 'w') as fd:
        writer = csv.DictWriter(fd, fieldnames=['Region', 'Interest'])
        writer.writeheader()
        for region, interest in interest_data.items():
            writer.writerow({'Region': region, 'Interest': interest})
    print(f"Saved data to {fname}")

    driver.quit()

    # Create the plot from the saved data
    plot_data(output_file)


if __name__ == "__main__":
    main()
