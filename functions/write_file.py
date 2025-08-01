import os



def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            print(f'parent directory for "{target_file}" created')
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target_file) and os.path.isdir(target_file):
        return f'Error: "{file_path}" is a directory, not a file'  


   
    try:
        with open(target_file, "w") as z:
            z.write(content)
            print(f'Successfully created and wrote to "{file_path}" ({len(content)} characters written)')
            return f'Successfully created and wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f'Error: could not create and write to "{file_path}')
        return f'Error: could not create and write to "{file_path}'
    
        

