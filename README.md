# IoT-Secure-Voting-System

## The idea
In view of the need to create a secure voting system already presented in the SecureVoting project, i thought of implementing an IoT device that could guarantee secure voting.

## The implementation
This is implemented via an esp32 consisting of four buttons, each of which allows a candidate to be voted for. The authentication that enables voting is implemented by an RFID chip that checks and assigns accounts on the blockchain.

### Hardware used
- Esp32
- RFID-RC522

### Software used
On Flask: 
- Json
- Web3
- SSLify

on ESP32:
- WiFi
- WiFiClientSecure
- HTTPClient
- SPI
- MFRC522

## Author

- [@Givaa](https://github.com/Givaa)