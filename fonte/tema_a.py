"""Tema a: O músculo cardíaco e as valvas cardíacas (Guyton & Hall, cap. 9; bulhas do cap. 23)."""

SECTIONS = [
    ("1. Visão geral: o coração como duas bombas", [
        ("p", "O coração são <b>duas bombas pulsáteis em série</b>: o coração direito leva sangue aos pulmões e o esquerdo à "
              "circulação sistêmica. Cada lado tem um <b>átrio</b> (bomba fraca, câmara de entrada) e um <b>ventrículo</b> "
              "(fonte principal de força). O pericárdio envolve e fixa o coração."),
        ("p", "Existem três tipos de músculo cardíaco: <b>atrial</b>, <b>ventricular</b> (contraem como o esquelético, mas por "
              "muito mais tempo) e <b>fibras excitatórias e condutoras especializadas</b> (quase sem miofibrilas; geram e "
              "conduzem o impulso, assunto do tema b)."),
    ]),
    ("2. Anatomia funcional do miocárdio", [
        ("ul", [
            "<b>Estriado</b>, com actina e miosina organizadas em sarcômeros, deslizando como no músculo esquelético.",
            "<b>Discos intercalares</b>: membranas que separam as células; nelas há <b>junções comunicantes (gap junctions)</b> "
            "de baixa resistência, por onde os íons passam livremente.",
            "Resultado: o miocárdio funciona como um <b>sincício funcional</b>. Excitada uma célula, o potencial de ação se "
            "espalha para todas.",
            "São <b>dois sincícios</b>: <b>atrial</b> e <b>ventricular</b>, separados pelo <b>esqueleto fibroso</b> em torno dos "
            "anéis valvares AV. O impulso só passa dos átrios aos ventrículos pelo <b>feixe AV</b>. Isso permite que os átrios "
            "contraiam um pouco antes dos ventrículos.",
            "<b>Torção do VE</b>: fibras subepicárdicas em hélice para a esquerda e subendocárdicas para a direita. Na sístole o "
            "ápice gira em sentido horário e a base em anti-horário, puxando a base em direção ao ápice (\"torcer a toalha\"). "
            "Na diástole a destorção funciona como mola que ajuda a sucção do sangue.",
        ]),
    ]),
    ("3. Potencial de ação do músculo ventricular", [
        ("fig", "fig/a_potencial_acao.png", "Figura 1. Potencial de ação da fibra ventricular e suas fases (esquema; valores do Guyton).", 14.5),
        ("p", "Repouso ≈ <b>−85 mV</b>; pico ≈ <b>+20 mV</b> (amplitude ≈ 105 mV). Após o pico, a membrana fica despolarizada "
              "por ≈ <b>0,2 s</b> no <b>platô</b>, e então repolariza abruptamente. Por causa do platô, a contração ventricular "
              "dura até <b>15 vezes</b> mais que a do músculo esquelético."),
        ("table", [
            ["Fase", "O que acontece", "Corrente dominante"],
            ["0 · despolarização", "Abrem os <b>canais rápidos de Na⁺</b> dependentes de voltagem; potencial vai a ≈ +20 mV", "Entrada de Na⁺"],
            ["1 · repolarização inicial", "Canais de Na⁺ fecham; K⁺ sai por canais transitórios", "Saída de K⁺"],
            ["2 · platô", "Abrem lentamente os <b>canais de Ca²⁺ tipo L</b> (lentos, \"cálcio-sódio\") e <b>cai ~5× a permeabilidade ao K⁺</b>", "Entrada de Ca²⁺ ≈ saída de K⁺"],
            ["3 · repolarização rápida", "Canais de Ca²⁺ fecham; abrem canais lentos de K⁺ (retificador tardio)", "Saída de K⁺"],
            ["4 · repouso", "Potencial estável em −80 a −90 mV (no ventrículo)", "K⁺ (canais de repouso)"],
        ], [3.6, 9.4, 4.4]),
        ("box", "Por que o potencial de ação cardíaco é longo? (duas diferenças em relação ao esquelético)", [
            "Além dos canais rápidos de Na⁺, existem <b>canais lentos de Ca²⁺ tipo L</b> que ficam abertos por <b>décimos de segundo</b>, "
            "mantendo a despolarização. O Ca²⁺ que entra também <b>ativa a contração</b>.",
            "Logo após o início do potencial, a <b>permeabilidade ao K⁺ cai cerca de 5 vezes</b> (efeito que não existe no esquelético), "
            "impedindo a repolarização precoce. Quando os canais de Ca²⁺ fecham (0,2 a 0,3 s), a permeabilidade ao K⁺ sobe e a fibra repolariza.",
        ]),
        ("h2", "Velocidade de condução e período refratário"),
        ("table", [
            ["Parâmetro", "Valor (Guyton)"],
            ["Condução no músculo atrial e ventricular", "0,3 a 0,5 m/s (≈ 1/250 das fibras nervosas grandes, ≈ 1/10 do músculo esquelético)"],
            ["Condução nas fibras de Purkinje", "até 4 m/s"],
            ["Período refratário absoluto do ventrículo", "0,25 a 0,30 s (≈ duração do potencial com platô)"],
            ["Período refratário relativo do ventrículo", "≈ 0,05 s adicional (só estímulo muito forte excita)"],
            ["Período refratário do átrio", "≈ 0,15 s (bem mais curto que o ventricular)"],
        ], [7.4, 10.0]),
        ("box", "Consequência clínica importante", "Como o período refratário dura quase toda a contração, <b>o coração não entra em "
               "tetania</b> e as extrassístoles <b>não somam</b> força como no músculo esquelético. O átrio, com refratário mais curto, "
               "consegue sustentar frequências muito mais altas (base do flutter e da fibrilação atrial)."),
    ]),
    ("4. Acoplamento excitação-contração", [
        ("ul", [
            "O potencial de ação percorre o sarcolema e entra pelos <b>túbulos T</b>.",
            "Nos túbulos T, abrem-se <b>canais de Ca²⁺ tipo L</b> (receptores de di-hidropiridina). O Ca²⁺ que entra do "
            "<b>líquido extracelular</b> ativa os <b>receptores de rianodina (RyR2)</b> do retículo sarcoplasmático, que liberam "
            "muito mais Ca²⁺: é a <b>liberação de cálcio induzida por cálcio</b>.",
            "O Ca²⁺ citosólico liga-se à <b>troponina C</b>, a tropomiosina se desloca e formam-se as <b>pontes cruzadas</b> actina-miosina.",
            "<b>Relaxamento</b>: fim do platô, o influxo de Ca²⁺ cessa. O Ca²⁺ é recaptado pela <b>SERCA2</b> (Ca²⁺-ATPase do RS) e "
            "expulso da célula pelo <b>trocador Na⁺/Ca²⁺ (NCX)</b>; o Na⁺ que entrou sai pela <b>Na⁺/K⁺-ATPase</b>.",
        ]),
        ("box", "Diferenças do músculo cardíaco em relação ao esquelético (cai muito em prova)", [
            "O <b>retículo sarcoplasmático é menos desenvolvido</b> e não armazena Ca²⁺ suficiente para uma contração completa.",
            "Os <b>túbulos T são 5× mais largos</b> (volume <b>25× maior</b>) e contêm <b>mucopolissacarídeos com carga negativa</b> que "
            "armazenam Ca²⁺ extracelular.",
            "Por isso a <b>força de contração depende muito da [Ca²⁺] extracelular</b>: um coração em solução sem cálcio para de bater "
            "rapidamente. Já o esquelético quase não é afetado por variações moderadas do Ca²⁺ extracelular.",
            "A <b>duração da contração</b> acompanha a do potencial de ação: ≈ 0,2 s no átrio e ≈ 0,3 s no ventrículo.",
        ]),
        ("tip", "Para conectar com a clínica (conhecimento complementar, não está no cap. 9)",
               "Bloqueadores dos canais de Ca²⁺ tipo L (verapamil, diltiazem) reduzem a força de contração; a digoxina inibe a "
               "Na⁺/K⁺-ATPase, diminui a saída de Ca²⁺ pelo NCX e aumenta a força (efeito inotrópico positivo). A estimulação "
               "β-adrenérgica fosforila canais L e fosfolambano, aumentando a força e acelerando o relaxamento."),
    ]),
    ("5. Ciclo cardíaco", [
        ("p", "Ciclo cardíaco = eventos entre o início de um batimento e o início do seguinte. Começa com um potencial de ação "
              "espontâneo no <b>nó sinusal</b> (parede superolateral do átrio direito, junto à veia cava superior). Há um "
              "<b>atraso de mais de 0,1 s</b> na passagem do impulso dos átrios aos ventrículos (nó e feixe AV), o que permite "
              "que os átrios contraiam antes e funcionem como <b>bombas de escorva</b>."),
        ("p", "Duração do ciclo = 1/FC. Com FC de 72 bpm, cada ciclo dura ≈ <b>0,833 s</b>. Quando a FC sobe, <b>a diástole encurta "
              "proporcionalmente mais que a sístole</b>: a sístole ocupa ≈ 0,4 do ciclo a 72 bpm e ≈ 0,65 com FC três vezes maior. "
              "Em taquicardias muito altas o enchimento ventricular fica incompleto."),
        ("fig", "fig/a_wiggers.png", "Figura 2. Diagrama de Wiggers do lado esquerdo (esquema com valores aproximados do Guyton). "
                "Linhas tracejadas: fechamento e abertura das valvas mitral e aórtica.", 14.5),
        ("h2", "ECG e ciclo mecânico"),
        ("ul", [
            "<b>Onda P</b>: despolarização atrial, seguida da contração atrial (onda <i>a</i> de pressão).",
            "<b>QRS</b>: aparece ≈ 0,16 s após o início da P; despolarização ventricular; começa <b>um pouco antes</b> da sístole ventricular.",
            "<b>Onda T</b>: repolarização ventricular; ocorre <b>um pouco antes do fim</b> da contração ventricular.",
        ]),
        ("h2", "Átrios como bombas de escorva e ondas de pressão atrial"),
        ("p", "Cerca de <b>80%</b> do enchimento ventricular ocorre passivamente, antes da contração atrial; a <b>contração atrial "
              "acrescenta ≈ 20%</b>. Como o coração pode bombear 300 a 400% mais do que o necessário em repouso, a perda da "
              "contração atrial (p. ex., fibrilação atrial) costuma passar despercebida em repouso, mas pode causar dispneia no "
              "esforço. Ventrículos rígidos (idade, hipertensão, diabetes, fibrose) dependem mais da contração atrial."),
        ("table", [
            ["Onda", "Momento", "Causa"],
            ["<b>a</b>", "Fim da diástole", "<b>Contração atrial</b>. AD sobe 4 a 6 mmHg; AE sobe 7 a 8 mmHg"],
            ["<b>c</b>", "Início da sístole ventricular", "Principalmente <b>abaulamento das valvas AV</b> para os átrios pela pressão ventricular (e leve refluxo)"],
            ["<b>v</b>", "Fim da sístole ventricular", "<b>Enchimento atrial</b> pelas veias com as valvas AV fechadas; some quando as AV abrem"],
        ], [1.6, 4.4, 11.4]),
        ("h2", "As fases do ciclo (lado esquerdo)"),
        ("table", [
            ["Fase", "Valvas", "Duração / valores", "O que acontece"],
            ["Enchimento rápido", "AV abertas; semilunares fechadas", "1º terço da diástole", "Sangue acumulado nos átrios durante a sístole entra rapidamente"],
            ["Diástase", "AV abertas", "Terço médio", "Pouco fluxo: sangue que chega das veias passa direto"],
            ["Sístole atrial", "AV abertas", "Último terço; ≈ 20% do enchimento", "Complementa o volume diastólico final"],
            ["Contração isovolumétrica", "<b>Todas fechadas</b>", "0,02 a 0,03 s", "Tensão sobe, volume constante. Termina quando PVE &gt; ≈ 80 mmHg (PVD &gt; ≈ 8 mmHg)"],
            ["Ejeção rápida", "Semilunares abertas", "1º terço da ejeção: ≈ 70% do volume ejetado", ""],
            ["Ejeção lenta", "Semilunares abertas", "2/3 finais: ≈ 30%", ""],
            ["Relaxamento isovolumétrico", "<b>Todas fechadas</b>", "0,03 a 0,06 s", "Pressão cai até abaixo da atrial; então abrem as AV"],
        ], [3.6, 3.4, 4.2, 6.2]),
        ("h2", "Volumes"),
        ("table", [
            ["Grandeza", "Normal", "Faixa possível"],
            ["Volume diastólico final (VDF)", "110 a 120 mℓ", "até 150 a 180 mℓ"],
            ["Volume sistólico (débito sistólico, VS)", "≈ 70 mℓ", "pode mais que dobrar"],
            ["Volume sistólico final (VSF)", "40 a 50 mℓ", "até 10 a 20 mℓ com contração forte"],
            ["Fração de ejeção (VS/VDF)", "≈ 0,6 (60%)", "índice clínico da função sistólica"],
        ], [7.0, 4.2, 6.2]),
    ]),
    ("6. Valvas cardíacas", [
        ("p", "As valvas <b>abrem e fecham passivamente</b>, conforme o gradiente de pressão: fecham com gradiente retrógrado e "
              "abrem com gradiente anterógrado. As <b>AV</b> (tricúspide e mitral) impedem refluxo ventrículo → átrio na sístole; "
              "as <b>semilunares</b> (aórtica e pulmonar) impedem refluxo artéria → ventrículo na diástole."),
        ("table", [
            ["", "Valvas AV (mitral, tricúspide)", "Valvas semilunares (aórtica, pulmonar)"],
            ["Estrutura", "Finas, com <b>cordas tendíneas e músculos papilares</b>", "Tecido fibroso forte e flexível; <b>sem cordas</b>"],
            ["Fechamento", "Suave, quase sem refluxo", "<b>Abrupto</b> (alta pressão arterial no fim da sístole), com pequeno refluxo de milissegundos"],
            ["Velocidade do fluxo", "Menor (orifício grande)", "<b>Maior</b> (orifício menor)"],
            ["Desgaste", "Menor", "<b>Maior abrasão mecânica</b> nas bordas"],
            ["Som de fechamento", "<b>B1</b>: grave, mais longo (≈ 0,14 s)", "<b>B2</b>: agudo, estalido curto (≈ 0,11 s)"],
        ], [3.0, 7.0, 7.4]),
        ("box", "Músculos papilares: pegadinha clássica", [
            "Contraem junto com a parede ventricular, mas <b>NÃO ajudam a fechar as valvas</b>.",
            "Eles puxam as cúspides em direção ao ventrículo, <b>impedindo que abaulem demais (prolapsem) para o átrio</b> na sístole.",
            "Ruptura de corda tendínea ou paralisia do músculo papilar (p. ex., isquemia no infarto) → a valva everte e vaza: "
            "<b>insuficiência mitral aguda</b>, que pode causar insuficiência cardíaca grave ou letal.",
        ]),
        ("h2", "Curva de pressão aórtica"),
        ("ul", [
            "Após a abertura da valva aórtica, a pressão no VE sobe mais devagar porque o sangue já está saindo para a aorta.",
            "A distensão das artérias elásticas leva a pressão a ≈ <b>120 mmHg</b> (sistólica).",
            "<b>Incisura</b> (nó dicrótico): pequeno refluxo logo antes do fechamento aórtico, seguido da interrupção súbita desse refluxo.",
            "Na diástole a pressão cai lentamente (as artérias elásticas continuam empurrando sangue para a periferia) até ≈ <b>80 mmHg</b> (diastólica).",
            "No VD e na artéria pulmonar as curvas são semelhantes, mas as pressões são ≈ <b>1/6</b> das esquerdas.",
        ]),
        ("h2", "Bulhas cardíacas (Guyton, cap. 23)"),
        ("table", [
            ["Bulha", "Causa", "Quando / significado"],
            ["<b>B1</b>", "Fechamento das AV e vibração de valvas tensas, cordas, sangue e paredes", "Início da sístole; grave e mais longa"],
            ["<b>B2</b>", "Fechamento das semilunares e reverberação entre artéria, valva e ventrículo", "Fim da sístole; mais aguda (valvas mais retesadas, paredes arteriais mais elásticas)"],
            ["<b>B3</b>", "Oscilação do sangue que entra no ventrículo no enchimento", "Início do terço médio da diástole; normal em crianças e jovens, em idosos sugere <b>IC sistólica</b>"],
            ["<b>B4</b>", "Contração atrial empurrando sangue para ventrículo pouco complacente", "Fim da diástole; <b>hipertrofia do VE</b> em idosos, ventrículo rígido. Não existe em fibrilação atrial"],
        ], [1.4, 8.0, 8.0]),
        ("p", "A abertura das valvas normalmente <b>não produz som</b> (processo lento). Os focos de ausculta não ficam sobre as "
              "valvas: o aórtico e o pulmonar ficam acima, ao longo das artérias; o tricúspide sobre o VD; o mitral no ápice do VE."),
        ("tip", "Ponte com valvopatias (cap. 23)",
               "Febre reumática lesa mais a <b>mitral</b> e depois a <b>aórtica</b> (valvas de alta pressão). A <b>estenose aórtica "
               "calcificada senil</b> é hoje a valvopatia mais comum: causa hipertrofia concêntrica do VE, gradiente de 75 a 100 mmHg "
               "nos casos graves, sopro sistólico áspero irradiado para o pescoço, e a tríade angina, síncope e dispneia aos esforços."),
    ]),
    ("7. Trabalho cardíaco e alça pressão-volume", [
        ("p", "<b>Trabalho sistólico</b> = energia convertida em trabalho a cada batimento. Tem duas partes: (1) <b>trabalho "
              "pressão-volume (externo)</b>, a maior parte, para levar sangue das veias de baixa pressão para as artérias de alta "
              "pressão; (2) <b>energia cinética</b>, ≈ 1% do total no VE normal, proporcional a massa × velocidade². Na "
              "<b>estenose aórtica</b> a energia cinética pode passar de <b>50%</b> do trabalho total. O trabalho externo do VD é "
              "≈ 1/6 do VE."),
        ("fig", "fig/a_alca_pv.png", "Figura 3. Alça pressão-volume do VE. A área interna é o trabalho externo (TE).", 11.5),
        ("table", [
            ["Fase da alça", "Trecho", "Detalhe"],
            ["I · enchimento", "A → B", "De ≈ 50 mℓ (VSF) e 2 a 3 mmHg até ≈ 120 mℓ (VDF) e 5 a 7 mmHg"],
            ["II · contração isovolumétrica", "B → C", "Volume fixo; pressão sobe até ≈ 80 mmHg (pressão aórtica diastólica): abre a aórtica"],
            ["III · ejeção", "C → D", "Volume cai 70 mℓ; pressão sobe ao pico e depois cai; em D fecha a aórtica"],
            ["IV · relaxamento isovolumétrico", "D → A", "Volume fixo; pressão cai ao nível diastólico; abre a mitral"],
        ], [5.0, 2.0, 10.4]),
        ("ul", [
            "Curva de <b>pressão diastólica</b>: quase plana até ≈ 150 mℓ; acima disso sobe muito (tecido fibroso e pericárdio no limite).",
            "Curva de <b>pressão sistólica</b>: máxima com 150 a 170 mℓ; acima disso cai (sobreposição actina-miosina menos que ideal). "
            "Pico isovolumétrico máximo: <b>250 a 300 mmHg no VE</b> e <b>60 a 80 mmHg no VD</b>.",
            "Com mais retorno venoso e estímulo simpático, a alça fica mais larga (mais VDF), mais alta (mais pressão) e vai mais à esquerda (menor VSF).",
        ]),
        ("box", "Pré-carga e pós-carga (definições do Guyton)", [
            "<b>Pré-carga</b>: tensão do músculo ao começar a contrair; para o ventrículo, a <b>pressão diastólica final</b> (ventrículo cheio).",
            "<b>Pós-carga</b>: carga contra a qual o músculo contrai; para o ventrículo, a <b>pressão na artéria de saída</b> (aorta). "
            "Às vezes, de forma menos precisa, fala-se da resistência vascular.",
        ]),
        ("h2", "Consumo de O₂ e eficiência"),
        ("ul", [
            "Combustível: <b>70 a 90% ácidos graxos</b> (metabolismo oxidativo); 10 a 30% glicose e lactato.",
            "O consumo de O₂ é proporcional à área <b>TE + EP</b> (energia potencial) e ao <b>índice tensão-tempo</b>.",
            "<b>Lei de Laplace</b>: T = P × r. Pressão sistólica alta → mais tensão → mais O₂. Sobrecarga de pressão crônica → "
            "<b>hipertrofia concêntrica</b> (parede grossa, raio menor, alivia a tensão). Ventrículo <b>dilatado</b> (hipertrofia "
            "excêntrica) gasta mais energia para a mesma pressão, porque o raio é maior; paradoxo da insuficiência cardíaca.",
            "<b>Eficiência</b> máxima do coração normal: <b>20 a 25%</b> (resto vira calor); na insuficiência cardíaca pode cair a 5%.",
        ]),
    ]),
    ("8. Regulação do bombeamento", [
        ("p", "Débito cardíaco de repouso: <b>4 a 6 ℓ/min</b>; no exercício intenso, <b>4 a 7 vezes</b> mais. Dois mecanismos: "
              "(1) <b>regulação intrínseca</b> (Frank-Starling) e (2) <b>controle autonômico</b> da frequência e da força."),
        ("h2", "Mecanismo de Frank-Starling"),
        ("box", "Frank-Starling em uma frase",
               "Dentro dos limites fisiológicos, <b>o coração bombeia todo o sangue que volta a ele pelas veias</b>: quanto mais o "
               "músculo é distendido no enchimento, maior a força de contração e o volume ejetado."),
        ("ul", [
            "Mecanismo: o estiramento leva actina e miosina a um grau de <b>sobreposição mais próximo do ideal</b>. É propriedade de todo músculo estriado.",
            "O débito cardíaco é determinado principalmente pelo <b>retorno venoso</b>, que é a soma dos fluxos locais dos tecidos (tema g).",
            "Estiramento do átrio direito também <b>aumenta a FC em 10 a 20%</b> diretamente (nó sinusal) e ativa o <b>reflexo de Bainbridge</b> "
            "(via vago), que pode aumentar a FC em mais 40 a 60%.",
            "<b>Curvas de função ventricular</b> (trabalho sistólico ou débito ventricular × pressão atrial) são a expressão gráfica de Frank-Starling.",
        ]),
        ("h2", "Controle autonômico"),
        ("table", [
            ["", "Simpático", "Parassimpático (vago)"],
            ["Frequência cardíaca", "De ≈ 70 para 180 a 200 bpm (raramente 250)", "Estímulo forte pode parar o coração por segundos; depois \"escapa\" a 20 a 40 bpm"],
            ["Força de contração", "Pode <b>dobrar</b>", "Reduz 20 a 30% (fibras vagais vão sobretudo aos <b>átrios</b>)"],
            ["Débito cardíaco", "Aumenta 2 a 3 vezes (além do Frank-Starling); &gt; 100% a uma mesma pressão atrial", "Pode cair 50% ou mais; quase a zero com estímulo máximo"],
            ["Tônus basal", "Mantém o bombeamento ≈ 30% acima do que seria sem simpático; inibição reduz até 30%", "Predomina no repouso sobre a FC"],
        ], [3.6, 6.8, 7.0]),
        ("h2", "Íons e temperatura"),
        ("table", [
            ["Situação", "Efeito no coração"],
            ["<b>Hiperpotassemia</b>", "Coração <b>dilatado e flácido</b>, FC ↓, bloqueio AV. 8 a 12 mEq/ℓ (2 a 3× o normal) pode matar. "
                                      "Mecanismo: despolariza parcialmente o repouso → potencial de ação menor → contração mais fraca"],
            ["<b>Hipercalcemia</b>", "Tendência à <b>contração espástica</b> (efeito oposto ao K⁺)"],
            ["<b>Hipocalcemia</b>", "Fraqueza cardíaca (semelhante ao K⁺ alto). Clinicamente raro, pois o Ca²⁺ é muito bem regulado"],
            ["<b>Febre</b>", "FC ↑ (até o dobro): calor aumenta a permeabilidade iônica e acelera a autoexcitação. Elevação moderada "
                             "aumenta a força; elevação prolongada esgota o metabolismo e enfraquece"],
            ["<b>Hipotermia</b>", "FC ↓ muito; poucos batimentos/min com 15,5 a 21 °C"],
        ], [3.6, 13.8]),
        ("box", "Pós-carga e débito cardíaco",
               "Aumentar a pressão arterial <b>não reduz o débito cardíaco</b> até a pressão arterial média passar de ≈ <b>160 mmHg</b>. "
               "Na faixa normal, quem determina o débito é a facilidade do fluxo pelos tecidos, ou seja, o <b>retorno venoso</b>."),
    ]),
    ("9. Números para decorar", [
        ("table", [
            ["Item", "Valor"],
            ["Potencial de repouso ventricular / pico", "−85 mV / +20 mV (amplitude 105 mV)"],
            ["Duração do platô", "≈ 0,2 s (canais de Ca²⁺ fecham em 0,2 a 0,3 s)"],
            ["Refratário absoluto ventricular / relativo / atrial", "0,25 a 0,30 s / +0,05 s / 0,15 s"],
            ["Condução muscular / Purkinje", "0,3 a 0,5 m/s / até 4 m/s"],
            ["Atraso AV", "&gt; 0,1 s; QRS ≈ 0,16 s após o início da P"],
            ["Ciclo a 72 bpm", "0,833 s; sístole ≈ 40% do ciclo (≈ 65% com FC 3×)"],
            ["Contribuição atrial ao enchimento", "≈ 20% (80% passivo)"],
            ["Onda a: AD / AE", "+4 a 6 / +7 a 8 mmHg"],
            ["Contração isovolumétrica / relaxamento isovolumétrico", "0,02 a 0,03 s / 0,03 a 0,06 s"],
            ["Abertura semilunar: VE / VD", "&gt; 80 mmHg / &gt; 8 mmHg"],
            ["VDF / VS / VSF / FE", "110 a 120 / 70 / 40 a 50 mℓ / 60%"],
            ["Ejeção rápida", "70% do volume no 1º terço da ejeção"],
            ["Aorta", "120/80 mmHg; pulmonar ≈ 1/6"],
            ["Energia cinética no trabalho do VE", "≈ 1% (normal); &gt; 50% (estenose aórtica)"],
            ["Pico sistólico isovolumétrico: VE / VD", "250 a 300 / 60 a 80 mmHg"],
            ["Substrato energético", "70 a 90% ácidos graxos"],
            ["Eficiência cardíaca", "20 a 25% (IC: até 5%)"],
            ["Débito cardíaco repouso / exercício", "4 a 6 ℓ/min / 4 a 7×"],
            ["Bainbridge / estiramento direto do nó SA", "FC +40 a 60% / +10 a 20%"],
            ["Simpático máximo / escape vagal", "180 a 200 bpm / 20 a 40 bpm"],
            ["K⁺ letal", "8 a 12 mEq/ℓ"],
            ["Pressão média a partir da qual o DC cai", "&gt; 160 mmHg"],
        ], [8.4, 9.0]),
    ]),
]

MCQ = [
    dict(q="O potencial de ação da fibra muscular ventricular apresenta um platô prolongado. Esse platô se deve principalmente a:",
         opts=["Abertura prolongada dos canais rápidos de Na⁺ dependentes de voltagem",
               "Entrada de Ca²⁺ por canais tipo L associada à redução da permeabilidade ao K⁺",
               "Ativação da Na⁺/K⁺-ATPase, que gera corrente despolarizante",
               "Liberação de Ca²⁺ do retículo sarcoplasmático para o líquido extracelular",
               "Aumento da permeabilidade ao Cl⁻ durante a fase 2"],
         a=1, c="O platô (fase 2) resulta de duas diferenças em relação ao músculo esquelético: canais lentos de Ca²⁺ tipo L que "
                "ficam abertos por décimos de segundo e queda de cerca de 5 vezes da permeabilidade ao K⁺. Os canais rápidos de Na⁺ "
                "ficam abertos só por milésimos de segundo, por isso não sustentam o platô."),
    dict(q="Qual é a principal consequência funcional do longo período refratário do músculo ventricular?",
         opts=["Permitir a somação de ondas para aumentar a força",
               "Aumentar a velocidade de condução nas fibras de Purkinje",
               "Impedir a tetania, garantindo o relaxamento e o enchimento entre os batimentos",
               "Tornar o ventrículo capaz de responder a frequências maiores que o átrio",
               "Eliminar o período refratário relativo"],
         a=2, c="O período refratário absoluto ventricular (0,25 a 0,30 s) dura quase toda a contração. Por isso não há somação nem "
                "tetania, e o ventrículo relaxa e enche a cada ciclo. O átrio tem refratário mais curto (≈ 0,15 s) e aceita "
                "frequências mais altas, e não o ventrículo."),
    dict(q="Sobre o acoplamento excitação-contração no músculo cardíaco, assinale a alternativa correta:",
         opts=["O Ca²⁺ que inicia a contração vem exclusivamente do retículo sarcoplasmático, como no músculo esquelético",
               "Os túbulos T cardíacos têm diâmetro menor que os do músculo esquelético",
               "O Ca²⁺ que entra pelos canais tipo L do túbulo T ativa os receptores de rianodina, liberando Ca²⁺ do retículo sarcoplasmático",
               "A força de contração cardíaca é pouco afetada pela concentração extracelular de Ca²⁺",
               "O relaxamento depende exclusivamente da Na⁺/K⁺-ATPase"],
         a=2, c="É a liberação de Ca²⁺ induzida por Ca²⁺: o Ca²⁺ extracelular entra pelos canais L do túbulo T e abre os RyR2. "
                "Os túbulos T cardíacos são 5× mais largos, a força depende muito do Ca²⁺ extracelular e o relaxamento envolve "
                "SERCA2 e o trocador Na⁺/Ca²⁺ (com a Na⁺/K⁺-ATPase removendo o Na⁺)."),
    dict(q="Um coração isolado perfundido com solução sem cálcio para de bater rapidamente. A melhor explicação é:",
         opts=["O retículo sarcoplasmático cardíaco é pouco desenvolvido e a contração depende do Ca²⁺ que chega pelos túbulos T do meio extracelular",
               "Sem Ca²⁺ extracelular, os canais rápidos de Na⁺ não abrem",
               "O Ca²⁺ é necessário para abrir as junções comunicantes dos discos intercalares",
               "A falta de Ca²⁺ causa hiperpolarização e parada em sístole",
               "O Ca²⁺ extracelular é o principal determinante do potencial de repouso"],
         a=0, c="O retículo sarcoplasmático cardíaco não armazena Ca²⁺ suficiente para a contração completa. Os túbulos T, abertos ao "
                "interstício e ricos em mucopolissacarídeos que ligam Ca²⁺, fornecem o cálcio extracelular que dispara e complementa a contração."),
    dict(q="Os discos intercalares do miocárdio são importantes porque:",
         opts=["Isolam eletricamente cada cardiomiócito, impedindo arritmias",
               "Contêm junções comunicantes de baixa resistência que fazem o miocárdio funcionar como sincício",
               "São o local de armazenamento de Ca²⁺ para a contração",
               "Conduzem o impulso dos átrios para os ventrículos através do esqueleto fibroso",
               "Geram o potencial de ação espontâneo"],
         a=1, c="Nos discos intercalares as membranas se fundem em gap junctions, que permitem a difusão rápida de íons entre as "
                "células. Assim o potencial de ação passa de célula a célula (sincício funcional). A passagem átrio → ventrículo "
                "acontece apenas pelo feixe AV, e não pelo esqueleto fibroso."),
    dict(q="Por que átrios e ventrículos constituem dois sincícios funcionais separados?",
         opts=["Porque os átrios não têm discos intercalares",
               "Porque o nó sinusal fica no ventrículo",
               "Porque o potencial de ação atrial não tem fase 0",
               "Porque o tecido fibroso dos anéis AV isola os dois, e o impulso só atravessa pelo feixe AV",
               "Porque o miocárdio ventricular não tem junções comunicantes"],
         a=3, c="O esqueleto fibroso ao redor das valvas AV não conduz o impulso. A condução só ocorre pelo sistema especializado "
                "(feixe AV), o que permite que os átrios contraiam um pouco antes dos ventrículos."),
    dict(q="Qual evento do ciclo cardíaco corresponde ao período em que TODAS as valvas cardíacas estão fechadas e a pressão ventricular esquerda sobe de ≈ 8 para ≈ 80 mmHg?",
         opts=["Ejeção rápida", "Enchimento rápido", "Diástase", "Relaxamento isovolumétrico", "Contração isovolumétrica"],
         a=4, c="Na contração isovolumétrica (0,02 a 0,03 s), a mitral já fechou e a aórtica ainda não abriu. A tensão sobe sem "
                "mudança de volume até a pressão do VE superar a aórtica (≈ 80 mmHg)."),
    dict(q="Com relação às ondas de pressão atrial, a onda c é causada principalmente por:",
         opts=["Contração atrial",
               "Enchimento atrial pelas veias com as valvas AV fechadas",
               "Abaulamento das valvas AV em direção aos átrios no início da contração ventricular",
               "Abertura das valvas AV no início da diástole",
               "Fechamento das valvas semilunares"],
         a=2, c="A onda a é a contração atrial; a onda c ocorre no início da sístole ventricular, principalmente pelo abaulamento das "
                "valvas AV para os átrios (e leve refluxo); a onda v resulta do enchimento atrial com as AV fechadas, no fim da sístole."),
    dict(q="Em um adulto saudável em repouso, qual é a contribuição aproximada da contração atrial para o enchimento ventricular?",
         opts=["5%", "20%", "50%", "80%", "100%"], keep=True,
         a=1, c="Cerca de 80% do sangue passa passivamente dos átrios aos ventrículos; a contração atrial acrescenta ≈ 20%. Por isso "
                "a perda da contração atrial costuma dar sintomas só no esforço (reserva de 300 a 400%)."),
    dict(q="Um homem saudável tem volume diastólico final de 120 mℓ e volume sistólico final de 50 mℓ. Sua fração de ejeção e seu volume sistólico são, respectivamente:",
         opts=["42% e 50 mℓ", "58% e 70 mℓ", "70% e 120 mℓ", "60% e 50 mℓ", "41% e 70 mℓ"],
         a=1, c="VS = VDF − VSF = 120 − 50 = 70 mℓ. FE = VS/VDF = 70/120 ≈ 0,58 (≈ 60%, valor normal citado no Guyton)."),
    dict(q="Durante o período de ejeção ventricular:",
         opts=["O volume ejetado distribui-se igualmente ao longo de toda a ejeção",
               "Cerca de 70% do volume sistólico sai no primeiro terço do período de ejeção",
               "A valva mitral está aberta",
               "O ventrículo ejeta cerca de 100% do volume diastólico final",
               "A pressão ventricular é sempre menor que a aórtica"],
         a=1, c="O primeiro terço é a ejeção rápida (≈ 70% do volume ejetado); os dois terços finais, a ejeção lenta (≈ 30%). "
                "Normalmente sai ≈ 60% do VDF."),
    dict(q="Um estudante afirma que os músculos papilares se contraem para fechar as valvas mitral e tricúspide. Sobre essa afirmação:",
         opts=["Está correta, pois sem eles as valvas AV ficariam abertas na sístole",
               "Está incorreta: os músculos papilares puxam as cúspides para o ventrículo, evitando o abaulamento excessivo para os átrios",
               "Está correta apenas para a valva tricúspide",
               "Está incorreta, pois os músculos papilares só se contraem na diástole",
               "Está incorreta, pois os músculos papilares estão ligados às valvas semilunares"],
         a=1, c="As valvas fecham passivamente pelo gradiente de pressão. Os músculos papilares contraem junto com a parede e, pelas "
                "cordas tendíneas, impedem que as cúspides prolapsem para os átrios. Sua disfunção (infarto) causa insuficiência mitral."),
    dict(q="Qual característica é das valvas semilunares, e não das valvas AV?",
         opts=["São sustentadas por cordas tendíneas",
               "Fecham-se de forma suave, quase sem refluxo",
               "Por elas o sangue passa com menor velocidade",
               "Fecham-se abruptamente e sofrem maior abrasão mecânica",
               "Seu fechamento gera a primeira bulha"],
         a=3, c="As semilunares fecham abruptamente pela alta pressão arterial no fim da sístole, têm orifício menor (maior velocidade) "
                "e sofrem mais abrasão. Não têm cordas tendíneas. B1 vem do fechamento das AV."),
    dict(q="A incisura (nó dicrótico) da curva de pressão aórtica corresponde a:",
         opts=["Abertura da valva aórtica",
               "Contração atrial",
               "Breve refluxo de sangue seguido da interrupção súbita quando a valva aórtica se fecha",
               "Pico da ejeção rápida",
               "Abertura da valva mitral"],
         a=2, c="Logo antes do fechamento da valva aórtica ocorre um pequeno refluxo, interrompido bruscamente pelo fechamento; isso "
                "produz a incisura, que coincide com B2."),
    dict(q="A primeira bulha cardíaca (B1):",
         opts=["É causada pela abertura das valvas semilunares",
               "É mais aguda e mais curta que B2",
               "Ocorre no fim da diástole por contração atrial",
               "É causada pelo fechamento das valvas AV e é grave e relativamente longa",
               "É normalmente inaudível ao estetoscópio"],
         a=3, c="B1 = fechamento das AV no início da sístole: grave e com ≈ 0,14 s. B2 (semilunares) é mais aguda e curta (≈ 0,11 s). "
                "A abertura das valvas não produz som."),
    dict(q="Em um idoso com hipertrofia ventricular esquerda por hipertensão, ausculta-se um som de baixa frequência imediatamente antes de B1. Esse som:",
         opts=["É B3 e indica sobrecarga de volume",
               "É B4, gerado pela contração atrial contra um ventrículo pouco complacente",
               "É um estalido de abertura mitral",
               "É B2 desdobrado",
               "Estaria presente mesmo em fibrilação atrial"],
         a=1, c="B4 ocorre na sístole atrial (fim da diástole, logo antes de B1) quando o ventrículo tem complacência reduzida, como na "
                "HVE do idoso. Como depende da contração atrial, desaparece na fibrilação atrial."),
    dict(q="Qual afirmação sobre a terceira bulha (B3) está correta segundo o Guyton?",
         opts=["Ocorre no início do terço médio da diástole e pode ser normal em crianças e adultos jovens",
               "Resulta do fechamento das valvas semilunares",
               "Ocorre durante a contração isovolumétrica",
               "É sempre patológica",
               "É causada pela contração atrial"],
         a=0, c="B3 ocorre no início do terço médio da diástole, pela oscilação do sangue que entra no ventrículo. É normal em jovens; "
                "em idosos geralmente indica insuficiência cardíaca sistólica."),
    dict(q="Quando a frequência cardíaca aumenta muito (por exemplo, triplica), o que acontece com o ciclo cardíaco?",
         opts=["Sístole e diástole encurtam na mesma proporção",
               "Só a sístole encurta",
               "A diástole encurta proporcionalmente mais, e a sístole passa a ocupar ≈ 65% do ciclo",
               "A duração do potencial de ação aumenta",
               "O enchimento ventricular melhora"],
         a=2, c="A sístole ocupa ≈ 40% do ciclo a 72 bpm e ≈ 65% com FC três vezes maior. A diástole encurta mais, e o enchimento pode "
                "ficar incompleto em taquicardias muito altas."),
    dict(q="Na alça pressão-volume do ventrículo esquerdo, a área interna da alça representa:",
         opts=["A fração de ejeção",
               "O trabalho sistólico externo do ventrículo",
               "O consumo total de O₂ do miocárdio",
               "A complacência ventricular",
               "A energia potencial"],
         a=1, c="A área da alça (TE) é o trabalho externo líquido por batimento. O consumo de O₂ é proporcional a TE + EP (energia potencial)."),
    dict(q="Em qual situação a energia cinética do fluxo sanguíneo pode representar mais de 50% do trabalho do ventrículo esquerdo?",
         opts=["Exercício físico moderado", "Insuficiência mitral", "Estenose aórtica", "Bradicardia sinusal", "Hipovolemia"],
         a=2, c="Normalmente a energia cinética é ≈ 1% do trabalho do VE. Na estenose aórtica o sangue atravessa o orifício estreito com "
                "velocidade muito alta, e como a energia cinética é proporcional a massa × velocidade², ela pode passar de 50%."),
    dict(q="Segundo o Guyton, a pré-carga e a pós-carga ventriculares são, respectivamente:",
         opts=["Pressão aórtica e pressão diastólica final",
               "Volume sistólico e resistência periférica",
               "Pressão diastólica final e pressão na artéria de saída do ventrículo",
               "Frequência cardíaca e contratilidade",
               "Pressão atrial média e pressão venosa central"],
         a=2, c="Pré-carga = tensão ao iniciar a contração, representada pela pressão diastólica final. Pós-carga = carga contra a qual o "
                "ventrículo contrai, a pressão na aorta (ou artéria pulmonar)."),
    dict(q="De acordo com a lei de Laplace aplicada ao ventrículo, qual situação aumenta mais o consumo de O₂ para gerar a mesma pressão sistólica?",
         opts=["Ventrículo com hipertrofia concêntrica",
               "Ventrículo dilatado (raio aumentado)",
               "Redução do volume diastólico final",
               "Bradicardia",
               "Redução da pressão arterial"],
         a=1, c="T = P × r. Com o raio maior (ventrículo dilatado), a tensão da parede e o gasto de energia sobem para a mesma pressão. "
                "A hipertrofia concêntrica, ao contrário, reduz o raio e alivia a tensão."),
    dict(q="O principal substrato energético do miocárdio em repouso e a eficiência máxima do coração normal são:",
         opts=["Glicose; 50%", "Ácidos graxos; 20 a 25%", "Lactato; 5%", "Corpos cetônicos; 40%", "Aminoácidos; 20 a 25%"],
         a=1, c="70 a 90% da energia vem da oxidação de ácidos graxos. A eficiência (trabalho/energia química) é de 20 a 25%; na "
                "insuficiência cardíaca pode cair a 5%."),
    dict(q="O mecanismo de Frank-Starling é explicado principalmente por:",
         opts=["Aumento da frequência cardíaca pelo estiramento atrial",
               "Liberação de noradrenalina pelo estiramento ventricular",
               "Aproximação da sobreposição de actina e miosina ao grau ideal quando a fibra é distendida",
               "Aumento da condução no feixe AV",
               "Redução da pós-carga com o aumento do volume"],
         a=2, c="Mais enchimento distende as fibras e leva a sobreposição actina-miosina a um ponto mais próximo do ótimo, aumentando a "
                "força. O aumento da FC pelo estiramento atrial (10 a 20%) e o reflexo de Bainbridge são efeitos adicionais e menores."),
    dict(q="Sobre o controle autonômico do coração, assinale a correta:",
         opts=["A estimulação vagal reduz principalmente a força de contração ventricular, pois o vago inerva sobretudo os ventrículos",
               "A estimulação simpática pode dobrar a força de contração e elevar a FC para 180 a 200 bpm",
               "Sem tônus simpático basal, o bombeamento aumenta 30%",
               "A estimulação vagal intensa mantida causa parada cardíaca definitiva",
               "O simpático não altera a curva de função cardíaca"],
         a=1, c="O simpático pode dobrar a força e levar a FC a 180 a 200 bpm, aumentando o débito 2 a 3 vezes. O vago inerva sobretudo "
                "os átrios (efeito principal na FC). Após parada vagal, o coração \"escapa\" a 20 a 40 bpm. O tônus simpático basal "
                "mantém o bombeamento ≈ 30% acima do que seria sem ele."),
    dict(q="O reflexo de Bainbridge:",
         opts=["Reduz a FC quando a pressão arterial aumenta",
               "Aumenta a FC em resposta ao estiramento atrial, por via vagal aferente",
               "Aumenta a contratilidade pelo estiramento ventricular",
               "É mediado por quimiorreceptores carotídeos",
               "Diminui o retorno venoso"],
         a=1, c="O estiramento atrial ativa receptores que, por via do vago, aumentam a FC em 40 a 60%, ajudando o coração a bombear o "
                "volume extra que chega. Quem reduz a FC com PA alta é o barorreflexo, não o Bainbridge."),
    dict(q="Paciente com insuficiência renal apresenta K⁺ sérico de 9 mEq/ℓ. O efeito esperado sobre o coração é:",
         opts=["Contração espástica e taquicardia",
               "Coração dilatado e flácido, bradicardia e possível bloqueio AV",
               "Aumento da amplitude do potencial de ação",
               "Hiperpolarização do potencial de repouso",
               "Nenhum efeito relevante"],
         a=1, c="O K⁺ extracelular alto despolariza parcialmente o repouso, diminui a amplitude do potencial de ação e enfraquece a "
                "contração. O coração fica dilatado e flácido, a FC cai e pode haver bloqueio AV. Com 8 a 12 mEq/ℓ pode haver morte."),
    dict(q="O excesso de Ca²⁺ no líquido extracelular tende a causar:",
         opts=["Contração espástica", "Coração flácido", "Aumento do período refratário atrial", "Bloqueio AV total", "Redução da FC por febre"],
         a=0, c="O Ca²⁺ em excesso tem efeito quase oposto ao do K⁺ alto, levando o coração à contração espástica. A hipocalcemia causa fraqueza."),
    dict(q="Um paciente tem febre de 39,5 °C. Espera-se:",
         opts=["Bradicardia pela redução da permeabilidade iônica",
               "Aumento da FC, pois o calor aumenta a permeabilidade da membrana e acelera a autoexcitação",
               "Nenhuma alteração da FC",
               "Redução imediata e permanente da força de contração",
               "Bloqueio AV por hiperpotassemia"],
         a=1, c="A febre aumenta muito a FC (às vezes até o dobro). Elevação moderada aumenta temporariamente a força; elevação "
                "prolongada esgota o metabolismo e enfraquece o coração."),
    dict(q="Segundo o Guyton, o aumento da pressão arterial (pós-carga) passa a reduzir significativamente o débito cardíaco de um coração normal quando a pressão arterial média ultrapassa cerca de:",
         opts=["80 mmHg", "100 mmHg", "120 mmHg", "140 mmHg", "160 mmHg"], keep=True,
         a=4, c="O débito cardíaco se mantém até a pressão média ≈ 160 mmHg. Na faixa normal, quem determina o débito é o retorno venoso "
                "(fluxo pelos tecidos), não a pós-carga."),
    dict(q="Qual das afirmações sobre a torção do ventrículo esquerdo é correta?",
         opts=["As fibras subepicárdicas e subendocárdicas têm a mesma orientação",
               "Na sístole, o ápice gira em sentido anti-horário e a base em sentido horário",
               "A destorção na diástole funciona como mola e favorece a entrada rápida de sangue",
               "A torção dificulta a ejeção",
               "A torção ocorre apenas no ventrículo direito"],
         a=2, c="Subepicárdicas em hélice à esquerda e subendocárdicas à direita. Na sístole o ápice gira no sentido horário e a base no "
                "anti-horário, puxando a base ao ápice. Na diástole o VE \"destorce\" como uma mola comprimida, ajudando o enchimento rápido."),
    dict(q="Na curva de pressão diastólica do VE (relação volume-pressão passiva), a pressão sobe acentuadamente quando o volume ultrapassa ≈ 150 mℓ. Isso ocorre porque:",
         opts=["As valvas AV se fecham",
               "O tecido fibroso cardíaco não se estica mais e o pericárdio chega perto do seu limite",
               "A actina e a miosina se sobrepõem demais",
               "Aumenta a atividade simpática",
               "A valva aórtica se abre"],
         a=1, c="Até ≈ 150 mℓ o ventrículo enche com pouca variação de pressão. Acima disso, o tecido fibroso e o pericárdio limitam a "
                "distensão, e a pressão diastólica sobe rapidamente."),
    dict(q="O atraso de mais de 0,1 s na passagem do impulso dos átrios para os ventrículos tem como função:",
         opts=["Permitir que o nó sinusal repolarize",
               "Permitir que os átrios contraiam e completem o enchimento ventricular antes da sístole ventricular",
               "Gerar a onda T",
               "Reduzir a velocidade das fibras de Purkinje",
               "Evitar a abertura das valvas semilunares"],
         a=1, c="O atraso AV faz os átrios funcionarem como bombas de escorva, contraindo antes dos ventrículos e acrescentando ≈ 20% ao enchimento."),
    dict(q="Qual afirmação sobre as pressões do lado direito do coração está correta?",
         opts=["A valva pulmonar abre quando a pressão do VD ultrapassa ≈ 80 mmHg",
               "As pressões do VD e da artéria pulmonar são ≈ 1/6 das pressões do lado esquerdo",
               "O trabalho externo do VD é igual ao do VE",
               "A pressão sistólica máxima do VD normal é de 250 a 300 mmHg",
               "A onda a do átrio direito é maior que a do esquerdo"],
         a=1, c="A pulmonar abre com PVD acima de ≈ 8 mmHg. As pressões direitas são ≈ 1/6 das esquerdas, e o trabalho externo do VD "
                "também. O pico isovolumétrico do VD é 60 a 80 mmHg. A onda a é de 4 a 6 mmHg no AD e 7 a 8 mmHg no AE."),
    dict(q="Sobre a relação entre ECG e ciclo mecânico, é correto afirmar que:",
         opts=["O QRS ocorre depois do início da ejeção",
               "A onda T coincide com a abertura da valva aórtica",
               "O QRS começa um pouco antes da sístole ventricular, e a onda T ocorre um pouco antes do fim da contração ventricular",
               "A onda P é seguida da contração ventricular",
               "O intervalo entre o início da P e o QRS é de 0,5 s"],
         a=2, c="A P precede a contração atrial; o QRS surge ≈ 0,16 s após o início da P e precede a sístole ventricular; a T "
                "(repolarização) ocorre um pouco antes do fim da contração."),
    dict(q="Quanto à velocidade de condução do potencial de ação no coração:",
         opts=["É maior no músculo ventricular (4 m/s) que nas fibras de Purkinje",
               "É de 0,3 a 0,5 m/s no músculo atrial e ventricular e chega a 4 m/s nas fibras de Purkinje",
               "É igual à dos nervos mielinizados grandes",
               "É 10 vezes maior que no músculo esquelético",
               "Não depende das junções comunicantes"],
         a=1, c="Músculo cardíaco: 0,3 a 0,5 m/s (≈ 1/250 dos nervos grandes e ≈ 1/10 do músculo esquelético). Purkinje: até 4 m/s, "
                "permitindo a ativação quase simultânea dos ventrículos."),
    dict(q="Qual é a valva mais frequentemente lesada na febre reumática, e por quê?",
         opts=["Tricúspide, por receber o sangue venoso",
               "Pulmonar, por ser a mais fina",
               "Mitral, por sofrer maior traumatismo mecânico sob alta pressão",
               "Aórtica, por ter cordas tendíneas",
               "Todas são afetadas igualmente"],
         a=2, c="A mitral sofre mais trauma durante sua ação e é a mais lesada; a aórtica é a segunda. As valvas direitas, sob baixa "
                "pressão, são muito menos afetadas."),
]

OPEN = [
    dict(q="Mulher de 74 anos, hipertensa há 20 anos, procura o pronto-socorro com dispneia intensa e palpitações há 6 horas. "
           "Estava bem, apenas com cansaço aos grandes esforços. ECG: fibrilação atrial com resposta ventricular de 150 bpm. "
           "Ecocardiograma prévio: hipertrofia concêntrica do VE, fração de ejeção de 65%. Antes do episódio, ao exame, "
           "ouvia-se uma B4. (a) Explique, com base na fisiologia do ciclo cardíaco, por que ela descompensou com a FA de alta "
           "resposta, mesmo com fração de ejeção normal. (b) O que se espera da B4 durante a FA? Justifique. (c) Por que a "
           "hipertensão crônica levou a hipertrofia concêntrica?",
         a=["(a) Duas perdas simultâneas: <b>perda da contração atrial</b> (normalmente ≈ 20% do enchimento, e bem mais em ventrículo "
            "rígido, que enche pouco no início da diástole) e <b>encurtamento da diástole</b> pela taquicardia (a sístole passa de "
            "≈ 40% do ciclo para uma fração muito maior, e a diástole encurta mais que a sístole). Resultado: VDF e volume sistólico "
            "caem, e a pressão diastólica final e a do átrio esquerdo sobem (curva diastólica íngreme do ventrículo pouco complacente), "
            "com congestão pulmonar e dispneia. A fração de ejeção normal não protege porque o problema é de enchimento (diastólico).",
            "(b) A B4 <b>desaparece</b>, porque é gerada pela contração atrial empurrando sangue para um ventrículo pouco complacente. "
            "Na FA não há contração atrial organizada.",
            "(c) Lei de Laplace (T = P × r): a pressão sistólica cronicamente alta eleva a tensão da parede e o consumo de O₂. O "
            "espessamento da parede com redução do raio (hipertrofia concêntrica) alivia parcialmente essa tensão, mas deixa o "
            "ventrículo mais rígido e fibrótico."]),
    dict(q="Homem de 62 anos, 3 dias após infarto agudo do miocárdio inferior, apresenta dispneia súbita, estertores em ambos os "
           "campos pulmonares, hipotensão e um sopro sistólico novo no foco mitral. A monitorização da pressão capilar pulmonar "
           "mostra ondas v gigantes. (a) Qual estrutura provavelmente falhou e qual é a função normal dela? (b) Explique a origem "
           "das ondas v gigantes. (c) Como fica o volume sistólico efetivo que chega à aorta e por quê?",
         a=["(a) <b>Músculo papilar</b> (isquemia ou ruptura) ou corda tendínea, levando a <b>insuficiência mitral aguda</b>. "
            "Normalmente os papilares contraem com a parede e, pelas cordas tendíneas, <b>impedem o prolapso das cúspides para o átrio</b> "
            "na sístole. Eles não fecham a valva, que fecha passivamente pelo gradiente de pressão.",
            "(b) A onda v normal reflete o enchimento atrial com as valvas AV fechadas durante a sístole ventricular. Com a mitral "
            "incompetente, parte do volume do VE volta ao átrio na sístole. Como o átrio esquerdo não teve tempo de dilatar (quadro "
            "agudo, baixa complacência), a pressão sobe muito: <b>onda v gigante</b>, transmitida aos capilares pulmonares (edema).",
            "(c) O volume sistólico <b>efetivo cai</b>, porque parte do volume ejetado segue para o átrio de baixa pressão em vez da "
            "aorta. Pode haver regurgitação até durante a contração isovolumétrica, que deixa de ser realmente isovolumétrica. "
            "Resultado: baixo débito e hipotensão, com congestão pulmonar."]),
    dict(q="Paciente de 58 anos, com doença renal crônica e em uso de espironolactona, chega com fraqueza e bradicardia (38 bpm). "
           "Potássio sérico: 8,8 mEq/ℓ. (a) Explique o mecanismo pelo qual a hiperpotassemia altera o potencial de ação e a "
           "contração cardíaca. (b) Que efeitos sobre o coração o Guyton descreve para essa faixa de K⁺? (c) Por que o gluconato "
           "de cálcio é usado nessa situação, considerando o efeito do Ca²⁺ sobre o coração?",
         a=["(a) O K⁺ extracelular alto reduz o gradiente de K⁺ e <b>despolariza parcialmente o potencial de repouso</b> (fica menos negativo). "
            "Com isso a amplitude do potencial de ação diminui (menos canais de Na⁺ disponíveis), a condução fica lenta e a contração enfraquece.",
            "(b) Coração <b>dilatado e flácido</b>, <b>queda da frequência</b>, <b>bloqueio da condução AV</b> e, com 8 a 12 mEq/ℓ (2 a 3× o "
            "normal), fraqueza grave, arritmias e morte.",
            "(c) O Ca²⁺ tem efeito quase oposto ao do K⁺ alto sobre o coração (tende à contração mais forte, até espástica) e estabiliza a "
            "membrana, contrapondo o efeito do K⁺ enquanto se trata a causa e se retira o potássio. (A estabilização de membrana é conhecimento "
            "clínico complementar ao cap. 9.)"]),
]

CARDS = [
    ("Por que o miocárdio funciona como um sincício?", "Os <b>discos intercalares</b> têm <b>junções comunicantes (gap junctions)</b> de baixa resistência; o potencial de ação passa livremente de célula a célula."),
    ("Quantos sincícios funcionais tem o coração e o que os separa?", "Dois: <b>atrial</b> e <b>ventricular</b>, separados pelo <b>tecido fibroso</b> dos anéis AV. A conexão é só pelo <b>feixe AV</b>."),
    ("Potencial de repouso e pico do potencial de ação ventricular", "Repouso ≈ <b>−85 mV</b>; pico ≈ <b>+20 mV</b> (amplitude ≈ 105 mV)."),
    ("Duração do platô do potencial de ação ventricular", "≈ <b>0,2 s</b> (canais de Ca²⁺ fecham em 0,2 a 0,3 s)."),
    ("Quais os dois fatores que causam o platô cardíaco?", "1) <b>Canais lentos de Ca²⁺ tipo L</b> (cálcio-sódio) abertos por décimos de segundo; 2) <b>queda de ~5× da permeabilidade ao K⁺</b>."),
    ("Fase 0 do potencial ventricular", "Despolarização: abertura dos <b>canais rápidos de Na⁺</b>."),
    ("Fase 1 do potencial ventricular", "Repolarização inicial: <b>fecham os canais de Na⁺</b>, sai K⁺ (canais transitórios)."),
    ("Fase 2 do potencial ventricular", "<b>Platô</b>: entrada de Ca²⁺ (canais L) e redução da saída de K⁺."),
    ("Fase 3 do potencial ventricular", "Repolarização rápida: <b>fecham canais de Ca²⁺</b>, abrem canais lentos de K⁺."),
    ("Fase 4 do potencial ventricular", "Repouso: −80 a −90 mV."),
    ("Quanto tempo a contração cardíaca dura em relação à esquelética?", "Até <b>15 vezes</b> mais (por causa do platô)."),
    ("Velocidade de condução no músculo atrial/ventricular", "<b>0,3 a 0,5 m/s</b> (≈ 1/250 dos nervos grandes; ≈ 1/10 do músculo esquelético)."),
    ("Velocidade de condução nas fibras de Purkinje", "Até <b>4 m/s</b>."),
    ("Período refratário absoluto do ventrículo", "<b>0,25 a 0,30 s</b> (≈ duração do potencial com platô)."),
    ("Período refratário relativo do ventrículo", "≈ <b>0,05 s</b> adicional."),
    ("Período refratário do átrio", "≈ <b>0,15 s</b> (mais curto que o ventricular)."),
    ("Por que o coração não entra em tetania?", "Porque o <b>período refratário</b> dura quase toda a contração; extrassístoles não somam força."),
    ("Acoplamento excitação-contração cardíaco: qual o gatilho da liberação de Ca²⁺ do RS?", "O <b>Ca²⁺ que entra pelos canais tipo L do túbulo T</b> ativa os <b>receptores de rianodina (RyR2)</b>: liberação de cálcio induzida por cálcio."),
    ("Túbulos T cardíacos × esqueléticos", "Diâmetro <b>5× maior</b>, volume <b>25× maior</b>; contêm <b>mucopolissacarídeos negativos</b> que armazenam Ca²⁺."),
    ("Por que a força cardíaca depende do Ca²⁺ extracelular?", "O <b>RS cardíaco é pouco desenvolvido</b>; os túbulos T abertos ao interstício trazem o Ca²⁺ extracelular que dispara e complementa a contração."),
    ("O que acontece com um coração em solução sem Ca²⁺?", "<b>Para de bater</b> rapidamente."),
    ("Mecanismos de remoção de Ca²⁺ no relaxamento cardíaco", "<b>SERCA2</b> (recaptação para o RS) e <b>trocador Na⁺/Ca²⁺</b> (saída da célula); o Na⁺ sai pela <b>Na⁺/K⁺-ATPase</b>."),
    ("Duração da contração atrial e ventricular", "≈ <b>0,2 s</b> (átrio) e ≈ <b>0,3 s</b> (ventrículo)."),
    ("Torção do VE: sentido na sístole", "Ápice gira em sentido <b>horário</b> e base em <b>anti-horário</b>; na diástole destorce como mola."),
    ("Onde fica o nó sinusal?", "Parede <b>superolateral do átrio direito</b>, perto da abertura da veia cava superior."),
    ("Atraso na passagem átrio → ventrículo e sua função", "&gt; <b>0,1 s</b>; permite que os átrios contraiam antes (bombas de escorva)."),
    ("Duração do ciclo cardíaco a 72 bpm", "1/72 min ≈ <b>0,833 s</b>."),
    ("Fração do ciclo ocupada pela sístole a 72 bpm e com FC 3×", "≈ <b>0,4</b> a 72 bpm; ≈ <b>0,65</b> com FC triplicada (a diástole encurta mais)."),
    ("Intervalo entre o início da P e o QRS (Guyton, cap. 9)", "≈ <b>0,16 s</b>."),
    ("QRS e onda T em relação à contração ventricular", "QRS começa <b>um pouco antes</b> da sístole; T ocorre <b>um pouco antes do fim</b> da contração."),
    ("Contribuição da contração atrial ao enchimento ventricular", "≈ <b>20%</b> (80% é passivo)."),
    ("Onda a de pressão atrial", "Causada pela <b>contração atrial</b>: AD +4 a 6 mmHg; AE +7 a 8 mmHg."),
    ("Onda c de pressão atrial", "Início da sístole ventricular: <b>abaulamento das valvas AV</b> para os átrios (e leve refluxo)."),
    ("Onda v de pressão atrial", "Fim da sístole: <b>enchimento atrial</b> pelas veias com as valvas AV fechadas."),
    ("Divisão da diástole em terços", "1º terço: <b>enchimento rápido</b>; terço médio: <b>diástase</b>; último terço: <b>sístole atrial</b>."),
    ("Duração da contração isovolumétrica", "<b>0,02 a 0,03 s</b> (todas as valvas fechadas)."),
    ("Pressão que abre as semilunares (VE e VD)", "VE &gt; ≈ <b>80 mmHg</b>; VD &gt; ≈ <b>8 mmHg</b>."),
    ("Ejeção rápida × lenta", "1º terço da ejeção: ≈ <b>70%</b> do volume; 2/3 finais: ≈ <b>30%</b>."),
    ("Duração do relaxamento isovolumétrico", "<b>0,03 a 0,06 s</b>."),
    ("VDF, VS, VSF e FE normais", "VDF 110 a 120 mℓ; VS ≈ 70 mℓ; VSF 40 a 50 mℓ; FE ≈ 60%."),
    ("Fórmula da fração de ejeção", "FE = <b>VS / VDF</b> = (VDF − VSF)/VDF."),
    ("Limites de VDF e VSF em situações extremas", "VDF até 150 a 180 mℓ; VSF até 10 a 20 mℓ."),
    ("Como as valvas cardíacas abrem e fecham?", "<b>Passivamente</b>, pelo gradiente de pressão."),
    ("Função dos músculos papilares", "<b>Não fecham as valvas</b>; puxam as cúspides para o ventrículo, <b>impedindo o prolapso</b> para os átrios na sístole."),
    ("Consequência de ruptura de corda tendínea / disfunção de papilar", "<b>Insuficiência mitral aguda</b>, podendo causar IC grave ou letal."),
    ("4 diferenças das valvas semilunares em relação às AV", "Fechamento <b>abrupto</b>; maior <b>velocidade</b> de fluxo; maior <b>abrasão</b>; <b>sem cordas tendíneas</b>."),
    ("Incisura da curva aórtica", "Breve <b>refluxo</b> antes do fechamento da valva aórtica, interrompido bruscamente."),
    ("Pressões na aorta e na artéria pulmonar", "Aorta ≈ <b>120/80</b> mmHg; lado direito ≈ <b>1/6</b> disso."),
    ("Causa e características de B1", "<b>Fechamento das AV</b>; grave, mais longa (≈ 0,14 s)."),
    ("Causa e características de B2", "<b>Fechamento das semilunares</b>; mais aguda e curta (≈ 0,11 s)."),
    ("B3: momento e significado", "Início do <b>terço médio da diástole</b>; normal em jovens; em idosos sugere <b>IC sistólica</b>."),
    ("B4: momento e significado", "<b>Sístole atrial</b> (fim da diástole) contra ventrículo pouco complacente, p. ex., <b>HVE</b> do idoso. Some na FA."),
    ("A abertura das valvas produz som?", "Normalmente <b>não</b> (processo lento)."),
    ("Valvas mais lesadas na febre reumática", "<b>Mitral</b>, depois <b>aórtica</b> (valvas de alta pressão)."),
    ("Valvopatia mais comum hoje (Guyton)", "<b>Estenose aórtica calcificada senil</b>."),
    ("Componentes do trabalho sistólico", "<b>Trabalho pressão-volume (externo)</b> e <b>energia cinética</b> (≈ 1%)."),
    ("Quando a energia cinética passa de 50% do trabalho do VE?", "Na <b>estenose aórtica</b> (alta velocidade pelo orifício estreito)."),
    ("Trabalho externo do VD em relação ao VE", "≈ <b>1/6</b>."),
    ("Alça PV: fase I", "<b>Enchimento</b> (A→B): 50 → 120 mℓ; pressão 2 a 3 → 5 a 7 mmHg."),
    ("Alça PV: fase II", "<b>Contração isovolumétrica</b> (B→C): pressão sobe a ≈ 80 mmHg, volume fixo."),
    ("Alça PV: fase III", "<b>Ejeção</b> (C→D): volume cai ≈ 70 mℓ."),
    ("Alça PV: fase IV", "<b>Relaxamento isovolumétrico</b> (D→A): pressão cai, volume fixo."),
    ("O que representa a área da alça PV?", "O <b>trabalho sistólico externo</b> (TE)."),
    ("Pico de pressão sistólica isovolumétrica máxima: VE e VD", "VE <b>250 a 300 mmHg</b>; VD <b>60 a 80 mmHg</b>."),
    ("Por que a curva de pressão diastólica sobe muito acima de 150 mℓ?", "O <b>tecido fibroso</b> não estica mais e o <b>pericárdio</b> chega ao limite."),
    ("Pré-carga (Guyton)", "<b>Pressão diastólica final</b> do ventrículo."),
    ("Pós-carga (Guyton)", "<b>Pressão na artéria</b> que sai do ventrículo (aorta)."),
    ("Principal substrato energético do miocárdio", "<b>Ácidos graxos</b> (70 a 90%)."),
    ("Consumo de O₂ miocárdico é proporcional a...", "Área <b>TE + EP</b> da alça e ao <b>índice tensão-tempo</b>."),
    ("Lei de Laplace no ventrículo", "<b>T = P × r</b>."),
    ("Hipertrofia concêntrica × excêntrica (energia)", "Concêntrica: parede grossa, raio menor, <b>alivia tensão</b>. Excêntrica (dilatada): raio maior, <b>mais tensão e mais O₂</b> para a mesma pressão."),
    ("Eficiência cardíaca", "<b>20 a 25%</b> no normal; até 5% na IC."),
    ("Débito cardíaco em repouso e no exercício", "<b>4 a 6 ℓ/min</b>; até <b>4 a 7×</b> no exercício intenso."),
    ("Mecanismo de Frank-Starling", "Quanto mais o músculo é distendido no enchimento, <b>maior a força</b>: o coração bombeia todo o sangue que retorna."),
    ("Base molecular do Frank-Starling", "Sobreposição <b>actina-miosina mais próxima do ideal</b> com o estiramento."),
    ("Efeito direto do estiramento do AD na FC", "Aumenta a FC em <b>10 a 20%</b>."),
    ("Reflexo de Bainbridge", "Estiramento atrial → via <b>vagal</b> → FC ↑ <b>40 a 60%</b>."),
    ("Efeitos máximos do simpático no coração", "FC até <b>180 a 200 bpm</b> (raro 250); força <b>dobra</b>; DC 2 a 3×."),
    ("Tônus simpático basal", "Mantém o bombeamento ≈ <b>30%</b> acima do que seria sem simpático."),
    ("Estimulação vagal intensa", "Pode parar o coração por segundos; <b>escape</b> a 20 a 40 bpm; força ↓ 20 a 30%."),
    ("Por que o vago reduz mais a FC que a força?", "As fibras vagais vão principalmente aos <b>átrios</b>."),
    ("Efeitos da hiperpotassemia no coração", "Coração <b>dilatado e flácido</b>, FC ↓, <b>bloqueio AV</b>; 8 a 12 mEq/ℓ pode matar."),
    ("Mecanismo da fraqueza na hiperpotassemia", "Despolarização parcial do repouso → <b>potencial de ação menor</b> → contração fraca."),
    ("Efeito do excesso de Ca²⁺ extracelular", "<b>Contração espástica</b>."),
    ("Efeito da febre no coração", "FC ↑ (até o dobro); força ↑ transitoriamente, depois fraqueza se prolongada."),
    ("Até que pressão média a pós-carga não reduz o DC?", "≈ <b>160 mmHg</b>."),
]

TOPIC = dict(
    code="a", slug="a-musculo-cardiaco-e-valvas", title="Músculo cardíaco e valvas cardíacas",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 9 (bulhas e valvopatias: cap. 23)",
    sections=SECTIONS, mcq=MCQ, open=OPEN, cards=CARDS,
)
