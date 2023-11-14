import requests
import os
import json

from pathlib import Path
from bs4 import BeautifulSoup as soup


class SipanduHandler:
    
    def __init__(self):
        self.session    = requests.Session()
        self.url        = 'https://elitery.sipandu.co.id'
        self.login_url  = self.url + '/scp/login.php'
        self.task_url   = self.url + '/scp/tasks.php'
        
    def generate_cookie(self):
        html        = self.session.get(self.login_url)
        cookie      = html.cookies.get_dict() # ambil response header cookie
        home_dir    = os.path.expanduser('~')
        sipandu_dir = home_dir + '/.sipandu'
        
        if not os.path.exists(sipandu_dir):
            os.makedirs(sipandu_dir)
        
        with open(os.path.join(sipandu_dir, 'cookie.json'), 'w') as cookie_file:
            cookie_file.write(json.dumps(cookie))
        
        return html

    def login(self, user_email, user_password):
        """
        Cookie otomatis didapatkan melalui response header
        'Set-Cookie' ketika mengambil csrf token kemudian
        ketika login akan dikirim di dalam 1 session yang sama
        """
        
        # ambil csrf token dari session di generate_cookie()
        # untuk login cookie menggunakan dari session sebelumnya sehingga tidak perlu membaca file
        html = self.generate_cookie()
        csrf_token  = soup(html.text, 'lxml').find('input', {"name": "__CSRFToken__"})['value']
        payload     = {
            "__CSRFToken__" : csrf_token,
            "do" : "scplogin",
            "userid" : user_email,
            "passwd": user_password,
            "ajax" : "1"
        }
        r = self.session.post(self.login_url, data=payload).json()
        #temporary code
        if r.get('status') == 302 and r.get('redirect') == 'index.php':
            print('success login')
            return 'Login Berhasil'
        
        return r
    
