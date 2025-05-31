# Socket Client Project

This project contains Python scripts for sending and receiving files over a socket connection using the DSLP protocol.

## Prerequisites
- Python 3.x
- No additional libraries required (uses standard libraries)

## Usage

### Sender Script
Sends a file to the server:
```
python sender.py <output_filename> <file_to_send>
```
Example:
```
python sender.py received_file.txt document.pdf
```

### Receiver Script
Receives a file from the server and saves it locally:
```
python receiver.py <output_file>
```
Example:
```
python receiver.py received_data.txt
```

## Server Information
The server for this project is located in a separate repository:  
https://github.com/C3MO/Socket_Server

## Project Structure
- `sender.py` - File sending client
- `receiver.py` - File receiving client

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.