import argparse

def main():
    parser = argparse.ArgumentParser(description="Job Application Tracker")
    parser.add_argument("action", choices=["add", "update", "list"], help="Action to perform")
    parser.add_argument("--file", help="Path to the job description text file")
    
    args = parser.parse_args()
    
    if args.action == "add":
        print(f"Parsing job description from {args.file}...")
        # TODO: Add extraction logic here
    elif args.action == "list":
        print("Listing all job applications...")

if __name__ == "__main__":
    main()