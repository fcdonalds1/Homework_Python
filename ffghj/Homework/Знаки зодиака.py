import time

b = []

while len(b) < 3:
    b.append('a')
    print(b)
    time.sleep(1)
else:
    print('Ready')
