import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv

load_dotenv()
segaid = os.getenv('SEGA_ID')
password = os.getenv('PASSWORD')

def get_score_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    score_data = []

    for score_block in soup.select('.music_master_score_back'):
        difficulty = score_block.select_one('img').get('src')
        level = score_block.select_one('.music_lv_block').text.strip()
        title = score_block.select_one('.music_name_block').text.strip()
        score = score_block.select_one('.music_score_block:nth-of-type(1)').text.strip()
        deluxe_score_block = score_block.select_one('.music_score_block:nth-of-type(2)').text.strip()
        deluxe_score = deluxe_score_block.split('/')[0].strip()
        total_deluxe_score = deluxe_score_block.split('/')[1].strip()
        music_icon_backs = [img.get('src') for img in score_block.select('.music_icon_back')]
        music_icon_aas = [img.get('src') for img in score_block.select('.music_icon_aa')]
        music_icon_fcs = [img.get('src') for img in score_block.select('.music_icon_fc')]

        score_data.append({
            'difficulty': difficulty,
            'level': level,
            'title': title,
            'score': score,
            'deluxe_score': deluxe_score,
            'total_deluxe_score': total_deluxe_score,
            'music_icon_backs': music_icon_backs,
            'music_icon_aas': music_icon_aas,
            'music_icon_fcs': music_icon_fcs,
        })

    return score_data



async def scrape(version, fuck_you_work, segaid, password):
    async with async_playwright() as p:

        if fuck_you_work == 0:
            fuck = 'basic'
        elif fuck_you_work == 1:
            fuck = 'advanced'
        elif fuck_you_work == 2:
            fuck = 'expert'
        elif fuck_you_work == 3:
            fuck = 'master'
        else:
            fuck = 'remaster'



        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # navigate to the login page
        await page.goto('https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/&back_url=https://maimai.sega.com/')

        # wait for the login page to load
        await page.wait_for_selector('span[class="c-button--openid--segaId"]')

        # click the SEGA ID button
        await page.click('span[class="c-button--openid--segaId"]')

        # wait for the SEGA ID form to load
        await page.wait_for_selector('input[type="text"][id="sid"]')

        # fill in login credentials
        await page.fill('input[type="text"][id="sid"]', segaid)
        await page.fill('input[type="password"][id="password"]', password)

        # click the login button
        await page.click('input[type="submit"][class="c-button--login"]')

        # wait for the page to load after login
        await page.wait_for_selector('a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')

        # click the record menu
        await page.click('a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')

        # wait for the sub-record music menu to appear
        await page.wait_for_selector('img[src="https://maimaidx-eng.com/maimai-mobile/img/menu_sub_record_music.png?ver=1.30"]')

        # click the sub-record music menu
        await page.click('img[src="https://maimaidx-eng.com/maimai-mobile/img/menu_sub_record_music.png?ver=1.30"]')

        # wait for the version menu to appear
        await page.wait_for_selector('img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_music_version.png"]')

        # click the version menu
        await page.click('img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_music_version.png"]')

        # wait for the dropdown menu to appear
        await page.wait_for_selector('select[class="w_300 m_10"]')

        await page.select_option('select[class="w_300 m_10"]', str(version))

        # wait for the master music button to appear
        await page.wait_for_selector(f'button[value="{fuck_you_work}"]')

        # click the master music button
        await page.click(f'button[value="{fuck_you_work}"]')

        # wait for the page to load after clicking the button
        await page.wait_for_selector(f'div[class="music_{fuck}_score_back pointer w_450 m_15 p_3 f_0"]')
        await page.wait_for_load_state('load')

        # parse the HTML content
        wrapper = await page.query_selector('div.wrapper.main_wrapper.t_c')
        div_elements = await wrapper.query_selector_all(f'div[class="music_{fuck}_score_back pointer w_450 m_15 p_3 f_0"]')
        #print("div_elements:", div_elements)
        results = []
        for count, div in enumerate(div_elements):
            # get the HTML content of the div element
            div_content = await div.inner_html()
            results.append(div_content)

        for test in results:
            with open(f'output_{fuck_you_work}.txt', 'a', encoding='utf-8') as f:
                f.write(test)
                f.write('|')


        #Print a message to indicate that the program has finished executing and the output has been saved
        print(f"Saved version {version} as output_{fuck_you_work}.txt'")
        print(len(results))

#asyncio.run(scrape(2, segaid, password))


for diff in range(5):
    for ver in range(20):
        asyncio.run(scrape(ver, diff, segaid, password))

#for ver in range(20):
        #asyncio.run(scrape(ver, segaid, password))