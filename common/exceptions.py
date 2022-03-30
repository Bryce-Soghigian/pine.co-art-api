
class BucketDoesNotExist(Exception):
    """
    Bucket you tried to access does not exist. What else could this message mean bruh.
    """


class EnvConfigurationError(Exception):
    """
    You tried to access environment variables that do not exist. 
    """