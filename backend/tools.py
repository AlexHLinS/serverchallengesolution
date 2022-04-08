import os


def get_param_from_file_environ(default_value, file_name, environ_key):
    try:
        # trying to get info from file
        with open(file_name, 'r') as datafile:
            result = datafile.read()
    except FileNotFoundError:
        try:
            # from environment variables
            result = os.environ[environ_key]
        except KeyError:
            # if all try is fault - using default value
            result = default_value
    return result


def get_file_existing_status(file_name):
    return os.path.exists(file_name)
