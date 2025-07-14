import requests

if 1 == 2:
    x = requests.get("http://httpbin.org/get")

    print(x.headers)
    print(x.headers['Server'])

    if x.status_code == 200:
        print("Success! Site found.")
    elif x.status_code == 404:
        print("404 Not found!")

    print(x.elapsed)
    print(x.cookies)

    x= requests.get('http://httpbin.org/get?id=1')
    print(x.url)

    x= requests.get('http://httpbin.org/get', params={'id' : '1'}, headers={'Accept' : 'application/json', 'test_header' : 'test'})
    print(x.text)

    x = requests.delete('http://httpbin.org/delete')
    print(x.text)

    x = requests.post('http://httpbin.org/post', data={'a' : '1', 'b' : '2', 'c' : '3'})
    print(x.text)

#file = {'file' : open('google.png', 'rb')}
#x = requests.post('http://httpbin.org/post', files=file)
#print(x.text)

    x = requests.get('http://httpbin.org/get', auth=("username", "password"))
    print(x.text)

#x = requests.get('https://expired.badssl.com', verify=False)
#print(x.text)
else:
    x = requests.Session()
    x.cookies.update({'a' : 'b'})
    print(x.get('http://httpbin.org/cookies').text)
    print(x.get('http://httpbin.org/cookies').text)
