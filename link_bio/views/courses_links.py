
import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title 
from link_bio.styles.styles import Spacer as size
from link_bio.routes import Routes as Routes
import link_bio.constants  as constants

def courses_links() -> rx.Component:
        return rx.chakra.vstack(
                title("Cursos Gratis"),
                link_button("Retos de programacion",
                            "Ruta de estudio semanal para practicar logica de programacion",
                            "/icons/code.svg",
                            constants.CODE_CHALLENGE_URL
                            
                ),

                title("Mucho más en :"),
                link_button("Youtube",
                            "Directos de lunes a Viernes",
                            "/icons/twitch.svg",
                            "www.youtube.com"),
                link_button("Twitch",
                            "Tutoriales Semanales",
                            "/icons/twitch.svg",
                            "www.twitch.com"),
                link_button("Discord",
                            "Tutoriales Semanales",
                            "/icons/twitch.svg",
                            "www.discord.com"),


                width="100%",
                spacing=size.MEDIUM.value
        )
