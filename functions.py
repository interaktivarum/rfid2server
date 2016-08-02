import binascii, requests, json, datetime

def sendToServer(ip,host,endpoint,static_user_data,uid,action):

    params = {'userData':static_user_data, 'action':action, 'tagUid':binascii.hexlify(uid), 'time':datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')}

    print('\nSend server request to: ' + ip + " " + host)

    if ip != '':
        #Post request with ip and host name
        r = requests.post('http://' + ip + '/' + endpoint, params=json.dumps(params), headers={'host': host})        
    else:
        #Post request with host name
        r = requests.post('http://' + host + '/' + endpoint, params=json.dumps(params), headers={})

    if r.status_code == 200:
        print('Server response:\n' + r.content)
    else:
        print 'REQUEST ERROR! Status code: ' + str(r.status_code)
        print('Server response:\n' + r.content)
