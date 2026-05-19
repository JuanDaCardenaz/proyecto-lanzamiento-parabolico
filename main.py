from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import minimize_scalar

class SistemaFisico(ABC):
    @abstractmethod
    def simular(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

class Proyectil:
    def __init__(self, velocidad_inicial, gravedad):
        self.v0 = velocidad_inicial
        self.g = gravedad

class LanzamientoParabolico(SistemaFisico):
    def __init__(self, proyectil, objetivo_x, objetivo_y):
        self.proyectil = proyectil
        self.objetivo_x = objetivo_x
        self.objetivo_y = objetivo_y
        self.angulo_optimo = None
        self.error_minimo = None
        self.t = None
        self.x = None
        self.y = None

    def posicion(self, angulo, t):
        v0 = self.proyectil.v0
        g = self.proyectil.g
        x = v0 * np.cos(angulo) * t
        y = v0 * np.sin(angulo) * t - 0.5 * g * t**2
        return x, y

    def error_objetivo(self, angulo):
        v0 = self.proyectil.v0
        t_objetivo = self.objetivo_x / (v0 * np.cos(angulo))
        _, altura = self.posicion(angulo, t_objetivo)
        return abs(altura - self.objetivo_y)

    def optimizar_angulo(self):
        resultado = minimize_scalar(
            self.error_objetivo,
            bounds=(np.radians(1), np.radians(89)),
            method="bounded"
        )
        self.angulo_optimo = resultado.x
        self.error_minimo = resultado.fun

    def simular(self):
        if self.angulo_optimo is None:
            self.optimizar_angulo()
        v0 = self.proyectil.v0
        g = self.proyectil.g
        theta = self.angulo_optimo
        t_final = 2 * v0 * np.sin(theta) / g
        self.t = np.linspace(0, t_final, 160)
        self.x, self.y = self.posicion(theta, self.t)
        return self.t, self.x, self.y

    def resumen(self):
        return {
            "angulo": np.degrees(self.angulo_optimo),
            "error": self.error_minimo,
            "altura_maxima": np.max(self.y),
            "alcance": np.max(self.x)
        }

class Analizador:
    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):
        datos = self.sistema.resumen()
        print("ANALISIS DEL LANZAMIENTO")
        print(f"Velocidad inicial: {self.sistema.proyectil.v0:.2f} m/s")
        print(f"Gravedad: {self.sistema.proyectil.g:.2f} m/s^2")
        print(f"Objetivo: ({self.sistema.objetivo_x:.2f}, {self.sistema.objetivo_y:.2f}) m")
        print(f"Angulo optimo: {datos['angulo']:.2f} grados")
        print(f"Error minimo: {datos['error']:.4f} m")
        print(f"Altura maxima: {datos['altura_maxima']:.2f} m")
        print(f"Alcance de la trayectoria: {datos['alcance']:.2f} m")

class Visualizador:
    def __init__(self, sistema):
        self.sistema = sistema

    def animar(self):
        t, x, y = self.sistema.simular()
        fig, ax = plt.subplots(figsize=(8, 5))

        ax.set_xlim(0, max(np.max(x), self.sistema.objetivo_x) + 10)
        ax.set_ylim(0, max(np.max(y), self.sistema.objetivo_y) + 10)
        ax.set_title("Busqueda del angulo para golpear un objetivo")
        ax.set_xlabel("x (m)")
        ax.set_ylabel("y (m)")
        ax.grid(True)

        ax.plot(x, y, "-", label="trayectoria optimizada")
        ax.scatter(self.sistema.objetivo_x, self.sistema.objetivo_y,
                   marker="x", s=110, label="objetivo")

        punto, = ax.plot([], [], "o", markersize=9)
        texto = ax.text(0.03, 0.87, "", transform=ax.transAxes)
        angulo = np.degrees(self.sistema.angulo_optimo)

        def iniciar():
            punto.set_data([], [])
            texto.set_text("")
            return punto, texto

        def actualizar(i):
            punto.set_data([x[i]], [y[i]])
            texto.set_text(
                f"t = {t[i]:.2f} s\n"
                f"angulo = {angulo:.2f} grados\n"
                f"error = {self.sistema.error_minimo:.4f} m"
            )
            return punto, texto

        animacion = FuncAnimation(
            fig, actualizar, frames=len(t),
            init_func=iniciar, interval=35, blit=True
        )

        ax.legend()
        plt.show()
        return animacion

def main():
    velocidad_inicial = 28.0
    gravedad = 9.81
    objetivo_x = 5.0
    objetivo_y = 14.0

    proyectil = Proyectil(velocidad_inicial, gravedad)
    sistema = LanzamientoParabolico(proyectil, objetivo_x, objetivo_y)

    sistema.simular()
    Analizador(sistema).mostrar()
    Visualizador(sistema).animar()

if __name__ == "__main__":
    main()
