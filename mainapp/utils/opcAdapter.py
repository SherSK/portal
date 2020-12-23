import OpenOPC,time

try:
    stTime=time.time()
    opc=OpenOPC.client()
    opc.connect('Lectus.OPC.1') 
    lst=opc.read(opc.list('*Item*',flat=True),update=1,group='value',include_error=True)
    for item in lst:
        print(f"{item[0]}:{item[1]} quality {item[2]}")
    endTime=time.time()
    print(f"Duration time {endTime-stTime} second")

finally:
    opc.remove('value')
    opc.close()