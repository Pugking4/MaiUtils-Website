from playwright.async_api import async_playwright
import asyncio
import datetime
from bs4 import BeautifulSoup
import json

async def scrape(segaid, password, debug=False):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # navigate to the login page
        await page.goto('https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/record//&back_url=https://maimai.sega.com/')

        # wait for the login page to load
        await page.wait_for_selector('span[class="c-button--openid--segaId"]')

        # click the SEGA ID button
        await page.click('span[class="c-button--openid--segaId"]')

        # wait for the SEGA ID form to load
        await page.wait_for_selector('input[type="text"][id="sid"]')

        # fill in login credential
        await page.fill('input[type="text"][id="sid"]', segaid)
        await page.fill('input[type="password"][id="password"]', password)

        # click the login button
        await page.click('input[type="submit"][class="c-button--login"]')

        # wait for the error message to appear
        await page.wait_for_selector('img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_back.png"][class="w_80 m_t_10"]')

        # click the back button
        await page.click('img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_back.png"][class="w_80 m_t_10"]')

        # wait for the page to load after login
        await page.wait_for_selector('a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')

        # click the record menu
        await page.click('a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')

        # wait for the page to load after clicking the button
        await page.wait_for_selector('div[class="p_10 t_l f_0 v_b"]')
        await asyncio.sleep(3)

        # parse the HTML content
        wrapper = await page.query_selector('div.wrapper.main_wrapper.t_c')
        div_elements = await wrapper.query_selector_all('div[class="p_10 t_l f_0 v_b"]')
        if debug:
            print("Gathered div elements")
        buttons = []
        if debug:
            print(f"Found {len(div_elements)} div elements.")
        for i, div in enumerate(div_elements):
            # get the HTML content of the div element
            div_content = await div.inner_html()
            soup = BeautifulSoup(div_content, "html.parser")

            # Check if the score is a new record
            new_record = soup.find("img", {"class": "playlog_achievement_newrecord", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/newrecord.png'})
            if new_record:
                buttons.append(f'div.p_10:nth-child({i+4}) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > form:nth-child(7) > button:nth-child(2)')
            else:
                buttons.append(f'div.p_10:nth-child({i+4}) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > form:nth-child(6) > button:nth-child(2)')
            #print(f"New record: {new_record}")

        submit_buttons = buttons
        # get all the submit buttons
        if debug:
            print(f"Found {len(submit_buttons)} submit buttons.")
            print(submit_buttons)

        results = []
        for i in range(len(submit_buttons)):
            if debug:
                print(f"Clicking submit button {i+1}")
            #await page.wait_for_selector(submit_buttons[i])
            await page.wait_for_load_state('load')
            #await asyncio.sleep(2)

            button = await page.query_selector(submit_buttons[i])

            await button.click()

            # wait for the page to load after clicking the button
            await page.wait_for_selector('div[class="gray_block m_10 m_t_0 p_b_5 f_0"]')

            # Inject and execute the script
            script = """
                javascript:void(function(){if(['maimaidx-eng.com','maimaidx.jp'].indexOf(document.location.host)>=0&&(document.location.pathname.indexOf('/maimai-mobile/record/playlogDetail')>=0))document.body.appendChild(document.createElement('script')).src='https://spiritsunite.github.io/maimai-score-details/score-details.js'})();
            """
            await page.evaluate(script)
            
            if debug:
                print("Waiting for the page to load")
            await page.wait_for_load_state('load')
            #await asyncio.sleep(1)
            if debug:
                print("Page loaded")
            


            # parse the HTML content
            wrapper = await page.query_selector('div.wrapper.main_wrapper.t_c')
            card_div = await wrapper.query_selector('div[class="p_10 t_l f_0 v_b"]')
            grey_block_div = await wrapper.query_selector('div[class="gray_block m_10 m_t_0 p_b_5 f_0"]')
            matching_div = await wrapper.query_selector('div[id="matching"][class="see_through_block m_10 p_5 t_l f_0"]')
            if matching_div:
                results.append(await card_div.inner_html() + '\n' + await grey_block_div.inner_html() + '\n' + await matching_div.inner_html())
            else:
                results.append(await card_div.inner_html() + '\n' + await grey_block_div.inner_html())

            if debug:
                print("HTML content parsed")
                print("Waiting for the page to load (back button)")
            #await asyncio.sleep(1)
            if debug:
                print("Page loaded (back button)")

            # click the back button
            await page.click('button[class="f_0"], [type="button"], [onclick="JavaScript:history.back();"]')
            if debug:
                print("Went back to the previous page")
            
            print(len(results))

        if debug:
            for html_block in results:
                with open(f'output_record.txt', 'a', encoding='utf-8') as f:
                    f.write(html_block)
                    f.write('|')
        return results

#asyncio.run(scrape('pugking4', 'Cocothe4th00', debug=True))

def get_score_data(html, debug=False):
    data_list = []
    for html_block in html:
        combo, sync, place = None, None, None
        players = 1

        soup = BeautifulSoup(html_block, "html.parser")
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
        
        # Get the combo badge
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fcplus.png?ver=1.30'})
        if comb:
            combo = 'FC+'
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fc.png?ver=1.30'})
        if comb:
            combo = 'FC'
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/ap.png?ver=1.30'})
        if comb:
            combo = 'AP'
        comb = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/applus.png?ver=1.30'})
        if comb:
            combo = 'AP+'

        if debug:
            print(f"Combo: {combo}")

        # Get the 2p 1st or 2nd place badge
        plac1 = soup.find("img", {"class": "playlog_matching_icon f_r", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/2nd.png'})
        if plac1:
            place = '2nd'
            players = 2
        
        plac2 = soup.find("img", {"class": "playlog_matching_icon f_r", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/1st.png'})
        if plac2:
            place = '1st'
            players = 2

        # Check if the score is a new record deluxe
        new_record_deluxe = soup.find("img", {"class": "playlog_deluxscore_newrecord", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/newrecord.png'})
        if new_record_deluxe:
            new_record_deluxe = True
        else:
            new_record_deluxe = False
        
        # Check if the score is a new record
        new_record = soup.find("img", {"class": "playlog_achievement_newrecord", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/newrecord.png'})
        if new_record:
            new_record = True
        else:
            new_record = False

        # Get the 2p combo badge
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fsplus.png?ver=1.30'})
        if syn:
            sync = 'FS+'
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fs.png?ver=1.30'})
        if syn:
            sync = 'FS'
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fsd.png?ver=1.30'})
        if syn:
            sync = 'FSD'
        syn = soup.find("img", {"class": "h_35 m_5 f_l", 'src': 'https://maimaidx-eng.com/maimai-mobile/img/playlog/fsdplus.png?ver=1.30'})
        if syn:
            sync = 'FSD+'

        if debug:
            print(f"Sync: {sync}")

        # Get crit perfects
        td_list = soup.find_all('td')



        cp_taps = int(td_list[0].text)
        cp_holds = int(td_list[1].text)
        cp_slides = int(td_list[2].text.split('\n')[0])
        cp_touches = int(td_list[3].text.split('\n')[0])
        cp_breaks = int(td_list[4].text.split('\n')[0])

        # Get perfects



        # Get perfect % loss
        p_breaks_loss = soup.find('div', {'class': 'playlog_achievement_perfectloss'}).text.split('\n')[0]


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
        
        if debug:
            #print(f"Difficulty: {diff.upper()}")
            #print(f"Title: {title}")
            #print(f"Score: {score}")
            #print(f"Deluxe Score: {dx_score}")
            ...

        child_dict = {
            'title': title,
            'difficulty': difficulty,
            'score': score,
            'deluxe_score': dx_score,
            'type': type,
            'time': time,
            'track': track,
            'img_link': img_link,
            'combo': combo,
            'sync': sync,
            'place': place,
            'players': players,
            'new_record': new_record,
            'new_record_deluxe': new_record_deluxe
        }
        data_list.append(child_dict)
    return data_list

def scrape_records(segaid, password, debug=False):
    data = get_score_data(asyncio.run(scrape(segaid, password)))
    today = datetime.datetime.now().strftime('%Y/%m/%d')
    file = datetime.datetime.now().strftime('%Y-%m-%d')
    #today = '2023/04/25'
    #file = '2023-04-25'
    filtered_data = [item for item in data if item['time'].startswith(today)]
    if debug:
        print(data)
    json_data = json.dumps(filtered_data, indent=4)
    with open(fr'{file}.json', "w", encoding='utf-8') as f:
        f.write(json_data)
    return filtered_data

scrape_records('pugking4', 'Cocothe4th00')