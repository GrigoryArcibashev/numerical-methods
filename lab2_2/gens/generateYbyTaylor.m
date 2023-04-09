function [Y] = generateYbyTaylor(n, y0)
    addpath methods\
    [h, X, Y] = getAuxiliaryThings(n, y0);
    x = X(1);
    y = Y(1);
    for i = 1:1:n
        [x, y] = Taylor(x, y, h);
        Y(i + 1) = y;
    end
end
