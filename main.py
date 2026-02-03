from pyscript import document
import asyncio

score = 0
running = False
time_left = 0

score_el = document.querySelector("#score")
status_el = document.querySelector("#status")
btn = document.querySelector("#btn")
start_btn = document.querySelector("#start")

def set_score(n: int):
    score_el.innerText = str(n)

def set_status(msg: str):
    status_el.innerText = msg

def on_click(evt=None):
    global score, running
    if not running:
        return
    score += 1
    set_score(score)

async def timer():
    global running, time_left
    time_left = 10
    while time_left > 0 and running:
        set_status(f"Time left: {time_left}s")
        await asyncio.sleep(1)
        time_left -= 1
    running = False
    set_status(f"Done! Final score: {score}")

async def start_game(evt=None):
    global score, running
    score = 0
    set_score(score)
    running = True
    set_status("Go!")
    await timer()

btn.addEventListener("click", on_click)
start_btn.addEventListener("click", lambda e: asyncio.ensure_future(start_game(e)))
