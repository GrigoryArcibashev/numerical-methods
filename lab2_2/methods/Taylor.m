function [x_next, y_next] = Taylor(x, y, h)
    addpath func_f\
    x_next = x + h;
    y_next = y ...
        + h * f(x, y) ...
        + h * h / 2 * (f_x(x, y) + f_y(x, y) * f(x, y));
end
