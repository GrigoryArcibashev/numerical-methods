function [x_next, y_next] = Cauchy(x, y, h)
    addpath func_f\
    x_next = x + h;
    x_half = x + h / 2;
    y_half = y + h / 2 * f(x, y);
    y_next = y + h * f(x_half, y_half);
end
