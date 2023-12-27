from visual import *
from math import radians, sin, cos

scene.width = 1100
scene.height = 700

def simuliraj_gibanje_projektila(v0, visina, kut, stupnjevi):
    # Konstante
    g = vector(0, -9.8, 0)  # Gravitacijsko ubrzanje (m/s^2)
    dt = 0.01  # Vremenski korak (s)

    # Kreiraj tlo
    tlo = box(pos=vector(0, 0, 0), size=vector(40, 0.5, 20), color=color.green)
    platforma = box(pos=vector(0, visina/2, 0), size=vector(0.2, visina-0.5, 1), color=color.green)

    tekst_pocetne_brzine = label(pos=vector(-8, 9, 0), text='Pocetna brzina = {:.4f} m/s'.format(v0), height=10, box=False)
    tekst_pocetne_visine = label(pos=vector(-8, 7, 0), text='Pocetna visina = {:.4f} m'.format(visina), height=10, box=False)
    tekst_pocetnog_kuta = label(pos=vector(-8, 5, 0), text='Pocetni kut bacanja = {:.4f} stupnjeva'.format(stupnjevi), height=10, box=False)

    tekst_brzine = label(pos=vector(-8, -9, 0), text='Trenutna brzina = {:.4f} m/s'.format(v0), height=10, box=False)
    tekst_visine = label(pos=vector(-8, -7, 0), text='Trenutna visina = {:.4f} m'.format(visina), height=10, box=False)
    tekst_udaljenosti = label(pos=vector(-8, -5, 0), text='Udaljenost = {:.4f} m'.format(0), height=10, box=False)

    # Kreiraj kuglu
    kugla = sphere(pos=vector(0, visina, 0), radius=0.2, color=color.blue, make_trail=True)

    # Inicijaliziraj varijable
    pocetna_pozicija = vector(0, visina, 0)
    pocetna_brzina = vector(v0 * cos(kut), 0, v0 * sin(kut))
    v0y = v0 * sin(kut)

    # Kreiraj vektore brzine
    pocetna_duljina_strelice = 1.0  # Postavite pocetnu duljinu strelice
    vektor_brzine = arrow(pos=vector(0, visina, 0), color=color.red, axis=vector(v0 * cos(kut), v0y, 0), shaftwidth=0.1, length=pocetna_duljina_strelice)
    strelica_vy = arrow(pos=vector(0, visina, 0), color=color.green, axis=vector(0, v0y, 0), shaftwidth=0.1, length=pocetna_duljina_strelice)
    strelica_vx = arrow(pos=vector(0, visina, 0), color=color.yellow, axis=vector(v0 * cos(kut), 0, 0), shaftwidth=0.1, length=pocetna_duljina_strelice)

    t = 0
    # Petlja simulacije
    while True:
        rate(100)  # Ograniciti brzinu simulacije radi bolje vizualizacije

        # Azuriraj poziciju i brzinu koristeci kinematicke jednadzbe
        kugla.pos.x += v0 * cos(kut) * dt
        kugla.pos.y += v0y * dt
        v0y += g.y * dt
        vt = v0 * sin(kut) - 9.81 * t

        t += dt

        if vt <= 0:
            vt = vt * -1

        # Azuriraj poziciju i smjer strelice za vektor brzine
        vektor_brzine.pos = vector(kugla.pos.x, kugla.pos.y, kugla.pos.z)
        vektor_brzine.axis = vector(v0 * cos(kut), v0y, 0)

        strelica_vy.pos = vector(kugla.pos.x, kugla.pos.y, kugla.pos.z)
        strelica_vy.axis = vector(0, v0y, 0)

        strelica_vx.pos = vector(kugla.pos.x, kugla.pos.y, kugla.pos.z)
        strelica_vx.axis = vector(v0 * cos(kut), 0, 0)

        # Postavite duljinu strelica na pocetnu duljinu
        vektor_brzine.length = pocetna_duljina_strelice
        strelica_vy.length = pocetna_duljina_strelice
        strelica_vx.length = pocetna_duljina_strelice

        # Provjeri je li kugla udarila o tlo
        if kugla.pos.y <= tlo.pos.y + 0.2:
            udaljenost = kugla.pos.x
            kugla.pos = pocetna_pozicija
            kugla.axis = pocetna_brzina
            vp = v0
            v0 = 0
            v0y = v0 * sin(kut)  # Resetiraj v0y
            t = 0  # Resetiraj vrijeme
            vt = v0 * sin(kut) - 9.81 * t  # Ponovo izracunaj vt u trenutku udara
            visina = 0
            tekst_brzine.text = 'Trenutna brzina = {:.4f} m/s'.format(vt)
            tekst_visine.text = 'Trenutna visina = {:.4f} m'.format(visina)
            tekst_udaljenosti.text = 'Udaljenost = {:.4f} m'.format(udaljenost)
            kugla.trail_object.visible = false
            kugla.visible = false
            v0 = vp
            vektor_brzine.visible = False
            strelica_vy.visible = False
            strelica_vx.visible = False
            break

        tekst_brzine.text = 'Trenutna brzina = {:.4f} m/s'.format(vt)
        tekst_visine.text = 'Trenutna visina = {:.4f} m'.format(kugla.pos.y)
        tekst_udaljenosti.text = 'Udaljenost = {:.4f} m'.format(kugla.pos.x)

# Inicijalni unos korisnika
v0 = float(input("Unesite brzinu v0 (m/s): "))
visina = float(input("Unesite visinu s koje je bacen objekt (m): "))
kut = float(input("Unesite kut pod kojim je bacen objekt (u stupnjevima): "))
stupnjevi = kut
kut = radians(kut)  # Pretvori kut u radijane

while True:
    simuliraj_gibanje_projektila(v0, visina, kut, stupnjevi)
    sleep(1)
