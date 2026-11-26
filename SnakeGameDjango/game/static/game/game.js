const canvas = document.getElementById("game-canvas");
const context = canvas.getContext("2d");
const scoreElement = document.getElementById("score");
const bestScoreElement = document.getElementById("best-score");
const statusElement = document.getElementById("status");
const startButton = document.getElementById("start-button");
const restartButton = document.getElementById("restart-button");

const CELL = 24;
const COLS = canvas.width / CELL;
const ROWS = canvas.height / CELL;
const SPEED = 105;

let snake;
let food;
let direction;
let nextDirection;
let score = 0;
let bestScore = Number(localStorage.getItem("snake-best-score") || 0);
let running = false;
let paused = false;
let gameOver = false;
let timer = null;

function resetRound() {
  const centerY = Math.floor(ROWS / 2);
  snake = [[8, centerY], [7, centerY], [6, centerY]];
  food = createFood();
  direction = [1, 0];
  nextDirection = [1, 0];
  score = 0;
  running = false;
  paused = false;
  gameOver = false;
  updateScoreboard();
  setStatus("Ready when you are");
  draw();
}

function createFood() {
  const freeCells = [];
  for (let x = 0; x < COLS; x += 1) {
    for (let y = 0; y < ROWS; y += 1) {
      if (!snake.some(([snakeX, snakeY]) => snakeX === x && snakeY === y)) {
        freeCells.push([x, y]);
      }
    }
  }
  return freeCells[Math.floor(Math.random() * freeCells.length)];
}

function startGame() {
  if (running) return;
  if (gameOver) resetRound();
  running = true;
  paused = false;
  setStatus("Game on — keep moving!");
  scheduleTick();
}

function restartGame() {
  resetRound();
  startGame();
}

function togglePause() {
  if (!running || gameOver) return;
  paused = !paused;
  setStatus(paused ? "Paused — press Space to resume" : "Game on — keep moving!");
  draw();
}

function changeDirection(newDirection) {
  if (gameOver) return;
  if (newDirection[0] === -direction[0] && newDirection[1] === -direction[1]) return;
  nextDirection = newDirection;
  if (!running) startGame();
}

function scheduleTick() {
  clearTimeout(timer);
  timer = setTimeout(tick, SPEED);
}

function tick() {
  if (!running) return;
  if (paused) {
    scheduleTick();
    return;
  }

  direction = nextDirection;
  const [headX, headY] = snake[0];
  const newHead = [headX + direction[0], headY + direction[1]];
  const hitWall = newHead[0] < 0 || newHead[0] >= COLS || newHead[1] < 0 || newHead[1] >= ROWS;
  const hitSelf = snake.slice(0, -1).some(([x, y]) => x === newHead[0] && y === newHead[1]);

  if (hitWall || hitSelf) {
    finishGame();
    return;
  }

  snake.unshift(newHead);
  if (newHead[0] === food[0] && newHead[1] === food[1]) {
    score += 1;
    bestScore = Math.max(bestScore, score);
    localStorage.setItem("snake-best-score", bestScore);
    food = createFood();
    updateScoreboard();
  } else {
    snake.pop();
  }

  draw();
  scheduleTick();
}

function finishGame() {
  running = false;
  gameOver = true;
  setStatus("Game over — press R to try again");
  draw();
}

function setStatus(message) {
  statusElement.textContent = message;
}

function updateScoreboard() {
  scoreElement.textContent = String(score).padStart(3, "0");
  bestScoreElement.textContent = String(bestScore).padStart(3, "0");
}

function draw() {
  context.fillStyle = "#0f1a2b";
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.strokeStyle = "#17263b";
  context.lineWidth = 1;
  for (let x = 0; x <= canvas.width; x += CELL) {
    context.beginPath(); context.moveTo(x, 0); context.lineTo(x, canvas.height); context.stroke();
  }
  for (let y = 0; y <= canvas.height; y += CELL) {
    context.beginPath(); context.moveTo(0, y); context.lineTo(canvas.width, y); context.stroke();
  }

  const foodX = food[0] * CELL + 5;
  const foodY = food[1] * CELL + 5;
  context.fillStyle = "#ff6b7a";
  context.beginPath(); context.arc(foodX + 7, foodY + 7, 7, 0, Math.PI * 2); context.fill();

  snake.forEach(([x, y], index) => {
    context.fillStyle = index === 0 ? "#7cf2c2" : "#46d9a0";
    const pad = index === 0 ? 2 : 3;
    context.fillRect(x * CELL + pad, y * CELL + pad, CELL - pad * 2, CELL - pad * 2);
  });

  if (!running && !gameOver) drawOverlay("PRESS START", "Use the arrow keys or WASD to begin");
  if (paused) drawOverlay("PAUSED", "Press Space to continue");
  if (gameOver) drawOverlay("GAME OVER", `Score: ${score}   •   Press R to restart`);
}

function drawOverlay(title, subtitle) {
  context.fillStyle = "rgba(11, 18, 32, .78)";
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.fillStyle = "#e6edf7";
  context.font = "700 28px Segoe UI, sans-serif";
  context.textAlign = "center";
  context.fillText(title, canvas.width / 2, canvas.height / 2 - 18);
  context.fillStyle = "#91a4bf";
  context.font = "14px Segoe UI, sans-serif";
  context.fillText(subtitle, canvas.width / 2, canvas.height / 2 + 20);
}

startButton.addEventListener("click", startGame);
restartButton.addEventListener("click", restartGame);
window.addEventListener("keydown", (event) => {
  const key = event.key.toLowerCase();
  const moves = {
    arrowup: [0, -1], w: [0, -1],
    arrowdown: [0, 1], s: [0, 1],
    arrowleft: [-1, 0], a: [-1, 0],
    arrowright: [1, 0], d: [1, 0],
  };
  if (moves[key]) {
    event.preventDefault();
    changeDirection(moves[key]);
  } else if (key === " ") {
    event.preventDefault();
    togglePause();
  } else if (key === "r") {
    restartGame();
  }
});

resetRound();
