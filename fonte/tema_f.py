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
        ("fig", None, "fig_livro/g17_03.png", "Teoria da demanda de O₂: pouco O₂ relaxa metarteríolas e esfíncteres pré-capilares.", 7.5),
        ("fig", None, "fig_livro/g17_04.png", "Hiperemia reativa (após oclusão) e hiperemia ativa (após exercício).", 7.5),
        ("fig", None, "fig_livro/g17_05.png", "Autorregulação: aguda (vermelho) e de longo prazo (tracejado verde).", 8),
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
        ("fig", None, "fig_livro/g17_06.png", "Cisalhamento → eNOS → NO → guanilato ciclase solúvel → GMPc → relaxamento.", 8.5),
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
        ("fig", None, "fig_livro/g17_08.png", "Tipos de remodelagem vascular.", 6.5),
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
        ("fig", None, "fig_livro/g18_03.png", "Áreas do encéfalo que controlam a circulação; o centro vasomotor fica no bulbo e na ponte.", 8.5),
        ("ul", [
            "Simpático: fibras de T1 a L1-L2 → cadeia simpática → nervos viscerais e nervos espinhais. Inerva <b>todos os vasos exceto capilares</b>. "
            "Arteríolas: ↑ resistência. Veias: ↓ volume, empurram sangue ao coração. Coração: ↑ FC e força.",
            "Constrição simpática forte em <b>rins, intestino, baço e pele</b>; fraca em músculo, coração e cérebro.",
            "Parassimpático (vago): papel vascular pequeno; efeito principal é <b>↓ FC</b> (e leve ↓ contratilidade).",
            "<b>Tônus vasoconstritor</b>: disparo contínuo de <b>0,5 a 2 impulsos/s</b>. Raquianestesia total: PA cai de <b>100 para 50 mmHg</b>.",
            "Noradrenalina age em <b>receptores α</b>. Medula adrenal libera adrenalina e noradrenalina ao mesmo tempo (sistema duplo).",
            "<b>Síncope vasovagal</b>: emoção → hipotálamo anterior → vasodilatação muscular + vago forte (FC ↓) → PA ↓ → desmaio.",
        ]),
        ("fig", None, "fig_livro/g18_04.png", "Raquianestesia total: perda do tônus simpático, PA 100 → 50 mmHg; noradrenalina a restaura.", 7.5),
        ("box", "O controle nervoso é o mais rápido", [
            "Três ações simultâneas: <b>arteríolas contraem</b> (↑ RPT), <b>veias contraem</b> (↑ retorno), <b>coração estimulado</b> (FC até 3×, DC até 2×).",
            "Dobra a PA em <b>5 a 10 s</b>; a inibição súbita a reduz à metade em 10 a 40 s.",
            "Exercício: PA ↑ 30 a 40% (ativação reticular junto do córtex motor). <b>Reação de alarme</b>: PA ↑ 75 a 100 mmHg em segundos.",
        ]),
    ]),
    ("7. Reflexos que mantêm a PA", [
        ("fig", None, "fig_livro/g18_06.png", "Sistema barorreceptor: seio carotídeo (nervo de Hering → glossofaríngeo) e arco aórtico (vago).", 9),
        ("ul", [
            "<b>Barorreceptores</b>: terminações livres de estiramento no <b>seio carotídeo</b> (carótida interna, acima da bifurcação) e no "
            "<b>arco aórtico</b>. Carotídeo: nervo de <b>Hering → IX</b>; aórtico: <b>X</b>; ambos → <b>núcleo do trato solitário</b>.",
            "Carotídeos: silenciosos de 0 a 50–60 mmHg, máximo ≈ 180; os aórticos operam ≈ 30 mmHg acima. Respondem mais a pressão que <b>varia</b> "
            "(até 2× mais do que a estável).",
            "Ocluir as carótidas comuns → ↓ disparo → PA sobe. Ao levantar-se, evitam a queda da PA na cabeça.",
            "<b>Tampão</b>: sem eles a faixa de PA do dia aumenta 2,5× (50 a &gt; 160 mmHg); com eles, variação ≈ <b>1/3</b>. Reajustam em "
            "<b>1 a 2 dias</b>, mas não totalmente (ajudam via simpático renal). Estimulação crônica do seio carotídeo ↓ PA 15 a 20 mmHg.",
        ]),
        ("fig", None, "fig_livro/g18_05.png", "Resposta do seio carotídeo: sem disparo abaixo de 50–60 mmHg, ganho máximo (ΔI/ΔP) perto de 100 mmHg.", 7.5),
        ("fig", None, "fig_livro/g18_09.png", "PA ao longo do dia: com barorreceptores (normal) e sem eles (desnervado).", 7.5),
        ("ul", [
            "<b>Quimiorreceptores</b> (corpos carotídeos e aórticos, ≈ 2 mm, fluxo abundante): sentem ↓ O₂, ↑ CO₂ e ↑ H⁺; excitam o centro vasomotor "
            "quando a PA cai <b>abaixo de 80</b>. Contribuem para HAS na obesidade e na <b>apneia do sono</b>.",
            "<b>Resposta isquêmica do SNC</b>: isquemia do centro vasomotor (acúmulo de CO₂) → PA até <b>250 mmHg</b> por até 10 min; rim pode parar de "
            "urinar. Só abaixo de <b>60</b> (máxima em 15 a 20): último recurso.",
            "<b>Reação de Cushing</b>: ↑ pressão do liquor comprime as artérias cerebrais → resposta isquêmica → PA sobe até ficar pouco acima da pressão "
            "do liquor (clínica: hipertensão com bradicardia na hipertensão intracraniana).",
        ]),
        ("fig", None, "fig_livro/g18_10.png", "Reflexos atriais e da artéria pulmonar (baixa pressão): Bainbridge e reflexo de volume.", 9),
        ("ul", [
            "<b>Compressão abdominal</b>: reflexos também contraem músculos abdominais, espremendo os reservatórios venosos → ↑ DC e PA. "
            "Paralisados têm mais hipotensão.",
            "Exercício: a contração muscular comprime vasos e ajuda o DC a subir <b>5 a 7×</b>; PA média 100 → <b>130 a 160</b>.",
            "<b>Ondas respiratórias</b>: 4 a 6 mmHg (até 20 na respiração profunda); a PA sobe no início da expiração. "
            "<b>Ondas de Mayer (vasomotoras)</b>: 10 a 40 mmHg, ciclos de 7 a 10 s no humano, por oscilação do barorreflexo (ou quimiorreflexo a 40–80 mmHg).",
        ]),
    ]),
]


G = "fig_livro/"
CARDS = [
    ("c", "Fração do DC em repouso: fígado {{c1::27%}}; rins {{c2::22%}}; músculo {{c3::15%}}; cérebro 14%; coração 4%."),
    ("c", "Maior fluxo por 100 g: {{c1::rins (≈ 360 mℓ/min/100 g)}}; músculo em repouso só {{c2::4}}."),
    ("c", "No exercício, metabolismo muscular ↑ {{c1::60×}} e fluxo ↑ até {{c2::20×}}."),
    ("c", "Controle local {{c1::agudo}}: segundos a minutos (diâmetro); {{c2::longo prazo}}: dias a meses (número de vasos)."),
    ("c", "Principal vasodilatador metabólico no coração: {{c1::adenosina}}."),
    ("c", "Vasodilatadores metabólicos: adenosina, {{c1::CO₂}}, fosfatos de adenosina, histamina, {{c2::K⁺}} e {{c3::H⁺}}."),
    ("c", "Deficiência de {{c1::tiamina (beribéri)}} causa vasodilatação periférica 2 a 3×."),
    ("c", "Hiperemia {{c1::reativa}}: após oclusão, fluxo ↑ {{c2::4 a 7×}}.", "", "fig_livro/g17_04.png"),
    ("c", "Hiperemia {{c1::ativa}}: fluxo ↑ quando o {{c2::metabolismo}} do tecido aumenta."),
    ("c", "Autorregulação aguda: de {{c1::70 a 175 mmHg}} o fluxo varia só {{c2::20 a 30%}}.", "", "fig_livro/g17_05.png"),
    ("c", "Teorias da autorregulação: {{c1::metabólica}} e {{c2::miogênica}}."),
    ("c", "Resposta miogênica: estiramento → {{c1::despolarização}} → entrada de {{c2::Ca²⁺}} → contração."),
    ("c", "Rim: {{c1::feedback tubuloglomerular}} pela {{c2::mácula densa}}."),
    ("c", "No cérebro, {{c1::CO₂}} e {{c2::H⁺}} dilatam fortemente os vasos."),
    ("c", "Pele: fluxo de 3 mℓ/min/100 g no frio até {{c1::7 a 8 ℓ/min}} no calor, controlado pelo {{c2::simpático}}."),
    ("c", "NO: {{c1::eNOS}} → NO → {{c2::guanilato ciclase solúvel}} → {{c3::GMPc}} → relaxamento.", "", "fig_livro/g17_06.png"),
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
     "", "fig_livro/g17_08.png"),
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
     "", "fig_livro/g18_03.png"),
    ("c", "Noradrenalina contrai vasos via receptores {{c1::α}}."),
    ("c", "Síncope vasovagal: vasodilatação {{c1::muscular}} + {{c2::bradicardia vagal}}."),
    ("c", "O controle nervoso dobra a PA em {{c1::5 a 10 s}}."),
    ("c", "Seio carotídeo → nervo de {{c1::Hering}} → {{c2::glossofaríngeo}}; arco aórtico → {{c3::vago}}."),
    ("c", "Seio carotídeo: sem disparo abaixo de {{c1::50 a 60 mmHg}}; máximo em ≈ {{c2::180}}; maior ganho em ≈ {{c3::100}}.",
     "", "fig_livro/g18_05.png"),
    ("c", "Barorreceptores {{c1::reajustam}} ao novo nível em {{c2::1 a 2 dias}}."),
    ("c", "Sem barorreceptores, a faixa diária de PA fica {{c1::2,5×}} maior."),
    ("c", "Quimiorreceptores importam com PA abaixo de {{c1::80 mmHg}}."),
    ("c", "Resposta isquêmica do SNC: abaixo de {{c1::60 mmHg}}; PA até {{c2::250 mmHg}}.", "", "fig_livro/g18_09.png"),
    ("c", "Reação de {{c1::Cushing}}: ↑ pressão do liquor → resposta isquêmica → PA ↑."),
    ("c", "Reflexo de {{c1::Bainbridge}}: átrio estirado → FC ↑ {{c2::40 a 60%}}.", "", "fig_livro/g18_10.png"),
    ("c", "Estiramento atrial: ↓ simpático renal, ↓ {{c1::ADH}} e ↑ {{c2::peptídeo natriurético atrial}}."),
    ("c", "Ondas de {{c1::Mayer}}: 10 a 40 mmHg, a cada 7 a 10 s, por oscilação do {{c2::barorreflexo}}."),
    ("b", "Três ações simpáticas que elevam a PA rapidamente?", "Contrai arteríolas (↑ RPT), contrai veias (↑ retorno) e estimula o coração (FC e força)."),
    ("b", "Por que vasoativos crônicos mudam pouco o fluxo tecidual?", "Porque a <b>autorregulação</b> ajusta o fluxo ao metabolismo; só muda se o metabolismo mudar."),
]

OCC_IMG = [
    (G + "g17_04.png", 'Hiperemia reativa', 'Qual fenômeno?', '<b>Hiperemia reativa</b>: após oclusão, fluxo ↑ 4 a 7×.'),
    (G + "g17_04.png", 'Hiperemia ativa', 'Qual fenômeno?', '<b>Hiperemia ativa</b>: metabolismo ↑ → fluxo ↑ (músculo até 20×).'),
    (G + "g17_05.png", 'Agudo', 'Qual curva?', '<b>Autorregulação aguda</b> (70 a 175 mmHg; fluxo varia 20 a 30%).'),
    (G + "g17_05.png", 'Longo prazo', 'Qual curva?', '<b>Autorregulação de longo prazo</b> (quase plana de 50 a 200 mmHg).'),
    (G + "g17_06.png", 'L-Arginina', 'Substrato da eNOS?', '<b>L-arginina</b> (+ O₂ → NO + L-citrulina).'),
    (G + "g17_06.png", 'Guanilato ciclase solúvel', 'Alvo do NO no músculo liso?', '<b>Guanilato ciclase solúvel</b> → GMPc.'),
    (G + "g17_08.png", 'Remodelagem eutrófica concêntrica', 'Qual remodelagem (arteríola na hipertensão)?', '<b>Eutrófica concêntrica</b>: luz menor, mesma área de parede.'),
    (G + "g17_08.png", 'Remodelagem hipertrófica', 'Qual remodelagem (grandes artérias na hipertensão)?', '<b>Hipertrófica</b>: parede mais grossa e rígida.'),
    (G + "g17_08.png", 'Remodelagem eutrófica excêntrica', 'Qual remodelagem (↑ fluxo crônico, ex.: fístula AV)?', '<b>Eutrófica excêntrica</b>: ↑ luz, parede igual.'),
    (G + "g18_03.png", 'VASOMOTOR', 'Qual centro?', '<b>Centro vasomotor</b> (bulbo e ponte inferior).'),
    (G + "g18_06.png", 'Nervo de Hering', 'Qual nervo?', '<b>Nervo de Hering</b> → glossofaríngeo (IX).'),
    (G + "g18_06.png", 'Seio carotídeo', 'Qual estrutura?', '<b>Seio carotídeo</b>: barorreceptores (estiramento).'),
    (G + "g18_06.png", 'Corpo carotídeo (quimiorreceptor)', 'Qual estrutura?', '<b>Corpo carotídeo</b>: quimiorreceptor (↓ O₂, ↑ CO₂, ↑ H⁺).'),
    (G + "g18_06.png", 'Barorreceptores aórticos', 'Qual estrutura (e nervo)?', '<b>Barorreceptores aórticos</b> → nervo vago (X).'),
    (G + "g18_06.png", 'Nervo vago', 'Qual nervo?', '<b>Vago (X)</b>: leva os sinais do arco aórtico.'),
    (G + "g18_10.png", 'Bainbridge', 'Qual reflexo (átrio estirado → ↑ FC)?', '<b>Reflexo de Bainbridge</b>.'),
    (G + "g18_10.png", 'Hormônio antidiurético', 'Qual hormônio cai com o estiramento atrial?', '<b>Hormônio antidiurético (ADH)</b> ↓.'),
    (G + "g18_10.png", 'Peptídeo atrial natriurético', 'Qual hormônio sobe com o estiramento atrial?', '<b>Peptídeo natriurético atrial</b> ↑.'),
]

TOPIC = dict(
    code="f", slug="f-controle-circulacao", title="Controle local, humoral e nervoso da circulação",
    source="Guyton & Hall, Tratado de Fisiologia Médica, caps. 17 e 18",
    sections=SECTIONS, cards=CARDS, occ_img=OCC_IMG,
)
