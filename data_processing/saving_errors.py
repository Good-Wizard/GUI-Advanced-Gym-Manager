from data_processing.modules import getcwd, join

def save_error(error):
    project_path = getcwd()  # Get the current working directory of the project
    error_file_path = join(project_path, "Errors.log")
    with open(error_file_path, "a+") as f:
        f.write(f"{error}\n")