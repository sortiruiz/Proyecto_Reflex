
import reflex as rx 
from link_bio.components.navbar import navbar
import link_bio.utils as utils 
from link_bio.views.header import header
from link_bio.views.index_links import index_links 
from link_bio.components.footer import footer
from link_bio.views.sponsors import sponsors as sponsor
import link_bio.styles.styles as st
from link_bio.styles.styles import Spacer as size

@rx.page( #Todos los atributos que necesita la propia web recogidos en un unico fichero 
        title  = utils.index_title,
        description = utils.index_description,
        image = utils.preview,
        meta = utils.index_meta,
)

def index()-> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.chakra.vstack(
                header(),                           
                index_links(),
                sponsor(),
                max_width = st.MAX_WIDTH,
                margin_y= size.BIG,
                width="100%",
                padding = size.BIG.value,
            ),
        ),
        footer(),
    )


