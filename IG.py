import streamlit as st
from altair import Chart
from PIL import Image
from requests import post
from io import BytesIO


def Imagegeneration(input3):
    
    b = post (
    "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
    headers = {
    'Authorization': 'Bearer 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'
    },

    json = {
        "inputs" : input3
    }

)

    i = Image.open(BytesIO(b.content))
    # i.save("guru.png")
    return i


def main():
    input3 = st.text_input("Enter the prompt to generate")
    st.write("Sample Image")
    output3 = Imagegeneration(input3)
    st.write("You can dowmload the Image..")
    st.image(output3)


if __name__ == "__main__":
    main()