Title: Make Google Cloud CDN serve gzip compressed content for Nginx server  
Slug: make-google-cloud-cdn-serve-gzip-compressed-content-for-nginx-server
Date: 2020-07-11 20:22:05  
Authors: m157q  
Category: Note
Tags: GCP, Google Cloud Platform, CDN, gzip, Nginx
Summary: How to make Google Cloud CDN serve gzip compressed content.


# Preface

Google Cloud CDN is not like Cloudflare, which can make you serve gzip compressed content on the proxy servers with just one click.


# TL;DR

Add these two lines below into `/etc/nginx/default.conf`

```
gzip_proxied     any;
gzip_vary        on;
```

And restart the Nginx server.


# Explanation

According to [Google Cloud CDN troubleshooting](https://cloud.google.com/cdn/docs/troubleshooting-steps):  

> The first line enables compression even for requests forwarded by a proxy like HTTP(S) load balancing.

> The second line adds a `Vary: Accept-Encoding` header to responses. `Vary: Accept-Encoding` notifies caching proxies such as Cloud CDN that they should maintain separate cache entries for compressed and non-compressed variants of compressible resources.
