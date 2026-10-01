CODIGO = "c"
SLUG = "c-ecg-normal"
TITULO = "Eletrocardiograma normal"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 11 (PDF p. 427–450)",
    "Guyton & Hall, 14ª ed., cap. 12 (eixos e eixo elétrico médio, PDF p. 451–470)",
]

ESSENCIAL = [
    "**Onda P** é a despolarização dos átrios. O **QRS** é a despolarização dos ventrículos. A **onda T** é a repolarização dos ventrículos. A repolarização atrial fica escondida no QRS.",
    "O ECG só registra algo quando o músculo está **parcialmente** despolarizado ou repolarizado. Músculo todo em repouso ou todo despolarizado dá linha reta.",
    "**Papel:** 25 mm/s, então um quadradinho (1 mm) vale **0,04 s** e um quadrado grande (5 mm) vale **0,20 s**. Na vertical, 10 mm valem **1 mV**.",
    "**Valores de Guyton:** PR **0,16 s**, QRS **0,06–0,08 s**, QT **0,35 s**, RR **0,83 s** (72 bpm).",
    "**Derivações:** D1, D2 e D3 (bipolares), aVR, aVL e aVF (aumentadas) e V1 a V6 (precordiais). **Lei de Einthoven: D1 + D3 = D2.**",
    "**Eixo elétrico médio** do QRS: ≈ **+59°** (normal de ≈ 20° a 100°). A onda T é positiva porque o epicárdio do ápice se repolariza **primeiro**.",
]

CORPO = r'''
= As ondas do ECG

Quando o impulso percorre o coração, uma pequena parte da corrente chega à pele. Eletrodos em lados opostos do coração registram essa diferença de potencial: é o *eletrocardiograma*. Um ECG normal tem as ondas e os intervalos da #vf("g11_01"). O que cada elemento representa está na #vf("t-ondas").

#fig("g11_01", [ECG normal de dois batimentos, com as ondas, os intervalos P-R, Q-T e R-R e o segmento S-T.])


#tabela(rotulo: "t-ondas", titulo: [O que cada elemento do ECG representa e seus valores normais.], (auto, 1fr, auto), ([Elemento], [O que representa], [Duração / voltagem]),
  [*Onda P*], [Despolarização dos *átrios*. Ocorre no início da contração atrial.], [0,1–0,3 mV],
  [*Complexo QRS*], [Despolarização dos *ventrículos*. Ocorre no início da contração ventricular. Q é a primeira deflexão negativa, R a positiva e S a negativa depois de R.], [0,06–0,08 s · 1,0–1,5 mV],
  [*Onda T*], [Repolarização dos *ventrículos* (0,25–0,35 s após a despolarização). É longa e mais baixa que o QRS.], [0,2–0,3 mV],
  [*T atrial*], [Repolarização dos átrios, 0,15–0,20 s após a P. Fica *escondida no QRS* e quase nunca aparece.], [],
  [*Intervalo P-R (P-Q)*], [Do início da P ao início do QRS: do início da excitação atrial ao início da ventricular (inclui o atraso no nó AV).], [≈ 0,16 s],
  [*Intervalo Q-T*], [Do início do QRS ao fim da T: dura quase toda a contração ventricular.], [≈ 0,35 s],
  [*Segmento S-T*], [Do fim do QRS ao início da T. Os ventrículos estão todos despolarizados, por isso é isoelétrico.], [],
  [*Intervalo R-R*], [Tempo entre dois batimentos.], [≈ 0,83 s],
  tamanho: 8.8pt,
)

== Despolarização, repolarização e potencial de ação

O ECG não é o potencial de ação. Ele registra a *diferença de potencial entre áreas* do coração. A #vf("g11_03") mostra os dois registros lado a lado:

- Quando *todo* o ventrículo está em repouso (polarizado) ou *todo* despolarizado (platô), não há diferença entre as áreas e o traçado fica na *linha de base*. Por isso o segmento S-T é isoelétrico.
- O *QRS* aparece no *início* do potencial de ação e a *onda T* no *fim*.
- O potencial de ação dura *0,25–0,35 s* e tem *≈110 mV*. No ECG dos membros o QRS tem só 1,0–1,5 mV; com o eletrodo sobre o coração, até 3–4 mV.

#fig("g11_03", [Potencial de ação de uma fibra ventricular (em cima) e o ECG registrado ao mesmo tempo (embaixo).])

== Por que a onda T é positiva?

A repolarização dos ventrículos começa ≈0,15 s após a despolarização e termina em ≈0,35 s. Seria lógico que o endocárdio, que despolarizou primeiro, também repolarizasse primeiro. Mas é o contrário: o *epicárdio, perto do ápice, repolariza primeiro*, e o endocárdio por último. A explicação proposta é que a alta pressão dentro do ventrículo na sístole reduz o fluxo coronário para o endocárdio e atrasa sua repolarização. O vetor de repolarização aponta então para o ápice, como o do QRS, e a *onda T normal é positiva* nas derivações bipolares, com a mesma polaridade da maior parte do QRS.

= Calibração e leitura do papel

O papel corre a *25 mm/s* e as linhas da grade servem de régua de tempo e de voltagem (#vf("t-papel")).

#tabela(rotulo: "t-papel", titulo: [Equivalências do papel de ECG na calibração padrão.], (1fr, auto), ([Medida no papel], [Valor]),
  [Velocidade padrão], [*25 mm/s*],
  [1 quadradinho (1 mm) na horizontal], [*0,04 s*],
  [1 quadrado grande (5 mm)], [*0,20 s*],
  [5 quadrados grandes (25 mm)], [*1 s*],
  [10 quadradinhos na vertical], [*1 mV*],
)

*Frequência cardíaca:* é o inverso do intervalo R-R. RR de 1 s dá 60 bpm. O RR normal de 0,83 s dá 60/0,83 = *72 bpm*. Na prática, com o papel a 25 mm/s:

- FC = *1.500 ÷ nº de quadradinhos* entre dois R;
- FC = *300 ÷ nº de quadrados grandes* entre dois R (300, 150, 100, 75, 60, 50).

O *P-R encurta* quando a FC sobe (mais simpático, menos vago, condução AV mais rápida) e *alonga* quando a FC cai.

= Por onde a corrente flui no tórax

O coração está mergulhado em um meio condutor (pulmões e líquidos). O impulso chega primeiro ao *septo* e às superfícies *endocárdicas*, que ficam negativas por fora, enquanto o epicárdio ainda está positivo. A média das correntes vai da *base (negativa) para o ápice (positivo)* durante quase toda a despolarização. Só no fim, por ≈0,01 s, ela se inverte, porque as últimas regiões a despolarizar são as paredes externas perto da base. Por isso um eletrodo perto do ápice registra QRS positivo.

= As 12 derivações

== Derivações bipolares dos membros

Os dois braços e a perna esquerda são os vértices do *triângulo de Einthoven*, em torno do coração. Cada derivação bipolar liga dois desses membros (#vf("t-bipolares")).

#tabela(rotulo: "t-bipolares", titulo: [Polos das derivações bipolares dos membros.], (auto, 1fr, 1fr), ([Derivação], [Polo −], [Polo +]),
  [*D1 (I)*], [Braço direito], [Braço esquerdo],
  [*D2 (II)*], [Braço direito], [Perna esquerda],
  [*D3 (III)*], [Braço esquerdo], [Perna esquerda],
)

As três derivações são parecidas (P, QRS e T positivos). Para arritmias, qualquer uma serve, porque o diagnóstico depende do *tempo* entre as ondas. Para lesões do músculo ou do sistema de Purkinje, a derivação escolhida importa muito.

*Lei de Einthoven:* em qualquer instante, *D1 + D3 = D2*, respeitando os sinais. Na #vf("g11_06"), por exemplo, 0,5 + 0,7 = 1,2 mV.

#fig("g11_06", [Eletrodos das derivações bipolares e triângulo de Einthoven. No exemplo, D1 = +0,5 mV, D3 = +0,7 mV e D2 = +1,2 mV.])

== Derivações aumentadas e precordiais

- *Aumentadas dos membros:* um membro vai ao polo positivo e os outros dois, unidos por resistências, ao negativo. Positivo no braço direito é *aVR*; no braço esquerdo, *aVL*; na perna esquerda, *aVF*. São parecidas com as bipolares, mas *aVR é invertida*: o polo positivo fica do lado oposto ao vetor do coração.
- *Precordiais (V1–V6):* eletrodo explorador na parede anterior do tórax (polo positivo) e *terminal central de Wilson* (os três membros unidos) como polo negativo (#vf("g11_08")). Cada eletrodo "vê" principalmente o músculo logo abaixo dele. Por isso pequenas lesões da parede anterior mudam bastante essas derivações.

#fig("g11_08", [Conexões para as derivações precordiais (V1 a V6) com o terminal central de Wilson. BD, braço direito; BE, braço esquerdo.])

A posição de cada eletrodo precordial, padrão da prática clínica, está na #vf("t-precordiais").

#tabela(rotulo: "t-precordiais", titulo: [Posição dos eletrodos precordiais.], (auto, 1fr), ([], [Posição]),
  [*V1*], [4º espaço intercostal, borda esternal direita],
  [*V2*], [4º espaço intercostal, borda esternal esquerda],
  [*V3*], [Entre V2 e V4],
  [*V4*], [5º espaço intercostal, linha hemiclavicular esquerda],
  [*V5*], [Mesmo nível de V4, linha axilar anterior],
  [*V6*], [Mesmo nível de V4, linha axilar média],
)

Em *V1 e V2* o QRS é principalmente *negativo*, porque esses eletrodos estão mais perto da *base*, o lado negativo durante a despolarização. Em *V4 a V6* é principalmente *positivo*, porque estão mais perto do *ápice*. O traçado completo das 12 derivações está na #vf("g11_11").

#fig("g11_11", [ECG normal de 12 derivações: bipolares (I, II, III), aumentadas (aVR, aVL, aVF) e precordiais (V1 a V6). Note o QRS negativo em aVR e a transição de negativo (V1) para positivo (V6).])

= Eixos das derivações e eixo elétrico médio

O *eixo* de uma derivação é a direção do polo negativo para o positivo. Juntos, os seis eixos dos membros formam o *sistema hexagonal* da #vf("g12_03").

#fig("g12_03", [Sistema de referência hexagonal: eixos das derivações bipolares e aumentadas.])

Um vetor que aponta para o polo positivo de uma derivação dá deflexão *positiva* nela; para o negativo, deflexão *negativa*. O ângulo de cada eixo está na #vf("t-eixos").

#tabela(rotulo: "t-eixos", titulo: [Ângulo do eixo de cada derivação dos membros.], (1fr, auto, 1fr, auto), ([Derivação], [Eixo], [Derivação], [Eixo]),
  [*D1*], [0°], [*aVL*], [−30°],
  [*D2*], [+60°], [*aVF*], [+90°],
  [*D3*], [+120°], [*aVR*], [+210°],
)

O *eixo elétrico médio dos ventrículos* (direção média do vetor do QRS) é ≈ *+59°*, e varia normalmente de *≈ 20° a 100°*. O eixo desvia *para o lado do ventrículo hipertrofiado* (mais músculo e despolarização mais demorada desse lado) e *para o lado do ramo bloqueado* (aquele ventrículo despolariza por último). As causas comuns estão na #vf("t-desvios").

#tabela(rotulo: "t-desvios", titulo: [Causas de desvio do eixo elétrico médio.], (1fr, 1fr), ([Eixo desvia para a *esquerda*], [Eixo desvia para a *direita*]),
  [Fim da expiração profunda], [Fim da inspiração profunda],
  [Deitar (vísceras empurram o diafragma)], [Ficar de pé],
  [Obesos], [Pessoas altas e magras (coração "pendurado")],
  [*Hipertrofia do VE* (hipertensão, estenose aórtica)], [*Hipertrofia do VD* (estenose pulmonar)],
  [*Bloqueio de ramo esquerdo*], [*Bloqueio de ramo direito*],
)
'''

VALORES = [
    ("Velocidade do papel", "25 mm/s", "1 mm = 0,04 s · 5 mm = 0,20 s"),
    ("Calibração vertical", "10 mm = 1 mV", ""),
    ("Intervalo P-R", "≈ 0,16 s", "Encurta com FC alta"),
    ("Duração do QRS", "0,06–0,08 s", "Longo se > 0,09 s; bloqueio se > 0,12 s"),
    ("Intervalo Q-T", "≈ 0,35 s", "≈ duração da contração ventricular"),
    ("Intervalo R-R", "≈ 0,83 s", "= 72 bpm"),
    ("Voltagem do QRS (membros)", "1,0–1,5 mV", "Eletrodo sobre o coração: 3–4 mV"),
    ("Voltagem da P", "0,1–0,3 mV", ""),
    ("Voltagem da T", "0,2–0,3 mV", ""),
    ("Potencial de ação ventricular", "≈ 110 mV · 0,25–0,35 s", ""),
    ("Repolarização atrial", "0,15–0,20 s após a P", "Escondida no QRS"),
    ("Eixos: D1, D2, D3", "0°, +60°, +120°", ""),
    ("Eixos: aVL, aVF, aVR", "−30°, +90°, +210°", ""),
    ("Eixo médio do QRS", "≈ +59°", "Normal ≈ 20° a 100°"),
    ("Frequência cardíaca no papel", "1.500 ÷ mm · 300 ÷ quadrados", "Entre dois R"),
]

CLINICA = [
    ("Bloqueios e PR", "PR longo sugere **atraso no nó AV** (vago aumentado, fármacos, doença do sistema de condução). PR curto sugere **via acessória** (pré-excitação)."),
    ("QRS largo", "QRS > 0,09 s é anormal; **> 0,12 s** indica bloqueio de condução no sistema de Purkinje, como o **bloqueio de ramo**. Hipertrofia ou dilatação alargam o QRS para 0,09–0,12 s."),
    ("Desvio do eixo", "Desvio para a esquerda na **hipertensão** (hipertrofia do VE) e no bloqueio de ramo esquerdo. Desvio para a direita na hipertrofia do VD e no bloqueio de ramo direito."),
    ("Holter e monitores", "Para sintomas transitórios (síncope, palpitações, tontura) usa-se o **Holter** (24–48 h), registradores intermitentes (semanas) ou o monitor de eventos implantável (até 2–3 anos)."),
]

PEGADINHAS = [
    "Onda T é **repolarização ventricular**, não atrial. A repolarização atrial some dentro do QRS.",
    "Durante o **segmento S-T** os ventrículos estão **todos despolarizados**: não há diferença de potencial, então o traçado é isoelétrico.",
    "A onda T normal é **positiva** porque a repolarização começa no **epicárdio do ápice**, ao contrário da despolarização.",
    "**aVR** é normalmente **negativa**.",
    "Lei de Einthoven: **D1 + D3 = D2** (não D1 + D2 = D3).",
    "Em V1 o QRS é predominantemente **negativo**; em V6, **positivo**.",
    "Um quadradinho vale **0,04 s**, não 0,4 s; o quadrado grande vale **0,20 s**.",
]

GLOSSARIO = [
    ("Derivação", "Par de eletrodos (ou eletrodo + referência) e o circuito até o eletrocardiógrafo."),
    ("Derivação bipolar", "Registra a diferença entre dois membros (D1, D2, D3)."),
    ("Derivação aumentada", "Um membro no polo positivo e os outros dois unidos no negativo (aVR, aVL, aVF)."),
    ("Terminal central de Wilson", "Os três membros unidos por resistências iguais, usado como polo negativo das precordiais."),
    ("Triângulo de Einthoven", "Triângulo formado pelos dois braços e a perna esquerda em torno do coração."),
    ("Eixo da derivação", "Direção do polo negativo para o positivo da derivação."),
    ("Eixo elétrico médio", "Direção média do vetor de despolarização ventricular (≈ +59°)."),
    ("Segmento", "Trecho entre ondas, sem incluir ondas (ex.: S-T)."),
    ("Intervalo", "Trecho que inclui ondas (ex.: P-R, Q-T)."),
    ("Isoelétrico", "Na linha de base: sem diferença de potencial."),
    ("Holter", "Registro contínuo do ECG por 24–48 h durante a vida diária."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 11 · PDF p. 427–435", "Ondas, relação com o potencial de ação, calibração e valores normais (Fig. 11.1 a 11.3)"),
    ("Guyton & Hall", "Cap. 11 · PDF p. 435–449", "Corrente no tórax e as 12 derivações (Fig. 11.5 a 11.11)"),
    ("Guyton & Hall", "Cap. 12 · PDF p. 453–455", "Eixos das derivações, sistema hexagonal (Fig. 12.3)"),
    ("Guyton & Hall", "Cap. 12 · PDF p. 459–470", "Vetores do QRS e da T, eixo médio e desvios"),
]

BASICOS = [
    ("O que cada onda do ECG representa?", "**P:** despolarização atrial · **QRS:** despolarização ventricular · **T:** repolarização ventricular.", "g11_01"),
    ("Por que não se vê a repolarização atrial?", "Ela ocorre 0,15–0,20 s após a P, ao mesmo tempo que o **QRS**, que a encobre."),
    ("Quando o ECG fica na linha de base?", "Quando o músculo está **todo polarizado** ou **todo despolarizado**: não há diferença de potencial entre as áreas.", "g11_03"),
    ("O que o intervalo P-R mede e qual seu valor?", "Do início da excitação atrial ao início da ventricular (inclui o atraso no nó AV). **≈ 0,16 s**."),
    ("O que acontece com o P-R quando a FC aumenta?", "**Encurta**: mais simpático e menos vago aceleram a condução no nó AV."),
    ("Duração normal do QRS? Quando é anormal?", "**0,06–0,08 s**. Anormal acima de 0,09 s; acima de **0,12 s** sugere bloqueio de ramo."),
    ("O que o intervalo Q-T representa?", "Aproximadamente a **duração da contração ventricular** (≈ 0,35 s)."),
    ("Quanto vale um quadradinho e um quadrado grande a 25 mm/s?", "Quadradinho (1 mm) = **0,04 s**. Quadrado grande (5 mm) = **0,20 s**."),
    ("Como calcular a FC no papel?", "**300 ÷ quadrados grandes** ou **1.500 ÷ quadradinhos** entre dois R. Ou 60 ÷ RR em segundos."),
    ("Quais são os polos de D1, D2 e D3?", "D1: BD (−) → BE (+). D2: BD (−) → PE (+). D3: BE (−) → PE (+).", "g11_06"),
    ("Enuncie a lei de Einthoven.", "Em qualquer instante, **D1 + D3 = D2**."),
    ("Por que aVR é invertida?", "Seu polo positivo (braço direito) fica do lado **oposto** à direção do vetor do coração (base → ápice, para a esquerda e para baixo)."),
    ("Qual é o polo negativo das derivações precordiais?", "O **terminal central de Wilson**: os três membros unidos por resistências iguais.", "g11_08"),
    ("Por que o QRS é negativo em V1 e positivo em V6?", "V1 está perto da **base** (negativa na despolarização); V6 perto do **ápice** (positivo)."),
    ("Por que a onda T normal é positiva?", "O **epicárdio do ápice repolariza primeiro** (o endocárdio fica por último), e o vetor de repolarização aponta para o ápice."),
    ("Eixos de D1, D2, D3, aVR, aVL e aVF?", "D1 **0°** · D2 **+60°** · D3 **+120°** · aVL **−30°** · aVF **+90°** · aVR **+210°**.", "g12_03"),
    ("Eixo elétrico médio normal do QRS?", "≈ **+59°**, variando de ≈ 20° a 100°."),
    ("Para que lado desvia o eixo na hipertrofia ventricular?", "Para o lado do **ventrículo hipertrofiado** (esquerda na HVE, direita na HVD)."),
    ("Para que lado desvia o eixo no bloqueio de ramo?", "Para o lado do **ramo bloqueado**: aquele ventrículo despolariza por último."),
    ("Onde fica V1? E V4?", "V1: 4º espaço intercostal, borda esternal **direita**. V4: 5º espaço intercostal, linha **hemiclavicular** esquerda."),
]

LACUNAS = [
    ("O intervalo P-R normal é de cerca de {{c1::0,16}} s e o Q-T, de cerca de {{c2::0,35}} s.", ""),
    ("O QRS normal dura {{c1::0,06–0,08}} s.", "Acima de 0,12 s: bloqueio de ramo."),
    ("No papel a 25 mm/s, cada quadradinho vale {{c1::0,04}} s e cada quadrado grande vale {{c2::0,20}} s.", ""),
    ("Na calibração padrão, {{c1::10 mm}} na vertical correspondem a {{c2::1 mV}}.", ""),
    ("Lei de Einthoven: {{c1::D1}} + {{c2::D3}} = {{c3::D2}}.", ""),
    ("O eixo elétrico médio normal do QRS é de cerca de {{c1::+59°}}.", "Faixa normal ≈ 20° a 100°."),
    ("D2 tem eixo de {{c1::+60°}}, D3 de {{c2::+120°}} e aVF de {{c3::+90°}}.", ""),
    ("O polo negativo das precordiais é o terminal central de {{c1::Wilson}}.", ""),
    ("Um RR de 0,83 s corresponde a uma FC de {{c1::72}} bpm.", ""),
    ("No ECG dos membros, o QRS tem {{c1::1,0–1,5}} mV, a P {{c2::0,1–0,3}} mV e a T {{c3::0,2–0,3}} mV.", ""),
]

OCLUSOES = [
    ("g11_01", (80, 230, 192, 262), "O que está indicado?", "Intervalo P-R (≈ 0,16 s)"),
    ("g11_01", (525, 120, 597, 156), "O que está indicado?", "Segmento S-T"),
    ("g11_01", (514, 246, 608, 265), "O que está indicado?", "Intervalo Q-T (≈ 0,35 s)"),
    ("g11_01", (350, 41, 440, 59), "O que está indicado?", "Intervalo R-R"),
    ("g12_03", (47, 82, 81, 98), "Qual derivação tem este eixo?", "aVR (+210°)"),
    ("g12_03", (309, 82, 340, 98), "Qual derivação tem este eixo?", "aVL (−30°)"),
    ("g12_03", (202, 350, 234, 364), "Qual derivação tem este eixo?", "aVF (+90°)"),
    ("g12_03", (234, 126, 270, 142), "Qual o ângulo deste eixo?", "−30° (aVL)"),
    ("g12_03", (142, 297, 176, 313), "Qual o ângulo deste eixo?", "+120° (D3)"),
    ("g11_06", (371, 634, 466, 650), "Que derivação é esta?", "Derivação III (BE → perna esquerda)"),
]
