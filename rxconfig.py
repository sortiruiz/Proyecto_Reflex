import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "https://localhost:3000",
        "https://sortiruiz-web.vercel.app/"
    ]
)