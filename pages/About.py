import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="About",
        page_icon="👋",
    )

    st.write("#Welcome to my Project! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        hallo
        
    """
    )


if __name__ == "__main__":
    run()
