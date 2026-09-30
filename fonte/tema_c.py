"""Tema c: O eletrocardiograma normal (Guyton & Hall, cap. 11, e vetores normais do cap. 12)."""

SECTIONS = [
    ("1. O que cada onda representa", [
        ("fig", "fig/c_ecg_normal.png", "fig_livro/g11_01.png", "ECG normal: ondas, intervalos e segmento ST.", 16.5),
        ("table", [
            ["Onda", "Evento elétrico", "Detalhe que cai"],
            ["<b>P</b>", "Despolarização <b>atrial</b>", "0,1 a 0,3 mV; começa ≈ 0,16 s antes do QRS"],
            ["<b>QRS</b>", "Despolarização <b>ventricular</b>", "Q, R e S; 1,0 a 1,5 mV nos membros (até 3 a 4 mV no precórdio)"],
            ["<b>T</b>", "Repolarização <b>ventricular</b>", "0,2 a 0,3 mV; ocorre 0,25 a 0,35 s após a despolarização"],
            ["T atrial", "Repolarização atrial", "0,15 a 0,20 s após a P: fica <b>escondida no QRS</b>"],
        ], [2.4, 5.2, 9.8]),
        ("ul", [
            "P e QRS são <b>ondas de despolarização</b>; T é <b>onda de repolarização</b>.",
            "<b>Sem corrente, sem onda</b>: com o músculo todo polarizado (repouso) ou todo despolarizado (segmento ST), o ECG fica na linha de base.",
            "O potencial de ação monofásico tem ≈ 110 mV; o ECG na pele registra só ≈ 1 mV, porque o sinal é captado à distância.",
            "O ECG é gerado pela <b>diferença de potencial entre partes despolarizadas e partes polarizadas</b> do coração.",
        ]),
    ]),
    ("2. Papel, calibração e intervalos", [
        ("fig", "fig/c_papel.png", None, "O papel do ECG a 25 mm/s e 10 mm/mV.", 8.5),
        ("table", [
            ["Medida", "Valor", "Como lembrar"],
            ["1 quadradinho (1 mm)", "0,04 s · 0,1 mV", "5 quadradinhos = 1 quadrado grande"],
            ["1 quadrado grande (5 mm)", "0,20 s · 0,5 mV", "5 quadrados grandes = 1 s"],
            ["Calibração", "10 mm = 1 mV", "Pulso retangular de 2 quadrados grandes"],
            ["<b>Intervalo PR (PQ)</b>", "≈ <b>0,16 s</b>", "Início da P ao início do QRS; ↓ simpático, ↑ vago"],
            ["<b>QRS</b>", "≈ 0,06 a 0,08 s", "&gt; 0,09 s é prolongado; &gt; 0,12 s quase sempre bloqueio"],
            ["<b>Intervalo QT</b>", "≈ <b>0,35 s</b>", "Início do QRS ao fim da T: dura a contração ventricular"],
            ["<b>RR</b>", "0,83 s → 72 bpm", "FC = 60 / RR (em segundos)"],
        ], [4.6, 3.8, 9.0]),
        ("box", "Frequência cardíaca em 5 segundos (complemento clínico)", [
            "<b>FC = 60 / RR</b> (Guyton). Na prática: <b>1500 / nº de quadradinhos</b> entre dois R, ou <b>300 / nº de quadrados grandes</b>.",
            "Sequência dos quadrados grandes: 1 = 300 · 2 = 150 · 3 = 100 · 4 = 75 · 5 = 60 · 6 = 50 bpm.",
            "Ritmo irregular: conte os QRS em 6 s (30 quadrados grandes) e multiplique por 10.",
        ]),
    ]),
    ("3. As 12 derivações", [
        ("fig", "fig/c_einthoven.png", "fig_livro/g11_06.png", "Derivações bipolares dos membros e triângulo de Einthoven. Note: I + III = II.", 9),
        ("table", [
            ["Derivação", "Polo negativo", "Polo positivo", "Eixo"],
            ["<b>I</b>", "Braço direito", "Braço esquerdo", "0°"],
            ["<b>II</b>", "Braço direito", "Perna esquerda", "+60°"],
            ["<b>III</b>", "Braço esquerdo", "Perna esquerda", "+120°"],
            ["<b>aVR</b>", "(central dos outros dois)", "Braço direito", "−150° (210°)"],
            ["<b>aVL</b>", "(central dos outros dois)", "Braço esquerdo", "−30°"],
            ["<b>aVF</b>", "(central dos outros dois)", "Perna esquerda", "+90°"],
        ], [3.0, 4.6, 4.6, 5.2]),
        ("ul", [
            "<b>Triângulo de Einthoven</b>: braços e perna esquerda são os vértices em volta do coração. A perna direita é só o terra.",
            "<b>Lei de Einthoven</b>: em qualquer instante, <b>I + III = II</b>. Ex.: I = +0,5 e III = +0,7 → II = +1,2 mV. Conhecendo duas, calcula-se a terceira.",
            "Como os eixos de I, II e III apontam para o lado positivo do vetor normal, o QRS é <b>positivo nas três</b>, maior em <b>II</b>.",
            "<b>Aumentadas (aV)</b>: um membro contra os outros dois unidos. <b>aVR sai invertida</b> (QRS negativo); aVL e aVF parecem com as bipolares.",
        ]),
        ("fig", "fig/c_precordiais.png", "fig_livro/g11_08.png", "Derivações precordiais: eletrodo explorador no tórax contra o terminal central (Wilson), 5.000 Ω em cada membro.", 11),
        ("fig", None, "fig_livro/g11_09.png", "Precordiais normais: V1 e V2 negativas, V4 a V6 positivas.", 8),
        ("ul", [
            "Eletrodo no tórax (+) contra o <b>terminal central de Wilson</b> (−: braços e perna esquerda ligados por resistências).",
            "<b>V1 e V2</b>: QRS <b>predominantemente negativo</b> (eletrodo mais perto da <b>base</b>, que fica negativa durante quase toda a despolarização).",
            "<b>V4 a V6</b>: QRS <b>predominantemente positivo</b> (perto do <b>ápice</b>). A transição fica em V3 ou V4.",
            "Posições (complemento clínico): V1 4º EIC direito e V2 4º EIC esquerdo, na borda esternal; V4 5º EIC na linha hemiclavicular; V3 entre V2 e V4; V5 axilar anterior e V6 axilar média, no nível de V4.",
            "ECG de rotina = <b>12 derivações</b>: I, II, III, aVR, aVL, aVF e V1 a V6.",
        ]),
        ("fig", None, "fig_livro/g11_11.png", "Registro normal de 12 derivações.", 15),
    ]),
    ("4. Vetores e eixo elétrico", [
        ("fig", "fig/c_hexaxial.png", "fig_livro/g12_03.png", "Sistema hexaxial: eixos das seis derivações dos membros.", 8),
        ("ul", [
            "Durante quase toda a despolarização a corrente vai da <b>base para o ápice</b> (base negativa, ápice positivo). Nos últimos 0,01 s ela se inverte.",
            "Sequência: o <b>septo despolariza da esquerda para a direita</b> primeiro (pequena <b>Q</b>), depois as paredes a partir do endocárdio (<b>R</b>), e por fim a base do VE (<b>S</b>). A despolarização ventricular leva ≈ 0,06 s.",
            "<b>T positiva</b>: o <b>epicárdio e o ápice repolarizam primeiro</b>, porque o endocárdio tem o fluxo coronariano comprimido durante a contração. "
            "Repolarização em sentido oposto à despolarização dá onda de <b>mesmo sentido</b> do QRS.",
            "<b>Eixo médio do QRS normal: +59°</b>; varia de ≈ <b>20° a 100°</b> em corações normais (Guyton). Na clínica, normal = <b>−30° a +90°</b>.",
        ]),
        ("fig", None, "fig_livro/g12_11.png", "Cálculo do eixo: voltagem líquida do QRS em I e III projetada nos eixos → +59°.", 7),
        ("fig", "fig/c_quadrantes.png", None, "Regra rápida do eixo com I e aVF (complemento clínico).", 7),
        ("box", "O que desvia o eixo em corações normais", [
            "<b>Para a esquerda</b>: expiração, deitar, obesidade (coração mais horizontal).",
            "<b>Para a direita</b>: inspiração, ficar em pé, biotipo alto e magro (coração mais vertical).",
            "Em doença, o eixo desvia <b>para o lado do ventrículo hipertrofiado</b> (mais massa, mais corrente) ou para o lado de um ramo bloqueado.",
        ]),
    ]),
    ("5. Roteiro de leitura e monitorização", [
        ("box", "Roteiro para ler um ECG normal (complemento clínico)", [
            "<b>1. Calibração e velocidade</b>: 10 mm/mV, 25 mm/s.",
            "<b>2. Ritmo sinusal</b>: onda P antes de cada QRS, P positiva em I e II (e negativa em aVR), PR constante.",
            "<b>3. FC</b>: 60–100 bpm (300 / quadrados grandes).",
            "<b>4. Intervalos</b>: PR 0,12–0,20 s; QRS &lt; 0,12 s; QT ≈ 0,35 s (varia com a FC).",
            "<b>5. Eixo</b>: I e aVF positivos = normal.",
            "<b>6. Progressão de R</b> nas precordiais: R cresce de V1 a V5.",
        ]),
        ("ul", [
            "<b>Holter</b>: ECG contínuo por <b>24 a 48 h</b> durante a rotina, para sintomas frequentes.",
            "<b>Monitor de eventos/intermitente</b>: semanas, para sintomas esporádicos; o paciente aciona na hora do sintoma.",
            "<b>Monitor implantável (loop)</b>: subcutâneo, <b>2 a 3 anos</b>, para síncope rara e inexplicada.",
        ]),
    ]),
]

MCQ = [
    dict(q="A onda P do eletrocardiograma normal representa:",
         opts=["A despolarização atrial", "A repolarização atrial", "A despolarização do nó sinusal isolado",
               "A condução pelo nó AV", "A despolarização do septo interventricular"],
         a=0, c="A onda P é causada pelo potencial elétrico gerado quando os átrios se despolarizam, antes da contração atrial. "
                "A descarga do nó sinusal em si é pequena demais para aparecer no ECG de superfície."),
    dict(q="Por que a onda de repolarização atrial não costuma ser vista no ECG normal?",
         opts=["Porque os átrios não repolarizam", "Porque ela ocorre durante o QRS e é encoberta por ele",
               "Porque ocorre junto com a onda T", "Porque tem voltagem maior que o QRS", "Porque só aparece em aVR"],
         a=1, c="Os átrios repolarizam 0,15 a 0,20 s depois da onda P, exatamente quando o QRS está sendo registrado. A onda T atrial, "
                "pequena, fica mascarada pelo QRS, muito maior."),
    dict(q="Durante o segmento ST, com todo o músculo ventricular despolarizado, o ECG normal:",
         opts=["Registra a maior voltagem do ciclo", "Fica na linha de base, porque não há diferença de potencial entre as regiões",
               "Registra a onda U", "Registra a repolarização atrial em destaque", "Mostra deflexão negativa em todas as derivações"],
         a=1, c="O ECG só registra corrente quando parte do coração está polarizada e parte despolarizada. Com todo o ventrículo "
                "despolarizado (ou todo em repouso) não há corrente, e o traçado fica no potencial zero."),
    dict(q="No papel padrão do ECG (25 mm/s), cada quadradinho de 1 mm corresponde, na horizontal, a:",
         opts=["0,01 s", "0,02 s", "0,04 s", "0,20 s", "1,0 s"], keep=True,
         a=2, c="A 25 mm/s, 1 s ocupa 25 mm: 1 mm = 0,04 s e 5 mm (quadrado grande) = 0,20 s."),
    dict(q="Na calibração padrão do eletrocardiógrafo, 1 mV corresponde a:",
         opts=["1 mm", "2 mm", "5 mm", "10 mm", "25 mm"], keep=True,
         a=3, c="O padrão é 10 mm/mV: 10 quadradinhos (2 quadrados grandes) na vertical. Cada quadradinho = 0,1 mV."),
    dict(q="O intervalo PR normal mede cerca de:",
         opts=["0,04 s", "0,08 s", "0,16 s", "0,35 s", "0,50 s"], keep=True,
         a=2, c="O PR (ou PQ) vai do início da P ao início do QRS e mede ≈ 0,16 s. Ele encurta com estímulo simpático e alonga com estímulo vagal."),
    dict(q="O intervalo QT, cujo valor normal é de cerca de 0,35 s, corresponde aproximadamente:",
         opts=["À contração atrial", "Ao atraso no nó AV", "À contração ventricular (despolarização e repolarização)",
               "Ao enchimento rápido ventricular", "À diástase"],
         a=2, c="O QT vai do início do QRS ao fim da onda T, isto é, da despolarização ao fim da repolarização ventricular: é o período "
                "da contração ventricular."),
    dict(q="Num ECG a 25 mm/s, o intervalo entre dois complexos QRS é de 4 quadrados grandes. A frequência cardíaca é:",
         opts=["30 bpm", "40 bpm", "50 bpm", "60 bpm", "75 bpm"], keep=True,
         a=4, c="4 quadrados grandes = 4 × 0,20 = 0,80 s. FC = 60 / 0,80 = 75 bpm (ou 300 / 4 = 75)."),
    dict(q="Um intervalo RR de 0,83 s corresponde a uma frequência cardíaca de aproximadamente:",
         opts=["60 bpm", "72 bpm", "83 bpm", "100 bpm", "120 bpm"], keep=True,
         a=1, c="FC = 60 / RR = 60 / 0,83 ≈ 72 bpm, o exemplo usado pelo Guyton."),
    dict(q="Na derivação I, os eletrodos são conectados da seguinte forma:",
         opts=["Braço direito (−) e braço esquerdo (+)", "Braço direito (−) e perna esquerda (+)",
               "Braço esquerdo (−) e perna esquerda (+)", "Braço esquerdo (−) e braço direito (+)", "Perna direita (−) e braço esquerdo (+)"],
         a=0, c="I: braço direito negativo, braço esquerdo positivo. II: braço direito − e perna esquerda +. III: braço esquerdo − e perna esquerda +."),
    dict(q="Em determinado instante, a voltagem registrada é +0,4 mV na derivação I e +0,6 mV na derivação III. Pela lei de Einthoven, a derivação II registra:",
         opts=["+0,2 mV", "+0,4 mV", "+0,6 mV", "+1,0 mV", "+2,4 mV"], keep=True,
         a=3, c="Lei de Einthoven: I + III = II. Logo, 0,4 + 0,6 = +1,0 mV."),
    dict(q="Nas derivações bipolares dos membros de uma pessoa normal, o complexo QRS é:",
         opts=["Negativo nas três", "Positivo nas três, geralmente maior em II", "Positivo apenas em III",
               "Isoelétrico em II", "Negativo em I e positivo em III"],
         a=1, c="O vetor médio normal (≈ +59°) aponta para o lado positivo dos eixos de I (0°), II (+60°) e III (+120°). A projeção é "
                "maior em II, cujo eixo quase coincide com o vetor."),
    dict(q="Qual derivação do ECG normal apresenta tipicamente o complexo QRS invertido (predominantemente negativo)?",
         opts=["aVR", "aVF", "aVL", "II", "V5"],
         a=0, c="O eixo positivo de aVR aponta para o braço direito (−150°), oposto ao vetor médio do coração, então o QRS sai invertido."),
    dict(q="O eixo de derivação de aVF está em:",
         opts=["0°", "+60°", "+90°", "+120°", "−30°"], keep=True,
         a=2, c="aVF: +90° (perna esquerda). I 0°, II +60°, III +120°, aVL −30°, aVR −150°."),
    dict(q="Nas derivações precordiais normais, V1 e V2 mostram QRS predominantemente negativo porque:",
         opts=["Estão sobre o ventrículo esquerdo", "O eletrodo fica mais perto da base, eletronegativa durante quase toda a despolarização",
               "Estão ligadas ao braço direito", "Registram só a despolarização atrial", "A calibração dessas derivações é invertida"],
         a=1, c="Em V1 e V2 o eletrodo fica perto da base do coração, que é a região negativa durante a maior parte da despolarização. "
                "V4 a V6, perto do ápice (positivo), mostram QRS positivo."),
    dict(q="O polo negativo (indiferente) das derivações precordiais é formado por:",
         opts=["O eletrodo da perna direita", "O terminal central, com braços e perna esquerda ligados por resistências",
               "O eletrodo de V6", "O braço direito isolado", "Um eletrodo esofágico"],
         a=1, c="No terminal central de Wilson, os três membros são ligados por resistências elétricas (5.000 Ω no Guyton) ao polo negativo, "
                "e o eletrodo torácico é o positivo."),
    dict(q="O eletrodo de V4 deve ser posicionado:",
         opts=["No 4º espaço intercostal direito, junto ao esterno", "No 4º espaço intercostal esquerdo, junto ao esterno",
               "No 5º espaço intercostal esquerdo, na linha hemiclavicular", "Na linha axilar média, no nível de V1",
               "No 2º espaço intercostal esquerdo"],
         a=2, c="V1: 4º EIC direito paraesternal; V2: 4º EIC esquerdo paraesternal; V4: 5º EIC esquerdo na linha hemiclavicular; "
                "V3 entre V2 e V4; V5 e V6 nas linhas axilares anterior e média, no nível de V4."),
    dict(q="A pequena onda Q no início do QRS normal decorre de:",
         opts=["Despolarização do septo da esquerda para a direita", "Repolarização atrial", "Despolarização da base do VE",
               "Despolarização do ápice", "Atraso no nó AV"],
         a=0, c="A primeira região ventricular a despolarizar é o lado esquerdo do septo, e a onda vai da esquerda para a direita, "
                "oposta ao vetor principal. Isso gera a pequena deflexão negativa Q em I e nas derivações esquerdas."),
    dict(q="A onda T é normalmente positiva nas derivações em que o QRS é positivo. A explicação é que:",
         opts=["A repolarização segue o mesmo trajeto da despolarização",
               "O epicárdio e o ápice repolarizam antes do endocárdio, em sentido oposto à despolarização",
               "A repolarização não gera corrente", "A onda T é gerada pelos átrios",
               "O nó sinusal repolariza durante a T"],
         a=1, c="O endocárdio tem o fluxo coronariano comprimido durante a sístole e repolariza por último. Como a repolarização caminha "
                "do epicárdio para o endocárdio (oposta à despolarização) e é um processo de carga oposta, a deflexão sai no mesmo sentido do QRS."),
    dict(q="O eixo elétrico médio do QRS de um coração normal é de cerca de:",
         opts=["−60°", "+59°", "+120°", "+150°", "+180°"], keep=True,
         a=1, c="Guyton: eixo médio ≈ +59°, variando de ≈ 20° a 100° em pessoas normais. Na prática clínica o normal vai de −30° a +90°."),
    dict(q="Um paciente tem QRS positivo em I e positivo em aVF. O eixo elétrico está:",
         opts=["Normal (entre 0° e +90°)", "Desviado para a esquerda", "Desviado para a direita", "Em desvio extremo", "Indeterminado"],
         a=0, c="I positivo = vetor aponta para a esquerda do paciente; aVF positivo = aponta para baixo. O quadrante inferior esquerdo é o normal."),
    dict(q="Qual das condições tende a desviar o eixo elétrico para a ESQUERDA em uma pessoa normal?",
         opts=["Inspiração profunda", "Ficar em pé", "Biotipo alto e magro", "Obesidade", "Hipertrofia do ventrículo direito"],
         a=3, c="Obesidade, expiração e decúbito deixam o coração mais horizontal e desviam o eixo à esquerda. Inspiração, ortostase e "
                "biotipo longilíneo desviam à direita. Hipertrofia desvia para o lado do ventrículo hipertrofiado."),
    dict(q="Qual a duração do complexo QRS a partir da qual se suspeita fortemente de bloqueio da condução intraventricular?",
         opts=["0,04 s", "0,06 s", "0,08 s", "0,12 s", "0,35 s"], keep=True,
         a=3, c="Guyton: QRS acima de 0,09 s já é prolongado; acima de 0,12 s é quase certamente bloqueio em algum ponto da condução ventricular."),
    dict(q="Sobre a voltagem das ondas no ECG normal registrado nos membros, é correto afirmar:",
         opts=["O QRS mede cerca de 110 mV, como o potencial de ação", "O QRS mede 1,0 a 1,5 mV, e a onda P 0,1 a 0,3 mV",
               "A onda T é sempre maior que o QRS", "A onda P mede cerca de 3 mV", "Todas as ondas têm a mesma voltagem"],
         a=1, c="Nos membros, QRS 1,0 a 1,5 mV, P 0,1 a 0,3 mV e T 0,2 a 0,3 mV. Sobre o coração o QRS chega a 3 a 4 mV, ainda muito "
                "menor que os ≈ 110 mV do potencial de ação monofásico."),
    dict(q="Paciente com palpitações e síncopes raras (uma a cada poucos meses), com ECG de repouso e Holter de 24 h normais. O exame mais adequado para documentar o ritmo durante o sintoma é:",
         opts=["Repetir o ECG de 12 derivações", "Holter de 24 h novamente", "Monitor de eventos implantável (loop)",
               "Teste de calibração do eletrocardiógrafo", "Radiografia de tórax"],
         a=2, c="Holter (24 a 48 h) serve para sintomas frequentes. Para eventos raros, o monitor implantável subcutâneo registra por 2 a 3 anos "
                "e captura o ritmo no momento do sintoma."),
]

OPEN = [
    dict(q="Estudante de 20 anos, assintomático, faz ECG de rotina (25 mm/s, 10 mm/mV). Há uma onda P antes de cada QRS, positiva em I e II. "
           "Entre dois R há 20 quadradinhos. O início da P ao início do QRS mede 4 quadradinhos, o QRS mede 2 quadradinhos e do início do QRS "
           "ao fim da T há 9 quadradinhos. (a) Calcule a FC. (b) Calcule PR, QRS e QT em segundos e diga se são normais. (c) Qual evento "
           "elétrico corresponde a cada um desses intervalos?",
         a=["(a) RR = 20 × 0,04 = <b>0,80 s</b>; FC = 60 / 0,80 = <b>75 bpm</b> (ou 1500 / 20). Normal, e o ritmo é <b>sinusal</b> (P antes de cada QRS, positiva em I e II).",
            "(b) PR = 4 × 0,04 = <b>0,16 s</b> (normal). QRS = 2 × 0,04 = <b>0,08 s</b> (normal, &lt; 0,09 s pelo Guyton). "
            "QT = 9 × 0,04 = <b>0,36 s</b> (normal, ≈ 0,35 s).",
            "(c) PR: despolarização atrial + atraso no nó AV/feixe até o início da despolarização ventricular. QRS: despolarização dos "
            "ventrículos. QT: da despolarização ao fim da repolarização ventricular, ou seja, a contração ventricular."]),
    dict(q="Mulher de 58 anos, obesa, faz ECG deitada. O QRS tem voltagem líquida de +0,6 mV em I e +0,2 mV em III. (a) Pela lei de Einthoven, "
           "qual a voltagem líquida em II? (b) Os eixos de I, II e III ficam em quais ângulos, e em que quadrante está o eixo desta paciente? "
           "(c) Por que a obesidade e o decúbito podem desviar o eixo, e para qual lado? (d) Em qual derivação dos membros se espera QRS negativo?",
         a=["(a) <b>I + III = II</b> → 0,6 + 0,2 = <b>+0,8 mV</b>.",
            "(b) I = 0°, II = +60°, III = +120°. Com QRS positivo em I e em III (e II), o vetor está entre 0° e +90°. Como I é bem maior "
            "que III, ele fica perto de <b>+45°</b>: <b>eixo normal, puxado para a esquerda</b> em relação aos +59° típicos.",
            "(c) Obesidade e decúbito (e a expiração) elevam o diafragma e deixam o coração mais <b>horizontal</b>, desviando o eixo "
            "<b>para a esquerda</b>. Em pé, na inspiração e no longilíneo ocorre o contrário.",
            "(d) Em <b>aVR</b> (eixo −150°), oposto ao vetor médio: QRS negativo é normal."]),
    dict(q="Homem de 45 anos refere tonturas e palpitações duas a três vezes por semana, sem relação com esforço. O ECG de 12 derivações no "
           "consultório é normal. (a) Por que um ECG normal não afasta arritmia? (b) Qual exame indicar e por quanto tempo? (c) Se os sintomas "
           "fossem síncopes a cada poucos meses, o que mudaria? (d) Cite as 12 derivações que compõem o ECG de rotina.",
         a=["(a) O ECG de repouso registra só <b>alguns segundos</b>; arritmias paroxísticas podem não ocorrer durante o exame.",
            "(b) <b>Holter</b>: ECG contínuo por <b>24 a 48 h</b>, durante a rotina, com diário de sintomas para correlacionar sintoma e ritmo.",
            "(c) Para eventos raros, usa-se <b>monitor de eventos</b> (semanas) ou <b>monitor implantável (loop)</b> subcutâneo, que registra "
            "por <b>2 a 3 anos</b>.",
            "(d) Bipolares <b>I, II, III</b>; aumentadas <b>aVR, aVL, aVF</b>; precordiais <b>V1 a V6</b>."]),
]

OPEN_EXTRA = [
    ("Relacione cada onda do ECG normal com o evento elétrico e o evento mecânico correspondente.",
     "P: despolarização atrial, seguida da contração atrial. QRS: despolarização ventricular, seguida da contração ventricular (a pressão "
     "sobe logo após o início do QRS). T: repolarização ventricular, que antecede o relaxamento ventricular. A repolarização atrial fica "
     "escondida no QRS."),
    ("Por que não há registro no ECG quando o músculo está totalmente polarizado ou totalmente despolarizado?",
     "Porque o ECG registra corrente extracelular gerada pela diferença de potencial entre regiões despolarizadas e polarizadas. Com o "
     "músculo todo igual (repouso ou platô, no segmento ST), não há diferença e não há corrente: o traçado fica na linha de base."),
    ("Explique a lei de Einthoven e dê um exemplo numérico.",
     "Se os potenciais de duas das três derivações bipolares são conhecidos, a terceira é a soma algébrica das outras: I + III = II "
     "(respeitando os sinais). Ex.: I = +0,5 mV, III = +0,7 mV → II = +1,2 mV."),
    ("Descreva a sequência de despolarização ventricular e como ela gera Q, R e S.",
     "O septo despolariza primeiro, da esquerda para a direita (vetor pequeno oposto ao principal = Q). Depois as paredes, do endocárdio "
     "para o epicárdio, com vetor para o ápice e a esquerda (grande R). Por último a base posterior do VE (vetor para cima e para trás = S). "
     "Leva ≈ 0,06 s."),
    ("Por que a onda T normal é positiva, se a repolarização é um processo de carga oposta à despolarização?",
     "Porque a repolarização começa no epicárdio e no ápice e termina no endocárdio (o endocárdio tem fluxo coronariano comprimido na "
     "sístole e repolariza por último). Com sentido e carga opostos à despolarização, os dois sinais se anulam e a deflexão sai positiva, "
     "como o QRS."),
    ("Como se determina o eixo elétrico médio do QRS e qual o valor normal?",
     "Mede-se a voltagem líquida do QRS (positivo menos negativo) em duas derivações (ex.: I e III), projeta-se cada uma no seu eixo e "
     "traçam-se perpendiculares; o cruzamento dá o vetor médio. Normal ≈ +59° (20° a 100° no Guyton; −30° a +90° na clínica). Rápido: "
     "I e aVF positivos = normal."),
]

G = "fig_livro/"
CARDS = [
    ("c", "Onda P = {{c1::despolarização atrial}}; QRS = {{c2::despolarização ventricular}}; T = {{c3::repolarização ventricular}}.", "", "fig/c_ecg_normal.png"),
    ("c", "A repolarização atrial ocorre {{c1::0,15 a 0,20 s}} após a P e fica escondida no {{c2::QRS}}."),
    ("c", "A onda T ocorre {{c1::0,25 a 0,35 s}} após a despolarização ventricular."),
    ("c", "O ECG não registra potencial quando o músculo está {{c1::todo polarizado ou todo despolarizado}}."),
    ("c", "Voltagens nos membros: QRS {{c1::1,0 a 1,5 mV}}; P {{c2::0,1 a 0,3 mV}}; T {{c3::0,2 a 0,3 mV}}."),
    ("c", "Sobre o coração o QRS chega a {{c1::3 a 4 mV}}; o potencial de ação monofásico tem ≈ {{c2::110 mV}}."),
    ("c", "Calibração: {{c1::10 mm}} = 1 mV; velocidade padrão {{c2::25 mm/s}}.", "", "fig/c_papel.png"),
    ("c", "A 25 mm/s: 1 quadradinho = {{c1::0,04 s}}; 1 quadrado grande = {{c2::0,20 s}}."),
    ("c", "Intervalo PR normal ≈ {{c1::0,16 s}}; QT ≈ {{c2::0,35 s}}."),
    ("c", "O PR {{c1::encurta}} com simpático e {{c2::alonga}} com vago."),
    ("c", "FC = {{c1::60 / RR}} (s); RR 0,83 s = {{c2::72 bpm}}."),
    ("c", "FC pelo papel: {{c1::1500}} / quadradinhos ou {{c2::300}} / quadrados grandes."),
    ("c", "Quadrados grandes entre R: 1 = 300 · 2 = {{c1::150}} · 3 = {{c2::100}} · 4 = {{c3::75}} · 5 = {{c4::60}} bpm."),
    ("c", "QRS acima de {{c1::0,09 s}} é prolongado; acima de {{c2::0,12 s}} é quase certamente bloqueio."),
    ("c", "Derivação I: braço direito {{c1::(−)}} e braço esquerdo {{c2::(+)}}."),
    ("c", "Derivação II: {{c1::braço direito (−)}} e {{c2::perna esquerda (+)}}."),
    ("c", "Derivação III: {{c1::braço esquerdo (−)}} e {{c2::perna esquerda (+)}}."),
    ("c", "Lei de Einthoven: {{c1::I + III = II}}.", "Ex.: +0,5 + 0,7 = +1,2 mV", G + "g11_06.png"),
    ("c", "Eixos: I {{c1::0°}}, II {{c2::+60°}}, III {{c3::+120°}}.", "", "fig/c_hexaxial.png"),
    ("c", "Eixos: aVR {{c1::−150° (210°)}}, aVL {{c2::−30°}}, aVF {{c3::+90°}}."),
    ("c", "No ECG normal, a derivação {{c1::aVR}} sai invertida.", "", G + "g11_10.png"),
    ("c", "O polo negativo das precordiais é o {{c1::terminal central de Wilson}}."),
    ("c", "V1 e V2 têm QRS {{c1::negativo}} (perto da {{c2::base}}); V4 a V6, {{c3::positivo}} (perto do ápice).", "", G + "g11_09.png"),
    ("c", "V1: {{c1::4º EIC direito}}, paraesternal; V2: {{c2::4º EIC esquerdo}}, paraesternal.", "", "fig/c_precordiais.png"),
    ("c", "V4: {{c1::5º EIC esquerdo, linha hemiclavicular}}; V6: {{c2::linha axilar média}}, no nível de V4."),
    ("c", "O ECG de rotina tem {{c1::12}} derivações: 3 bipolares, 3 {{c2::aumentadas}} e 6 {{c3::precordiais}}."),
    ("c", "Na despolarização a corrente vai da {{c1::base}} para o {{c2::ápice}}; inverte nos últimos {{c3::0,01 s}}."),
    ("c", "A onda Q vem da despolarização do {{c1::septo}}, da {{c2::esquerda para a direita}}."),
    ("c", "A despolarização ventricular dura ≈ {{c1::0,06 s}}."),
    ("c", "T positiva: o {{c1::epicárdio/ápice}} repolariza primeiro porque o endocárdio tem {{c2::fluxo coronariano comprimido}} na sístole."),
    ("c", "Eixo médio do QRS normal: {{c1::+59°}}; faixa normal (Guyton) {{c2::20° a 100°}}; na clínica {{c3::−30° a +90°}}.", "", G + "g12_11.png"),
    ("c", "I positivo e aVF positivo = eixo {{c1::normal}}; I + e aVF − = desvio à {{c2::esquerda}}; I − e aVF + = desvio à {{c3::direita}}.",
     "", "fig/c_quadrantes.png"),
    ("c", "Desviam o eixo à esquerda: {{c1::expiração, decúbito, obesidade}}.", "Coração mais horizontal"),
    ("c", "Desviam o eixo à direita: {{c1::inspiração, ortostase, biotipo alto e magro}}.", "Coração mais vertical"),
    ("c", "Em hipertrofia, o eixo desvia para o lado do {{c1::ventrículo hipertrofiado}}."),
    ("c", "Holter registra por {{c1::24 a 48 h}}; monitor implantável (loop) por {{c2::2 a 3 anos}}."),
    ("b", "O que o ECG registra, afinal?", "A corrente extracelular gerada pela <b>diferença de potencial entre regiões despolarizadas e polarizadas</b> do coração."),
    ("b", "Critérios de ritmo sinusal (complemento clínico)?", "Onda <b>P antes de cada QRS</b>, P <b>positiva em I e II</b> (negativa em aVR), PR constante, FC 60 a 100."),
    ("b", "Por que o QRS é maior em II no normal?", "O eixo de II (<b>+60°</b>) quase coincide com o vetor médio (<b>+59°</b>)."),
    ("b", "Por que aVR sai invertida?", "Seu polo positivo (braço direito, <b>−150°</b>) aponta contra o vetor médio do coração."),
    ("b", "O que o intervalo QT representa?", "Da despolarização ao fim da repolarização ventricular: a <b>contração ventricular</b>."),
    ("b", "Qual o papel da perna direita no ECG?", "É só o <b>terra</b> (referência), não entra nas derivações."),
    ("b", "Qual a ordem de despolarização que gera Q, R e S?", "<b>Septo</b> E→D (Q) → <b>paredes/ápice</b> (R) → <b>base posterior do VE</b> (S)."),
]

# oclusão sobre a Figura 12.3 do Guyton (coordenadas em pixels da imagem original, 388 × 384)
OCC_IMG = [
    (G + "g12_03.png", (40, 76, 86, 102), "Qual derivação?", "<b>aVR</b> (−150° ou 210°)."),
    (G + "g12_03.png", (302, 76, 346, 102), "Qual derivação?", "<b>aVL</b> (−30°)."),
    (G + "g12_03.png", (198, 344, 238, 368), "Qual derivação?", "<b>aVF</b> (+90°)."),
    (G + "g12_03.png", (260, 287, 284, 311), "Qual derivação?", "<b>II</b> (+60°)."),
    (G + "g12_03.png", (95, 287, 122, 311), "Qual derivação?", "<b>III</b> (+120°)."),
]

TOPIC = dict(
    code="c", slug="c-ecg-normal", title="O eletrocardiograma normal",
    source="Guyton & Hall, Tratado de Fisiologia Médica, caps. 11 e 12",
    sections=SECTIONS, mcq=MCQ, open=OPEN, open_extra=OPEN_EXTRA, cards=CARDS, occ="dia_c", occ_img=OCC_IMG,
)
