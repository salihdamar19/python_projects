from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def kullanici_giris():
    try:
        user_input = str(input('Cikmak icin "cikis" yazin.\nAratmak istediginiz hisse kodunu giriniz: '))
    except ValueError:
        print('Lutfen dogru duzgun yaziniz')
    else:
        return user_input

def search(arama):
    katilim_flag = False
    for i in range(0, len(elemanlar), 2):
        kod = elemanlar[i].text
        isim = elemanlar[i+1].text
        if kod == arama:
            print(f"{kod} - {isim} katilim endeksinde.")
            katilim_flag = True
    if katilim_flag == False:
        print(f"{arama} katilim endeksinde degil.")

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.kap.org.tr/tr/Endeksler")

tum_endeksler = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Tüm Endeksler')]"))
)
tum_endeksler.click()

endeks_arama = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Arama..."]'))
)
endeks_arama.send_keys("BIST KATILIM TUM")

sonuc = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'BIST KATILIM TUM')]"))
)
sonuc.click()

tablo = driver.find_element(By.ID, 'indicesTable')
elemanlar = driver.find_elements(By.CSS_SELECTOR, "[class*='no-underline']")

#print(f"Bulunan eleman sayisi: {len(elemanlar)}")

print("© 2026 Salih Damar\nKatılım Bot v1.0")

user_input = kullanici_giris()
while  user_input != 'cikis':
    search(user_input)
    user_input = kullanici_giris()

driver.quit()