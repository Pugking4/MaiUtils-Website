from bs4 import BeautifulSoup

html = '<td>95</td>'
soup = BeautifulSoup(html, 'html.parser')

td_tag = soup.find('td')
number_with_percent = td_tag.text.strip()
number = number_with_percent.split('\n')[0]  # extract only the first line

print(number)  # prints '95'