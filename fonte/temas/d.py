CODIGO = "d"
SLUG = "d-biofisica-da-circulacao"
TITULO = "Biofísica da circulação"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 14 (PDF p. 535–568)",
]

ESSENCIAL = [
    "**Lei de Ohm da circulação:** fluxo = **ΔP / R**. Quem move o sangue é a **diferença** de pressão entre as pontas do vaso, não a pressão absoluta.",
    "**Poiseuille:** o fluxo é proporcional à **4ª potência do raio**. Dobrar o raio multiplica o fluxo por 16. Por isso as **arteríolas** (≈ 2/3 da resistência sistêmica) controlam o fluxo.",
    "**Velocidade = fluxo / área.** A área total dos capilares é a maior (≈ 2.500 cm²), então o sangue é **mais lento nos capilares** (≈ 0,3 mm/s) e mais rápido na aorta (≈ 33 cm/s).",
    "**Volume:** ≈ **64% do sangue está nas veias** (reservatório). Só ≈ 7% está em arteríolas e capilares.",
    "**Resistências:** em **série** somam; em **paralelo** a total é **menor** que a de qualquer ramo. RPT ≈ **1 URP**; pulmonar ≈ **0,14 URP**.",
    "**Viscosidade** depende do **hematócrito**: sangue normal ≈ 3–4 vezes a água; policitemia até 10 vezes.",
    "**Autorregulação:** entre ≈ **70 e 175 mmHg** de pressão média, o fluxo do tecido fica quase constante.",
]

CORPO = r'''
= Organização da circulação

A circulação se divide em *sistêmica* (grande circulação, para todos os tecidos menos os pulmões) e *pulmonar* (#vf("g14_01")). Cada segmento tem uma função:

- *Artérias:* levam o sangue sob *alta pressão*, em alta velocidade. Têm parede forte.
- *Arteríolas:* são os *registros de controle* da circulação. A parede muscular forte pode fechá-las por completo ou dilatá-las várias vezes, e assim elas ajustam o fluxo de cada tecido.
- *Capilares:* fazem a *troca* de líquidos, nutrientes e eletrólitos com o interstício. Parede fina, com poros.
- *Vênulas e veias:* levam o sangue de volta ao coração e funcionam como *reservatório* controlável. Pressão baixa e parede fina, mas com músculo capaz de contrair.

#fig("g14_01", [Distribuição do sangue (em % do volume total) nas partes da circulação.])

== Onde está o sangue

Cerca de *84%* do sangue está na circulação sistêmica e *16%* no coração e nos pulmões. Dentro da sistêmica, as *veias guardam ≈ 64%*, as artérias 13% e arteríolas e capilares só 7%. O coração tem 7% e os vasos pulmonares 9%. É no pequeno volume dos capilares que acontece a função mais importante da circulação: a troca com os tecidos.

== Área de seção transversal e velocidade

Somando todos os vasos de cada tipo, a área total é muito diferente de um segmento para outro (#vf("t-areas")). As veias têm, em média, cerca de *4 vezes* a área das artérias, o que explica sua grande capacidade de armazenar sangue.

#tabela(rotulo: "t-areas", titulo: [Área de seção transversal total de cada tipo de vaso (adulto médio).], (1fr, auto), ([Vaso], [Área total (cm²)]),
  [Aorta], [2,5],
  [Pequenas artérias], [20],
  [Arteríolas], [40],
  [*Capilares*], [*2.500*],
  [Vênulas], [250],
  [Pequenas veias], [80],
  [Veias cavas], [8],
)

Como o mesmo fluxo (F) passa por todos os segmentos, a *velocidade (v) é inversamente proporcional à área (A)*: *v = F / A*. Em repouso, a velocidade média é ≈ *33 cm/s na aorta* e só ≈ *0,3 mm/s nos capilares* (1/1.000). Os capilares medem 0,3 a 1 mm, então o sangue fica neles apenas *1 a 3 segundos*, tempo em que toda a troca precisa acontecer.

== Pressões ao longo da circulação

Os valores de pressão para decorar estão na #vf("t-pressoes").

#tabela(rotulo: "t-pressoes", titulo: [Pressões normais nas circulações sistêmica e pulmonar.], (1fr, auto), ([Local], [Pressão]),
  [Aorta (média)], [≈ 100 mmHg (120/80)],
  [Capilar sistêmico: ponta arteriolar → venosa], [35 → 10 mmHg],
  [Capilar sistêmico (pressão funcional média)], [≈ 17 mmHg],
  [Capilar glomerular (rim)], [≈ 60 mmHg],
  [Fim das veias cavas / átrio direito], [≈ 0 mmHg],
  [Artéria pulmonar], [25/8 mmHg (média ≈ 16)],
  [Capilar pulmonar (médio)], [≈ 7 mmHg],
)

A #vf("g14_02") mostra como a pressão cai do ventrículo esquerdo até o átrio direito e, no lado direito da figura, na circulação pulmonar.

#fig("g14_02", [Pressão (mmHg) nas partes da circulação com a pessoa deitada. À esquerda, a circulação sistêmica; à direita, a pulmonar.])


A pressão do capilar sistêmico é baixa o bastante para que pouco plasma escape pelos poros, mas os nutrientes se difundem com facilidade. Na circulação pulmonar as pressões são bem menores, mas o *fluxo é o mesmo* da sistêmica a cada minuto.

== Três princípios da função circulatória

+ O *fluxo de cada tecido é controlado pela necessidade dele*. Um tecido ativo pode precisar de 20 a 30 vezes o fluxo de repouso, mas o coração só aumenta o débito 4 a 7 vezes. Por isso as arteríolas de cada tecido ajustam o fluxo local.
+ O *débito cardíaco é a soma de todos os fluxos locais*. O sangue que passa pelos tecidos volta pelas veias e o coração bombeia o que recebe.
+ A *pressão arterial é regulada de forma independente* do fluxo local e do débito. Se cai abaixo de ≈ 100 mmHg, reflexos nervosos em segundos aumentam a força do coração, contraem os reservatórios venosos e contraem as arteríolas. A longo prazo, os rins regulam a pressão por hormônios e pelo volume de sangue.

= Pressão, fluxo e resistência

O fluxo por um vaso depende de dois fatores: a *diferença de pressão* entre as duas pontas (P1 − P2), que empurra o sangue, e a *resistência vascular*, que vem do atrito do sangue com o endotélio (#vf("g14_03")).

#fig("g14_03", [Relação entre pressão, resistência e fluxo. P1, pressão na origem do vaso; P2, pressão na outra ponta.])

#essencial(titulo: "Lei de Ohm aplicada à circulação")[
  *F = ΔP / R*, em que F é o fluxo, ΔP = P1 − P2 e R é a resistência. Também vale *ΔP = F × R* e *R = ΔP / F*.

  O fluxo é *diretamente proporcional à diferença de pressão* e *inversamente proporcional à resistência*. Se as duas pontas estão a 100 mmHg, *não há fluxo*, mesmo com pressão alta dentro do vaso.
]

== Fluxo sanguíneo

Fluxo é a quantidade de sangue que passa por um ponto em um tempo (mL/min ou L/min). O fluxo total em repouso é ≈ *5.000 mL/min*, que é o *débito cardíaco*. Na prática experimental ele é medido sem abrir o vaso pelo *fluxômetro eletromagnético* ou pelo *Doppler ultrassônico* (o som refletido pelas hemácias que se afastam volta com frequência mais baixa).

== Fluxo laminar e fluxo turbulento

No *fluxo laminar*, o sangue corre em camadas concêntricas. A camada encostada na parede quase não se move e cada camada mais central desliza sobre a anterior, então o centro é o mais rápido. Isso forma o *perfil parabólico* de velocidade (#vf("g14_06"), B).

O *fluxo turbulento* aparece quando o fluxo é muito rápido, passa por uma obstrução, faz curva fechada ou encontra superfície áspera (#vf("g14_06"), C). O sangue forma redemoinhos e a *resistência fica muito maior*.

#fig("g14_06", [A. Dois líquidos antes do fluxo. B. Perfil parabólico 1 s após o início do fluxo laminar. C. Fluxo turbulento.])

A tendência à turbulência é medida pelo *número de Reynolds*: *Re = v · d · ρ / η* (velocidade × diâmetro × densidade ÷ viscosidade). Re de *200 a 400* já causa turbulência nos ramos dos vasos; acima de *≈ 2.000* há turbulência mesmo em vaso reto. Na *aorta proximal e na artéria pulmonar*, Re chega a milhares na ejeção rápida: fluxo rápido e pulsátil, vaso largo e mudança brusca de calibre. Em vasos pequenos quase nunca há turbulência.

== Unidades de pressão e de resistência

A pressão é medida em *mmHg*: 100 mmHg é a força que sustenta uma coluna de mercúrio de 100 mm. *1 mmHg = 1,36 cmH₂O*, porque o mercúrio é 13,6 vezes mais denso que a água. O manômetro de mercúrio não acompanha variações rápidas; para isso se usam transdutores eletrônicos.

A resistência não é medida direto: ela é calculada de ΔP e F. *1 URP* (unidade de resistência periférica) é a resistência com ΔP de 1 mmHg e fluxo de 1 mL/s. Os valores do adulto estão na #vf("t-resist").

#tabela(rotulo: "t-resist", titulo: [Resistências totais no adulto em repouso (débito ≈ 100 mL/s).], (1fr, auto, auto), ([Circulação], [ΔP], [Resistência]),
  [*Sistêmica* (resistência periférica total)], [≈ 100 mmHg], [*≈ 1 URP*],
  [Sistêmica com vasos muito contraídos], [], [até 4 URP],
  [Sistêmica com vasos muito dilatados], [], [até 0,2 URP],
  [*Pulmonar* (16 − 2 mmHg)], [≈ 14 mmHg], [*≈ 0,14 URP*],
)

A *condutância* é o inverso da resistência: *C = 1 / R*. Ela mede quanto fluxo passa para uma dada diferença de pressão.

= O raio manda: lei de Poiseuille

Pequenas mudanças no raio mudam muito a condutância. Na #vf("g14_08") (A), três vasos com raios 1, 2 e 4 e a mesma ΔP de 100 mmHg têm fluxos de *1, 16 e 256 mL/min*. A condutância é proporcional à *quarta potência do raio*.

#fig("g14_08", [A. Efeito do raio sobre o fluxo com a mesma pressão. B. Anéis de sangue com velocidades diferentes: quanto mais longe da parede, mais rápido.])

O motivo está na #vf("g14_08") (B): no vaso grande há muitos anéis de sangue entre a parede e o centro, e o centro corre rápido. No vaso pequeno quase todo o sangue está perto da parede, onde a velocidade é baixa. Somando a velocidade de todos os anéis chega-se à lei de Poiseuille.

#essencial(titulo: "Lei de Poiseuille")[
  *F = π · ΔP · r⁴ / (8 · η · l)*, em que r é o raio, l o comprimento do vaso e η a viscosidade.

  O fluxo é proporcional a *r⁴* e inversamente proporcional à *viscosidade* e ao *comprimento*. O raio é, de longe, o fator mais importante.
]

As *arteríolas* respondem por *≈ 2/3 da resistência sistêmica*. Seu diâmetro interno varia de 4 a 25 µm e pode mudar até 4 vezes, o que muda o fluxo até 256 vezes. Assim, com pequenas mudanças de calibre, respondendo a sinais nervosos ou químicos locais, as arteríolas quase param o fluxo de um tecido ou o aumentam muito.

== Resistências em série e em paralelo

- *Em série* (artérias, arteríolas, capilares, vênulas e veias, um depois do outro): o fluxo é o mesmo em todos e as resistências *somam*: *R total = R1 + R2 + R3 + …*
- *Em paralelo* (as circulações cerebral, renal, muscular, gastrintestinal, cutânea e coronária): *1 / R total = 1 / R1 + 1 / R2 + …* e as condutâncias *somam*: *C total = C1 + C2 + …*. A resistência total é *menor* que a de qualquer ramo isolado, e cada tecido regula seu fluxo quase independente dos outros.

Por isso *amputar um membro ou retirar um rim* remove um circuito em paralelo: a condutância total cai e a *resistência periférica total aumenta*.

= Hematócrito e viscosidade

O *hematócrito* é a porcentagem do sangue ocupada por hemácias: ≈ *42 no homem* e ≈ *38 na mulher*. As hemácias são o principal motivo de o sangue ser viscoso, porque cada uma atrita com as vizinhas e com a parede. A viscosidade sobe muito com o hematócrito (#vf("g14_11")).

- Sangue total com hematócrito normal: viscosidade *3 a 4 vezes* a da água.
- Hematócrito de 60 a 70 (*policitemia*): até *10 vezes* a da água, com fluxo muito reduzido.
- Plasma: ≈ *1,5 vez* a da água. As proteínas plasmáticas pesam pouco perto do hematócrito.

#fig("g14_11", [Efeito do hematócrito sobre a viscosidade do sangue (viscosidade da água = 1).])

= Pressão, resistência e fluxo nos tecidos

== Autorregulação

Seria de esperar que o fluxo subisse na mesma proporção da pressão. Mas, na maioria dos tecidos, quando a pressão sobe a resistência também sobe em poucos segundos, por mecanismos locais, e o fluxo quase não muda. Quando a pressão cai, a resistência cai. Isso é a *autorregulação do fluxo*, que funciona entre *≈ 70 e 175 mmHg* (#vf("g14_12")).

#fig("g14_12", [Fluxo de um tecido (como o músculo esquelético) em função da pressão arterial média. Entre 70 e 175 mmHg o fluxo é autorregulado. A linha azul mostra o efeito do simpático ou de vasoconstritores.])

Estimulação simpática forte e vasoconstritores (*noradrenalina, angiotensina II, vasopressina, endotelina*) reduzem o fluxo, mas o efeito raramente dura mais que algumas horas: os mecanismos locais acabam devolvendo ao tecido o fluxo de que ele precisa.

== Vaso passivo e pressão crítica de fechamento

Num vaso isolado, sem autorregulação, o fluxo sobe *mais* que o previsto por Poiseuille quando a pressão sobe, porque a pressão também *distende* o vaso e reduz a resistência. Quando a pressão cai, o vaso colapsa aos poucos. Abaixo da *pressão crítica de fechamento*, o vaso fecha e o fluxo para. A inibição simpática desloca a curva para a esquerda (mais fluxo); o simpático forte, para a direita, e pode zerar o fluxo por alguns segundos mesmo com pressão alta.

== Tensão na parede e tensão de cisalhamento

A *tensão na parede* estica as células em todas as direções e segue a *lei de Laplace*: *T = ΔP · r / h* (pressão transmural × raio ÷ espessura da parede). Vasos grandes com pressão alta, como a aorta, precisam de parede forte, reforçada por colágeno. Os capilares, de raio muito pequeno, suportam pressões de 65 a 70 mmHg (no rim) com parede fina (#vf("g14_14"), A).

A *tensão de cisalhamento* é o atrito do sangue que corre sobre o endotélio (#vf("g14_14"), B). É proporcional à *velocidade* e à *viscosidade* e inversamente proporcional ao *cubo do raio*. Apesar de pequena, ela orienta o desenvolvimento e a remodelação dos vasos.

#fig("g14_14", [A. Tensão na parede pela pressão transmural (lei de Laplace). B. Tensão de cisalhamento sobre o endotélio.])
'''

VALORES = [
    ("Débito cardíaco (repouso)", "≈ 5.000 mL/min", "≈ 100 mL/s"),
    ("Sangue nas veias sistêmicas", "≈ 64%", "Artérias 13% · arteríolas+capilares 7%"),
    ("Sangue no coração / pulmões", "7% / 9%", "Sistêmica 84%"),
    ("Área total dos capilares", "≈ 2.500 cm²", "Aorta 2,5 cm²"),
    ("Velocidade na aorta", "≈ 33 cm/s", ""),
    ("Velocidade nos capilares", "≈ 0,3 mm/s", "Trânsito de 1–3 s"),
    ("Pressão média na aorta", "≈ 100 mmHg", "120/80"),
    ("Pressão capilar sistêmica", "35 → 10 mmHg", "Funcional média ≈ 17"),
    ("Pressão capilar glomerular", "≈ 60 mmHg", ""),
    ("Artéria pulmonar", "25/8 mmHg", "Média ≈ 16"),
    ("Capilar pulmonar", "≈ 7 mmHg", ""),
    ("Resistência periférica total", "≈ 1 URP", "0,2 a 4 URP"),
    ("Resistência pulmonar total", "≈ 0,14 URP", "≈ 1/7 da sistêmica"),
    ("Resistência das arteríolas", "≈ 2/3 da sistêmica", "Diâmetro 4–25 µm"),
    ("Reynolds com turbulência", "200–400 em ramos", "> 2.000 em vaso reto"),
    ("1 mmHg", "1,36 cmH₂O", ""),
    ("Hematócrito", "♂ ≈ 42 · ♀ ≈ 38", ""),
    ("Viscosidade do sangue", "3–4 × a água", "Policitemia até 10 ×; plasma 1,5 ×"),
    ("Faixa de autorregulação", "≈ 70–175 mmHg", "Pressão arterial média"),
]

CLINICA = [
    ("Sopros", "**Estenose** (vaso ou valva estreitada) aumenta a velocidade e cria **fluxo turbulento**, que vibra e é ouvido como **sopro**. A aorta proximal já tem certa turbulência na ejeção rápida."),
    ("Policitemia e anemia", "Na **policitemia** (hematócrito 60–70) a viscosidade chega a 10 vezes a da água e o fluxo cai muito. Na **anemia** a viscosidade cai e a resistência periférica diminui."),
    ("Vasodilatadores e arteríolas", "Como o fluxo depende de **r⁴**, pequenas dilatações das arteríolas aumentam muito o fluxo e baixam a resistência periférica total: é o alvo dos anti-hipertensivos vasodilatadores."),
    ("Aneurisma", "Pela **lei de Laplace**, quanto maior o raio, maior a tensão na parede: o aneurisma tende a crescer cada vez mais e a romper."),
]

PEGADINHAS = [
    "O fluxo depende da **diferença** de pressão (ΔP), não da pressão absoluta. Pressão igual nas duas pontas = fluxo zero.",
    "A **maior** área de seção transversal é a dos **capilares**, por isso eles têm a **menor** velocidade, não a maior.",
    "A maior parte do sangue está nas **veias** (≈ 64%), não nas artérias.",
    "A **maior resistência** está nas **arteríolas**, não nos capilares: cada capilar é estreito, mas eles estão em paralelo e são muitos.",
    "Em **paralelo**, somar ramos **diminui** a resistência total. Retirar um rim ou amputar um membro **aumenta** a resistência periférica total.",
    "Fluxo ∝ **r⁴**: dobrar o raio aumenta o fluxo **16 vezes**, não 2 nem 4.",
    "**Turbulência** aumenta com velocidade, diâmetro e densidade e **diminui** com a viscosidade.",
]

GLOSSARIO = [
    ("Fluxo sanguíneo", "Volume que passa por um ponto em um tempo (mL/min)."),
    ("Resistência vascular", "Dificuldade ao fluxo, calculada por ΔP / F."),
    ("URP", "Unidade de resistência periférica: 1 mmHg para 1 mL/s."),
    ("Condutância", "Inverso da resistência: fluxo por unidade de ΔP."),
    ("Fluxo laminar", "Fluxo em camadas concêntricas, com perfil parabólico de velocidade."),
    ("Fluxo turbulento", "Fluxo desordenado, com redemoinhos e resistência maior."),
    ("Número de Reynolds", "Índice da tendência à turbulência (v · d · ρ / η)."),
    ("Hematócrito", "Porcentagem do sangue ocupada por hemácias."),
    ("Viscosidade", "Atrito interno do líquido; no sangue, depende sobretudo das hemácias."),
    ("Autorregulação", "Manutenção do fluxo de um tecido apesar de mudanças da pressão (≈ 70–175 mmHg)."),
    ("Pressão crítica de fechamento", "Pressão abaixo da qual um vaso colapsa e o fluxo para."),
    ("Pressão transmural", "Pressão de dentro menos a de fora do vaso."),
    ("Tensão de cisalhamento", "Atrito do sangue sobre o endotélio."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 14 · PDF p. 535–543", "Partes da circulação, volumes, áreas, velocidade e pressões (Fig. 14.1 e 14.2)"),
    ("Guyton & Hall", "Cap. 14 · PDF p. 543–550", "Lei de Ohm, fluxo, laminar e turbulento (Fig. 14.3 a 14.6)"),
    ("Guyton & Hall", "Cap. 14 · PDF p. 550–559", "Unidades, resistência, Poiseuille, série e paralelo (Fig. 14.8 e 14.9)"),
    ("Guyton & Hall", "Cap. 14 · PDF p. 559–568", "Hematócrito, viscosidade, autorregulação, Laplace (Fig. 14.10 a 14.14)"),
]

BASICOS = [
    ("Onde está a maior parte do volume de sangue?", "Nas **veias sistêmicas** (≈ 64%), que funcionam como reservatório.", "g14_01"),
    ("Função das arteríolas?", "São os **registros de controle**: com parede muscular forte, ajustam o fluxo de cada tecido."),
    ("Qual segmento tem a maior área total? E a menor velocidade?", "Os **capilares** (≈ 2.500 cm²); por isso a velocidade é mínima (≈ 0,3 mm/s)."),
    ("Fórmula da velocidade do sangue em função da área?", "**v = F / A**: velocidade inversamente proporcional à área de seção transversal."),
    ("Pressão média do capilar sistêmico? E do glomerular?", "Sistêmico ≈ **17 mmHg** (35 → 10). Glomerular ≈ **60 mmHg**.", "g14_02"),
    ("Pressões da artéria pulmonar?", "**25/8 mmHg**, média ≈ 16. Capilar pulmonar ≈ 7 mmHg."),
    ("Lei de Ohm aplicada à circulação?", "**F = ΔP / R**.", "g14_03"),
    ("O que determina o fluxo: a pressão absoluta ou a diferença de pressão?", "A **diferença** de pressão entre as duas pontas do vaso."),
    ("O que é o perfil parabólico do fluxo laminar?", "O centro do vaso é o mais rápido e a camada junto à parede quase não se move.", "g14_06"),
    ("Fatores que favorecem o fluxo turbulento?", "**Velocidade, diâmetro e densidade** altos e **viscosidade** baixa; também obstrução, curva fechada e superfície áspera."),
    ("Acima de que número de Reynolds há turbulência?", "200–400 nos ramos; > **2.000** mesmo em vaso reto."),
    ("Quanto vale a resistência periférica total? E a pulmonar?", "Sistêmica ≈ **1 URP**; pulmonar ≈ **0,14 URP**."),
    ("Lei de Poiseuille?", "**F = π · ΔP · r⁴ / (8 · η · l)**: fluxo proporcional à 4ª potência do raio.", "g14_08"),
    ("Raios 1, 2 e 4 com a mesma ΔP dão quais fluxos?", "**1, 16 e 256** mL/min."),
    ("Que vasos têm a maior parte da resistência sistêmica?", "As **arteríolas** (≈ 2/3)."),
    ("Como somam resistências em série e em paralelo?", "Série: **R = R1 + R2 + …**. Paralelo: **1/R = 1/R1 + 1/R2 + …** (somam as condutâncias)."),
    ("O que acontece com a RPT após nefrectomia ou amputação?", "**Aumenta**: retira-se um circuito em paralelo e a condutância total cai."),
    ("Viscosidade do sangue normal e na policitemia?", "Normal **3–4 ×** a água; policitemia até **10 ×**.", "g14_11"),
    ("O que é autorregulação do fluxo e sua faixa?", "O tecido mantém o fluxo quase constante entre ≈ **70 e 175 mmHg** ajustando a resistência.", "g14_12"),
    ("O que é pressão crítica de fechamento?", "Pressão abaixo da qual o vaso passivo colapsa e o fluxo para.", "g14_13"),
    ("Lei de Laplace?", "**T = ΔP · r / h**: tensão na parede proporcional à pressão transmural e ao raio, inversa à espessura.", "g14_14"),
]

LACUNAS = [
    ("Fluxo = {{c1::diferença de pressão}} ÷ {{c2::resistência}}.", "Lei de Ohm da circulação."),
    ("Cerca de {{c1::64}}% do sangue está nas veias sistêmicas.", ""),
    ("A velocidade do sangue é ≈ {{c1::33 cm/s}} na aorta e ≈ {{c2::0,3 mm/s}} nos capilares.", ""),
    ("A área total dos capilares é de ≈ {{c1::2.500}} cm².", ""),
    ("O fluxo é proporcional à {{c1::quarta}} potência do raio.", "Lei de Poiseuille."),
    ("As arteríolas respondem por ≈ {{c1::2/3}} da resistência sistêmica.", ""),
    ("A resistência periférica total é ≈ {{c1::1}} URP e a pulmonar ≈ {{c2::0,14}} URP.", ""),
    ("Turbulência ocorre mesmo em vaso reto com Reynolds acima de ≈ {{c1::2.000}}.", ""),
    ("1 mmHg equivale a {{c1::1,36}} cmH₂O.", ""),
    ("A viscosidade do sangue normal é {{c1::3 a 4}} vezes a da água; a do plasma, {{c2::1,5}} vez.", ""),
    ("A autorregulação mantém o fluxo entre ≈ {{c1::70}} e {{c2::175}} mmHg.", ""),
    ("Lei de Laplace: T = {{c1::ΔP · r / h}}.", ""),
]

OCLUSOES = [
    ("g14_01", "64%", "Que porcentagem do sangue está aqui?", "64% (veias, vênulas e seios venosos)"),
    ("g14_01", "13%", "Que porcentagem do sangue está aqui?", "13% (artérias)"),
    ("g14_01", "84%", "Que porcentagem do sangue está na circulação sistêmica?", "84%"),
    ("g14_01", "9%", "Que porcentagem do sangue está aqui?", "9% (circulação pulmonar)"),
    ("g14_08", "16", "Qual o fluxo com raio 2?", "16 mL/min"),
    ("g14_08", "256", "Qual o fluxo com raio 4?", "256 mL/min"),
    ("g14_12", "Vasoconstritores", "O que desloca a curva para baixo?", "Vasoconstritores e simpático"),
    ("g14_13", "fechamento", "O que é indicado nestes pontos?", "Pressão crítica de fechamento"),
]
