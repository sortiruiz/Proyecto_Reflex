import reflex as rx 
import datetime 
import link_bio.styles.styles  as st
from link_bio.styles.styles import Spacer as size
from link_bio.styles.colors import TextColor as TextColor 
import link_bio.constants as Const
def footer() -> rx.Component:
    
    return rx.chakra.vstack(
        rx.image(src="avatar.jpg",
                 height=size.VERYBIG.value,
                 weight=size.VERYBIG.value,
                 alt = "Logotipo de Sortiruiz"),
                 
        rx.link(f"Esto es un enlace a mi web personal {datetime.date.today().year}",
                href="",is_external=True,
                font_size=size.MEDIUM.value,
                padding_top = size.LARGE.value,
                ),
        
        rx.link(
            rx.hstack(
                rx.image(
                    src = "/icons/sponsor.svg",
                    height =size.LARGE.value,
                    width = size.LARGE.value,
                ),
        
                rx.text("Este es el footer de mi web",
                        margin_top=size.ZERO.value,
                        style = st.button_body_style,
                        ),
                
            ),  
            href = Const.REPO_URL,
            is_external=True,          
        ), 
        align="center",
        margin_bottom=size.BIG.value,
        padding_x = size.BIG.value,
        padding_bottom = size.BIG.value,
        spacing  = size.ZERO.value,
        color = TextColor.FOOTER.value,
    )