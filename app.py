import streamlit as st
from bria_api.text_to_image import generate_image
from bria_api.product_cutout import product_cutout
from bria_api.resolution import increase_resolution
from bria_api.packshot import generate_packshot
from bria_api.shadow import add_shadow
from bria_api.lifestyle import generate_lifestyle
from utils import icon

st.set_page_config(page_title="Product Snap", layout="wide", initial_sidebar_state="auto", page_icon=":camera:")

st.markdown("<br />", unsafe_allow_html=True)
icon.show_icon(":lipstick:")
st.markdown("""<h1>Product Snap <span style="margin: 0; color: gray; font-size: 20px;"> ✧  Smart Product Creator</span></h1> """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    body {
        background-color: #f5f6f8;
    }
    .block-container {
        padding-top: 2rem;
    }
    .stButton button {
        background-color: #1f2937;
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    .stButton button:hover {
        background-color: #111827;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Product Snap Workflow")
steps = [
    "Generate Image",
    "Cutout",
    "Enhance Resolution",
    "Packshot",
    "Add Shadow",
    "Lifestyle Shot"
]
choice = st.sidebar.radio("Select Step", steps)

st.session_state.setdefault("image_url", None)
st.session_state.setdefault("cutout_url", None)
st.session_state.setdefault("res_url", None)
st.session_state.setdefault("packshot_url", None)
st.session_state.setdefault("shadow_url", None)

sku = "sku001"

if choice == steps[0]:
    st.subheader("🎨  Generate Product Image")
    
    with st.form(key="photo_gen_form"):
        col1, col2, col3 = st.columns([2, 1, 1])

        prompt = col1.text_input(
            "Describe your product",
            "A ceramic mug on a wooden table",
            key="prompt_input"
        )

        aspect_ratio = col2.selectbox(
            "Aspect Ratio",
            options=[
                "1:1", "2:3", "3:2", "3:4", "4:3", 
                "4:5", "5:4", "9:16", "16:9"
            ],
            index=0,
            key="aspect_ratio"
        )

        seed = col3.slider(
            "Seed (randomness)",
            min_value=0,
            max_value=999999,
            value=0,
            help="Set to 0 for random results. Use a fixed number for repeatability.",
            key="seed"
        )

        steps_num = col3.slider(
            "Refinement Steps",
            min_value=20,
            max_value=50,
            value=30,
            help="Higher means more refined image (slower).",
            key="steps_num"
        )

        submit = st.form_submit_button("🖌️ Generate Product Image")

        if submit:
            st.session_state.image_url = generate_image(
                prompt=prompt,
                aspect_ratio=aspect_ratio,
                seed=seed,
                steps_num=steps_num
            )
            if st.session_state.image_url:
                st.image(st.session_state.image_url, caption="Generated Image", use_column_width=True)

elif choice == steps[1]:
    st.subheader("✂️ Cutout Product")
    if st.session_state.image_url:
        st.image(st.session_state.image_url, caption="Original Image", use_column_width=True, width=700)
        if st.button("Cutout Product"):
            st.session_state.cutout_url = product_cutout(st.session_state.image_url)
            if st.session_state.cutout_url:
                st.image(st.session_state.cutout_url, caption="Cutout Image", use_column_width=True)
    else:
        st.warning("Please generate an image first.")

elif choice == steps[2]:
    st.subheader("🔍 Enhance Image Resolution")
    st.image(st.session_state.cutout_url, caption="Cutout Image", use_column_width=True, width=700)
    if st.session_state.cutout_url:
        if st.button("Enhance Resolution"):
            st.session_state.res_url = increase_resolution(st.session_state.cutout_url)
            if st.session_state.res_url:
                st.image(st.session_state.res_url, caption="High Resolution Image", use_column_width=True)
    else:
        st.warning("Please complete cutout step first.")

elif choice == steps[3]:
    st.subheader("📦 Generate Packshot")
    if st.session_state.res_url:
        st.image(st.session_state.res_url, caption="Resolution Enhanced Image", use_column_width=True, width=700)
        if st.button("Generate Packshot"):
            st.session_state.packshot_url = generate_packshot(st.session_state.res_url)
        if st.session_state.packshot_url:
            st.image(st.session_state.packshot_url, caption="Product Packshot", use_column_width=True)
    else:
        st.warning("Please increase resolution first.")

elif choice == steps[4]:
    st.subheader("🌓 Add Shadow")
    if st.session_state.packshot_url:
        st.image(st.session_state.packshot_url, caption="Product Packshot", use_column_width=True, width=700)

        with st.form("shadow_form"):
            col1, col2, col3 = st.columns(3)

            shadow_color = col1.text_input(
                "Shadow Color (Hex)",
                value="#000000",
                help="Hex code for shadow color. Default is black."
            )

            shadow_intensity = col2.slider(
                "Shadow Intensity",
                min_value=0,
                max_value=100,
                value=60,
                help="Adjusts how strong the shadow appears."
            )

            shadow_blur = col3.slider(
                "Shadow Blur",
                min_value=0,
                max_value=100,
                value=15,
                help="Controls the softness of the shadow edges."
            )

            submit_shadow = st.form_submit_button("Add Shadow")

            if submit_shadow:
                st.session_state.shadow_url = add_shadow(
                    image_url=st.session_state.packshot_url,
                    shadow_color=shadow_color,
                    shadow_intensity=shadow_intensity,
                    shadow_blur=shadow_blur
                )

        if st.session_state.shadow_url:
            st.image(st.session_state.shadow_url, caption="Shadow Added", use_column_width=True)
    else:
        st.warning("Please create packshot first.")


elif choice == steps[5]:
    st.subheader("🌄 Generate Lifestyle Shot")
    if st.session_state.shadow_url:
        st.image(st.session_state.shadow_url, caption="Shadow Added", use_column_width=True, width=700)
        if st.button("Generate Lifestyle Shot"):
            st.session_state.lifestyle_url = generate_lifestyle(st.session_state.shadow_url)

            if st.session_state.lifestyle_url:
                st.image(st.session_state.lifestyle_url, caption="Lifestyle Shot", use_column_width=True)

    else:
        st.warning("Please add shadow first.")
