CODIGO = "g"
SLUG = "g-debito-cardiaco-e-retorno-venoso"
TITULO = "Débito cardíaco e retorno venoso"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 20 (PDF p. 770–813)",
]

ESSENCIAL = [
    "**Débito cardíaco (DC)** em repouso ≈ **5 L/min** (homem jovem 5,6; mulher 4,9). **Índice cardíaco** ≈ **3 L/min/m²** (superfície ≈ 1,7 m²).",
    "Normalmente quem controla o DC é o **retorno venoso**, ou seja, a **soma dos fluxos locais** dos tecidos. O coração bombeia o que chega pelo **Frank-Starling**.",
    "Com PA constante, o DC varia **inversamente** à **resistência periférica total** (DC = PA ÷ RPT).",
    "O coração normal bombeia até ≈ **13 L/min** (platô, 2,5 × o normal); com simpático máximo ≈ **25 L/min**; atleta treinado **30–40 L/min**.",
    "**Retorno venoso = (PES − PAD) ÷ RRV.** Normal: 5 = (7 − 0) ÷ 1,4. **PES ≈ 7 mmHg**; o RV cai a zero quando a PAD sobe até a PES.",
    "**Ponto de equilíbrio:** onde a curva de DC cruza a de RV (normal: DC 5 L/min, PAD 0 mmHg).",
    "**DC alto** = queda crônica da RPT (beribéri, fístula AV, hipertireoidismo, anemia). **DC baixo** = coração fraco ou **retorno venoso baixo** (hemorragia, dilatação venosa).",
    "**Fick:** DC = consumo de O₂ ÷ (O₂ arterial − O₂ venoso) = 200 ÷ (200 − 160) × 1 L = **5 L/min**.",
]

CORPO = r'''
= Valores normais

O *débito cardíaco (DC)* é o volume que o coração bombeia para a aorta por minuto; o *retorno venoso (RV)* é o volume que chega ao átrio direito por minuto. Os dois são *iguais*, exceto por alguns batimentos.

- *Repouso:* ≈ *5,6 L/min* no homem jovem e ≈ *4,9 L/min* na mulher; ≈ *5 L/min* no adulto em geral.
- *Índice cardíaco:* DC por m² de superfície corporal. Um adulto de 70 kg tem ≈ 1,7 m², então o normal é ≈ *3 L/min/m²*. É maior que 4 aos 10 anos e cai para ≈ 2,4 aos 80 anos, pela menor atividade e massa muscular.
- O DC aumenta com o *metabolismo*, o *exercício* e o *tamanho* do corpo.

= O retorno venoso controla o DC

Na maioria das situações, quem determina o DC são os fatores *periféricos* que controlam o retorno venoso, e não o coração:

- *Frank-Starling:* o sangue extra que chega estira as câmaras e o coração se contrai com mais força, ejetando o excesso.
- O estiramento do *nó sinusal* aumenta a FC em 10–15%, e o *reflexo de Bainbridge* aumenta ainda mais.

O retorno venoso é a *soma dos fluxos locais* de todos os tecidos (#vf("g20_02")). Como cada tecido ajusta o próprio fluxo ao seu *metabolismo*, o DC é, no fim, a soma de todas as regulações locais. No exercício, DC e consumo de O₂ sobem em paralelo.

#fig("g20_02", largura: 7.5cm, [O débito cardíaco é igual ao retorno venoso e à soma dos fluxos dos órgãos.])

#essencial(titulo: "DC e resistência periférica")[
  *DC = PA ÷ resistência periférica total (RPT).* Com a pressão arterial constante, o DC de longo prazo varia na *direção oposta* à RPT: RPT menor, DC maior.
]

= Limites do coração

A *curva de débito cardíaco* relaciona o DC com a pressão do átrio direito (#vf("g20_05")). O coração normal, sem estímulo especial, chega a um platô de ≈ *13 L/min*: só acima de 2,5 vezes o normal ele passa a *limitar* o DC.

#fig("g20_05", largura: 6.5cm, [Curvas de débito cardíaco do coração normal, hiperfuncionante e hipofuncionante.])

- *Hiperfunção por estímulo nervoso:* simpático com inibição vagal sobe a FC de 72 para 180–200 bpm e *dobra* a contratilidade. O platô chega a ≈ *25 L/min*.
- *Hiperfunção por hipertrofia:* o coração do maratonista tem 50–75% mais massa e platô 60–100% maior. Com o simpático, chega a *30–40 L/min*.
- *Hipofunção:* hipertensão grave (mais pós-carga), inibição nervosa, arritmias, infarto, valvopatias, cardiopatia congênita, miocardite e hipóxia cardíaca.

== Papel do sistema nervoso

Quando os tecidos dilatam seus vasos, o RV sobe, mas a PA tenderia a cair. Os reflexos simpáticos *mantêm a PA*, e só assim o DC aumenta muito. Num cão com metabolismo 4 vezes maior (dinitrofenol), o DC quadruplicou com controle nervoso; sem ele, a PA caiu à metade e o DC subiu só 1,6 vez. No exercício, o simpático eleva a PA acima do normal e aumenta o DC em mais 30–100%.

= DC alto e DC baixo

As causas de DC anormal estão na #vf("t-dc").

#tabela(rotulo: "t-dc", titulo: [Causas de débito cardíaco alto e baixo (Guyton, Fig. 20.7).], (auto, 1fr), ([Situação], [Causas e mecanismo]),
  [*DC alto*], [Sempre por *queda crônica da RPT*, nunca por excitação do coração: *beribéri* (falta de tiamina, RPT cai à metade, DC dobra), *fístula arteriovenosa*, *hipertireoidismo* (DC +40–80%) e *anemia* (menos viscosidade e hipóxia tecidual).],
  [*DC baixo cardíaco*], [Infarto, valvopatia grave, miocardite, *tamponamento*, distúrbios metabólicos do coração. Se o DC não nutre os tecidos: *choque cardiogênico*.],
  [*DC baixo periférico*], [Queda do *retorno venoso*: *hemorragia* (a causa mais comum), *dilatação venosa aguda* (desmaio, perda do simpático), obstrução de grandes veias, menor massa muscular e menor metabolismo (repouso no leito, hipotireoidismo).],
)

= Curvas de DC e pressão externa

A pressão em volta do coração é a *pressão intrapleural*, normal ≈ *−4 mmHg*. Se ela sobe, o átrio direito precisa de mais pressão para encher, e toda a curva de DC se desloca para a *direita*:

- Intrapleural de −2 mmHg desloca a curva 2 mmHg; de +2 mmHg, 6 mmHg.
- *Respiração com pressão positiva* e *tórax aberto* (intrapleural 0, desvio de 4 mmHg) deslocam para a direita; respiração contra pressão negativa, para a esquerda.
- *Tamponamento cardíaco* desloca mais a parte alta da curva, porque a pressão do pericárdio cresce com o enchimento.

= Curva de retorno venoso

Três fatores determinam o retorno venoso:

- a *pressão do átrio direito*, que empurra o sangue para trás;
- o *grau de enchimento* da circulação, medido pela *pressão média de enchimento sistêmico (PES)*;
- a *resistência ao retorno venoso*.

Na curva normal (#vf("g20_10")), o RV cai a *zero* quando a pressão do átrio direito sobe a ≈ *+7 mmHg*, que é a PES. Abaixo de ≈ −2 mmHg há um *platô*: as grandes veias que entram no tórax *colapsam*, e pressões ainda mais negativas não aumentam o retorno.

#fig("g20_10", [Curva normal de retorno venoso: platô por colapso das veias, transição e declive até a pressão média de enchimento sistêmico.])

== Pressão média de enchimento

Se o coração para, as pressões se igualam em toda a circulação: é a *pressão média de enchimento circulatório*, ≈ *7 mmHg*. A PES (só da circulação sistêmica) tem praticamente o mesmo valor.

- Com ≈ 4.000 mL de sangue a pressão de enchimento é ≈ 0; com 5.000 mL é 7 mmHg. Mais *volume* aumenta a PES.
- *Simpático máximo* contrai os vasos e dobra a PES para ≈ *14 mmHg*; a *inibição simpática* a reduz para ≈ *4 mmHg*.

Quanto maior a PES, mais a curva de RV sobe e se desloca para a *direita* (#vf("g20_12")). A diferença *PES − PAD* é o *gradiente de pressão para o retorno venoso*.

#fig("g20_12", [Curvas de retorno venoso com PES normal (7 mmHg), aumentada (14) e diminuída (3,5).])

== Resistência ao retorno venoso

≈ *2/3* da resistência ao retorno venoso estão nas *veias* e ≈ 1/3 nas arteríolas e pequenas artérias. As veias pesam mais porque são muito distensíveis: o sangue represado nelas quase não sobe a pressão. Já nas artérias (capacitância 1/30 das veias) um pequeno acúmulo sobe muito a pressão e vence a resistência.

#essencial(titulo: "Equação do retorno venoso")[
  *RV = (PES − PAD) ÷ RRV.* No adulto: RV = 5 L/min, PES = 7 mmHg, PAD = 0 e RRV = 1,4 mmHg por L/min.
]

Resistência pela metade *dobra a inclinação* da curva; resistência dobrada a reduz à metade (#vf("g20_13")). Em todas as curvas o RV é zero quando a PAD iguala a PES: por mais que o coração falhe, a *PAD nunca passa da PES*.

#fig("g20_13", largura: 6.5cm, [Curvas de retorno venoso com resistência normal, metade e dobro, todas com PES de 7 mmHg.])

= Ponto de equilíbrio

O coração e a circulação sistêmica funcionam juntos: o RV tem de ser igual ao DC, e a PAD é a mesma para os dois. Por isso o DC real é o *cruzamento* da curva de DC com a curva de RV (#vf("g20_15")). No normal (ponto A): *DC 5 L/min e PAD 0 mmHg*.

#fig("g20_15", [Equilíbrio entre a curva de débito cardíaco (vermelha) e a de retorno venoso (azul). Transfusão de 20% do volume leva de A para B.])

- *Transfusão de 20% do volume:* a PES sobe a 16 mmHg e a resistência ao RV cai. O DC sobe *2,5 a 3 vezes* e a PAD vai a ≈ +8 mmHg (ponto B). Em *10–40 min* volta ao normal: líquido sai pelos capilares, as veias se distendem (estresse-relaxamento) e a autorregulação aumenta a resistência.
- *Simpático máximo:* coração ≈ 100% mais eficaz e PES a 17 mmHg. O DC ≈ *dobra* e a PAD quase não muda (#vf("g20_16")).
- *Inibição simpática* (raquianestesia total): PES cai a ≈ 4 mmHg e o coração a ≈ 80%. O DC cai ≈ 40% (fica em ≈ 60% do normal).

#fig("g20_16", largura: 7cm, [Efeito da estimulação simpática moderada (C), máxima (D) e da raquianestesia (B) sobre o ponto de equilíbrio.])

*Fístula AV grande:* de imediato a resistência ao RV despenca e o DC vai de 5 a *13 L/min* (PAD +3). Em 1 min o simpático restaura a PA e sobe a PES de 7 para 9 mmHg: DC ≈ 16 L/min. Em semanas, a retenção de sal e água leva a PES a 12 mmHg e o coração hipertrofia: DC ≈ *20 L/min*, PAD ≈ 6 mmHg.

= Medida do débito cardíaco

*Princípio de Fick:* o sangue que passa pelos pulmões capta O₂. Se o corpo consome 200 mL de O₂ por minuto e cada litro de sangue ganha 40 mL (de 160 mL/L no sangue venoso misto para 200 mL/L no arterial), passam 200 ÷ 40 = *5 L/min* (#vf("g20_19")).

#fig("g20_19", largura: 7.5cm, [Princípio de Fick para medir o débito cardíaco.])

#essencial(titulo: "Equação de Fick")[
  *DC (L/min) = O₂ absorvido nos pulmões (mL/min) ÷ diferença arteriovenosa de O₂ (mL/L de sangue).* O sangue venoso misto vem do *ventrículo direito ou da artéria pulmonar* (por cateter).
]

- *Diluição do indicador:* injeta-se um corante (ou soro frio, na *termodiluição*) no átrio direito e mede-se a concentração numa artéria. *DC = quantidade injetada ÷ (concentração média × duração da curva)*. A recirculação é corrigida extrapolando a curva. Ex.: 5 mg, média 0,25 mg/dL por 12 s → 2 L em 12 s = 10 L/min.
- *Ecocardiografia:* volume sistólico pela velocidade do sangue na aorta × área da aorta; DC = VS × FC.
- *Bioimpedância torácica:* não invasiva, mas com erro de 20–40%.
'''

VALORES = [
    ("DC em repouso", "≈ 5 L/min", "Homem 5,6; mulher 4,9"),
    ("Índice cardíaco", "≈ 3 L/min/m²", ">4 aos 10 anos; 2,4 aos 80"),
    ("Superfície corporal (70 kg)", "≈ 1,7 m²", ""),
    ("Platô da curva de DC normal", "≈ 13 L/min", "2,5 × o normal"),
    ("Platô com simpático máximo", "≈ 25 L/min", "FC até 180–200 bpm"),
    ("Atleta treinado", "30–40 L/min", "Coração 50–75% maior"),
    ("Exercício (PA mantida)", "DC + 30–100%", "Pelo simpático"),
    ("Pressão intrapleural", "≈ −4 mmHg", "Tórax aberto: 0"),
    ("PES / pressão de enchimento circulatório", "≈ 7 mmHg", "Simpático máx. 14; inibição 4"),
    ("Volume com enchimento zero", "≈ 4.000 mL", "5.000 mL → 7 mmHg"),
    ("RV zero quando PAD =", "PES (≈ +7 mmHg)", ""),
    ("Platô do retorno venoso", "PAD ≈ −2 mmHg", "Colapso das veias"),
    ("Resistência ao RV (RRV)", "≈ 1,4 mmHg/(L/min)", "2/3 nas veias"),
    ("Capacitância arterial", "1/30 da venosa", ""),
    ("Ponto de equilíbrio normal", "DC 5 L/min, PAD 0", ""),
    ("Transfusão de 20%", "DC 2,5–3 ×", "Normaliza em 10–40 min"),
    ("Simpático máximo", "DC ≈ 2 ×", "PES 17 mmHg"),
    ("Raquianestesia total", "DC ≈ 60% do normal", "PES ≈ 4 mmHg"),
    ("Fístula AV grande", "5 → 13 → 16 → 20 L/min", "Imediato, 1 min, semanas"),
    ("Hipertireoidismo", "DC + 40–80%", ""),
    ("Fick (exemplo)", "200 ÷ (200 − 160) = 5 L/min", "mL O₂/min ÷ mL O₂/L"),
]

CLINICA = [
    ("Choque hipovolêmico", "A hemorragia reduz o enchimento (PES) e o **retorno venoso**; o DC cai mesmo com coração normal. Repor volume restaura a PES."),
    ("Síncope", "A perda súbita do simpático dilata as veias, a PES cai e o **retorno venoso** desaba: o DC e a PA caem."),
    ("Tamponamento cardíaco", "Líquido no pericárdio aumenta a pressão externa e desloca a curva de DC para a direita: **PVC alta com DC baixo**."),
    ("Ventilação com pressão positiva", "Aumenta a pressão intrapleural, desloca a curva de DC para a direita e pode **reduzir o DC** em pacientes com pouco volume."),
    ("Estados de alto débito", "**Beribéri, fístula AV, hipertireoidismo, anemia**: a RPT baixa aumenta o retorno venoso e o DC; podem levar à insuficiência cardíaca de alto débito."),
    ("Medida na UTI", "O cateter de artéria pulmonar mede o DC por **termodiluição**; a gasometria venosa mista permite o cálculo por **Fick**."),
]

PEGADINHAS = [
    "Na maioria das situações, quem determina o DC é a **periferia** (retorno venoso), não o coração.",
    "**DC alto** crônico vem sempre de **RPT baixa**, nunca de um coração \"excitado demais\".",
    "A **PAD nunca passa da PES**: com PAD = PES, o retorno venoso é zero.",
    "Pressão atrial direita muito negativa **não** aumenta o retorno venoso: as veias do tórax **colapsam** (platô).",
    "A resistência ao retorno venoso está **2/3 nas veias**, não nas arteríolas.",
    "Aumento da pressão intrapleural desloca a curva de DC para a **direita**, sem mudar o platô.",
    "Simpático **dobra** o DC quase sem mudar a PAD, porque desloca as duas curvas ao mesmo tempo.",
    "No Fick, o sangue venoso misto vem da **artéria pulmonar** (ou VD), não de uma veia periférica.",
]

GLOSSARIO = [
    ("Débito cardíaco", "Volume bombeado pelo coração por minuto."),
    ("Retorno venoso", "Volume que chega ao átrio direito por minuto."),
    ("Índice cardíaco", "DC por m² de superfície corporal."),
    ("Curva de débito cardíaco", "DC em função da pressão do átrio direito."),
    ("Curva de retorno venoso", "RV em função da pressão do átrio direito."),
    ("PES", "Pressão média de enchimento sistêmico (≈ 7 mmHg)."),
    ("Gradiente para o retorno venoso", "PES menos pressão do átrio direito."),
    ("RRV", "Resistência ao retorno venoso."),
    ("Ponto de equilíbrio", "Cruzamento das curvas de DC e de RV."),
    ("Tamponamento", "Líquido no pericárdio que comprime o coração."),
    ("Princípio de Fick", "DC = consumo de O₂ ÷ diferença arteriovenosa de O₂."),
    ("Termodiluição", "Diluição do indicador usando soro frio."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 20 · PDF p. 770–777", "Valores normais, índice cardíaco, Frank-Starling, DC e RPT (Fig. 20.1 a 20.4)"),
    ("Guyton & Hall", "Cap. 20 · PDF p. 777–787", "Limites do coração, controle nervoso, DC alto e baixo (Fig. 20.5 a 20.7)"),
    ("Guyton & Hall", "Cap. 20 · PDF p. 787–791", "Curvas de DC e pressão externa (Fig. 20.8 e 20.9)"),
    ("Guyton & Hall", "Cap. 20 · PDF p. 791–800", "Retorno venoso, PES e resistência (Fig. 20.10 a 20.14)"),
    ("Guyton & Hall", "Cap. 20 · PDF p. 800–808", "Ponto de equilíbrio, volume, simpático e fístula AV (Fig. 20.15 a 20.17)"),
    ("Guyton & Hall", "Cap. 20 · PDF p. 808–814", "Fick, diluição, eco e bioimpedância (Fig. 20.18 a 20.20)"),
]

BASICOS = [
    ("DC normal em repouso no adulto?", "≈ **5 L/min**."),
    ("O que é índice cardíaco e qual o normal?", "DC por m² de superfície: ≈ **3 L/min/m²**."),
    ("O que normalmente controla o DC?", "O **retorno venoso**, que é a soma dos fluxos locais dos tecidos.", "g20_02"),
    ("Dois mecanismos pelos quais o coração se ajusta ao retorno venoso?", "**Frank-Starling** e aumento da FC (estiramento do nó sinusal e **reflexo de Bainbridge**)."),
    ("Relação entre DC e RPT com PA constante?", "**Inversa**: DC = PA ÷ RPT."),
    ("Platô da curva de DC do coração normal?", "≈ **13 L/min** (2,5 × o normal).", "g20_05"),
    ("Dois fatores que tornam o coração hiperfuncionante?", "**Estímulo simpático** (com inibição vagal) e **hipertrofia**."),
    ("Por que o sistema nervoso é necessário para o DC subir muito?", "Mantém a **PA** enquanto os tecidos se dilatam; sem ele a PA cai e o DC sobe pouco."),
    ("Mecanismo comum das causas de DC alto?", "**Queda crônica da RPT**."),
    ("Cite quatro causas de DC alto.", "**Beribéri, fístula AV, hipertireoidismo, anemia**."),
    ("Causa periférica mais comum de DC baixo?", "**Hemorragia** (queda do volume e do retorno venoso)."),
    ("Pressão intrapleural normal e efeito do aumento?", "≈ **−4 mmHg**; aumento desloca a curva de DC para a **direita**."),
    ("Três fatores que determinam o retorno venoso?", "**PAD**, **PES** (enchimento) e **resistência ao RV**."),
    ("Com que PAD o retorno venoso é zero?", "Quando a PAD iguala a **PES** (≈ +7 mmHg).", "g20_10"),
    ("Por que a curva de RV tem platô com PAD negativa?", "As grandes veias que entram no tórax **colapsam**."),
    ("O que é a pressão média de enchimento sistêmico?", "Pressão na circulação sistêmica com o fluxo parado: ≈ **7 mmHg**."),
    ("Efeito do simpático e do volume na PES?", "Ambos **aumentam** a PES (simpático máximo ≈ 14 mmHg)."),
    ("Efeito do aumento da PES na curva de RV?", "Desloca a curva para **cima e para a direita**.", "g20_12"),
    ("Equação do retorno venoso?", "**RV = (PES − PAD) ÷ RRV**."),
    ("Onde está a maior parte da resistência ao retorno venoso?", "≈ **2/3 nas veias**."),
    ("Efeito de reduzir à metade a resistência ao RV?", "**Dobra** a inclinação da curva (mesma PES).", "g20_13"),
    ("Como se acha o DC real a partir das curvas?", "No **cruzamento** da curva de DC com a de RV (ponto de equilíbrio).", "g20_15"),
    ("O que acontece com o DC após transfusão de 20% do volume?", "Sobe **2,5–3 ×** e volta ao normal em **10–40 min**."),
    ("Efeito do simpático máximo no ponto de equilíbrio?", "DC ≈ **2 ×**, PAD quase igual.", "g20_16"),
    ("Efeito da raquianestesia total no DC?", "PES ≈ 4 mmHg; DC cai a ≈ **60%** do normal."),
    ("Equação de Fick?", "**DC = O₂ absorvido ÷ (O₂ arterial − O₂ venoso misto)**.", "g20_19"),
    ("Onde se colhe o sangue venoso misto no Fick?", "No **ventrículo direito ou na artéria pulmonar**."),
    ("Equação da diluição do indicador?", "**DC = quantidade injetada ÷ (concentração média × duração)**."),
]

LACUNAS = [
    ("O índice cardíaco normal é ≈ {{c1::3}} L/min/m².", ""),
    ("DC = {{c1::PA}} ÷ {{c2::resistência periférica total}}.", ""),
    ("O platô da curva de DC normal é ≈ {{c1::13}} L/min; com simpático máximo, ≈ {{c2::25}} L/min.", ""),
    ("RV = ({{c1::PES}} − {{c2::PAD}}) ÷ {{c3::RRV}}.", ""),
    ("A pressão média de enchimento sistêmico normal é ≈ {{c1::7}} mmHg.", ""),
    ("O simpático máximo eleva a PES para ≈ {{c1::14}} mmHg; a inibição a reduz para ≈ {{c2::4}} mmHg.", ""),
    ("Cerca de {{c1::2/3}} da resistência ao retorno venoso está nas {{c2::veias}}.", ""),
    ("A pressão intrapleural normal é ≈ {{c1::−4}} mmHg.", ""),
    ("No ponto de equilíbrio normal o DC é {{c1::5}} L/min e a PAD {{c2::0}} mmHg.", ""),
    ("Fick: 200 mL O₂/min ÷ ({{c1::200}} − {{c2::160}}) mL/L = {{c3::5}} L/min.", ""),
    ("O DC alto crônico sempre resulta de {{c1::queda da resistência periférica total}}.", ""),
]

OCLUSOES = [
    ("g20_10", "Platô", "Que trecho da curva é este?", "Platô (colapso das grandes veias)"),
    ("g20_10", (380, 28, 472, 108), "Que pressão corresponde a este ponto?", "Pressão média de enchimento sistêmico (≈ 7 mmHg)"),
    ("g20_02", (195, 355, 305, 390), "Que órgão recebe 22% do DC?", "Rins"),
    ("g20_05", "Hiperfuncionante", "Que tipo de coração dá estas curvas?", "Hiperfuncionante"),
    ("g20_05", "Hipofuncionante", "Que tipo de coração dá estas curvas?", "Hipofuncionante"),
    ("g20_16", "Raquianestesia", "Que situação dá esta curva?", "Raquianestesia"),
]
