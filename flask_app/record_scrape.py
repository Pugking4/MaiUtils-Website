from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

def scrape(segaid, password):
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # navigate to the login page
    driver.get("https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/record//&back_url=https://maimai.sega.com/")

    # wait for the login page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="c-button--openid--segaId"]')))

    # click the SEGA ID button
    driver.find_element(By.CSS_SELECTOR, 'span[class="c-button--openid--segaId"]').click()

    # wait for the SEGA ID form to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][id="sid"]')))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"][id="password"]')))

    # fill in login credential
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"][id="sid"]').send_keys(segaid)
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"][id="password"]').send_keys(password)

    # click the login button
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][class="c-button--login"]').click()

    # wait for the error message to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_back.png"][class="w_80 m_t_10"]')))

    # click the back button
    driver.find_element(By.CSS_SELECTOR, 'img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_back.png"][class="w_80 m_t_10"]').click()

    # wait for the page to load after login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')))

    # click the record menu
    driver.find_element(By.CSS_SELECTOR, 'a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]').click()

    # wait for the page to load after clicking the button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="p_10 t_l f_0 v_b"]')))

    print("Waiting for page to load...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Page loaded!")

    # parse the HTML content
    wrapper = driver.find_element(By.CSS_SELECTOR, 'div.wrapper.main_wrapper.t_c')
    div_elements = wrapper.find_elements(By.CSS_SELECTOR, 'div[class="p_10 t_l f_0 v_b"]')
    print("Gathered div elements")
    results = []
    for div in div_elements:
        # get the HTML content of the div element
        div_content = div.get_attribute('innerHTML')
        results.append(div_content)

    html_data = []
    for html_block in results:
        html_data.append(html_block)
        #with open(f'output_record.txt', 'a', encoding='utf-8') as f:
        #    f.write(html_block)
        #    f.write('|')
    return html_data