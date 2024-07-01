import reflex as rx
import link_bio.styles.styles as st

def title(text : str) -> rx.Component:
    return rx.chakra.heading(
        text,
        style = st.title_style,
    )