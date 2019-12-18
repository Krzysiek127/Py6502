MOS 6502 Emulator written by Krzysiek127
Version Early Alpha 1.0

## USING EMULATOR IN NON PERIPHERAL MODE ##
Just compile the mnemonics to object code (for example using www.masswerk.at/6502/assembler.html) and save it to Program.txt

## WRITING AND USING PERIPHERALS ##
To retrieve information from bus you can use function 'connectBus(adr)' where adr is the memory adress
In the main loop of your peripheral there must be 'ExternalControl()'
For more info look at the 'Text Monitor Example'

Explanation of 'Text Monitor Example'
Program of this example is simple. It loads an ASCII value to accumulator and stores it in memory adress 07d0 (2000) where it's read by connectBus and being outputed at the end of execution.

