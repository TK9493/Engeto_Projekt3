import csv
import sys
import traceback
import requests
from bs4 import BeautifulSoup


def main() -> None:
    """
    Main calling function.
    """
    arguments()
    url = sys.argv[1]
    file_name = sys.argv[2]
    elected_parties(url, file_name)


def elected_parties(url: str, file_name: str) -> None:
    """
    This function performs web scraping.
    """
    soup = main_page_content(url)
    municipalities = select_municipality(soup)
    results = result(link_select(soup))

    for i in range(len(municipalities)):
        municipalities[i].update(results[i])
    complete_list = municipalities
    record_csv(complete_list, file_name)


def arguments():
    """
    This function checks three default arguments to run the program.
    """
    if len(sys.argv) != 3:
        print(f"File: {sys.argv[0]} needs 2 arguments to run. Ending ...")
        exit()
    elif not sys.argv[1].startswith("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj="):
        print(f"Argument one {sys.argv[1]} is not correct! Ending ...")
        exit()
    elif not sys.argv[2].endswith(".csv"):
        print(f"File: {sys.argv[2]} is not a CSV file! Ending ...")
        exit()
    else:
        print(f'STAHUJI DATA Z VYBRANEHO URL: {sys.argv[1]}')


def main_page_content(url: str):
    """
    This function retrieves the content of a web page.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    page = requests.get(url, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')


def select_municipality(soup: 'BeautifulSoup') -> list:
    municipalities = []
    for row in soup.select('tr', headers="t1sa1 t1sb2"):
        row = list(row.stripped_strings)
        if row[0].isnumeric() is True:
            municipality = {'Kód': row[0], 'Obec': row[1]}
            municipalities.append(municipality)
        else:
            continue
    return municipalities


def link_select(soup: 'BeautifulSoup') -> list:
    """
    This function creates a list of links
    """
    links = [link.get('href') for link in soup.select('table a', href=True)]

    select_links = []

    for x in links:
        link = "https://www.volby.cz/pls/ps2017nss/" + x
        if len(link) < 80:
            continue
        elif link in select_links:
            continue
        else:
            select_links.append(link)

    return select_links


def result(select_links: list) -> list:
    """
    This function returns a list of parties with their results.
    """
    results = []
    for link in select_links:

        page = requests.get(select_links[select_links.index(link)])
        link_soup = BeautifulSoup(page.content, 'html.parser')
        table_tag = link_soup.find("div", {"class": "topline"})
        td_tag = table_tag.find_all("td")

        result = {}
        for i in td_tag:
            g = len(td_tag)
            if td_tag.index(i) in range(g - (g - 10), g - 4, 5):
                result[td_tag[td_tag.index(i)].get_text()] = td_tag[td_tag.index(i) + 1].get_text()
            elif td_tag.index(i) == 3:
                result["Voliči v seznamu"] = td_tag[3].get_text()
            elif td_tag.index(i) == 4:
                result["Vydané obálky"] = td_tag[4].get_text()
            elif td_tag.index(i) == 7:
                result["Platné hlasy"] = td_tag[7].get_text()
            else:
                continue
        results.append(result)
    return results


def record_csv(complete_list: list, file_name: str) -> str:
    """
    Write data (par. 'complete_list') to the specified file (par. 'file_name').
    From the first index par. 'complete_list' tries to take the key names and create a file header from them.
    """
    with open(file_name, mode="w", newline='', encoding="utf-8") as csv_file:

        try:
            columns = complete_list[0].keys()

        except FileExistsError:
            return traceback.format_exc()

        else:
            print(f'UKLADAM DO SOUBORU: {sys.argv[2]}')
            record = csv.DictWriter(csv_file, fieldnames=columns, extrasaction='ignore')
            record.writeheader()
            for element in complete_list:
                record.writerow(element)

        finally:
            print(f'UKONCUJI election-scraper')
            csv_file.close()


if __name__ == "__main__":
    main()

    