from visual import *

# Postavljanje scene
scene.width = 1400
scene.height = 1000
scene.range = 30

# Unos pocetnih uvjeta od korisnika
x0 = float(raw_input("Unesite pocetnu tocku x0 (m): "))
y0 = float(raw_input("Unesite pocetnu tocku y0 (m): "))
v0 = float(raw_input("Unesite pocetnu brzinu v0 (m/s): "))
k = float(raw_input("Unesite jakost otpora zraka k: "))
t = float(raw_input("Unesite vrijeme trajanja gibanja (s): "))
pom = t
def simulacija():
    t = pom
    # Konstante
    g = vector(0, -9.8, 0)  # Gravitacijsko ubrzanje (m/s^2)
    dt = 0.01  # Vremenski korak (s)

    # Kreiranje kuglice (objekta)
    kuglica = sphere(pos=vector(x0, y0, 0), radius=0.2, color=color.blue, make_trail=True)

    # Inicijalizacija varijabli
    brzina = vector(v0, 0, 0)

    # Prikaz pocetnih uvjeta
    y0_text = label(pos=vector(x0-4, y0-5, 0), text='Pocetna tocka y0: {y0} m\n'.format(y0=y0), height=13, box=False)
    x0_text = label(pos=vector(x0-4, y0-4, 0), text='Pocetna tocka x0: {x0} m\n'.format(x0=x0), height=13, box=False)
    v0_text = label(pos=vector(x0-4, y0-3, 0), text='Pocetna brzina v0: {v0} m/s\n'.format(v0=v0), height=13, box=False)
    k_text = label(pos=vector(x0-4, y0-2, 0), text='Jakost otpora k: {k}\n'.format(k=k), height=13, box=False)
    t_text = label(pos=vector(x0-4, y0-1, 0), text='Vrijeme trajanja gibanja t: {t} s\n'.format(t=t), height=13, box=False)
    remaining_info_text = label(pos=vector(x0-4, y0-8, 0), height=13, box=False)

    # Petlja simulacije
    while True:
        rate(100)

        # Racunanje nove pozicije i brzine koristeci kinematicke jednadzbe
        brzina.y += g.y * dt
        brzina.x += (-k * brzina.x) * dt  # Uzimamo otpor zraka u obzir
        kuglica.pos.x += brzina.x * dt
        kuglica.pos.y += brzina.y * dt

        ver_brzina = brzina.y
        if brzina.y <=0:
            ver_brzina = ver_brzina*-1
        # Provjera uvjeta zavrsetka simulacije
        if t <= 0:
            kuglica.trail_object.visible = False
            remaining_info_text.text = 'Preostalo vrijeme: {:.2f} s\nTrenutna pozicija: ({:.2f}, {:.2f}) m\nTrenutna brzina: ({:.2f}, {:.2f}) m/s'.format(0, kuglica.pos.x, kuglica.pos.y, 0, 0)
            break
        # Azuriranje preostalog vremena
        # Azuriranje preostalog vremena
        t -= dt
        
        remaining_info_text.pos = vector(x0-4, y0-8, 0)
        # Azuriranje teksta o preostalom vremenu, poziciji i brzini
        remaining_info_text.text = 'Preostalo vrijeme: {:.2f} s\nTrenutna pozicija: ({:.2f}, {:.2f}) m\nTrenutna brzina: ({:.2f}, {:.2f}) m/s'.format(t, kuglica.pos.x, kuglica.pos.y, brzina.x, ver_brzina)
        
while True:
    simulacija()
    sleep(1)
