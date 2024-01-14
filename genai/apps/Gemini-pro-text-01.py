import streamlit as st

from vertexai.preview.language_models import TextGenerationModel
import os
import streamlit as st
import vertexai
#from PIL import Image
import PIL.Image
import google.ai.generativelanguage as glm


from vertexai.preview.generative_models import (Content,
                                                GenerationConfig,
                                                GenerativeModel,
                                                GenerationResponse,
                                                Image, 
                                                HarmCategory, 
                                                HarmBlockThreshold, 
                                                Part)


#st.markdown("# Projects 🎈")

st.markdown("# Gemini Pro - Text and Vision🎉")

PROJECT_ID="pkdeltaai-02"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

#PROJECT_ID = os.environ.get('GCP_PROJECT') #Your Google Cloud Project ID
#LOCATION = os.environ.get('GCP_REGION')   #Your Google Cloud Project Region
vertexai.init(project=PROJECT_ID, location=LOCATION)

@st.cache_resource
def load_model_gemini_pro():
    text_model_pro = GenerativeModel("gemini-pro")
    return text_model_pro

@st.cache_resource
def load_model_gemini_pro_vision():
    multimodal_model_pro = GenerativeModel("gemini-pro-vision")
    return multimodal_model_pro


def get_gemini_pro_text_response( model: GenerativeModel,
                                  contents: str, 
                                  generation_config: GenerationConfig,
                                  stream=True):
    
    
    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
    
    
    responses = model.generate_content(prompt,
                                       generation_config = generation_config,
                                       safety_settings=safety_settings,
                                       stream=True)

    final_response = []
    for response in responses:
        try:
            # st.write(response.text)
            final_response.append(response.text)
        except IndexError:
            # st.write(response)
            final_response.append("")
            continue
    return " ".join(final_response)


text_model_pro = load_model_gemini_pro()

def get_gemini_response(input):
    generation_config = {'temperature': 0.1,
                        'max_output_tokens': 2048
                        }
    model = GenerativeModel("gemini-pro-vision")

    if (len(input) == 0):
        responses = "Invalid input"
    else:
        responses = model.generate_content(input,generation_config = generation_config,stream=True)
        final_response = []
        for response in responses:
            try:
                final_response.append(response.text)
            except IndexError: 
                pass
    return("".join(final_response))



tab1, tab2 = st.tabs(["QnA","Image Analysis"])

with tab1:
    st.write("Using Gemini Pro - Text model")
    st.subheader("Goal - Generate a response to user query")

    prompt_text = st.text_input("Enter Text: \n\n",key="prompt_text",value="Who is the chancellor of Germany")

    prompt = f"""prompt_text: {prompt_text} \n
        """

    config = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
        }

    generate_t2t = st.button("Generate", key="generate_t2t")
    if generate_t2t and prompt:
        # st.write(prompt)
        with st.spinner("Generating response to your query..."):
            first_tab1, first_tab2 = st.tabs(["Story", "Prompt"])
            with first_tab1: 
                response = get_gemini_pro_text_response(
                    text_model_pro,
                    prompt,
                    generation_config=config,
                )
                if response:
                    st.write("Generated Response:")
                    st.write(response)
            with first_tab2: 
                st.text(prompt)


input_prompt = """
            You are an expert in writing Technical Blogs on Large language models.
            You will receive input images &
            you will have to write a blog on the input image
            """
#input=st.text_input("Inputs for writing Blog: ",key="input")

with tab2:
    st.write("Using Gemini Pro - Vision model")
    st.subheader("Goal: Image Analysis")

    #for pkdeltaai-03 project
    #blog_uri = "gs://bkt-03-invoices/blog-image.png"
    blog_uri = "gs://pk-llm-bucket/blog-image.png"
    blog_url = "https://storage.googleapis.com/"+blog_uri.split("gs://")[1]

    blog_img = Part.from_uri(blog_uri, mime_type="image/jpeg")
    st.image(blog_url,width=600, caption="Image input for writing a Blog")
  
    generate = st.button("Generate!")

    if generate: 
        with st.spinner("Generating Image analysis using Gemini..."):
            response=get_gemini_response([input_prompt,blog_img])
            st.markdown(response)
            st.markdown("\n\n\n")
