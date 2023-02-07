from urllib.parse import urlencode
from urllib.request import urlretrieve
import urllib
from pathlib import Path

SCREENSHOTS_FOLDER = "screenshots"

def get_screenshot_from_adress(adress,folder:str=SCREENSHOTS_FOLDER) -> str:
    """Get screenshot from an internet adress using flash api. The screenshot is saved in the `SCREENSHOTS_FOLDER`.

    Args:
        adress (str): Adress to take screenshot from
        folder (str, optional): Folder to save the screenshot. Defaults to SCREENSHOTS_FOLDER.

    Returns:
        str: Path to the screenshot
    """
    
    with open("API_Keys/Flash_key") as f:
        FLASH_KEY = f.read()
    location = Path(folder,str(adress) + ".jpeg")
    params = urlencode(dict(access_key=FLASH_KEY,format="jpeg",delay="1",fresh="true",full_page="true",url=f"http://{adress}"))
    try:
        urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, location)
        return Path(str(location))
    except urllib.error.HTTPError as e:
        print(f"Taking screenshot error with Flash API : {str(e)}")
        return Path("")

if __name__ == "__main__":
    get_screenshot_from_adress("airfrance.com.ml")