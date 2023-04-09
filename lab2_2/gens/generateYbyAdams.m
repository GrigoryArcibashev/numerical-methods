function [Y] = generateYbyAdams(n, y0)
    addpath methods\
    [h, X, Y] = getAuxiliaryThings(n, y0);
    [x, y] = Runge_Kutt(X(1), Y(1), h);
    Y(2) = y;
    for i = 2:1:n
        [x, y] = Adams(x, y, X(i-1), Y(i-1), h);
        Y(i + 1) = y;
    end
end
