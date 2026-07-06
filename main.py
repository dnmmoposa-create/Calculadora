from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Configurar el tamaño de la ventana para pruebas en PC (opcional)
Window.size = (350, 520)

class CalculadoraApp(App):
    def build(self):
        self.title = "Calculadora"
        
        # Layout Principal (Vertical: Pantalla arriba, Botones abajo)
        layout_principal = BoxLayout(orientation='vertical', spacing=10, padding=15)
        # Fondo ultra oscuro (convertido de #171c1c a valores 0-1)
        Window.clearcolor = (0.09, 0.11, 0.11, 1)

        # ---------------- Pantalla ----------------
        self.pantalla = TextInput(
            font_size=36,
            readonly=True,
            halign='right',
            multiline=False,
            background_color=(0.11, 0.14, 0.14, 1), # #1d2424
            foreground_color=(1, 1, 1, 1),          # Blanco
            size_hint_y=0.2,
            padding=[10, 20, 10, 10]
        )
        layout_principal.add_widget(self.pantalla)

        # ---------------- Contenedor de Botones ----------------
        # Usamos un BoxLayout horizontal para separar los números de la barra del "="
        layout_inferior = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.8)

        # Cuadrícula para los botones normales (4 columnas)
        cuadrilla = GridLayout(cols=4, spacing=8, size_hint_x=0.8)

        # Definición de los botones (Fila por fila)
        botones = [
            "C", "/", "*", "-",
            "7", "8", "9", "+",
            "4", "5", "6", ".",
            "1", "2", "3", "0"
        ]

        for texto in botones:
            # Asignar colores según el tipo de botón
            if texto in ["/", "*", "-", "+"]:
                bg_color = (0.95, 0.61, 0.07, 1)  # Naranja #f39c12
            elif texto == "C":
                bg_color = (0.75, 0.22, 0.17, 1)  # Rojo #c0392b
            else:
                bg_color = (0.17, 0.22, 0.22, 1)  # Gris #2d3838

            btn = Button(
                text=texto,
                font_size=22,
                bold=True,
                background_normal='',  # Permite cambiar el color de fondo plano
                background_color=bg_color,
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.al_presionar_boton)
            cuadrilla.add_widget(btn)

        layout_inferior.add_widget(cuadrilla)

        # Botón "=" vertical a la derecha (abarca el alto de la botonera)
        btn_igual = Button(
            text="=",
            font_size=24,
            bold=True,
            background_normal='',
            background_color=(0.15, 0.68, 0.37, 1), # Verde #27ae60
            color=(1, 1, 1, 1),
            size_hint_x=0.2
        )
        btn_igual.bind(on_press=self.al_presionar_boton)
        layout_inferior.add_widget(btn_igual)

        layout_principal.add_widget(layout_inferior)
        return layout_principal

    # ---------------- Lógica de la Calculadora ----------------
    def al_presionar_boton(self, instancia):
        texto_boton = instancia.text
        texto_actual = self.pantalla.text

        if texto_boton == "C":
            self.pantalla.text = ""
        elif texto_boton == "=":
            try:
                # Reemplazar símbolos si es necesario y evaluar
                resultado = eval(texto_actual)
                # Evitar decimales flotantes limpios (ej: 5.0 -> 5)
                if isinstance(resultado, float) and resultado.is_integer():
                    resultado = int(resultado)
                self.pantalla.text = str(resultado)
            except Exception:
                self.pantalla.text = "Error"
        else:
            # Si hay un "Error" previo en pantalla, lo limpia antes de escribir
            if texto_actual == "Error":
                texto_actual = ""
            self.pantalla.text = texto_actual + texto_boton

if __name__ == '__main__':
    CalculadoraApp().run()
