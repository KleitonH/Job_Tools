# Job_Tools
Repositório dedicado aos algoritmos de Python para automatizar tarefas
Todos os algoritmos utilizam estruturas em python com implementação de bibliotecas externas, fundamentalmente, se baseia em pyautogui com complementares de auxílio como o Tesseract OCR.

Em suma, os algoritmos criados estão encarregados de realizarem tarefas específicas, todas direcionadas à correção gerencial do estoque.

Algumas váriaveis, como as terminadas em 'watcher' ou 'error', servem para aumentar a segurança de operação. Como o computador que executa o algoritmo é o mesmo que possui o sistema, a troca de janelas de aplicativos e o manuseio de informações importantes ocorre a todo instante; sendo necessárias, então, medidas preventivas.

Seguem os algoritmos criados:
    BrandRepairer: Utiliza o menu "Alteração em massa de produtos" para redefinir uma marca em outra, ambas definidas dentro das especificações.

    OutputBlocker: Alguns produtos só podem terem uma venda com um valor mínimo de saldo, dessa forma, ele automatiza o processo. Ele é uma extensão de outros algoritmos, ou seja, ele ajusta a seção do item, inativa caso necessário e adiciona a saída mínima, necessário que os itens estejam em ordem. Pode ser melhorado para inativar um grupo seleto de itens em uma lista diversificada.

    Position: Um algoritmo de desenvolvimento. Serve para encontrar as posições do ponteiro do mouse para posterior aplicação em código.

    SectionGroups: Algoritmo para classificação de grupos e subgrupos. Serve para classificar uma seção inteira do estoque por meio de dicionários em python. Como um dos últimos algoritmos-ferramenta criado, ele possui uma organização melhorada com uso de funções e serve como molde para cadastros futuros depois da correção completa da seção.

    SectionRepairer: Corrige a seção do item com base em sua descrição. Muito útil para corrigir padrões de itens indevidamente colocados em uma seção.

    SimpleAutomation: Possui a função de modificar completamente uma seção para outra, como possui padrões fixos, é recomendado apenas para seções pequenas ou de características muito similares entre os produtos que as pertencem.

    UltraInat: Algoritmo pioneiro desse conjunto de ferramentas. Possui o objetivo de classificar a seção de um item e inativá-lo caso esteja sem uma movimentação maior/igual a um ano. Utiliza bibliotecas de automação de controle, conversão de imagem em texto e conversão para padrões númericos. Vários padrões desse algoritmo foram utilizados nos demais, principalmente o OutputBlocker. Caso queira entender o funcionamento das demais ferramentas, recomendo começar por aqui, visto que está completamente comentado para compreendimento geral.

    Breaker possui a função de módulo de interrupção, seus métodos podem ser inseridos em outros algoritmos para encerrar uma tarefa em execução com o comando ALT + K