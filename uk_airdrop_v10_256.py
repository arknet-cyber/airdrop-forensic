import hashlib
import concurrent.futures
from tqdm import tqdm

# Function to check if a given string is a valid hexadecimal of specified length
def is_valid_hex(s, length):
    try:
        return len(s) == length and int(s, 16) >= 0
    except ValueError:
        return False

# Function to generate and check hashed phone numbers against target hash fragments
def hash_check(prefix, targetstart, targetend, batch_size=10000):
    matching_numbers = []  # List to store matching phone numbers
    for suffix in range(0, 1000000, batch_size):  # Loop through possible suffixes in batches
        for i in range(suffix, min(suffix + batch_size, 1000000)):
            phone_number = f'{prefix}{i:06d}'  # Generate phone number with prefix and 6-digit suffix
            hashed_number = hashlib.sha256(phone_number.encode()).hexdigest()  # Hash the phone number
            # Check if hash starts and ends with the specified fragments
            if hashed_number.startswith(targetstart) and hashed_number.endswith(targetend):
                matching_numbers.append(phone_number)  # Add matching number to the list
    return matching_numbers

# Main function to orchestrate the hash checking process
def main():
    # Get target hash start and end fragments from user
    targetstart = input('Enter the target hash start fragment: ')
    targetend = input('Enter the target hash end fragment: ')

    # Validate the input hash fragments
    if not (is_valid_hex(targetstart, 5) and is_valid_hex(targetend, 5)):
        print("Invalid hash fragments. Please enter valid hexadecimal strings.")
        return

    # Generate UK mobile phone number prefixes
    uk_mobile_prefixes = [f'07{prefix:03d}' for prefix in range(1000)]

    # Use concurrent processing to check hashes in parallel
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        # Submit tasks to executor for each prefix
        futures = [executor.submit(hash_check, prefix, targetstart, targetend) for prefix in uk_mobile_prefixes]

        matching_numbers = []  # List to store all matching phone numbers
        # Process completed futures and collect results
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(uk_mobile_prefixes), desc="Processing", unit="prefix"):
            matching_numbers.extend(future.result())

    # Print the matching phone numbers if any are found
    if matching_numbers:
        print("Possible matching UK mobile phone numbers:")
        for number in matching_numbers:
            print(number)
    else:
        print('No matching phone number found.')

# Entry point of the script
if __name__ == "__main__":
    print("WARNING: Use this script only for ethical and legal purposes.")
    main()
