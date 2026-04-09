from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

from app.application.get_dice_roll import get_dice_roll


def get_dice_roll_screen() -> HTMLResponse:
    roll = get_dice_roll()
    return HTMLResponse(
        content=(
            "<html><body style='margin:0;background:#000;color:#00ff41;"
            "font-family:monospace;display:grid;place-items:center;height:100vh;'>"
            f"<h1 style='font-size:3rem;'>DADO: {roll}</h1>"
            "</body></html>"
        )
    )


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_api_route(
        path="/", endpoint=lambda: RedirectResponse(app.url_path_for(get_dice_roll_screen.__name__)), methods=["GET"], include_in_schema=False
    )

    app.add_api_route(path="/dice/roll", endpoint=get_dice_roll_screen)

    return app


app = create_app()
