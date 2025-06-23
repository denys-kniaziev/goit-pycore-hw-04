def total_salary(path: str) -> tuple[float, float]:
    """
    Calculate the total and average salary from a text file.
    
    Args:
        path (str): Path to the text file containing salary data.
        
    Returns:
        tuple[float, float]: A tuple containing the total salary sum and average salary.
        
    The function reads a file where each line contains a developer's name and salary
    separated by a comma (e.g., "John Doe,5000").
    
    Example:
        total, average = total_salary("salary_file.txt")
        print(f"Total salary: {total}, Average salary: {average}")
    """
    try:
        total_sum = 0
        count = 0
        
        # Open the file with proper encoding
        with open(path, 'r', encoding='utf-8') as file:
            # Process each line in the file
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                    
                # Split the line by comma and extract the salary
                try:
                    _, salary = line.strip().split(',')
                    salary = float(salary)
                    total_sum += salary
                    count += 1
                except ValueError:
                    # Skip lines with incorrect format
                    continue
        
        # Calculate the average salary
        average = total_sum / count if count > 0 else 0
        
        return (total_sum, average)
    
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return (0, 0)
    except Exception as e:
        print(f"Error processing file: {e}")
        return (0, 0)


# Example usage
if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Total salary: {total}, Average salary: {average}")
