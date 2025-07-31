import os



# def get_files_info(working_directory, directory="."):
    
    
#     abs_path_working = os.path.abspath(working_directory)
#     my_path = (os.path.abspath(os.path.join(working_directory, directory))) + "/"

    
    
#     print(my_path)
#     # print(abs_path_working)
#     if my_path.startswith(abs_path_working) == False:
#          print("Error: Cannot list '{directory}' as it is outside the permitted working directory")
#          return f'Error: Cannot list "{directory}" as it is outside the permitted working directory"'
#     if os.path.isdir(my_path) == False:
#         print(f'Error: "{my_path}" is not a directory')
#         return f'Error: "{directory}" is not a directory'
#     if directory == ".":
#         print("result for current directory:")
#     else:
#         print(f"Result for '{directory}' directory:")

#     dir_list = os.listdir(path=my_path)
    
#     for i in dir_list:
#           print(f"- {i}: file_size={os.path.getsize(my_path + i)} bytes, is_dir={os.path.isdir(os.path.abspath(my_path + i))}")

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

        
    





