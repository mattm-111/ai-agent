import os
import sys
from functions.configs import MAX_CHARS




def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, 'r') as file:
            text = file.read().strip().split()
            len_chars = sum(len(word) for word in text)
        with open(target_file, "r") as x:
            if len_chars > 10000:
                file_read = x.read(MAX_CHARS) + f'...File "{file_path}" truncated at 10000 characters'
            else:    
                file_read = x.read(MAX_CHARS)
                print(file_read)
        return file_read
    
    except Exception as e:
        print(f"Error reading files: {e}")
        return f"Error reading files: {e}"
        

    

    


