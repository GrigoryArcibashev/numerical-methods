function [y] = analytical(x)
    addpath func_f\
    y = 0.1 * exp(10 * x^3 - 27/2 * x^2 + 21/5 * x);
end
