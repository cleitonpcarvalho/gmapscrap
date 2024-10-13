import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        # Set background color for the whole window
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Light gray background

        # Customize the label for niche search
        self.label = Label(text="Qual nicho deseja pesquisar:", size_hint=(None, None), height=30, color=(0, 0, 0, 1), font_size=18)
        self.label.width = 300
        self.label.size_hint_x = None
        self.label.pos_hint = {'center_x': 0.5}
        self.add_widget(self.label)

        # Input for keyword with rounded corners and narrow width
        self.palavra_chave_input = TextInput(
            multiline=False,
            size_hint=(None, None),
            width=300,
            height=40,
            background_normal='',
            background_color=(1, 1, 1, 1),  # White background
            foreground_color=(0, 0, 0, 1),  # Black text
            padding=(10, 10),
            hint_text="Digite a palavra-chave"
        )
        self.palavra_chave_input.pos_hint = {'center_x': 0.5}
        self.add_widget(self.palavra_chave_input)

        # Label for quantity search
        self.label_qtd = Label(text="Quantas buscas deseja fazer:", size_hint=(None, None), height=30, color=(0, 0, 0, 1), font_size=18)
        self.label_qtd.width = 300
        self.label_qtd.size_hint_x = None
        self.label_qtd.pos_hint = {'center_x': 0.5}
        self.add_widget(self.label_qtd)

        # Input for quantity of searches, also with narrow width
        self.qtd_input = TextInput(
            multiline=False,
            size_hint=(None, None),
            width=100,
            height=40,
            background_normal='',
            background_color=(1, 1, 1, 1),  # White background
            foreground_color=(0, 0, 0, 1),  # Black text
            padding=(10, 10),
            hint_text="Digite o número",
            input_filter='int'  # Allows only numbers
        )
        self.qtd_input.pos_hint = {'center_x': 0.5}
        self.add_widget(self.qtd_input)

        # Run button with visual effects and rounded corners, narrower
        self.btn_run = Button(
            text="Iniciar Busca",
            size_hint=(None, None),
            width=200,
            height=50,
            background_normal='',
            background_color=(0.3, 0.6, 0.3, 1),  # Green button
            color=(1, 1, 1, 1),  # White text
            font_size=18
        )
        self.btn_run.pos_hint = {'center_x': 0.5}
        self.btn_run.bind(on_press=self.start_search)
        self.add_widget(self.btn_run)

        # Apply rounded corners to the button
        with self.btn_run.canvas.before:
            Color(0.3, 0.6, 0.3, 1)
            self.rect = RoundedRectangle(size=self.btn_run.size, pos=self.btn_run.pos, radius=[20])

        self.btn_run.bind(size=self.update_rect, pos=self.update_rect)

        # Output label
        self.output_label = Label(text="", size_hint=(None, None), height=40, width=300, color=(0, 0, 0, 1))
        self.output_label.size_hint_x = None
        self.output_label.pos_hint = {'center_x': 0.5}
        self.add_widget(self.output_label)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def start_search(self, instance):
        # Obtém os valores do campo de entrada
        palavrachave = self.palavra_chave_input.text
        qtd = self.qtd_input.text

        # Verifica se os campos estão preenchidos
        if not palavrachave:
            self.output_label.text = "Por favor, insira uma palavra-chave."
            return

        if not qtd or int(qtd) <= 0:
            self.output_label.text = "Por favor, insira um número válido de buscas."
            return

        # Inicia uma thread para executar a busca
        threading.Thread(target=self.run_search, args=(palavrachave, int(qtd))).start()

    def run_search(self, palavrachave, qtd):
        # Chama a função para executar o script de coleta de dados
        self.output_label.text = "Iniciando a busca..."
        os.system(f'python script.py "{palavrachave}" {qtd}')

        # Após a busca, abre o diálogo para salvar o arquivo
        self.open_save_dialog()

    def open_save_dialog(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 title="Salvar Planilha",
                                                 filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            messagebox.showinfo("Sucesso", f"Planilha salva em: {file_path}")

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
