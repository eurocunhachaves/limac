"""Tema d: Biofísica da circulação (Guyton & Hall, caps. 14 e 15)."""

SECTIONS = [
    ("1. Visão geral: onde está o sangue e onde está a pressão", [
        ("fig", "fig/d_volumes.png", "fig_livro/g14_01.png", "Distribuição do volume sanguíneo nas partes da circulação.", 8),
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
        ("fig", "fig/d_pressoes.png", "fig_livro/g14_02.png", "Pressões ao longo das circulações sistêmica e pulmonar (decúbito).", 16),
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
        ("fig", "fig/d_poiseuille.png", "fig_livro/g14_08.png", "Efeito do raio sobre o fluxo (lei da quarta potência).", 10),
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
        ("fig", "fig/d_fluxo.png", None, "Fluxo laminar (parabólico) e turbulento.", 10),
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
        ("fig", "fig/d_complacencia.png", "fig_livro/g15_01.png", "Curvas volume-pressão dos sistemas arterial e venoso.", 9),
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
        ("fig", "fig/d_pulso.png", "fig_livro/g15_03.png", "Pulso de pressão na aorta ascendente.", 9),
        ("box", "Pressão de pulso (PP = PAS − PAD ≈ 40 mmHg)", [
            "<b>PP ≈ volume sistólico / complacência arterial</b>. ↑ VS ou ↓ complacência (artéria rígida) → ↑ PP.",
            "Idoso com <b>arteriosclerose</b>: PP pode <b>dobrar</b> (sistólica alta).",
        ]),
        ("fig", None, "fig_livro/g15_04.png", "Pulsos aórticos anormais.", 7),
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
        ("fig", "fig/d_korotkoff.png", "fig_livro/g15_07.png", "Método auscultatório: sons de Korotkoff.", 10),
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
        ("fig", "fig/d_gravidade.png", "fig_livro/g15_10.png", "Efeito da gravidade sobre as pressões venosas (em pé, imóvel).", 7),
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

MCQ = [
    dict(q="Em repouso, onde se encontra a maior parte do volume sanguíneo total?",
         opts=["Nas artérias sistêmicas", "Nos capilares sistêmicos", "Nas veias, vênulas e seios venosos sistêmicos",
               "No coração", "Nos vasos pulmonares"],
         a=2, c="≈ 64% do sangue está nas veias sistêmicas; artérias 13%, arteríolas e capilares 7%, coração 7% e pulmões 9%."),
    dict(q="A velocidade média do sangue é muito menor nos capilares do que na aorta porque:",
         opts=["O fluxo total nos capilares é menor que na aorta", "A área total de secção transversal dos capilares é muito maior",
               "A viscosidade do sangue aumenta nos capilares", "A pressão capilar é negativa", "Os capilares são mais longos que a aorta"],
         a=1, c="v = F/A. O mesmo fluxo passa por todos os segmentos em série; como a área capilar total (≈ 2.500 cm²) é ≈ 1.000× a da aorta "
                "(2,5 cm²), a velocidade cai de ≈ 33 cm/s para ≈ 0,3 mm/s."),
    dict(q="A maior queda de pressão ao longo da circulação sistêmica ocorre:",
         opts=["Na aorta", "Nas grandes artérias", "Nas arteríolas", "Nas vênulas", "Nas veias cavas"],
         a=2, c="As arteríolas respondem por ≈ 2/3 da resistência sistêmica total, e é nelas que a pressão cai mais."),
    dict(q="A pressão média na artéria pulmonar é de aproximadamente:",
         opts=["2 mmHg", "7 mmHg", "16 mmHg", "40 mmHg", "100 mmHg"], keep=True,
         a=2, c="Artéria pulmonar ≈ 25/8 mmHg, média ≈ 16; capilar pulmonar ≈ 7 mmHg."),
    dict(q="Dois pontos de um vaso têm ambos 100 mmHg de pressão. Nessa situação, o fluxo entre eles é:",
         opts=["Máximo, pois a pressão é alta", "Nulo, pois não há diferença de pressão", "Metade do normal",
               "Dependente apenas da viscosidade", "Turbulento"],
         a=1, c="F = ΔP/R. O que move o sangue é a diferença de pressão entre as extremidades, não o valor absoluto."),
    dict(q="O raio de uma arteríola dobra, mantendo-se todos os outros fatores constantes. O fluxo por ela aumenta:",
         opts=["2 vezes", "4 vezes", "8 vezes", "16 vezes", "256 vezes"], keep=True,
         a=3, c="Poiseuille: F ∝ r⁴. 2⁴ = 16. Com raio 4×, o fluxo sobe 256×."),
    dict(q="Na lei de Poiseuille (F = π·ΔP·r⁴ / 8·η·ℓ), o fluxo é inversamente proporcional a:",
         opts=["Raio e diferença de pressão", "Viscosidade e comprimento do vaso", "Raio e comprimento",
               "Diferença de pressão e viscosidade", "Somente o raio"],
         a=1, c="O fluxo sobe com ΔP e r⁴ e cai com a viscosidade (η) e o comprimento (ℓ)."),
    dict(q="O débito cardíaco é de 100 mℓ/s e a diferença de pressão entre artérias e veias sistêmicas é de 100 mmHg. A resistência periférica total é:",
         opts=["0,14 URP", "0,5 URP", "1 URP", "4 URP", "100 URP"], keep=True,
         a=2, c="R = ΔP/F = 100/100 = 1 URP (unidade de resistência periférica). Pode variar de 0,2 (vasodilatação) a 4 URP (constrição)."),
    dict(q="A resistência vascular pulmonar total, comparada à sistêmica, é aproximadamente:",
         opts=["Igual", "O dobro", "Um sétimo", "Dez vezes maior", "Metade"],
         a=2, c="ΔP pulmonar = 16 − 2 = 14 mmHg para o mesmo fluxo (100 mℓ/s): R ≈ 0,14 URP, cerca de 1/7 da sistêmica."),
    dict(q="Sobre vasos dispostos em paralelo, é correto afirmar:",
         opts=["A resistência total é a soma das resistências", "A resistência total é menor que a de qualquer vaso isolado",
               "O fluxo é igual em todos os vasos", "Remover um circuito paralelo reduz a resistência total",
               "A condutância total é o inverso da soma das condutâncias"],
         a=1, c="Em paralelo, 1/Rt = 1/R1 + 1/R2 + ... e as condutâncias se somam; cada via extra facilita o fluxo. Remover um rim "
                "ou amputar um membro tira uma via paralela e aumenta a RPT."),
    dict(q="Qual das condições aumenta a tendência a fluxo turbulento (número de Reynolds)?",
         opts=["Aumento da viscosidade do sangue", "Redução da velocidade do fluxo", "Anemia, com maior velocidade do fluxo",
               "Redução do diâmetro do vaso em vaso liso e reto com fluxo lento", "Policitemia"],
         a=2, c="Re = v·d·ρ/η. Na anemia a viscosidade cai e o débito (velocidade) sobe: ambos aumentam o Reynolds, o que explica sopros funcionais."),
    dict(q="A partir de qual número de Reynolds costuma haver turbulência mesmo em vaso reto e liso?",
         opts=["20", "200", "400", "2.000", "20.000"], keep=True,
         a=3, c="Re de 200 a 400 já causa turbulência em ramificações; acima de ≈ 2.000 há turbulência até em vaso reto e liso."),
    dict(q="O principal determinante da viscosidade do sangue é:",
         opts=["A concentração de albumina", "A concentração de fibrinogênio", "O número de eritrócitos (hematócrito)",
               "A concentração de sódio", "A temperatura corporal"],
         a=2, c="As proteínas plasmáticas têm efeito pequeno. O hematócrito domina: sangue normal 3 a 4× a água; Ht 60 a 70 (policitemia) até 10×."),
    dict(q="A capacidade de um tecido de manter seu fluxo quase constante apesar de variações da pressão arterial ocorre aproximadamente na faixa de:",
         opts=["0 a 50 mmHg", "20 a 70 mmHg", "70 a 175 mmHg", "175 a 250 mmHg", "Em qualquer pressão"],
         a=2, c="Autorregulação do fluxo sanguíneo: entre ≈ 70 e 175 mmHg a resistência se ajusta e o fluxo muda pouco."),
    dict(q="De acordo com a lei de Laplace, a tensão na parede de um vaso é:",
         opts=["Inversamente proporcional ao raio", "Proporcional à pressão transmural vezes o raio, dividido pela espessura da parede",
               "Independente da pressão", "Proporcional à viscosidade", "Maior nos capilares que na aorta"],
         a=1, c="T = ΔP·r/h. A aorta (raio e pressão altos) precisa de parede forte; os capilares têm raio mínimo e tensão baixa."),
    dict(q="Por que a complacência de uma veia sistêmica é cerca de 24 vezes a da artéria correspondente?",
         opts=["Porque a veia tem pressão 24× maior", "Porque é ≈ 8× mais distensível e tem ≈ 3× o volume",
               "Porque tem parede 24× mais espessa", "Porque não tem músculo liso", "Porque tem válvulas"],
         a=1, c="Complacência = distensibilidade × volume. Veia: 8× mais distensível × 3× o volume = 24×."),
    dict(q="Um vaso de 10 mℓ aumenta 1 mℓ quando a pressão sobe 1 mmHg. Sua distensibilidade é:",
         opts=["1% por mmHg", "10% por mmHg", "1 mℓ/mmHg", "0,01 por mmHg", "100% por mmHg"],
         a=1, c="Distensibilidade = ΔV/(ΔP × V) = 1/(1 × 10) = 0,1/mmHg = 10% por mmHg. (1 mℓ/mmHg seria a complacência.)"),
    dict(q="O fenômeno em que a pressão num segmento venoso sobe após injeção de volume e depois cai gradualmente, sem retirada de sangue, chama-se:",
         opts=["Autorregulação", "Complacência tardia (estresse-relaxamento)", "Pressão crítica de fechamento", "Amortecimento", "Efeito Doppler"],
         a=1, c="O músculo liso da parede se alonga progressivamente e sua tensão cai. Isso acomoda volume extra (transfusão) e, no sentido inverso, ajusta após hemorragia."),
    dict(q="Os dois principais determinantes da pressão de pulso são:",
         opts=["Frequência cardíaca e hematócrito", "Volume sistólico e complacência arterial", "Resistência periférica e PVC",
               "Viscosidade e comprimento da aorta", "Pressão capilar e pressão oncótica"],
         a=1, c="PP ≈ volume sistólico / complacência arterial. ↑ VS ou artérias rígidas (↓ complacência) aumentam a PP."),
    dict(q="Qual condição produz pulso aórtico com pressão diastólica muito baixa e ausência da incisura?",
         opts=["Estenose aórtica", "Insuficiência aórtica", "Arteriosclerose", "Hipovolemia leve", "Bloqueio AV de 1º grau"],
         a=1, c="Na insuficiência aórtica o sangue reflui para o VE: a pressão pode cair a ≈ 0 na diástole e não há incisura porque a valva não fecha."),
    dict(q="Na estenose valvar aórtica, o pulso aórtico caracteristicamente apresenta:",
         opts=["Pressão de pulso muito aumentada", "Pressão de pulso diminuída", "Diastólica próxima de zero",
               "Incisura exagerada", "Pressão de pulso normal com FC alta"],
         a=1, c="O fluxo ejetado pela valva estreita é reduzido, então o pulso de pressão aórtica é bem menor."),
    dict(q="A velocidade de transmissão da onda de pulso é mais alta:",
         opts=["Na aorta, por ser mais complacente", "Nas pequenas artérias distais, por serem menos complacentes",
               "Nos capilares", "Nas veias", "É igual em toda a árvore arterial"],
         a=1, c="Quanto maior a complacência, mais lenta a transmissão: aorta 3 a 5 m/s, grandes ramos 7 a 10, pequenas artérias 15 a 35 m/s."),
    dict(q="No método auscultatório, a pressão sistólica corresponde ao momento em que:",
         opts=["Os sons de Korotkoff desaparecem", "Os sons ficam abafados", "Surge o primeiro som de Korotkoff",
               "O manguito é inflado até 200 mmHg", "A oscilação do manguito é máxima"],
         a=2, c="O 1º som aparece quando a pressão do manguito cai logo abaixo da sistólica e passa um jato no pico da sístole. "
                "Abafamento/desaparecimento = diastólica. Oscilação máxima (oscilométrico) = PAM."),
    dict(q="A pressão arterial média fica mais próxima da diastólica do que da sistólica porque:",
         opts=["A sístole dura mais que a diástole", "A diástole ocupa a maior parte do ciclo em FC normais",
               "A pressão diastólica é medida no pé", "Os barorreceptores só leem a diastólica", "A complacência é zero na diástole"],
         a=1, c="PAM ≈ 60% PAD + 40% PAS. Em FC muito altas a diástole encurta e a PAM se aproxima da média aritmética."),
    dict(q="A pressão atrial direita (pressão venosa central) normal é de aproximadamente:",
         opts=["−10 mmHg", "0 mmHg", "+10 mmHg", "+25 mmHg", "+90 mmHg"], keep=True,
         a=1, c="≈ 0 mmHg (atmosférica); pode ir a −3 a −5 (coração vigoroso, hemorragia) ou 20 a 30 mmHg (IC grave, transfusão maciça)."),
    dict(q="Um adulto em pé, absolutamente imóvel, tem pressão nas veias dos pés de cerca de:",
         opts=["0 mmHg", "+20 mmHg", "+35 mmHg", "+90 mmHg", "+190 mmHg"], keep=True,
         a=3, c="Pelo peso da coluna de sangue (+1 mmHg a cada 13,6 mm), ≈ +90 mmHg. Caminhando, a bomba venosa mantém &lt; +20 mmHg. "
                "190 mmHg é a pressão arterial nos pés."),
    dict(q="Durante uma neurocirurgia com o paciente sentado, o seio sagital é aberto. O principal risco imediato é:",
         opts=["Hemorragia arterial", "Embolia gasosa, porque a pressão no seio é negativa", "Hipertensão intracraniana",
               "Trombose venosa profunda", "Hipercalemia"],
         a=1, c="As veias intracranianas estão numa cavidade rígida e não colapsam; em pé/sentado a pressão no seio sagital é ≈ −10 mmHg, e o ar pode ser aspirado."),
    dict(q="O nível de referência para a medida das pressões circulatórias, onde a gravidade altera pouco a pressão, localiza-se:",
         opts=["No arco aórtico", "Na valva tricúspide", "No 4º espaço intercostal esquerdo", "Na veia femoral", "No seio carotídeo"],
         a=1, c="O próprio coração regula por retroalimentação a pressão na valva tricúspide; ali a gravidade muda a pressão só 1 a 2 mmHg."),
]

OPEN = [
    dict(q="Homem de 74 anos, hipertenso, tem PA de 172/78 mmHg em várias medidas. O ecocardiograma é normal e a frequência cardíaca é 70 bpm. "
           "(a) Calcule a pressão de pulso e a PAM aproximada (use a regra do Guyton). (b) Explique, com base na fisiologia, por que a "
           "sistólica sobe e a diastólica não. (c) Por que a PAM fica mais próxima da diastólica? (d) Cite outra condição que aumenta a pressão de "
           "pulso por mecanismo diferente.",
         a=["(a) PP = 172 − 78 = <b>94 mmHg</b> (normal ≈ 40). PAM ≈ 0,6 × 78 + 0,4 × 172 ≈ 47 + 69 = <b>≈ 116 mmHg</b> (pela regra clínica PAD + PP/3 ≈ 109).",
            "(b) <b>PP ≈ volume sistólico / complacência arterial</b>. Com a idade e a arteriosclerose, as artérias ficam <b>rígidas (↓ complacência)</b>: o mesmo "
            "volume sistólico eleva muito mais a pressão na sístole, e sem o \"efeito reservatório\" elástico a pressão cai mais na diástole.",
            "(c) Porque, em FC normais, a <b>diástole ocupa a maior parte do ciclo</b>: a PAM é ≈ 60% determinada pela diastólica e 40% pela sistólica.",
            "(d) <b>Insuficiência aórtica</b> (refluxo para o VE, PAD cai muito, VS grande) ou <b>persistência do canal arterial</b> (escape para a artéria "
            "pulmonar). Também ↑ VS (exercício, hipertireoidismo)."]),
    dict(q="Mulher de 28 anos com anemia grave (hemoglobina 6 g/dℓ) apresenta sopro sistólico suave, sem doença valvar. Após tratamento, o sopro desaparece. "
           "(a) Como a anemia altera a viscosidade do sangue e a resistência vascular? (b) Explique o sopro usando o número de Reynolds. "
           "(c) Na situação oposta, a policitemia (Ht 65%), o que acontece com o fluxo? (d) Quanto mudaria o fluxo numa arteríola que reduzisse o raio à metade?",
         a=["(a) Hematócrito baixo → <b>viscosidade ↓</b> (sangue normal 3 a 4× a água). Pela lei de Poiseuille, R ∝ η: a resistência cai e o fluxo "
            "(e o débito cardíaco) sobe.",
            "(b) <b>Re = v·d·ρ / η</b>. Com ↓ viscosidade e ↑ velocidade (débito alto), o Re sobe e passa do limite em que o fluxo vira "
            "<b>turbulento</b> na aorta e na artéria pulmonar. A turbulência gera vibração audível: o sopro funcional (\"inocente\").",
            "(c) Viscosidade pode chegar a <b>≈ 10× a da água</b>: resistência ↑ e fluxo muito ↓ (risco de estase e trombose).",
            "(d) F ∝ r⁴: (1/2)⁴ = <b>1/16</b> do fluxo, ou seja, queda de ≈ 94% com a mesma ΔP."]),
    dict(q="Soldado de 20 anos desmaia após 25 minutos parado em posição de sentido num dia quente. Sua mãe, de 55 anos, que trabalha em pé há "
           "décadas, tem varizes e edema nas pernas ao fim do dia. (a) Qual a pressão venosa nos pés de uma pessoa em pé imóvel e ao caminhar? "
           "(b) Explique por que o soldado desmaiou. (c) Explique a formação das varizes. (d) Que medidas simples previnem os dois problemas?",
         a=["(a) Imóvel: ≈ <b>+90 mmHg</b> (peso da coluna de sangue do coração aos pés, +1 mmHg a cada 13,6 mm). Caminhando: <b>&lt; +20 mmHg</b>, pela "
            "<b>bomba venosa (muscular)</b> com as válvulas.",
            "(b) Sem contração muscular, a pressão venosa das pernas chega a 90 mmHg em ≈ 30 s; a pressão capilar sobe, o líquido sai para o interstício "
            "e o sangue se acumula nas veias. Perde-se <b>10 a 20% do volume circulante</b> em 15 a 30 min → ↓ retorno venoso → ↓ DC → ↓ fluxo cerebral → síncope.",
            "(c) A distensão crônica das veias (ficar em pé, gravidez) aumenta o diâmetro, mas os folhetos das <b>válvulas não crescem</b>: elas deixam de fechar. "
            "A bomba falha, a pressão sobe mais e as veias dilatam ainda mais (ciclo vicioso). Resultado: <b>varizes</b>, edema, dor e até úlcera.",
            "(d) Contrair periodicamente os músculos das pernas e flexionar os joelhos (soldado); <b>elevar as pernas</b> acima do coração e usar "
            "<b>meias de compressão</b> (varizes)."]),
]

OPEN_EXTRA = [
    ("Enuncie a lei de Poiseuille e explique por que as arteríolas são os principais vasos de controle do fluxo.",
     "F = π·ΔP·r⁴ / (8·η·ℓ). O fluxo depende da quarta potência do raio. As arteríolas concentram ≈ 2/3 da resistência sistêmica e têm "
     "parede muscular forte, que muda o diâmetro até 4×: isso muda o fluxo até 256×, permitindo desde quase fechar até aumentar muito o fluxo de cada tecido."),
    ("Diferencie distensibilidade de complacência e compare artérias e veias.",
     "Distensibilidade = ΔV/(ΔP × V): aumento fracional de volume por mmHg. Complacência = ΔV/ΔP = distensibilidade × volume: volume "
     "armazenado por mmHg. Veias são ≈ 8× mais distensíveis e têm ≈ 3× o volume das artérias: complacência ≈ 24×. Por isso são o reservatório de sangue."),
    ("Explique o método auscultatório de medida da PA e a origem dos sons de Korotkoff.",
     "Infla-se o manguito acima da sistólica (artéria fechada, sem som) e desinfla-se devagar. Quando a pressão do manguito fica abaixo da sistólica, passa "
     "um jato no pico de cada sístole: 1º som = sistólica. Os sons mudam e ficam abafados perto da diastólica; quando a artéria não fecha mais, somem "
     "(diastólica). Os sons vêm do jato turbulento pela artéria parcialmente ocluída e da vibração da parede."),
    ("Por que o fluxo sanguíneo nos capilares é contínuo, e não pulsátil?",
     "Porque a árvore arterial amortece o pulso. A complacência arterial armazena parte do volume ejetado na sístole e o libera na diástole, e a "
     "resistência dificulta o avanço da onda. O amortecimento é proporcional ao produto resistência × complacência."),
    ("Quais fatores determinam a pressão atrial direita (PVC) e quais a elevam?",
     "Equilíbrio entre a capacidade do coração direito de bombear e a tendência do sangue de voltar das veias periféricas. Bomba fraca eleva a PVC; "
     "bomba forte a reduz. Elevam a PVC também: ↑ volume sanguíneo, ↑ tônus dos grandes vasos (↑ pressões venosas periféricas) e dilatação arteriolar "
     "(passa mais sangue rápido para as veias). Normal ≈ 0; até 20 a 30 mmHg na IC grave ou transfusão maciça."),
    ("Qual o papel das veias e do simpático na hemorragia?",
     "As veias contêm &gt; 60% do sangue e são muito complacentes. Na hemorragia, barorreceptores disparam e o simpático contrai as veias (e reservatórios "
     "como baço, fígado, veias abdominais e plexo cutâneo), deslocando sangue para o coração. A circulação funciona quase normal com perdas de até 20 a 25%. "
     "Depois, a complacência tardia reversa ajusta o leito ao volume menor."),
]

G = "fig_livro/"
CARDS = [
    ("c", "Volume sanguíneo: veias sistêmicas {{c1::64%}}; artérias {{c2::13%}}; arteríolas + capilares {{c3::7%}}; coração 7%; pulmões 9%.",
     "", G + "g14_01.png"),
    ("c", "Velocidade do sangue: {{c1::v = F / A}}; aorta ≈ {{c2::33 cm/s}}, capilar ≈ {{c3::0,3 mm/s}}."),
    ("c", "O sangue permanece {{c1::1 a 3 s}} no capilar."),
    ("c", "Área de secção: aorta {{c1::2,5 cm²}}; capilares ≈ {{c2::2.500 cm²}}."),
    ("c", "Pressão na aorta: {{c1::120/80}}, média {{c2::100 mmHg}}.", "", "fig/d_pressoes.png"),
    ("c", "Pressão capilar sistêmica: {{c1::35}} → {{c2::10}} mmHg; média funcional ≈ {{c3::17 mmHg}}."),
    ("c", "Capilar glomerular: ≈ {{c1::60 mmHg}}."),
    ("c", "Artéria pulmonar: {{c1::25/8}}, média {{c2::16}}; capilar pulmonar ≈ {{c3::7 mmHg}}."),
    ("c", "O tecido ativo pode pedir {{c1::20 a 30×}} o fluxo; o coração só aumenta o DC {{c2::4 a 7×}}."),
    ("c", "Lei de Ohm da circulação: {{c1::F = ΔP / R}}."),
    ("c", "DC de repouso ≈ {{c1::5.000 mℓ/min}}; RPT ≈ {{c2::1 URP}} (faixa {{c3::0,2 a 4}})."),
    ("c", "Resistência pulmonar ≈ {{c1::0,14 URP}}, ≈ {{c2::1/7}} da sistêmica."),
    ("c", "Condutância = {{c1::1 / R}} e é proporcional a {{c2::r⁴}}."),
    ("c", "Poiseuille: {{c1::F = π·ΔP·r⁴ / (8·η·ℓ)}}.", "", "fig/d_poiseuille.png"),
    ("c", "Raio 2× → fluxo {{c1::16×}}; raio 4× → fluxo {{c2::256×}}.", "", G + "g14_08.png"),
    ("c", "As arteríolas respondem por ≈ {{c1::2/3}} da resistência sistêmica; diâmetro de {{c2::4 a 25 µm}}."),
    ("c", "Em série as {{c1::resistências}} se somam; em paralelo somam-se as {{c2::condutâncias}}."),
    ("c", "Remover um rim ou amputar um membro {{c1::aumenta}} a resistência periférica total."),
    ("c", "Fluxo laminar tem perfil de velocidade {{c1::parabólico}}.", "", "fig/d_fluxo.png"),
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
    ("c", "Veias são ≈ {{c1::8×}} mais distensíveis e têm complacência ≈ {{c2::24×}} a das artérias.", "", "fig/d_complacencia.png"),
    ("c", "Sistema arterial: {{c1::700 mℓ}} → PAM 100 mmHg; com {{c2::400 mℓ}} a pressão cai a zero.", "", G + "g15_01.png"),
    ("c", "Com simpático, a circulação funciona quase normal com perda de até {{c1::25%}} do volume."),
    ("c", "Após ↑ súbito de volume, a pressão volta ao normal em minutos: {{c1::complacência tardia (estresse-relaxamento)}}."),
    ("c", "Pressão de pulso ≈ {{c1::volume sistólico}} / {{c2::complacência arterial}}.", "", "fig/d_pulso.png"),
    ("c", "Na arteriosclerose a pressão de pulso pode {{c1::dobrar}}."),
    ("c", "Estenose aórtica: pressão de pulso {{c1::diminuída}}.", "", G + "g15_04.png"),
    ("c", "Insuficiência aórtica: diastólica pode chegar a {{c1::≈ 0}} e {{c2::não há incisura}}."),
    ("c", "Persistência do canal arterial: ≥ {{c1::50%}} do sangue aórtico volta para a {{c2::artéria pulmonar}}; PP ↑."),
    ("c", "Transmissão do pulso: aorta {{c1::3 a 5 m/s}}; grandes ramos {{c2::7 a 10 m/s}}; pequenas artérias {{c3::15 a 35 m/s}}."),
    ("c", "Quanto mais {{c1::complacente}} o vaso, mais lenta a transmissão do pulso."),
    ("c", "Amortecimento do pulso ∝ {{c1::resistência × complacência}}.", "", G + "g15_06.png"),
    ("c", "Korotkoff: 1º som = {{c1::sistólica}}; abafamento/desaparecimento = {{c2::diastólica}}.", "", "fig/d_korotkoff.png"),
    ("c", "No método oscilométrico, a oscilação máxima corresponde à {{c1::PAM}}."),
    ("c", "PAM ≈ {{c1::60%}} diastólica + {{c2::40%}} sistólica.", "Clínica: PAD + PP/3"),
    ("c", "Sons de Korotkoff persistem com manguito vazio em {{c1::fístula AV}} e {{c2::insuficiência aórtica}}."),
    ("c", "PVC normal ≈ {{c1::0 mmHg}}; mínimo {{c2::−3 a −5}}; máximo {{c3::20 a 30}} (IC grave)."),
    ("c", "Veias periféricas em decúbito ficam {{c1::+4 a +6 mmHg}} acima do AD por pontos de compressão."),
    ("c", "Jugulares começam a distender com PAD ≈ {{c1::+10}} e ficam todas cheias com {{c2::+15 mmHg}}."),
    ("c", "Pressão hidrostática: +1 mmHg a cada {{c1::13,6 mm}}.", "", "fig/d_gravidade.png"),
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
]

TOPIC = dict(
    code="d", slug="d-biofisica-circulacao", title="Biofísica da circulação",
    source="Guyton & Hall, Tratado de Fisiologia Médica, caps. 14 e 15",
    sections=SECTIONS, mcq=MCQ, open=OPEN, open_extra=OPEN_EXTRA, cards=CARDS, occ="dia_d", occ_img=OCC_IMG,
)
