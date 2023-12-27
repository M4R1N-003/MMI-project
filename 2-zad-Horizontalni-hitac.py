from visual import *
from math import radians, sin, cos

scene.width = 1100
scene.height = 700
    
def simuliraj_gibanje_projektila(v0, visina):
    # Konstante
    g = vector(0, -9.8, 0)  # Gravitacijsko ubrzanje (m/s^2)
    dt = 0.01  # Vremenski korak (s)
    kut = 0
    # Kreiraj tlo
    tlo = box(pos=vector(0, 0, 0), size=vector(40, 0.5, 20), color=color.green)
    platforma = box(pos=vector(0, visina/2, 0), size=vector(0.2, visina-0.5, 1), color=color.green)

    tekst_brzine = label(pos=vector(-8, 9, 0), text='Trenutna brzina = {:.4f} m/s'.format(v0), height=10, box=False)
    tekst_visine = label(pos=vector(-8, 7, 0), text='Trenutna visina = {:.4f} m'.format(visina), height=10, box=False)
    tekst_udaljenosti = label(pos=vector(-8, 5, 0), text='Udaljenost = {:.4f} m'.format(0), height=10, box=False)

    # Kreiraj lopticu
    loptica = sphere(pos=vector(0, visina, 0), axis=vector(v0 * cos(kut), 0, v0 * sin(kut)), radius=0.2, color=color.blue, make_trail=True)

    # Inicijaliziraj varijable
    pocetna_pozicija = vector(0, visina, 0)
    pocetna_brzina = vector(v0 * cos(kut), 0, v0 * sin(kut))
    v0y = v0 * sin(kut)

    t = 0
    # Petlja simulacije
    while True:
        rate(100)  # Ogranici brzinu simulacije radi bolje vizualizacije

        # Azuriraj poziciju i brzinu koristeci kinematicke jednadzbe
        loptica.pos.x += v0 * cos(kut) * dt
        loptica.pos.y += v0y * dt
        v0y += g.y * dt
        vt = v0 * sin(kut) - 9.81 * t
        loptica.axis = vector(v0 * cos(kut), 0, v0y)

        t += dt

        if vt <= 0:
            vt = vt * -1
            
        # Provjeri udara li loptica u tlo
        if loptica.pos.y <= tlo.pos.y + 0.2:
            loptica.pos = pocetna_pozicija
            loptica.axis = pocetna_brzina
            v0y = v0 * sin(kut)  # Resetiraj v0y
            t = 0  # Resetiraj vrijeme
            vt = v0 * sin(kut) - 9.81 * t
            udaljenost = loptica.pos.x
            udaljenost = v0 * sqrt((2*visina)/9.81)
            trenutna_visina = loptica.pos.y
            trenutna_visina = 0
            tekst_brzine.text = 'Trenutna brzina = {:.4f} m/s'.format(vt)
            tekst_visine.text = 'Trenutna visina = {:.4f} m'.format(trenutna_visina)
            tekst_udaljenosti.text = 'Udaljenost = {:.4f} m'.format(udaljenost)
            loptica.trail_object.visible = False
            loptica.visible = False
            break
        
        tekst_brzine.text = 'Trenutna brzina = {:.4f} m/s'.format(vt)
        tekst_visine.text = 'Trenutna visina = {:.4f} m'.format(loptica.pos.y)
        tekst_udaljenosti.text = 'Udaljenost = {:.4f} m'.format(loptica.pos.x)

# Pocetni unos korisnika
v0 = float(input("Unesite brzinu v0 (m/s): "))
visina = float(input("Unesite visinu s koje je gurnut objekt (m): "))

while True:
    simuliraj_gibanje_projektila(v0, visina)
    sleep(1)
