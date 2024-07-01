import reflex as rx
import link_bio.styles.styles as st

def link_sponsor(imagen : str, url:str, alt : str) -> rx.Component:
    return rx.link(
            rx.image(
                src=imagen,
                height  = "3.5em",
                aspect_radio = "5/2",
                width="auto",
                alt = alt,
            ),
            href = url,
            is_external=True,   
),

