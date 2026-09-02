import requests
from js import Response


async def on_fetch(request, env):
    html = """
    <!DOCTYPE html>
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Worker</title>
    </head>
    <body>
        <h1>سلام 👋</h1>
        <p>این HTML توسط Python Worker کلادفلر برگردانده شده است.</p>
    </body>
    </html>
    """

    print("HTML requested")

    return Response.new(
        html,
        {
            "headers": {
                "Content-Type": "text/html; charset=UTF-8"
            }
        }
    )
