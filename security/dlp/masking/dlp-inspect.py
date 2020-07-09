#=================================================================================
# This module inspects the given string and identifies that it is an email type.
# usage: python dlp-inspect.py
# output:
# {'value': 'pk@pktest.com'}
# Quote: pk@pktest.com
# Info type: EMAIL_ADDRESS
# Likelihood: 4
#=================================================================================

def inspect_string_basic(
    project,
    content_string,
    info_types=["PHONE_NUMBER","EMAIL_ADDRESS"],
):
    """Uses the Data Loss Prevention API to analyze strings for protected data.
    Args:
        project: The Google Cloud project id to use as a parent resource.
        content_string: The string to inspect.
        info_types: A list of strings representing info types to look for.
            A full list of info type categories can be fetched from the API.
    Returns:
        None; the response from the API is printed to the terminal.
    """

    # Import the client library.
    import google.cloud.dlp

    # Instantiate a client.
    dlp = google.cloud.dlp_v2.DlpServiceClient()

    # Prepare info_types by converting the list of strings into a list of
    # dictionaries (protos are also accepted).
    info_types = [{"name": info_type} for info_type in info_types]

    # Construct the configuration dictionary.
    inspect_config = {
        "info_types": info_types,
        "include_quote": True,
    }

    # Construct the `item`.
    item = {"value": content_string}

    print(item)
    # Convert the project id into a full resource id.
    parent = dlp.project_path(project)

    # Call the API.
    response = dlp.inspect_content(parent, inspect_config, item)

    # Print out the results.
    if response.result.findings:
        for finding in response.result.findings:
            print("Quote: {}".format(finding.quote))
            print("Info type: {}".format(finding.info_type.name))
            print("Likelihood: {}".format(finding.likelihood))
    else:
        print("No findings.")

project="intense-cortex-278011"
#input_str="(555) 253-0000"
input_str="pk@pktest.com"

# The info types to search for in the content. Required.
#info_types = [{"name": "FIRST_NAME"}]
inspect_string_basic(project, input_str)

