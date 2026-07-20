import serial
import random

s = serial.Serial("COM11")
s.baudrate=9600
ending_char = '\r\n'

s_out = ""

while 1:
    if s.in_waiting > 0:
        res = s.read(s.in_waiting).decode()
        s_out += res

        print(res, end='')

        if s_out.endswith(ending_char):
            s_out = s_out.removesuffix(ending_char).strip().upper()
            
            print("read serial command: %s, char count %d" % (s_out, len(s_out)))

            # Read command
            if s_out == "SIR":
                prefix = "S S "
                suffix = " kg\r\n"
                weight = round(random.uniform(0, 100), 2)
                out = prefix + "%.2f" % weight + suffix
                s.write(out.encode())
                print("serial response: %s" % out)

            # Tare command
            elif s_out == "T":
                out = "Done\r\n"
                s.write(out.encode())
                print("serial response: %s" % out)

            s_out = ""