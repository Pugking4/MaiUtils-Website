from bs4 import BeautifulSoup
import re
from playwright.async_api import async_playwright
import pandas as pd

dataframes = {}

def get_score_data(html, ver):

    soup = BeautifulSoup(html, "html.parser")
    # Get the difficulty level
    diff_img = soup.find("img", {"class": "h_20 f_l"})
    diff = re.search(r"diff_(\w+)\.png", diff_img["src"]).group(1)
    # Get the level
    level = soup.find("div", {"class": "music_lv_block"}).text
    # Get the song title
    title = soup.find("div", {"class": "music_name_block"}).text

    # Check if the song has a score
    score = soup.find("div", {"class": "music_score_block w_120 t_r f_l f_12"})
    if score is not None:
        # get the score percentage
        score = score.text
    else:
        score = "0.000%"

    # find the div element with class="music_score_block w_180 t_r f_l f_12"
    # find the score block
    score_block = soup.find("div", {"class": "music_score_block w_180 t_r f_l f_12"})

    #print(score_block)

    if score_block is not None:
        # Find the img element with the deluxe score image and get the next div element
        deluxe_score_div = score_block.find("img", {"class": "v_b f_l"})#.find_next_sibling("div")
        deluxe_score_div = deluxe_score_div.next_sibling
        deluxe_score = deluxe_score_div.strip()
    else:
        deluxe_score = "N/A"
    
    type_img = soup.find('img', {'class': 'music_kind_icon f_r', 'src': 'https://maimaidx-eng.com/maimai-mobile/img/music_standard.png'})
    if type_img:
        type = 'standard'
    else:
        type = 'dx'

    '''
    print(f"Difficulty: {diff.upper()}")
    print(f"Level: {level}")
    print(f"Title: {title}")
    print(f"Score: {score}")
    print(f"Deluxe Score: {deluxe_score}")
    '''

    dict = {
        'title': title,
        'version': ver,
        'type': type,
        'difficulty': diff.upper(),
        'level': level,
        'score': score,
        'deluxe_score': deluxe_score
    }
    return dict

def iterate_scores(diff):
    data = []
    with open(f"output_{diff}.txt", "r", encoding='utf-8') as f:
        results = f.read().split("|")
    #deletes the last empty element
    del results[-1]
    for html in results:
        data.append(get_score_data(html, diff))

    df = pd.DataFrame(data)
    df.set_index('title', inplace=True)
    dataframes[diff] = df

for i in range(20):
    iterate_scores(i)

#df = pd.DataFrame(data)
#df.set_index('title', inplace=True)

writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet
for diff, df in enumerate(dataframes.values()):
    df.to_excel(writer, sheet_name=f'Sheet{diff}')

# Save the excel file
writer.save()


#print(data)