def NRMethod(f: object, g: float = 0.0) -> float:
    """
    :param f: la funzione. Passa una funzione anonima lambda
    :param g: un qualsiasi punto da provare
    :return: float: il punto in cui la funzione fa 0
    """

    def zerodi(f, x0):
        """
        :param f: la funzione. Passa una funzione anonima lambda
        :return: float: il punto in cui la funzione fa 0
        """

        # data un equazione lineare, rida' il valore x in cui quella equazione e' uguale a 0

        # funzione per trovare la derivata di una funzione in un punto di essa
        def dydx(f):
            dx = 0.0005
            return (f(g + dx) - f(g)) / dx

        m = dydx(f)
        # equazione: y = m(x-x0) + y0
        # rigiro un po' di cose quando y = 0...
        # -y0 = m(x-x0)
        # -y0/m = x-x0
        # x = -y0/m + x0
        y0 = f(x0)
        try:
            return -(y0 / m) + x0
        except ZeroDivisionError:
            return x0+0.05
    n = 15  # numero di iterazioni
    for _ in range(n):
        g = zerodi(f, g)
    return g