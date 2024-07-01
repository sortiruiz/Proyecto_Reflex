import reflex as rx 
import link_bio.styles.styles as styles
from  link_bio.pages.index import index  #esto es importante para que coja el rx.app 
from  link_bio.pages.courses import courses  #esto es importante para que coja el rx.app 


app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLES,
)
