from pe4_1 import GetallenStringsAndConversion
from pe4_2 import OperatorPrecedence
from pe4_3 import Input_Output

def RunLesson():

    les = int(input("Les: "))
    opdracht = int(input("Opdracht: "))

    def Switcher_Lessons(les, opdracht):
        switcher = {
            3: print('Niks hier'),
            4: Switcher_4(opdracht)
        }
        return switcher.get(les, "Deze les bestaat niet")

    def Switcher_4(opdracht):
        switcher = {
            1: GetallenStringsAndConversion()
        }
        return switcher.get(opdracht, "Deze opdracht bestaat niet")

    Switcher_Lessons(les, opdrachtwha)

RunLesson()