import reflex as rx
#COMUN

def lang () -> rx.Component : 
    return rx.script("document.documentElement.lang='es'")


_meta = [
    
]
preview = "https:// moure.dev./preview.jpg"

#Index

index_title  ="Sortiruiz, te enseño programacion y desarrollo software"
index_description = "Hola, mi nombre es Samuel, soy desarrollador software y estoy iniciandome en este campo"
index_meta = [
    {"name" : "og:title", "content" : index_title}, 
    {"name" : "og:description", "content" : index_description},
]
index_meta.extend(_meta)

#CURSOS
courses_title = ""
courses_description = ""
courses_meta = [
    
]
courses_meta.extend(_meta)

