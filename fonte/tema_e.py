"""Tema e: Microcirculação e sistema linfático (Guyton & Hall, cap. 16)."""

SECTIONS = [
    ("1. Estrutura da microcirculação", [
        ("fig", None, "fig_livro/g16_01.png", "Microcirculação: arteríola, metarteríolas, esfíncteres pré-capilares, capilares e vênulas.", 8.5),
        ("ul", [
            "Função: levar nutrientes e remover resíduos. ≈ <b>10 bilhões de capilares</b>, <b>500 a 700 m²</b> de superfície; quase nenhuma "
            "célula fica a mais de <b>20 a 30 µm</b> de um capilar.",
            "<b>Arteríolas</b> (10 a 15 µm): muito musculares, controlam o fluxo de cada tecido. <b>Metarteríolas</b>: músculo só em "
            "pontos intermitentes. <b>Esfíncter pré-capilar</b>: anel muscular na origem de cada capilar verdadeiro.",
            "<b>Vênulas</b>: maiores que as arteríolas e com músculo fraco, mas contraem bem porque a pressão nelas é baixa.",
            "Parede capilar: <b>1 camada de endotélio</b> + membrana basal, ≈ <b>0,5 µm</b>; luz de <b>4 a 9 µm</b> (a hemácia passa justa).",
        ]),
        ("tip", "Vasomotricidade", "O fluxo no capilar é <b>intermitente</b> (abre e fecha a cada segundos ou minutos) pela contração das "
                "metarteríolas e esfíncteres. O fator principal é o <b>O₂ tecidual</b>: com O₂ baixo, os períodos de fluxo ficam mais longos "
                "e mais frequentes. Como há bilhões de capilares, raciocinamos com os valores médios."),
    ]),
    ("2. Parede capilar e trocas por difusão", [
        ("fig", None, "fig_livro/g16_02.png", "Parede capilar: fenda intercelular entre as células endoteliais e cavéolas (transcitose).", 8),
        ("ul", [
            "<b>Difusão</b> é o principal meio de troca entre plasma e interstício. Só as <b>proteínas</b> não passam com facilidade.",
            "<b>Lipossolúveis</b> (O₂, CO₂) atravessam a membrana do endotélio em toda a área: muito mais rápidos.",
            "<b>Hidrossolúveis</b> (água, Na⁺, Cl⁻, glicose) passam pelas <b>fendas intercelulares</b> de <b>6 a 7 nm</b> (≈ 1/1.000 da área). "
            "Mesmo assim, a água do plasma troca com o interstício <b>≈ 80×</b> enquanto o sangue percorre o capilar.",
            "<b>Cavéolas</b> (vesículas com caveolina): endocitose e <b>transcitose</b> de macromoléculas.",
            "A difusão efetiva é proporcional à <b>diferença de concentração</b>: O₂ sai para o tecido, CO₂ entra no sangue.",
        ]),
        ("table", [
            ["Substância", "Peso molecular", "Permeabilidade relativa (músculo)"],
            ["Água", "18", "<b>1,00</b>"],
            ["NaCl · ureia", "58,5 · 60", "0,96 · 0,8"],
            ["Glicose", "180", "0,6"],
            ["Insulina", "5.000", "0,2"],
            ["Hemoglobina", "68.000", "0,01"],
            ["<b>Albumina</b>", "69.000", "<b>0,001</b>"],
        ], [5.0, 4.0, 8.4]),
        ("box", "O que a prova cobra", [
            "<b>Cérebro</b>: junções oclusivas (barreira hematoencefálica). <b>Fígado</b>: sinusoides, passam até proteínas. "
            "<b>Glomérulo</b>: fenestrações, permeabilidade à água ≈ 500× a do músculo, mas não às proteínas. <b>Intestino</b>: intermediário.",
            "A albumina é um pouco maior que a fenda: por isso quase não sai e gera a pressão oncótica do plasma.",
        ]),
    ]),
    ("3. Interstício", [
        ("fig", None, "fig_livro/g16_04.png", "Interstício: feixes de colágeno e filamentos de proteoglicanos (gel); o líquido livre é raro.", 8),
        ("ul", [
            "≈ <b>1/6</b> do volume corporal. Sólidos: <b>fibras de colágeno</b> (força) e <b>filamentos de proteoglicanos</b> "
            "(98% ácido hialurônico).",
            "O líquido fica preso entre os proteoglicanos como <b>gel tecidual</b>: move-se por <b>difusão</b> (95 a 99% da velocidade livre), "
            "não por fluxo.",
            "<b>Líquido livre</b>: normalmente <b>&lt; 1%</b>. No <b>edema</b>, a metade ou mais vira líquido livre.",
            "Composição igual à do plasma, mas com bem menos proteína (≈ 40% do plasma, ≈ 3 g/dℓ).",
        ]),
    ]),
    ("4. Forças de Starling e filtração", [
        ("fig", None, "fig_livro/g16_05.png", "As quatro forças de Starling que movem o líquido pela membrana capilar.", 8.5),
        ("box", "Fórmulas", [
            "<b>PEF = Pc − Pi − Πp + Πi</b> (Pi negativa soma para fora).",
            "<b>Filtração = Kf × PEF</b>. Kf do corpo ≈ <b>6,67 mℓ/min por mmHg</b>; nos tecidos ≈ 0,01 mℓ/min/mmHg/100 g "
            "(pequeno no cérebro e músculo, enorme no fígado e glomérulo).",
        ]),
        ("table", [
            ["Força", "Valor", "Detalhe"],
            ["<b>Pc</b> (hidrostática capilar)", "arterial <b>30</b> · venosa <b>10</b> · funcional <b>17</b>",
             "Micropipeta: 30–40 → 10–15, meio ≈ 25. Glomérulo ≈ <b>60</b>; peritubular ≈ 13"],
            ["<b>Pi</b> (intersticial)", "≈ <b>−3</b> (subcutâneo)", "Micropipeta −2; cápsula −6. Encapsulados positivos: cérebro +4 a +6, rim +6"],
            ["<b>Πp</b> (oncótica do plasma)", "<b>28</b>", "19 da proteína + 9 do <b>efeito Donnan</b>; <b>albumina ≈ 80%</b>"],
            ["<b>Πi</b> (oncótica intersticial)", "<b>8</b>", "Proteína intersticial ≈ 3 g/dℓ (40% da do plasma)"],
        ], [4.4, 5.2, 7.8]),
        ("table", [
            ["Balanço", "Para fora", "Para dentro", "Resultado"],
            ["Extremidade arterial", "30 + 3 + 8 = 41", "28", "<b>13 para fora</b> (filtra ≈ 1/200 do plasma)"],
            ["Extremidade venosa", "10 + 3 + 8 = 21", "28", "<b>7 para dentro</b> (reabsorve 9/10)"],
            ["Média (equilíbrio de Starling)", "17,3 + 3 + 8 = 28,3", "28", "<b>0,3 para fora</b> → ≈ <b>2 mℓ/min</b> (vai para a linfa)"],
        ], [4.6, 3.8, 2.6, 6.4]),
        ("ul", [
            "Por que 7 mmHg bastam para reabsorver? Os capilares venosos são <b>mais numerosos e mais permeáveis</b>.",
            "Se Pc sobe <b>20 mmHg</b>: PEF vai de 0,3 a 20,3 → filtração <b>68×</b> maior, 2 a 5× acima da capacidade dos linfáticos "
            "→ <b>edema</b>. Se Pc cai muito: reabsorção efetiva, o volume sanguíneo sobe à custa do interstício.",
            "Cavidades com líquido livre também são negativas: <b>pleura −8</b>; sinovial e epidural −4 a −6 mmHg.",
        ]),
        ("fig", None, "fig_livro/g16_03.png", "O líquido filtrado no capilar volta quase todo ao sangue; o excesso vai para o linfático.", 9),
    ]),
    ("5. Sistema linfático", [
        ("fig", None, "fig_livro/g16_07.png", "Capilar linfático: bordas das células endoteliais funcionam como válvulas; filamentos de ancoragem.", 8.5),
        ("ul", [
            "Via acessória do interstício para o sangue. Função vital: devolver as <b>proteínas</b> que escaparam (sem isso, morte em ≈ <b>24 h</b>). "
            "Também absorve as <b>gorduras</b> do intestino (linfa com 1 a 2% de gordura após refeição) e filtra bactérias nos linfonodos.",
            "Volume: ≈ <b>1/10 do filtrado</b>; ≈ <b>120 mℓ/h</b> (100 pelo ducto torácico), <b>2 a 3 ℓ/dia</b>.",
            "<b>Ducto torácico</b>: parte inferior do corpo + lado esquerdo da cabeça, braço E e tórax; desemboca na junção <b>jugular interna E + "
            "subclávia E</b>. <b>Ducto linfático direito</b>: lado direito da cabeça, pescoço, braço D e tórax D.",
            "Sem linfáticos: pele superficial, <b>SNC</b>, endomísio e ossos (têm <b>pré-linfáticos</b>; no cérebro drenam para o liquor).",
            "Proteína na linfa: tecidos ≈ 2 g/dℓ; <b>fígado 6</b>; intestino 3 a 4; ducto torácico 3 a 5 g/dℓ (2/3 da linfa vem do fígado e intestino).",
        ]),
        ("fig", None, "fig_livro/g16_08.png", "Fluxo linfático × pressão intersticial: sobe muito até Pi ≈ 0 e depois faz platô.", 7.5),
        ("ul", [
            "Aumentam o fluxo linfático: <b>↑ Pc</b>, <b>↓ Πp</b>, <b>↑ Πi</b>, <b>↑ permeabilidade</b> capilar (todos ↑ Pi).",
            "<b>Bomba linfática</b>: cada segmento entre válvulas se contrai quando é estirado; ducto torácico gera 50 a 100 mmHg. "
            "Bomba externa, em ordem: <b>contração muscular</b>, movimento, pulso arterial, compressão externa. Exercício: <b>10 a 30×</b>.",
            "O bombeamento linfático é a causa da <b>Pi negativa</b>, que mantém os tecidos unidos (vácuo parcial). Perdeu a Pi negativa → edema.",
        ]),
        ("tip", "Ciclo proteína → linfa", "Proteína escapa para o interstício → ↑ Πi → mais filtração → ↑ volume e Pi → ↑ fluxo linfático, que remove "
                "o excesso de líquido e proteína até um novo estado estacionário. O linfático controla a proteína, o volume e a pressão do interstício."),
        ("fig", None, "fig_livro/g16_06.png", "Sistema linfático: ducto torácico, ducto linfático direito e linfonodos.", 12),
    ]),
]


G = "fig_livro/"
CARDS = [
    ("c", "O corpo tem ≈ {{c1::10 bilhões}} de capilares, com {{c2::500 a 700 m²}}; nenhuma célula fica a mais de {{c3::20 a 30 µm}} de um capilar."),
    ("c", "Arteríolas têm {{c1::10 a 15 µm}} e músculo contínuo; metarteríolas têm músculo {{c2::intermitente}}.", "", "fig_livro/g16_01.png"),
    ("c", "O {{c1::esfíncter pré-capilar}} abre e fecha a entrada de cada capilar verdadeiro."),
    ("c", "Parede capilar ≈ {{c1::0,5 µm}}; diâmetro interno {{c2::4 a 9 µm}}."),
    ("c", "Vasomotricidade: fluxo {{c1::intermitente}} nos capilares; principal regulador: {{c2::O₂ tecidual}}."),
    ("c", "Difusão é o meio {{c1::mais importante}} de troca entre plasma e interstício."),
    ("c", "O₂ e CO₂ são {{c1::lipossolúveis}}: atravessam a membrana do endotélio; água e glicose passam pelas {{c2::fendas intercelulares}}.",
     "", "fig_livro/g16_02.png"),
    ("c", "Fenda intercelular: {{c1::6 a 7 nm}}, ≈ {{c2::1/1.000}} da área da parede."),
    ("c", "A água do plasma troca com o interstício ≈ {{c1::80×}} durante a passagem pelo capilar."),
    ("c", "Permeabilidade relativa (água = 1): glicose {{c1::0,6}}; albumina {{c2::0,001}}."),
    ("c", "Cérebro: junções {{c1::oclusivas}}; fígado: fendas {{c2::quase abertas}} (passam proteínas); glomérulo: {{c3::fenestrações}}.",
     ""),
    ("c", "Cavéolas são formadas por {{c1::caveolina}} e participam da {{c2::transcitose}} de macromoléculas."),
    ("c", "O interstício é ≈ {{c1::1/6}} do volume corporal; sólidos: {{c2::colágeno}} e {{c3::proteoglicanos}} (98% ácido hialurônico)."),
    ("c", "Líquido intersticial fica preso como {{c1::gel}}; o líquido livre é {{c2::&lt; 1%}} (sobe muito no edema)."),
    ("c", "PEF = {{c1::Pc − Pi − Πp + Πi}}; filtração = {{c2::Kf × PEF}}."),
    ("c", "Pc: extremidade arterial {{c1::30}}, venosa {{c2::10}}, média funcional {{c3::17 mmHg}}.", "", "fig_livro/g16_05.png"),
    ("c", "Pc glomerular ≈ {{c1::60 mmHg}}; peritubular ≈ {{c2::13 mmHg}}."),
    ("c", "Pi no subcutâneo ≈ {{c1::−3 mmHg}}; pleura {{c2::−8}}; sinovial e epidural {{c3::−4 a −6}}."),
    ("c", "Tecidos encapsulados têm Pi {{c1::positiva}}: cérebro {{c2::+4 a +6}}, rim ≈ {{c3::+6 mmHg}}."),
    ("c", "Πp ≈ {{c1::28 mmHg}}: 19 da proteína + 9 do {{c2::efeito Donnan}}."),
    ("c", "A {{c1::albumina}} gera ≈ {{c2::80%}} da pressão oncótica do plasma."),
    ("c", "Πi ≈ {{c1::8 mmHg}} (proteína intersticial ≈ 3 g/dℓ)."),
    ("c", "Extremidade arterial: {{c1::13 mmHg}} para fora; extremidade venosa: {{c2::7 mmHg}} para dentro."),
    ("c", "Na média, a PEF é {{c1::0,3 mmHg}}, gerando filtração efetiva de ≈ {{c2::2 mℓ/min}}."),
    ("c", "Kf corporal ≈ {{c1::6,67 mℓ/min por mmHg}}."),
    ("c", "Reabsorve-se ≈ {{c1::9/10}} do filtrado; {{c2::1/10}} volta pela linfa."),
    ("c", "Pc + 20 mmHg → filtração ≈ {{c1::68×}} maior → {{c2::edema}}."),
    ("c", "Fluxo de linfa: ≈ {{c1::120 mℓ/h}}, {{c2::2 a 3 ℓ/dia}}."),
    ("c", "Ducto torácico drena na junção {{c1::jugular interna E + subclávia E}}."),
    ("c", "Sem linfáticos: pele superficial, {{c1::SNC}}, endomísio e ossos (têm {{c2::pré-linfáticos}})."),
    ("c", "Sem retorno linfático de proteínas, a morte ocorre em ≈ {{c1::24 h}}."),
    ("c", "Proteína na linfa do fígado ≈ {{c1::6 g/dℓ}}; ducto torácico {{c2::3 a 5 g/dℓ}}."),
    ("c", "Pi de −6 para 0 mmHg → fluxo linfático ↑ {{c1::&gt; 20×}}; platô acima de {{c2::+1 a +2 mmHg}}.", "", "fig_livro/g16_08.png"),
    ("c", "Fluxo linfático = {{c1::Pi}} × {{c2::atividade da bomba linfática}}."),
    ("c", "A bomba do ducto torácico gera até {{c1::50 a 100 mmHg}}; no exercício o fluxo sobe {{c2::10 a 30×}}."),
    ("b", "Quais fatores aumentam o fluxo linfático?", "↑ Pc, ↓ Πp, ↑ Πi e ↑ permeabilidade capilar (todos elevam a Pi)."),
    ("b", "Qual a causa básica da Pi negativa?", "O <b>bombeamento linfático</b>, que remove continuamente líquido e proteína do interstício."),
    ("b", "Por que 7 mmHg de reabsorção compensam 13 de filtração?", "Capilares venosos são <b>mais numerosos e mais permeáveis</b>."),
    ("b", "Como a linfa entra no capilar linfático e não volta?", "Filamentos de ancoragem abrem as junções quando o tecido incha; "
     "as bordas sobrepostas funcionam como <b>válvulas</b> que só abrem para dentro.", "fig_livro/g16_07.png"),
    ("b", "Quatro causas de edema pelas forças de Starling?", "↑ Pc (IC, obstrução venosa), ↓ Πp (cirrose, síndrome nefrótica, desnutrição), "
     "↑ permeabilidade (queimadura, inflamação) e obstrução linfática (linfedema)."),
]

OCC_IMG = [
    (G + "g16_01.png", 'Esfíncteres pré-capilares', 'Qual estrutura?', '<b>Esfíncteres pré-capilares</b>: abrem e fecham a entrada do capilar.'),
    (G + "g16_01.png", 'Metarteríolas', 'Qual estrutura?', '<b>Metarteríolas</b>: músculo liso intermitente.'),
    (G + "g16_01.png", 'Arteriola', 'Qual vaso?', '<b>Arteríola</b>: muito muscular, controla o fluxo do tecido.'),
    (G + "g16_01.png", 'Vênulas', 'Qual vaso?', '<b>Vênulas</b>.'),
    (G + "g16_02.png", ('intercelular', 0, (6, 14, 6, 0)), 'Por onde passam água e solutos hidrossolúveis?', '<b>Fenda intercelular</b> (6 a 7 nm).'),
    (G + "g16_02.png", 'Cavéolas (vesículas plasmáticas)', 'Qual estrutura faz a transcitose?', '<b>Cavéolas</b> (vesículas com caveolina).'),
    (G + "g16_05.png", 'Pressão capilar', 'Qual força (e valor médio)?', '<b>Pressão capilar (Pc)</b>: ≈ 17 mmHg funcional; empurra para fora.'),
    (G + "g16_05.png", 'Pressão coloidosmótica plasmática', 'Qual força (e valor)?', '<b>Pressão oncótica do plasma (Πp)</b>: 28 mmHg; puxa para dentro.'),
    (G + "g16_05.png", 'Pressão do líquido intersticial', 'Qual força (e valor)?', '<b>Pressão do líquido intersticial (Pi)</b>: ≈ −3 mmHg; negativa, puxa para fora.'),
    (G + "g16_05.png", 'Pressão coloidosmótica do líquido intersticial', 'Qual força (e valor)?', '<b>Pressão oncótica intersticial (Πi)</b>: 8 mmHg; puxa para fora.'),
]

TOPIC = dict(
    code="e", slug="e-microcirculacao-linfatico", title="Microcirculação e sistema linfático",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 16",
    sections=SECTIONS, cards=CARDS, occ_img=OCC_IMG,
)
