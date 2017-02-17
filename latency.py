import subprocess
import re
import operator

host = ["23.23.255.255", "50.18.56.1", "34.248.60.213", "35.160.63.253",
"35.156.63.252", "52.56.34.0", "52.222.9.163", "13.112.63.251", "52.14.64.0",
"52.78.63.252", "46.51.216.14", "13.54.63.252", "35.154.63.252",
"52.67.255.254", "52.60.50.0"]

dicto ={}
minim = None
maxim = None
minhost = None
maxhost= None
region= None

for host in host:
    ping = subprocess.Popen(
    ["ping", "-c", "3", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE)
    out, error = ping.communicate()
    start = out.find('stddev = ') + 9
    end = out.find('ms', start)
    k = [m.start() for m in re.finditer(r"/",out)][3]
    l = [m.start() for m in re.finditer(r"/",out)][4]
    avg = float(out[k+1:l])

    if host == "23.23.255.255":
        region = "us-east-1"
    elif host == "50.18.56.1":
        region = "us-west-1"
    elif host == "34.248.60.213":
        region = "eu-west-1"
    elif host == "35.160.63.253":
        region = "us-west-2"
    elif host == "35.156.63.252":
        region = "eu-central-1"
    elif host == "52.56.34.0":
        region = "eu-west-2"
    elif host == "52.222.9.163":
        region = "us-gov-west-1"
    elif host == "13.112.63.251":
        region = "ap-northeast-1"
    elif host == "52.14.64.0":
        region = "us-east-2"
    elif host == "52.78.63.252":
        region = "ap-northeast-2"
    elif host == "46.51.216.14":
        region = "ap-southeast-1"
    elif host == "13.54.63.252":
        region = "ap-southeast-2"
    elif host == "35.154.63.252":
        region = "ap-south-1"
    elif host == "52.67.255.254":
        region = "sa-east-1"
    elif host == "52.60.50.0":
        region = "ca-central-1"
    else:
        region = "not known"

    host = region + " "+ host

    dicto[host]=avg

sortdicto =sorted(dicto.items(), key=lambda x: x[1])

#sorted_x = sorted(dicto.items(), key=operator.itemgetter(1))

print str(sortdicto[0]) + " Minimum Latency"
print str(sortdicto[1])
print str(sortdicto[2])
print str(sortdicto[3])
print str(sortdicto[4])
print str(sortdicto[5])
print str(sortdicto[6])
print str(sortdicto[7])
print str(sortdicto[8])
print str(sortdicto[9])
print str(sortdicto[10])
print str(sortdicto[11])
print str(sortdicto[12])
print str(sortdicto[13])
print str(sortdicto[14]) + " Maximum Latency"

print 'Maximum: '+str(sortdicto[len(sortdicto)-1][0]) + ' with max latency avg :' +str(sortdicto[len(sortdicto)-1][1])
print 'Minimum: '+str(sortdicto[0][0]) + ' with min latency avg :' +str(sortdicto[0][1])
