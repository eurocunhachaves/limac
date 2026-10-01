"""Tema d: Biofísica da circulação (Guyton & Hall, caps. 14 e 15)."""

SECTIONS = [
    ("1. Visão geral: onde está o sangue e onde está a pressão", [
        ("fig", None, "fig_livro/g14_01.png", "Distribuição do volume sanguíneo nas partes da circulação.", 7),
        ("table", [
            ["Segmento", "Função", "Detalhe que cai"],
            ["<b>Artérias</b>", "Levar sangue sob alta pressão", "Paredes fortes, fluxo rápido"],
            ["<b>Arteríolas</b>", "<b>Válvulas de controle</b> do fluxo", "Parede muscular forte: fecham ou dilatam várias vezes"],
            ["<b>Capilares</b>", "<b>Trocas</b> com o interstício", "Paredes finas com poros"],
            ["<b>Veias</b>", "Retorno e <b>reservatório</b> controlável", "Pressão baixa, parede fina mas com músculo"],
        ], [3.0, 5.6, 8.8]),
        ("ul", [
            "Volume: <b>84% na circulação sistêmica</b> (veias <b>64%</b>, artérias 13%, arteríolas + capilares 7%), coração 7%, pulmões 9%.",
            "<b>v = F / A</b>: a velocidade é inversa à área de secção. Aorta 2,5 cm² e ≈ 33 cm/s; capilares ≈ 2.500 cm² e ≈ 0,3 mm/s. "
            "O sangue fica só <b>1 a 3 s</b> no capilar.",
            "Área das veias ≈ 4× a das artérias: explica a grande capacidade de armazenamento venoso.",
        ]),
        ("fig", None, "fig_livro/g14_02.png", "Pressões ao longo das circulações sistêmica e pulmonar (decúbito).", 13),
        ("table", [
            ["Local", "Pressão (mmHg)"],
            ["Aorta", "120/80, média <b>100</b>"],
            ["Capilar sistêmico", "35 → 10, média funcional <b>≈ 17</b> (glomérulo ≈ 60)"],
            ["Átrio direito (fim das cavas)", "<b>≈ 0</b>"],
            ["Artéria pulmonar", "<b>25/8</b>, média <b>16</b>"],
            ["Capilar pulmonar", "<b>≈ 7</b>"],
        ], [6.4, 11.0]),
        ("box", "Os 3 princípios da circulação", [
            "O fluxo de cada tecido é controlado pela <b>necessidade do tecido</b> (arteríolas). O tecido ativo pode pedir 20 a 30× o fluxo; o coração só sobe o DC 4 a 7×.",
            "O <b>débito cardíaco é a soma dos fluxos locais</b>: o que volta, o coração bombeia.",
            "A <b>PA é regulada de forma independente</b> do fluxo local e do DC: reflexos nervosos em segundos; rins em horas e dias.",
        ]),
    ]),
    ("2. Pressão, fluxo e resistência", [
        ("fig", None, "fig_livro/g14_08.png", "Efeito do raio sobre o fluxo (lei da quarta potência).", 8),
        ("ul", [
            "<b>Lei de Ohm: F = ΔP / R</b>. O que move o sangue é a <b>diferença</b> de pressão, não a pressão absoluta.",
            "DC de repouso ≈ <b>5.000 mℓ/min</b> (≈ 100 mℓ/s). Resistência periférica total ≈ 100 mmHg / 100 mℓ/s = <b>1 URP</b> "
            "(vai de 0,2 a 4 URP). Resistência pulmonar ≈ <b>0,14 URP</b> (≈ 1/7 da sistêmica).",
            "<b>Condutância = 1 / R</b>, e é proporcional a <b>r⁴</b>.",
            "<b>Poiseuille: F = π·ΔP·r⁴ / (8·η·ℓ)</b>. O <b>raio</b> é o fator mais importante: raio 2× → fluxo 16×; raio 4× → 256×.",
            "As <b>arteríolas</b> (4 a 25 µm) fazem ≈ <b>2/3 da resistência sistêmica</b> e mudam o diâmetro até 4×: por isso controlam o fluxo local.",
            "<b>Série</b>: R total = R1 + R2 + ... (mesmo fluxo em cada um). <b>Paralelo</b>: 1/R total = 1/R1 + 1/R2 + ...; C total = C1 + C2 + ... "
            "A resistência total em paralelo é <b>menor que a de qualquer ramo</b>. Tirar um rim ou amputar um membro <b>aumenta a RPT</b>.",
        ]),
        ("fig", None, "fig_livro/g14_06.png", "A: dois líquidos lado a lado. B: fluxo laminar (parabólico). C: fluxo turbulento.", 7),
        ("table", [
            ["Conceito", "O que saber"],
            ["<b>Fluxo laminar</b>", "Camadas concêntricas; perfil <b>parabólico</b>: centro rápido, junto à parede quase parado"],
            ["<b>Fluxo turbulento</b>", "Redemoinhos, <b>resistência muito maior</b>; gera sopros e sons de Korotkoff"],
            ["<b>Reynolds: Re = v·d·ρ / η</b>", "↑ com velocidade, diâmetro e densidade; ↓ com viscosidade. <b>200 a 400</b>: turbulência nos ramos; "
             "<b>&gt; 2.000</b>: turbulência até em vaso reto"],
            ["Onde há turbulência normal", "Aorta proximal e artéria pulmonar na ejeção rápida (Re de milhares)"],
        ], [5.0, 12.4]),
        ("h2", "Viscosidade e hematócrito"),
        ("fig", None, "fig_livro/g14_11.png", "Efeito do hematócrito sobre a viscosidade do sangue (água = 1).", 6.5),
        ("ul", [
            "Hematócrito médio: homens <b>42</b>, mulheres <b>38</b>. Os <b>eritrócitos</b> são o principal determinante da viscosidade.",
            "Sangue normal: viscosidade <b>3 a 4×</b> a da água; plasma ≈ 1,5×. <b>Policitemia</b> (Ht 60 a 70): até <b>10×</b>, fluxo muito reduzido.",
        ]),
        ("h2", "Autorregulação, fechamento crítico, Laplace e cisalhamento"),
        ("fig", None, "fig_livro/g14_12.png", "Autorregulação: fluxo quase constante entre 70 e 175 mmHg.", 6.5),
        ("ul", [
            "<b>Autorregulação</b>: entre ≈ <b>70 e 175 mmHg</b>, o tecido ajusta a resistência e mantém o fluxo (cap. 17).",
            "Num vaso passivo, ↑ pressão distende o vaso e ↓ R (fluxo sobe mais que o previsto). Abaixo da <b>pressão crítica de fechamento</b>, o vaso colapsa e o fluxo para.",
            "<b>Lei de Laplace: T = ΔP · r / h</b>. Vasos grandes sob alta pressão (aorta) precisam de parede forte; capilares, de raio mínimo, aguentam pouca tensão.",
            "<b>Tensão de cisalhamento</b>: atrito do fluxo no endotélio; ∝ velocidade × viscosidade, ∝ 1/r³. Sinaliza remodelamento vascular.",
            "Unidades: 1 mmHg = <b>1,36 cmH₂O</b>.",
        ]),
    ]),
    ("3. Distensibilidade e complacência", [
        ("fig", None, "fig_livro/g15_01.png", "Curvas volume-pressão dos sistemas arterial e venoso.", 8),
        ("table", [
            ["", "Fórmula", "Artéria × veia"],
            ["<b>Distensibilidade</b>", "ΔV / (ΔP × V inicial)", "Veias ≈ <b>8×</b> mais distensíveis"],
            ["<b>Complacência (capacitância)</b>", "ΔV / ΔP = distensibilidade × volume", "Veias ≈ <b>24×</b> (8× × 3× o volume)"],
        ], [5.0, 6.4, 6.0]),
        ("ul", [
            "Sistema arterial: <b>700 mℓ → PAM 100 mmHg</b>; com 400 mℓ a pressão cai a zero. Sistema venoso: 2.000 a 3.500 mℓ, e centenas de mℓ mudam a pressão só 3 a 5 mmHg.",
            "Por isso dá para transfundir <b>meio litro</b> em minutos sem grande efeito. As artérias pulmonares são ≈ 6× mais distensíveis que as sistêmicas.",
            "<b>Simpático</b> ↑ a pressão para cada volume: contrai sobretudo as veias e <b>desloca sangue para o coração</b>. Permite circular quase normal com até <b>25%</b> de perda.",
            "<b>Complacência tardia (estresse-relaxamento)</b>: após ↑ súbito de volume, a pressão sobe e depois volta em minutos a horas, porque o músculo liso se alonga. Acomoda transfusão; no sentido inverso, ajusta após hemorragia.",
        ]),
    ]),
    ("4. Pulso arterial e medida da PA", [
        ("fig", None, "fig_livro/g15_03.png", "Pulso de pressão na aorta ascendente.", 7),
        ("box", "Pressão de pulso (PP = PAS − PAD ≈ 40 mmHg)", [
            "<b>PP ≈ volume sistólico / complacência arterial</b>. ↑ VS ou ↓ complacência (artéria rígida) → ↑ PP.",
            "Idoso com <b>arteriosclerose</b>: PP pode <b>dobrar</b> (sistólica alta).",
        ]),
        ("fig", None, "fig_livro/g15_04.png", "Pulsos aórticos anormais.", 8),
        ("table", [
            ["Condição", "Pulso aórtico", "Por quê"],
            ["<b>Arteriosclerose</b>", "PP ↑↑", "Complacência ↓"],
            ["<b>Estenose aórtica</b>", "PP <b>↓</b>, pulso pequeno", "Pouco fluxo pela valva estreita"],
            ["<b>Persistência do canal arterial</b>", "PAD ↓, PP ↑", "≥ 50% do sangue volta pela artéria pulmonar"],
            ["<b>Insuficiência aórtica</b>", "PAD pode ir a ≈ 0, PP ↑↑, <b>sem incisura</b>", "Refluxo para o VE; valva não fecha"],
        ], [4.6, 5.6, 7.2]),
        ("ul", [
            "<b>Transmissão do pulso</b>: 3 a 5 m/s na aorta, 7 a 10 m/s nos grandes ramos, 15 a 35 m/s nas pequenas artérias. Quanto <b>mais complacente, mais lenta</b>. É ≈ 15× a velocidade do sangue.",
            "<b>Amortecimento</b> do pulso (quase some nos capilares) ∝ <b>resistência × complacência</b>.",
        ]),
        ("fig", None, "fig_livro/g15_07.png", "Método auscultatório: sons de Korotkoff.", 7),
        ("ul", [
            "<b>Korotkoff</b>: jato turbulento pela artéria parcialmente ocluída + vibração da parede. <b>1º som = sistólica</b>; "
            "som <b>abafado</b> (ou desaparecimento, preferido por muitos) = <b>diastólica</b>. Erro ≈ 10% vs cateter.",
            "Sons que não somem com manguito vazio: <b>fístula AV</b> de hemodiálise e <b>insuficiência aórtica</b>.",
            "<b>Oscilométrico</b>: a oscilação <b>máxima</b> corresponde à <b>PAM</b>; evita o efeito do jaleco, mas erra com manguito inadequado ou artérias rígidas.",
            "<b>PAM ≈ 60% diastólica + 40% sistólica</b> (fica mais perto da diastólica porque a diástole é mais longa). Em FC muito alta, aproxima-se da média simples. "
            "Na clínica: <b>PAM ≈ PAD + PP/3</b>.",
            "A PA sobe com a idade (rins, após os 50); após os 60, a sistólica e a PP sobem mais (artérias rígidas).",
        ]),
    ]),
    ("5. Veias: pressão venosa, gravidade e reservatório", [
        ("ul", [
            "<b>Pressão venosa central (átrio direito) ≈ 0 mmHg</b>; de −3 a −5 (coração vigoroso, hemorragia) até 20 a 30 (IC grave, transfusão maciça).",
            "PVC é o equilíbrio entre <b>bombeamento do coração direito</b> (bomba forte ↓ PVC) e <b>retorno venoso</b> "
            "(↑ volume, ↑ tônus venoso, dilatação arteriolar ↑ PVC).",
            "Veias periféricas em decúbito: <b>+4 a +6 mmHg</b> acima do AD, por pontos de compressão (1ª costela, pescoço colapsado, abdome).",
            "Pressão intra-abdominal (normal ≈ +6; gravidez, obesidade, ascite +15 a +30) eleva a pressão das veias das pernas ao mesmo nível.",
            "<b>Jugulares</b>: sentado normal, nunca distendidas; começam a distender com PAD ≈ <b>+10</b> e ficam todas cheias com <b>+15 mmHg</b>.",
        ]),
        ("fig", None, "fig_livro/g15_10.png", "Efeito da gravidade sobre as pressões venosas (em pé, imóvel).", 6.5),
        ("ul", [
            "Pressão hidrostática: <b>+1 mmHg a cada 13,6 mm</b> abaixo do coração. Em pé e imóvel: pés <b>+90</b>; mão +35; pescoço 0 (colapsa); "
            "seio sagital <b>−10</b> (risco de <b>embolia gasosa</b> se aberto). Artérias: PAM 100 no coração → ≈ 190 nos pés.",
            "<b>Bomba venosa (muscular)</b> + <b>válvulas</b>: caminhando, pressão nos pés <b>&lt; +20 mmHg</b>. Imóvel, chega a 90 em ≈ 30 s; "
            "perde-se <b>10 a 20% do volume</b> em 15 a 30 min (desmaio do soldado em posição de sentido).",
            "<b>Varizes</b>: distensão crônica → válvulas incompetentes → falha da bomba → edema, úlcera. Tratamento: elevar as pernas, meia de compressão.",
            "<b>Nível de referência</b> das pressões: <b>valva tricúspide</b> (efeito gravitacional ≤ 1 a 2 mmHg); deitado, ≈ 60% da espessura do tórax a partir do dorso.",
            "<b>Reservatórios</b>: veias (&gt; 60% do sangue; circulação quase normal com até 20% de perda), baço (até 100 mℓ; até 50 mℓ de hemácias, Ht +1 a 2%), "
            "fígado (centenas de mℓ), veias abdominais (≈ 300 mℓ), plexo subcutâneo, coração (50 a 100 mℓ) e pulmões (100 a 200 mℓ).",
        ]),
    ]),
]


G = "fig_livro/"
CARDS = [
    ("c", "Volume sanguíneo: veias sistêmicas {{c1::64%}}; artérias {{c2::13%}}; arteríolas + capilares {{c3::7%}}; coração 7%; pulmões 9%.",
     "", G + "g14_01.png"),
    ("c", "Velocidade do sangue: {{c1::v = F / A}}; aorta ≈ {{c2::33 cm/s}}, capilar ≈ {{c3::0,3 mm/s}}."),
    ("c", "O sangue permanece {{c1::1 a 3 s}} no capilar."),
    ("c", "Área de secção: aorta {{c1::2,5 cm²}}; capilares ≈ {{c2::2.500 cm²}}."),
    ("c", "Pressão na aorta: {{c1::120/80}}, média {{c2::100 mmHg}}."),
    ("c", "Pressão capilar sistêmica: {{c1::35}} → {{c2::10}} mmHg; média funcional ≈ {{c3::17 mmHg}}."),
    ("c", "Capilar glomerular: ≈ {{c1::60 mmHg}}."),
    ("c", "Artéria pulmonar: {{c1::25/8}}, média {{c2::16}}; capilar pulmonar ≈ {{c3::7 mmHg}}."),
    ("c", "O tecido ativo pode pedir {{c1::20 a 30×}} o fluxo; o coração só aumenta o DC {{c2::4 a 7×}}."),
    ("c", "Lei de Ohm da circulação: {{c1::F = ΔP / R}}."),
    ("c", "DC de repouso ≈ {{c1::5.000 mℓ/min}}; RPT ≈ {{c2::1 URP}} (faixa {{c3::0,2 a 4}})."),
    ("c", "Resistência pulmonar ≈ {{c1::0,14 URP}}, ≈ {{c2::1/7}} da sistêmica."),
    ("c", "Condutância = {{c1::1 / R}} e é proporcional a {{c2::r⁴}}."),
    ("c", "Poiseuille: {{c1::F = π·ΔP·r⁴ / (8·η·ℓ)}}."),
    ("c", "Raio 2× → fluxo {{c1::16×}}; raio 4× → fluxo {{c2::256×}}.", "", G + "g14_08.png"),
    ("c", "As arteríolas respondem por ≈ {{c1::2/3}} da resistência sistêmica; diâmetro de {{c2::4 a 25 µm}}."),
    ("c", "Em série as {{c1::resistências}} se somam; em paralelo somam-se as {{c2::condutâncias}}."),
    ("c", "Remover um rim ou amputar um membro {{c1::aumenta}} a resistência periférica total."),
    ("c", "Fluxo laminar tem perfil de velocidade {{c1::parabólico}}.", "", "fig_livro/g14_06.png"),
    ("c", "Número de Reynolds: {{c1::Re = v·d·ρ / η}}."),
    ("c", "Re {{c1::200 a 400}}: turbulência nas ramificações; Re > {{c2::2.000}}: turbulência até em vaso reto."),
    ("c", "Turbulência fisiológica ocorre na {{c1::aorta proximal e artéria pulmonar}} durante a ejeção rápida."),
    ("c", "Hematócrito médio: homens {{c1::42}}, mulheres {{c2::38}}."),
    ("c", "Viscosidade: sangue normal {{c1::3 a 4×}} a água; plasma {{c2::1,5×}}; policitemia até {{c3::10×}}.", "", G + "g14_11.png"),
    ("c", "Autorregulação do fluxo: PA entre {{c1::70 e 175 mmHg}}.", "", G + "g14_12.png"),
    ("c", "Abaixo da {{c1::pressão crítica de fechamento}}, o vaso colapsa e o fluxo para."),
    ("c", "Lei de Laplace: {{c1::T = ΔP · r / h}}."),
    ("c", "Tensão de cisalhamento é proporcional a {{c1::velocidade × viscosidade}} e inversa a {{c2::r³}}."),
    ("c", "1 mmHg = {{c1::1,36 cmH₂O}}."),
    ("c", "Distensibilidade = {{c1::ΔV / (ΔP × V)}}; complacência = {{c2::ΔV / ΔP}}."),
    ("c", "Veias são ≈ {{c1::8×}} mais distensíveis e têm complacência ≈ {{c2::24×}} a das artérias."),
    ("c", "Sistema arterial: {{c1::700 mℓ}} → PAM 100 mmHg; com {{c2::400 mℓ}} a pressão cai a zero.", "", G + "g15_01.png"),
    ("c", "Com simpático, a circulação funciona quase normal com perda de até {{c1::25%}} do volume."),
    ("c", "Após ↑ súbito de volume, a pressão volta ao normal em minutos: {{c1::complacência tardia (estresse-relaxamento)}}."),
    ("c", "Pressão de pulso ≈ {{c1::volume sistólico}} / {{c2::complacência arterial}}."),
    ("c", "Na arteriosclerose a pressão de pulso pode {{c1::dobrar}}."),
    ("c", "Estenose aórtica: pressão de pulso {{c1::diminuída}}.", "", G + "g15_04.png"),
    ("c", "Insuficiência aórtica: diastólica pode chegar a {{c1::≈ 0}} e {{c2::não há incisura}}."),
    ("c", "Persistência do canal arterial: ≥ {{c1::50%}} do sangue aórtico volta para a {{c2::artéria pulmonar}}; PP ↑."),
    ("c", "Transmissão do pulso: aorta {{c1::3 a 5 m/s}}; grandes ramos {{c2::7 a 10 m/s}}; pequenas artérias {{c3::15 a 35 m/s}}."),
    ("c", "Quanto mais {{c1::complacente}} o vaso, mais lenta a transmissão do pulso."),
    ("c", "Amortecimento do pulso ∝ {{c1::resistência × complacência}}.", "", G + "g15_06.png"),
    ("c", "Korotkoff: 1º som = {{c1::sistólica}}; abafamento/desaparecimento = {{c2::diastólica}}."),
    ("c", "No método oscilométrico, a oscilação máxima corresponde à {{c1::PAM}}."),
    ("c", "PAM ≈ {{c1::60%}} diastólica + {{c2::40%}} sistólica.", "Clínica: PAD + PP/3"),
    ("c", "Sons de Korotkoff persistem com manguito vazio em {{c1::fístula AV}} e {{c2::insuficiência aórtica}}."),
    ("c", "PVC normal ≈ {{c1::0 mmHg}}; mínimo {{c2::−3 a −5}}; máximo {{c3::20 a 30}} (IC grave)."),
    ("c", "Veias periféricas em decúbito ficam {{c1::+4 a +6 mmHg}} acima do AD por pontos de compressão."),
    ("c", "Jugulares começam a distender com PAD ≈ {{c1::+10}} e ficam todas cheias com {{c2::+15 mmHg}}."),
    ("c", "Pressão hidrostática: +1 mmHg a cada {{c1::13,6 mm}}."),
    ("c", "Em pé imóvel: pés {{c1::+90}}; seio sagital {{c2::−10}}; mão {{c3::+35 mmHg}}.", "", G + "g15_10.png"),
    ("c", "Caminhando, a bomba venosa mantém a pressão nos pés < {{c1::+20 mmHg}}.", "", G + "g15_11.png"),
    ("c", "Imóvel em pé, perde-se {{c1::10 a 20%}} do volume em {{c2::15 a 30 min}}."),
    ("c", "Nível de referência das pressões: {{c1::valva tricúspide}}."),
    ("c", "O baço libera até {{c1::100 mℓ}} de sangue e até {{c2::50 mℓ}} de hemácias (Ht +1 a 2%)."),
    ("b", "Quais as três funções-princípio da circulação?", "Fluxo local segue a <b>necessidade do tecido</b>; <b>DC = soma dos fluxos locais</b>; "
          "<b>PA regulada independentemente</b> (nervoso rápido, rins a longo prazo)."),
    ("b", "Por que o raio é o fator mais importante do fluxo?", "Porque F ∝ <b>r⁴</b> (Poiseuille)."),
    ("b", "Por que a anemia pode causar sopro?", "↓ viscosidade e ↑ velocidade → <b>↑ Reynolds</b> → fluxo turbulento."),
    ("b", "Por que a PAM fica mais perto da diastólica?", "A <b>diástole dura mais</b> que a sístole em FC normal."),
    ("b", "Por que abrir o seio sagital em pé é perigoso?", "Pressão <b>negativa (≈ −10 mmHg)</b> em cavidade rígida: <b>embolia gasosa</b>."),
    ("b", "Por que surgem varizes?", "Veia distende, <b>válvulas não crescem</b> e ficam incompetentes → bomba venosa falha → mais distensão."),
    ("b", "Por que as veias do pescoço têm pressão zero em pé?", "A pressão atmosférica as <b>colapsa</b>; qualquer ↑ abre a veia e o fluxo traz a pressão de volta a 0."),
]

# oclusão sobre figuras do Guyton (coordenadas em pixels da imagem original)
OCC_IMG = [
    (G + "g14_01.png", (386, 290, 426, 312), "Qual % do sangue?", "<b>Coração: 7%</b>."),
    (G + "g14_01.png", (386, 444, 432, 465), "Qual % do sangue?", "<b>Artérias: 13%</b>."),
    (G + "g14_01.png", (386, 538, 426, 560), "Qual % do sangue?", "<b>Arteríolas e capilares: 7%</b>."),
    (G + "g14_01.png", (78, 680, 120, 700), "Qual % do sangue?", "<b>Veias, vênulas e seios venosos: 64%</b>."),
    (G + "g14_01.png", (72, 16, 110, 38), "Qual % do sangue?", "<b>Circulação pulmonar: 9%</b>."),
    (G + "g15_10.png", (352, 18, 445, 40), "Pressão no seio sagital (em pé)?", "<b>−10 mmHg</b>."),
    (G + "g15_10.png", (352, 350, 445, 372), "Pressão nas veias da mão?", "<b>+35 mmHg</b>."),
    (G + "g15_10.png", (352, 650, 445, 672), "Pressão nas veias dos pés (em pé, imóvel)?", "<b>+90 mmHg</b>."),
    (G + "g15_01.png", 'Sistema arterial', 'Qual curva?', '<b>Sistema arterial</b>: pouco complacente.'),
    (G + "g15_01.png", 'Sistema venoso', 'Qual curva?', '<b>Sistema venoso</b>: complacência ≈ 24× a arterial.'),
    (G + "g15_03.png", 'Incisura', 'O que é este evento?', '<b>Incisura</b>: fechamento da valva aórtica.'),
]

TOPIC = dict(
    code="d", slug="d-biofisica-circulacao", title="Biofísica da circulação",
    source="Guyton & Hall, Tratado de Fisiologia Médica, caps. 14 e 15",
    sections=SECTIONS, cards=CARDS, occ_img=OCC_IMG,
)
