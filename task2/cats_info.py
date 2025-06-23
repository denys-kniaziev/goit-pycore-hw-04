def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Read information about cats from a file and return a list of dictionaries.
    
    Args:
        path (str): Path to the text file containing cat data.
        
    Returns:
        list: A list of dictionaries, where each dictionary contains information 
              about one cat with keys "id", "name", and "age".
        
    The function reads a file where each line contains a cat's ID, name, and age
    separated by commas (e.g., "60b90c1c13067a15887e1ae1,Tayson,3").
    
    Example:
        cats_info = get_cats_info("cats_file.txt")
        print(cats_info)
    """
    cats_list = []
    
    try:
        # Open the file with proper encoding
        with open(path, 'r', encoding='utf-8') as file:
            # Process each line in the file
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                    
                # Split the line by comma and extract cat information
                try:
                    cat_id, name, age = line.strip().split(',')
                    
                    # Create a dictionary for the current cat
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    
                    # Add the cat dictionary to the list
                    cats_list.append(cat_dict)
                except ValueError:
                    # Skip lines with incorrect format
                    continue
        
        return cats_list
    
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []
    except Exception as e:
        print(f"Error processing file: {e}")
        return []


# Example usage
if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
