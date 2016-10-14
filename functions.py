import binascii, requests, json, datetime

def sendRequest(ip,host,endpoint,static_user_data,uid,action):

    data = {'userData':static_user_data, 'action':action, 'tagUid':binascii.hexlify(uid), 'time':datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')}

    print('\nSend server request to: ' + ip + " " + host)

    url = ''
    headers = {'Content-Type': 'application/json', 'X-TagUID': uid}
    r = None

    if ip != '':
        url = 'http://' + ip + '/' + endpoint
        headers = {'host': host, 'Content-Type': 'application/json', 'X-TagUID': uid}
    else:
        url = 'http://' + host + '/' + endpoint

    #Post request with host name
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers, timeout=3)
    except requests.exceptions.ConnectionError:
        print "Network connection error"
    except requests.exceptions.Timeout:
        print "Timeout exception"
                
    if r != None:
        if r.status_code == 200:
            print('Server response:\n' + r.content)
        else:
            print 'REQUEST ERROR! Status code: ' + str(r.status_code)
            print('Server response:\n' + r.content)