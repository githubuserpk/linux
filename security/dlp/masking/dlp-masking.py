# =================================================================================================
# In this module deidentify with mask is done.
# usage: python dlp-masking.py 
# The input string has this value: (555) 253-0000
# It will be masked with * ie star value 
# output: **************
# =================================================================================================

def deidentify_with_mask(
    project, input_str, info_types, masking_character=None, number_to_mask=0
):
    """Uses the Data Loss Prevention API to deidentify sensitive data in a
    string by masking it with a character.
    Args:
        project: The Google Cloud project id to use as a parent resource.
        input_str: The string to deidentify (will be treated as text).
        masking_character: The character to mask matching sensitive data with.
        number_to_mask: The maximum number of sensitive characters to mask in
            a match. If omitted or set to zero, the API will default to no
            maximum.
    Returns:
        None; the response from the API is printed to the terminal.
    """

    # Import the client library
    import google.cloud.dlp

    # Instantiate a client
    dlp = google.cloud.dlp_v2.DlpServiceClient()

    # Convert the project id into a full resource id.
    parent = dlp.project_path(project)

    # Construct inspect configuration dictionary
    inspect_config = {
        "info_types": [{"name": info_type} for info_type in info_types]
    }

    # Construct deidentify configuration dictionary
    deidentify_config = {
        "info_type_transformations": {
            "transformations": [
                {
                    "primitive_transformation": {
                        "character_mask_config": {
                            "masking_character": masking_character,
                            "number_to_mask": number_to_mask,
                        }
                    }
                }
            ]
        }
    }

    # Construct item
    item = {"value": input_str}

    # Call the API
    response = dlp.deidentify_content(
        parent,
        inspect_config=inspect_config,
        deidentify_config=deidentify_config,
        item=item,
    )

    # Print out the results.
    print(response.item.value)

project="intense-cortex-278011"
#input_str="pk@pk.com"
input_str="(555) 253-0000"
info_types=["PHONE_NUMBER","EMAIL_ADDRESS"]

# The info types to search for in the content. Required.
#info_types = [{"name": "FIRST_NAME"}]
deidentify_with_mask(project, input_str, info_types)


