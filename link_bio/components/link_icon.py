import reflex as rx
import link_bio.styles.styles as st
from link_bio.styles.styles import Spacer as Size

def link_icon(image : str, url:str , alt : str) -> rx.Component:
    return rx.link(
            rx.chakra.image(
                src = image,
                width = Size.DEFAULT.value,
                alt = alt ,
            ),
            href=url,
            is_external=True,
        ),

