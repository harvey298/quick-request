import requests, platform
from colour_lib import caution, error, info
debug = False

tor_proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

def mk_req(api,headers=False,json=False,type="get",tor=False):
    try:
        if tor == True:
            if platform.system() != "Windows":
                req = requests.get(api,proxies=tor_proxies)
                return req
            else:
                pass
        if type == "get":
            if headers != False:
                if json != False:
                    req = requests.get(api,headers=headers,json=json)
                else:
                    req = requests.get(api,headers=headers)
            elif json != False:
                if headers != False:
                    req = requests.get(api,headers=headers,json=json)
                else:
                    req = requests.get(api)
            else:
                req = requests.get(api)
        elif type == "post":
            if headers != False:
                if json != False:
                    req = requests.post(api,headers=headers,json=json)
                else:
                    req = requests.post(api,headers=headers)
            elif json != False:
                if headers != False:
                    req = requests.post(api,headers=headers,json=json)
                else:
                    req = requests.post(api)
            else:
                req = requests.post(api)
        else:
            if headers != False:
                if json != False:
                    req = requests.get(api,headers=headers,json=json)
                else:
                    req = requests.get(api,headers=headers)
            elif json != False:
                if headers != False:
                    req = requests.get(api,headers=headers,json=json)
                else:
                    req = requests.get(api)
            else:
                req = requests.get(api)

        return req
    except ConnectionRefusedError as e:
        error(e,0)
        return False
    except ConnectionAbortedError as e:
        error(e,0)
        return False
    except ConnectionResetError as e:
        error(e,0)
        error("Am I allowed to connect?",0)
        return False
    except requests.exceptions.ConnectionError as e:
        error(e,0)
        return False
    except requests.exceptions.InvalidURL as e:
        error(e,0)
        return False

def bug(api):
    req = mk_req(api)
    if req == False:
        return False


    response = req(api)
    info("API Url: "+api)
    info("Response Status Code: "+str(req.status_code))
    if response == False:
        info("No Vaild Response to Display! Not attempting!")
    else:
        info("Full Response: \n"+str(req.json()))


def server_status(api):
    req = mk_req(api)
    if req == False:
        return False
    elif req.status_code == 200:
        return True
    else:
        return False

def req(api,headers=False,json=False,type="get",tor=False):
    req = mk_req(api,headers=headers,json=json,type=type,tor=tor)
    if req == False:
        return False
    reqs = req.status_code
    if "2" in str(reqs):
        if reqs == 200:
            return req.json()
        elif reqs == 520:
            error("520 status code! Unknown response",0)
            return False
        else:
            caution(str(reqs)+" status code! Data maybe fine?")
            return req.join()
    elif "4" in str(reqs):
        if reqs == 400:
            error("Bad Request!",0)
            return False
        elif reqs == 401:
            error("401 status code! Do I need some credentials?",0)
            return False
        elif reqs == 403:
            error("403 status code! Forbidden! is this the right api? do I need some credentials?",0)
            return False
        elif reqs == 404:
            error("404 status code! Resource not found! is the api correct?",0)
            return False
        else:
            error(str(reqs)+" status code is out of my 400 code scope and I do not know how to handle it!",0)
            return False
    else:
        if reqs == 301:
            caution("301 Status code data may be malformed!")
            return req.json()
        elif reqs == 503:
            error("503 status code! The server is not ready to handle this api request!",0)
            return False
        else:
            error(str(reqs)+" status code is out of my scope and I do not know how to handle it!",0)
            if debug == True:
                caution("Debug is enabled sending back the data")
                return req.json()
            else:
                return False
    
