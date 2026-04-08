import {
  createInitialState,
  queueDirection,
  step,
  togglePause,
} from "./snakeLogic.js";

const TICK_MS = 140;
const STORAGE_KEY = "snake-best-score";

const board = document.querySelector("#board");
const scoreLabel = document.querySelector("#score");
const bestScoreLabel = document.querySelector("#best-score");
const message = document.querySelector("#message");
const pauseButton = document.querySelector("#pause-button");
const restartButton = document.querySelector("#restart-button");
const controlButtons = Array.from(document.querySelectorAll("[data-direction]"));

let state = createInitialState();
let timerId = null;
let bestScore = readBestScore();

function readBestScore() {
  const stored = window.localStorage.getItem(STORAGE_KEY);
  return stored ? Number.parseInt(stored, 10) || 0 : 0;
}

function writeBestScore(score) {
  window.localStorage.setItem(STORAGE_KEY, String(score));
}

function updateBestScore() {
  if (state.score > bestScore) {
    bestScore = state.score;
    writeBestScore(bestScore);
  }
}

function createBoard() {
  const totalCells = state.gridSize * state.gridSize;

  for (let index = 0; index < totalCells; index += 1) {
    const cell = document.createElement("div");
    cell.className = "cell";
    cell.dataset.index = String(index);
    board.appendChild(cell);
  }
}

function cellIndex({ x, y }) {
  return y * state.gridSize + x;
}

function render() {
  const cells = Array.from(board.children);
  for (const cell of cells) {
    cell.className = "cell";
  }

  for (let index = state.snake.length - 1; index >= 0; index -= 1) {
    const segment = state.snake[index];
    const cell = cells[cellIndex(segment)];
    if (!cell) {
      continue;
    }

    cell.classList.add("snake");
    if (index === 0) {
      cell.classList.add("head");
    }
  }

  if (state.food) {
    const foodCell = cells[cellIndex(state.food)];
    if (foodCell) {
      foodCell.classList.add("food");
    }
  }

  updateBestScore();
  scoreLabel.textContent = String(state.score);
  bestScoreLabel.textContent = String(bestScore);

  if (!state.isAlive) {
    message.textContent = "Game over. Press Restart to play again.";
  } else if (state.isPaused) {
    message.textContent = "Paused.";
  } else if (!state.isStarted) {
    message.textContent = "Press any arrow key or WASD to start.";
  } else {
    message.textContent = "";
  }

  pauseButton.textContent = state.isPaused ? "Resume" : "Pause";
}

function startLoop() {
  if (timerId !== null) {
    return;
  }

  timerId = window.setInterval(() => {
    const nextState = step(state);
    if (nextState === state) {
      return;
    }

    state = nextState;
    render();

    if (!state.isAlive) {
      stopLoop();
    }
  }, TICK_MS);
}

function stopLoop() {
  if (timerId !== null) {
    window.clearInterval(timerId);
    timerId = null;
  }
}

function beginIfReady() {
  if (!state.isAlive) {
    return;
  }

  if (!state.isStarted) {
    state = {
      ...state,
      isStarted: true,
    };
  }

  if (!state.isPaused) {
    startLoop();
  }

  render();
}

function setDirection(direction) {
  const nextState = queueDirection(state, direction);
  if (nextState !== state) {
    state = nextState;
    beginIfReady();
  }
}

function restartGame() {
  stopLoop();
  state = createInitialState();
  render();
}

function handlePause() {
  state = togglePause(state);
  if (state.isPaused) {
    stopLoop();
  } else if (state.isStarted && state.isAlive) {
    startLoop();
  }
  render();
}

function onKeyDown(event) {
  const keyMap = {
    ArrowUp: "up",
    w: "up",
    W: "up",
    ArrowDown: "down",
    s: "down",
    S: "down",
    ArrowLeft: "left",
    a: "left",
    A: "left",
    ArrowRight: "right",
    d: "right",
    D: "right",
  };

  if (event.code === "Space") {
    event.preventDefault();
    handlePause();
    return;
  }

  const direction = keyMap[event.key];
  if (!direction) {
    return;
  }

  event.preventDefault();
  setDirection(direction);
}

createBoard();
render();

document.addEventListener("keydown", onKeyDown);
pauseButton.addEventListener("click", handlePause);
restartButton.addEventListener("click", restartGame);

for (const button of controlButtons) {
  button.addEventListener("click", () => {
    setDirection(button.dataset.direction);
  });
}
