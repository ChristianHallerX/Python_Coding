# Snake

A small dependency-free Snake game built as a static page.

## Run

Open `index.html` in a browser, or serve the folder with any simple static server.

If Python is available on your machine, one easy option is:

```bash
python -m http.server 8123
```

Then navigate to `http://localhost:8123/snake/`.

## Controls

- Arrow keys or `WASD`: move
- `Space`: pause or resume
- `Restart`: reset the game

## Manual Verification

- Start a game and confirm movement begins on the first direction input.
- Eat food and confirm the snake grows by one segment and the score increments.
- Confirm the snake cannot reverse directly into itself.
- Run into a wall or the snake body and confirm the game ends.
- Pause and resume with `Space` or the pause button.
- Restart and confirm score resets while best score persists for the browser session.
