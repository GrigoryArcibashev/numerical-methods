function [h, X, Y] = getAuxiliaryThings(n, y0)
    h = 1 / n;
    X = 0:h:1;
    Y = zeros(1, n + 1, 'double');
    Y(1, 1) = y0;
end
