function [x_next, y_next] = Euler(x, y, h)
    addpath func_f\
    x_next = x + h;
    y_next = y + h * f(x, y);
end
