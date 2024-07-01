from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight


#Constants
MAX_WIDTH = "600px"

STYLESHEETS  = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"]


#Sizes 
class Spacer(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MEDIUM_LARGE = "1.3em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG = "4em"

#Styles

BASE_STYLES = {
    
    "font_family" : Font.DEFAULT.value,
    "font_weight" : FontWeight.LIGHT.value,
    "background_color" : Color.BACKGROUND.value,
    
    rx.chakra.button:{
        "width":"100%",
        "height":"100%",
        "padding":Spacer.SMALL,
        "border_radius":Spacer.SMALL,
        "color" : TextColor.HEADER.value, 
        "background_color" : Color.CONTENT.value,
        "white_space" : "normal",
        "text_align" : "start",
        "_hover" : {
            "background_color" : Color.SECONDARY.value,
        },
        
    },

    rx.chakra.link:{
        "text_decoration":"none",
        "_hover":{}
    },
    
    rx.link:{
        "text_decoration" : "none", 
    },
    
    rx.chakra.heading : {
        "font_size" : "2xl",
        "color" : TextColor.HEADER.value,
        "font_family" : Font.DEFAULT.value,  
        "font_weight" : FontWeight.MEDIUM.value,  
    },
}

button_title_style = dict(
    font_family =  Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size= Spacer.DEFAULT.value,
    color = TextColor.HEADER.value,

)

button_body_style = dict(
    font_family =  Font.DEFAULT.value,
    font_weight = FontWeight.LIGHT.value,
    font_size=Spacer.MEDIUM.value,   
    color = TextColor.BODY.value,
)

navbar_title_style = dict(
    font_family = Font.LOGO.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Spacer.MEDIUM_LARGE.value,

)

title_style = dict(
    width="100%",
    font_weight = FontWeight.MEDIUM.value,
    padding_top=Spacer.DEFAULT.value,
    color = TextColor.HEADER.value,
)
