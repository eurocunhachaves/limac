"""Tema f: Controle local, humoral e nervoso da circulação (Guyton & Hall, caps. 17 e 18)."""

SECTIONS = [
    ("1. Cada tecido controla o próprio fluxo", [
        ("table", [
            ["Órgão (repouso)", "% do DC", "mℓ/min", "mℓ/min/100 g"],
            ["<b>Fígado</b> (portal 21% + arterial 6%)", "<b>27</b>", "1.350", "95"],
            ["<b>Rins</b>", "<b>22</b>", "1.100", "<b>360</b>"],
            ["Músculo (inativo)", "15", "750", "<b>4</b>"],
            ["Cérebro", "14", "700", "50"],
            ["Coração", "4", "200", "70"],
            ["Pele (frio) · ossos", "6 · 5", "300 · 250", "3 · 3"],
            ["Tireoide · adrenais", "1 · 0,5", "50 · 25", "160 · 300"],
        ], [6.4, 2.8, 3.4, 4.8]),
        ("ul", [
            "O fluxo de cada tecido é mantido no <b>mínimo suficiente</b> para suas necessidades (O₂, nutrientes, remoção de CO₂ e H⁺). "
            "Fluxo alto para todos exigiria mais do que o coração bombeia.",
            "Músculo: 30 a 40% da massa corporal, mas só ≈ 4 mℓ/min/100 g em repouso; no exercício o metabolismo sobe <b>60×</b> e o fluxo <b>20×</b>.",
            "Dois tempos: <b>agudo</b> (segundos a minutos, diâmetro de arteríolas, metarteríolas e esfíncteres) e <b>longo prazo</b> "
            "(dias a meses, número e tamanho dos vasos).",
        ]),
    ]),
    ("2. Controle agudo: metabolismo e autorregulação", [
        ("ul", [
            "Metabolismo 8× → fluxo agudo ≈ 4×. <b>Falta de O₂</b> (altitude, pneumonia, CO, cianeto) aumenta muito o fluxo: saturação a 25% → fluxo 3×; "
            "cianeto → até 7×.",
            "<b>Teoria vasodilatadora</b>: tecido ativo ou com pouco O₂ libera <b>adenosina</b> (a principal no coração), CO₂, compostos de fosfato, "
            "histamina, <b>K⁺</b>, <b>H⁺</b> e lactato, que dilatam arteríolas, metarteríolas e esfíncteres.",
            "<b>Teoria da demanda de O₂</b>: o músculo liso precisa de O₂ para contrair; com pouco O₂ relaxa. Explica a <b>vasomoção</b> "
            "(esfíncteres totalmente abertos ou fechados). Provavelmente as duas atuam juntas.",
            "Deficiência de <b>tiamina (beribéri)</b>, riboflavina ou niacina: vasodilatação e fluxo periférico 2 a 3×.",
        ]),
        ("fig", "fig/f_hiperemia.png", None, "Hiperemia reativa e ativa: duas faces do controle metabólico.", 16),
        ("fig", "fig/f_autorregulacao.png", None, "Autorregulação aguda (vermelho) e de longo prazo (verde).", 15),
        ("ul", [
            "<b>Autorregulação</b>: a pressão sobe, o fluxo sobe e em &lt; 1 minuto volta quase ao normal. Entre <b>70 e 175 mmHg</b> o fluxo muda só "
            "<b>20 a 30%</b> (cérebro e coração, ainda menos).",
            "<b>Metabólica</b>: excesso de fluxo traz O₂ e lava os vasodilatadores → constrição. <b>Miogênica</b>: estiramento despolariza o músculo liso "
            "→ entra Ca²⁺ → contração (sem nervo nem hormônio; mais forte nas arteríolas). No exercício, o metabólico prevalece.",
        ]),
        ("table", [
            ["Órgão", "Mecanismo especial"],
            ["<b>Rim</b>", "<b>Feedback tubuloglomerular</b>: a <b>mácula densa</b> sente o líquido do túbulo distal e contrai a arteríola aferente"],
            ["<b>Cérebro</b>", "<b>CO₂ e H⁺</b> ↑ dilatam fortemente (excitabilidade depende deles), além do O₂"],
            ["<b>Pele</b>", "Temperatura, via <b>simpático</b>: 3 mℓ/min/100 g no frio até <b>7 a 8 ℓ/min</b> no corpo todo no calor"],
        ], [3.0, 14.4]),
    ]),
    ("3. Endotélio: óxido nítrico e endotelina", [
        ("fig", "fig/f_endotelio.png", None, "Via do NO (relaxa) e a endotelina (contrai).", 16),
        ("ul", [
            "<b>NO</b>: eNOS (arginina + O₂) → NO (gás, meia-vida ≈ 6 s) → <b>guanilato ciclase solúvel</b> → <b>GMPc</b> → PKG → relaxamento.",
            "Estímulo principal: <b>tensão de cisalhamento</b> do fluxo. Quando a microcirculação dilata, o fluxo maior libera NO nas artérias proximais, "
            "que também dilatam. Angiotensina II também libera NO (freio contra constrição excessiva).",
            "Endotélio lesado (hipertensão, aterosclerose) produz menos NO → mais constrição e mais lesão.",
            "<b>Nitratos</b> liberam NO (angina). <b>Sildenafila</b> inibe a <b>PDE-5</b>, que degrada o GMPc (disfunção erétil).",
            "<b>Endotelina</b>: peptídeo de 27 aminoácidos, constrição potente em nanogramas; liberada pelo <b>endotélio lesado</b> (evita sangramento em "
            "artérias até 5 mm). Bloqueadores: hipertensão pulmonar.",
        ]),
    ]),
    ("4. Controle de longo prazo e remodelagem", [
        ("ul", [
            "O controle agudo corrige só <b>≈ 3/4</b>: PA 100 → 150 faz o fluxo subir 100% e voltar a <b>10 a 15% acima</b> em 30 s a 2 min. "
            "Em semanas, volta ao normal (plano de 50 a 200 mmHg).",
            "<b>Angiogênese</b>: hipóxia → <b>HIF</b> → <b>VEGF</b>, FGF, PDGF, angiogenina. Brotamento: dissolve a membrana basal, células endoteliais "
            "crescem em cordão, formam tubo e alça. Rápida no jovem e no tumor, lenta no idoso.",
            "Antiangiogênicos naturais: <b>angiostatina</b> (do plasminogênio) e <b>endostatina</b>. Esteroides podem sumir com vasos.",
            "A vascularização segue a necessidade <b>máxima</b>, não a média. <b>Retinopatia da prematuridade</b>: O₂ alto para o crescimento de vasos; "
            "ao retirar, crescimento explosivo para o vítreo.",
            "<b>Colaterais</b>: dilatação metabólica em 1 a 2 min (&lt; 1/4 da necessidade), metade em 1 dia, suficiente em poucos dias; crescem por "
            "meses (muitos canais pequenos). Explicam coronárias ocluídas sem infarto.",
        ]),
        ("fig", "fig/f_remodelagem.png", None, "Remodelagem vascular conforme pressão e fluxo crônicos.", 16),
    ]),
    ("5. Controle humoral", [
        ("table", [
            ["Substância", "Efeito", "Detalhe que cai"],
            ["<b>Noradrenalina</b>", "Constritor potente", "Terminais simpáticos e adrenal (receptores α)"],
            ["<b>Adrenalina</b>", "Constritor menor; dilata em alguns leitos", "Dilata coronárias e músculo (β)"],
            ["<b>Angiotensina II</b>", "Constrição forte das pequenas arteríolas", "1 µg pode ↑ PA ≥ 50 mmHg; ↑ RPT e ↓ excreção de Na⁺ e água"],
            ["<b>Vasopressina (ADH)</b>", "Constritor <b>mais potente que a Ang II</b>", "Hipotálamo → neuro-hipófise; importante na hemorragia grave; "
             "função principal: reabsorver água"],
            ["<b>Bradicinina</b>", "Dilatação arteriolar + ↑ permeabilidade", "Calicreína → calidina → bradicinina; inativada pela ECA; 1 µg ↑ fluxo do braço 6×"],
            ["<b>Histamina</b>", "Dilatação + ↑ permeabilidade (edema)", "Mastócitos e basófilos; alergia e inflamação"],
        ], [3.6, 5.6, 8.2]),
        ("ul", [
            "Íons: <b>↑ Ca²⁺</b> intracelular contrai; <b>↑ K⁺</b>, <b>↑ Mg²⁺</b>, <b>↑ H⁺</b> (↓ pH), acetato e citrato dilatam. "
            "<b>CO₂</b> dilata pouco nos tecidos e muito no cérebro, mas no centro vasomotor causa <b>constrição generalizada</b>.",
            "Vasoativos crônicos mudam pouco o fluxo a longo prazo se não mudarem o metabolismo: a autorregulação vence.",
        ]),
    ]),
    ("6. Controle nervoso: o centro vasomotor", [
        ("fig", "fig/f_centro_vasomotor.png", None, "Centro vasomotor no bulbo e ponte, aferências e eferências.", 13),
        ("ul", [
            "Simpático: fibras de T1 a L1-L2 → cadeia simpática → nervos viscerais e nervos espinhais. Inerva <b>todos os vasos exceto capilares</b>. "
            "Arteríolas: ↑ resistência. Veias: ↓ volume, empurram sangue ao coração. Coração: ↑ FC e força.",
            "Constrição simpática forte em <b>rins, intestino, baço e pele</b>; fraca em músculo, coração e cérebro.",
            "Parassimpático (vago): papel vascular pequeno; efeito principal é <b>↓ FC</b> (e leve ↓ contratilidade).",
            "<b>Tônus vasoconstritor</b>: disparo contínuo de <b>0,5 a 2 impulsos/s</b>. Raquianestesia total: PA cai de <b>100 para 50 mmHg</b>.",
            "Noradrenalina age em <b>receptores α</b>. Medula adrenal libera adrenalina e noradrenalina ao mesmo tempo (sistema duplo).",
            "<b>Síncope vasovagal</b>: emoção → hipotálamo anterior → vasodilatação muscular + vago forte (FC ↓) → PA ↓ → desmaio.",
        ]),
        ("box", "O controle nervoso é o mais rápido", [
            "Três ações simultâneas: <b>arteríolas contraem</b> (↑ RPT), <b>veias contraem</b> (↑ retorno), <b>coração estimulado</b> (FC até 3×, DC até 2×).",
            "Dobra a PA em <b>5 a 10 s</b>; a inibição súbita a reduz à metade em 10 a 40 s.",
            "Exercício: PA ↑ 30 a 40% (ativação reticular junto do córtex motor). <b>Reação de alarme</b>: PA ↑ 75 a 100 mmHg em segundos.",
        ]),
    ]),
    ("7. Reflexos que mantêm a PA", [
        ("fig", "fig/f_barorreceptor.png", None, "Resposta dos barorreceptores carotídeos e a alça do reflexo.", 16),
        ("ul", [
            "<b>Barorreceptores</b>: terminações livres de estiramento no <b>seio carotídeo</b> (carótida interna, acima da bifurcação) e no "
            "<b>arco aórtico</b>. Carotídeo: nervo de <b>Hering → IX</b>; aórtico: <b>X</b>; ambos → <b>núcleo do trato solitário</b>.",
            "Carotídeos: silenciosos de 0 a 50–60 mmHg, máximo ≈ 180; os aórticos operam ≈ 30 mmHg acima. Respondem mais a pressão que <b>varia</b> "
            "(até 2× mais do que a estável).",
            "Ocluir as carótidas comuns → ↓ disparo → PA sobe. Ao levantar-se, evitam a queda da PA na cabeça.",
            "<b>Tampão</b>: sem eles a faixa de PA do dia aumenta 2,5× (50 a &gt; 160 mmHg); com eles, variação ≈ <b>1/3</b>. Reajustam em "
            "<b>1 a 2 dias</b>, mas não totalmente (ajudam via simpático renal). Estimulação crônica do seio carotídeo ↓ PA 15 a 20 mmHg.",
        ]),
        ("fig", "fig/f_faixas.png", None, "Cada reflexo atua numa faixa de pressão.", 13),
        ("ul", [
            "<b>Quimiorreceptores</b> (corpos carotídeos e aórticos, ≈ 2 mm, fluxo abundante): sentem ↓ O₂, ↑ CO₂ e ↑ H⁺; excitam o centro vasomotor "
            "quando a PA cai <b>abaixo de 80</b>. Contribuem para HAS na obesidade e na <b>apneia do sono</b>.",
            "<b>Resposta isquêmica do SNC</b>: isquemia do centro vasomotor (acúmulo de CO₂) → PA até <b>250 mmHg</b> por até 10 min; rim pode parar de "
            "urinar. Só abaixo de <b>60</b> (máxima em 15 a 20): último recurso.",
            "<b>Reação de Cushing</b>: ↑ pressão do liquor comprime as artérias cerebrais → resposta isquêmica → PA sobe até ficar pouco acima da pressão "
            "do liquor (clínica: hipertensão com bradicardia na hipertensão intracraniana).",
        ]),
        ("fig", "fig/f_baixa_pressao.png", None, "Receptores de baixa pressão (átrios e artéria pulmonar) e reflexos atriais.", 15),
        ("ul", [
            "<b>Compressão abdominal</b>: reflexos também contraem músculos abdominais, espremendo os reservatórios venosos → ↑ DC e PA. "
            "Paralisados têm mais hipotensão.",
            "Exercício: a contração muscular comprime vasos e ajuda o DC a subir <b>5 a 7×</b>; PA média 100 → <b>130 a 160</b>.",
            "<b>Ondas respiratórias</b>: 4 a 6 mmHg (até 20 na respiração profunda); a PA sobe no início da expiração. "
            "<b>Ondas de Mayer (vasomotoras)</b>: 10 a 40 mmHg, ciclos de 7 a 10 s no humano, por oscilação do barorreflexo (ou quimiorreflexo a 40–80 mmHg).",
        ]),
    ]),
]

MCQ = [
    dict(q="Em repouso, qual órgão recebe o maior fluxo sanguíneo por 100 g de tecido?",
         opts=["Cérebro", "Coração", "Rim", "Fígado", "Músculo esquelético"],
         a=2, c="Rim ≈ 360 mℓ/min/100 g (22% do DC). Fígado recebe a maior fração do DC (27%), mas 95 mℓ/min/100 g."),
    dict(q="Durante exercício intenso, o fluxo sanguíneo total da musculatura esquelética pode aumentar até aproximadamente:",
         opts=["2 vezes", "5 vezes", "20 vezes", "60 vezes", "100 vezes"], keep=True,
         a=2, c="O metabolismo muscular sobe &gt; 60×, mas o fluxo até ≈ 20× (de 750 para ≈ 16.000 mℓ/min)."),
    dict(q="Qual substância é considerada o principal vasodilatador metabólico na regulação do fluxo coronariano?",
         opts=["Histamina", "Adenosina", "Bradicinina", "Acetilcolina", "Serotonina"],
         a=1, c="Com mais trabalho cardíaco, cai o O₂, o ATP é degradado e a adenosina sai das células e dilata as coronárias."),
    dict(q="Após a liberação de uma artéria que ficou ocluída por alguns minutos, o fluxo sobe 4 a 7 vezes acima do normal. Esse fenômeno é:",
         opts=["Hiperemia ativa", "Hiperemia reativa", "Autorregulação miogênica", "Reflexo de Bainbridge", "Reação de Cushing"],
         a=1, c="Hiperemia reativa: o fluxo extra compensa quase exatamente o déficit de O₂ acumulado. Hiperemia ativa é pelo aumento do metabolismo."),
    dict(q="Na autorregulação aguda, quando a pressão arterial varia entre 70 e 175 mmHg, o fluxo sanguíneo tecidual:",
         opts=["Varia proporcionalmente à pressão", "Varia só 20 a 30%", "Permanece exatamente constante", "Cai à medida que a pressão sobe",
               "Aumenta 150%"],
         a=1, c="A pressão sobe 150% e o fluxo só 20 a 30%. A longo prazo (semanas), fica quase plano de 50 a 200 mmHg."),
    dict(q="A teoria miogênica da autorregulação propõe que:",
         opts=["O excesso de O₂ lava os vasodilatadores", "O estiramento do vaso despolariza o músculo liso, que se contrai",
               "O simpático contrai as arteríolas quando a PA sobe", "O NO é liberado pelo cisalhamento", "A angiotensina II contrai a eferente"],
         a=1, c="O estiramento despolariza o músculo liso, entra Ca²⁺ e o vaso contrai. Independe de nervos e hormônios; mais forte nas arteríolas."),
    dict(q="No rim, o mecanismo especial de controle agudo do fluxo em que a composição do líquido tubular é detectada e a arteríola aferente se contrai chama-se:",
         opts=["Reflexo de volume", "Feedback tubuloglomerular (mácula densa)", "Reflexo de Bezold-Jarisch", "Reação de Cushing", "Hiperemia reativa"],
         a=1, c="A mácula densa no túbulo distal inicial ajusta a arteríola aferente e ajuda a manter a TFG."),
    dict(q="O principal estímulo fisiológico para a liberação de óxido nítrico pelo endotélio das artérias é:",
         opts=["A hipóxia do músculo liso", "A tensão de cisalhamento do fluxo sanguíneo", "A noradrenalina", "A endotelina", "O frio"],
         a=1, c="O cisalhamento distorce as células endoteliais e ↑ NO: artérias proximais dilatam quando a microcirculação distal dilata."),
    dict(q="O óxido nítrico relaxa o músculo liso vascular porque ativa:",
         opts=["Adenilato ciclase → AMPc", "Guanilato ciclase solúvel → GMPc", "Fosfolipase C → IP₃", "Canais de Ca²⁺ tipo L", "Receptores α1"],
         a=1, c="NO → guanilato ciclase solúvel → GTP vira GMPc → proteinoquinase G → relaxamento."),
    dict(q="A sildenafila potencializa a ação do óxido nítrico porque:",
         opts=["Doa NO diretamente", "Inibe a PDE-5, que degrada o GMPc", "Ativa a eNOS", "Bloqueia receptores de endotelina", "Inibe a ECA"],
         a=1, c="Ao impedir a degradação do GMPc, prolonga o efeito do NO (uso: disfunção erétil). Nitratos é que doam NO."),
    dict(q="A endotelina:",
         opts=["É um gás de meia-vida curta que dilata vasos", "É um peptídeo vasoconstritor potente liberado pelo endotélio lesado",
               "É liberada pelos mastócitos na alergia", "Aumenta a permeabilidade capilar como a histamina", "Degrada a bradicinina"],
         a=1, c="Peptídeo de 27 aminoácidos, age em nanogramas; ajuda a evitar hemorragia em artérias até 5 mm. Bloqueadores: hipertensão pulmonar."),
    dict(q="O principal fator de crescimento envolvido na angiogênese induzida por hipóxia é:",
         opts=["Endostatina", "Angiostatina", "VEGF", "Endotelina", "Bradicinina"],
         a=2, c="Hipóxia → HIF → VEGF (e FGF, PDGF, angiogenina). Angiostatina e endostatina inibem a angiogênese."),
    dict(q="Um prematuro mantido em alta concentração de O₂ e depois retirado dela desenvolve crescimento explosivo de vasos da retina para o vítreo. O mecanismo é:",
         opts=["Hiperemia ativa", "Controle de longo prazo pelo O₂ (angiogênese)", "Autorregulação miogênica", "Reação de Cushing", "Remodelagem hipertrófica"],
         a=1, c="O₂ alto para o crescimento vascular; a queda súbita de O₂ dispara fatores angiogênicos: retinopatia da prematuridade (fibroplasia retrolental)."),
    dict(q="Na hipertensão crônica, pequenas artérias e arteríolas que se contraem com o aumento da pressão sofrem remodelagem:",
         opts=["Eutrófica excêntrica", "Hipertrófica excêntrica", "Eutrófica concêntrica", "Aneurismática", "Nenhuma"],
         a=2, c="Luz menor e parede mais grossa, sem mudar a área de parede. Grandes artérias sofrem remodelagem hipertrófica (mais rígidas)."),
    dict(q="Qual destas substâncias é o vasoconstritor humoral mais potente?",
         opts=["Angiotensina II", "Vasopressina (ADH)", "Adrenalina", "Histamina", "Bradicinina"],
         a=1, c="A vasopressina é ainda mais potente que a angiotensina II, mas em condições normais é secretada em pouca quantidade (importa na hemorragia)."),
    dict(q="Bradicinina e histamina têm em comum:",
         opts=["Vasoconstrição e ↓ permeabilidade", "Vasodilatação arteriolar e ↑ permeabilidade capilar",
               "Origem nos mastócitos", "Inativação pela eNOS", "Ação exclusiva no cérebro"],
         a=1, c="Ambas dilatam arteríolas e alargam os poros capilares (edema). A bradicinina é inativada pela ECA."),
    dict(q="O aumento da concentração de qual íon provoca vasoconstrição?",
         opts=["K⁺ (faixa fisiológica)", "Mg²⁺", "H⁺", "Ca²⁺ intracelular", "Citrato"],
         a=3, c="↑ Ca²⁺ estimula a contração do músculo liso. K⁺, Mg²⁺, H⁺, acetato e citrato dilatam."),
    dict(q="A vasoconstrição simpática é mais potente em qual destes leitos?",
         opts=["Cérebro", "Coração", "Músculo esquelético", "Rins", "Retina"],
         a=3, c="Forte em rins, intestino, baço e pele; fraca em músculo, coração e cérebro."),
    dict(q="Após raquianestesia total em um animal, a pressão arterial cai de 100 para cerca de 50 mmHg. Isso demonstra:",
         opts=["A importância do reflexo de Bainbridge", "A perda do tônus vasoconstritor simpático", "A falha da autorregulação renal",
               "A ação da vasopressina", "A resposta isquêmica do SNC"],
         a=1, c="O centro vasomotor dispara continuamente 0,5 a 2 impulsos/s (tônus vasomotor). Noradrenalina injetada restaura a PA."),
    dict(q="As aferências dos barorreceptores do seio carotídeo chegam ao bulbo por qual via?",
         opts=["Nervo vago", "Nervo de Hering e glossofaríngeo", "Nervo frênico", "Nervo hipoglosso", "Cadeia simpática cervical"],
         a=1, c="Seio carotídeo → Hering → IX → núcleo do trato solitário. Arco aórtico → vago (X)."),
    dict(q="Os barorreceptores do seio carotídeo:",
         opts=["Disparam mais entre 0 e 50 mmHg", "Têm maior sensibilidade perto de 100 mmHg", "Não respondem a variações rápidas",
               "Operam 30 mmHg acima dos aórticos", "São quimiorreceptores de O₂"],
         a=1, c="Silenciosos de 0 a 50–60, máximo ≈ 180 e maior ganho na faixa normal (≈ 100). Os aórticos operam ≈ 30 mmHg acima."),
    dict(q="A oclusão bilateral das artérias carótidas comuns abaixo do seio carotídeo causa:",
         opts=["Queda da PA por estímulo dos barorreceptores", "Aumento da PA por menor disparo dos barorreceptores",
               "Bradicardia por reflexo de Cushing", "Nenhum efeito", "Aumento do disparo vagal"],
         a=1, c="A pressão no seio cai, o disparo diminui e o centro vasomotor fica menos inibido: a PA sobe."),
    dict(q="Por que os barorreceptores são pouco eficazes no controle da PA a longo prazo?",
         opts=["Porque só respondem à pressão venosa", "Porque se reajustam ao novo nível de pressão em 1 a 2 dias",
               "Porque são inibidos pela angiotensina", "Porque dependem de hormônios", "Porque só atuam abaixo de 60 mmHg"],
         a=1, c="O disparo volta quase ao normal em 1 a 2 dias mesmo com PA alta. O controle crônico é do sistema rim-líquidos (tema h)."),
    dict(q="Os quimiorreceptores carotídeos e aórticos passam a ser importantes no controle da PA quando ela cai abaixo de:",
         opts=["140 mmHg", "100 mmHg", "80 mmHg", "40 mmHg", "15 mmHg"], keep=True,
         a=2, c="Abaixo de 80 mmHg, a hipoperfusão dos corpos (≈ 2 mm) reduz O₂ e acumula CO₂ e H⁺, excitando o centro vasomotor."),
    dict(q="A resposta isquêmica do SNC:",
         opts=["Atua continuamente na faixa normal de PA", "É um mecanismo de emergência que atua abaixo de 60 mmHg",
               "Reduz a pressão arterial", "Depende dos barorreceptores", "É mediada pelo vago"],
         a=1, c="Isquemia do centro vasomotor (acúmulo de CO₂) → descarga simpática máxima, PA até 250 mmHg. Máxima com PA de 15 a 20."),
    dict(q="Um paciente com hipertensão intracraniana apresenta elevação da pressão arterial. Esse mecanismo é chamado de:",
         opts=["Reflexo de Bainbridge", "Reação de Cushing", "Reflexo de volume", "Hiperemia reativa", "Síncope vasovagal"],
         a=1, c="↑ pressão do liquor comprime as artérias cerebrais → resposta isquêmica do SNC → PA sobe até ficar pouco acima da pressão do liquor."),
    dict(q="Após infusão rápida de 300 mℓ de sangue em um cão com todos os reflexos intactos, a PA sobe cerca de 15 mmHg. Sem barorreceptores arteriais e sem receptores de baixa pressão, subiria cerca de:",
         opts=["15 mmHg", "25 mmHg", "40 mmHg", "100 mmHg", "250 mmHg"], keep=True,
         a=3, c="Intacto +15; sem barorreceptores arteriais +40; sem os de baixa pressão também +100."),
    dict(q="O reflexo de Bainbridge consiste em:",
         opts=["Bradicardia pelo estiramento do seio carotídeo", "Aumento da FC pelo estiramento dos átrios",
               "Aumento da PA por isquemia cerebral", "Vasodilatação muscular na emoção", "Queda da PA ao levantar"],
         a=1, c="Átrio estirado → aferência vagal → FC ↑ 40 a 60% (mais 15% pelo estiramento direto do nó sinusal)."),
    dict(q="O estiramento atrial por aumento do volume sanguíneo leva a:",
         opts=["↑ ADH e ↑ simpático renal", "↓ ADH, ↓ simpático renal e ↑ peptídeo natriurético atrial",
               "↑ aldosterona", "↑ reabsorção de água", "Constrição da arteríola aferente"],
         a=1, c="Reflexo de volume: dilata a aferente, ↑ filtração, ↓ reabsorção, ↓ ADH e ↑ PNA → o rim elimina o excesso."),
    dict(q="As ondas de Mayer (vasomotoras) na pressão arterial resultam principalmente de:",
         opts=["Movimentos respiratórios", "Oscilação do reflexo barorreceptor", "Contrações atriais", "Variação da frequência cardíaca sinusal",
               "Arritmia ventricular"],
         a=1, c="Oscilações de 10 a 40 mmHg a cada 7 a 10 s: atraso + ganho alto no barorreflexo (ou quimiorreflexo entre 40 e 80 mmHg)."),
]

OPEN = [
    dict(q="Jovem de 19 anos assiste a uma coleta de sangue, fica pálido, com FC de 42 bpm e PA de 70/40 mmHg, e desmaia. Recupera-se deitado com as pernas "
           "elevadas. (a) Qual o diagnóstico fisiológico e a via nervosa envolvida? (b) Explique por que a PA cai tanto. (c) Por que a posição deitada ajuda "
           "e qual reflexo normalmente protege contra a queda da PA ao ficar em pé?",
         a=["(a) <b>Síncope vasovagal</b> (desmaio emocional): córtex → centro vasodilatador do <b>hipotálamo anterior</b> → núcleos vagais do bulbo (FC ↓) "
            "e fibras vasodilatadoras simpáticas dos músculos.",
            "(b) Duas coisas juntas: <b>vasodilatação muscular</b> (↓ resistência periférica) e <b>bradicardia vagal intensa</b> (↓ DC). PA = DC × RPT cai, "
            "e o fluxo cerebral fica insuficiente.",
            "(c) Deitado, a gravidade deixa de tirar sangue do cérebro e as pernas elevadas aumentam o retorno venoso. Ao levantar, o <b>barorreflexo</b> "
            "(seio carotídeo e arco aórtico) detecta a queda e dispara descarga simpática que contrai arteríolas e veias e acelera o coração."]),
    dict(q="Homem de 45 anos sofre trauma craniano. Horas depois, está sonolento, com PA de 190/100 mmHg, FC de 48 bpm e respiração irregular. "
           "(a) Como se chama essa resposta e qual o seu mecanismo? (b) Por que a PA sobe? A que nível ela tende a se estabilizar? "
           "(c) Por que a FC está baixa? (d) A partir de que pressão arterial a resposta isquêmica do SNC passa a atuar em condições gerais?",
         a=["(a) <b>Reação de Cushing</b>: a pressão do liquor sobe, comprime o cérebro e as artérias cerebrais e causa isquemia do centro vasomotor, "
            "que dispara a <b>resposta isquêmica do SNC</b> (acúmulo local de CO₂ e ácido lático).",
            "(b) Descarga simpática máxima (vasoconstrição intensa, até 250 mmHg). A PA sobe até ficar <b>pouco acima da pressão do liquor</b>, "
            "o suficiente para o sangue voltar a entrar no cérebro.",
            "(c) A PA muito alta estimula os <b>barorreceptores</b>, que ativam o vago: bradicardia reflexa (a clássica tríade de Cushing).",
            "(d) Abaixo de <b>60 mmHg</b>, com máximo de estimulação em 15 a 20 mmHg. É um mecanismo de emergência, o último recurso."]),
    dict(q="Mulher de 62 anos, obesa, com apneia obstrutiva do sono, tem hipertensão resistente. O cardiologista cita o barorreflexo e os quimiorreceptores. "
           "(a) Onde ficam os barorreceptores e quais nervos levam seus sinais? (b) Descreva a resposta reflexa a um aumento agudo da PA. "
           "(c) Por que os barorreceptores não impedem a hipertensão crônica? (d) Como a apneia do sono pode elevar a PA?",
         a=["(a) <b>Seio carotídeo</b> (parede da carótida interna, acima da bifurcação) → nervo de Hering → <b>glossofaríngeo</b>; <b>arco aórtico</b> → "
            "<b>vago</b>. Ambos chegam ao <b>núcleo do trato solitário</b>.",
            "(b) ↑ PA → estiramento → ↑ disparo → NTS inibe a área vasoconstritora e excita o vago → <b>vasodilatação</b> de arteríolas e veias, "
            "<b>↓ FC e ↓ contratilidade</b> → PA volta ao normal.",
            "(c) Porque se <b>reajustam</b> ao novo nível em 1 a 2 dias (a descarga volta ao normal com PA alta). Ajudam pouco a longo prazo, via simpático "
            "renal; o controle crônico é do rim (curva de natriurese pressórica).",
            "(d) Episódios repetidos de <b>hipóxia</b> ativam os <b>quimiorreceptores</b> carotídeos, que excitam o centro vasomotor e ↑ o simpático, "
            "contribuindo para a hipertensão (o mesmo ocorre na obesidade grave)."]),
]

OPEN_EXTRA = [
    ("Compare as teorias vasodilatadora e da demanda de O₂ no controle agudo do fluxo local.",
     "Vasodilatadora: com metabolismo alto ou pouco O₂, o tecido libera adenosina, CO₂, K⁺, H⁺, lactato, histamina, que dilatam arteríolas e esfíncteres. "
     "Demanda de O₂: o músculo liso precisa de O₂ para se contrair; com pouco O₂ ele relaxa; explica a vasomoção cíclica dos esfíncteres (tudo ou nada). "
     "Provavelmente atuam juntas."),
    ("Explique a autorregulação do fluxo e suas duas teorias.",
     "Quando a PA sobe, o fluxo sobe e em menos de 1 minuto volta quase ao normal (70 a 175 mmHg: fluxo varia só 20 a 30%). Metabólica: o excesso de "
     "fluxo traz O₂ e lava vasodilatadores, e o vaso contrai. Miogênica: o estiramento despolariza o músculo liso, entra Ca²⁺ e ele contrai; "
     "é intrínseca e protege contra estiramento excessivo."),
    ("Descreva a via do óxido nítrico e dois fármacos que atuam nela.",
     "Cisalhamento (e ACh, bradicinina, Ang II) ativa a eNOS, que forma NO de arginina e O₂. O NO difunde para o músculo liso, ativa a guanilata ciclase "
     "solúvel, forma GMPc, ativa PKG e relaxa o vaso. Nitratos (nitroglicerina) liberam NO: angina. Sildenafila inibe a PDE-5, que degrada o GMPc: "
     "disfunção erétil."),
    ("Como ocorre o controle do fluxo a longo prazo?",
     "Mudança da vascularização em dias a meses: hipóxia → HIF → VEGF, FGF, PDGF, angiogenina → angiogênese (brotamento de vasos). A vascularização segue "
     "a necessidade máxima. Colaterais se abrem em minutos e crescem por meses. Remodelagem: pressão alta → parede mais grossa (eutrófica concêntrica "
     "nas arteríolas, hipertrófica nas grandes); fluxo alto → luz maior (excêntrica)."),
    ("Quais as três ações do simpático para elevar rapidamente a PA?",
     "Constrição das arteríolas (↑ resistência periférica), constrição das veias (desloca sangue para o coração, ↑ enchimento e força) e estímulo direto "
     "do coração (FC até 3×, contratilidade; DC até 2×). Dobra a PA em 5 a 10 s."),
    ("Compare barorreceptores, quimiorreceptores e resposta isquêmica do SNC.",
     "Barorreceptores: estiramento no seio carotídeo e arco aórtico; atuam de 60 a 180 mmHg com maior ganho perto de 100; tamponam variações rápidas e "
     "reajustam em 1 a 2 dias. Quimiorreceptores: corpos carotídeos e aórticos, sentem ↓ O₂ e ↑ CO₂/H⁺; importantes abaixo de 80 mmHg. Resposta isquêmica "
     "do SNC: isquemia do próprio centro vasomotor; abaixo de 60 mmHg, máxima em 15 a 20; eleva a PA até 250; é o último recurso."),
]

CARDS = [
    ("c", "Fração do DC em repouso: fígado {{c1::27%}}; rins {{c2::22%}}; músculo {{c3::15%}}; cérebro 14%; coração 4%."),
    ("c", "Maior fluxo por 100 g: {{c1::rins (≈ 360 mℓ/min/100 g)}}; músculo em repouso só {{c2::4}}."),
    ("c", "No exercício, metabolismo muscular ↑ {{c1::60×}} e fluxo ↑ até {{c2::20×}}."),
    ("c", "Controle local {{c1::agudo}}: segundos a minutos (diâmetro); {{c2::longo prazo}}: dias a meses (número de vasos)."),
    ("c", "Principal vasodilatador metabólico no coração: {{c1::adenosina}}."),
    ("c", "Vasodilatadores metabólicos: adenosina, {{c1::CO₂}}, fosfatos de adenosina, histamina, {{c2::K⁺}} e {{c3::H⁺}}."),
    ("c", "Deficiência de {{c1::tiamina (beribéri)}} causa vasodilatação periférica 2 a 3×."),
    ("c", "Hiperemia {{c1::reativa}}: após oclusão, fluxo ↑ {{c2::4 a 7×}}.", "", "fig/f_hiperemia.png"),
    ("c", "Hiperemia {{c1::ativa}}: fluxo ↑ quando o {{c2::metabolismo}} do tecido aumenta."),
    ("c", "Autorregulação aguda: de {{c1::70 a 175 mmHg}} o fluxo varia só {{c2::20 a 30%}}.", "", "fig/f_autorregulacao.png"),
    ("c", "Teorias da autorregulação: {{c1::metabólica}} e {{c2::miogênica}}."),
    ("c", "Resposta miogênica: estiramento → {{c1::despolarização}} → entrada de {{c2::Ca²⁺}} → contração."),
    ("c", "Rim: {{c1::feedback tubuloglomerular}} pela {{c2::mácula densa}}."),
    ("c", "No cérebro, {{c1::CO₂}} e {{c2::H⁺}} dilatam fortemente os vasos."),
    ("c", "Pele: fluxo de 3 mℓ/min/100 g no frio até {{c1::7 a 8 ℓ/min}} no calor, controlado pelo {{c2::simpático}}."),
    ("c", "NO: {{c1::eNOS}} → NO → {{c2::guanilato ciclase solúvel}} → {{c3::GMPc}} → relaxamento.", "", "fig/f_endotelio.png"),
    ("c", "Estímulo principal para liberar NO: {{c1::tensão de cisalhamento}}."),
    ("c", "Meia-vida do NO no sangue: ≈ {{c1::6 s}}."),
    ("c", "Sildenafila inibe a {{c1::PDE-5}}; nitratos {{c2::liberam NO}}."),
    ("c", "{{c1::Endotelina}}: vasoconstritor potente liberado pelo endotélio {{c2::lesado}}."),
    ("c", "Controle agudo corrige só ≈ {{c1::3/4}}; PA 100 → 150 deixa o fluxo {{c2::10 a 15%}} acima após 2 min."),
    ("c", "Angiogênese: hipóxia → {{c1::HIF}} → {{c2::VEGF}}."),
    ("c", "Inibidores naturais da angiogênese: {{c1::angiostatina}} e {{c2::endostatina}}."),
    ("c", "A vascularização segue a necessidade {{c1::máxima}}, não a média."),
    ("c", "O₂ alto no prematuro e retirada súbita: {{c1::retinopatia da prematuridade}}."),
    ("c", "Colaterais: {{c1::metade}} da necessidade em 1 dia; suficiente em {{c2::poucos dias}}."),
    ("c", "Pressão crônica alta em arteríolas: remodelagem {{c1::eutrófica concêntrica}}; em grandes artérias: {{c2::hipertrófica}}.",
     "", "fig/f_remodelagem.png"),
    ("c", "Fluxo crônico alto (fístula AV): remodelagem {{c1::excêntrica}} (↑ luz)."),
    ("c", "Vasoconstritor mais potente: {{c1::vasopressina}}; depois {{c2::angiotensina II}}."),
    ("c", "1 µg de angiotensina II pode ↑ a PA em ≥ {{c1::50 mmHg}}."),
    ("c", "Bradicinina: calicreína → {{c1::calidina}} → bradicinina; inativada pela {{c2::ECA}}."),
    ("c", "Histamina e bradicinina: vasodilatação + ↑ {{c1::permeabilidade capilar}}."),
    ("c", "Íons: ↑ {{c1::Ca²⁺}} contrai; ↑ K⁺, Mg²⁺ e H⁺ {{c2::dilatam}}."),
    ("c", "O simpático inerva todos os vasos exceto os {{c1::capilares}}."),
    ("c", "Constrição simpática forte em {{c1::rins, intestino, baço e pele}}; fraca em músculo, coração e cérebro."),
    ("c", "Tônus vasoconstritor simpático: {{c1::0,5 a 2}} impulsos/s; raquianestesia total: PA {{c2::100 → 50 mmHg}}."),
    ("c", "Área vasoconstritora: bulbo {{c1::anterolateral superior}}; área sensorial: {{c2::núcleo do trato solitário}}.",
     "", "fig/f_centro_vasomotor.png"),
    ("c", "Noradrenalina contrai vasos via receptores {{c1::α}}."),
    ("c", "Síncope vasovagal: vasodilatação {{c1::muscular}} + {{c2::bradicardia vagal}}."),
    ("c", "O controle nervoso dobra a PA em {{c1::5 a 10 s}}."),
    ("c", "Seio carotídeo → nervo de {{c1::Hering}} → {{c2::glossofaríngeo}}; arco aórtico → {{c3::vago}}."),
    ("c", "Seio carotídeo: sem disparo abaixo de {{c1::50 a 60 mmHg}}; máximo em ≈ {{c2::180}}; maior ganho em ≈ {{c3::100}}.",
     "", "fig/f_barorreceptor.png"),
    ("c", "Barorreceptores {{c1::reajustam}} ao novo nível em {{c2::1 a 2 dias}}."),
    ("c", "Sem barorreceptores, a faixa diária de PA fica {{c1::2,5×}} maior."),
    ("c", "Quimiorreceptores importam com PA abaixo de {{c1::80 mmHg}}."),
    ("c", "Resposta isquêmica do SNC: abaixo de {{c1::60 mmHg}}; PA até {{c2::250 mmHg}}.", "", "fig/f_faixas.png"),
    ("c", "Reação de {{c1::Cushing}}: ↑ pressão do liquor → resposta isquêmica → PA ↑."),
    ("c", "Reflexo de {{c1::Bainbridge}}: átrio estirado → FC ↑ {{c2::40 a 60%}}.", "", "fig/f_baixa_pressao.png"),
    ("c", "Estiramento atrial: ↓ simpático renal, ↓ {{c1::ADH}} e ↑ {{c2::peptídeo natriurético atrial}}."),
    ("c", "Ondas de {{c1::Mayer}}: 10 a 40 mmHg, a cada 7 a 10 s, por oscilação do {{c2::barorreflexo}}."),
    ("b", "Três ações simpáticas que elevam a PA rapidamente?", "Contrai arteríolas (↑ RPT), contrai veias (↑ retorno) e estimula o coração (FC e força)."),
    ("b", "Por que vasoativos crônicos mudam pouco o fluxo tecidual?", "Porque a <b>autorregulação</b> ajusta o fluxo ao metabolismo; só muda se o metabolismo mudar."),
]

TOPIC = dict(
    code="f", slug="f-controle-circulacao", title="Controle local, humoral e nervoso da circulação",
    source="Guyton & Hall, Tratado de Fisiologia Médica, caps. 17 e 18",
    sections=SECTIONS, mcq=MCQ, open=OPEN, open_extra=OPEN_EXTRA, cards=CARDS, occ="dia_f",
)
