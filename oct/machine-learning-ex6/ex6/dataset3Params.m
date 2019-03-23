function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and
%   sigma. You should complete this function to return the optimal C and
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1.0;
sigma = 0.1;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example,
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using
%        mean(double(predictions ~= yval))
%
%c_vals = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
%sig_vals = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];

%model = svmTrain(X, y, c_vals(1), @(x1, x2) gaussianKernel(x1, x2, sig_vals(1)));
%predictions = svmPredict(model, Xval);

%min_error = [c_vals(1), sig_vals(1), mean(double(predictions ~= yval))];
%for i = 1:size(c_vals, 2),
%  for j = 2:size(sig_vals, 2),
%    model = svmTrain(X, y, c_vals(i), @(x1, x2) gaussianKernel(x1, x2, sig_vals(j)));
%    predictions = svmPredict(model, Xval);
%    disp(mean(double(predictions ~= yval)))
%    if (mean(double(predictions ~= yval)) < min_error(3)),
%      disp(c_vals(i))
%      disp(sig_vals(j))
%      min_error = [c_vals(i), sig_vals(j), mean(double(predictions ~= yval))];
%    end
%  end
%end

%disp(min_error)

%C = min_error(1);
%sigma = min_error(2);

% =========================================================================

end
