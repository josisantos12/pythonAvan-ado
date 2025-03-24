import threading
def new():
    print('Hello, World!')
thread = threading.Thread(target=new)
thread.start()
thread.join()
print('Goodbye, World!')