import urllib3

def main():
    http = urllib3.PoolManager()

    auth = "cGVyZm9ybWFuY2U6cGVyZm9ybWFuY2U="
    headers = {
        'User-Agent': 'curl',
        # ruleid: hardcoded-basic-token
        'Authorization': 'Basic ' + auth
    }

    http.request("GET", url, headers=headers)
    
    # ruleid: hardcoded-basic-token
    http.request("GET", url, preload_content=True, headers={'Authorization': 'Basic cGVyZm9ybWFuY2U6cGVyZm9ybWFuY2U='})

    # ok: hardcoded-basic-token
    http.request("GET", url, preload_content=True, headers={'Authorization': 'Basic test'})


from requests import Request, Session

def secret():
    s = Session()
    auth = "cGVyZm9ybWFuY2U6cGVyZm9ybWFuY2U="
    headers = {}
    # ruleid: hardcoded-basic-token
    headers['Authorization'] = 'Basic cGVyZm9ybWFuY2U6cGVyZm9ybWFuY2U='
    req = Request('POST', url, data=data, headers=headers)

    # ruleid: hardcoded-basic-token
    headers['Authorization'] = 'Basic ' + auth
    req = Request('POST', url, data=data, headers=headers)

    # ok: hardcoded-basic-token
    headers['Authorization'] = 'Basic ' + config['basic_auth']
    req = Request('POST', url, data=data, headers=headers)

