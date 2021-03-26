#!/usr/bin/env python3

from selenium import webdriver
import selenium
import time

def get_screenshot(icao='', fname='screenshot.png'):
  #url = f"https://globe.adsbexchange.com/?icao={icao}"
  #url = f'https://globe.adsbexchange.com/?icao={icao}&zoom=11&hideSidebar&hideButtons'
  url = f'https://ramonk.net/tar1090/?icao={icao}&zoom=11&hideSidebar&hideButtons'

  co = selenium.webdriver.chrome.options.Options()
  co.add_argument("--headless")
  co.add_argument("--no-sandbox")
  co.add_argument("--incognito")
  browser = selenium.webdriver.Chrome(options=co)

  browser.get(url)
  #elems = browser.find_elements_by_css_selector("#map_canvas canvas")
  #if not len(elems):
  #  raise Exception("no elements found (eg missing map canvas)")
  #elif not elems[0].is_displayed():
  #  raise Exception(f"have {len(elems)}, but the first isn't displayed")

  time.sleep(3)
  br = browser.save_screenshot(fname)
  print(f"done {br}")

  browser.quit()

  return fname

f = get_screenshot(fname='/tmp/snap.png')
print(f)

