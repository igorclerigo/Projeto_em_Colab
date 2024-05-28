import dearpygui.dearpygui as dpg
def fechar_sistema():
    dpg.stop_dearpygui()

dpg.create_context()
def conversao():
    opcao = dpg.get_value("opcao")
    temperatura = dpg.get_value("temperatura")
    

    try:
        opcao = int(opcao)
        temperatura = float(temperatura)

        if opcao == 1:
            resultado = temperatura + 273
            dpg.set_value("resultado", f"O valor informado em Celsius valerá {resultado} em Kelvin!")
        elif opcao == 2:
            resultado = temperatura - 273
            dpg.set_value("resultado", f"O valor informado em Kelvin valerá {resultado} em Celsius!")
        elif opcao == 3:
            resultado = temperatura * 1.8 + 32
            dpg.set_value("resultado", f"O valor informado em Celsius valerá {resultado} em Fahrenheit!")
        else:
            dpg.set_value("resultado", "Erro de cálculo!")

    except ValueError:
        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Sistema de conversão de escalas termométricas', width=700, height=300)

with dpg.window(label="Conversão de temperatura", width=700, height=300):
    dpg.add_text("Qual a opção vc quer \nCelsius para Kelvin Digite = 1 \nKelvin para Celsius Digite = 2 \nCelcius para Fahrenheit Digite = 3")
    dpg.add_input_text(label="Informe a opção desejada:", tag="opcao")
    dpg.add_input_text(label="Informe a temperatura:", tag="temperatura")
    dpg.add_button(label="Converter medidas", callback=conversao)
    dpg.add_button(label="Sair", callback=fechar_sistema)
    dpg.add_text("", tag="resultado")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


