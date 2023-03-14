from requests import post
import os

def header():
    os.system('cls' if os.name=='nt' else 'clear');print("""
 ██████╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗  ████████╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝  ╚══██╔══╝
██║     ███████║██╔██╗ ██║███████║██████╔╝ ╚████╔╝█████╗██║   
██║     ██╔══██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝ ╚════╝██║   
╚██████╗██║  ██║██║ ╚████║██║  ██║██║  ██║   ██║        ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝   
                                                              
                By @TweakPY - @vv1ck
""")
header()
url1=input('- Enter Your url: ')
if url1=='':exit('- Enter a url ! ')
if 'http://' in url1:pass
elif 'https://' in url1:pass
else:exit('- Enter valid url please !')
email=input("- Enter Your Email : ")
if '@' not in email.strip():exit('- Enter valid Email ! ')

d=f"""-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="type"

slow_redirect
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="email"

{email}
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="webhook"


-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="fmt"


-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="memo"

Hi There ! , Your Canarytoken was Triggered , From @TweakPY - @vv1ck
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="azure_id_cert_file_name"


-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="cmd_process"


-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="clonedsite"


-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="sql_server_table_name"

TABLE1
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="sql_server_view_name"

VIEW1
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="sql_server_function_name"

FUNCTION1
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="sql_server_trigger_name"

TRIGGER1
-----------------------------406211663434286349742714178120
Content-Disposition: form-data; name="redirect_url"

{url1}
-----------------------------406211663434286349742714178120--
"""
r=post("https://canarytokens.org/generate",headers={'Host': 'canarytokens.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------406211663434286349742714178120','Content-Length': '1695','Origin': 'https://canarytokens.com','Referer': 'https://canarytokens.com/generate','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},data=d).json()

try:
    if r["Error"]==2:exit('- Error ! ')
    elif r["Url_components"]==None:exit('- Error ! ')
    elif r["Message"]=="No memo supplied":exit('- Error ! ')
    else:token=r["Token"];em=r["Email"];url2=f'https://canarytokens.com/TweakPY.vv1ck/{token}'
except:exit('- Error ! ')
try:
    r2=post('https://hideuri.com/api/v1/shorten',headers={'Host': 'hideuri.com','Cookie': '_cfvdata=','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://hideuri.com/','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '47','Origin': 'https://hideuri.com','Te': 'trailers'},data=f'url={url2}')
    if 'result_url' in r2.json():url3=r2.json()['result_url']
    else:url3=None
except:url3=None

header();print(f'''- Your Token: {token}')
- Your url: {url2}
- Shorted url: {url3}
- Your Email: {em}\n''')
