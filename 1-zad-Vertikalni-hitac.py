from visual import *

scene.width = 1600
scene.height = 1000
def simulacija():
    g = 9.81  
    t = 0      
    dt = 0.01  

    v0_input = float(raw_input("Unesite pocetnu brzinu (m/s): "))
    h = 0
    v0 = v0_input
    ravnina_lokacija = vector(0, -0.5, 0)
    ravnina = box(pos=ravnina_lokacija, size=vector(10, 0.01, 10), color=color.green)
    y0 = h

    loptica = sphere(pos=vector(0, y0, 0), radius=0.5, color=color.red)

    visina = 0
    brzina_oznaka = label(pos=vector(-4, 3, 0), text="Brzina: {:.4f} m/s".format(v0), height=16, color=color.red, box=False)
    visina_oznaka = label(pos=vector(4, 3, 0), text="Visina: {:.4f} m".format(h), height=16, color=color.red, box=False)
    max_visina_oznaka = label(pos=vector(0, -1, 0), text="Najveca visina: {:.4f} m".format(0), height=16, color=color.red, box=False)

    max_visina = 0

    while loptica.pos.y >= 0:
        rate(100)
        loptica.pos.y = y0 + v0 * t - 0.5 * g * t**2
        loptica.velocity = vector(0, v0 - g * t, 0)

        visina = loptica.pos.y - y0
        brzina = mag(loptica.velocity)
        if loptica.pos.y <= 0:
            brzina = 0
            visina = 0
            t = 0
            loptica.pos.y = y0
            loptica.velocity = vector(0, 0, 0)

        brzina_oznaka.text = "Brzina: {:.4f} m/s".format(brzina)
        visina_oznaka.text = "Visina: {:.4f} m".format(visina)

        if visina > max_visina:
            max_visina = visina
            max_visina_oznaka.text = "Najveca visina: {:.4f} m".format(max_visina)

        t += dt

    loptica.visible = False

while True:
    simulacija()
