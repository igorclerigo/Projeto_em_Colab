# Sistema de conversão de Escalas Termométricas

# Importando biblioteca externa do Python
import dearpygui.dearpygui as dpg

# Cria um contexto para Dear PyGui, que é necessário para iniciar qualquer aplicação usando esta biblioteca
dpg.create_context()

# Definição de função

# Informar opção para determinar condição

def conversao():
    opcao = dpg.get_value("opcao")
    temperatura = dpg.get_value("temperatura")
    

    try:
        opcao = int(opcao)
        temperatura = float(temperatura)

        # Transforma a temperatura informada em Celsius para Kelvin
        if opcao == 1:
            resultado = temperatura + 273
            dpg.set_value("resultado", f"O valor informado em Celsius valerá {resultado} em Kelvin!")
        elif opcao == 2:
            resultado = temperatura - 273
            dpg.set_value("resultado", f"O valor informado em Kelvin valerá {resultado} em Celsius!")
        else:
            # Define uma mensagem de erro se os valores inseridos não puderem ser convertidos para numéricos
            dpg.set_value("resultado", "Erro de cálculo!")

    except ValueError:
        # Define uma mensagem de erro se os valores inseridos não puderem ser convertidos para numéricos
        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

# Cria uma janela para visualização da aplicação com um título e dimensões definidas
dpg.create_viewport(title='Sistema de conversão de escalas termométricas', width=700, height=300)

# Define a janela principal onde os elementos da interface serão colocados
with dpg.window(label="Conversão de temperatura", width=700, height=300):
    # Adiciona um campo de texto para o usuário inserir o preço FIPE
    dpg.add_input_text(label="Informe a opção desejada:", tag="opcao")
    # Adiciona um campo de texto para o usuário inserir a nota de avaliação
    dpg.add_input_text(label="Informe a temperatura:", tag="temperatura")
    # Adiciona um botão que, quando clicado, chama a função 'calcular_preco'
    dpg.add_button(label="Converter medidas", callback=conversao)
    # Adiciona um espaço para exibir o resultado ou mensagens de erro
    dpg.add_text("", tag="resultado")

# Configura e mostra a janela
dpg.setup_dearpygui()
dpg.show_viewport()
# Inicia o loop de eventos da interface, onde a aplicação efetivamente roda e espera por interações do usuário
dpg.start_dearpygui()
# Destroi o contexto da aplicação após o fechamento da janela, liberando recursos
dpg.destroy_context()



