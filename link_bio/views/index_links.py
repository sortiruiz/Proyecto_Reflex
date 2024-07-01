
import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title 
from link_bio.styles.styles import Spacer as size
from link_bio.routes import Routes as Routes

def index_links() -> rx.Component:
        return rx.chakra.vstack(
                title("Comunidad"),
                link_button("Cursos Gratis",
                            "Consulta mis tutoriales para aprender programacion",
                            "/icons/code.svg",
                            Routes.COURSES.value,
                            is_external= False),
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
                link_button("Youtube(Canal Secundario)",
                            "Tutoriales Semanales",
                            "/icons/twitch.svg",
                            "www.youtube.com"),
                title("Comunidad"),
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
                link_button("Youtube(Canal Secundario)",
                            "Tutoriales Semanales",
                            "/icons/twitch.svg",
                            "www.youtube.com"),

                title("Contacto"),
                
                link_button(
                        "MyPublicInbox",
                        "Respuesta rapida y con preferencia",
                        "/icons/twitch.svg",
                        "www.google.es",
                ),
                link_button(
                        "Email",
                        "¿Quieres ayudarme a que siga creadno contenido?",
                        "/icons/twitch.svg",
                        "www.google.com",        
                ),

                width="100%",
                spacing=size.MEDIUM.value
        )

