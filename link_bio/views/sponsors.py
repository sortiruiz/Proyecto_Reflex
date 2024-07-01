import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor 
from link_bio.styles.styles import Spacer as size

def sponsors() -> rx.Component: 
    return rx.chakra.vstack(
        title("Colaboran"),
        rx.chakra.responsive_grid(
            #url es la web que deberiamos añadir desde constantes
            
            link_sponsor("/avatar.jpg","url","Logotipo El Gato"),
            link_sponsor("/avatar.jpg","url","Logotipo Microsoft"),
            link_sponsor("/icons/sponsor.svg","url","Logotipo twitch"),
            spacing=size.BIG.value,
            columns=[1,3],
        ),
        width="100%",
        align_items="start",
        spacing =size.MEDIUM.value,
    )