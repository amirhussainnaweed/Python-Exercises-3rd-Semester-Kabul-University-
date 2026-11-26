# Snake — Django Edition

A browser-based Snake game built with Django, HTML Canvas, CSS, and vanilla JavaScript. Django serves the game page and static assets; the game itself runs in the browser.

## Run it

From the project folder in a PowerShell terminal:

```powershell
\.venv\Scripts\python.exe -m pip install -r requirements.txt
\.venv\Scripts\python.exe manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## Controls

- Arrow keys or `WASD`: move
- `Space`: pause or resume
- `R`: restart

The game starts when you press a movement key or the Start Game button.
