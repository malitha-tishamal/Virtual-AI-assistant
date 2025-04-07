from requests_html import HTMLSession

def weather(location="Labuduwa"):
    # Create an HTML session
    s = HTMLSession()
    url = f"https://www.google.com/search?q=weather+{location}"
    
    # Send a GET request to the URL with a user-agent header
    r = s.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})
    
    # Extract weather details
    temp_element = r.html.find('span#wob_tm', first=True)
    unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
    desc_element = r.html.find('span#wob_dc', first=True)

    # Check if elements are found
    if not temp_element or not unit_element or not desc_element:
        print("Could not retrieve weather information. Google might be blocking automated requests.")
        return

    # Extract text from elements
    temp = temp_element.text
    unit = unit_element.text
    desc = desc_element.text

    # Print weather details
    print(f"Weather in {location}:")
    print(f"Temperature: {temp}{unit}")
    print(f"Condition: {desc}")

if __name__ == "__main__":
    print("Fetching weather details for Labuduwa...\n")
    weather("Labuduwa")