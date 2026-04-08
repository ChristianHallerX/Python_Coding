const GRID_SIZE = 16;
const INITIAL_DIRECTION = "right";

const OFFSETS = {
  up: { x: 0, y: -1 },
  down: { x: 0, y: 1 },
  left: { x: -1, y: 0 },
  right: { x: 1, y: 0 },
};

const OPPOSITES = {
  up: "down",
  down: "up",
  left: "right",
  right: "left",
};

function toKey(position) {
  return `${position.x},${position.y}`;
}

export function createFood(snake, gridSize = GRID_SIZE, random = Math.random) {
  const occupied = new Set(snake.map(toKey));
  const available = [];

  for (let y = 0; y < gridSize; y += 1) {
    for (let x = 0; x < gridSize; x += 1) {
      const cell = { x, y };
      if (!occupied.has(toKey(cell))) {
        available.push(cell);
      }
    }
  }

  if (available.length === 0) {
    return null;
  }

  const index = Math.floor(random() * available.length);
  return available[index];
}

export function createInitialState(random = Math.random, gridSize = GRID_SIZE) {
  const center = Math.floor(gridSize / 2);
  const snake = [
    { x: center, y: center },
    { x: center - 1, y: center },
    { x: center - 2, y: center },
  ];

  return {
    gridSize,
    snake,
    direction: INITIAL_DIRECTION,
    pendingDirection: INITIAL_DIRECTION,
    food: createFood(snake, gridSize, random),
    score: 0,
    isAlive: true,
    isStarted: false,
    isPaused: false,
  };
}

export function queueDirection(state, nextDirection) {
  if (!OFFSETS[nextDirection]) {
    return state;
  }

  if (OPPOSITES[state.direction] === nextDirection && state.snake.length > 1) {
    return state;
  }

  return {
    ...state,
    pendingDirection: nextDirection,
  };
}

export function togglePause(state) {
  if (!state.isAlive || !state.isStarted) {
    return state;
  }

  return {
    ...state,
    isPaused: !state.isPaused,
  };
}

export function step(state, random = Math.random) {
  if (!state.isAlive || state.isPaused) {
    return state;
  }

  const direction = state.pendingDirection;
  const head = state.snake[0];
  const offset = OFFSETS[direction];
  const nextHead = {
    x: head.x + offset.x,
    y: head.y + offset.y,
  };

  const hitsWall =
    nextHead.x < 0 ||
    nextHead.y < 0 ||
    nextHead.x >= state.gridSize ||
    nextHead.y >= state.gridSize;

  if (hitsWall) {
    return {
      ...state,
      direction,
      isAlive: false,
      isStarted: true,
      isPaused: false,
    };
  }

  const grows =
    state.food !== null &&
    nextHead.x === state.food.x &&
    nextHead.y === state.food.y;

  const nextSnake = [nextHead, ...state.snake];
  if (!grows) {
    nextSnake.pop();
  }

  const body = grows ? nextSnake.slice(1) : nextSnake.slice(1);
  const bodyCollision = body.some(
    (segment) => segment.x === nextHead.x && segment.y === nextHead.y,
  );

  if (bodyCollision) {
    return {
      ...state,
      direction,
      isAlive: false,
      isStarted: true,
      isPaused: false,
    };
  }

  const food = grows ? createFood(nextSnake, state.gridSize, random) : state.food;

  return {
    ...state,
    snake: nextSnake,
    direction,
    pendingDirection: direction,
    food,
    score: state.score + (grows ? 1 : 0),
    isAlive: true,
    isStarted: true,
  };
}

export const SnakeLogic = {
  GRID_SIZE,
  createFood,
  createInitialState,
  queueDirection,
  step,
  togglePause,
};
