function [x_next, y_next] = Runge_Kutt(x, y, h)
    addpath func_f\
    K1 = h * f(x, y);
    K2 = h * f(x + h / 2, y + K1 / 2);
    K3 = h * f(x + h / 2, y + K2 / 2);
    K4 = h * f(x + h, y + K3);
    x_next = x + h;
    y_next = y + (K1 + 2 * K2 + 2 * K3 + K4) / 6;
end
