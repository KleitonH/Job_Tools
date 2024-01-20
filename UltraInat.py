
from email.mime import text 
import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo 
import re # Importação da biblioteca re para modificação de strings
import pickle # Importação da biblioteca pickle para salvar arquivos
from pyscreeze import screenshot # Importação da biblioteca pyscreeze para captura de tela
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
tempo_de_execucao = 40000 # Tempo de execução máximo da operação 

# Carrega as listas caso existam arquivos salvos, caso contrário, cria listas predeterminadas
try:  # Tenta abrir o arquivo de lista de LATARIAS
    with open('lista_latarias.pkl', 'rb') as f: 
        lista_latarias = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_latarias = ["ALMA", "ALOJAMENTO FAROL", "ANTI-RUIDO", "ASSOALHO", "BACIA CAIXA ESTEPE", "BANDEJA CABECOTE", "BASE(FUNDO)", "BICO CAPO", "BRACO DO CAPO", "CABECOTE MONTADO", "CAIXA AR", "CAIXA DE AR", "CAPO DIANT", "CARCACA LANTERNA", "CHAPA", "CHAPEU NAPOLEAO", "CHURRASQUEIRA", "CURVAO TRAS", "DOBRADICA", "EMENDA", "ESTRIBO", "FECHAMENTO", "FRISO LATERAL", "FUNDO (REMENDO)", "GRADE", "LONGARINA", "LONG DIANT", "MECANISMO TRILHO", "MEIA LATERAL DIANT", "MEIO ASSOALHO", "MEIO PAINEL DIANT", "MOLDURA ACABAMENTO", "MOLDURA REVESTIMENTO", "PAINEL DIANT", "PAINEL TRAS", "PARALAMA", "PÉ COLUNA", "PONTA (REMENDO)", "PONTA LATERAL", "PONTA PARALAMA", "PONTEIRA ESCAPAMENTO", "PORTA DIANT", "PORTA TRAS", "PORTINHOLA TANQUE", "PROTETOR INT", "QUADRO SUSPEN", "REFORCO", "REMENDO", "REVESTIMENTO INT LAT", "REVESTIMENTO RADIADOR", "SAIA", "SUPORTE DIANT", "SUPORTE ESTEPE", "SUPORTE FIXAR", "SUPORTE FORRACAO", "SUPORTE INTERNO", "SUPORTE LATERAL", "SUPORTE PARACHOQUE", "SUPORTE RADIADOR", "SUPORTE TRAS", "TAMPA (CHAPA)", "TAMPA BARRA TORCAO", "TAMPA CACAMBA", "TAMPA FACAO", "TAMPA TRAS", "TRAVESSA", "TRILHO"]
try:  # Tenta abrir o arquivo de lista de ALIMENTOS
    with open('lista_alimentos.pkl', 'rb') as f: 
        lista_alimentos = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_alimentos = ["PICOLE", "CHICLETE", "SALGADINHO", "BOMBOM", "BALA FREEGELLS", "BARRA CHOCOLATE", "WAFER", "PIPOCA", "YOKITOS", "BATATA", "BALA DE GOMA", "AMENDOIM JAPONES", "PACOQUINHA", "SORVETE", "TRENTO", "PIRULITO", "BISCOITO", "TORTUGUITA", "COOKIES", "CEREAL BARRA", "BARRA CEREAL", "BIS LACTA", "AGUA MINERAL", "REFRIGERANTE", "SUCO"]

try: # Tenta abrir o arquivo de lista de MECANICA
    with open('lista_mecanica.pkl', 'rb') as f:
        lista_mecanica = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_mecanica = ["ACOPLAMENTO BARRA CAMB", "ADAPTADOR TAMPA TANQ", "BARRA AXIAL", "BOIA COMB", "HELICE", "JOGO JUNTA", "JUNTA ANEL", "JUNTA CABECOTE", "JUNTA CAMBIO", "JUNTA COLETOR", "JUNTA MOTOR", "JUNTA RETIFICA", "PIVO SUSPENSAO", "SUPORTE BRACO TENSOR", "TERMINAL CAIXA CAMB", "TERMINAL DIRECAO", "TUBO ABASTECIMENTO"]

try: # Tenta abrir o arquivo de lista de PLASTICOS
    with open('lista_plasticos.pkl', 'rb') as f:
        lista_plasticos = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_plasticos = ["BASE MACANETA", "BORBOLETA CIL IGNIC", "GUIA MACANETA", "DESCANSA BRACO", "ENCOSTO TRINCO", "ENCOSTO BATENTE", "GUARNICAO(ACABAMENTO)", "GRAMPO", "FAROL", "SUPORTE INTERNO PUXADOR", "MANIVELA VIDRO", "SAIDA AR PAINEL", "ESPELHO MACANETA", "TAMPA TANQUE", "CALCO BORRACHA", "BORRACHA", "LANTERNA DIANT", "LANTERNA TRAS", "CONTRACAPA TELECOMANDO", "GUIA LAT VIDRO","ALCA TETO", "PUXADOR PORTA", "PUXAD INT", "PUXADOR VIDRO", "ESPELHO(MOLDURA)", "TAMPA RESERV", "TAMPA CAPA VENTIL", "BOLA CAMBIO", "TAMPA OLEO", "TAMPA PROTETORA AMORT", "MANIVELA REGULADORA", "MANOPLA FREIO MAO", "SUPORTE MACANETA", "PARACHOQUE", "PRESILHA CALHA", "CALCO MACANETA", "CALCO MACANETA PORTA", "APOIA BRACO", "MOLDURA MACANETA", "MOLDURA ESPELHO"]

try: # Tenta abrir o arquivo de lista de ELÉTRICA
    with open('lista_eletrica.pkl', 'rb') as f:
        lista_eletrica = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_eletrica = ["ANTENA/MODULO", "BOTAO", "CABO ANTENA", "CILINDRO IGNICAO", "COMUTADOR IGNICAO", "INTERRUPTOR IGNICAO", "TRAVA ELETRICA"]
 
try: # Tenta abrir o arquivo de lista de ESCAPAMENTOS
    with open('lista_escapamentos.pkl', 'rb') as f:
        lista_escapamentos = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_escapamentos = ["PONTEIRA ESCAPAMENTO"]

try: # Tenta abrir o arquivo de lista de FERRAGENS
    with open('lista_ferragens.pkl', 'rb') as f:
        lista_ferragens = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_ferragens = ["ALAVANCA ABERTURA", "ALAVANCA CAPO", "AMORTECEDOR", "ARO VIDRO", "ARRUELA", "BATENTE", "BATENTE AMORTECEDOR", "BATENTE FECHADURA PORTA", "BATENTE FECHO TAMPA", "BATENTE INF", "BATENTE PORTA", "BATENTE GUIA DA PORTA", "BATENTE GUIA DA TAMPA", "BATENTE BARRA PRESSAO", "BATENTE BORRACHA CHUPETINHA", "BATENTE TAMPA", "BUCHA DOBRADICA", "BUCHA MACANETA", "BUCHA TRILHO", "CABO ACION", "CABO CAPO", "CABO LIMITADOR", "CABO DESTRAVA PORTA", "CABO MACANETA EXT", "CABO FECH", "CABO FECHADURA PORTA", "CABO TAMPA TRAS", "CABO TAMPA CACAMBA", "CHAPA BATENTE PORTA", "CONJUNTO BATENTE", "CONJUNTO CILINDRO", "CONJUNTO MACANETA", "COMANDO MACANETA", "CILINDRO INTERNO BAU", "CILINDRO MALA", "CILINDRO PORTA", "CILINDRO TAMPA", "CILINDRO (BOTAO)", "DISPOSITIVO TRAVA BANCO", "FECHADURA", "FECHO CILINDRO PORTA", "FECHO CINTO", "FECHO PORTA", "FECHO/TRINCO", "FIXADOR TRINCO", "GANCHO", "GATILHO MACANETA", "GUIA INT PORTA", "GUIA PORTA", "GUIA VIDRO", "HASTE FECHADURA", "JOGO CILINDRO MACANETA", "JG CILINDRO", "KIT ADAPTACAO MOTOR", "KIT CILINDRO", "KIT FIXADOR", "KIT MACANETA", "KIT PARAF", "LIMITADOR PORTA", "MACANETA DIANT", "MACANETA EXT", "MACANETA EXTERNA", "MACANETA INT", "MAQUINA DE VIDRO", "MAQUINA VIDRO", "MOTOR MAQ VIDRO", "MOTOR MAQUINA VIDRO", "PALHETA", "PARAFUSO", "PEDAL ACELERADOR", "PINO BATENTE", "PINO DO CAPO", "PINO SUPORTE", "PINO TRAVA", "PORCA", "PRESILHA FECH", "QUADRO PORTA", "ROLDANA MAQUINA DE VIDRO", "ROLDANA MAQUINA VIDRO", "SUPORTE CAPO", "SUPORTE LAT VIDRO", "SUPORTE VIDRO", "TAMPA RADIADOR", "TIRANTE CORDA", "TIRANTE TAMPA", "TRAVA DIR", "TRAVA IGNICAO", "TRAVA SEGURANCA PORTA", "TRAVA TAMPA CACAMBA", "TRINCO BASC", "TRINCO BASE LAT", "TRINCO CROMADO", "TRINCO FIXADOR", "TRINCO JANELA", "TRINCO QUEBRA VENTO", "TRINCO VIDRO", "VARETA ACIONAMENTO", "VARETA TRAVA"]

try: # Tenta abrir o arquivo de lista de VIDROS
    with open('lista_vidros.pkl', 'rb') as f:
        lista_vidros = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_vidros = ["VENTAROLA", "VIDRO PORTA", "VIDRO TRAS"]

try:  # Tenta abrir o arquivo de lista de ACESSÓRIOS
    with open('lista_acessorios.pkl', 'rb') as f: 
        lista_acessorios = pickle.load(f)
except FileNotFoundError: # Caso o arquivo não exista, cria uma lista padrão
    lista_acessorios = ["ESPACADOR", "KIT FIXADOR PARACHOQUE", "PARACHOQUE IMPULSAO", "TRAVA VOLANTE", "TRIANGULO SEGURANCA"]

todas_secoes = [lista_latarias, lista_alimentos, lista_mecanica, lista_plasticos, lista_eletrica,
                lista_escapamentos, lista_ferragens, lista_vidros, lista_acessorios]

print("---------------------------------------------------------------------------------------")
print("Bem-vindo ao UltraInat, o programa que inativa e classifica seções de itens no sistema.") # Mensagem de boas vindas
option = "" # Variável que receberá a opção selecionada
while option != "4":
    print("Para começar, analise a opção desejada: \n 1 - Iniciar inativação e classificação \n 2 - Adicionar item regra \n 3 - Remover item de regra \n 4 - Sair do programa") # Mensagem de seleção de opções
    option = input("Digite o número da opção desejada: ") # Input para seleção de opção
    if option == "1": # Se a opção for 1, inicia a operação
        print("_____________________________________________________________________________")
        print("Iniciando operação de inativação e classificação de itens em 5 segundos...") # Mensagem de início de operação
        time.sleep(1) # Intervalo de 1 segundo
        print("4 segundos...")
        time.sleep(1)
        print("3 segundos...")
        time.sleep(1)
        print("2 segundos...")
        time.sleep(1)
        print("1 segundo...")
        time.sleep(1)
        print("Iniciando operação...") # Mensagem de início de operação
        tempo_inicial = time.time() # Regra para definir o período de tempo
        contadorinativos = 0 # Variável que receberá o número de itens inativados na operação
        contadorverificados = -1 # Variável que define a quantidade de itens verificados, começa com -1 pois o loop inicia adicionando 1 a contagem
        while(time.time() - tempo_inicial) < tempo_de_execucao: # Loop de execução enquanto o contador de tempo estiver ativo
            contadorverificados += 1 # Adiciona uma verificação para o ciclo, aumentado o contador de itens verificados
            print(f"_______________________________")
            print(f"Número de verificações: {contadorverificados}") # Exibe a quantidade de verificações feitas
            print(f'Número de itens inativados : {contadorinativos}') # Apresenta na tela a quantidade de itens que foram inativados
            screenshotwatcher = pyautogui.screenshot(region=(38, 22, 150, 45)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotwatcher = screenshotwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotwatcher.save('screenshotwatcher.png') # Salva a captura com o nome do arquivo .png dado
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotwatcher = Image.open('screenshotwatcher.png') # A variável recebe o arquivo de imagem dado
            textwatcher = pytesseract.image_to_string(screenshotwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            watch = 'Livre' # Define uma palavra-chave que deve ser encontrada no conjunto de textos convertidos
            watch2 = 'campos' # Define uma segunda palavra-chave
            time.sleep(1) # Tempo de operação para segurança

            if watch in textwatcher or watch2 in textwatcher: # Se a palavra-chave 1 ou 2 estiverem no texto
                time.sleep(0.3) # Intervalo de segurança
                screenshotcod = pyautogui.screenshot(region=(37, 743.5, 59, 15)) # Variável para receber código da célula do item da tabela
                screenshotcod = screenshotcod.convert("L")  # Converte para escala de cinza
                screenshotcod.save('screenshotcod.png') # Salva a imagem

                from PIL import Image # Interpretação de imagem
                screenshootcod = Image.open('screenshotcod.png') # Recebimento da imagem
                textcod = pytesseract.image_to_string(screenshotcod) # Converte para texto
                time.sleep(2) # Intervalo
                pyautogui.click(559, 873) # Clica na posição do ícone da barra de tarefas do sistema
                time.sleep(0.9) 
                pyautogui.click(470, 809) # Clica na outra aba de sistema aberta
                time.sleep(1)

                screenshotwatcher2 = pyautogui.screenshot(region=(77, 769, 280, 25)) # Segundo método de verificação, segue a mesma lógica do primeiro, buscando outras palavras. Garante que esteja na tela correta de operação
                screenshotwatcher2 = screenshotwatcher2.convert("L") # Converte para escala de cinza
                screenshotwatcher2.save('screenshotwatcher2.png') # Salva a imagem
                from PIL import Image # Interpretação de imagem
                screenshotwatcher2 = Image.open('screenshotwatcher2.png') # Recebimento da imagem
                textwatcher2 = pytesseract.image_to_string(screenshotwatcher2) # Converte para texto
                watch3 = "sistan" # Palavra-chave
                time.sleep(0.5) # Intervalo de segurança

                if watch3 in textwatcher2: # Se a palavra-chave estiver no texto
                    time.sleep(0.5) # Intervalo de segurança
                    pyautogui.press("f5") # Pressiona a tecla F5 para atualizar a tela
                    time.sleep(0.5) # Intervalo de segurança
                    pyautogui.typewrite(textcod) # Digita o código do item
                    time.sleep(1) # Intervalo de segurança
                    
                    screenshoterror = pyautogui.screenshot(region=(680, 402, 235, 60)) # Observa s ehouve um erro de identificação de registro
                    screenshoterror = screenshoterror.convert("L") # Converte para escala de cinza
                    screenshoterror.save('screenshoterror.png') # Salva a imagem
                    from PIL import Image # Interpretação de imagem 
                    screenshooterror = Image.open('screenshoterror.png') # Recebimento da imagem
                    texterror = pytesseract.image_to_string(screenshoterror) # Converte para texto
                    errorname = 'registro' # Palavra-chave de erro

                    if errorname in texterror: # Se a palavra-chave estiver no texto
                        pyautogui.click(790, 486) # Clica no botão de fechar o erro
                        time.sleep(0.8) # Intervalo de segurança
                        pyautogui.press("esc") # Pressiona a tecla ESC, fechando a aba de procura
                        time.sleep(0.5) # Intervalo de segurança
                        pass
                    else: # Se não houver erro
                        time.sleep(1) # Intervalo de segurança
                        pyautogui.press("enter") # Clica no item encontrado
                        time.sleep(0.2)
                        pyautogui.press("enter") # Clica no item na lista de similares, caso haja
                        time.sleep(0.8) # Intervalo de segurança
                        pyautogui.click(403, 190) # Clica na aba de Histórico de Movimentações
                        time.sleep(1.3) # Intervalo de segurança
                        screenshotdate = pyautogui.screenshot(region=(195, 510, 56, 17)) # Captura a data do total de modificações de entrada do item no último ano
                        screenshotdate = screenshotdate.convert("L")  # Converte para escala de cinza
                        screenshotdate.save('screenshotdate.png') # Salva a imagem
                        from PIL import Image # Interpretação de imagem
                        screenshootdate = Image.open('screenshotdate.png') # Recebimento da imagem
                        textdate = pytesseract.image_to_string(screenshotdate) # Converte para texto
                        screenshotdate2 = pyautogui.screenshot(region=(385, 510, 56, 17)) # Captura a data do total de modificações de entrada de devoluções do item no último ano
                        screenshotdate2 = screenshotdate2.convert("L")  # Converte para escala de cinza
                        screenshotdate2.save('screenshotdate2.png') # Salva a imagem
                        from PIL import Image # Interpretação de imagem
                        screenshootdate2 = Image.open('screenshotdate2.png') # Recebimento da imagem
                        textdate2 = pytesseract.image_to_string(screenshotdate2) # Converte para texto
                        padrao_numerico = r'\b\d+\.\d+|\b[0-9]+\b' # Define um padrão de busca de números, neste caso, para converter a string da imagem em um número na próxima etapa
                        numeros_textdate = [float(match.group()) for match in re.finditer(padrao_numerico, textdate)] # Converte a string em um número
                        numeros_textdate2 = [float(match.group()) for match in re.finditer(padrao_numerico, textdate2)] # Converte a string em um número
                        time.sleep(1) # Intervalo de segurança
                        
                        if any(numero >= 1 for numero in numeros_textdate) or any(numero >= 1 for numero in numeros_textdate2): # Se o número for maior ou igual a 1, houve movimentação, não sendo necessária a inativação
                            pyautogui.press("esc") # Visto que não houve inativação, pressiona a tecla ESC para fechar a aba do item
                            time.sleep(0.2)
                            pyautogui.press("esc") # Pressiona a tecla ESC novamente para fechar a aba de procura
                            time.sleep(0.5) # Intervalo de segurança
                        else:  # Se o número for menor que 1, não houve movimentação, sendo necessária a inativação
                            pyautogui.press("esc") # Pressiona a tecla ESC para fechar a aba do item
                            time.sleep(0.2)
                            pyautogui.press("esc") # Pressiona a tecla ESC novamente para fechar a aba de procura
                            time.sleep(0.5) # Intervalo de segurança
                            pyautogui.press("f3") # Pressiona a tecla F3 para abrir a aba de procura de item com modificação de estoque
                            time.sleep(0.5) # Intervalo de segurança
                            pyautogui.typewrite(textcod) # Digita o código do item
                            time.sleep(0.8) # Intervalo de segurança
                            pyautogui.press("enter") # Clica no item encontrado
                            time.sleep(0.2) # Intervalo de segurança
                            pyautogui.press("enter") # Clica no item na lista de similares, caso haja
                            time.sleep(1) # Intervalo de segurança
                            pyautogui.click(945, 566) # Clica em inativar
                            time.sleep(0.5) # Intervalo de segurança
                            pyautogui.click(650, 660) # Clica em gravar
                            time.sleep(0.5) # Intervalo de segurança
                            screenshoterror2 = pyautogui.screenshot(region=(450, 371, 692, 141)) # Captura a mensagem de erro de inativação, neste caso, se o item já estiver inativo ou se há duplicação de código de barra, o que bloqueia inativação
                            screenshoterror2 = screenshoterror2.convert("L")  # Converte para escala de cinza
                            screenshoterror2.save('screenshoterror2.png') # Salva a imagem
                            from PIL import Image # Interpretação de imagem
                            screenshoterror2 = Image.open('screenshoterror2.png') # Recebimento da imagem
                            texterror2 = pytesseract.image_to_string(screenshoterror2) # Converte para texto
                            errorname2 = "inativar" # Palavra-chave de erro caso esteja inativo
                            errorname3 = "nativo" # Palavra-chave de erro caso esteja inativo
                            errorname4 = "duplicado"  # Palavra-chave de erro caso haja duplicação de código de barra
                            
                            if errorname2 in texterror2 or errorname3 in texterror2 or errorname4 in texterror2: # Caso ocorrer os erros citados acima
                                pyautogui.click(802, 483) # Clica no botão de fechar o erro
                                time.sleep(0.6) # Intervalo de segurança
                                pyautogui.press("esc") # Pressiona a tecla ESC para tentar fechar a aba do item
                                time.sleep(0.6) # Intervalo de segurança
                                pyautogui.click(744, 483) # Clica no botão para confirmar a saída do item
                                time.sleep(0.6) # Intervalo de segurança
                                pyautogui.press("esc") # Pressiona a tecla ESC para fechar a aba do item
                                time.sleep(0.6) # Intervalo de segurança
                            else:
                                pyautogui.press("esc") # Pressiona a tecla ESC para fechar a aba de procura
                                time.sleep(0.2) # Intervalo de segurança 
                                contadorinativos += 1 # Adiciona um inativo ao contador de itens inativados
                else: # Se não houver a palavra-chave 3 no texto, a qual garante que a janela esteja limpa para a modificação do próximo item
                    exit() # Sai do programa

                pyautogui.click(559, 883) # Clica na posição do ícone da barra de tarefas do sistema
                time.sleep(0.5) # Intervalo de segurança
                pyautogui.click(674, 809) # Clica na outra aba de sistema aberta da lista de item
                time.sleep(1.5) # Intervalo de segurança
                
                screenshotdesc = pyautogui.screenshot(region=(276, 743.5, 458, 15)) # Captura a descrição do item
                screenshotdesc = screenshotdesc.convert("L")  # Converte para escala de cinza
                screenshotdesc.save('screenshotdesc.png') # Salva a imagem
                from PIL import Image
                screenshotdesc = Image.open('screenshotdesc.png') # Recebimento da imagem
                textdesc = pytesseract.image_to_string(screenshotdesc) # Converte para texto

                secaoescolhida = "" # Variável que receberá a seção escolhida
                itemescolhido = 0 # Variável que receberá o tamanho escolhido
                for secao_lista in todas_secoes:
                    for item in secao_lista:
                        if item in textdesc:
                            if len(item) > itemescolhido:
                                itemescolhido = len(item)
                                # Obter o nome da seção com base na lista atual
                                secaoescolhida = todas_secoes.index(secao_lista)
                                secaoescolhida = ["latarias", "alimentos", "mecanica", "plasticos", "eletrica", "escapamentos",
                                "ferragens", "vidros", "acessorios"][secaoescolhida]

                if secaoescolhida:
                    if secaoescolhida == "latarias": # Se a seção escolhida for latarias
                        pyautogui.typewrite('5039')
                    elif secaoescolhida == "alimentos": # Se a seção escolhida for alimentos 
                        pyautogui.typewrite('5042')
                    elif secaoescolhida == "mecanica": # Se a seção escolhida for mecânica 
                        pyautogui.typewrite('5048')
                    elif secaoescolhida == "plasticos": # Se a seção escolhida for plásticos
                        pyautogui.typewrite('5049')
                    elif secaoescolhida == "eletrica": # Se a seção escolhida for elétrica
                        pyautogui.typewrite('5058')
                    elif secaoescolhida == "escapamentos": # Se a seção escolhida for escapamentos 
                        pyautogui.typewrite('5062')
                    elif secaoescolhida == "ferragens": # Se a seção escolhida for ferragens 
                        pyautogui.typewrite('5066')
                    elif secaoescolhida == "vidros": # Se a seção escolhida for vidros 
                        pyautogui.typewrite('5059')
                    elif secaoescolhida == "acessorios": # Se a seção escolhida for vidros 
                        pyautogui.typewrite('5060')
                time.sleep(0.3) # Intervalo de segurança
                pyautogui.press("down") # Pressiona a tecla de seta para baixo passando para o próximo item de modificação
            else:
                exit()
    elif option == "2": # Se a opção for 2, inicia a operação de adição de item
        print("________________________________________________________________________________________")
        print("Você selecionou a opção de adicionar item regra.\n Primeiro, insira o nome do item.") # Mensagem de seleção de opção
        nome_item = input("Nome do item: ").upper() # Input para seleção de item a ser adicionado na lista de regras inserindo sempre com letras maiúsculas
        print("Agora, insira a qual seção ele pertence: \n 1 - Latarias \n 2 - Alimentos \n 3 - Mecânica \n 4 - Plásticos \n 5 - Elétrica \n 6 - Escapamentos \n 7 - Ferragens \n 8 - Vidros \n 9 - Acessórios") # Mensagem de seleção de opção
        secao_item = input("Seção do item: ") # Input para seleção de seção do item
        if int(secao_item) == 1: # Se a seção for 1, adiciona o item na lista de latarias
            lista_latarias.append(nome_item.upper)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 2: # Se a seção for 2, adiciona o item na lista de alimentos
            lista_alimentos.append(nome_item.upper)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 3: # Se a seção for 3, adiciona o item na lista de mecânica
            lista_mecanica.append(nome_item)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 4: # Se a seção for 4, adiciona o item na lista de plásticos
            lista_plasticos.append(nome_item)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 5: # Se a seção for 5, adiciona o item na lista de elétrica
            lista_eletrica.append(nome_item)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 6: # Se a seção for 6, adiciona o item na lista de escapamentos 
            lista_escapamentos.append(nome_item)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 7: # Se a seção for 7, adiciona o item na lista de ferragens
            lista_ferragens.append(nome_item)
        elif int(secao_item) == 8: # Se a seção for 8, adiciona o item na lista de vidros
            lista_vidros.append(nome_item)
        elif int(secao_item) == 9: # Se a seção for 8, adiciona o item na lista de vidros
            lista_acessorios.append(nome_item)

            print("Item adicionado com sucesso.")
        else:
            print("Opção inválida.")

    elif option == "3": # Se a opção for 3, inicia a operação de remoção de item
        print("Você selecionou a opção de remover item regra.\n Primeiro, insira o nome do item.")
        nome_item = input("Nome do item: ").upper() # Input para seleção de item a ser removido da lista de regras buscando sempre com letras maiúsculas    
        print("Agora, insira a qual seção ele pertence: \n 1 - Latarias \n 2 - Alimentos \n 3 - Mecânica \n 4 - Plásticos \n 5 - Elétrica \n 6 - Escapamentos \n 7 - Ferragens \n 8 - Vidros \n 9 - Acessórios")
        secao_item = input("Seção do item: ")
        if secao_item == 1:
            lista_latarias.remove(nome_item) # Remove o item da lista de latarias
        elif secao_item == 2:
            lista_alimentos.remove(nome_item) # Remove o item da lista de alimentos
        elif secao_item == 3:
            lista_mecanica.remove(nome_item) # Remove o item da lista de mecânica 
        elif secao_item == 4:
            lista_plasticos.remove(nome_item) # Remove o item da lista de plásticos
        elif secao_item == 5:
            lista_eletrica.remove(nome_item) # Remove o item da lista de elétrica
        elif secao_item == 6:
            lista_escapamentos.remove(nome_item) # Remove o item da lista de escapamentos 
        elif secao_item == 7:
            lista_ferragens.remove(nome_item) # Remove o item da lista de ferragens
        elif secao_item == 8:
            lista_vidros.remove(nome_item) # Remove o item da lista de ferragens
        elif secao_item == 9:
            lista_acessorios.remove(nome_item) # Remove o item da lista de ferragens
        else:
            print("Opção inválida.")
    
    elif option == "4": # Se a opção for 4, sai do programa
        print("Saindo do programa...") # Mensagem de saída
        break # Quebra o loop

# Salva os arquivos ao final do programa, encontra-se em fase de testes
with open('lista_latarias.pkl', 'wb') as f: 
        pickle.dump(lista_latarias, f)
with open('lista_alimentos.pkl', 'wb') as f:
        pickle.dump(lista_alimentos, f)
with open('lista_mecanica.pkl', 'wb') as f:
        pickle.dump(lista_mecanica, f)
with open('lista_plasticos.pkl', 'wb') as f:
        pickle.dump(lista_plasticos, f)
with open('lista_eletrica.pkl', 'wb') as f:
        pickle.dump(lista_eletrica, f)
with open('lista_escapamentos.pkl', 'wb') as f:
        pickle.dump(lista_escapamentos, f)
with open('lista_ferragens.pkl', 'wb') as f:
        pickle.dump(lista_ferragens, f)
