import sys
import socket

if len(sys.argv) != 2:
    print("Usage: python receiver.py <output_file>")
    sys.exit(1)

output_file = sys.argv[1]
address = "dbl44.beuth-hochschule.de"
port = 44444

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    print("Connected to server!")
    
    # Receive message via dslp1.2
    data = s.recv(1024)
    
    with open(output_file, 'w') as f:
        f.write(bytes.decode(data))
        print(f"Received data saved to {output_file}")
        
except Exception as e:
    print(f"Connection error: {e}")
    sys.exit(1)
finally:
    s.close()
