CODIGO = "f"
SLUG = "f-controle-da-circulacao"
TITULO = "Controle local, humoral e nervoso da circulação"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 17 (PDF p. 642–680)",
    "Guyton & Hall, 14ª ed., cap. 18 (PDF p. 681–715)",
]

ESSENCIAL = [
    "**Controle local:** cada tecido ajusta o próprio fluxo à sua **necessidade metabólica** (sobretudo de **O₂**). Metabolismo 8 × maior faz o fluxo subir ≈ 4 ×.",
    "**Autorregulação:** entre ≈ **70 e 175 mmHg** o fluxo quase não muda. Duas teorias: **metabólica** (lava os vasodilatadores) e **miogênica** (estiramento abre canais de Ca²⁺ e contrai).",
    "**Óxido nítrico:** o endotélio o libera sob **tensão de cisalhamento**; ativa **guanilato ciclase → GMPc** e relaxa o músculo liso. **Endotelina** é o vasoconstritor do endotélio lesado.",
    "**Longo prazo:** muda a **vascularização** (angiogênese por **VEGF**, estimulada pela falta de O₂) e remodela a parede dos vasos.",
    "**Humoral:** constritores = **noradrenalina/adrenalina, angiotensina II, vasopressina, endotelina**. Dilatadores = **bradicinina, histamina** (e NO).",
    "**Nervoso:** quase todo pelo **simpático** (noradrenalina em receptores **α**). O **centro vasomotor** (bulbo e ponte) mantém o **tônus vasomotor**; o **vago** reduz a FC.",
    "**Barorreflexo:** seio carotídeo (n. de Hering → IX) e arco aórtico (X) → **núcleo do trato solitário**. PA alta → inibe o simpático e excita o vago. Faixa de 60 a 180 mmHg, mais sensível perto de **100 mmHg**; reajusta em 1–2 dias.",
    "**Quimiorreceptores** só pesam abaixo de **80 mmHg**; a **resposta isquêmica do SNC** abaixo de **60 mmHg** (máxima em 15–20). **Reação de Cushing:** hipertensão intracraniana → PA sobe.",
]

CORPO = r'''
= Controle local do fluxo

Cada tecido controla o próprio fluxo de acordo com o que precisa: entregar *O₂* e nutrientes, retirar CO₂ e H⁺, e, em alguns órgãos, cumprir uma função especial (rim, pele). O fluxo de cada órgão em repouso está na #vf("t-fluxos").

#tabela(rotulo: "t-fluxos", titulo: [Fluxo sanguíneo dos órgãos em repouso (Guyton, Tabela 17.1).], (1fr, auto, auto, auto), ([Órgão], [% do DC], [mL/min], [mL/min/100 g]),
  [Cérebro], [14], [700], [50],
  [Coração], [4], [200], [70],
  [*Rins*], [22], [1.100], [*360*],
  [*Fígado*], [*27*], [*1.350*], [95],
  [Músculo (inativo)], [15], [750], [4],
  [Pele (frio)], [6], [300], [3],
  [Tireoide], [1], [50], [160],
  [Adrenais], [0,5], [25], [300],
  [*Total*], [100], [*5.000*], [—],
)

O controle tem duas fases: o *agudo*, em segundos a minutos, por constrição e dilatação de arteríolas, metarteríolas e esfíncteres pré-capilares; e o *de longo prazo*, em dias a meses, por mudança no tamanho e no número de vasos.

== Controle agudo pelo metabolismo

Quando o metabolismo aumenta 8 vezes, o fluxo aumenta ≈ 4 vezes (#vf("g17_01")). A falta de O₂ (altitude, pneumonia, intoxicação por monóxido de carbono ou cianeto) também dilata: no cianeto o fluxo pode subir até 7 vezes.

#fig("g17_01", [Efeito do aumento da taxa de metabolismo sobre o fluxo sanguíneo do tecido.])

Duas teorias explicam esse controle e provavelmente atuam juntas:

- *Teoria vasodilatadora:* o tecido ativo ou com pouco O₂ libera *adenosina*, *CO₂*, *H⁺*, *K⁺*, *histamina* e ácido láctico, que dilatam as arteríolas. A *adenosina* é o principal no *coração*.
- *Teoria da demanda de O₂ (nutrientes):* o músculo liso precisa de O₂ para se contrair. Com pouco O₂ ele relaxa, e os esfíncteres pré-capilares ficam abertos mais tempo (*vasomotricidade*).

== Hiperemias

A #vf("g17_04") mostra as duas hiperemias, que são consequência do controle metabólico:

- *Hiperemia reativa:* após ocluir a artéria por segundos a horas, o fluxo sobe *4 a 7 vezes* quando ela é liberada. O excesso dura o bastante para pagar a "dívida" de O₂.
- *Hiperemia ativa:* quando o tecido trabalha mais (músculo no exercício, glândula secretando, cérebro pensando). No músculo esquelético o fluxo pode subir até *20 vezes*.

#fig("g17_04", largura: 6cm, [Hiperemia reativa após oclusão arterial (acima) e hiperemia ativa durante estimulação muscular (abaixo).])

== Autorregulação

Se a pressão arterial sobe de repente, o fluxo aumenta, mas em menos de 1 minuto volta perto do normal. Entre ≈ *70 e 175 mmHg*, um aumento de 150% na pressão aumenta o fluxo em só 20–30% (#vf("g17_05")). No cérebro e no coração a autorregulação é ainda mais precisa.

#fig("g17_05", [Fluxo muscular em diferentes pressões: curva aguda (vermelha) e curva após semanas de regulação de longo prazo (tracejada).])

- *Teoria metabólica:* pressão alta traz O₂ demais e lava os vasodilatadores, e os vasos se contraem.
- *Teoria miogênica:* o *estiramento* da parede despolariza o músculo liso, abre canais de *Ca²⁺* e ele se contrai. Protege sobretudo contra pressão alta nos vasos pequenos.

Órgãos com função especial têm mecanismos próprios: no *rim*, o *feedback tubuloglomerular* (a *mácula densa* detecta o líquido do túbulo distal e ajusta as arteríolas); no *cérebro*, *CO₂* e *H⁺* altos dilatam os vasos; na *pele*, o fluxo segue a *temperatura* (de 3 mL/min/100 g até 7–8 L/min no corpo todo, controlado pelo simpático).

= Endotélio

O endotélio sente a *tensão de cisalhamento* do sangue e libera substâncias que mudam o tônus do vaso (#vf("g17_06")).

#fig("g17_06", [Síntese de óxido nítrico (NO) no endotélio e relaxamento do músculo liso via guanilato ciclase e GMPc.])

- *Óxido nítrico (NO):* a *eNOS* o produz a partir da *arginina*. Meia-vida de ≈ 6 s. No músculo liso ativa a *guanilato ciclase solúvel*, que forma *GMPc* e ativa a proteína cinase G, causando relaxamento. Quando o fluxo na microcirculação aumenta, o cisalhamento libera NO e dilata as *artérias a montante* ("dilatação mediada pelo fluxo"). Angiotensina II e acetilcolina também liberam NO.
- *Uso clínico:* *nitroglicerina* e outros nitratos liberam NO (angina). A *sildenafila* inibe a fosfodiesterase 5 (PDE-5), que degrada o GMPc.
- *Endotelina:* peptídeo de 27 aminoácidos, liberado pelo *endotélio lesado*. Concentrações mínimas causam vasoconstrição intensa; evita sangramento de artérias de até 5 mm de diâmetro.

O endotélio lesado (hipertensão crônica, aterosclerose) produz menos NO e contribui para a doença.

= Controle de longo prazo

O controle agudo corrige só ≈ 3/4 do excesso de fluxo. Se a pressão sobe de 100 para 150 mmHg, o fluxo dobra de imediato, cai a +10–15% em 30 s a 2 min e, ao longo de semanas, volta quase ao normal (curva tracejada da #vf("g17_05")). O mecanismo principal é mudar a *vascularização*.

- *Angiogênese:* pouco O₂ estimula fatores como o *VEGF* (fator de crescimento do endotélio vascular), o FGF, o PDGF e a angiogenina. Brotam novos vasos a partir de vênulas e capilares. *Angiostatina* e *endostatina* inibem o processo.
- A vascularização se ajusta à *necessidade máxima* de fluxo, não à média.
- *Retinopatia da prematuridade:* o recém-nascido prematuro tratado com O₂ em excesso para de formar vasos na retina; ao sair do O₂, o crescimento é explosivo e pode causar cegueira.
- *Colaterais:* quando uma artéria é ocluída, vasos pequenos se dilatam em segundos a minutos (≈ 1/4 do fluxo), chegam à metade em 1 dia e, em poucos dias, ao fluxo quase normal. Por isso a oclusão coronariana lenta é mais bem tolerada que a súbita.

== Remodelagem vascular

A parede dos vasos se adapta a mudanças crônicas de pressão e fluxo (#vf("g17_08")). A tensão na parede segue *Laplace: T = r × P*.

#fig("g17_08", largura: 5cm, [Remodelagem vascular após aumento crônico de pressão ou de fluxo.])

- *Eutrófica concêntrica:* pequenas artérias que se contraem com a hipertensão. Lúmen menor, parede mais espessa, *mesma área de parede*.
- *Hipertrófica:* grandes artérias com pressão alta. Parede mais espessa e mais rígida, marca da hipertensão crônica.
- *Eutrófica excêntrica:* aumento crônico de *fluxo*. Lúmen maior, parede igual (artéria radial de uma fístula arteriovenosa).
- *Hipertrófica excêntrica:* aumento de pressão e fluxo. Lúmen e parede maiores (veia da fístula, *veia safena* usada em ponte coronária, que em meses fica com parede de artéria).

= Controle humoral

Substâncias do sangue também mudam o tônus dos vasos (#vf("t-humoral")). Elas têm pouco efeito no fluxo de longo prazo, a menos que mudem o metabolismo do tecido.

#tabela(rotulo: "t-humoral", titulo: [Principais agentes humorais vasoativos.], (auto, 1fr), ([Agente], [Origem e efeito]),
  [*Noradrenalina*], [Simpático e medula adrenal. Vasoconstritor potente (receptores α).],
  [*Adrenalina*], [Medula adrenal. Constritor menos potente; *dilata as coronárias* (β) no aumento da atividade cardíaca.],
  [*Angiotensina II*], [Constrição potente das arteríolas: 1 milionésimo de grama sobe a PA em ≈ 50 mmHg. Eleva a resistência periférica total.],
  [*Vasopressina (ADH)*], [Hipotálamo, neuro-hipófise. Constritor ainda mais potente que a angiotensina II; sobe muito na hemorragia. Sua função principal é reabsorver água no rim.],
  [*Bradicinina*], [Formada pela calicreína, inativada pela *ECA*. Dilatação arteriolar intensa e mais permeabilidade capilar (edema).],
  [*Histamina*], [Mastócitos e basófilos (lesão, alergia). Dilata arteríolas e aumenta a permeabilidade capilar: edema.],
)

*Íons:* Ca²⁺ alto causa *constrição*; K⁺, Mg²⁺ e H⁺ altos causam *dilatação* (acetato e citrato também). O *CO₂* dilata a maioria dos tecidos, sobretudo o *cérebro*, mas pelo centro vasomotor causa constrição generalizada indireta.

= Controle nervoso

O controle nervoso tem ação mais *global*: redistribui o fluxo entre os órgãos, muda o bombeamento do coração e controla a pressão arterial *rapidamente*. É feito quase todo pelo *sistema nervoso autônomo*.

== Simpático e parassimpático

- *Simpático:* fibras saem da medula torácica e lombar alta. Inervam *todos os vasos exceto os capilares*. Nas arteríolas aumenta a resistência; nas *veias* reduz o volume e empurra sangue ao coração. No coração aumenta a *frequência* e a *contratilidade*. O efeito vasoconstritor é forte em *rins, intestino, baço e pele* e fraco em músculo esquelético, coração e cérebro.
- *Parassimpático:* papel pequeno nos vasos. Seu efeito principal é *reduzir a frequência cardíaca* pelo *vago* (e um pouco a contratilidade).

== Centro vasomotor

O *centro vasomotor* fica na substância reticular do *bulbo* e no terço inferior da *ponte* (#vf("g18_03")). Ele envia sinais simpáticos pela medula e parassimpáticos pelo vago e tem três áreas (#vf("t-centro")).

#tabela(rotulo: "t-centro", titulo: [As três áreas do centro vasomotor.], (auto, 1fr), ([Área], [Local e função]),
  [*Vasoconstritora*], [Bulbo superior, anterolateral. Excita os neurônios simpáticos pré-ganglionares.],
  [*Vasodilatadora*], [Bulbo inferior, anterolateral. Inibe a área vasoconstritora.],
  [*Sensorial*], [*Núcleo do trato solitário*. Recebe os sinais dos nervos *vago e glossofaríngeo* e comanda os reflexos.],
)

#fig("g18_03", largura: 7cm, [Áreas do encéfalo que controlam a circulação. As linhas tracejadas são vias inibitórias.])

A área vasoconstritora dispara continuamente (0,5–2 impulsos/s): é o *tônus vasoconstritor simpático*, que mantém os vasos parcialmente contraídos (*tônus vasomotor*). Uma raquianestesia total bloqueia esse tônus e a PA cai de *100 para 50 mmHg*. Hipotálamo, formação reticular e córtex podem excitar ou inibir o centro vasomotor.

*Noradrenalina* é o neurotransmissor vasoconstritor (receptores *α*). A *medula adrenal* lança adrenalina e noradrenalina no sangue ao mesmo tempo. Nos músculos, a adrenalina em receptores *β* pode dilatar.

*Síncope vasovagal (desmaio emocional):* uma emoção forte ativa os vasodilatadores dos músculos e o centro cardioinibitório vagal. A FC e a PA caem, o fluxo cerebral diminui e a pessoa desmaia.

== Aumento rápido da pressão

Para subir a PA, o sistema nervoso faz três coisas *ao mesmo tempo*: contrai as *arteríolas* (mais resistência), contrai as *veias* (mais retorno e enchimento do coração) e estimula o *coração* (FC até 3 ×, bombeamento até 2 ×). É o mecanismo *mais rápido*: dobra a PA em *5–10 s*, ou a reduz à metade em 10–40 s.

No *exercício* a PA sobe 30–40%, sobretudo por ativação do centro vasomotor junto com as áreas motoras. Na *reação de alarme* (medo intenso) a PA pode subir 75–100 mmHg em segundos.

= Reflexos que mantêm a PA

== Barorreceptores

São *terminações nervosas livres* sensíveis ao *estiramento*, abundantes no *seio carotídeo* (carótida interna, logo acima da bifurcação) e no *arco aórtico* (#vf("g18_05")). Os sinais do seio carotídeo seguem pelo *nervo de Hering* ao *glossofaríngeo* (IX); os do arco aórtico, pelo *vago* (X). Ambos chegam ao *núcleo do trato solitário*.

#fig("g18_05", [Sistema barorreceptor: seio carotídeo, arco aórtico e suas vias nervosas até o bulbo.])

PA alta estira os barorreceptores, que *inibem o centro vasoconstritor* e *excitam o vago*: há vasodilatação de veias e arteríolas e queda da FC e da contratilidade, e a PA cai. PA baixa faz o contrário.

O seio carotídeo *não dispara abaixo de 50–60 mmHg* e chega ao máximo em ≈ *180 mmHg* (#vf("g18_06")). A maior sensibilidade (ΔI/ΔP máximo) fica em ≈ *100 mmHg*, onde ela é mais útil. Os aórticos operam ≈ 30 mmHg acima. Eles respondem mais a pressão que *muda rápido* do que a pressão estável.

#fig("g18_06", [Impulsos do nervo do seio carotídeo em cada nível de pressão arterial. A maior inclinação (ΔI/ΔP) fica perto de 100 mmHg.])

- *Postura:* ao levantar, a PA na cabeça cai; o barorreflexo dispara o simpático e evita o desmaio.
- *Sistema tampão:* sem barorreceptores, a variação diária da PA fica ≈ *2,5 vezes maior* (de 50 a mais de 160 mmHg). O barorreflexo reduz a variação a ≈ 1/3.
- *Longo prazo:* os barorreceptores *se reajustam* em *1–2 dias* ao novo nível de pressão, por isso pesam pouco no controle crônico. Ajudam um pouco ao reduzir a atividade simpática renal. A estimulação elétrica crônica do seio carotídeo baixa a PA em 15–20 mmHg.

== Quimiorreceptores

Células sensíveis a *O₂ baixo*, *CO₂ alto* e *H⁺ alto*, nos *corpos carotídeos* (na bifurcação da carótida comum) e *aórticos*, de ≈ 2 mm. Quando a PA cai, o fluxo nesses corpos diminui e os quimiorreceptores excitam o centro vasomotor. Só são potentes com PA *abaixo de 80 mmHg*. Também elevam a PA na obesidade grave e na apneia obstrutiva do sono.

== Receptores de baixa pressão e reflexo de volume

Os *átrios* e as *artérias pulmonares* têm receptores de estiramento que detectam aumento de *volume*. Infundir 300 mL num cão sobe a PA em 15 mmHg com todos os receptores, 40 sem os barorreceptores e 100 sem os de baixa pressão também. O estiramento atrial desencadeia os reflexos da #vf("g18_10").

#fig("g18_10", largura: 9cm, [Respostas reflexas ao aumento do volume de sangue e ao estiramento atrial.])

- *Reflexo de volume:* menos simpático renal (dilata a arteríola aferente e filtra mais), menos *ADH* e liberação do *peptídeo natriurético atrial*. O resultado é excretar sódio e água.
- *Reflexo de Bainbridge:* o estiramento dos átrios aumenta a FC em até 75% (40–60% pelo reflexo, via vago, e até 15% pelo estiramento direto do nó sinusal). Evita o represamento de sangue nas veias.

== Resposta isquêmica do SNC

Se o fluxo para o centro vasomotor cai muito, o *CO₂* acumulado excita diretamente os neurônios vasoconstritores. A PA pode chegar a *250 mmHg* por até 10 min, e a constrição renal pode parar a produção de urina. É um sistema de *emergência*: só atua com PA *abaixo de 60 mmHg* e é máximo em *15–20 mmHg*.

*Reação de Cushing:* quando a pressão do *líquor* sobe até igualar a pressão arterial, as artérias cerebrais são comprimidas; a isquemia eleva a PA até ficar um pouco acima da pressão do líquor, e o fluxo cerebral volta.

'''

VALORES = [
    ("Débito cardíaco em repouso", "5.000 mL/min", ""),
    ("Fluxo renal", "1.100 mL/min (22%)", "360 mL/min/100 g, o maior por peso"),
    ("Fluxo hepático", "1.350 mL/min (27%)", "Maior fluxo absoluto"),
    ("Fluxo cerebral", "700 mL/min (14%)", "50 mL/min/100 g"),
    ("Fluxo coronariano", "200 mL/min (4%)", "70 mL/min/100 g"),
    ("Metabolismo 8 ×", "Fluxo ≈ 4 ×", ""),
    ("Hiperemia reativa", "4–7 × o fluxo", ""),
    ("Hiperemia ativa (músculo)", "Até 20 ×", ""),
    ("Faixa de autorregulação", "≈ 70–175 mmHg", "+150% de PA → +20–30% de fluxo"),
    ("Controle agudo corrige", "≈ 3/4 do excesso", "Longo prazo corrige o resto"),
    ("Meia-vida do NO", "≈ 6 s", ""),
    ("Endotelina", "27 aminoácidos", "Hemostasia em artérias até 5 mm"),
    ("Angiotensina II", "1 µg → PA + 50 mmHg", ""),
    ("Tônus simpático", "0,5–2 impulsos/s", "Raquianestesia total: PA 100 → 50"),
    ("Simpático máximo", "FC até 3 ×", "Bombeamento até 2 ×"),
    ("Velocidade do controle nervoso", "PA × 2 em 5–10 s", "PA ÷ 2 em 10–40 s"),
    ("Seio carotídeo", "Silencioso < 50–60 mmHg", "Máximo ≈ 180 mmHg"),
    ("Maior sensibilidade barorreceptora", "≈ 100 mmHg", ""),
    ("Reajuste dos barorreceptores", "1–2 dias", ""),
    ("Quimiorreceptores", "PA < 80 mmHg", "Corpos de ≈ 2 mm"),
    ("Resposta isquêmica do SNC", "PA < 60 mmHg", "Máxima em 15–20; PA até 250"),
    ("Reflexo de Bainbridge", "FC até + 75%", ""),
]

CLINICA = [
    ("Nitratos e sildenafila", "A **nitroglicerina** libera NO e dilata (angina). A **sildenafila** inibe a PDE-5 e mantém o GMPc. Juntos podem causar **hipotensão grave**."),
    ("Circulação colateral", "Oclusão coronariana **lenta** dá tempo para colaterais (dias) e é mais bem tolerada que a oclusão **súbita**, que causa infarto."),
    ("Hipotensão ortostática", "Ao levantar, o **barorreflexo** evita a queda da PA na cabeça. Se falha (disautonomia, idosos, desidratação), surgem tontura e síncope."),
    ("Síncope vasovagal", "Emoção forte: vasodilatação muscular + **bradicardia vagal** → PA e fluxo cerebral caem → desmaio."),
    ("Massagem do seio carotídeo", "Estimula os barorreceptores → **aumenta o tônus vagal** e reduz a FC (usada para reverter taquicardias supraventriculares)."),
    ("Tríade de Cushing", "Hipertensão intracraniana: **PA alta**, **bradicardia** (barorreflexo) e respiração irregular. Sinal de herniação iminente."),
    ("Inibidores da ECA", "Bloqueiam a formação de angiotensina II **e** a degradação da bradicinina; a bradicinina acumulada explica a **tosse** e o **angioedema**."),
    ("Retinopatia da prematuridade", "Excesso de O₂ suprime e depois desencadeia crescimento vascular explosivo na retina, com risco de cegueira."),
]

PEGADINHAS = [
    "Maior fluxo **por grama** é o do **rim** (360 mL/min/100 g); maior fluxo **absoluto** é o do **fígado** (1.350 mL/min).",
    "Autorregulação **não** mantém o fluxo totalmente constante: +150% de pressão ainda dá +20–30% de fluxo.",
    "Na teoria **miogênica**, quem dispara a contração é o **estiramento** (entrada de Ca²⁺), não um metabólito.",
    "O simpático inerva **todos os vasos exceto os capilares**.",
    "O **parassimpático** quase não age nos vasos: o efeito circulatório principal é **reduzir a FC**.",
    "Barorreceptores do **seio carotídeo** → nervo de Hering → **glossofaríngeo (IX)**; do **arco aórtico** → **vago (X)**.",
    "Barorreceptores **não** controlam bem a PA a longo prazo: **reajustam em 1–2 dias**.",
    "Quimiorreceptores e resposta isquêmica do SNC **não** regulam a PA normal: só abaixo de 80 e de 60 mmHg.",
    "**Corpo** carotídeo (quimiorreceptor, na bifurcação) ≠ **seio** carotídeo (barorreceptor, na carótida interna).",
    "A **adrenalina** dilata as coronárias e os vasos musculares (β); a noradrenalina contrai (α).",
]

GLOSSARIO = [
    ("Hiperemia reativa", "Aumento do fluxo após o fim de uma oclusão arterial."),
    ("Hiperemia ativa", "Aumento do fluxo quando o tecido aumenta a atividade."),
    ("Autorregulação", "Fluxo quase constante apesar de mudanças da pressão arterial."),
    ("Teoria miogênica", "Contração do músculo liso em resposta ao estiramento."),
    ("Feedback tubuloglomerular", "Ajuste das arteríolas renais pela mácula densa."),
    ("Tensão de cisalhamento", "Força de arrasto do sangue sobre o endotélio."),
    ("eNOS", "Óxido nítrico sintase endotelial."),
    ("Endotelina", "Peptídeo vasoconstritor do endotélio lesado."),
    ("VEGF", "Fator de crescimento do endotélio vascular (angiogênese)."),
    ("Remodelagem eutrófica", "Mudança do lúmen sem mudar a área da parede."),
    ("Centro vasomotor", "Área do bulbo e da ponte que comanda simpático e vago."),
    ("Tônus vasomotor", "Constrição parcial contínua dos vasos pelo simpático."),
    ("Núcleo do trato solitário", "Área sensorial do bulbo que recebe IX e X."),
    ("Barorreceptor", "Terminação nervosa sensível ao estiramento arterial."),
    ("Quimiorreceptor", "Célula sensível a O₂ baixo, CO₂ e H⁺ altos."),
    ("Reflexo de Bainbridge", "Aumento da FC pelo estiramento atrial."),
    ("Reação de Cushing", "Aumento da PA pela isquemia cerebral na hipertensão intracraniana."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 17 · PDF p. 642–654", "Fluxo dos órgãos, controle metabólico, hiperemias (Tabela 17.1, Fig. 17.1 a 17.4)"),
    ("Guyton & Hall", "Cap. 17 · PDF p. 654–661", "Autorregulação, rim, cérebro, pele, NO e endotelina (Fig. 17.5 e 17.6)"),
    ("Guyton & Hall", "Cap. 17 · PDF p. 662–673", "Longo prazo, angiogênese, colaterais, remodelagem (Fig. 17.7 e 17.8)"),
    ("Guyton & Hall", "Cap. 17 · PDF p. 673–680", "Controle humoral e íons"),
    ("Guyton & Hall", "Cap. 18 · PDF p. 681–693", "Simpático, centro vasomotor, tônus, controle rápido (Fig. 18.1 a 18.4)"),
    ("Guyton & Hall", "Cap. 18 · PDF p. 694–709", "Barorreceptores, quimiorreceptores, reflexos atriais, isquemia do SNC (Fig. 18.5 a 18.10)"),
    ("Guyton & Hall", "Cap. 18 · PDF p. 710–713", "Compressão abdominal, ondas respiratórias e de Mayer (Fig. 18.11), leitura opcional"),
]

BASICOS = [
    ("Qual órgão tem o maior fluxo por grama de tecido?", "O **rim** (≈ 360 mL/min/100 g)."),
    ("Qual órgão recebe o maior fluxo absoluto em repouso?", "O **fígado** (≈ 1.350 mL/min, 27% do DC)."),
    ("Quanto sobe o fluxo quando o metabolismo aumenta 8 vezes?", "≈ **4 vezes**.", "g17_01"),
    ("Cite vasodilatadores metabólicos locais.", "**Adenosina**, CO₂, H⁺, K⁺, histamina, ácido láctico."),
    ("Principal vasodilatador metabólico no coração?", "**Adenosina**."),
    ("O que é hiperemia reativa?", "Aumento de **4–7 ×** do fluxo após o fim de uma oclusão arterial.", "g17_04"),
    ("O que é hiperemia ativa?", "Aumento do fluxo quando o tecido trabalha mais (músculo até **20 ×**)."),
    ("Faixa de pressão da autorregulação?", "≈ **70–175 mmHg**.", "g17_05"),
    ("Explique a teoria miogênica.", "O **estiramento** da parede abre canais de **Ca²⁺** e o músculo liso se contrai."),
    ("Mecanismo de autorregulação especial do rim?", "**Feedback tubuloglomerular** pela **mácula densa**."),
    ("Via de ação do óxido nítrico?", "**Guanilato ciclase** → **GMPc** → proteína cinase G → relaxamento.", "g17_06"),
    ("Principal estímulo para liberar NO?", "A **tensão de cisalhamento** do sangue no endotélio."),
    ("Como age a sildenafila?", "Inibe a **PDE-5**, que degrada o GMPc."),
    ("O que é a endotelina?", "Peptídeo **vasoconstritor** liberado pelo **endotélio lesado**."),
    ("Principal fator angiogênico?", "**VEGF**, estimulado pela falta de O₂."),
    ("Que remodelagem ocorre nas pequenas artérias na hipertensão?", "**Eutrófica concêntrica**: lúmen menor, mesma área de parede.", "g17_08"),
    ("Que remodelagem ocorre na artéria de uma fístula AV?", "**Eutrófica excêntrica** (lúmen maior pelo fluxo alto)."),
    ("Vasoconstritor humoral mais potente: angiotensina II ou vasopressina?", "**Vasopressina**."),
    ("Que enzima inativa a bradicinina?", "A **ECA** (enzima conversora de angiotensina)."),
    ("Efeito do simpático em cada tipo de vaso?", "Arteríolas: **mais resistência**. Veias: **menos volume** (mais retorno). Capilares: **sem inervação**."),
    ("Onde fica o centro vasomotor e quais suas áreas?", "**Bulbo e ponte inferior**: vasoconstritora, vasodilatadora e sensorial (**trato solitário**).", "g18_03"),
    ("O que é tônus vasomotor?", "Constrição parcial contínua dos vasos pelo disparo simpático de **0,5–2 impulsos/s**."),
    ("O que acontece com a PA na raquianestesia total?", "Cai de **100 para 50 mmHg** pela perda do tônus vasomotor."),
    ("Três ações simultâneas do simpático para subir a PA?", "Contrai **arteríolas**, contrai **veias** e estimula o **coração**."),
    ("Onde ficam os barorreceptores e quais nervos os levam?", "**Seio carotídeo** (Hering → IX) e **arco aórtico** (X).", "g18_05"),
    ("Resposta reflexa ao aumento da PA?", "Inibe o centro vasoconstritor e excita o vago: **vasodilatação** e **queda de FC e contratilidade**."),
    ("Faixa de resposta do seio carotídeo?", "Silencioso abaixo de **50–60 mmHg**, máximo em **≈ 180 mmHg**, mais sensível em **≈ 100**.", "g18_06"),
    ("Por que o barorreflexo pesa pouco no controle crônico?", "Os receptores **se reajustam em 1–2 dias**."),
    ("Abaixo de que PA os quimiorreceptores ficam importantes?", "**80 mmHg**."),
    ("Abaixo de que PA atua a resposta isquêmica do SNC?", "**60 mmHg** (máxima em 15–20 mmHg)."),
    ("Quais os efeitos do reflexo de volume?", "Menos simpático renal, menos **ADH** e mais **peptídeo natriurético atrial**: excreção de sódio e água.", "g18_10"),
    ("O que é o reflexo de Bainbridge?", "O **estiramento atrial aumenta a FC** (até 75%)."),
    ("O que é a reação de Cushing?", "Pressão do líquor alta comprime o cérebro; a isquemia **eleva a PA** acima da pressão do líquor."),
    ("O que causa a síncope vasovagal?", "Vasodilatação muscular + **bradicardia vagal** por emoção forte."),
]

LACUNAS = [
    ("Os rins recebem ≈ {{c1::22}}% do débito cardíaco e o fígado ≈ {{c2::27}}%.", ""),
    ("A autorregulação mantém o fluxo entre ≈ {{c1::70}} e {{c2::175}} mmHg.", ""),
    ("Na hiperemia reativa o fluxo sobe {{c1::4–7}} vezes; na ativa, no músculo, até {{c2::20}} vezes.", ""),
    ("O NO é sintetizado a partir da {{c1::arginina}} pela {{c2::eNOS}}.", ""),
    ("O NO ativa a {{c1::guanilato ciclase}}, que forma {{c2::GMPc}}.", ""),
    ("O controle agudo corrige ≈ {{c1::3/4}} do excesso de fluxo.", ""),
    ("O tônus vasoconstritor simpático é de {{c1::0,5–2}} impulsos por segundo.", ""),
    ("A raquianestesia total reduz a PA de {{c1::100}} para {{c2::50}} mmHg.", ""),
    ("Os sinais do seio carotídeo seguem pelo nervo de {{c1::Hering}} e pelo {{c2::glossofaríngeo}}; os do arco aórtico pelo {{c3::vago}}.", ""),
    ("Os barorreceptores aferentes chegam ao {{c1::núcleo do trato solitário}}.", ""),
    ("O seio carotídeo não dispara abaixo de {{c1::50–60}} mmHg e é máximo em ≈ {{c2::180}} mmHg.", ""),
    ("Os barorreceptores se reajustam em {{c1::1–2 dias}}.", ""),
    ("Os quimiorreceptores só são potentes com PA abaixo de {{c1::80}} mmHg.", ""),
    ("A resposta isquêmica do SNC atua com PA abaixo de {{c1::60}} mmHg.", ""),
]

OCLUSOES = [
    ("g17_04", "reativa", "Que fenômeno é este?", "Hiperemia reativa"),
    ("g17_04", "ativa", "Que fenômeno é este?", "Hiperemia ativa"),
    ("g17_06", (225, 95, 280, 118), "Que enzima está oculta?", "eNOS (óxido nítrico sintase endotelial)"),
    ("g17_06", "GMPc", "Que segundo mensageiro está oculto?", "GMPc"),
    ("g18_03", (325, 362, 445, 402), "Que área está oculta?", "Centro vasomotor"),
    ("g18_10", "antidiurético", "Que hormônio diminui no reflexo de volume?", "Hormônio antidiurético (ADH)"),
    ("g18_10", "natriurético", "Que hormônio aumenta com o estiramento atrial?", "Peptídeo atrial natriurético"),
    ("g18_10", "Bainbridge", "Que reflexo está oculto?", "Reflexo de Bainbridge"),
]
