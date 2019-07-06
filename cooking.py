from bs4 import BeautifulSoup

with open('cooking.html') as f:
  body = f.read()

soup = BeautifulSoup(body, 'lxml')

def rows(soup):
  item = soup.find(id='Recipes').find_next('table').tr
  while item:
    if item:
      item = item.next_sibling
    if item:
      item = item.next_sibling
    if item:
      yield item

def counts(text):
  start = 0
  end = text.find(')', start)
  while end != -1:
    mid = text.find('(', start, end)
    name = text[start:mid].strip().replace(u'\xa0', ' ')
    count = int(text[mid+1:end])
    yield name, count
    start = end + 1
    end = text.find(')', start)

def edges(item):
  td = item.find_all('td')
  name = td[1].text.strip()
  for ingredient, count in counts(td[3].text):
    yield name, ingredient, count

mappings = (
    (u'\xa0', ' '),
    (u' ', ';'),
    (u'(', None),
    (u')', None),
)

for item in rows(soup):
  for a, b, c in edges(item):
    print('{}\t{}\t{}'.format(a, b, c))
