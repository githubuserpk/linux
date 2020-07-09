# =========================================================================================
# Reference url: 
# https://cloud.google.com/dlp/docs/pseudonymization#dlp-deid-text-fpe-python
# In this module, we have a original phone number 435991673.  This is passed to the deidentify module.
# The deidentify step takes the phone number and does a tokenization using FPE format preserving encryption 
# The output phone number returned is: 9617256398
# usage: python deid-fpe.py
# output:
# Before deidentify, ie original phone no: 435991673
# My phone number is PHONE_TOKEN(10):9617256398
# deid completed!
# =========================================================================================

def deidentify_free_text_with_fpe_using_surrogate(
    project,
    input_str,
    alphabet="NUMERIC",
    info_type="PHONE_NUMBER",
    surrogate_type="PHONE_TOKEN",
    unwrapped_key="YWJjZGVmZ2hpamtsbW5vcA==",
):
    """Uses the Data Loss Prevention API to deidentify sensitive data in a
       string using Format Preserving Encryption (FPE).
       The encryption is performed with an unwrapped key.
    Args:
        project: The Google Cloud project id to use as a parent resource.
        input_str: The string to deidentify (will be treated as text).
        alphabet: The set of characters to replace sensitive ones with. For
            more information, see https://cloud.google.com/dlp/docs/reference/
            rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        info_type: The name of the info type to de-identify
        surrogate_type: The name of the surrogate custom info type to use. Can
            be essentially any arbitrary string, as long as it doesn't appear
            in your dataset otherwise.
        unwrapped_key: The base64-encoded AES-256 key to use.
    Returns:
        None; the response from the API is printed to the terminal.
    """
    # Import the client library
    import google.cloud.dlp

    # Instantiate a client
    dlp = google.cloud.dlp_v2.DlpServiceClient()

    # Convert the project id into a full resource id.
    parent = dlp.project_path(project)

    # The unwrapped key is base64-encoded, but the library expects a binary
    # string, so decode it here.
    import base64

    unwrapped_key = base64.b64decode(unwrapped_key)

    # Construct de-identify config
    transformation = {
        "info_types": [{"name": info_type}],
        "primitive_transformation": {
            "crypto_replace_ffx_fpe_config": {
                "crypto_key": {
                    "unwrapped": {"key": unwrapped_key}
                },
                "common_alphabet": alphabet,
                "surrogate_info_type": {"name": surrogate_type},
            }
        }
    }

    deidentify_config = {
        "info_type_transformations": {
            "transformations": [transformation]
        }
    }

    # Construct the inspect config, trying to finding all PII with likelihood
    # higher than UNLIKELY
    inspect_config = {
        "info_types": [{"name": info_type}],
        "min_likelihood": "UNLIKELY"
    }

    # Convert string to item
    item = {"value": input_str}

    # Call the API
    response = dlp.deidentify_content(
        parent,
        inspect_config=inspect_config,
        deidentify_config=deidentify_config,
        item=item,
    )

    # Print results
    print(response.item.value)

project="intense-cortex-278011"
input_str="My phone number is 4359916732"
print("Before deidentify, ie original phone no: 435991673")
deidentify_free_text_with_fpe_using_surrogate(project, input_str)
print("deid completed!")
