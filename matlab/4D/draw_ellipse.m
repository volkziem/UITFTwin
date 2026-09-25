% draw_ellipse.m, V. Ziemann, 260911
function draw_ellipse(xc,yc,w,h)
t = linspace(0, 2*pi, 100);
x = xc + 0.5*w*cos(t);
y = yc + 0.5*h*sin(t);
fill(x, y, 'cyan', 'EdgeColor', 'black');