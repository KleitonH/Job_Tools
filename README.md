# Job_Tools 🔨
## Repositório dedicado aos algoritmos de Python para automatizar tarefas. <br> Todos os algoritmos utilizam estruturas em python com implementação de bibliotecas externas, fundamentalmente, se baseia em pyautogui com complementares de auxílio como o <b>Tesseract OCR</b>.

Em suma, os algoritmos criados estão encarregados de realizarem tarefas específicas, todas direcionadas à correção gerencial do estoque.

_Algumas váriaveis, como as terminadas em 'watcher' ou 'error', servem para aumentar a segurança de operação. Como o computador que executa o algoritmo é o mesmo que possui o sistema, a troca de janelas de aplicativos e o manuseio de informações importantes ocorre a todo instante; sendo necessárias, então, medidas preventivas._
<hr>
Seguem os algoritmos criados:

- **apitrello**: Algoritmos pertencentes à pasta apitrello servem para modificar um quadro na plataforma Trello, assim, implementando as listas da classificação de itens.
- **BrandRepairer**: Utiliza o menu "Alteração em massa de produtos" para redefinir uma marca em outra, ambas definidas dentro das especificações.
- **Breaker**: Possui a função de módulo de interrupção, seus métodos podem ser inseridos em outros algoritmos para encerrar uma tarefa em execução com o comando ALT + K.
- **LostSale**: Utiliza o menu de consulta de vendas perdidas para agrupar todos os itens que se repetiram em um único dia. Assim que é identificada uma repetição, o algoritmo transfere a ocorrência para uma planilha em excel. (Alguns pequenos erros de transcrição ainda passam, talvez aperfeiçoar ainda mais os filtros resolva, ou uma atualização do Tesseract. Os erros são pouco relevantes com um método de consulta do item em paralelo à operação).
- **OutputBlocker**: Alguns produtos só podem terem uma venda com um valor mínimo de saldo, dessa forma, ele automatiza o processo. Ele é uma extensão de outros algoritmos, ou seja, ele ajusta a seção do item, inativa caso necessário e adiciona a saída mínima, necessário que os itens estejam em ordem. Pode ser melhorado para inativar um grupo seleto de itens em uma lista diversificada.
- **PositionTools**: Conjunto de algoritmos voltados ao desenvolvimento. Serve para encontrar as posições do ponteiro do mouse para posterior aplicação em código.
- **SectionGroups**: Algoritmo para classificação de grupos e subgrupos. Serve para classificar uma seção inteira do estoque por meio de dicionários em python. Como um dos últimos algoritmos-ferramenta criado, ele possui uma organização melhorada com uso de funções e serve como molde para cadastros futuros depois da correção completa da seção.
- **SectionRepairer**: Corrige a seção do item com base em sua descrição. Muito útil para corrigir padrões de itens indevidamente colocados em uma seção.
- **SimpleAutomation**: Possui a função de modificar completamente uma seção para outra, como possui padrões fixos, é recomendado apenas para seções pequenas ou de características muito similares entre os produtos que as pertencem.
- **UltraInat**: Algoritmo pioneiro desse conjunto de ferramentas. Possui o objetivo de classificar a seção de um item e inativá-lo caso esteja sem uma movimentação maior/igual a um ano. Utiliza bibliotecas de automação de controle, conversão de imagem em texto e conversão para padrões númericos. Vários padrões desse algoritmo foram utilizados nos demais, principalmente o OutputBlocker. Caso queira entender o funcionamento das demais ferramentas, recomendo começar por aqui, visto que está completamente comentado para compreendimento geral.
<hr>
