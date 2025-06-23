import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def display_directory_structure(directory_path: str, indent=""):
    """
    Recursively display the structure of a directory with colored output.
    
    Args:
        directory_path (Path): Path object pointing to the directory.
        indent (str): Indentation string for nested directories.
    """
    # Check if the path exists and is a directory
    path = Path(directory_path)
    if not path.exists():
        print(f"Error: Path '{directory_path}' does not exist.")
        return
    if not path.is_dir():
        print(f"Error: '{directory_path}' is not a directory.")
        return
    
    # Display the root directory name
    if indent == "":
        print(f"{Fore.BLUE}{Style.BRIGHT}{path.name}/")
    
    # Sort items to show directories first, then files
    items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    
    # Count items to determine when to use different branch characters
    items_list = list(items)
    items_count = len(items_list)
    
    for i, item in enumerate(items_list):
        is_last = i == items_count - 1
        branch = "└── " if is_last else "├── "
        
        # Display the item with proper indentation and color
        if item.is_dir():
            print(f"{indent}{branch}{Fore.BLUE}{Style.BRIGHT}{item.name}/")
            
            # Recursively display the contents of the subdirectory
            next_indent = indent + ("    " if is_last else "│   ")
            display_directory_structure(item, next_indent)
        else:
            print(f"{indent}{branch}{Fore.GREEN}{item.name}")

def main() -> None:
    """Main function to handle command-line arguments and start directory visualization."""
    # Check if a directory path was provided
    if len(sys.argv) != 2:
        print("Usage: python directory_visualizer.py <directory_path>")
        return
    
    # Get the directory path from command-line argument
    directory_path = sys.argv[1]
    
    # Display the directory structure
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()
