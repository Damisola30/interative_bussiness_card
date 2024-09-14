import os
import wget
import asyncio
import shutil
from pyppeteer import launch



async def screenshot(file_path, element_id):
    """
    Takes a screenshot of a specific HTML element.
    """
    # Path to your existing Chrome/Chromium installation
    chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

    # Launch the browser using the existing Chrome/Chromium installation
    browser = await launch(headless=True, executablePath=chrome_path)
    page = await browser.newPage()

    # Open the HTML file
    await page.goto(f"file://{file_path}")

    # Wait for the element to be visible
    await page.waitForSelector(f'#{element_id}')

    # Capture the screenshot of the specific element
    element = await page.querySelector(f'#{element_id}')
    await element.screenshot({'path': f'my_screenshot_folder/{element_id}.png'})

    # Close the browser
    await browser.close()



def download_image(image_path, save_path):
    """
    Downloads an image from a given local path by copying it to the save path.
    """
    shutil.copy(image_path, save_path)
    print("File downloaded successfully")

def capture_and_download_element(template_file, element_id, download_path):
    """
    Captures a screenshot of a specific HTML element and downloads it.
    """
    # Create a new event loop if one doesn't exist
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Take screenshot of the specified HTML element
    loop.run_until_complete(screenshot(template_file, element_id))

    # Construct the local file path of the screenshot
    screenshot_file = f'my_screenshot_folder/{element_id}.png'

    # Download the screenshot (in this case, it's already local, so just move it)
    download_image(screenshot_file, download_path)

    # Close the event loop
    loop.close()

    asyncio.get_event_loop().run_until_complete(screenshot(template_file, element_id))

# def download_image(image_path, save_path):
#     """
#     Downloads an image from a given local path using wget.
#     """
#     wget.download(image_path, save_path)
#     print('File downloaded successfully')

# def capture_and_download_element(template_file, element_id, download_path):
#     """
#     Captures a screenshot of a specific HTML element and downloads it.
#     """
#     # Take screenshot of the specified HTML element
#     screenshot(template_file, element_id)
    
#     # Construct the local file path of the screenshot
#     screenshot_file = f'my_screenshot_folder/{element_id}.png'
    
#     # Download the screenshot (in this case, it's already local, so just move it)
#     download_image(screenshot_file, download_path)

# Example usage
# template_file = 'templates/your_template.html'
# element_id = 'businessCard'
# download_path = 'downloaded_business_card.png'
# capture_and_download_element(template_file, element_id, download_path)
