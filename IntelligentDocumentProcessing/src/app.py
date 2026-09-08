import sys
import os
import json
import tempfile

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from src.api.routes import process_file


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Intelligent Document AI",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📄 Intelligent Document AI")

st.write(
    "Upload a document and extract important information using OCR."
)

st.divider()


# --------------------------------------------------
# File Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["png", "jpg", "jpeg", "pdf"]
)


if uploaded_file is not None:

    st.success(f"✅ File uploaded: {uploaded_file.name}")

    file_suffix = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=file_suffix
    ) as temp_file:

        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name


    # --------------------------------------------------
    # Process Document
    # --------------------------------------------------

    if st.button("🔍 Process Document", type="primary"):

        with st.spinner("🔄 Processing document..."):

            try:

                result = process_file(temp_path)

                fields = result["fields"]

                st.success("🎉 Document processed successfully!")

                st.divider()


                # --------------------------------------------------
                # Extracted Fields
                # --------------------------------------------------

                st.subheader("📋 Extracted Fields")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "👤 Name",
                        fields["name"] or "Not found"
                    )

                with col2:
                    st.metric(
                        "📧 Email",
                        fields["email"] or "Not found"
                    )

                with col3:
                    st.metric(
                        "📞 Phone",
                        fields["phone"] or "Not found"
                    )


                col4, col5, col6 = st.columns(3)

                with col4:
                    st.metric(
                        "📅 Date",
                        fields["date"] or "Not found"
                    )

                with col5:
                    st.metric(
                        "💰 Amount",
                        fields["amount"] or "Not found"
                    )

                with col6:
                    st.metric(
                        "📍 Address",
                        fields["address"] or "Not found"
                    )


                st.divider()


                # --------------------------------------------------
                # Download Extracted Data
                # --------------------------------------------------

                st.subheader("⬇️ Download Extracted Data")

                json_data = json.dumps(
                    fields,
                    indent=4,
                    ensure_ascii=False
                )

                st.download_button(
                    label="📥 Download JSON",
                    data=json_data,
                    file_name="extracted_data.json",
                    mime="application/json"
                )


                st.divider()


                # --------------------------------------------------
                # OCR Text
                # --------------------------------------------------

                st.subheader("📝 OCR Text")

                st.text_area(
                    "Extracted Text",
                    result["text"],
                    height=250
                )


            except Exception as e:

                st.error(f"❌ Error: {e}")


            finally:

                if os.path.exists(temp_path):
                    os.remove(temp_path)