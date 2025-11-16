import requests
import bs4


def get_available_words() -> set[str]:
    results: set[str] = set()
    try:
        resp = requests.get("https://wordraiders.com/solvers/wordle/")
        if resp.status_code == 200:
            soup = bs4.BeautifulSoup(resp.content, 'lxml')
            all_words = soup.find('div', class_='list-body')
            unused_words = all_words.find_all('div', class_='single-word unused-word')
            for unused_word in unused_words:
                results.add(unused_word.text)
        else:
            print("Could not reach https://wordraiders.com/solvers/wordle/")
    except ConnectionError:
        print("Could not reach wordraiders.com")
    return results


if __name__ == '__main__':
    print(get_available_words())
