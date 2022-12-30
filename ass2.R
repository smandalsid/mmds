ar=matrix(c(2.5, -1, -1, 2.5),2,2)
eig=eigen(ar)
eig_vals=eig$values
P=eig$vectors
library(matlib)
PInverse=