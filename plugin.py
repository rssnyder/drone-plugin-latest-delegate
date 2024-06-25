from os import getenv
from sys import exit

from requests import get


def write_outputs(outputs: dict[str, str]):
    """
    write key value outputs to a local file to be rendered in the plugin step

    args:
        outputs (dict[str, str]): string to string mappings
    """

    output_file = open(getenv("DRONE_OUTPUT"), "a")

    for k, v in outputs.items():
        output_file.write(f"{k}={v}\n")

    output_file.close()


def check_env(variable: str, default: str = None):
    """
    resolves an environment variable, returning a default if not found
    if no default is given, variable is considered required and must be set
    if not, print the required var and fail the program

    args:
        variable (str): environment variable to resolve
        default (str): default value for variable if not found

    returns:
        str: the value of the variable
    """

    value = getenv(variable, default)
    if not value:
        # if we are missing a PLUGIN_ var, ask the user for the expected setting
        stripped_variable = variable if "PLUGIN_" not in variable else variable[7:]
        print(f"{stripped_variable} required")
        exit(1)

    return value


def main():
    account_id = check_env("HARNESS_ACCOUNT_ID")
    endpoint = check_env("PLUGIN_HARNESS_ENDPOINT", "app.harness.io")
    api_key = check_env("PLUGIN_HARNESS_PLATFORM_API_KEY")

    resp = get(
        f"https://{endpoint}/ng/api/delegate-setup/latest-supported-version",
        params={"accountIdentifier": account_id},
        headers={"x-api-key": api_key},
    )

    resp.raise_for_status()

    data = resp.json()

    write_outputs(data.get("resource", {}))


if __name__ == "__main__":
    main()
