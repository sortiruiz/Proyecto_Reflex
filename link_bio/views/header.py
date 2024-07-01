import reflex as rx
from link_bio.styles.styles import Spacer as size
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title as title
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import Font as Font

def header(details = True) -> rx.Component:
        
        return rx.chakra.vstack(
                rx.chakra.hstack(
                        rx.chakra.avatar(name="Samuel Ortiz", 
                                         size="xl",
                                         src="SR_AVATAR.png",
                                         color=TextColor.BODY.value,
                                         bg=Color.CONTENT.value,
                                         padding = "2px",
                                         border = "4px",
                                         border_color = Color.PRIMARY.value,
                                         ),
                        rx.chakra.vstack(
                               title(
                                        "Samuel Ortiz",
                                ),
                                rx.text(
                                        "@sortiruiz",
                                        margin_top="0px",
                                        color = TextColor.BODY.value,
                                ),
                                rx.chakra.hstack(   
                                        rx.chakra.responsive_grid(           
                                                link_icon("/icons/twitch.svg",
                                                        "www.sortiruiz.com",
                                                        "Twitch"),
                                                link_icon("/icons/twitch.svg",
                                                        "www.sortiruiz.com",
                                                        "Instagram"),
                                                link_icon("/icons/twitch.svg",
                                                        "www.sortiruiz.com",
                                                        "TikTok"),
                                                link_icon("/icons/twitch.svg",
                                                        "www.sortiruiz.com",
                                                        "Spotify"),
                                                link_icon("/icons/twitch.svg",
                                                        "www.sortiruiz.com",
                                                        "Linkedin"),
                                                link_icon("/icons/twitch.svg",
                                                        "www.sortiruiz.com",
                                                        "Github"),
                                                spacing = size.MEDIUM.value,
                                                columns=[3,6],
                                        ),
                                        spacing= size.MEDIUM.value,
                                ),
                                align_items="start",
                        ),
                        
                                
                        spacing=size.BIG.value

                ),
                


                
                
                #ESTO LO TENGO QUE CONDICIONAR
                rx.cond(details, 
                        rx.chakra.vstack(
                                rx.flex(#FLEX SE ENCARGA DE AJUSTAR A LA PANTALLA DISPONIBLE EL DISEÑO 
                                        info_text("+13 ","Años de experiencia"),
                                        rx.spacer(),
                                        info_text("+100 ","Aplicaciones creadas"),
                                        rx.spacer(),
                                        info_text("+100M ","seguidores"),
                                        width="100%",
                                ),
                                rx.text("""
                                        Estoy empezando con el desarrollo
                                        de software, esta será mi primera 
                                        pagina con reflex 
                                        Estoy emocionado de compartir este espacio 
                                        contigo y de embarcarme en esta aventura juntos.
                                        Espero que encuentres algo aquí que te inspire, 
                                        te enseñe algo nuevo, o simplemente te haga sonreír.

                                        Gracias por visitar mi página web. ¡Explora, disfruta 
                                        y no dudes en ponerte en contacto si quieres saber más!""",

                                        color = TextColor.BODY.value,
                                        font_size  = size.MEDIUM.value,
                                        ),
                                width = "100%",
                                spacing=size.BIG.value,
                        ),
                ),     
                spacing=size.BIG.value,
                align_items="start"

        )