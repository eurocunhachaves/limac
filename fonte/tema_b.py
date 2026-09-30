"""Tema b: Excitação rítmica do coração (Guyton & Hall, cap. 10)."""

SECTIONS = [
    ("1. O sistema excitocondutor", [
        ("fig", "fig/b_conducao.png", "fig_livro/g10_01.png", "Nó sinusal, vias internodais, nó AV, feixe AV e ramos (sistema de Purkinje).", 9),
        ("p", "Duas funções: <b>gerar</b> o impulso rítmico e <b>conduzi-lo</b> rápido. Resultado: os átrios contraem ≈ 1/6 s antes dos "
              "ventrículos, e todas as partes dos ventrículos contraem <b>quase ao mesmo tempo</b>. É um sistema sensível à isquemia."),
        ("table", [
            ["Estrutura", "Onde / como", "Detalhe que cai"],
            ["<b>Nó sinusal (SA)</b>", "Parede posterolateral superior do AD, logo abaixo e lateral à veia cava superior",
             "3 × 15 × 1 mm; fibras de 3 a 5 µm, quase sem miofibrilas; ligadas direto ao músculo atrial"],
            ["<b>Vias internodais</b>", "Anterior, média e posterior; <b>feixe de Bachmann</b> (interatrial anterior) leva ao AE",
             "≈ 1 m/s (músculo atrial comum ≈ 0,3 m/s)"],
            ["<b>Nó AV</b>", "Parede posterior do AD, atrás da valva tricúspide", "<b>Retarda</b> o impulso"],
            ["<b>Feixe AV (His)</b>", "Atravessa o esqueleto fibroso; desce 5 a 15 mm no septo", "<b>Condução unidirecional</b> (átrio → ventrículo)"],
            ["<b>Ramos e Purkinje</b>", "Ramos direito e esquerdo subendocárdicos → ápice → voltam à base; penetram 1/3 da parede",
             "Fibras grandes, <b>1,5 a 4 m/s</b>"],
        ], [3.2, 7.4, 6.8]),
    ]),
    ("2. Por que o nó sinusal dispara sozinho", [
        ("fig", "fig/b_potencial_sa.png", "fig_livro/g10_02.png", "Potencial do nó sinusal comparado com o da fibra ventricular.", 10),
        ("ul", [
            "\"Repouso\" de <b>−55 a −60 mV</b> (ventrículo: −85 a −90), porque a membrana é naturalmente permeável a <b>Na⁺ e Ca²⁺</b>.",
            "A −55 mV os <b>canais rápidos de Na⁺ estão inativados</b>: quem faz o potencial são os <b>canais de Ca²⁺ tipo L (lentos)</b>. "
            "Por isso a subida e a repolarização são lentas.",
            "Entre os batimentos, o Na⁺ entra pela <b>corrente funny</b> e o potencial sobe devagar até o <b>limiar ≈ −40 mV</b>: abrem os canais tipo L e dispara.",
            "Fim: os canais de Ca²⁺ <b>inativam em 100 a 150 ms</b> e <b>abrem canais de K⁺</b> → repolariza e <b>hiperpolariza</b>. "
            "Os canais de K⁺ vão fechando, o vazamento de Na⁺/Ca²⁺ vence de novo e o ciclo recomeça.",
        ]),
        ("box", "Resumo em uma linha",
               "<b>Vazamento de Na⁺ (funny) → limiar −40 mV → Ca²⁺ tipo L dispara → K⁺ repolariza/hiperpolariza → recomeça.</b>"),
    ]),
    ("3. Condução: onde atrasa e onde acelera", [
        ("fig", None, "fig_livro/g10_04.png", "Tempo (em segundos) de chegada do impulso a cada região do coração.", 7.5),
        ("table", [
            ["Trecho", "Tempo acumulado", "Por quê"],
            ["Nó sinusal → nó AV", "0,03 s", "Vias internodais"],
            ["Dentro do nó AV", "+0,09 s (→ 0,12 s)", "Atraso nodal"],
            ["Feixe AV penetrante", "+0,04 s (→ 0,16 s)", "Atravessa o tecido fibroso"],
            ["Ramos → fim do Purkinje", "+0,03 s (→ ≈ 0,19 s)", "Purkinje 1,5 a 4 m/s"],
            ["Endocárdio → epicárdio", "+0,03 s (→ ≈ 0,22 s)", "Músculo 0,3 a 0,5 m/s, em espiral"],
        ], [5.0, 4.6, 7.8]),
        ("box", "O que a prova cobra", [
            "<b>Atraso AV total = 0,13 s</b> no nó + feixe; somando as vias internodais, <b>0,16 s</b> até o ventrículo. Serve para o átrio esvaziar antes da sístole.",
            "Causa do atraso: <b>poucas junções comunicantes</b> entre as células do nó (alta resistência).",
            "Causa da rapidez do Purkinje: fibras <b>grossas</b> e <b>junções comunicantes muito permeáveis</b>. Velocidade ≈ 6× o músculo e ≈ 150× algumas fibras do nó AV.",
            "Dos ramos até a última fibra ventricular: <b>≈ 0,06 s</b>. Contração <b>síncrona</b>; condução lenta nos ventrículos reduz o bombeamento em 20 a 30%.",
            "A <b>barreira fibrosa</b> isola átrio de ventrículo. Uma <b>via acessória</b> que a atravesse permite <b>reentrada</b> e arritmias graves.",
        ]),
    ]),
    ("4. Hierarquia dos marca-passos", [
        ("fig", "fig/b_marcapassos.png", None, "Frequências intrínsecas de disparo.", 9),
        ("ul", [
            "Nó sinusal <b>70 a 80</b>/min · nó AV <b>40 a 60</b>/min · Purkinje <b>15 a 40</b>/min.",
            "O nó sinusal comanda porque é o <b>mais rápido</b>: descarrega o nó AV e o Purkinje antes que eles atinjam o próprio limiar.",
            "<b>Marca-passo ectópico</b>: outro local passa a disparar mais rápido que o sinusal (ou o impulso sinusal é bloqueado). Contração em sequência anormal.",
            "<b>Bloqueio AV total</b>: átrios seguem o sinusal; ventrículos passam a um ritmo do Purkinje de <b>15 a 40 bpm</b>.",
        ]),
        ("box", "Síndrome de Stokes-Adams",
               "No bloqueio AV súbito, o Purkinje estava <b>suprimido</b> pelo ritmo sinusal rápido (supressão por sobrecarga) e só assume após "
               "<b>5 a 20 s</b>. Sem bombeamento, a pessoa <b>desmaia após 4 a 5 s</b>. Se a pausa for longa, pode morrer."),
    ]),
    ("5. Controle autonômico do ritmo e da condução", [
        ("fig", "fig/b_autonomo.png", None, "Efeito do simpático e do vago no potencial do nó sinusal.", 9.5),
        ("table", [
            ["", "Parassimpático (vago)", "Simpático"],
            ["Distribuição", "<b>Nós SA e AV</b>; pouco músculo atrial; quase nada no ventrículo", "Todo o coração, forte no <b>ventrículo</b>"],
            ["Mediador", "<b>Acetilcolina</b>", "<b>Noradrenalina</b> → receptores <b>β1</b>"],
            ["Mecanismo", "↑ permeabilidade ao <b>K⁺</b> → <b>hiperpolariza</b> (SA vai a −65 a −75 mV) → demora a chegar ao limiar",
             "↑ permeabilidade a <b>Na⁺ e Ca²⁺</b> → rampa diastólica mais íngreme"],
            ["Nó sinusal", "FC ↓ (vago moderado: até metade); forte: para", "FC ↑ (máximo: quase <b>triplica</b>)"],
            ["Nó AV", "↓ excitabilidade da junção AV → atrasa; forte: <b>bloqueia</b>", "Condução AV mais rápida"],
            ["Força", "Pouco efeito", "Até <b>2×</b> (mais Ca²⁺)"],
        ], [2.8, 7.6, 7.0]),
        ("box", "Escape ventricular",
               "Com estímulo vagal muito forte o ventrículo pode parar por 5 a 20 s. Depois, um ponto do Purkinje (geralmente na porção "
               "septal do feixe AV) assume a <b>15 a 40 bpm</b>: é o <b>escape ventricular</b>."),
    ]),
]

MCQ = [
    dict(q="O potencial de membrana \"de repouso\" da fibra do nó sinusal é de cerca de −55 a −60 mV. Isso ocorre porque:",
         opts=["A Na⁺/K⁺-ATPase é mais ativa no nó sinusal",
               "A membrana das fibras nodais é naturalmente permeável a Na⁺ e Ca²⁺",
               "O nó sinusal não tem canais de K⁺",
               "A concentração extracelular de K⁺ é maior no nó sinusal",
               "As fibras nodais são maiores que as musculares"],
         a=1, c="A entrada de cargas positivas (Na⁺ e Ca²⁺) neutraliza parte da negatividade intracelular, deixando o repouso em −55 a −60 mV, "
                "contra −85 a −90 mV na fibra ventricular."),
    dict(q="Por que a fase de subida do potencial de ação do nó sinusal é lenta?",
         opts=["Porque depende de canais rápidos de Na⁺ com poucas unidades",
               "Porque os canais rápidos de Na⁺ estão inativados em −55 mV, e o potencial depende dos canais de Ca²⁺ tipo L",
               "Porque o nó sinusal não tem junções comunicantes",
               "Porque a acetilcolina bloqueia os canais de Na⁺ permanentemente",
               "Porque o limiar do nó sinusal é −90 mV"],
         a=1, c="Quando a membrana fica menos negativa que ≈ −55 mV por alguns milissegundos, as portas de inativação dos canais rápidos de "
                "Na⁺ se fecham. Sobram os canais lentos de Ca²⁺ (tipo L), que produzem um potencial de subida e descida lentas."),
    dict(q="A despolarização diastólica lenta das fibras do nó sinusal, que leva o potencial ao limiar, é causada principalmente por:",
         opts=["Saída de K⁺ por canais retificadores", "Entrada de Cl⁻", "Entrada de Na⁺ pela corrente funny",
               "Liberação de Ca²⁺ pelo retículo sarcoplasmático", "Ativação da SERCA2"],
         a=2, c="Entre os batimentos, o Na⁺ vaza para dentro pelas \"funny currents\" (com contribuição do Ca²⁺), elevando lentamente o "
                "potencial até ≈ −40 mV, quando abrem os canais de Ca²⁺ tipo L."),
    dict(q="O limiar de disparo do potencial de ação no nó sinusal é de aproximadamente:",
         opts=["−90 mV", "−70 mV", "−55 mV", "−40 mV", "0 mV"], keep=True,
         a=3, c="Quando o potencial sobe até ≈ −40 mV, os canais de Ca²⁺ tipo L se abrem e disparam o potencial de ação nodal."),
    dict(q="O que impede que as fibras do nó sinusal fiquem despolarizadas o tempo todo?",
         opts=["O fechamento das junções comunicantes",
               "A inativação dos canais de Ca²⁺ tipo L em 100 a 150 ms e a abertura de canais de K⁺",
               "A ação contínua da acetilcolina",
               "A entrada de Cl⁻ no fim do potencial",
               "A ausência de canais funny"],
         a=1, c="Os canais tipo L se inativam em 100 a 150 ms e, ao mesmo tempo, abre-se um grande número de canais de K⁺. A saída de K⁺ "
                "repolariza e até hiperpolariza a fibra; depois esses canais fecham aos poucos e o ciclo recomeça."),
    dict(q="O nó sinusal localiza-se:",
         opts=["No septo interventricular",
               "Na parede posterior do átrio direito, atrás da valva tricúspide",
               "Na parede posterolateral superior do átrio direito, logo abaixo e lateral à abertura da veia cava superior",
               "No átrio esquerdo, junto às veias pulmonares",
               "No ápice do ventrículo esquerdo"],
         a=2, c="Nó sinusal: parede posterolateral superior do AD, junto à veia cava superior. Atrás da tricúspide, na parede posterior "
                "do AD, fica o nó AV."),
    dict(q="O feixe de Bachmann é:",
         opts=["O ramo esquerdo do feixe de His",
               "Uma via acessória que causa pré-excitação",
               "O feixe interatrial anterior, que conduz o impulso do átrio direito ao esquerdo",
               "A porção penetrante do feixe AV",
               "Um grupo de fibras de Purkinje do ventrículo direito"],
         a=2, c="O feixe interatrial anterior (de Bachmann) passa pela parede anterior dos átrios até o átrio esquerdo. As vias internodais "
                "anterior, média e posterior terminam no nó AV. Nessas faixas a condução é ≈ 1 m/s."),
    dict(q="Qual é o tempo aproximado desde o disparo do nó sinusal até o impulso alcançar os ramos no septo ventricular?",
         opts=["0,03 s", "0,09 s", "0,16 s", "0,30 s", "0,50 s"], keep=True,
         a=2, c="0,03 s até o nó AV + 0,09 s no nó AV + 0,04 s no feixe AV penetrante = 0,16 s."),
    dict(q="A principal causa da condução lenta no nó AV é:",
         opts=["O grande diâmetro das fibras nodais",
               "O pequeno número de junções comunicantes entre as células sucessivas",
               "A inervação simpática densa",
               "A presença de muitas miofibrilas",
               "O potencial de repouso mais negativo"],
         a=1, c="Com poucas gap junctions, a resistência à passagem de íons de uma célula para outra é grande, e cada célula demora a ser excitada."),
    dict(q="As fibras de Purkinje conduzem o impulso a 1,5 a 4 m/s. Isso se deve a:",
         opts=["Serem fibras finas com muitas miofibrilas",
               "Serem fibras grandes com junções comunicantes muito permeáveis",
               "Terem potencial de repouso de −55 mV",
               "Dependerem de canais de Ca²⁺ tipo L",
               "Receberem inervação vagal abundante"],
         a=1, c="Fibras de Purkinje são grandes (maiores que as ventriculares), têm poucas miofibrilas e gap junctions muito permeáveis. "
                "Conduzem ≈ 6× mais rápido que o músculo ventricular e ≈ 150× mais que algumas fibras do nó AV."),
    dict(q="Qual característica do feixe AV impede a reentrada do impulso dos ventrículos para os átrios em condições normais?",
         opts=["Alta velocidade de condução",
               "Condução unidirecional, associada ao isolamento pela barreira fibrosa",
               "Ausência de junções comunicantes",
               "Inervação exclusivamente simpática",
               "Período refratário mais curto que o do átrio"],
         a=1, c="O feixe AV normalmente só conduz no sentido átrio → ventrículo, e em todo o resto a barreira fibrosa isola átrio e ventrículo. "
                "Uma via acessória que atravesse essa barreira permite reentrada e arritmias."),
    dict(q="O tempo entre a excitação da primeira e da última fibra muscular ventricular normal é de cerca de:",
         opts=["0,003 s", "0,03 a 0,06 s", "0,16 s", "0,3 s", "1 s"], keep=True,
         a=1, c="A rápida condução do Purkinje faz a excitação do ventrículo inteiro caber em 0,03 a 0,06 s, garantindo contração síncrona."),
    dict(q="A transmissão do endocárdio para o epicárdio ventricular leva cerca de 0,03 s porque:",
         opts=["O impulso segue pelas fibras de Purkinje até o epicárdio",
               "O impulso percorre o músculo (0,3 a 0,5 m/s) em ângulo, acompanhando as camadas em espiral",
               "O epicárdio tem inervação vagal",
               "Há um nó intermediário no miocárdio",
               "O epicárdio é despolarizado antes do endocárdio"],
         a=1, c="As fibras de Purkinje penetram só ≈ 1/3 da parede. Depois o impulso segue pelo músculo, mais lento, angulando ao longo das espirais."),
    dict(q="As frequências intrínsecas de disparo do nó sinusal, do nó AV e das fibras de Purkinje são, respectivamente:",
         opts=["70 a 80; 40 a 60; 15 a 40 por minuto", "40 a 60; 70 a 80; 15 a 40 por minuto", "15 a 40; 40 a 60; 70 a 80 por minuto",
               "100; 80; 60 por minuto", "70 a 80; 15 a 40; 40 a 60 por minuto"],
         a=0, c="Nó sinusal 70 a 80, nó AV 40 a 60, Purkinje 15 a 40. O mais rápido comanda."),
    dict(q="O nó sinusal é o marca-passo normal do coração porque:",
         opts=["É o único tecido com automatismo",
               "Recebe inervação simpática exclusiva",
               "Sua frequência de descarga é maior e ele excita os demais tecidos antes que atinjam o próprio limiar",
               "Tem o potencial de repouso mais negativo",
               "Está mais próximo do nó AV"],
         a=2, c="Nó AV e Purkinje também têm automatismo, mas mais lento. Cada impulso sinusal os descarrega antes que se autoexcitem."),
    dict(q="Um paciente apresenta bloqueio AV total súbito e perde a consciência por alguns segundos antes de surgir um ritmo ventricular lento. Esse quadro é chamado:",
         opts=["Síndrome de Wolff-Parkinson-White", "Síndrome de Stokes-Adams", "Reflexo de Bainbridge", "Fibrilação ventricular", "Síncope vasovagal"],
         a=1, c="Após o bloqueio, o Purkinje estava suprimido pelo ritmo sinusal e demora 5 a 20 s para assumir. A pessoa desmaia após 4 a 5 s sem fluxo cerebral."),
    dict(q="Por que o sistema de Purkinje demora 5 a 20 segundos para assumir o ritmo após um bloqueio AV súbito?",
         opts=["Porque suas fibras estão em período refratário absoluto",
               "Porque estava suprimido pela estimulação rápida do nó sinusal (supressão por sobrecarga)",
               "Porque não possui automatismo",
               "Porque depende de estímulo simpático para disparar",
               "Porque o feixe AV conduz no sentido retrógrado"],
         a=1, c="Antes do bloqueio, as fibras de Purkinje foram \"sobrecarregadas\" pelos impulsos sinusais e ficam num estado suprimido por alguns segundos."),
    dict(q="Em um bloqueio AV total com escape pelo sistema de Purkinje, espera-se:",
         opts=["Átrios e ventrículos a 70 bpm, sincronizados",
               "Átrios na frequência sinusal e ventrículos a 15 a 40 bpm, de forma independente",
               "Átrios parados e ventrículos a 70 bpm",
               "Ventrículos a 150 bpm",
               "Átrios e ventrículos a 40 bpm, sincronizados"],
         a=1, c="Os átrios continuam no ritmo sinusal, e um marca-passo no Purkinje comanda os ventrículos a 15 a 40 bpm (dissociação AV)."),
    dict(q="O mecanismo pelo qual a acetilcolina reduz a frequência cardíaca é:",
         opts=["Aumentar a permeabilidade ao K⁺, hiperpolarizando o nó sinusal",
               "Aumentar a permeabilidade ao Na⁺ e Ca²⁺",
               "Bloquear a Na⁺/K⁺-ATPase",
               "Aumentar a corrente funny",
               "Estimular receptores β1"],
         a=0, c="A ACh aumenta muito a permeabilidade ao K⁺; o repouso do nó sinusal vai a −65 a −75 mV, e a despolarização lenta demora mais para chegar ao limiar."),
    dict(q="A inervação parassimpática (vagal) do coração distribui-se principalmente para:",
         opts=["Músculo ventricular", "Nós SA e AV", "Fibras de Purkinje", "Valvas cardíacas", "Artérias coronárias"],
         a=1, c="O vago vai principalmente aos nós SA e AV, menos ao músculo atrial e muito pouco ao ventrículo. O simpático atinge todo o coração, com forte representação ventricular."),
    dict(q="Qual é o efeito da estimulação simpática sobre o nó AV?",
         opts=["Retarda a condução", "Bloqueia a condução", "Aumenta a permeabilidade a Na⁺ e Ca²⁺ e acelera a condução AV",
               "Hiperpolariza as fibras de transição", "Não tem efeito"],
         a=2, c="A noradrenalina (β1) aumenta a permeabilidade a Na⁺ e Ca²⁺, facilitando a excitação de cada porção do feixe e diminuindo o tempo de condução AV."),
    dict(q="A estimulação simpática máxima pode aumentar a frequência cardíaca e a força de contração em, aproximadamente:",
         opts=["10% e 10%", "Quase três vezes e até duas vezes", "Duas vezes e cinco vezes", "Cinco vezes e três vezes", "Não altera a força"],
         a=1, c="Segundo o cap. 10, a estimulação simpática máxima quase triplica a FC e pode dobrar a força de contração."),
    dict(q="Um estímulo vagal muito intenso interrompe o nó sinusal. Após alguns segundos, os ventrículos voltam a bater a 15 a 40 bpm. Esse fenômeno é:",
         opts=["Reflexo de Bainbridge", "Escape ventricular", "Taquicardia paroxística", "Marca-passo sinusal errante", "Reentrada"],
         a=1, c="Um ponto do Purkinje (geralmente na porção septal do feixe AV) assume o ritmo: escape ventricular."),
]

OPEN = [
    dict(q="Mulher de 72 anos apresenta episódios de perda súbita da consciência, sem pródromos, com recuperação espontânea em poucos "
           "segundos. O ECG mostra ondas P regulares a 75/min e complexos QRS largos a 32/min, sem relação entre P e QRS. "
           "(a) Qual é o distúrbio e onde está o novo marca-passo ventricular? (b) Por que a frequência ventricular é de 32 bpm e a "
           "atrial de 75 bpm? (c) Explique, com base na fisiologia, os episódios de síncope.",
         a=["(a) <b>Bloqueio AV total</b> (dissociação AV). O ritmo ventricular vem do <b>sistema de Purkinje</b> (QRS largo = origem ventricular).",
            "(b) Os átrios seguem o <b>nó sinusal</b> (70 a 80/min); os ventrículos seguem a frequência intrínseca do <b>Purkinje (15 a 40/min)</b>, "
            "porque o impulso sinusal não atravessa o nó/feixe AV.",
            "(c) <b>Síndrome de Stokes-Adams</b>: quando o bloqueio se instala de forma súbita (ou o escape falha), o Purkinje estava suprimido "
            "pelo ritmo sinusal rápido e leva <b>5 a 20 s</b> para disparar. Sem bombeamento, o fluxo cerebral cessa e a pessoa desmaia após "
            "<b>4 a 5 s</b>, recuperando quando o escape ventricular aparece."]),
    dict(q="Jovem de 19 anos tem crises de palpitação de início e término súbitos. No ECG basal, o intervalo PR é curto e há um "
           "empastamento no início do QRS (onda delta), sugerindo uma via acessória entre átrio e ventrículo. (a) Qual estrutura "
           "normalmente impede a comunicação elétrica direta entre átrios e ventrículos, fora do feixe AV? (b) Por que o PR fica curto? "
           "(c) Como a via acessória favorece taquicardias?",
         a=["(a) A <b>barreira (esqueleto) fibrosa</b> atrioventricular, que isola o músculo atrial do ventricular. O único caminho normal é o feixe AV, que conduz só no sentido anterógrado.",
            "(b) A via acessória <b>não tem o atraso do nó AV</b> (0,09 s + 0,04 s no feixe), então parte do ventrículo é excitada precocemente: PR curto e onda delta.",
            "(c) Cria um <b>circuito de reentrada</b>: o impulso desce por uma via e volta pela outra (inclusive do ventrículo para o átrio), "
            "o que o feixe AV normal, unidirecional, não permite. Isso gera taquicardias paroxísticas."]),
    dict(q="Homem de 65 anos com insuficiência cardíaca e ventrículo esquerdo dilatado tem QRS de 170 ms por bloqueio de ramo esquerdo. "
           "O cardiologista indica um dispositivo de ressincronização. (a) Em condições normais, quanto tempo leva para todo o músculo "
           "ventricular ser excitado e qual estrutura garante isso? (b) O que acontece com o bombeamento quando a condução ventricular "
           "fica lenta? (c) Qual é a lógica da ressincronização?",
         a=["(a) <b>0,03 a 0,06 s</b> entre a primeira e a última fibra ventricular, graças às <b>fibras de Purkinje</b> (1,5 a 4 m/s), que "
            "distribuem o impulso quase instantaneamente pelo subendocárdio.",
            "(b) Se o impulso percorre o ventrículo devagar (pelo músculo, 0,3 a 0,5 m/s), partes do ventrículo contraem antes de outras "
            "(dessincronia), e a efetividade do bombeamento cai <b>20 a 30%</b>.",
            "(c) O dispositivo estimula átrio e <b>ambos os ventrículos</b> no tempo certo, restaurando a contração síncrona e melhorando o "
            "débito em corações dilatados e fracos."]),
]

OPEN_EXTRA = [
    ("Explique o mecanismo iônico da autoexcitação do nó sinusal.",
     "Repouso de −55 a −60 mV por permeabilidade natural a Na⁺ e Ca²⁺; nesse nível os canais rápidos de Na⁺ estão inativados. "
     "O vazamento de Na⁺ (corrente funny) despolariza lentamente até ≈ −40 mV, quando abrem canais de Ca²⁺ tipo L e ocorre o "
     "potencial. Os canais de Ca²⁺ inativam em 100 a 150 ms e abrem canais de K⁺, que repolarizam e hiperpolarizam; eles fecham "
     "aos poucos e o vazamento recomeça."),
    ("Descreva o trajeto do impulso cardíaco do nó sinusal até o epicárdio ventricular, com os tempos aproximados.",
     "Nó sinusal (0) → músculo atrial e vias internodais → nó AV (0,03 s) → atraso nodal de 0,09 s → feixe AV penetrante (0,12 s) "
     "→ +0,04 s → ramos no septo (0,16 s) → fibras de Purkinje até o fim (≈ 0,19 s) → músculo do endocárdio ao epicárdio (≈ 0,22 s)."),
    ("Qual a importância fisiológica do atraso no nó AV e qual a sua causa?",
     "Permite que os átrios contraiam e esvaziem nos ventrículos antes da sístole ventricular (≈ 20% do enchimento). A causa é o "
     "pequeno número de junções comunicantes entre as células nodais, com alta resistência à passagem de íons."),
    ("Por que o nó sinusal, e não o nó AV ou o Purkinje, comanda o ritmo cardíaco? O que é marca-passo ectópico?",
     "Porque tem a maior frequência intrínseca (70 a 80/min, contra 40 a 60 e 15 a 40): cada impulso sinusal descarrega os outros "
     "tecidos antes que atinjam o próprio limiar. Marca-passo ectópico é qualquer outro local que passa a comandar, por disparar "
     "mais rápido que o sinusal ou por bloqueio da condução sinusal."),
    ("Compare os efeitos do simpático e do parassimpático sobre o nó sinusal e o nó AV, incluindo o mecanismo iônico.",
     "Vago (ACh): ↑ permeabilidade ao K⁺, hiperpolariza (SA a −65 a −75 mV), reduz a FC e retarda ou bloqueia a condução AV. "
     "Simpático (noradrenalina, β1): ↑ permeabilidade a Na⁺ e Ca²⁺, acelera a rampa diastólica (FC ↑, até quase 3×), acelera a "
     "condução AV e aumenta a força (até 2×)."),
]

G = "fig_livro/"
CARDS = [
    ("c", "O nó sinusal fica na parede {{c1::posterolateral superior do átrio direito}}, junto à {{c2::veia cava superior}}.", "", G + "g10_01.png"),
    ("c", "O nó AV fica na parede {{c1::posterior do átrio direito}}, atrás da valva {{c2::tricúspide}}."),
    ("c", "Repouso do nó sinusal: {{c1::−55 a −60 mV}}; do músculo ventricular: {{c2::−85 a −90 mV}}.", "", "fig/b_potencial_sa.png"),
    ("c", "O repouso do nó sinusal é menos negativo porque a membrana é permeável a {{c1::Na⁺ e Ca²⁺}}."),
    ("c", "A −55 mV os canais {{c1::rápidos de Na⁺}} estão {{c2::inativados}}; o potencial nodal depende dos canais {{c3::de Ca²⁺ tipo L}}."),
    ("c", "A despolarização diastólica lenta vem da {{c1::corrente funny}} (vazamento de {{c2::Na⁺}})."),
    ("c", "Limiar de disparo do nó sinusal: ≈ {{c1::−40 mV}}."),
    ("c", "Os canais de Ca²⁺ tipo L do nó inativam em {{c1::100 a 150 ms}}, e abrem canais de {{c2::K⁺}}, que causam {{c3::hiperpolarização}}."),
    ("c", "Velocidade no músculo atrial ≈ {{c1::0,3 m/s}}; nas vias internodais ≈ {{c2::1 m/s}}."),
    ("c", "O feixe {{c1::de Bachmann}} (interatrial anterior) leva o impulso ao {{c2::átrio esquerdo}}."),
    ("c", "Vias internodais: {{c1::anterior, média e posterior}}."),
    ("c", "Tempos: nó AV {{c1::0,03 s}}; atraso nodal {{c2::0,09 s}}; feixe penetrante {{c3::0,04 s}}; chegada ao septo {{c4::0,16 s}}.",
     "", "fig/b_conducao.png"),
    ("c", "O atraso AV se deve a {{c1::poucas junções comunicantes}} entre as células nodais.", "", G + "g10_03.png"),
    ("c", "Purkinje conduz a {{c1::1,5 a 4 m/s}}: ≈ {{c2::6×}} o músculo e ≈ {{c3::150×}} o nó AV."),
    ("c", "A condução rápida no Purkinje se deve a fibras {{c1::grandes}} com junções comunicantes {{c2::muito permeáveis}}."),
    ("c", "O feixe AV conduz de forma {{c1::unidirecional}} (átrio → ventrículo)."),
    ("c", "Fora do feixe AV, átrio e ventrículo são isolados pela {{c1::barreira fibrosa}}; uma {{c2::via acessória}} permite {{c3::reentrada}}."),
    ("c", "O feixe AV desce {{c1::5 a 15 mm}} no septo antes de se dividir nos ramos {{c2::direito e esquerdo}}."),
    ("c", "As fibras de Purkinje penetram ≈ {{c1::1/3}} da espessura do músculo ventricular."),
    ("c", "Dos ramos até a última fibra ventricular: ≈ {{c1::0,06 s}}; endocárdio → epicárdio: {{c2::0,03 s}}.", "", G + "g10_04.png"),
    ("c", "Frequências intrínsecas: nó SA {{c1::70 a 80}}/min; nó AV {{c2::40 a 60}}/min; Purkinje {{c3::15 a 40}}/min.", "", "fig/b_marcapassos.png"),
    ("c", "Um marca-passo fora do nó sinusal é chamado {{c1::ectópico}}."),
    ("c", "No bloqueio AV súbito o Purkinje leva {{c1::5 a 20 s}} para assumir; o desmaio ocorre após {{c2::4 a 5 s}}: síndrome de {{c3::Stokes-Adams}}."),
    ("c", "A demora do Purkinje em assumir se deve à {{c1::supressão por sobrecarga}} pelo ritmo sinusal."),
    ("c", "Condução ventricular lenta reduz o bombeamento em {{c1::20 a 30%}}; trata-se com {{c2::ressincronização}}."),
    ("c", "O vago inerva principalmente os {{c1::nós SA e AV}}; o simpático, {{c2::todo o coração (forte no ventrículo)}}."),
    ("c", "A acetilcolina aumenta a permeabilidade ao {{c1::K⁺}} e leva o nó sinusal a {{c2::−65 a −75 mV}}.", "", "fig/b_autonomo.png"),
    ("c", "Vago moderado reduz a FC até {{c1::a metade}}; vago forte pode {{c2::parar o nó sinusal ou bloquear o nó AV}}."),
    ("c", "Após parada vagal, o ritmo do Purkinje a 15 a 40 bpm é o {{c1::escape ventricular}}."),
    ("c", "Noradrenalina age em receptores {{c1::β1}} e aumenta a permeabilidade a {{c2::Na⁺ e Ca²⁺}}."),
    ("c", "Simpático máximo: FC quase {{c1::triplica}} e força até {{c2::dobra}}."),
    ("b", "Quais as duas funções do sistema excitocondutor?", "<b>Gerar</b> o impulso rítmico e <b>conduzi-lo</b> rápido, com átrio antes do ventrículo e ventrículos síncronos."),
    ("b", "Por que o potencial do nó sinusal sobe e desce devagar?", "Depende de <b>canais de Ca²⁺ tipo L</b> (lentos); os rápidos de Na⁺ estão inativados."),
    ("b", "Por que o nó sinusal comanda o ritmo?", "É o <b>mais rápido</b>: descarrega nó AV e Purkinje antes que atinjam o próprio limiar."),
    ("b", "Bloqueio AV total: o que fazem átrios e ventrículos?", "Átrios no ritmo <b>sinusal</b>; ventrículos no ritmo do <b>Purkinje</b> (15 a 40 bpm), sem relação."),
    ("b", "Qual o efeito do vago no nó AV?", "Reduz a excitabilidade das fibras de transição (<b>menor fator de segurança</b>): atrasa ou bloqueia."),
    ("b", "Qual o efeito do simpático no nó AV?", "<b>Acelera</b> a condução (↑ permeabilidade a Na⁺ e Ca²⁺)."),
    ("b", "Por que a via acessória causa arritmias?", "Atravessa a barreira fibrosa e permite <b>reentrada</b> do ventrículo para o átrio."),
]

# oclusão sobre a Figura 10.1 do Guyton (coordenadas em pixels da imagem original, 469 × 453)
OCC_IMG = [
    (G + "g10_01.png", (10, 158, 78, 202), "Qual estrutura?", "<b>Nó sinusal</b>."),
    (G + "g10_01.png", (0, 232, 86, 274), "Qual estrutura?", "<b>Feixes (vias) internodais</b>."),
    (G + "g10_01.png", (16, 299, 74, 323), "Qual estrutura?", "<b>Nó AV</b>."),
    (G + "g10_01.png", (348, 156, 424, 181), "Qual estrutura?", "<b>Feixe AV</b> (His)."),
    (G + "g10_01.png", (393, 230, 469, 291), "Qual estrutura?", "<b>Ramo esquerdo do feixe</b>."),
    (G + "g10_01.png", (407, 314, 469, 376), "Qual estrutura?", "<b>Ramo direito do feixe</b>."),
]

TOPIC = dict(
    code="b", slug="b-excitacao-ritmica", title="Excitação rítmica do coração",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 10",
    sections=SECTIONS, mcq=MCQ, open=OPEN, open_extra=OPEN_EXTRA, cards=CARDS, occ="fig_tema_b", occ_img=OCC_IMG,
)
