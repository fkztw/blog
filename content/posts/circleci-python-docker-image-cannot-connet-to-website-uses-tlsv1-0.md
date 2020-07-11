Title: CircleCI Python docker image cannot connet to website uses TLSv1.0  
Slug: circleci-python-docker-image-cannot-connet-to-website-uses-tlsv1-0  
Date: 2020-07-11 16:51:46  
Authors: m157q  
Category: Note
Tags: Python, CircleCI, Docker, SSL, TLSv1.0  
Summary: While writing the test for my side project, I encountered a problem which didn't happen while using Travis CI but CircleCI.


# TL;DR

Add

`sudo sed -i -E 's/MinProtocol[=\ ]+.*/MinProtocol = TLSv1.0/g' /etc/ssl/openssl.cnf`

in `.circleci/config.yml` before running the test which will connect to the website uses TLSv1.0.


# Exception

```
Traceback (most recent call last):
  File "/home/circleci/repo/venv/lib/python3.5/site-packages/urllib3/connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "/home/circleci/repo/venv/lib/python3.5/site-packages/urllib3/connectionpool.py", line 381, in _make_request
    self._validate_conn(conn)
  File "/home/circleci/repo/venv/lib/python3.5/site-packages/urllib3/connectionpool.py", line 976, in _validate_conn
    conn.connect()
  File "/home/circleci/repo/venv/lib/python3.5/site-packages/urllib3/connection.py", line 370, in connect
    ssl_context=context,
  File "/home/circleci/repo/venv/lib/python3.5/site-packages/urllib3/util/ssl_.py", line 377, in ssl_wrap_socket
    return context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/local/lib/python3.5/ssl.py", line 385, in wrap_socket
    _context=self)
  File "/usr/local/lib/python3.5/ssl.py", line 760, in __init__
    self.do_handshake()
  File "/usr/local/lib/python3.5/ssl.py", line 996, in do_handshake
    self._sslobj.do_handshake()
  File "/usr/local/lib/python3.5/ssl.py", line 641, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: UNSUPPORTED_PROTOCOL] unsupported protocol (_ssl.c:728)
```


# Another solution which DIDN'T work for me

```
import requests
import ssl

requests.get(url, verify=ssl.CERT_NONE)
```


# References

- [12. Appendix — pywbem 1.0.0b3.dev1 documentation](https://pywbem.readthedocs.io/en/latest/appendix.html#connectionerror-raised-with-ssl-unsupported-protocol)
- [ssl.SSLError: \[SSL: UNSUPPORTED_PROTOCOL\] unsupported protocol (_ssl.c:852) in Docker Python:3.6-slim - Stack Overflow](https://stackoverflow.com/questions/59408646/ssl-sslerror-ssl-unsupported-protocol-unsupported-protocol-ssl-c852-in-d)
- [web scraping - In Python3.6.5 Requests getting SSL Certificate Error - Stack Overflow](https://stackoverflow.com/questions/54829759/in-python3-6-5-requests-getting-ssl-certificate-error)
