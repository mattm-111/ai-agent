import os
import subprocess




def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        print(f'Error: File "{file_path}" not found.')
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        print(f'Error: "{file_path}" is not a Python file.')
        return f'Error: "{file_path}" is not a Python file.'
    

    try:
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(
            command, cwd=abs_working_dir, timeout=30, capture_output=True, check=True, text=True
            )
        
        execution = []

        if result.stdout:
            execution.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            execution.append(f"STDERR:\n{result.stderr}")
        # if result.returncode != 0:
        #     execution.append(f'process exited with code {result.returncode}')

        if execution:
            return "\n".join(execution)
        
        else:
            print("No output produced.")
            return "No output produced."


    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Called Process Error caught Stderr: {e.stderr}")
        print(f'Process exited with code {e.returncode}')
    except Exception as e:
        print(f'Error: executing Python file: {e}')





    
    

