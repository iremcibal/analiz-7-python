#definition Tanımlama

def ortalamaHesaplama() -> None :
    final =80
    vize=75
    ortalama = (vize* 0.4) + (final*0.6)
    print(ortalama)

ortalamaHesaplama()

def ortalamaHesaplama2() -> float :
    final =80
    vize=75
    ortalama = (vize* 0.4) + (final*0.6)
    return ortalama 

print(ortalamaHesaplama2())


def ortalamaHesaplaVeDondur(vize:float,final:float) -> float:
    return (vize* 0.4) + (final*0.6)


print(ortalamaHesaplaVeDondur(100,80))