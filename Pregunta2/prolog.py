from pyswip import Prolog
prolog=Prolog()
prolog.assertz("padre('Juan','Maria')")
prolog.assertz("padre('Pablo','Juan')")
prolog.assertz("padre('Pablo','Marcela')")
prolog.assertz("padre('Carlos','Debora')")



for elemento in prolog.query("padre(X,Y)"):
	print(elemento["X"],"es el padre de ",elemento["Y"])

#print(padre())