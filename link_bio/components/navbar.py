import reflex as rx
from link_bio.styles.styles import Spacer as size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles
import link_bio.constants as constants
from link_bio.routes import Routes as Routes
from link_bio.components.ant_components import float_button

def navbar() -> rx.Component:

    return rx.chakra.hstack(
        rx.link(
            rx.box(
                rx.chakra.span("sorti",color=Color.PRIMARY.value),
                rx.chakra.span("ruiz",color = Color.SECONDARY.value),
                style= styles.navbar_title_style,
            ),
            href = Routes.INDEX.value,
            is_external = False,

        ),
                float_button(
                    #AHORA TENGO DOS PARAMETROS QUE INDICAR 
                    icon = rx.image(src="/iconns/donate.svg"),
                    href = constants.COFFE_URL
                ),
                position="sticky",
                bg=Color.CONTENT.value,
                padding_x=size.BIG.value,
                paddyng_y=size.DEFAULT.value,
                z_index = "999",
                top = "0",
                
    )