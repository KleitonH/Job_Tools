
from email.mime import text 
import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo 
import re # Importação da biblioteca re para modificação de strings
import pickle # Importação da biblioteca pickle para salvar arquivos (Em análise)
import Breaker
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
tempo_de_execucao = 40000 # Tempo de execução máximo da operação 

lista_latarias = ["ALMA", "ALOJAMENTO FAROL", "ANTI-RUIDO", "ASSOALHO", "BACIA CAIXA ESTEPE", "BANDEJA CABECOTE", "BASE(FUNDO)", "BICO CAPO", "BRACO DO CAPO", "CABECOTE MONTADO", "CAIXA AR", "CAIXA DE AR", "CAPO DIANT", "CARCACA LANTERNA", "CHAPA", "CHAPEU NAPOLEAO", "CHURRASQUEIRA", "CURVAO TRAS", "DOBRADICA", "EMENDA", "ESTRIBO", "FECHAMENTO", "FRISO LATERAL", "FUNDO (REMENDO)", "GRADE", "LONGARINA", "LONG DIANT", "MECANISMO TRILHO", "MEIA LATERAL DIANT", "MEIO ASSOALHO", "MEIO PAINEL DIANT", "MOLDURA ACABAMENTO", "MOLDURA REVESTIMENTO", "PAINEL DIANT", "PAINEL TRAS", "PARALAMA", "PÉ COLUNA", "PONTA (REMENDO)", "PONTA LATERAL", "PONTA PARALAMA", "PONTEIRA ESCAPAMENTO", "PORTA DIANT", "PORTA TRAS", "PORTINHOLA TANQUE", "PROTETOR INT", "QUADRO SUSPEN", "REFORCO", "REMENDO", "REVESTIMENTO INT LAT", "REVESTIMENTO RADIADOR", "SAIA", "SUPORTE DIANT", "SUPORTE ESTEPE", "SUPORTE FIXAR", "SUPORTE FORRACAO", "SUPORTE INTERNO", "SUPORTE LATERAL", "SUPORTE PARACHOQUE", "SUPORTE RADIADOR", "SUPORTE TRAS", "TAMPA (CHAPA)", "TAMPA BARRA TORCAO", "TAMPA CACAMBA", "TAMPA FACAO", "TAMPA TRAS", "TRAVESSA", "TRILHO"]
lista_alimentos = ["PICOLE", "CHICLETE", "SALGADINHO", "BOMBOM", "BALA FREEGELLS", "BARRA CHOCOLATE", "WAFER", "PIPOCA", "YOKITOS", "BATATA", "BALA DE GOMA", "AMENDOIM JAPONES", "PACOQUINHA", "SORVETE", "TRENTO", "PIRULITO", "BISCOITO", "TORTUGUITA", "COOKIES", "CEREAL BARRA", "BARRA CEREAL", "BIS LACTA", "AGUA MINERAL", "REFRIGERANTE", "SUCO"]
lista_mecanica = ['AMORTECEDOR', 'AMORTECEDOR DIANT', 'ANEIS PISTAO', 'ANEL BUJAO','CONJUNTO EMBREAGEM COMPRESSOR', 'MAGNETICO COMPRESSOR','BRUCUTU', 'BUCHA BOMBA ESGUICHO', 'KIT CAVALETE DISTR AGUA', 'PRESILHA FIX SUPORTE RADIADOR', 'SUPORTE COXIM RADIADOR','BUCHA RADIADOR', 'BUCHA BOMBA ESGUICHO', 'BUCHA RESERVATORIO GAS PARTIDA','RADIADOR', 'RADIADOR AGUA','BOMBA AGUA', 'BOMBA D.HIDR', 'BOMBA DAGUA','CABO ACIONADOR PORTINHOLA', 'CABO AR FORCADO', 'CABO PORTA CORRER', 'CABO PORTA MALA', 'CABO PORTINHOLA', 'CABO TEMPERATURA', 'PARAFUSO QUEBRA GALHO CABO ACELERADOR', 'SUPORTE CABO EMBREAGEM', 'SUPORTE CABO', 'TAMPA PORTINHOLA','CABO ACEL', 'CABO ACELERADO', 'CABO DE ACELERADOR', 'CABO PARADA MOTOR','CABO EMB', 'CABO EMBR', 'CABO EMBREAGE', 'CABO FLEX EMBR', 'CABO TRANSMISSAO', 'FLEXIVEL EMBREAGEM','CABO DE FREIO', 'CABO FREIO', 'CABO LIBERACAO FREIO','CABO CAPO', 'CABO PUXADOR CAPO', 'CABO ABERTURA CAPO','CABO DE VELOCIMETRO', 'CABO TACOGRAFO', 'CABO TACOMETRO', 'CABO VELOCIMETRO', 'CABO VELOC','CABO LIMITADOR DA TAMPA TRAS', 'CABO PUXADOR TAMPA', 'CABO TAMPA TRAS', 'CABO LIMITADOR TAMPA','CABO AFOGADOR', 'CABO ESTRANGULADOR','CABO CAMBIO', 'CABO COMANDO', 'CABO COMANDO MARCHA', 'CABO ENGATE COMANDO', 'CABO ENGATE', 'CABO ENGATE MARCHA', 'CABO MARCHA', 'CABO REDUZIDA', 'CABO SELECAO CAMBIO', 'CABO SELECAO MARCHA', 'CABO SELECAO COMANDO','CABO COMANDO FECHADURA', 'CABO FECHADURA', 'HASTE CABO FECHADURA', 'HASTE FECHADURA','CABO ACION MACANETA', 'CABO ACO LIGACAO MACANETA', 'CABO DESTRAVA PORTA', 'CABO MACANETA','CABO MAQUINA VIDRO','CABO TRAVA BANCO','TERMINAL CABO COMANDO', 'TERMINAL CABO ENGATE', 'TERMINAL CABO MARCHA', 'TERMINAL CABO SELECAO','AVANCO DISTRIBUIDOR', 'BOIA CARBURADOR', 'AFOGADOR', 'AVANCO DO DISTRIBUIDOR', 'CONJUNTO VALVULA BOIA CARBURADOR', 'EIXO CARBURADOR', 'KIT POSICIONADOR AFOGADOR', 'PARAFUSO MISTURADOR REGULAGEM', 'PORTA GICLE MARCHA CARBURADOR', "SAPATILHA CAME DEFOGADOR CARBURADOR",'CARBURADOR', 'KIT CARBURADOR',"AGULHA CARBURADOR", 'BASE CARB', 'BASE CARBURADOR', 'BASE VEDACAO CARB', 'BENGALA CARB', 'BENGALA INJETOR CARBURAD', 'BORBOLETA CARBURADOR', 'ESGUICHO CARB', 'GICLE CARBURADOR', 'HASTE CARBURADOR', 'ESGUICHO CARBURADOR', 'ESPACADOR BASE CARB',  'FILTRO DIFUSOR SECUNDARIO', 'PISTAO ANEL MOTOR', 'PISTAO REPARO PINCA', 'PISTAO CARBURADOR','DIAFRAGMA CARBURADO', 'DIAFRAGMA ACELERA','PORCA FLANGE COMB', 'PROTETOR CALOR CAIXA AR', 'VENTURI CARBURADOR', 'PARAFUSO OCO TUBO','ANTICHAMA', 'ANTI CHAMA', 'DEFLETOR ANTICHAMA','CAVALETE', 'FLANGE CAVALETE AGUA','TUBO ABASTECIMENTO', 'TUBO RESPIRO', 'TUBO AGUA', 'TUBO AR PAINEL', 'TUBO CILINDRO', 'TUBO CIRCULACAO AGUA', 'TUBO COLETOR', 'TUBO CIRCULACAO', 'TUBO COLETOR', 'TUBO COMBUSTIVEL', 'TUBO CONEXAO', 'TUBO DISTRIBUIDOR', 'TUBO FLANGE', 'TUBO FLUXO AGUA', 'TUBO GARGALO', 'TUBO LIGACAO', 'TUBO MANGUEIRA', 'TUBO MISTURADOR CARBURADOR', 'TUBO MOTOR', 'TUBO RADIADOR', 'TUBO REFRIGERACAO', 'TUBO RETORNO', 'TUBO SUPERIOR', 'TUBO VENTILACAO', 'TUBO CONEXAO BOMBA', 'TUBO CANO EMBREAGEM', 'TUBO CORRUGADO BOMBA', 'TUBO MANGUEIRA DIRECAO', 'TUBO MANGUEIRA TANQUE','CONECTOR LIGACAO MANGUEIRA', 'CONECTOR MANGUEIRA', 'CONECTOR 3/8', 'CONECTOR AGUA', 'CONECTOR CAMB', 'CONECTOR DUPLO UNIVE', 'CONECTOR GASOLINA', 'CONECTOR QUICK', 'CONECTOR SELADO', 'CONECTOR UNIVERSAL', 'CONEXAO RESERVATORIO', 'CONEXAO AGUA', 'CONEXAO CARC VALV', 'CONEXAO COM REGISTRO', 'CONEXAO DUPLA MANG', 'CONEXAO ESGUICHO', 'CONEXAO INF', 'CONEXAO MANG', 'CONEXAO RAPIDA', 'CONEXAO RADIADOR', 'CONEXAO Y DUPLO', 'EMENDA CONEXAO','CONEXAO (COTOVELO)', 'COTOVELO', 'COTOVELO CAVALETE','CAPA CORREIA', 'JOGO PROTETOR CORREIA', 'KIT CAPA PROTETOR CORREIA', 'KIT CAPA CORREIA', 'KIT PROTETOR CORREIA', 'PROTETOR CORREIA','CARCACA', 'CAIXA FILTRO AR', 'CAIXA FILTRO AR CARB', 'CAMARA VALVULA TERMOS','FLANGE  MOTOR', 'FLANGE MANG CABECOTE', 'FLANGE AGUA', 'FLANGE BOMBA DAGUA', 'FLANGE CONEXAO', 'FLANGE ROLAMENTO CAIXA CAMBIO', 'FLANGE SEMI EIXO', 'FLANGE TERMOSTATO', 'FLAGE TUBO MANGUEIRA', 'FLANGE VALV TERMOST',"ADAPTADOR TAMPA TANQUE", 'BORRACHA FLANGE COM', 'CANO COMBUSTIVEL', 'PORCA TAMPA BOMBA COMB',"ADAPTADOR FLANGE CAIXA", "FLANGE", 'FLANGE COMBUSTIVEL', 'FLANGE MODULO COMBUSTIVEL','TANQUE COMBUSTIVEL','CORREIA VENTOINHA', 'KIT CORREIA E TENSOR', 'PARAFUSO TENSOR CORREIA','CORREIA COMANDO', 'CORREIA DENTADA', 'KIT CORREIA COM', 'KIT CORREIA COMANDO','CORREIA ALT', 'CORREIA ALTERNADOR', 'CORREIA AR COND', 'CORREIA MICRO V', 'CORREIA POLY V', 'CORREIA MULTI V', 'KIT CORREIA VIRABREQUIM','CORREIA EM V', 'CORREIA EM V AR COND', 'CORREIA EM V ALT',"ADAPTADOR VOLANTE", 'BORRACHA FIXADORA CAIXA DIRE', 'BORRACHA']
lista_plasticos = ["BASE MACANETA", "BORBOLETA CIL IGNIC", "GUIA MACANETA", "DESCANSA BRACO", "ENCOSTO TRINCO", "ENCOSTO BATENTE", "GUARNICAO(ACABAMENTO)", "GRAMPO", "FAROL", "SUPORTE INTERNO PUXADOR", "MANIVELA VIDRO", "SAIDA AR PAINEL", "ESPELHO MACANETA", "TAMPA TANQUE", "CALCO BORRACHA", "BORRACHA", "LANTERNA DIANT", "LANTERNA TRAS", "CONTRACAPA TELECOMANDO", "GUIA LAT VIDRO","ALCA TETO", "PUXADOR PORTA", "PUXAD INT", "PUXADOR VIDRO", "ESPELHO(MOLDURA)", "TAMPA RESERV", "TAMPA CAPA VENTIL", "BOLA CAMBIO", "TAMPA OLEO", "TAMPA PROTETORA AMORT", "MANIVELA REGULADORA", "MANOPLA FREIO MAO", "SUPORTE MACANETA", "PARACHOQUE", "PRESILHA CALHA", "CALCO MACANETA", "CALCO MACANETA PORTA", "APOIA BRACO", "MOLDURA MACANETA", "MOLDURA ESPELHO"]
lista_eletrica = ['ALTERNADOR', 'BOMBA VACUO', 'PARAFUSO ALTERNADOR', 'SUPORTE ESCOVA ALTERNADOR', 'TRIODO', 'TRIODO ALTERNADOR', 'TRIODO EXCITACAO ALTERNADOR', 'SUPORTE ALTERNADOR', 'CONJUNTO RETIFICADOR', 'DIODO PLACA EXITADORA', 'PLACA DIODO ALTERNADOR', 'PLACA RETIFICADORA', 'RETIFICADOR', 'ESCOVA', 'ESCOVA DINAMO', 'ESCOVA ALTERNADOR', 'ESCOVA ARRANQUE', 'JOGO ESCOVA MOTOR', 'PORTA ESCOVA', 'ESTATOR', 'MANCAL', 'MANCAL ALTERNADOR', 'ROTOR', 'ROTOR DISTRIBUIDOR','ANTENA', 'ANTENA ESTAGIO', 'ANTENA INTERNA', 'ANTENA TETO', 'CONVERSOR RCA','AUTOMATICO', 'AUTOMATICO PARTIDA', 'BENDIX','BUZINA', 'SIRENE ELETRONICA','CABO (FIO) 16MM PARA POSITIVO', 'CABO BATERIA', 'CABO CONTROLE AR PAINEL', 'CABO NEGATIVO', 'CABO PARALELO SOM', 'CABO PONTE BATERIA', 'CABO RCA 5 METROS', 'CABO/CHUPETA', 'CAPA TERMINAL FIO FEMEA', 'EMENDA FIO', 'FIO INSTAL', 'ILHO PASSAGEM FIACAO', 'PASSA FIO', 'PORCA FIACAO','ADAPTADOR LAMPADA H5 PARA H1', 'ADAPTADOR LAMPADA', 'CIRCUITO LANTERNA', 'CIRCUITO SOQUETE LANTERNA', 'PAR CIRCUITO LANTERNA', 'KIT LAMPADA H4', 'LAMPADA ASSIMETRICA', 'LAMPADA H5', 'LAMPADA H1', 'LAMPADA H11', 'LAMAPADA H13', 'LAMPADA H16', 'LAMPADA H27', 'LAMPADA H3', 'LAMPADA H4', 'LAMPADA H7', 'LAMPADA H8', 'LAMPADA HB1', 'LAMPADA HB3', 'LAMPADA HB4', 'LAMPADA HIR2', 'LAMPADA 1 POLO', 'LAMPADA 2 POLO', 'LAMPADA 69', 'LAMPADA BASE VIDRO', 'LAMPADA T67', 'LAMPADA T5', 'LAMPADA MINI', 'LAMPADA PAINEL', 'LAMPADA PINGAO', 'LAMPADA PINGO', 'LAMPADA TORPEDO', 'LAMPADA PISCA AMARELO', 'LAMPADA T315', 'KIT LAMPADA H4 LED', 'LAMPADA H5 LED', 'LAMPADA H1 LED', 'LAMPADA H11 LED', 'LAMAPADA H13 LED', 'LAMPADA H16 LED', 'LAMPADA H27 LED', 'LAMPADA H3 LED', 'LAMPADA H4 LED', 'LAMPADA H7 LED', 'LAMPADA H8 LED', 'LAMPADA HB1 LED', 'LAMPADA HB3 LED', 'LAMPADA HB4 LED', 'LAMPADA HIR2 LED', 'KIT LAMPADA LED PINGO', 'LAMPADA 1 E 2 POLO LED', 'LAMPADA 1 LED', 'LAMPADA 1 POLO LED', 'LAMPADA 13 LEDS', 'LAMPADA 2 LEDS', 'LAMPADA 2 POLO LED', 'LAMPADA LED SILICONE', 'LAMPADA LED', 'LAMPADA LEDS', 'LAMPADA ESMAGADA LED', 'LAMPADA PAINEL LED', 'LAMPADA PINGAO LED', 'LAMPADA PINGO LED', 'LAMPADA TORPEDO LED', 'SOQUETE', 'SOQUETE CIRCUITO', 'SOQUETE FAROL', 'SOQUETE LAMPADA 2 POLOS', 'SOQUETE GLOBO', 'SOQUETE LAMPADA', 'SOQUETE LAMPADA PINGO', 'SOQUETE LANTERNA', 'SOQUETE LANTERNA DIANTEIRA', 'SOQUETE LISO', 'SOQUETE MEIA LUZ', 'SOQUETE METAL', 'SOQUETE MIRIM', 'SOQUETE PAINEL', 'SOQUETE PINGO', 'SOQUETE PISCA', 'SOQUETE UNIVERSAL','FILTRO BICO', 'FILTRO BICO INJETOR', 'FILTRO BICO ANEIS', 'FLAUTA INJE', 'KIT FLAUTA INJECAO', 'BICO INJETOR', 'KIT BICO INJETOR','SUPORTE SENSOR', 'INTERRUPTOR DE EMBREAGEM', 'INTERRUPTOR DE FREIO', 'INTERRUPTOR DIRECAO HIDRAULICA', 'INTERRUPTOR PRESSAO OLEO', 'INTERRUPTOR LUZ FREIO', 'INTERRUPTOR LUZ RE', 'INTERRUPTOR OLEO', 'INTERRUPTOR PARTIDA FRIO', 'INTERRUPTOR PEDAL', 'INTERRUPTOR RADIADOR', 'INTERRUPTOR RE', 'INTERRUPTOR REDUZIDA', 'INTERRUPTOR REGULAGEM', 'INTERRUPTOR RELE', 'INTERRUPTOR TEMPERATURA', 'INTERRUPTOR VENTILADOR', 'INTERRUPTOR LUZ', 'INTERRUPTOR DUPLO LUZ', 'INTERRUPTOR MOTOR', 'INTERRUPTOR SENSOR', 'MEDIDOR FLUXO AR', 'MEDIDOR MASSA AR', 'SENSOR FLUXO AR', 'SENSOR ABS', 'SENSOR', 'SENSOR AR CONDICIONADO', 'SENSOR BOIA COMBUSTIVEL', 'SENSOR BORBOLETA', 'SENSOR NIVEL', 'SENSOR POSICAO ARVORE', 'SENSOR ROTACAO', 'SENSOR VELOCIDADE', 'SENSOR DESGASTE PASTILHA', 'SENSOR DETONACAO', 'SENSOR FASE', 'SENSOR FLUXO AR', 'SENSOR HALL', 'SENSOR MAP', 'SENSOR NIVEL', 'SENSOR PARTIDA', 'SENSOR PASTILHA', 'SENSOR POSICAO BORBOLETA', 'SENSOR POSICAO PEDAL', 'SENSOR PRESSAO', 'SENSOR ROTACAO', 'SENSOR TEMPERATURA', 'SENSOR VELOCIDADE', 'SONDA LAMBDA','ESTABILIZADOR PAINEL', 'ESTABILIZADOR VOLTAGEM', 'MINI RELE', 'PRESSOSTATO', 'RELE LAMPADA FLUORESCENTE', 'RELE', 'RELE AUXILIAR', 'RELE BUZINA', 'RELE VIDRO ELETRICO', 'RELE AVISO', 'RELE AR CONDICIONADO', 'RELE BOMBA', 'RELE BOMBA COMBUSTIVEL', 'RELE BOMBA INJECAO', 'RELE BUZINA UNIVERSAL', 'RELE COMANDO INJECAO ELETRONICA', 'RELE COMANDO PISCA', 'RELE DE INJECAO', 'RELE DESEMBACADOR', 'RELE DUPLO AUXILIAR', 'RELE DUPLO INJECAO', 'RELE ELETRONICO', 'RELE FAROL', 'RELE INJECAO', 'RELE ENGATE', 'RELE LIMPADOR', 'RELE MONITOR', 'RELE PARTIDA FRIO', 'RELE PISCA', 'RELE TEMPERATURA', 'RELE TEMPORIZADOR', 'RELE TEMPORIZADOR LIMPADOR', 'RELE UNIVERSAL', 'RELE VENTILADOR RADIADOR', 'RELE VENTOINHA RADIADOR', 'RELE VIDRO ELETRICO','BOTAO CIGARRO', 'BOTAO BUZINA', 'BOTAO DESLIZANTE', 'BOTAO ESGUICHO/LIMPADOR']
lista_escapamentos = ["PONTEIRA ESCAPAMENTO"]
lista_ferragens = ["ALAVANCA ABERTURA", "ALAVANCA CAPO", "AMORTECEDOR TAMPA", "ARO VIDRO", "ARRUELA", "BATENTE", "BATENTE AMORTECEDOR", "BATENTE FECHADURA PORTA", "BATENTE FECHO TAMPA", "BATENTE INF", "BATENTE PORTA", "BATENTE GUIA DA PORTA", "BATENTE GUIA DA TAMPA", "BATENTE BARRA PRESSAO", "BATENTE BORRACHA CHUPETINHA", "BATENTE TAMPA", "BUCHA DOBRADICA", "BUCHA MACANETA", "BUCHA TRILHO", "CABO ACION", "CABO CAPO", "CABO LIMITADOR", "CABO DESTRAVA PORTA", "CABO MACANETA EXT", "CABO FECH", "CABO FECHADURA PORTA", "CABO TAMPA TRAS", "CABO TAMPA CACAMBA", "CHAPA BATENTE PORTA", "CONJUNTO BATENTE", "CONJUNTO CILINDRO", "CONJUNTO MACANETA", "COMANDO MACANETA", "CILINDRO INTERNO BAU", "CILINDRO MALA", "CILINDRO PORTA", "CILINDRO TAMPA", "CILINDRO (BOTAO)", "DISPOSITIVO TRAVA BANCO", "FECHADURA", "FECHO CILINDRO PORTA", "FECHO CINTO", "FECHO PORTA", "FECHO/TRINCO", "FIXADOR TRINCO", "GANCHO", "GATILHO MACANETA", "GUIA INT PORTA", "GUIA PORTA", "GUIA VIDRO", "HASTE FECHADURA", "JOGO CILINDRO MACANETA", "JG CILINDRO", "KIT ADAPTACAO MOTOR", "KIT CILINDRO", "KIT FIXADOR", "KIT MACANETA", "KIT PARAF", "LIMITADOR PORTA", "MACANETA DIANT", "MACANETA EXT", "MACANETA EXTERNA", "MACANETA INT", "MAQUINA DE VIDRO", "MAQUINA VIDRO", "MOTOR MAQ VIDRO", "MOTOR MAQUINA VIDRO", "PALHETA", "PARAFUSO", "PEDAL ACELERADOR", "PINO BATENTE", "PINO DO CAPO", "PINO SUPORTE", "PINO TRAVA", "PORCA", "PRESILHA FECH", "QUADRO PORTA", "ROLDANA MAQUINA DE VIDRO", "ROLDANA MAQUINA VIDRO", "SUPORTE CAPO", "SUPORTE LAT VIDRO", "SUPORTE VIDRO", "TAMPA RADIADOR", "TIRANTE CORDA", "TIRANTE TAMPA", "TRAVA DIR", "TRAVA IGNICAO", "TRAVA SEGURANCA PORTA", "TRAVA TAMPA CACAMBA", "TRINCO BASC", "TRINCO BASE LAT", "TRINCO CROMADO", "TRINCO FIXADOR", "TRINCO JANELA", "TRINCO QUEBRA VENTO", "TRINCO VIDRO", "VARETA ACIONAMENTO", "VARETA TRAVA"]
lista_vidros = ["VENTAROLA", "VIDRO PORTA", "VIDRO TRAS"]
lista_acessorios = ["ESPACADOR", "KIT FIXADOR PARACHOQUE", "PARACHOQUE IMPULSAO", "TRAVA VOLANTE", "TRIANGULO SEGURANCA"]

todas_secoes = [lista_latarias, lista_alimentos, lista_mecanica, lista_plasticos, lista_eletrica,
                lista_escapamentos, lista_ferragens, lista_vidros, lista_acessorios]

print("---------------------------------------------------------------------------------------")
print("Bem-vindo ao UltraInat, o programa que inativa e classifica seções de itens no sistema.") # Mensagem de boas vindas
option = "" # Variável que receberá a opção selecionada
while option != "2":
    print("Para começar, analise a opção desejada: \n 1 - Iniciar inativação e classificação \n 2 - Sair do programa") # Mensagem de seleção de opções
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
        monitor_thread = Breaker.iniciar_monitoramento()
        while(time.time() - tempo_inicial) < tempo_de_execucao and Breaker.verificar_interrupcao(): # Loop de execução enquanto o contador de tempo estiver ativo
            contadorverificados += 1 # Adiciona uma verificação para o ciclo, aumentado o contador de itens verificados
            print(f"_______________________________")
            print(f"Número de verificações: {contadorverificados}") # Exibe a quantidade de verificações feitas
            print(f'Número de itens inativados : {contadorinativos}') # Apresenta na tela a quantidade de itens que foram inativados
            screenshotwatcher = pyautogui.screenshot(region=(38, 22, 150, 45)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotwatcher = screenshotwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotwatcher.save('./screenshots/screenshotwatcher.png') # Salva a captura com o nome do arquivo .png dado
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotwatcher = Image.open('./screenshots/screenshotwatcher.png') # A variável recebe o arquivo de imagem dado
            textwatcher = pytesseract.image_to_string(screenshotwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            watch = 'Livre' # Define uma palavra-chave que deve ser encontrada no conjunto de textos convertidos
            watch2 = 'campos' # Define uma segunda palavra-chave
            time.sleep(1) # Tempo de operação para segurança

            if watch in textwatcher or watch2 in textwatcher: # Se a palavra-chave 1 ou 2 estiverem no texto
                if not Breaker.verificar_interrupcao():
                    exit()
                time.sleep(0.3) # Intervalo de segurança
                screenshotcod = pyautogui.screenshot(region=(36, 614, 59, 17)) # Variável para receber código da célula do item da tabela
                screenshotcod = screenshotcod.convert("L")  # Converte para escala de cinza
                screenshotcod.save('./screenshots/screenshotcod.png') # Salva a imagem

                from PIL import Image # Interpretação de imagem
                screenshootcod = Image.open('./screenshots/screenshotcod.png') # Recebimento da imagem
                textcod = pytesseract.image_to_string(screenshotcod) # Converte para texto
                clean_textcod = re.sub(r'[@,!#.]', '', textcod) #Limpa qualquer algarismo indesejado interpretado pelo Tesseract
                time.sleep(2) # Intervalo
                pyautogui.click(443, 742) # Clica na posição do ícone da barra de tarefas do sistema
                time.sleep(0.9) 
                pyautogui.click(329, 703) # Clica na outra aba de sistema aberta
                time.sleep(1)

                screenshotwatcher2 = pyautogui.screenshot(region=(77, 630, 280, 25)) # Segundo método de verificação, segue a mesma lógica do primeiro, buscando outras palavras. Garante que esteja na tela correta de operação
                screenshotwatcher2 = screenshotwatcher2.convert("L") # Converte para escala de cinza
                screenshotwatcher2.save('./screenshots/screenshotwatcher2.png') # Salva a imagem
                from PIL import Image # Interpretação de imagem
                screenshotwatcher2 = Image.open('./screenshots/screenshotwatcher2.png') # Recebimento da imagem
                textwatcher2 = pytesseract.image_to_string(screenshotwatcher2) # Converte para texto
                watch3 = "sistnias" # Palavra-chave
                time.sleep(0.5) # Intervalo de segurança
                # print (textwatcher2)

                if watch3 in textwatcher2: # Se a palavra-chave estiver no texto
                    if not Breaker.verificar_interrupcao():
                        exit()
                    time.sleep(0.5) # Intervalo de segurança
                    pyautogui.press("f5") # Pressiona a tecla F5 para atualizar a tela
                    time.sleep(0.5) # Intervalo de segurança
                    pyautogui.typewrite(clean_textcod) # Digita o código do item
                    time.sleep(1) # Intervalo de segurança
                    
                    screenshoterror = pyautogui.screenshot(region=(507, 304, 340, 142)) # Observa se houve um erro de identificação de registro
                    screenshoterror = screenshoterror.convert("L") # Converte para escala de cinza
                    screenshoterror.save('./screenshots/screenshoterror.png') # Salva a imagem
                    from PIL import Image # Interpretação de imagem 
                    screenshooterror = Image.open('./screenshots/screenshoterror.png') # Recebimento da imagem
                    texterror = pytesseract.image_to_string(screenshoterror) # Converte para texto
                    # print(f"texterror: {texterror}")
                    errorname = 'registro' # Palavra-chave de erro

                    if errorname in texterror: # Se a palavra-chave estiver no texto
                        if not Breaker.verificar_interrupcao():
                            exit()
                        pyautogui.click(670, 419) # Clica no botão de fechar o erro
                        time.sleep(0.8) # Intervalo de segurança
                        pyautogui.press("esc") # Pressiona a tecla ESC, fechando a aba de procura
                        time.sleep(0.5) # Intervalo de segurança
                        pass
                    else: # Se não houver erro
                        if not Breaker.verificar_interrupcao():
                            exit()
                        time.sleep(1) # Intervalo de segurança
                        pyautogui.press("enter") # Clica no item encontrado
                        time.sleep(0.2)
                        pyautogui.press("enter") # Clica no item na lista de similares, caso haja
                        time.sleep(0.8) # Intervalo de segurança
                        pyautogui.click(310, 101) # Clica na aba de Histórico de Movimentações
                        time.sleep(1.3) # Intervalo de segurança
                        screenshotdate = pyautogui.screenshot(region=(118, 419, 56, 17)) # Captura a data do total de modificações de entrada do item no último ano
                        screenshotdate = screenshotdate.convert("L")  # Converte para escala de cinza
                        screenshotdate.save('./screenshots/screenshotdate.png') # Salva a imagem
                        from PIL import Image # Interpretação de imagem
                        screenshootdate = Image.open('./screenshots/screenshotdate.png') # Recebimento da imagem
                        textdate = pytesseract.image_to_string(screenshotdate) # Converte para texto
                        screenshotdate2 = pyautogui.screenshot(region=(238, 419, 56, 17)) # Captura a data do total de modificações de entrada de devoluções do item no último ano
                        screenshotdate2 = screenshotdate2.convert("L")  # Converte para escala de cinza
                        screenshotdate2.save('./screenshots/screenshotdate2.png') # Salva a imagem
                        from PIL import Image # Interpretação de imagem
                        screenshootdate2 = Image.open('./screenshots/screenshotdate2.png') # Recebimento da imagem
                        textdate2 = pytesseract.image_to_string(screenshotdate2) # Converte para texto
                        padrao_numerico = r'\b\d+\.\d+|\b[0-9]+\b' # Define um padrão de busca de números, neste caso, para converter a string da imagem em um número na próxima etapa
                        numeros_textdate = [float(match.group()) for match in re.finditer(padrao_numerico, textdate)] # Converte a string em um número
                        numeros_textdate2 = [float(match.group()) for match in re.finditer(padrao_numerico, textdate2)] # Converte a string em um número
                        time.sleep(1) # Intervalo de segurança
                        
                        if any(numero >= 1 for numero in numeros_textdate) or any(numero >= 1 for numero in numeros_textdate2): # Se o número for maior ou igual a 1, houve movimentação, não sendo necessária a inativação
                            if not Breaker.verificar_interrupcao():
                                exit()
                            pyautogui.press("esc") # Visto que não houve inativação, pressiona a tecla ESC para fechar a aba do item
                            time.sleep(0.2)
                            pyautogui.press("esc") # Pressiona a tecla ESC novamente para fechar a aba de procura
                            time.sleep(0.5) # Intervalo de segurança
                        else:  # Se o número for menor que 1, não houve movimentação, sendo necessária a inativação
                            if not Breaker.verificar_interrupcao():
                                exit()
                            pyautogui.press("esc") # Pressiona a tecla ESC para fechar a aba do item
                            time.sleep(0.2)
                            pyautogui.press("esc") # Pressiona a tecla ESC novamente para fechar a aba de procura
                            time.sleep(0.5) # Intervalo de segurança
                            pyautogui.press("f3") # Pressiona a tecla F3 para abrir a aba de procura de item com modificação de estoque
                            time.sleep(0.5) # Intervalo de segurança
                            pyautogui.typewrite(clean_textcod) # Digita o código do item
                            time.sleep(0.8) # Intervalo de segurança
                            pyautogui.press("enter") # Clica no item encontrado
                            time.sleep(0.2) # Intervalo de segurança
                            pyautogui.press("enter") # Clica no item na lista de similares, caso haja
                            time.sleep(1) # Intervalo de segurança
                        
                            screenshoterror2 = pyautogui.screenshot(region=(330, 305, 692, 141)) # Captura a mensagem de erro de inativação, neste caso, se o item já estiver inativo ou se há duplicação de código de barra, o que bloqueia a inativação
                            screenshoterror2 = screenshoterror2.convert("L")  # Converte para escala de cinza
                            screenshoterror2.save('./screenshots/screenshoterror2.png') # Salva a imagem
                            from PIL import Image # Interpretação de imagem
                            screenshoterror2 = Image.open('./screenshots/screenshoterror2.png') # Recebimento da imagem
                            texterror2 = pytesseract.image_to_string(screenshoterror2) # Converte para texto
                            errorname2 = "inativar" # Palavra-chave de erro caso esteja inativo
                            errorname3 = "nativo" # Palavra-chave de erro caso esteja inativo
                            errorname4 = "duplicado"  # Palavra-chave de erro caso haja duplicação de código de barra
                            
                            if errorname2 in texterror2 or errorname3 in texterror2 or errorname4 in texterror2 and Breaker.verificar_interrupcao: # Caso ocorrer os erros citados acima
                                if not Breaker.verificar_interrupcao():
                                    exit()
                                pyautogui.click(674, 418) # Clica no botão de fechar o erro
                                time.sleep(0.6) # Intervalo de segurança
                                pyautogui.press("esc") # Pressiona a tecla ESC para tentar fechar a aba do item
                                time.sleep(0.6) # Intervalo de segurança
                                pyautogui.click(627, 419) # Clica no botão para confirmar a saída do item
                                time.sleep(0.6) # Intervalo de segurança
                                pyautogui.press("esc") # Pressiona a tecla ESC para fechar a aba do item
                                time.sleep(0.6) # Intervalo de segurança
                            else:
                                pyautogui.click(374, 219) # Clica na caixa de código do item
                                time.sleep(0.3) # Intervalo de segurança
                                pyautogui.press("end") # acessa o final do código
                                pyautogui.typewrite("INAT") # Digita INAT para identificação do item
                                time.sleep(0.3) # Intervalo de segurança
                                pyautogui.click(365, 300) # Clica na caixa de descrição
                                time.sleep(0.3) # Intervalo de segurança
                                pyautogui.press("end") # acessa o final da descrição
                                time.sleep(0.3) # Intervalo de segurança
                                pyautogui.typewrite(" (INATIVADO)") # Digita (INATIVADO) para identificação do item
                                time.sleep(0.3) # Intervalo de segurança
                                pyautogui.click(828, 498) # Clica em inativar
                                time.sleep(0.5) # Intervalo de segurança
                                pyautogui.click(543, 595) # Clica em gravar
                                time.sleep(0.5) # Intervalo de segurança
                                pyautogui.press("esc") # Pressiona a tecla ESC para fechar a aba de procura
                                time.sleep(0.2) # Intervalo de segurança 
                                contadorinativos += 1 # Adiciona um inativo ao contador de itens inativados
                else: # Se não houver a palavra-chave 3 no texto, a qual garante que a janela esteja limpa para a modificação do próximo item
                    exit() # Sai do programa

                pyautogui.click(443, 742) # Clica na posição do ícone da barra de tarefas do sistema
                time.sleep(0.5) # Intervalo de segurança
                pyautogui.click(553, 700) # Clica na outra aba de sistema aberta da lista de item
                time.sleep(1.5) # Intervalo de segurança
                
                screenshotdesc = pyautogui.screenshot(region=(274, 614, 458, 15)) # Captura a descrição do item
                screenshotdesc = screenshotdesc.convert("L")  # Converte para escala de cinza
                screenshotdesc.save('./screenshots/screenshotdesc.png') # Salva a imagem
                from PIL import Image
                screenshotdesc = Image.open('./screenshots/screenshotdesc.png') # Recebimento da imagem
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
                
    elif option == "2": # Se a opção for 4, sai do programa
        print("Saindo do programa...") # Mensagem de saída
        exit() # Quebra o loop