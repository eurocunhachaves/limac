"""Tema e: Microcirculação e sistema linfático (Guyton & Hall, cap. 16)."""

SECTIONS = [
    ("1. Estrutura da microcirculação", [
        ("fig", "fig/e_microcirculacao.png", None, "Leito microcirculatório: arteríola, metarteríola, esfíncteres pré-capilares, capilares e vênula.", 16),
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
        ("fig", "fig/e_parede.png", None, "Vias de passagem pela parede capilar.", 16),
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
        ("fig", "fig/e_tipos.png", None, "Os poros variam com o órgão.", 16),
        ("box", "O que a prova cobra", [
            "<b>Cérebro</b>: junções oclusivas (barreira hematoencefálica). <b>Fígado</b>: sinusoides, passam até proteínas. "
            "<b>Glomérulo</b>: fenestrações, permeabilidade à água ≈ 500× a do músculo, mas não às proteínas. <b>Intestino</b>: intermediário.",
            "A albumina é um pouco maior que a fenda: por isso quase não sai e gera a pressão oncótica do plasma.",
        ]),
    ]),
    ("3. Interstício", [
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
        ("fig", "fig/e_starling.png", None, "As quatro forças ao longo do capilar (valores médios do Guyton).", 16.5),
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
    ]),
    ("5. Sistema linfático", [
        ("fig", "fig/e_linfatico.png", None, "Capilar linfático terminal: filamentos de ancoragem e bordas que funcionam como válvulas.", 13),
        ("ul", [
            "Via acessória do interstício para o sangue. Função vital: devolver as <b>proteínas</b> que escaparam (sem isso, morte em ≈ <b>24 h</b>). "
            "Também absorve as <b>gorduras</b> do intestino (linfa com 1 a 2% de gordura após refeição) e filtra bactérias nos linfonodos.",
            "Volume: ≈ <b>1/10 do filtrado</b>; ≈ <b>120 mℓ/h</b> (100 pelo ducto torácico), <b>2 a 3 ℓ/dia</b>.",
            "<b>Ducto torácico</b>: parte inferior do corpo + lado esquerdo da cabeça, braço E e tórax; desemboca na junção <b>jugular interna E + "
            "subclávia E</b>. <b>Ducto linfático direito</b>: lado direito da cabeça, pescoço, braço D e tórax D.",
            "Sem linfáticos: pele superficial, <b>SNC</b>, endomísio e ossos (têm <b>pré-linfáticos</b>; no cérebro drenam para o liquor).",
            "Proteína na linfa: tecidos ≈ 2 g/dℓ; <b>fígado 6</b>; intestino 3 a 4; ducto torácico 3 a 5 g/dℓ (2/3 da linfa vem do fígado e intestino).",
        ]),
        ("fig", "fig/e_fluxo_linfa.png", None, "Fluxo linfático em função da pressão intersticial.", 13),
        ("ul", [
            "Aumentam o fluxo linfático: <b>↑ Pc</b>, <b>↓ Πp</b>, <b>↑ Πi</b>, <b>↑ permeabilidade</b> capilar (todos ↑ Pi).",
            "<b>Bomba linfática</b>: cada segmento entre válvulas se contrai quando é estirado; ducto torácico gera 50 a 100 mmHg. "
            "Bomba externa, em ordem: <b>contração muscular</b>, movimento, pulso arterial, compressão externa. Exercício: <b>10 a 30×</b>.",
            "O bombeamento linfático é a causa da <b>Pi negativa</b>, que mantém os tecidos unidos (vácuo parcial). Perdeu a Pi negativa → edema.",
        ]),
        ("tip", "Ciclo proteína → linfa", "Proteína escapa para o interstício → ↑ Πi → mais filtração → ↑ volume e Pi → ↑ fluxo linfático, que remove "
                "o excesso de líquido e proteína até um novo estado estacionário. O linfático controla a proteína, o volume e a pressão do interstício."),
    ]),
]

MCQ = [
    dict(q="Qual estrutura controla a entrada de sangue em cada capilar verdadeiro?",
         opts=["Vênula", "Esfíncter pré-capilar", "Membrana basal", "Pericito da vênula", "Válvula linfática"],
         a=1, c="Anel de músculo liso na origem de cada capilar a partir da metarteríola; abre e fecha a entrada (vasomotricidade)."),
    dict(q="O principal fator que regula a vasomotricidade (abertura e fechamento de metarteríolas e esfíncteres pré-capilares) é:",
         opts=["A concentração de O₂ nos tecidos", "A pressão coloidosmótica do plasma", "A pressão venosa central",
               "A concentração de Na⁺ no plasma", "O fluxo linfático"],
         a=0, c="Com O₂ tecidual baixo, os períodos de fluxo ficam mais frequentes e mais longos, levando mais O₂ ao tecido."),
    dict(q="O oxigênio atravessa a parede capilar muito mais rápido que a glicose porque:",
         opts=["É transportado por cavéolas", "Tem carga positiva", "É lipossolúvel e atravessa a membrana do endotélio em toda a área",
               "Passa apenas pelas fenestrações", "É ativamente bombeado pelo endotélio"],
         a=2, c="Substâncias lipossolúveis (O₂, CO₂) não dependem dos poros; hidrossolúveis (glicose, Na⁺) só passam pelas fendas (≈ 1/1.000 da área)."),
    dict(q="A largura da fenda intercelular dos capilares do músculo é de aproximadamente:",
         opts=["0,6 a 0,7 nm", "6 a 7 nm", "60 a 70 nm", "0,6 a 0,7 µm", "6 a 7 µm"], keep=True,
         a=1, c="6 a 7 nm (60 a 70 Å), pouco menor que a albumina e ≈ 20× o diâmetro da água."),
    dict(q="Em relação à água, a permeabilidade relativa do capilar muscular à albumina é de cerca de:",
         opts=["0,6", "0,2", "0,03", "0,01", "0,001"], keep=True,
         a=4, c="Tabela 16.1: glicose 0,6; insulina 0,2; mioglobina 0,03; hemoglobina 0,01; albumina 0,001."),
    dict(q="Em qual órgão os capilares permitem a passagem de proteínas plasmáticas quase tão facilmente quanto a de água?",
         opts=["Cérebro", "Músculo esquelético", "Fígado", "Pele", "Glomérulo renal"],
         a=2, c="Os sinusoides hepáticos têm fendas quase totalmente abertas. No glomérulo, as fenestrações deixam passar água e íons, não proteínas."),
    dict(q="A barreira hematoencefálica deve-se principalmente a:",
         opts=["Fenestrações largas", "Junções oclusivas entre as células endoteliais", "Ausência de membrana basal",
               "Grande número de cavéolas", "Pressão capilar muito alta"],
         a=1, c="No cérebro, as junções são oclusivas: passam só moléculas muito pequenas (água, O₂, CO₂)."),
    dict(q="O líquido intersticial, em condições normais, move-se principalmente:",
         opts=["Como líquido livre, em correntes", "Por difusão através do gel de proteoglicanos",
               "Por transporte ativo nas fibras de colágeno", "Por fluxo em massa pelas fendas", "Pelos vasos linfáticos"],
         a=1, c="O líquido fica preso no gel tecidual e se move molécula a molécula (difusão a 95–99% da velocidade livre). Líquido livre &lt; 1%."),
    dict(q="Qual das forças abaixo tende a mover líquido para DENTRO do capilar?",
         opts=["Pressão hidrostática capilar", "Pressão coloidosmótica do plasma", "Pressão coloidosmótica intersticial",
               "Pressão intersticial negativa", "Aumento da permeabilidade capilar"],
         a=1, c="Πp (≈ 28 mmHg) é a única força para dentro nos valores normais. Pc, Πi e a Pi negativa puxam para fora."),
    dict(q="A pressão coloidosmótica normal do plasma é de aproximadamente:",
         opts=["8 mmHg", "17 mmHg", "28 mmHg", "40 mmHg", "60 mmHg"], keep=True,
         a=2, c="≈ 28 mmHg: 19 da proteína dissolvida e 9 do efeito Donnan (cátions retidos pelas proteínas)."),
    dict(q="Qual proteína responde pela maior parte da pressão oncótica do plasma?",
         opts=["Fibrinogênio", "Globulinas", "Albumina", "Hemoglobina", "Imunoglobulina M"],
         a=2, c="Albumina ≈ 80% (21,8 de 28 mmHg): é a mais abundante e a de menor peso, logo o maior número de moléculas."),
    dict(q="Pelos valores do Guyton, a pressão efetiva na extremidade arterial do capilar é:",
         opts=["0,3 mmHg para fora", "7 mmHg para dentro", "13 mmHg para fora", "28 mmHg para dentro", "41 mmHg para fora"],
         a=2, c="Para fora: Pc 30 + Pi 3 (negativa) + Πi 8 = 41. Para dentro: Πp 28. Resultado 13 mmHg para fora (filtração)."),
    dict(q="Na extremidade venosa do capilar, a pressão efetiva de reabsorção é de 7 mmHg, menor que a de filtração arterial. Mesmo assim, "
           "cerca de 9/10 do filtrado é reabsorvido porque:",
         opts=["A pressão oncótica é maior na extremidade venosa", "Os capilares venosos são mais numerosos e mais permeáveis",
               "Há transporte ativo de água", "A linfa empurra o líquido de volta", "A Pi fica positiva nessa região"],
         a=1, c="Maior área e permeabilidade compensam a menor pressão efetiva. O décimo restante vai para os linfáticos."),
    dict(q="O valor médio da pressão intersticial no tecido subcutâneo frouxo, segundo o Guyton, é de cerca de:",
         opts=["+6 mmHg", "0 mmHg", "−3 mmHg", "−8 mmHg", "−28 mmHg"], keep=True,
         a=2, c="≈ −3 mmHg (micropipeta −2; cápsula −6). Negativa por causa do bombeamento linfático. Pleura −8."),
    dict(q="Qual é a causa básica da pressão negativa do líquido intersticial?",
         opts=["A pressão oncótica do plasma", "O bombeamento pelo sistema linfático", "A contração das fibras de colágeno",
               "A pressão atmosférica", "A reabsorção venosa de proteínas"],
         a=1, c="Os linfáticos removem continuamente líquido e proteína do interstício, criando a pressão ligeiramente subatmosférica."),
    dict(q="Em qual destes tecidos a pressão do líquido intersticial é normalmente POSITIVA?",
         opts=["Tecido subcutâneo frouxo", "Espaço pleural", "Rim (dentro da cápsula)", "Espaço epidural", "Articulação sinovial"],
         a=2, c="Tecidos com envoltório rígido (rim, cérebro, músculo com fáscia, olho) têm Pi positiva (rim ≈ +6), ainda menor que a do envoltório."),
    dict(q="Na média de todo o capilar, o desequilíbrio de forças de Starling é de 0,3 mmHg para fora. Isso corresponde a uma filtração efetiva no corpo (sem os rins) de:",
         opts=["0,2 mℓ/min", "2 mℓ/min", "20 mℓ/min", "125 mℓ/min", "2 ℓ/min"], keep=True,
         a=1, c="≈ 2 mℓ/min, devolvidos pela linfa. Kf corporal = 2/0,3 ≈ 6,67 mℓ/min por mmHg."),
    dict(q="Se a pressão capilar média sobe 20 mmHg, a filtração efetiva aumenta aproximadamente:",
         opts=["2 vezes", "7 vezes", "20 vezes", "68 vezes", "200 vezes"], keep=True,
         a=3, c="PEF passa de 0,3 para 20,3 mmHg: ≈ 68×, 2 a 5× acima da capacidade máxima dos linfáticos → edema."),
    dict(q="Qual fator NÃO aumenta o fluxo linfático?",
         opts=["Aumento da pressão capilar", "Queda da pressão oncótica do plasma", "Aumento da pressão oncótica intersticial",
               "Aumento da permeabilidade capilar", "Aumento da pressão oncótica do plasma"],
         a=4, c="↑ Πp puxa líquido para o capilar, reduz a Pi e o fluxo linfático. Os outros quatro elevam a Pi e a linfa."),
    dict(q="Quando a pressão intersticial sobe de −6 para 0 mmHg, o fluxo linfático:",
         opts=["Cai pela metade", "Não se altera", "Dobra", "Aumenta mais de 20 vezes", "Para, porque os linfáticos colapsam"],
         a=3, c="Sobe mais de 20×. Acima de +1 a +2 mmHg forma-se um platô, pois a pressão tecidual comprime os linfáticos maiores."),
    dict(q="O fluxo diário de linfa num adulto em repouso é de aproximadamente:",
         opts=["20 a 30 mℓ", "200 a 300 mℓ", "2 a 3 ℓ", "20 a 30 ℓ", "180 ℓ"], keep=True,
         a=2, c="≈ 120 mℓ/h (100 pelo ducto torácico + 20 por outras vias) = 2 a 3 ℓ/dia."),
    dict(q="O ducto torácico desemboca no sistema venoso na junção entre:",
         opts=["Veia cava superior e átrio direito", "Veia jugular interna esquerda e veia subclávia esquerda",
               "Veia jugular interna direita e veia subclávia direita", "Veia porta e veia cava inferior", "Veias ázigo e hemiázigo"],
         a=1, c="O ducto linfático direito, menor, drena na junção jugular interna D + subclávia D."),
    dict(q="O que impede que a linfa reflua do capilar linfático para o interstício?",
         opts=["Filamentos de ancoragem", "Bordas sobrepostas das células endoteliais, que funcionam como válvulas", "Membrana basal espessa",
               "Pressão linfática negativa", "Junções oclusivas"],
         a=1, c="A borda de uma célula se sobrepõe à vizinha e só se abre para dentro. Os filamentos de ancoragem abrem as junções quando o tecido incha."),
    dict(q="Qual destas funções pertence exclusivamente ao sistema linfático, e sem a qual a morte ocorreria em cerca de 24 horas?",
         opts=["Absorção de glicose intestinal", "Devolução ao sangue das proteínas que extravasaram para o interstício",
               "Filtração de água no glomérulo", "Produção de albumina", "Reabsorção de Na⁺"],
         a=1, c="As proteínas não voltam pelo capilar sanguíneo; só pela linfa. A linfa também absorve gorduras e filtra bactérias nos linfonodos."),
    dict(q="O fator externo mais importante para o bombeamento linfático é:",
         opts=["Pulsação das artérias adjacentes", "Compressão por objetos externos", "Contração dos músculos esqueléticos circundantes",
               "Movimento respiratório do diafragma", "Gravidade"],
         a=2, c="Ordem do Guyton: contração muscular, movimento das partes do corpo, pulso arterial, compressão externa. No exercício, 10 a 30×."),
    dict(q="Em qual tecido a concentração de proteína na linfa é mais alta?",
         opts=["Músculo", "Pele", "Intestino", "Fígado", "Cérebro"],
         a=3, c="Fígado ≈ 6 g/dℓ (sinusoides abertos); intestino 3 a 4; maioria dos tecidos ≈ 2; ducto torácico 3 a 5 g/dℓ."),
]

OPEN = [
    dict(q="Mulher de 52 anos com cirrose hepática apresenta edema de membros inferiores e ascite. Albumina sérica 2,0 g/dℓ (normal 3,5 a 5,0). "
           "(a) Qual força de Starling está alterada e em que sentido? (b) Explique, com as forças, por que surge o edema. (c) Por que a queda da "
           "albumina pesa mais que a das globulinas? (d) Qual mecanismo de segurança tenta evitar o edema e por que ele é superado?",
         a=["(a) <b>Πp (pressão oncótica do plasma) ↓</b>. A albumina responde por ≈ 80% dos 28 mmHg; com metade da albumina, a Πp cai muito.",
            "(b) PEF = Pc − Pi − Πp + Πi. Com Πp menor, a força para dentro cai: a <b>filtração aumenta</b> e a reabsorção venosa diminui. Quando "
            "o filtrado supera a capacidade dos linfáticos, o líquido se acumula no interstício (edema) e na cavidade peritoneal (ascite, também por "
            "hipertensão portal ↑ Pc).",
            "(c) A pressão osmótica depende do <b>número de moléculas</b>. A albumina é a proteína mais abundante e a mais leve (69.000): 1 g de "
            "globulina tem metade das moléculas de 1 g de albumina.",
            "(d) O <b>fluxo linfático</b> aumenta (Pi sobe de negativa para ≈ 0, fluxo ↑ &gt; 20×) e remove líquido e proteína (↓ Πi). "
            "Mas o fluxo tem um <b>platô</b> (Pi &gt; +1 a +2 comprime os linfáticos); acima disso o líquido se acumula."]),
    dict(q="Homem de 68 anos com insuficiência cardíaca esquerda descompensada tem pressão capilar pulmonar de 28 mmHg, dispneia e estertores. "
           "Seu vizinho, submetido a mastectomia com retirada de linfonodos axilares, tem o braço inchado. (a) Qual força de Starling explica o "
           "caso do primeiro paciente? (b) Por que o edema aparece quando a pressão capilar sobe? Use os números do Guyton. (c) Qual o mecanismo "
           "do edema do braço? (d) Por que esse edema tende a ser rico em proteína?",
         a=["(a) <b>↑ Pc</b> (pressão hidrostática capilar), por congestão venosa retrógrada do átrio esquerdo.",
            "(b) Na média, a PEF é só <b>0,3 mmHg</b> (filtração ≈ 2 mℓ/min). Um aumento de 20 mmHg em Pc eleva a PEF a 20,3: filtração <b>≈ 68×</b> "
            "maior, 2 a 5× acima da capacidade máxima dos linfáticos. O excesso se acumula no interstício (no pulmão, edema pulmonar).",
            "(c) <b>Obstrução linfática</b> (linfedema): sem os linfonodos e vasos, o 1/10 do filtrado que deveria voltar pela linfa fica no interstício.",
            "(d) Porque as <b>proteínas só voltam pela linfa</b>. Elas se acumulam, elevam a Πi, que puxa ainda mais líquido para fora (ciclo vicioso)."]),
    dict(q="Criança com queimadura extensa desenvolve edema intenso nas áreas lesadas e queda do volume plasmático. "
           "(a) Qual alteração da parede capilar explica o edema? (b) Como ela afeta Kf e as pressões oncóticas? "
           "(c) Por que o volume plasmático cai? (d) Cite as quatro forças de Starling com seus valores normais e a fórmula da pressão efetiva.",
         a=["(a) <b>↑ permeabilidade capilar</b> (lesão endotelial e mediadores inflamatórios): as fendas se alargam.",
            "(b) <b>Kf ↑</b> (mais filtração para a mesma PEF). A proteína passa para o interstício: <b>Πp ↓ e Πi ↑</b>, e a força para fora cresce ainda mais.",
            "(c) Líquido e proteína saem do plasma para o interstício (e para fora, pela pele queimada) mais rápido do que a linfa consegue devolver: "
            "hipovolemia e risco de choque.",
            "(d) Pc ≈ 17 mmHg (média; 30 arterial, 10 venosa), Pi ≈ −3, Πp ≈ 28, Πi ≈ 8. <b>PEF = Pc − Pi − Πp + Πi</b> = 17,3 + 3 − 28 + 8 ≈ 0,3 mmHg para fora."]),
]

OPEN_EXTRA = [
    ("Descreva a estrutura da microcirculação e a função do esfíncter pré-capilar.",
     "Artéria → arteríolas (10 a 15 µm, músculo contínuo) → metarteríolas (músculo intermitente) → capilares verdadeiros (endotélio + membrana "
     "basal, 0,5 µm) → vênulas. O esfíncter pré-capilar é um anel muscular na origem de cada capilar: abre e fecha a entrada. Metarteríolas e "
     "esfíncteres ficam junto do tecido e respondem às condições locais (O₂, metabólitos, H⁺): vasomotricidade."),
    ("Como as substâncias atravessam a parede capilar?",
     "Principalmente por difusão. Lipossolúveis (O₂, CO₂) atravessam a membrana do endotélio em toda a área. Hidrossolúveis (água, íons, glicose) "
     "passam pelas fendas intercelulares de 6 a 7 nm (1/1.000 da área), que bastam pela enorme velocidade térmica. Proteínas quase não passam; "
     "macromoléculas usam cavéolas (transcitose). A difusão é proporcional ao gradiente de concentração e cai com o tamanho da molécula."),
    ("Faça o balanço de Starling nas extremidades arterial e venosa e na média.",
     "Arterial: fora 30 + 3 + 8 = 41; dentro 28 → 13 mmHg para fora. Venosa: fora 10 + 3 + 8 = 21; dentro 28 → 7 mmHg para dentro. "
     "Média: fora 17,3 + 3 + 8 = 28,3; dentro 28 → 0,3 mmHg para fora = filtração efetiva ≈ 2 mℓ/min, que volta pela linfa."),
    ("Por que a pressão intersticial é negativa e qual sua importância?",
     "Porque os linfáticos bombeiam continuamente líquido e proteína para fora do interstício. A pressão ≈ −3 mmHg mantém os tecidos unidos "
     "(vácuo parcial) onde há pouco tecido conjuntivo e deixa uma margem antes do edema: a Pi precisa subir até ≈ 0 para o fluxo linfático "
     "aumentar muito."),
    ("Quais os determinantes do fluxo linfático?",
     "Fluxo = pressão do líquido intersticial × atividade da bomba linfática. Aumentam a Pi: ↑ Pc, ↓ Πp, ↑ Πi, ↑ permeabilidade. A bomba é a "
     "contração do músculo liso entre válvulas (até 50 a 100 mmHg no ducto torácico) e a compressão externa (músculos, movimento, pulso arterial). "
     "Fluxo ↑ &gt; 20× de −6 a 0 mmHg; platô acima de +1 a +2."),
    ("Quais as funções do sistema linfático?",
     "Devolver ao sangue a proteína e o excesso de líquido do interstício (vital: sem isso morte em ≈ 24 h), controlando concentração de proteína, "
     "volume e pressão intersticiais; absorver gorduras do intestino (quilomícrons); levar bactérias e partículas aos linfonodos para destruição."),
]

CARDS = [
    ("c", "O corpo tem ≈ {{c1::10 bilhões}} de capilares, com {{c2::500 a 700 m²}}; nenhuma célula fica a mais de {{c3::20 a 30 µm}} de um capilar."),
    ("c", "Arteríolas têm {{c1::10 a 15 µm}} e músculo contínuo; metarteríolas têm músculo {{c2::intermitente}}.", "", "fig/e_microcirculacao.png"),
    ("c", "O {{c1::esfíncter pré-capilar}} abre e fecha a entrada de cada capilar verdadeiro."),
    ("c", "Parede capilar ≈ {{c1::0,5 µm}}; diâmetro interno {{c2::4 a 9 µm}}."),
    ("c", "Vasomotricidade: fluxo {{c1::intermitente}} nos capilares; principal regulador: {{c2::O₂ tecidual}}."),
    ("c", "Difusão é o meio {{c1::mais importante}} de troca entre plasma e interstício."),
    ("c", "O₂ e CO₂ são {{c1::lipossolúveis}}: atravessam a membrana do endotélio; água e glicose passam pelas {{c2::fendas intercelulares}}.",
     "", "fig/e_parede.png"),
    ("c", "Fenda intercelular: {{c1::6 a 7 nm}}, ≈ {{c2::1/1.000}} da área da parede."),
    ("c", "A água do plasma troca com o interstício ≈ {{c1::80×}} durante a passagem pelo capilar."),
    ("c", "Permeabilidade relativa (água = 1): glicose {{c1::0,6}}; albumina {{c2::0,001}}."),
    ("c", "Cérebro: junções {{c1::oclusivas}}; fígado: fendas {{c2::quase abertas}} (passam proteínas); glomérulo: {{c3::fenestrações}}.",
     "", "fig/e_tipos.png"),
    ("c", "Cavéolas são formadas por {{c1::caveolina}} e participam da {{c2::transcitose}} de macromoléculas."),
    ("c", "O interstício é ≈ {{c1::1/6}} do volume corporal; sólidos: {{c2::colágeno}} e {{c3::proteoglicanos}} (98% ácido hialurônico)."),
    ("c", "Líquido intersticial fica preso como {{c1::gel}}; o líquido livre é {{c2::&lt; 1%}} (sobe muito no edema)."),
    ("c", "PEF = {{c1::Pc − Pi − Πp + Πi}}; filtração = {{c2::Kf × PEF}}."),
    ("c", "Pc: extremidade arterial {{c1::30}}, venosa {{c2::10}}, média funcional {{c3::17 mmHg}}.", "", "fig/e_starling.png"),
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
    ("c", "Pi de −6 para 0 mmHg → fluxo linfático ↑ {{c1::&gt; 20×}}; platô acima de {{c2::+1 a +2 mmHg}}.", "", "fig/e_fluxo_linfa.png"),
    ("c", "Fluxo linfático = {{c1::Pi}} × {{c2::atividade da bomba linfática}}."),
    ("c", "A bomba do ducto torácico gera até {{c1::50 a 100 mmHg}}; no exercício o fluxo sobe {{c2::10 a 30×}}."),
    ("b", "Quais fatores aumentam o fluxo linfático?", "↑ Pc, ↓ Πp, ↑ Πi e ↑ permeabilidade capilar (todos elevam a Pi)."),
    ("b", "Qual a causa básica da Pi negativa?", "O <b>bombeamento linfático</b>, que remove continuamente líquido e proteína do interstício."),
    ("b", "Por que 7 mmHg de reabsorção compensam 13 de filtração?", "Capilares venosos são <b>mais numerosos e mais permeáveis</b>."),
    ("b", "Como a linfa entra no capilar linfático e não volta?", "Filamentos de ancoragem abrem as junções quando o tecido incha; "
     "as bordas sobrepostas funcionam como <b>válvulas</b> que só abrem para dentro.", "fig/e_linfatico.png"),
    ("b", "Quatro causas de edema pelas forças de Starling?", "↑ Pc (IC, obstrução venosa), ↓ Πp (cirrose, síndrome nefrótica, desnutrição), "
     "↑ permeabilidade (queimadura, inflamação) e obstrução linfática (linfedema)."),
]

TOPIC = dict(
    code="e", slug="e-microcirculacao-linfatico", title="Microcirculação e sistema linfático",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 16",
    sections=SECTIONS, mcq=MCQ, open=OPEN, open_extra=OPEN_EXTRA, cards=CARDS, occ="dia_e",
)
