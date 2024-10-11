import os


def resource_path(file_name):
    return os.path.abspath(os.path.dirname(os.path.join(os.getcwd())) + f'//HW9//{file_name}')
