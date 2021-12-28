from urllib.request import urlopen
import urllib.request

class Htmlator():
    def __init__(self) -> None:
        pass

    def extract_html(self, url):
        """extract the raw html from a webpage"""
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        # print(html)
        return html

    def save_img_from_url(self, url, save_path):
        """saves an image to the indicated path"""
        urllib.request.urlretrieve(url, save_path)
        return save_path

    
    def extract_code(raw_html, term):
        start_idx = raw_html.find('<{}'.format(term)) + len('<{}'.format(term))
        end_idx = raw_html.find('<\{}'.format(term))
        code = raw_html[start_idx:end_idx]
        print(code)
        return code


    

# url = "http://challenge01.root-me.org/programmation/ch8/"

# h = Htmlator()
# raw = h.extract_html(url)
# idx = raw.find('<img src="')
# start_index = idx + len('<img src="')
# end_index = raw.find('" /><br><br><')
# result = raw[start_index:end_index]
# h.save_img_from_url(result, 'img/captcha.png')



