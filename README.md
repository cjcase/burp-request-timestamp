# burp-request-timestamp.py
Burp extension to replace a variable in the request with a fresh unix epoch timestamp
Some pesky frameworks use this as a mitigation method against manual analysis. This helps break those ;)

## How to use
* Add the extension to burp, remember to have Jython configured beforehand
* The string replace should work on every request, compatible with Intercept, Intruder, Repeater etc. 

Example request with the replace string:
```text
GET /data?t=%TIMESTAMP% HTTP/1.1
Host: example.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Time: %TIMESTAMP%
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close


```
Example request after replacing:
```text
GET /data?t=1649056668209 HTTP/2
Host: example.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Time: 1649056668209
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9


```

* Verify with logger that the request is being modified as necessary
* Happy Hacking!

**Issues and Pull requests are greatly appreciated :)**
