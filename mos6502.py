# MOS 6502 Emulator by Krzysiek127
#

import os,time

if __name__ == '__main__':
    clock = float(input("Clock Speed? "))
    os.system('cls')
else:
    clock = 0
RAM = []

running = True
RamMonShow = True
showMon = ""
if __name__ == '__main__':
    RamShowMin = int(input("Min. Ram monitor? "),base=16)
    RamShowMax = int(input("Max. Ram monitor? "),base=16)
    os.system('cls')

if __name__ == '__main__':
    if RamShowMin==0 and RamShowMax == 0:
        RamMonShow = False

def ForceInsert(list, index, value):
    list.insert(index,value)
    list.pop(index+1)

memory_size = 65535  # In kilobytes.
start_adress = 1024  # Decimal

for i in range(0, memory_size):
    RAM.append(0)

#with open("Program.txt") as f: # Old Program Loading Routine
#    content = f.readlines()
#content = [x.strip() for x in content]
#entries = len(content)

with open(input("Program Filename? ")) as f:  #  New Program Loading Routine
    content = f.read().split()
entries = len(content)

print("RAM size: ", len(RAM))
print("Program size: ", entries)

print("Loading program into RAM...")
for i in range(0,entries):
    write_adr = start_adress + i
    ForceInsert(RAM,write_adr,int(content[i],base=16))
print("Done!")

print("")
cycle = start_adress
X = 0
Y = 0
A = 0

def connectBus(RW,adr,val):
    if RW:  #  Writing
        RAM[adr] = val
    else:  #  Reading
        return RAM[adr]

def ebrc():  #  Check if registers are 8 bit
    global X,Y,A
    if X==256:
        X = 0
    if Y==256:
        Y = 0
    if A==256:
        A = 0

def FetchExecute(ex):
    global RAM,running,X,Y,A,cycle

    if ex==0:  #  BRK
        running = False
        print("BRK")

    elif ex==169:  #  LDA Immediate
        A = RAM[cycle+1]
        cycle +=1
    elif ex==165:  #  LDA Zero Page
        A = RAM[RAM[Cycle+1]]
        cycle += 1
    elif ex==181:  # LDA Zero Page,X
        A = RAM[RAM[Cycle+1+X]]
        cycle += 1
    elif ex==173:  # LDA Absolute
        ls = format(RAM[cycle + 2], 'x')
        ms = format(RAM[cycle + 1], 'x')
        AbsoluteVal = int(str(ls) + str(ms), base=16)
        A = RAM[AbsoluteVal]
        cycle += 2
    elif ex==189:  # LDA Absolute,X
        ls = format(RAM[cycle + 2], 'x')
        ms = format(RAM[cycle + 1], 'x')
        AbsoluteVal = int(str(ls) + str(ms), base=16)
        A = RAM[AbsoluteVal+X]
        cycle += 2
    elif ex==185:  # LDA Absolute,Y
        ls = format(RAM[cycle + 2], 'x')
        ms = format(RAM[cycle + 1], 'x')
        AbsoluteVal = int(str(ls) + str(ms), base=16)
        A = RAM[AbsoluteVal+Y]
        cycle += 2
    elif ex==161:  # LDA Indirect,X
        print("Indirect not supported.")
        cycle += 1
    elif ex==177:  # LDA Indirect,Y
        print("Indirect not supported.")
        cycle += 1

    elif ex==133:  #  STA Zero Page
        RAM[RAM[Cycle+1]] = A
        cycle += 1
    elif ex==149:  # STA Zero Page,X
        RAM[RAM[Cycle+1+X]] = A
        cycle += 1
    elif ex==141:  # STA Absolute
        ls = str(format(RAM[cycle + 2], 'x'))
        ms = str(format(RAM[cycle + 1], 'x'))
        if int(ls,base=16) < 16:
            ls = "0" + ls
        if int(ms,base=16) < 16:
            ms = "0" + ms
        AbsoluteVal = int(ls + ms, base=16)
        RAM[AbsoluteVal] = A
        cycle += 2
    elif ex==157:  # STA Absolute,X
        ls = str(format(RAM[cycle + 2], 'x'))
        ms = str(format(RAM[cycle + 1], 'x'))
        if int(ls, base=16) < 16:
            ls = "0" + ls
        if int(ms, base=16) < 16:
            ms = "0" + ms
        AbsoluteVal = int(ls + ms, base=16)
        RAM[AbsoluteVal + X] = A
        cycle += 2
    elif ex==153:  # STA Absolute,Y
        ls = str(format(RAM[cycle + 2], 'x'))
        ms = str(format(RAM[cycle + 1], 'x'))
        if int(ls, base=16) < 16:
            ls = "0" + ls
        if int(ms, base=16) < 16:
            ms = "0" + ms
        AbsoluteVal = int(ls + ms, base=16)
        RAM[AbsoluteVal + Y] = A
        cycle += 2
    elif ex==161:  # STA Indirect,X
        print("Indirect not supported.")
        cycle += 1
    elif ex==177:  # STA Indirect,Y
        print("Indirect not supported.")
        cycle += 1

    elif ex==232:  #  INX
        X +=1
    elif ex==200:  #  INY
        Y +=1

    elif ex==76:  # JMP Absolute
        ls = str(format(RAM[cycle + 2], 'x'))
        ms = str(format(RAM[cycle + 1], 'x'))
        if int(ls, base=16) < 16:
            ls = "0" + ls
        if int(ms, base=16) < 16:
            ms = "0" + ms
        AbsoluteVal = int(ls + ms, base=16)
        cycle = AbsoluteVal-1

    elif ex==230:  # INC Zeropage
        RAM[RAM[cycle + 1]] +=1
        if RAM[RAM[cycle + 1]]==256:
            RAM[RAM[cycle + 1]] = 0
        cycle += 1
    elif ex==246:  # INC Zeropage,X
        RAM[RAM[cycle + 1 + X]] +=1
        if RAM[RAM[cycle + 1]]==256:
            RAM[RAM[cycle + 1]] = 0
        cycle += 1
    elif ex==238:  # INC Absolute
        ls = format(RAM[cycle + 2], 'x')
        ms = format(RAM[cycle + 1], 'x')
        AbsoluteVal = int(str(ls) + str(ms), base=16)
        RAM[AbsoluteVal] +=1
        if RAM[AbsoluteVal]==256:
            RAM[AbsoluteVal] = 0
        cycle += 2
    elif ex==254:  # INC Absolute,X
        ls = format(RAM[cycle + 2], 'x')
        ms = format(RAM[cycle + 1], 'x')
        AbsoluteVal = int(str(ls) + str(ms), base=16)
        RAM[AbsoluteVal+X] +=1
        if RAM[AbsoluteVal+X]==256:
            RAM[AbsoluteVal+X] = 0
        cycle += 2
    #else:
        #print(ex)
    # TODO: Uzupełnij opcody
while __name__ == '__main__' and running:
    time.sleep(clock)
    Exec = RAM[cycle]
    print("RAM cycle: ",cycle," Executing: ", hex(Exec))
    print("X=",X," Y=",Y," A=",A,"PC=",cycle)
    print("")
    if RamMonShow:
        for i in range(RamShowMin,RamShowMax):
            showMon = showMon + str(RAM[i]) + " "
        print(showMon)
        showMon = ""
    ebrc()
    FetchExecute(Exec)
    cycle +=1

def ExternalControl():  #  This is NOT irq.
    global clock,cycle,RAM
    time.sleep(clock)
    Exec = RAM[cycle]
    ebrc()
    FetchExecute(Exec)
    cycle +=1

if __name__ == '__main__':
    os.system("pause")