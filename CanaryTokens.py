from requests import post
from user_agent import generate_user_agent
import os


def header():
    os.system('cls' if os.name=='nt' else 'clear');print("""
 ██████╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗  ████████╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝  ╚══██╔══╝
██║     ███████║██╔██╗ ██║███████║██████╔╝ ╚████╔╝█████╗██║   
██║     ██╔══██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝ ╚════╝██║   
╚██████╗██║  ██║██║ ╚████║██║  ██║██║  ██║   ██║        ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝   
                                                              
                github.com/filza2
""")
header()
url1=input('- Enter Your url: ')
if url1=='':exit('- Enter a url ! ')
if 'http://' in url1:pass
elif 'https://' in url1:pass
else:exit('- Enter valid url please !')
email=input("- Enter Your Email : ")
if '@' not in email.strip():exit('- Enter valid Email ! ')
r=post("https://canarytokens.org/d3aece8093b71007b5ccfedad91ebb11/generate",
       headers={
           'Host': 'canarytokens.org',
           'User-Agent': generate_user_agent(),
           'Accept': 'application/json, text/plain, */*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Origin': 'https://canarytokens.org',
           'Referer': 'https://canarytokens.org/nest/',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'Te': 'trailers',
           'Connection': 'close'},
       files={
           "redirect_url": (None,url1),
           "email": (None,email),
           "memo": (None,"Hi There !, Your Canarytoken was Triggered, ---> (https://github.com/filza2)"),
           "token_type": (None,"slow_redirect")})
try:data=r.json()
except ValueError:exit(f"- Error Response is not JSON. raw text :\n{r.text}")
token=data.get("token");token_url=data.get("token_url");auth_token=data.get("auth_token");email1=data.get("email");error=data.get("error");error_message=data.get("error_message");url2=f'https://canarytokens.com/filza2/{token}'
if error:print("- Error, The website returned an error : ",error_message or error)
if token:pass
else:exit("\n- Error No Token found in response")
if token_url:pass
else:exit("\n- Error No URL found in response")
try:
    r2=post('https://hideuri.com/api/v1/shorten',headers={'Host': 'hideuri.com','Cookie': '_cfvdata=','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://hideuri.com/','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '47','Origin': 'https://hideuri.com','Te': 'trailers'},data=f'url={url2}')
    if 'result_url' in r2.json():url3=r2.json()['result_url']
    else:url3=None
except:url3=None
header();print(f'''- Your Token: {token}
- Your url: {url2}
- Shorted url: {url3}
- Your Auth Token: {auth_token}
- Your Email: {email1}\n''')
