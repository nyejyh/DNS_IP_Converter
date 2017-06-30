#!/usr/bin/env python
### Program to translate DNS to IP, by Jason Huang

## Call libraries
import socket #extract IP address from URLS
import urllib
import urllib2
import urlparse #cut up URLs

## Declare variables
druple = []
ips = []

## You can replace testobject with your own working object that signals "200". 
## Because testobject points to google, only this link will show "200".
testobject = 'http://www.google.com/index.html'

## Open & define text file
with open("gitkrills.txt") as openfile: #keep the file open
    for line in openfile:
        if "SERVING" in line:
            line = line.strip() #get rid of "\n" at end of every line
            druple.append(line[8:]) #skip first 8 characters, add rest

## Convert and display
for i in druple:
    try:
        data = socket.gethostbyname_ex(i)
        if len(data[2])<2:
            string = ''.join(data[2])
            ips.append(string)
            print i + " = " + string
        else:
            string1 = ''.join(data[2][0])
            string2 = ''.join(data[2][-1])
            ips.append(string1)
            ips.append(string2)
            print i + " = " + string1 + ", " + string2
    except socket.gaierror:
        print i + " = Missing IP Address"
		
## curlwise it's curl -I --header 'Host:<HEAD>' 'http://<IP>/ok.txt'
## request format is class urllib2.Request(url[, data][, headers]...
## [, origin_req_host][, unverifiable])
dFish = urlparse.urlparse(testobject)
for i in ips:
    strip = ''.join(i)
    numb = str(strip)
    try:
        fish = dFish.scheme + '://' + numb + dFish.path #create IP & txt path
        hostheader = {'Host' : dFish.netloc} #create dictionary
        request = urllib2.Request(fish, None, hostheader) #insert url & header
        response = urllib2.urlopen(request, timeout=4)
        respcode = response.getcode()
        if respcode == 200:
            print numb + ' server green, is ' + str(respcode)
        else:
            print numb + ' server orange, is ' + str(respcode)
        response.close()
    except KeyboardInterrupt:
        exit()
    except:
        print numb + ' has timed out.'
