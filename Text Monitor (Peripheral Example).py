import mos6502 as master

read = False
output = ""
i = 0

while True:
    master.ExternalControl()
    bus = master.connectBus(False,2000,0)
    if bus==255:
        read = True
    if bus==254:
        print(output)
        break
    
    if read:
        if bus != 255:
            if i % 2 == 0:
                output = output + chr(bus)
    i +=1
