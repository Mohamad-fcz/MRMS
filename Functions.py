import os
import time
import ipywidgets as widgets
from IPython.display import IFrame
from IPython.display import display
from tqdm.notebook import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def download_wait(directory, timeout=1000, nfiles=None):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return


def MRMS_data_collector(start_date, end_date, meth, dur):
    dates = list()
    for single_date in daterange(start_date, end_date):
        dates.append(single_date.strftime("%Y/%m/%d"))

    pbar = tqdm(range(len(dates)))
    for i in pbar:
        pbar.set_description(f"Downloading data of {dates[i]}")
        options = Options()
        options.add_experimental_option("detach", True)
        options.headless = False
        if not os.path.exists(os.path.join(meth,os.getcwd(), str(dates[i].replace("/", "-")), dur)):
            os.mkdir(os.path.join(os.getcwd(), meth+"-"+str(dates[i].replace("/", "-"))+"-"+dur))
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": os.path.join(os.getcwd(), meth+"-"+str(dates[i].replace("/", "-"))+"-"+dur),
                 ### Set the path accordingly
                 "download.prompt_for_download": False,  ## change the downpath accordingly
                 "download.directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        # the driver is defined for Google Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # pass the URL of desired website
        if meth == "GaugeCorr":
            url = "https://mtarchive.geol.iastate.edu/" + dates[i] + "/mrms/ncep/GaugeCorr_"+dur+"/"
        else:
            url = "https://mtarchive.geol.iastate.edu/" + dates[i] + "/mrms/ncep/MultiSensor_"+dur+"_Pass2/"
        driver.get(url)
        driver.implicitly_wait(60)
        # wait until the page has fully loaded and the screenshot is of the entire page
        d_list = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=meth)
        for d in d_list:
            d.click()
            d_list.extend([a for a in driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=meth) if a not in d_list])
        download_wait(directory=os.path.join(os.getcwd(), meth+"-"+str(dates[i].replace("/", "-"))+"-"+dur))
        driver.quit()


def gui_widgets():
    output = widgets.Output()
    start = widgets.DatePicker(
        description='Pick start'
    )

    end = widgets.DatePicker(
        description='Pick end'
    )
    method = widgets.Dropdown(
        options=['MultiSensor', 'GaugeCorr'],
        value='MultiSensor',
        description='method:',
        disabled=False,
    )

    duration = widgets.Dropdown(
        options=[('1 Hour', "QPE_01H"), ('24 Hour', "QPE_24H"), ('72 Hour', "QPE_72H")],
        value='QPE_01H',
        description='Duration:'
    )

    button = widgets.Button(description="Start download", button_style='success',
                            layout=widgets.Layout(flex='3 1 0%', width='auto'),
                            disabled=False, tooltip='Click me',
                            icon='check')

    def on_button_clicked(b):
        with output:
            MRMS_data_collector(start_date=start.value, end_date=end.value, meth=method.value, dur=duration.value)

    button.on_click(on_button_clicked)
    items = [start, end, method,duration, button]
    tab_nest = widgets.GridBox(items, layout=widgets.Layout(grid_template_columns="repeat(2, 400px)"))
    return display(tab_nest, output)


gui_widgets()

