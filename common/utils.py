import typing
import os

from common.exceptions import EnvConfigurationError
def is_mod_of_x(quotient, x):
    return quotient % x == 0



def verify_env_vars(variable_keys: typing.List[str]):
    """
    Helper function used for verifying that all the environment variables we use in a function exist within our env.
    """
    for variable_key in variable_keys:
        variable = os.environ[variable_key]
        if variable == "" or variable == None:
            raise EnvConfigurationError