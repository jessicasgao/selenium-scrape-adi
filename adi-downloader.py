from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os, zipfile
import csv
import glob
import pandas as pd
import time

def download_adi():

    """Scrape 50 zipped files from Area Deprivation Index website and append into a single csv file.

    Args:
        [No args.]

    Returns:
        [No returned object.]

    """

    output_dir = r'output/dir/here'

    # Log into ADI website
    driver = webdriver.Chrome()
    driver.get("https://www.neighborhoodatlas.medicine.wisc.edu/login")

    username = driver.find_element_by_id("login-email")
    username.clear()
    username.send_keys("type-username-here")

    password = driver.find_element_by_id("login-pass")
    password.clear()
    password.send_keys("type-password-here")

    # Navigate to ADI data page and download each of 50 states
    driver.find_element_by_css_selector('.form-items.small-box').click()
    driver.get("https://www.neighborhoodatlas.medicine.wisc.edu/download")
    driver.find_element_by_css_selector("input[type='radio'][value='zipcode']").click()

    select = Select(driver.find_element_by_name("state-name"))
    options = select.options
    for index in range(0, len(options) - 1):
        select.select_by_index(index)
        driver.find_element_by_xpath("//input[@value='Download Data']").click()
        time.sleep(5)

    driver.quit()

    # Create subfolder to unzip downloaded data zips into 
    adi_folder = 'local/download/folder/adi/subfolder'
    if not os.path.exists(adi_folder):
        os.makedirs(adi_folder)
    dir_name = 'local/download/folder'
    extension = ".zip"
    prefix = "adi-download"

    # change directory from working dir to dir with files
    os.chdir(dir_name) 

    # Unzip all 50 data files
    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension) & item.startswith(prefix): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(adi_folder) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file

    # Do quick check to see that all data files unzipped
    os.chdir(adi_folder)
    adi_list = glob.glob('*_2015*.txt')
    if not len(adi_list) == 51:
        raise ValueError('There are not have enough/too many states.')

    # Append data files
    df = pd.DataFrame()
    for txt_file in adi_list:
        in_csv = pd.read_csv(txt_file, sep=",")
        df = df.append(in_csv)

    # Ensure all zip codes are 9-digit
    zips = df[['ZIPID', "ADI_NATRANK"]].copy()
    zips['ZIPID'] = zips['ZIPID'].str.replace(r'\D', '').str.pad(width=9, side='left', fillchar='0')

    # Save singular appended data file
    zips.to_csv(os.path.join(output_dir, "2015_adi_full.csv"), index=False)

    # Delete individual data files
    os.chdir(dir_name)
    if os.path.exists(adi_folder):
        files = glob.glob('adi/*')
        for f in files:
            os.remove(f)
        os.rmdir(adi_folder)

if __name__ == "__main__":
    download_adi()
