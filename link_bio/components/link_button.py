import reflex as rx
import link_bio.styles.styles as st

def link_button(title:str,body : str, image : str, url:str,is_external=True) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.hstack(
                rx.chakra.image(
                    src = image,
                    width=st.Spacer.LARGE.value,
                    heigth=st.Spacer.LARGE.value,
                    margin=st.Spacer.MEDIUM.value,
                    alt = title, 
                ),
                rx.chakra.vstack(
                    rx.text(title,
                            style=st.button_title_style
                            ),
                    rx.text(body,
                            style = st.button_body_style),

                    padding_right = st.Spacer.SMALL.value,
                    padding_y = st.Spacer.SMALL.value,
                    spacing = st.Spacer.SMALL.value,
                    align_items="start",
                    margin  = st.Spacer.ZERO.value,

                ),
                width = "100%",
            ),
        ),
        href=url,
        is_external=is_external,
        width="100%",
        
        
    )
