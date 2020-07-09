# =========================================================================================
# Reference url: 
# https://cloud.google.com/dlp/docs/pseudonymization#dlp-deid-text-fpe-python
# In this module, we have a deidentified phone number with us: 9617256398.  This is passed to the reidentify module.
# The reidentify step takes the phone number and does a reverse tokenization using FPE format preserving encryption 
# The output phone number returned is: 435991673
# usage: python reid-fpe.py
# output:
# Passing deidentified string: 9617256398
# phone number is 4359916732
# reid completed!
# =========================================================================================


def reidentify_free_text_with_fpe_using_surrogate(
    project,
    input_str,
    alphabet="NUMERIC",
    surrogate_type="PHONE_TOKEN",
    unwrapped_key="YWJjZGVmZ2hpamtsbW5vcA==",
):
    """Uses the Data Loss Prevention API to reidentify sensitive data in a
    string that was encrypted by Format Preserving Encryption (FPE) with
    surrogate type. The encryption is performed with an unwrapped key.
    Args:
        project: The Google Cloud project id to use as a parent resource.
        input_str: The string to deidentify (will be treated as text).
        alphabet: The set of characters to replace sensitive ones with. For
            more information, see https://cloud.google.com/dlp/docs/reference/
            rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        surrogate_type: The name of the surrogate custom info type to used
            during the encryption process.
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

    # Construct Deidentify Config
    transformation = {
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

    reidentify_config = {
        "info_type_transformations": {
            "transformations": [transformation]
        }
    }

    inspect_config = {
        "custom_info_types": [
            {"info_type": {"name": surrogate_type}, "surrogate_type": {}}        ]
    }

    # Convert string to item
    item = {"value": input_str}

    # Call the API
    response = dlp.reidentify_content(
        parent,
        inspect_config=inspect_config,
        reidentify_config=reidentify_config,
        item=item,
    )

    # Print results
    print(response.item.value)

project="intense-cortex-278011"
input_str="phone number is PHONE_TOKEN(10):9617256398"
print("Passing deidentified string: 9617256398")
reidentify_free_text_with_fpe_using_surrogate(project, input_str)
print("reid completed!")


