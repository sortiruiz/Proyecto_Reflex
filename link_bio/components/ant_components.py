#FICHERO CON LOS COMPONENTES DE LA LIBRERIA ANT 

import reflex as rx
from link_bio.styles.colors import Color as Color

class FloatButton(rx.Component): #PUEDO IMPORTAR DESDE OTRASLIBRERIAS Y DARLE ATRIBUTOS 
    library = "antd"
    tag = "FloatButton"  
    icon : rx.Var[rx.el.Img] #AVISO DE QUE SON VALORES DINAMICOS, LOS PUEDO PERSONALIZAR SEGUN LA PANTALLA DESDE DONDE LLAMO 
    href : rx.Var[str]
    target = "_blank"
    badge = {"dot" : True, "color" : Color.PRIMARY.value}

float_button = FloatButton.create