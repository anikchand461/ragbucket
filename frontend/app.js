const canvas = document.getElementById('bg');
if (canvas) {
  const c = canvas.getContext('2d');
  const points = Array.from({length:90}, () => ({x:Math.random()*innerWidth,y:Math.random()*innerHeight,vx:(Math.random()-.5)*.45,vy:(Math.random()-.5)*.45,r:Math.random()*2.1+0.5}));
  const resize = () => {canvas.width = innerWidth; canvas.height = innerHeight;};
  resize(); addEventListener('resize', resize);
  (function loop(){
    c.clearRect(0,0,canvas.width,canvas.height);
    for (const p of points) {
      p.x+=p.vx; p.y+=p.vy;
      if(p.x<0||p.x>canvas.width)p.vx*=-1;
      if(p.y<0||p.y>canvas.height)p.vy*=-1;
      c.fillStyle='rgba(255,255,255,0.5)'; c.beginPath(); c.arc(p.x,p.y,p.r,0,Math.PI*2); c.fill();
    }
    for (let i=0;i<points.length;i++) for (let j=i+1;j<points.length;j++) {
      const a=points[i], b=points[j];
      const d=Math.hypot(a.x-b.x,a.y-b.y);
      if(d<110){c.strokeStyle=`rgba(80,230,255,${(1-d/110)*0.2})`;c.lineWidth=1;c.beginPath();c.moveTo(a.x,a.y);c.lineTo(b.x,b.y);c.stroke();}
    }
    requestAnimationFrame(loop);
  })();
}

document.querySelectorAll('.links a').forEach(a=>{ if (location.pathname.endsWith(a.getAttribute('href'))) a.classList.add('active'); });

const chunks = document.getElementById('chunks');
if (chunks) {
  const docs = document.getElementById('docs');
  const meter = document.getElementById('meter');
  const log = document.getElementById('simlog');
  const render = () => {
    const d = Number(docs.value);
    const c = d * 12;
    const t = c * 768;
    const q = Math.max(6, Math.round(Math.log2(c) * 3));
    chunks.textContent = c.toLocaleString();
    meter.style.width = `${Math.min(100,d*4)}%`;
    log.textContent = `docs: ${d}\nchunks: ${c}\ntokens indexed: ${t.toLocaleString()}\nretrieval candidates: ${q}\nlatency estimate: ${(180+q*12)}ms`;
  };
  docs.addEventListener('input', render);
  render();
}
