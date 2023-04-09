function [Y] = generateYby_analytical(n, y0)
    addpath methods\
    [~, X, Y] = getAuxiliaryThings(n, y0);
    for i = 1:1:n
        Y(i + 1) = analytical(X(i + 1));
    end
end
