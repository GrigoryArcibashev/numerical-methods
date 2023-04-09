function [x_next, y_next] = Euler_implicit(x, y, h)
    addpath func_f\
    x_next = x + h;
    syms y_nt;
    y_next = vpasolve(y_nt - h * f(x_next, y_nt) - y == 0, y_nt);
end
