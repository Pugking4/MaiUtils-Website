from playwright.async_api import async_playwright

async def scrape(segaid, password):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
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

        # Inject and execute the script
        #script = """
        #    void(function(d){if(['maimaidx-eng.com','maimaidx.jp'].indexOf(d.location.host)>=0){var s=d.createElement('script');s.src='https://myjian.github.io/mai-tools/scripts/all-in-one.js?t='+Math.floor(Date.now()/60000);d.body.append(s);}})(document)
        #"""
        #await page.evaluate(script)

        print("Waiting for page to load...")
        await page.wait_for_load_state('load')
        #await page.wait_for_timeout(5000)
        print("Page loaded!")

        # parse the HTML content
        wrapper = await page.query_selector('div.wrapper.main_wrapper.t_c')
        div_elements = await wrapper.query_selector_all('div[class="p_10 t_l f_0 v_b"]')
        print("Gathered div elements")
        results = []
        for div in div_elements:
            # get the HTML content of the div element
            div_content = await div.inner_html()
            results.append(div_content)

        html_data = []
        for html_block in results:
            html_data.append(html_block)
            #with open(f'output_record.txt', 'a', encoding='utf-8') as f:
            #    f.write(html_block)
            #    f.write('|')
        return html_data

        #Print a message to indicate that the program has finished executing and the output has been saved
        print(f"Saved records as output_records.txt'")

#asyncio.run(scrape(segaid, password))
    