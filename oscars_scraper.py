import wikipedia
from bs4 import BeautifulSoup

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

    # Skip table's first row (titles) by slicing, as its only the headers.
    for row in rows[1:]:
        year_cell = row.find("th")
        if year_cell:
            year_text = year_cell.get_text(strip=True)
            # If there's a digit year, start a new 'current_year'
            if year_text.isdigit():
                current_year = year_text
                if current_year not in data:
                    data[current_year] = {
                        "winner": "",
                        "nominees": []
                    }

        cells = row.find_all("td")
        if not cells:
            continue

        film_title = cells[0].get_text(strip=True)

        # Find out if this row is a winner
        style = row.get("style", "")
        is_winner = False

        # Find out the winner by checking background:#B0C4DE
        # Either the whole row or the td
        # Lowercase the style as freaking wikipedia does what it wants and uses different cases
        style_lower = style.lower()
        if "background:#b0c4de" in style_lower:
            is_winner = True
        else:
            for c in cells:
                cell_style = (c.get("style") or "").lower()
                if "background:#b0c4de" in cell_style:
                    is_winner = True
                    break

        if current_year:
            data[current_year]["nominees"].append(film_title)
            if is_winner:
                data[current_year]["winner"] = film_title

    return data