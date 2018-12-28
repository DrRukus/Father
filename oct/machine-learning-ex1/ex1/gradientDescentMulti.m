function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta.
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %

    sums = zeros(size(X, 2), 1);
    for i = 1:size(X, 2),
      sums = sums + (theta' * X(i,:)' - y(i)) * X(i,:);
      % thisSum2 += (theta' * X(i,:)' - y(i)) * X(i,2);
    end;
    temps = theta - (alpha / m) * sums;
    % temp2 = theta(2) - (alpha / m) * thisSum2;
    theta = temps;

    % disp(computeCost(X, y, theta));



    % ============================================================

    % Save the cost J in every iteration
    J_history(iter) = computeCostMulti(X, y, theta);

end

end
