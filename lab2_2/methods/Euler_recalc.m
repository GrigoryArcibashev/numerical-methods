function [x_next, y_next] = Euler_recalc(x, y, h)
    addpath func_f\
    x_next = x + h;
    y_ = y + h * f(x, y);
    y_next = y + h / 2 * (f(x, y) + f(x_next, y_));
end
