                              # --- Glaciology Data Logger ---
# A complete command-line application to log and analyze geological samples.
# Built by: Shagun
# Concepts Used: Variables, Lists, Dictionaries, Loops, Conditionals, and Functions.

# Main list to hold the data. This is a global variable.

data_log = [
    {
        "sample_id": "HG-01",
        "location": "Siachen Glacier",
        "type": "Ice Core",
        "depth_m": 15,
        "contains_volcanic_ash": True
    },
    {
        "sample_id": "RG-01",
        "location": "Karakoram",
        "type": "Rock",
        "depth_m": 0,  # Surface sample
        "contains_volcanic_ash": False
    }
]

def display_menu():
    """Prints the main menu of options to the user."""
    print("\n--- Glaciology Data Logger ---", flush=True)
    print("[1] Add New Sample", flush=True)
    print("[2] View All Samples", flush=True)
    print("[3] Search by Sample ID", flush=True)
    print("[4] Run Analysis", flush=True)
    print("[5] Exit", flush=True)

def view_samples(log):
    """Loops through and prints all samples currently in the log."""
    print("\n--- Viewing All Samples ---")
    if not log:
        print("Log is empty. Please add a sample first.")
        return
    
    for sample in log:
        print(f"ID: {sample['sample_id']}")
        print(f"Location: {sample['location']}")
        print(f"Type: {sample['type']}")
        print(f"Depth (m): {sample['depth_m']}")
        print(f"Contains Volcanic Ash: {sample['contains_volcanic_ash']}")
        print("-" * 20)

def add_sample(log):
    """Gets input from the user to create and add a new sample to the log."""
    print("\n--- Adding a New Sample ---")

    sample_id = input("Enter Sample ID (e.g., HG-02): ")
    location = input("Enter Location: ")
    sample_type = input("Enter Type (e.g., Ice Core, Rock): ")

    while True:
        depth_str = input("Enter Depth (m): ")
        if depth_str.isdigit():
            depth_m = int(depth_str)
            break
        else:
            print("Invalid input. Please enter a whole number for depth.")

    while True:
        ash_input = input("Contains volcanic ash? (yes/no): ").lower()
        if ash_input in ['yes', 'no']:
            contains_volcanic_ash = (ash_input == 'yes')
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    new_sample = {
        "sample_id": sample_id,
        "location": location,
        "type": sample_type,
        "depth_m": depth_m,
        "contains_volcanic_ash": contains_volcanic_ash
    }
    
    # Correctly appends to the 'log' list that was passed into the function.
    log.append(new_sample)
    print("Sample successfully added.")

def search_by_id(log):
    """Searches the log for a sample with a matching ID."""
    print("\n--- Search for a Sample ---")
    id_to_find = input('Enter required sample id: ')

    found_sample = False
    for sample in log:
        if sample['sample_id'] == id_to_find:
            print("--- Sample Found ---")
            print(f"ID: {sample['sample_id']}")
            print(f"Location: {sample['location']}")
            print(f"Type: {sample['type']}")
            print(f"Depth (m): {sample['depth_m']}")
            print(f"Contains Volcanic Ash: {sample['contains_volcanic_ash']}")
            print("-" * 20)
            found_sample = True
            break
    
    if not found_sample:
        print('Sample not found!')

def run_analysis(log):
    """Calculates and prints summary statistics about the data in the log."""
    print('\n--- Data Analysis Report ---')
    if not log:
        print("No data to analyse!")
        return
    
    # Calculate and print total number of samples
    total_samples = len(log)
    print(f"Total number of samples: {total_samples}")

    # Calculate and print average depth
    total_depth = 0
    for sample in log:
        total_depth += sample['depth_m']
    average_depth = total_depth / total_samples
    print(f"Average Sample Depth: {average_depth:.2f} m")

    # Find and print all samples with volcanic ash
    ash_samples = []
    for sample in log:
        if sample['contains_volcanic_ash']: # This is a shorter way to check for True
            ash_samples.append(sample['sample_id'])
    
    print(f"Samples with volcanic ash: {ash_samples}")

def main():
    """The main function that runs the program's loop."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_sample(data_log)
        elif choice == '2':
            view_samples(data_log)
        elif choice == '3':
            search_by_id(data_log)
        elif choice == '4':
            run_analysis(data_log)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("\n*** Invalid choice, please try again. ***\n")

# This line starts the entire program
main()
