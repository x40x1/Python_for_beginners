export class Paddle {
  constructor(x, y, width, height, color) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.color = color;
    this.dy = 0;
  }

  draw(ctx) {
    ctx.fillStyle = this.color;
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }

  update(canvasHeight) {
    this.y += this.dy;

    // Keep paddle within canvas bounds
    if (this.y < 0) {
      this.y = 0;
    } else if (this.y + this.height > canvasHeight) {
      this.y = canvasHeight - this.height;
    }
  }

  moveUp() {
    this.dy = -5;
  }

  moveDown() {
    this.dy = 5;
  }

  stop() {
    this.dy = 0;
  }
}