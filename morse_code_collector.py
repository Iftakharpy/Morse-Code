import requests
import bs4

morse_code_selector_xpath = "//div/a/span[@style='font-size:x-large;']"
letter_selector_xpath = "//td/b/a[contains(@href,'/wiki/')]"

# used "https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01" as css selector reference
morse_code_selector_css = "table.wikitable > tbody > tr div > a > span"
letter_selector_css = "table.wikitable > tbody > tr > td > b"

# wiki article on morse code
url = "https://en.wikipedia.org/wiki/Morse_code"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, features="html.parser")

morse_codes = soup.select(morse_code_selector_css)
letters = soup.select(letter_selector_css)

if not len(morse_codes) == len(letters):
    raise ValueError("Length of morse codes and letters didn't match.")


def make_writable_morse_code(code):
    writable_code = ""
    for ch in code:
        if ch == "·":
            writable_code += "."
        elif ch == "−":
            writable_code += "-"
        else:
            pass
    return writable_code

def collect_morse_code(file_name, separator="|", write_header=True):
    with open(file_name, "w", encoding="utf-8") as file:
        if write_header:
            file.write(f"Letter{separator}Morse Code\n")    # header

        #inserting data
        for letter, code in zip(letters, morse_codes):
            letter = letter.text.strip()
            code = code.text.strip()
            code = make_writable_morse_code(code)

            try:
                file.write(f"{letter}{separator}{code}\n")
            except UnicodeEncodeError:
                print(f"Coudn't encode {letter}. Skipping")
                pass
