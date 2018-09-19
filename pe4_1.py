cijferCSN = 8
cijferICOR = 9
cijferPROG = 10

gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
beloning = (cijferCSN + cijferICOR + cijferPROG) * 30
overzicht = 'Mijn cijfers (gemiddeld een {}) leveren een beloning van €{} op!'.format(gemiddelde, beloning)

print(overzicht)