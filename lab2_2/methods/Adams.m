function [x_next, y_next] = Adams(x, y, x_prev, y_prev, h)
    addpath func_f\
    x_next = x + h;
    y_next = y + h / 2 * (3 * f(x, y) - f(x_prev, y_prev));
end
