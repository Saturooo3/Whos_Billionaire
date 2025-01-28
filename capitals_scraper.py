import wikipedia
from bs4 import BeautifulSoup


def get_list_of_capitals_and_countries():
    print("#####################################")
    print("Loading list.")
    print("Please wait...")
    article = wikipedia.page("List_of_national_capitals#List")
    soup = BeautifulSoup(article.html(), "html.parser")

    table = soup.find("table", {"class": "wikitable"})

    city_country_pairs = {}

    # Track the current country across row-spans for reuse:
    current_country = None
    remaining_country_rowspan = 0

    # Skip table's first row (titles) by slicing from the second row onwards.
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")

        # skip any empty or malformed rows
        if not cells:
            continue

        # Extract the city from the first cell:
        city_td = cells[0]
        city_text = city_td.get_text(strip=True)  # strip whitespace from the beginning and end

        # Extract country. Might be reused if it spanned over several cities.
        if remaining_country_rowspan == 0 and len(cells) > 1:
            country_td = cells[1]
            country_text = country_td.get_text(strip=True)

            # Check if the country is reused (rowspan)
            rowspan_val = country_td.get("rowspan")
            if rowspan_val:
                remaining_country_rowspan = int(rowspan_val) - 1
            else:
                remaining_country_rowspan = 0

            current_country = country_text
        else:
            country_text = current_country

            if remaining_country_rowspan > 0:
                remaining_country_rowspan -= 1

        city_country_pairs[f"{city_text}"] = f"{country_text}"

    print("Loaded!")
    print("#####################################")
    return city_country_pairs