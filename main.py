import sys
import csv

from bs4 import BeautifulSoup

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    author = soup.findAll('div', {'class': 'bookmark'})[1].getText(strip=True)
    title = soup.findAll('div', {'class': 'bookmark'})[0].getText(strip=True)
    title_index = title.find(' - ') + 3
    title = title[title_index:]
    with open(f'{title} - {author}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(('Highlight','Title', 'Author', 'Note', 'Location'))
        for element in soup.findAll('div', {'class': 'bookmark', 'id': True}):
            page = element.findNext('p', {'class': 'bm-page'}).string
            highlight = element.findNext('div', {'class': 'bm-text'}).p.getText('\n')
            note = element.findNext('div', {'class': 'bm-note'})
            if note is not None:
                note_text = note.p.getText('\n')
            else:
                note_text = ''
            writer.writerow((highlight, title, author, note_text, page))
