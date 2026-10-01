CODIGO = "u"
SLUG = "u-semiologia-pulsos-pulso-venoso-pa"
TITULO = "Semiologia: pulsos, pulso venoso e pressão arterial"
AREA = "Semiologia"
FONTES = [
    "Porto, Semiologia Médica, 8ª ed., cap. 47 (PDF p. 569–584)",
]

ESSENCIAL = [
    "**Pulso radial:** analise parede, **frequência** (60–100), **ritmo**, **amplitude**, **tensão**, **tipo de onda** e **comparação com o outro lado**. Conte **1 minuto inteiro** e compare com a FC (**déficit de pulso**: FA e extrassístoles).",
    "**Amplitude:** **magnus** na insuficiência aórtica; **parvus** na estenose aórtica. **Pulso duro** depende da **pressão diastólica** e indica hipertensão.",
    "**Tipos de pulso:** **célere** (martelo d’água) = insuficiência aórtica, fístula AV, anemia, hipertireoidismo; **anacrótico** = estenose aórtica; **bisferiens** = EAo + IAo; **dicrótico** = febre; **alternante** = **IVE**; **filiforme** = choque; **paradoxal** = queda **> 10 mmHg** da sistólica na inspiração (tamponamento, pericardite constritiva).",
    "**Pulso venoso** (jugular) reflete o **coração direito**: ondas **A** (contração atrial), **C**, **V** (enchimento atrial) e descensos **X** (relaxamento atrial, o mais visível) e **Y** (abertura da tricúspide).",
    "**Turgência jugular a 45°** = hipertensão venosa (IVD, pericardite constritiva, compressão da cava superior). **Onda A gigante:** estenose tricúspide, BAVT, hipertensão pulmonar. **Sem X:** FA. **V gigante:** insuficiência tricúspide.",
    "**PA = DC × RP.** O DC (volume sistólico) pesa mais na **sistólica**; a **resistência periférica**, na **diastólica**; a **rigidez da aorta** do idoso eleva só a sistólica.",
    "**Técnica:** repouso **≥ 3 min**, braço na altura do coração, manguito **2 cm acima da fossa cubital**, **palpatório antes** (evita o **hiato auscultatório**), insuflar **30 mmHg acima** e desinsuflar **2–3 mmHg/s**.",
    "**Korotkoff:** **sistólica = fase I** (primeiro som); **diastólica = fase V** (desaparecimento). Se os sons vão até zero, usa-se a **fase IV** (abafamento). Manguito **estreito superestima** a PA.",
    "**Hipertensão** no consultório: **≥ 140 × 90**. MAPA: **24 h ≥ 130 × 80**, vigília > 135 × 85, sono > 120 × 70. MRPA e AMPA: > 135 × 85. Descenso noturno normal ≈ **10%**.",
]

CORPO = r'''
= Pulso radial

Palpe a artéria radial entre a apófise estiloide do rádio e os tendões flexores com as polpas do *indicador e do médio*, com o polegar no dorso do punho; use a mão direita para o pulso esquerdo do paciente e vice-versa. As características analisadas estão na #vf("t-radial").

#tabela(rotulo: "t-radial", titulo: [Características do pulso radial (Porto, cap. 47).], (auto, 1fr), ([Característica], [Normal e alterações]),
  [*Parede*], [Normal: lisa e depressível. Dura e tortuosa (“traqueia de passarinho”): *mediosclerose de Mönckeberg*, que *não* indica aterosclerose.],
  [*Frequência*], [Conte *1 minuto*. Adulto: *60–100*. Acima de 100: *taquisfigmia*; abaixo de 60: *bradisfigmia*. Compare com a FC: *déficit de pulso* (mais batimentos que pulsos) na *fibrilação atrial* e nas *extrassístoles*.],
  [*Ritmo*], [Regular ou irregular. *Arritmia sinusal* (acelera na inspiração), extrassístoles (*falhas*), BAV de 2º grau (falhas), *fibrilação atrial* (totalmente irregular). O BAV total dá pulso *lento e regular*.],
  [*Amplitude*], [*Magnus* (amplo) na *insuficiência aórtica*; *parvus* (pequeno) na *estenose aórtica*.],
  [*Tensão*], [Pressão necessária para apagar o pulso: *mole* ou *duro*. Depende da *pressão diastólica*; pulso duro indica *hipertensão*.],
  [*Comparação*], [Palpe os dois lados ao mesmo tempo. Assimetria: lesão da *crossa da aorta* ou de seus ramos.],
)

A *manobra de Osler* é positiva quando a radial continua *palpável sem pulsar* com o manguito acima da sistólica: sugere *pseudo-hipertensão* por artéria rígida, comum em idosos (baixa sensibilidade e especificidade).

#essencial(titulo: "Tipos de onda de pulso")[
  - *Célere ou martelo d’água:* surge e some rápido, por *pressão diferencial alta*: *insuficiência aórtica*, fístula AV, anemia grave, hipertireoidismo. Palpe com o braço do paciente *elevado*.
  - *Anacrótico:* pequena onda no ramo ascendente: *estenose aórtica*.
  - *Bisferiens:* duas ondulações no ápice, mais nítidas com mais compressão: *estenose + insuficiência aórtica*.
  - *Dicrótico:* onda dupla, a segunda some com compressão forte: *febre*.
  - *Alternante:* onda ampla e fraca alternadas, com *intervalos iguais*: *insuficiência ventricular esquerda* (diferente do bigeminado).
  - *Filiforme:* pequeno e mole: *colapso circulatório*.
  - *Paradoxal:* amplitude cai na *inspiração*; queda *> 10 mmHg* da sistólica na inspiração profunda: *pericardite constritiva*, *derrame pericárdico volumoso*, enfisema.
]

O *pulso capilar* é o rubor intermitente no leito ungueal com leve compressão da unha; fica nítido quando a pressão diferencial é alta (*insuficiência aórtica*, fístula AV, hipertireoidismo, anemia). Nas mesmas condições, as carótidas pulsam visivelmente: a *dança arterial*.

= Carótidas e aorta

Palpe as *carótidas* no ângulo da mandíbula, de cada lado da traqueia, comparando os dois lados ao longo de todo o trajeto. Procure endurecimento, diferença de amplitude (estenose ou oclusão) e *frêmito*. À ausculta, o sopro pode nascer na própria carótida ou ser *irradiado da estenose aórtica*.

A *aorta* é examinada por inspeção (olhar tangencial), palpação e ausculta. Um *abaulamento pulsátil multidirecional* sugere *aneurisma*: à *direita do esterno* no 2º–3º EIC (aorta ascendente), no *manúbrio* (crossa) ou no dorso (descendente). Pulsação na *fúrcula esternal* aparece no idoso (esclerose senil), na hipertensão, na insuficiência aórtica e após exercício ou emoção.

= Pulso venoso jugular

O *pulso venoso* reflete as pressões do *coração direito*. Primeiro avalie a *turgência*: as jugulares normais ficam cheias deitado e *colabam* sentado. Se continuam túrgidas com o tronco a *45°* ou sentado, há *ingurgitamento jugular*: hipertensão venosa por *insuficiência ventricular direita*, *pericardite constritiva* ou compressão da veia cava superior.

*Técnica:* paciente deitado, quase horizontal se a pressão venosa é normal ou a *45°* se elevada, cabeça um pouco virada para o lado oposto; observe a base do pescoço, entre as inserções do esternocleidomastóideo. As diferenças entre pulso venoso e arterial estão na #vf("t-venoso").

#tabela(rotulo: "t-venoso", titulo: [Pulso venoso × pulso carotídeo (Porto, cap. 47).], (1fr, 1fr), ([Pulso venoso jugular], [Pulso carotídeo]),
  [*Ondulante*: 3 ondas e 2 descensos], [*Uma onda* única, pulsátil],
  [Mais *visível* que palpável], [Mais *palpável* que visível],
  [Mais evidente *deitado*], [Igual deitado ou sentado],
  [*Colaba na inspiração*], [Não varia com a respiração],
  [*Some* ao comprimir a base do pescoço], [Não some com essa compressão],
)

O registro do pulso venoso é o *flebograma* (#vf("p47_20")). Ondas e descensos:

- *Onda A:* contração do *átrio direito* (pré-sístole, precede B1).
- *Onda C:* subida de pressão na contração isovolumétrica, ou transmissão do pulso carotídeo.
- *Descenso X* (colapso sistólico): *relaxamento atrial*; é o acidente *mais visível*.
- *Onda V:* *enchimento atrial* com a tricúspide fechada.
- *Descenso Y* (colapso diastólico): *abertura da tricúspide* e enchimento ventricular.

#fig("p47_20", largura: 5.5cm, [Flebograma. A, normal (ondas A, C, V e descensos X, Y). B, onda A gigante. C, onda V proeminente. D, pulso venoso positivo, sem descenso X. E, descenso Y profundo.])

Como o colapso X é sistólico e mais visível, o pulso normal é chamado *pulso venoso negativo*. As alterações mais importantes estão na #vf("t-ondas").

#tabela(rotulo: "t-ondas", titulo: [Alterações do pulso venoso (Porto, Fig. 47.20).], (auto, 1fr), ([Alteração], [Causas]),
  [*Onda A gigante*], [Contração vigorosa do AD contra resistência: *estenose ou atresia tricúspide*, *estenose pulmonar*, *hipertensão pulmonar grave*, *BAV total* (ondas em canhão).],
  [*Ausência do descenso X*], [*Fibrilação atrial* (não há relaxamento atrial): pulso venoso *positivo*.],
  [*Onda V gigante*], [*Insuficiência tricúspide* com fibrilação atrial.],
  [*Descenso Y profundo*], [Colapso diastólico súbito com pressão venosa muito alta: *pericardite constritiva* e *derrame pericárdico*.],
)

= Determinantes da pressão arterial

*PA = DC × RP*, e *DC = VS × FC* (≈ 5–6 L/min em repouso, até 30 L/min no exercício).

- *Débito cardíaco:* influi sobretudo na *sistólica*; por isso exercício e emoção elevam mais a sistólica, e a miocardiopatia a reduz.
- *Resistência periférica:* tônus das *arteríolas* e esfíncteres pré-capilares; principal determinante da *diastólica*. Simpático (α contrai, β dilata), angiotensina e catecolaminas (constrição), prostaglandinas e cininas (dilatação).
- *Elasticidade dos grandes vasos:* a aorta amortece a ejeção. Com a *rigidez do idoso*, sobe a *sistólica* sem subir a diastólica.
- *Volemia:* desidratação e hemorragia baixam a PA; a glomerulonefrite aguda a eleva.
- *Viscosidade:* efeito pequeno (anemia grave baixa, policitemia eleva).

Esses fatores agem uns sobre os outros (*mosaico de Page*, Fig. 47.21 do Porto), em torno da relação *perfusão tecidual = pressão / resistência*.

= Medida da pressão arterial

A medida indireta tem erro aceitável de *± 8 mmHg*; a sistólica pela ausculta da braquial é 3–4 mmHg menor que a intra-arterial. O manômetro de *mercúrio* é o padrão-ouro; o *aneroide* precisa de calibração ao menos *semestral*; o *eletrônico oscilométrico* mede a sistólica e *calcula* a diastólica.

*Manguito:* escolha pela *circunferência do braço*, não pela idade. A bolsa deve cobrir *80% do comprimento* e *40% da circunferência* do braço. Manguito *estreito* dá valor *falsamente alto*. A técnica está resumida na #vf("t-tecnica").

#tabela(rotulo: "t-tecnica", titulo: [Técnica de medida da PA pelo método auscultatório (Porto, cap. 47).], (auto, 1fr), ([Etapa], [Como fazer]),
  [*Paciente*], [Repouso de *pelo menos 3 min*, ambiente calmo, *bexiga vazia*, *1 h sem cigarro, café* ou estimulantes. Braço apoiado na altura do coração (*4º EIC*), levemente fletido, palma para cima. Anote a posição.],
  [*Manguito*], [Sobre a pele (*nunca sobre a roupa*), *2 cm acima da fossa cubital*.],
  [*Palpatório*], [Palpe a radial, insufle até o pulso sumir e desinsufle: o *reaparecimento* do pulso é a *sistólica estimada*.],
  [*Auscultatório*], [Estetoscópio sobre a braquial, insufle *30 mmHg acima* da sistólica palpatória e desinsufle a *2–3 mmHg/s*.],
  [*Repetição*], [Esvazie o manguito e espere *pelo menos 1 min* antes de repetir.],
)

Ao desinsuflar, surgem os *sons de Korotkoff* (#vf("p47_27")):

- *Fase I:* primeiro som, claro como pancada = *pressão sistólica*.
- *Fase II:* batimentos com *murmúrio*.
- *Fase III:* murmúrio some, batimentos mais acentuados.
- *Fase IV:* *abafamento* dos sons.
- *Fase V:* *desaparecimento* dos sons = *pressão diastólica*.

#fig("p47_27", largura: 4.5cm, [Escala de Korotkoff normal (A) e com hiato auscultatório (B), um intervalo silencioso no lugar da fase II.])

#essencial(titulo: "Hiato auscultatório")[
  Desaparecimento dos sons no fim da fase I e na fase II, numa faixa de *30–40 mmHg*. Pode fazer *subestimar a sistólica* ou superestimar a diastólica. Evita-se fazendo *sempre o método palpatório antes*. É comum em *idosos*.
]

Se os sons persistem até o manguito vazio, registre a *fase IV* como diastólica, por exemplo *150 × 70 × 0 mmHg*. Em situações especiais:

- *Crianças:* manguito adequado; o choro eleva a PA *até 50 mmHg*; o palpatório dá 5–10 mmHg a menos; a diastólica costuma ser a *fase IV*. Hipertensão: acima do *percentil 95* para idade, sexo e altura em 3 ocasiões.
- *Idosos:* medir em *2–3 posições* (hipotensão postural); pensar em *pseudo-hipertensão* (Osler).
- *Gestantes:* do 3º trimestre em diante, em *decúbito lateral esquerdo*; registre as fases IV e V.

A *pressão diferencial* (sistólica − diastólica) costuma ficar entre *30 e 60 mmHg*. *Convergente* (pequena): estenose aórtica, derrame pericárdico, pericardite constritiva, IC grave, hipotensão aguda. *Divergente* (grande): *insuficiência aórtica*, hipertireoidismo, fístula AV, fibrose senil dos grandes vasos.

O *pulso alternante* também se reconhece na medida: na fase I, sons fortes e fracos se alternam com intervalos iguais.

= Variações e monitorização

Fatores que mudam a PA medida:

- O *médico* obtém valores mais altos que outros profissionais (*hipertensão do avental branco*); o fim da consulta dá valores menores que o início.
- *Sono:* queda de ≈ *10%*; ao *acordar*, a PA sobe.
- *Após refeições:* discreta elevação.
- *Deitado:* PA mais alta. *De pé:* sistólica cai um pouco e diastólica sobe um pouco.
- *Emoção* e *exercício* elevam mais a sistólica.
- Erros comuns: medir sobre a roupa, sem intervalo, sem palpatório, arredondar para *0 ou 5*, manguito frouxo ou inadequado, paciente com dor, bexiga cheia ou que acabou de fumar.

A *MAPA* faz medidas por 24 h (a cada 15–20 min de dia e 20–30 min à noite) e prevê melhor a lesão de órgãos-alvo que a medida casual. Indicações: *avental branco*, hipertensão lábil, episódica ou resistente, hipotensão, disfunção autonômica, síncope e avaliação do tratamento. A #vf("p47_24") mostra os perfis de 24 h.

#fig("p47_24", largura: 5cm, [Perfis de 24 h: a, normal; b, hipertensão de consultório; c, hipertensão com queda noturna; d, hipertensão sem queda noturna.])

A *MRPA* é feita em casa por 5 dias (1º dia de orientação; *3 medidas de manhã e 3 à tarde*), mais barata, mas sem dados do sono. A *AMPA* é a automedida sem protocolo. Os limites estão na #vf("t-mapa").

#tabela(rotulo: "t-mapa", titulo: [Valores de referência para hipertensão por método (Porto, Quadro 47.11).], (1fr, auto, auto), ([Método], [PAS (mmHg)], [PAD (mmHg)]),
  [*Consultório*], [≥ 140], [≥ 90],
  [*MAPA vigília*], [> 135], [> 85],
  [*MAPA sono*], [> 120], [> 70],
  [*MAPA 24 h*], [≥ 130], [> 80],
  [*MRPA e AMPA*], [> 135], [> 85],
)

= Classificação da pressão arterial

A PA tem distribuição contínua: o limite de normalidade é o valor a partir do qual *tratar traz mais benefício que risco*. No adulto, considera-se hipertensão a PA *≥ 140 × 90 mmHg* no consultório. A classificação da 7ª Diretriz Brasileira está na #vf("t-classes").

#tabela(rotulo: "t-classes", titulo: [Classificação da PA de consultório a partir dos 18 anos (7ª Diretriz Brasileira de Hipertensão, Porto, Quadro 47.10).], (1fr, auto, auto), ([Classificação], [PAS (mmHg)], [PAD (mmHg)]),
  [*Ótima (normal)*], [≤ 120], [≤ 80],
  [*Pré-hipertensão*], [121–139], [81–89],
  [*Hipertensão estágio 1*], [140–159], [90–99],
  [*Hipertensão estágio 2*], [160–179], [100–109],
  [*Hipertensão estágio 3*], [≥ 180], [≥ 110],
  [*Hipertensão sistólica isolada*], [≥ 140], [< 90],
)

Quando PAS e PAD caem em categorias diferentes, vale a *maior*. A *pressão arterial média* (PAM) traduz a perfusão tecidual e pode ser estimada por *PAM = PAD + (PAS − PAD) / 3*; não tem uso clínico rotineiro.
'''

VALORES = [
    ("Frequência do pulso no adulto", "60–100 bpm", "Contar 1 min"),
    ("Pulso paradoxal", "Queda > 10 mmHg da PAS", "Na inspiração profunda"),
    ("DC em repouso", "5–6 L/min", "Até 30 no exercício"),
    ("Erro aceitável da medida", "± 8 mmHg", ""),
    ("Repouso antes da medida", "≥ 3 min", ""),
    ("Sem cigarro e café antes", "1 h", ""),
    ("Bolsa do manguito", "80% do comprimento", "40% da circunferência"),
    ("Manguito acima da fossa cubital", "2 cm", ""),
    ("Insuflar acima da PAS palpatória", "30 mmHg", ""),
    ("Velocidade de desinsuflação", "2–3 mmHg/s", ""),
    ("Intervalo entre medidas", "≥ 1 min", ""),
    ("Hiato auscultatório", "30–40 mmHg", ""),
    ("Choro da criança", "PA até + 50 mmHg", ""),
    ("Pressão diferencial usual", "30–60 mmHg", ""),
    ("Queda noturna normal", "≈ 10%", ""),
    ("Hipertensão no consultório", "≥ 140 × 90", ""),
    ("MAPA 24 h normal", "< 130 × 80", ""),
    ("MAPA vigília normal", "< 135 × 85", ""),
    ("MAPA sono normal", "< 120 × 70", ""),
    ("MRPA e AMPA anormais", "> 135 × 85", ""),
    ("Calibração do aneroide", "Pelo menos semestral", ""),
]

CLINICA = [
    ("Insuficiência aórtica", "Pulso **célere** (martelo d’água) e **magnus**, **pulso capilar**, **dança arterial** e **pressão divergente**."),
    ("Estenose aórtica", "Pulso **parvus** e **anacrótico**, **pressão convergente**, frêmito e sopro nas carótidas."),
    ("Tamponamento e pericardite constritiva", "**Pulso paradoxal**, **turgência jugular** e **descenso Y profundo**."),
    ("Insuficiência ventricular esquerda", "**Pulso alternante** (sons alternados na fase I de Korotkoff)."),
    ("Insuficiência ventricular direita", "**Ingurgitamento jugular a 45°**, refluxo hepatojugular, hepatomegalia e edema."),
    ("Fibrilação atrial", "Pulso irregular com **déficit de pulso** e pulso venoso **sem descenso X**."),
    ("BAV total", "Pulso lento e regular e **ondas A em canhão** na jugular."),
    ("Hipertensão do avental branco", "PA alta só no consultório; confirmar com **MAPA** ou **MRPA**."),
    ("Coarctação ou lesão da crossa", "**Assimetria** dos pulsos e da PA entre os membros."),
]

PEGADINHAS = [
    "Pulso **duro** indica PA diastólica alta, não artéria endurecida.",
    "**Mediosclerose** da radial **não** indica aterosclerose coronária.",
    "Pulso **alternante** tem intervalos **iguais**; o **bigeminado**, não.",
    "O pulso venoso normal é **negativo**: o descenso **X** é o mais visível.",
    "O pulso venoso **colaba na inspiração** e some ao comprimir a base do pescoço.",
    "Manguito **estreito** = PA **falsamente alta**.",
    "Sem o método palpatório, o **hiato auscultatório** faz **subestimar** a sistólica.",
    "Diastólica = **fase V**; só usa a **fase IV** quando os sons vão até zero.",
    "Na classificação, se PAS e PAD divergem, vale a **categoria maior**.",
    "**Deitado** a PA é mais alta que em pé.",
]

GLOSSARIO = [
    ("Taquisfigmia", "Pulso acima de 100 por minuto."),
    ("Bradisfigmia", "Pulso abaixo de 60 por minuto."),
    ("Déficit de pulso", "Menos pulsos radiais que batimentos."),
    ("Pulso magnus / parvus", "Pulso amplo / pequeno."),
    ("Pulso célere", "Martelo d’água: sobe e cai rápido."),
    ("Pulso anacrótico", "Entalhe no ramo ascendente (estenose aórtica)."),
    ("Pulso bisferiens", "Dupla onda no ápice (EAo + IAo)."),
    ("Pulso dicrótico", "Dupla onda, a segunda após o ápice (febre)."),
    ("Pulso alternante", "Ondas fortes e fracas alternadas (IVE)."),
    ("Pulso paradoxal", "Queda da amplitude na inspiração."),
    ("Pulso capilar", "Rubor pulsátil no leito ungueal."),
    ("Manobra de Osler", "Radial palpável com manguito acima da sistólica."),
    ("Flebograma", "Registro das ondas do pulso venoso."),
    ("Ingurgitamento jugular", "Jugulares túrgidas a 45° ou sentado."),
    ("Sons de Korotkoff", "Ruídos arteriais na medida auscultatória da PA."),
    ("Hiato auscultatório", "Silêncio entre as fases I e III."),
    ("Pressão diferencial", "Sistólica menos diastólica."),
    ("MAPA", "Monitorização ambulatorial da PA por 24 h."),
    ("MRPA", "Monitorização residencial da PA com protocolo."),
    ("Avental branco", "PA alta só no consultório."),
]

LEITURA = [
    ("Porto", "Cap. 47 · PDF p. 569–572", "Exame da aorta, pulso radial, tipos de pulso, pulso capilar e carótidas"),
    ("Porto", "Cap. 47 · PDF p. 572–573", "Ingurgitamento jugular e pulso venoso (Fig. 47.20)"),
    ("Porto", "Cap. 47 · PDF p. 573–575", "Determinantes e regulação da PA (Fig. 47.21)"),
    ("Porto", "Cap. 47 · PDF p. 575–579", "Esfigmomanômetros, MAPA, MRPA e AMPA (Quadros 47.8 e 47.9, Fig. 47.22 a 47.26)"),
    ("Porto", "Cap. 47 · PDF p. 579–582", "Técnica, Korotkoff, hiato auscultatório e populações especiais (Fig. 47.27)"),
    ("Porto", "Cap. 47 · PDF p. 582–584", "Fatores de variação, pressão diferencial e valores normais (Quadros 47.10 e 47.11)"),
]

BASICOS = [
    ("Com que dedos se palpa o pulso radial?", "**Indicador e médio**, com o polegar no dorso do punho."),
    ("O que é déficit de pulso e suas causas?", "Menos pulsos que batimentos: **fibrilação atrial** e **extrassístoles**."),
    ("De que depende a tensão (dureza) do pulso?", "Da **pressão diastólica**."),
    ("Pulso magnus e pulso parvus aparecem em quê?", "Magnus: **insuficiência aórtica**. Parvus: **estenose aórtica**."),
    ("Causas de pulso célere?", "**Insuficiência aórtica**, fístula AV, anemia grave, hipertireoidismo."),
    ("Pulso anacrótico e bisferiens?", "Anacrótico: **estenose aórtica**. Bisferiens: **EAo + IAo**."),
    ("Pulso alternante indica?", "**Insuficiência ventricular esquerda**."),
    ("Como se define o pulso paradoxal pela PA?", "Queda **> 10 mmHg** da sistólica na inspiração profunda."),
    ("Causas de pulso paradoxal?", "**Derrame pericárdico volumoso**, **pericardite constritiva**, enfisema."),
    ("O que é a manobra de Osler?", "Radial **palpável sem pulsar** com manguito acima da sistólica: **pseudo-hipertensão**."),
    ("O que é a dança arterial?", "Pulsação visível das carótidas por **pressão diferencial alta** (insuficiência aórtica)."),
    ("O que significa jugular túrgida a 45°?", "**Hipertensão venosa**: IVD, pericardite constritiva, compressão da cava superior."),
    ("Cinco diferenças do pulso venoso em relação ao carotídeo?", "Ondulante, **mais visível que palpável**, melhor deitado, **colaba na inspiração**, some à compressão."),
    ("Origem da onda A e da onda V?", "A: **contração atrial**. V: **enchimento atrial**.", "p47_20"),
    ("Origem dos descensos X e Y?", "X: **relaxamento atrial**. Y: **abertura da tricúspide**.", "p47_20"),
    ("Causas de onda A gigante?", "**Estenose tricúspide**, estenose pulmonar, **hipertensão pulmonar grave**, **BAVT**."),
    ("Ausência do descenso X ocorre em quê?", "**Fibrilação atrial**."),
    ("Onda V gigante indica?", "**Insuficiência tricúspide** (com FA)."),
    ("Descenso Y profundo ocorre em quê?", "**Pericardite constritiva** e derrame pericárdico."),
    ("Qual componente da PA o DC e a resistência periférica mais influenciam?", "DC: **sistólica**. Resistência: **diastólica**."),
    ("Por que o idoso tem hipertensão sistólica isolada?", "**Rigidez da aorta** eleva a sistólica sem elevar a diastólica."),
    ("Proporções da bolsa do manguito?", "**80% do comprimento** e **40% da circunferência** do braço."),
    ("Efeito de um manguito estreito?", "PA **falsamente alta**."),
    ("Onde posicionar o manguito e o braço?", "**2 cm acima da fossa cubital**, braço na altura do **coração (4º EIC)**."),
    ("Por que medir pelo método palpatório antes?", "Para estimar a sistólica e evitar o **hiato auscultatório**."),
    ("Quanto insuflar e em que velocidade desinsuflar?", "**30 mmHg** acima da sistólica palpatória; **2–3 mmHg/s**."),
    ("Que fases de Korotkoff definem PAS e PAD?", "PAS: **fase I**. PAD: **fase V**.", "p47_27"),
    ("Quando a diastólica é a fase IV?", "Quando os sons **persistem até zero** (crianças, gestantes, hipercinéticos)."),
    ("O que é o hiato auscultatório?", "Silêncio de **30–40 mmHg** entre as fases I e III.", "p47_27"),
    ("Posição para medir PA na gestante do 3º trimestre?", "**Decúbito lateral esquerdo**."),
    ("Pressão convergente e divergente: exemplos?", "Convergente: **estenose aórtica**, tamponamento. Divergente: **insuficiência aórtica**, hipertireoidismo."),
    ("Limites normais da MAPA?", "24 h **< 130 × 80**; vigília **< 135 × 85**; sono **< 120 × 70**."),
    ("Descenso noturno normal da PA?", "≈ **10%**.", "p47_24"),
    ("Limite anormal da MRPA e da AMPA?", "**> 135 × 85 mmHg**."),
    ("Limite de hipertensão no consultório?", "**≥ 140 × 90 mmHg**."),
    ("Faixas de hipertensão estágio 1, 2 e 3?", "**140–159/90–99**; **160–179/100–109**; **≥ 180/110**."),
]

LACUNAS = [
    ("A frequência normal do pulso no adulto é de {{c1::60}} a {{c2::100}} por minuto.", ""),
    ("O pulso em martelo d’água é o pulso {{c1::célere}}, típico da {{c2::insuficiência aórtica}}.", ""),
    ("O pulso {{c1::alternante}} é sinal de insuficiência ventricular esquerda.", ""),
    ("No pulso paradoxal a sistólica cai mais de {{c1::10}} mmHg na inspiração.", ""),
    ("A onda A do pulso venoso resulta da {{c1::contração atrial}}.", ""),
    ("O descenso Y resulta da abertura da valva {{c1::tricúspide}}.", ""),
    ("Na fibrilação atrial falta o descenso {{c1::X}} do pulso venoso.", ""),
    ("A bolsa do manguito deve cobrir {{c1::80}}% do comprimento e {{c2::40}}% da circunferência do braço.", ""),
    ("O manguito fica {{c1::2}} cm acima da fossa cubital.", ""),
    ("Desinsufla-se o manguito a {{c1::2–3}} mmHg por segundo.", ""),
    ("A pressão sistólica é a fase {{c1::I}} e a diastólica, a fase {{c2::V}} de Korotkoff.", ""),
    ("O hiato auscultatório pode cobrir {{c1::30–40}} mmHg.", ""),
    ("A média normal da MAPA de 24 h é menor que {{c1::130 × 80}} mmHg.", ""),
    ("Hipertensão estágio 1 é PAS de {{c1::140–159}} ou PAD de {{c2::90–99}} mmHg.", ""),
]

OCLUSOES = [
    ("p47_27", "Hiato auscultatório", "Que fenômeno é este intervalo silencioso?", "Hiato auscultatório"),
    ("p47_27", "Desaparecimento dos sons", "O que marca a pressão diastólica?", "Desaparecimento dos sons (fase V)"),
    ("p47_27", "Primeiro som", "O que marca a pressão sistólica?", "Primeiro som (fase I)"),
]
