from dependencia import Dependencia


class ClaseBase(object):
    """docstring for ClaseBase"""

    __dependencia = None

    def __init__(self):
        """docstring for __init__"""
        super(ClaseBase, self).__init__()

    def get_dependencia(self):
        if self.__dependencia is None:
            self.__dependencia = Dependencia()
        return self.__dependencia

    def set_dependencia(self, depend):
        self.__dependencia = depend

    def imprime_normal(self):
        """docstring for imprime_normal"""
        self.dependencia.metodo_normal()

    def imprime_parametro(self, algo):
        """docstring for imprime_normal"""
        return self.dependencia.metodo_parametros(algo)

    dependencia = property(get_dependencia, set_dependencia)


def main():
    """docstring for main"""
    clase = ClaseBase()
    clase.imprime_normal()
    clase.imprime_parametro('holaaa')

if __name__ == '__main__':
    main()
