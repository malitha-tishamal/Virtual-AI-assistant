#https://www.google.com/search?q=weather+

from requests_html import HTMLSession

def weather():
    s=HTMLSession()
    query = "Moratuwa" 
    url = f"https://www.google.com/search?q=weather+{query}"
 
    r = s.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})
    temp_element = r.html.find('span#wob_tm',first=True)
   
    unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t',first=True)

    desc_element=r.html.find('span#wob_dc',first=True)

    if not temp_element or not unit_element or not desc_element:

        print("Could not retrieve weather information. Google might be blocking automated requests.")

        return
    temp=temp_element.text
    unit=unit_element.text
    desc=desc_element.text

    print(temp)
    print(unit)
    print(desc)
    

    weather()