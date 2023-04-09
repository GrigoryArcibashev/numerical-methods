function [Y] = generateYbyRunge_Kutt(n, y0)
    addpath methods\
    [h, X, Y] = getAuxiliaryThings(n, y0);
    x = X(1);
    y = Y(1);
    for i = 1:1:n
        [x, y] = Runge_Kutt(x, y, h);
        Y(i + 1) = y;
    end
end
