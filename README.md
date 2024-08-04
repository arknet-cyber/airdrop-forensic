# UK Mobile Phone Number Hash Checker

This Python script checks UK mobile phone numbers to find those whose SHA-256 hash starts and ends with user-specified hexadecimal fragments. The script leverages multiprocessing to speed up the process by checking multiple prefixes in parallel.

## Features

- Validates user input for correct hexadecimal format.
- Generates UK mobile phone number prefixes.
- Uses concurrent processing for efficient hash checking.
- Displays possible matching UK mobile phone numbers.

## Prerequisites

- Python 3.x
- Required Python libraries: `hashlib`, `concurrent.futures`, `tqdm`

## Installation

1. Clone the repository:
    ```sh
    gh repo clone arknet-cyber/airdrop-forensic
    cd airdrop-forensic
    ```

2. Install the required Python libraries:
    ```sh
    pip install tqdm
    ```

## Usage

1. Run the script:
    ```sh
    python uk_airdrop_v10_256.py
    ```

2. Enter the target hash start and end fragments when prompted:
    ```
    Enter the target hash start fragment: (e.g., 'abcde')
    Enter the target hash end fragment: (e.g., '12345')
    ```

3. The script will process the UK mobile phone number prefixes and display possible matching numbers.

## Example

```
WARNING: Use this script only for ethical and legal purposes.
Enter the target hash start fragment: abcde
Enter the target hash end fragment: 12345
Processing: 100%|████████████████████████████████████████████████████████████| 1000/1000 [02:15<00:00,  7.37prefix/s]
Possible matching UK mobile phone numbers:
071234567890
071234567891
```

## Warning

**This script should only be used for ethical and legal purposes. Unauthorized use of this script for malicious activities is strictly prohibited.**

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please contact [sec@arknet.uk](mailto:sec@arknet.uk).

---

