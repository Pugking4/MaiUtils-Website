from bs4 import BeautifulSoup
from record_scrape import scrape

def record_master(segaid, password):
    def get_score_data(html):

        soup = BeautifulSoup(html, "html.parser")
        # Get the score
        score = soup.find("div", {"class": "playlog_achievement_txt t_r"}).text
        # Get the song title
        title = soup.find("div", {"class": "basic_block m_5 p_5 p_l_10 f_13 break"}).text
        # Get the difficulty master
        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_master.png'})
        if diff:
            difficulty = 'MASTER'

        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_remaster.png'})
        if diff:
            difficulty = 'REMASTER'

        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_expert.png'})
        if diff:
            difficulty = 'EXPERT'

        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_advanced.png'})
        if diff:
            difficulty = 'ADVANCED'

        diff = soup.find("img", {"class": "playlog_diff v_b", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/diff_basic.png'})
        if diff:
            difficulty = 'BASIC'

        # Get the image link
        img_link = soup.find("img", {"class": "music_img m_5 m_r_0 f_l"})['src']

        # Get the dx score
        dx_score = soup.find("div", {"class": "white p_r_5 f_15 f_r"}).text

        type_img = soup.find('img', {'class': 'playlog_music_kind_icon', 'src': 'https://maimaidx-eng.com/maimai-mobile/img/music_standard.png'})
        if type_img:
            type = 'standard'
        else:
            type = 'dx'


        # Find all span elements inside the div element with class sub_title
        span_list = soup.find('div', {'class': 'sub_title'}).find_all('span')
        # Get the time/date (second span element)
        time = span_list[1].text
        # Get the track (first span element)
        track = span_list[0].text


        '''
        print(f"Difficulty: {diff.upper()}")
        print(f"Level: {level}")
        print(f"Title: {title}")
        print(f"Score: {score}")
        print(f"Deluxe Score: {deluxe_score}")
        '''

        data_dict = {}
        child_dict = {
            'title': title,
            'difficulty': difficulty,
            'score': score,
            'deluxe_score': dx_score,
            'type': type,
            'time': time,
            'track': track,
            'img_link': img_link
        }
        data_dict[f'{title}|{type}'] = child_dict
        return data_dict

    def iterate_scores(html_data):
        data = []
        #deletes the last empty element
        #del html_data[-1]
        for html in html_data:
            data.append(get_score_data(html))

        return data

        #df = pd.DataFrame(data)
        #df.set_index('title', inplace=True)
        #dataframes[diff] = df

    html_data = scrape(segaid, password)

    data = iterate_scores(html_data)

    #with open("output_gen.txt", "w", encoding='utf-8') as f:
    #    for i in data:
    #        f.write(str(i))
    #        f.write('\n')

    return data
    '''
    #df = pd.DataFrame(data)
    #df.set_index('title', inplace=True)

    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

    # Write each dataframe to a different worksheet
    for diff, df in enumerate(dataframes.values()):
        df.to_excel(writer, sheet_name=f'Sheet{diff}')

    # Save the excel file
    writer.save()

    '''