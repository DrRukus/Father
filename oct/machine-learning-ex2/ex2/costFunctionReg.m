function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

%sig = sigmoid(theta' * X(1,:)')
%J += (((-1 * y(1)) * log(sig)) - ((1 - y(1)) * log(1 - sig)))
%grad += (sig - y(1)) * X(1,:)'

for i = 1:m,
  sig = sigmoid(theta' * X(i,:)');
  J += (((-1 * y(i)) * log(sig)) - ((1 - y(i)) * log(1 - sig)));
  grad += (sig - y(i)) * X(i,:)'
end

for j = 2:size(theta, 1),
  J += (lambda / 2) * theta(j) * theta(j);
end

grad += lambda * [0; theta(2:size(theta,1))]

J /= m;
grad /= m;




% =============================================================

end
