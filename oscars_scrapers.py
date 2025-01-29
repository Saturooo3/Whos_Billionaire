import wikipedia
from bs4 import BeautifulSoup
import re

def get_golden_globe_winners():
    elements = wikipedia.page("Golden_Globe_Award_for_Best_Motion_Picture_–_Drama")
    soup = BeautifulSoup(elements.html(), "html.parser")
    # Only grab movies from the last three decates
    decades = ["2000s", "2010s", "2020s"]

    decade_results = {}

    for decade in decades:
        heading = soup.find("h3", id=decade)
        if not heading:
            print(f"No <h3> found with id='{decade}'.")
            continue

        table = heading.find_next("table", class_="wikitable")
        if not table:
            print(f"No table found for {decade}.")
            continue

        # parse the table
        decade_data = parse_golden_globe_table(table)
        decade_results[decade] = decade_data

    # Flatten decades into just one list
    all_years_data = {}
    for decade_data in decade_results.values():
        for year, details in decade_data.items():
            all_years_data[year] = details

    return all_years_data


def parse_golden_globe_table(table):
    rows = table.find_all("tr")
    data = {}
    current_year = None

    for row in rows[1:]:
        year_cell = row.find("th")
        if year_cell:
            year_text = year_cell.get_text(strip=True)
            # Use regex to find the first four-digit number in the year cell text
            year_match = re.search(r'\d{4}', year_text)
            if year_match:
                current_year = year_match.group()
                if current_year not in data:
                    data[current_year] = ""

        cells = row.find_all("td")
        if not cells:
            continue

        film_title = cells[0].get_text(strip=True)
        style = row.get("style", "").lower()
        is_winner = "background:#b0c4de" in style

        if not is_winner:
            for c in cells:
                cell_style = (c.get("style") or "").lower()
                if "background:#b0c4de" in cell_style:
                    is_winner = True
                    break

        if current_year and is_winner:
            data[current_year] = film_title

    return data
