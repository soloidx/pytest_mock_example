class Dependencia(object):
    """docstring for Dependencia"""

    def metodo_normal(self):
        """docstring for metodo_normal"""
        print "dependencia_metodo_normal"

    def metodo_parametros(self, parametro):
        """docstring for metodo_normal"""
        print "dependencia_metodo_parametro"
        return parametro + 'algo'
