import os




def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{target_file}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{target_file}" is not a file'