import wikipedia
from bs4 import BeautifulSoup

def get_elements():
    elements_page = wikipedia.page("List_of_chemical_elements")

    soup = BeautifulSoup(elements_page.html(), "html.parser")
    table = soup.find("table", {"class": "wikitable"})

    if not table:
        print("Could not find table.")
        return {}

    rows = table.find_all("tr")

    symbol_to_name = {}

    for row in rows[1:]:
        cells = row.find_all("td")

        # Skip short rows with less than 3 <td> cells - otherwise crash:
        if len(cells) < 3:
            continue

        symbol = cells[1].get_text(strip=True)
        name = cells[2].get_text(strip=True)

        symbol_to_name[symbol] = name

    return symbol_to_name