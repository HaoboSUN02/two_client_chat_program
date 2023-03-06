import im
import time
# server = im.IMServerProxy('https://28112-ex1.mkid.top/IMserver.php')
server = im.IMServerProxy('https://web.cs.manchester.ac.uk/x97151hs/comp28112_ex1/IMserver.php')
# state = True
def get_number(message):
    # text = server.__setitem__(key, message)
    x = message.split("||")
    return float(x[0])

def get_text(message):
    x = message.split("||")
    return x[1]


server.clear()



a = input("Press 1 to start a new discussion:"
          "Press 2 to continue a discussion:")
if a == "1":
    # key1 = input("Enter your name:")
    print("Now you're waiting")
    while True:
        getFor2 = server.__getitem__('key2').decode('utf-8').strip()
        server.__setitem__('key1', str("0") + "||" + "")
        if getFor2 != "":
            break
    while True:
        cur_time1 = float(time.time())
        # getFor2 = server.__getitem__('key2').decode('utf-8').strip()
        # getFor1 = server.__getitem__('key1').decode('utf-8').strip()
        gettime2 = get_number(server.__getitem__('key2').decode('utf-8').strip())
        gettime1 = get_number(server.__getitem__('key1').decode('utf-8').strip())
        # pre_time1 = get_number(getFor1)
        getOne = get_text(server.__getitem__('key2').decode('utf-8').strip())
        if gettime2>gettime1:
                print(getOne)
                print("Now you're talking")
                text = input("Enter your message:")
                server.__setitem__('key1', str(cur_time1)+"||"+text)
                print("Now you're waiting")
                if text == "exit":
                    server.clear()
                    break

elif a == "2":
    print("Now you're waiting")
    time1 = float(time.time())
    server.__setitem__('key2', str(time1)+"||"+" ")
    while True:
        cur_time2 = float(time.time())

        # getFor2 = server.__getitem__('key2').decode('utf-8').strip()
        # getFor1 = server.__getitem__('key1').decode('utf-8').strip()
        gettime2 = get_number(server.__getitem__('key2').decode('utf-8').strip())
        gettime1 = get_number(server.__getitem__('key1').decode('utf-8').strip())
        getFor1 = get_text(server.__getitem__('key1').decode('utf-8').strip())
        if gettime1>gettime2:
            print(getFor1)
            print("Now you're talking")
            text = input("Enter your message:")
            server.__setitem__('key2', str(cur_time2)+"||"+text)
            print("Now you're waiting")
            if text == "exit":
                server.clear()
                break
        # else:
        #     print("You're waiting")






