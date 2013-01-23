from ejemplo import ClaseBase
from mockito import mock, verify, when

KUNPARAMETRO = 'algo'


class TestEjemplo:
    """docstring for EjemploTest"""
    def test_one(self):
        """docstring for initSouldReturnAClaseBaseObject"""
        #setup
        #action
        new_object = ClaseBase()
        #verify
        assert type(new_object) is ClaseBase

    def test_imprime_normal_should_call_metodo_normal(self):
        #setup
        test_object = ClaseBase()
        myMock = mock()
        test_object.dependencia = myMock
        #action
        test_object.imprime_normal()
        #verify
        verify(myMock).metodo_normal()

    def test_imprime_parametro_should_call_metodo_parametros(self):
        #setup
        test_object = ClaseBase()
        myMock = mock()
        test_object.dependencia = myMock
        #action
        test_object.imprime_parametro(KUNPARAMETRO)
        #verify
        verify(myMock).metodo_parametros(KUNPARAMETRO)

    def test_imprime_parametro_should_return_a_text(self):
        #setup
        test_object = ClaseBase()
        myMock = mock()
        test_object.dependencia = myMock
        when(myMock).metodo_parametros(KUNPARAMETRO).thenReturn("hello")
        #action
        algo = test_object.imprime_parametro(KUNPARAMETRO)
        #verify
        assert algo == "hello"
