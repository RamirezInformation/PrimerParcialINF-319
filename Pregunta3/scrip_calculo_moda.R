attach(datos)
summary(datos)
mean(Edades,na.rm = T)
library(modeest)
moda <- mlv(Edades,method=mfv,na.rm = T)
moda

