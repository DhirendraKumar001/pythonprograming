import time
def countdown (t):
    while t <0:
        print(t)
        t=1
        time.sleep(1)
    print("blast off")

print ("How many seconds count down? Enter a integer:")
seconds=input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter a integer:")
    seconds = input()
seconds=int(seconds)
countdown(seconds)




