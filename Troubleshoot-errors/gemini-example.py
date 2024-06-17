import vertexai
from vertexai.generative_models import GenerativeModel

# TODO(developer): Update and un-comment below line
project_id = "pkdeltaai-05"

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel(model_name="gemini-1.0-pro-001")

prompt = "Why is the sky blue?"

# Prompt tokens count
response = model.count_tokens(prompt)
print(f"Prompt Token Count: {response.total_tokens}")
print(f"Prompt Character Count: {response.total_billable_characters}")

# Send text to Gemini
response = model.generate_content(prompt)

# Response tokens count
usage_metadata = response.usage_metadata
print(f"Prompt Token Count: {usage_metadata.prompt_token_count}")
print(f"Candidates Token Count: {usage_metadata.candidates_token_count}")
print(f"Total Token Count: {usage_metadata.total_token_count}")
