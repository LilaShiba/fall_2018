class Ship(){
  constructor(
    r=5,
    vel=createVector(random(0,7),
    pos = createVector(random(100,400),random(100,400)))
    {
    this.pos = pos;
    this.r = r;
    this.vel = vel;
    this.G = 6.67;
    this.acc = createVector(0,0);
    this.maxspeed = 5;
    this.maxforce = 17;
  }
  show() {
    stroke(255,10);
    strokeWeight(4);
    ellipse(this.pos.x, this.pos.y, this.r, this.r);
  }

  update() {
    this.vel.add(this.acc);
    this.vel.limit(this.maxspeed);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }
  applyForce(force) {
    var f = p5.Vector.div(force, this.r);
    this.acc.add(f)
  }
  attraction(m) {
    // direction of force
    let force = p5.Vector.sub(this.pos, m.pos);
    // distance between objects
    let distance = force.mag();
    // limit for atypical
    distance = constrain(distance, 20, 50);
    // normalize
    force.normalize();
    // get that gravitional force
    let strength = (this.G * this.r * m.r)/(distance * distance);
    // force vector = magnitude * direction
    force.mult(strength);
    return force;
  }
}
