## XOR Encryption

The XOR encryption is used in general for masking data payloads. This script generates a random text key and processes it for a later XOR encryption. This is widely used in corporate or private networks that use traffic encryption.

Traffic encryption is a mechanism to prevent traffic sniffers or IP sensors. It can work in two modes.

1. The signature mode, which inspects the packet parameters and data payloads passed through the sensors, is pretty much similar to an antivirus; it checks for matches at a signature database.

2. The behavior-based (anomalies) is used for studying IPS and the network itself. The IPS will learn the protocol types and packet rates passing through the sensor, the records can be stored in a database, and can also detect false positives based on the average traffic expected and recorded.

## Why XOR

Here are three simple reasons for it.

1. Enterprise networks with decryption devices that can terminate and clear your attempt through IP sensors
2. You will have E2E shell faces; if the shell faces the IPS server, it won't have any added value.
3. Modern firewalls can terminate SSH or SSL encryption for inspection purposes

### How it works

In a few words, the script will generate a random key used for the encryption with a 1kb length.

The XOR encryption message should be greater than the length of the message. (check the key length and the `ipconfig` value inside the `message` variable).

The encryption function will split the message and the XOR key in a tuple format. Each tuple is converted into an integer value with the help of the `ord` built-in function.

After this, it performs `exclusive XOR` on them, it will merge the result on `ASCII` for a later `join`.

### Run

Just: `python xor.py`

## Credits
[David Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
