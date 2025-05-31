import sys
import socket
import base64
import os

def send_message(s, filename, message):
    """Send message using DSLP protocol"""
    s.send(b"dslp/1.2\r\n")
    s.send(b"peer notify\r\n")
    s.send(str.encode(filename + "\r\n"))
    s.send(message + b"\r\n")
    s.send(b"dslp/end\r\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sender.py <output_filename> <file_to_send>")
        sys.exit(1)

    address = "dbl44.beuth-hochschule.de"
    port = 44444
    output_filename = sys.argv[1]
    file_path = sys.argv[2]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((address, port))
            print("Connected to server!")
            
            with open(file_path, 'rb') as f:
                file_data = f.read()
                file_encoded = base64.encodebytes(file_data)
            
            send_message(s, output_filename, file_encoded)
            print("File sent successfully!")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
