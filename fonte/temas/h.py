CODIGO = "h"
SLUG = "h-regulacao-renal-da-pa"
TITULO = "Regulação renal da pressão arterial"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 19 (PDF p. 716–769)",
]

ESSENCIAL = [
    "**Longo prazo = rim-volume.** PA alta → **diurese e natriurese por pressão** → volume cai → PA volta. Ganho por feedback **quase infinito**: a PA volta exatamente ao ponto de equilíbrio.",
    "**Ponto de equilíbrio:** cruzamento da **curva de débito renal** com a linha de **ingestão de sal e água**. Só dois determinantes mudam a PA de longo prazo: **deslocar a curva renal** ou **mudar a ingestão**.",
    "A curva **crônica** é muito mais **íngreme** que a aguda (simpático, angiotensina II e aldosterona caem quando a PA sobe). Por isso a maioria das pessoas é **insensível ao sal**.",
    "Aumentar a **resistência periférica total fora do rim** não sustenta hipertensão: em 1–2 dias o rim normaliza a PA. O que importa é a **resistência renal**.",
    "**Hipertensão por volume:** primeiro sobe o **DC**; depois a **autorregulação** normaliza o DC e eleva a **RPT**. A RPT alta é **efeito**, não causa.",
    "**Renina** (células **justaglomerulares**) ← PA baixa, pouco NaCl na **mácula densa**, simpático (**β1**). Angiotensinogênio → **Ang I** (10 aa) → **ECA (pulmão)** → **Ang II** (8 aa).",
    "**Ang II:** vasoconstrição (rápida, ≈ 20 min para efeito pleno) e **retenção renal de sal e água** (direta + **aldosterona**), o efeito mais potente a longo prazo.",
    "**Goldblatt:** estenose da artéria renal → renina → hipertensão. **Hipertensão essencial** (90–95%): obesidade, simpático renal, Ang II/aldosterona e natriurese por pressão prejudicada.",
]

CORPO = r'''
= Sistema rim-volume

O controle da PA a longo prazo depende do *volume de líquido* do corpo, que resulta do equilíbrio entre ingestão e eliminação de sal e água. Se o volume de sangue aumenta e a capacitância dos vasos não muda, a PA sobe; a PA alta faz o rim *excretar* o excesso, e a PA volta ao normal.

- *Diurese por pressão:* poucos mmHg a mais podem *dobrar* a eliminação de água.
- *Natriurese por pressão:* o mesmo para o sódio.

A *curva de débito renal* (#vf("g19_01")) mostra que com PA de *50 mmHg* o débito urinário é quase zero; com 100 mmHg é normal; com 200 mmHg é *4 a 6 vezes* o normal.

#fig("g19_01", largura: 6cm, [Curva de débito renal de sal e água em função da PA e linha de ingestão. A é o ponto de equilíbrio; em B (150 mmHg) a eliminação é ≈ 3 vezes a ingestão.])

Num cão sem reflexos nervosos, a infusão de 400 mL de sangue elevou a PA a 205 mmHg e o débito urinário 12 vezes, e tudo voltou ao normal em ≈ 1 hora.

== Ponto de equilíbrio e ganho infinito

A longo prazo, *eliminação = ingestão*. Isso só acontece no cruzamento da curva renal com a linha de ingestão: o *ponto de equilíbrio* (A).

- PA acima do equilíbrio: o rim elimina mais do que entra, o volume cai e a PA desce *até exatamente* o ponto A.
- PA abaixo: entra mais do que sai, o volume sobe e a PA volta ao ponto A.

Esse retorno completo é o *ganho por feedback quase infinito* do sistema rim-volume. Nenhum mecanismo nervoso corrige 100% do erro.

#essencial(titulo: "Dois determinantes da PA a longo prazo")[
  *1. A posição da curva de débito renal* no eixo da pressão. *2. O nível de ingestão de sal e água.* Sem mudar um deles, é impossível mudar a PA de longo prazo.
]

A #vf("g19_03") mostra os dois casos: uma doença renal que desloca a curva 50 mmHg para a direita eleva a PA em 50 mmHg; quadruplicar a ingestão, numa curva pouco íngreme, eleva a PA a 160 mmHg.

#fig("g19_03", largura: 5.5cm, [Duas formas de elevar a PA: A, deslocar a curva renal para a direita; B, aumentar a ingestão de sal e água.])

== Curva crônica e sensibilidade ao sal

A curva renal *crônica* é muito mais *íngreme* que a aguda (#vf("g19_04")). Quando a PA sobe, além do efeito direto no rim, *caem* o simpático, a angiotensina II e a aldosterona, que retêm sal. Por isso, com rins normais, aumentar a ingestão de sal *6 vezes* (ou reduzir a 1/6) quase não muda a PA: a pessoa é *insensível ao sal*.

#fig("g19_04", largura: 6.5cm, [Curvas de débito renal aguda e crônica. A e B são os equilíbrios com ingestão normal e 6 vezes maior.])

Ficam *sensíveis ao sal* (curva achatada, como a aguda) os que têm *perda de néfrons* (lesão renal, hipertensão, diabetes, envelhecimento) ou *excesso de hormônios antinatriuréticos* (angiotensina II, aldosterona).

== Resistência periférica e volume

*PA = DC × RPT*, mas aumentar a *RPT fora dos rins* não mantém a PA alta: em 1–2 dias a diurese e a natriurese por pressão normalizam a PA. Em fístula AV, beribéri, hipotireoidismo ou amputação, a RPT muda muito e a PA fica normal; quem varia é o DC. Quando a RPT alta causa hipertensão, é porque a *resistência renal* subiu junto.

O aumento do volume eleva a PA pela sequência da #vf("g19_06"): mais líquido extracelular → mais volume plasmático → mais *pressão média de enchimento* → mais retorno venoso → mais *DC* → mais PA. O DC também sobe a PA *indiretamente*, porque o fluxo excessivo faz os tecidos se *autorregularem* e aumentarem a RPT. Um DC só 5–10% maior pode elevar a PA de 100 para 150 mmHg.

#fig("g19_06", largura: 5.5cm, [Etapas pelas quais o aumento do volume extracelular eleva a PA, com o efeito direto do DC e o indireto pela autorregulação.])

*Sal × água:* o *sal* eleva mais a PA que a água, porque a água pura é excretada rápido. O sal acumulado aumenta a osmolaridade, que estimula a *sede* e o *ADH*, e assim aumenta o volume extracelular.

= Hipertensão por sobrecarga de volume

Hipertensão é PA média *> 110 mmHg* (normal ≈ 90), ou seja, diastólica > ≈ 90 e sistólica > ≈ 135 mmHg. Ela mata por *insuficiência cardíaca e doença coronariana*, por *AVC* e por *insuficiência renal*.

Em cães com só *30% da massa renal*, a PA subiu apenas 6 mmHg com água; ao beber *solução salina*, subiu ≈ 40 mmHg em poucos dias e voltou ao normal 2 dias após voltar à água.

#essencial(titulo: "Duas fases da hipertensão por volume")[
  *1ª fase (dias):* volume extracelular, volume plasmático e *DC sobem 20–40%*; a RPT até cai no início (barorreflexo), mas os barorreceptores se reajustam em 2–4 dias. *2ª fase (semanas):* a *autorregulação* traz o DC e o volume de volta quase ao normal e a *RPT sobe ≈ 33%*. A PA fica alta. A *RPT alta é consequência*, não causa.
]

O mesmo acontece em pacientes em *diálise* que acumulam volume e no *hiperaldosteronismo primário* (tumor adrenal que secreta aldosterona e retém sal e água).

= Sistema renina-angiotensina

A *renina* é uma *enzima* (não é vasoativa) produzida e armazenada nas *células justaglomerulares*, músculo liso modificado da parede da *arteríola aferente*. A cascata está na #vf("g19_09").

#fig("g19_09", largura: 5cm, [Mecanismo vasoconstritor renina-angiotensina.])

*Estímulos para liberar renina:*
- *queda da pressão* sentida pelos barorreceptores das próprias células justaglomerulares;
- *menos NaCl* chegando à *mácula densa* (início do túbulo distal);
- *simpático*, por receptores *β-adrenérgicos* das células justaglomerulares.

*A cascata:*
- A renina age sobre o *angiotensinogênio* (substrato de renina) e libera a *angiotensina I* (10 aminoácidos, pouco ativa). A renina dura *30–60 min* no sangue.
- A *ECA* (enzima conversora), presente sobretudo no *endotélio pulmonar*, retira 2 aminoácidos e forma a *angiotensina II* (8 aminoácidos).
- A angiotensina II dura só *1–2 min*: é inativada pelas *angiotensinases*.

== Efeitos da angiotensina II

- *Vasoconstrição:* intensa nas *arteríolas* (aumenta a RPT) e leve nas *veias* (aumenta o retorno venoso). É rápida.
- *Retenção renal de sal e água*, efeito *mais potente a longo prazo*. *Direta:* contrai a *arteríola eferente*, reduz o fluxo e a pressão nos capilares peritubulares e aumenta a reabsorção; age também nos túbulos. *Indireta:* é um dos estímulos mais potentes da *aldosterona*. Juntas, podem reduzir a urina a menos de 1/5 do normal.

Após hemorragia que levou a PA a 50 mmHg, ela voltou a *83 mmHg* com o sistema ativo e só a 60 mmHg com a renina bloqueada (#vf("g19_10")). O sistema leva ≈ *20 min* para ficar totalmente ativo, mais devagar que os reflexos nervosos.

#fig("g19_10", largura: 7cm, [Recuperação da PA após hemorragia com e sem o sistema renina-angiotensina.])

A angiotensina II *desloca a curva de débito renal para a direita* (#vf("g19_11")). Com angiotensina zero (inibidor da ECA) o equilíbrio fica em *75 mmHg*; com angiotensina 2,5 vezes o normal, em *115 mmHg*.

#fig("g19_11", largura: 6.5cm, [Curvas de débito renal com angiotensina II bloqueada (0) e 2,5 vezes o normal, com os pontos de equilíbrio.])

== Ingestão de sal

O sistema renina-angiotensina é o que mais permite variar o sal *sem mudar a PA*. Mais sal eleva um pouco o volume e a PA, o que *suprime a renina* e a angiotensina II; o rim então elimina o sal extra.

- Com o sistema normal, aumentar o sal *até 100 vezes* sobe a PA só *4–6 mmHg*.
- Se a angiotensina II não pode cair (infusão contínua), o mesmo aumento sobe a PA *40 mmHg ou mais*.
- Se a angiotensina II é bloqueada (inibidor da ECA), a PA *cai muito* quando se reduz o sal.

= Hipertensão renovascular

*Goldblatt de rim único:* um rim é retirado e o outro tem a artéria pinçada (#vf("g19_14")). A pressão distal ao grampo cai, a *renina* dispara (pico em 1–2 h) e a angiotensina II sobe a PA em minutos. Depois, a *retenção de sal e água* eleva a PA ainda mais em 5–7 dias, até a pressão distal ao grampo voltar ao normal; aí a renina volta ao normal, mas a hipertensão fica.

#fig("g19_14", largura: 5cm, [Hipertensão de rim único de Goldblatt: PA sistêmica, pressão renal distal ao grampo e secreção de renina.])

- *Goldblatt de dois rins:* só um rim tem a artéria estreitada. Ele retém sal pela pressão baixa e secreta renina; a angiotensina II e a aldosterona fazem o rim *normal* também reter sal. Corresponde à *hipertensão renovascular* (estenose aterosclerótica de uma artéria renal).
- *Doença renal isquêmica focal:* áreas isquêmicas secretam renina; causa comum em idosos.
- *Tumor de células justaglomerulares* (secretor de renina): hipertensão grave.
- *Coarctação da aorta:* constrição acima das artérias renais. PA dos *membros superiores* 40–50% maior que a dos inferiores. O mecanismo é o do Goldblatt; o fluxo nos braços e nas pernas fica normal pela *autorregulação*.
- *Pré-eclâmpsia* (5–10% das gestantes): a placenta isquêmica libera fatores que lesam o endotélio, há menos NO, menos filtração glomerular e natriurese por pressão prejudicada.

*Hipertensão neurogênica:* cortar os nervos dos barorreceptores ou destruir o trato solitário eleva a PA de 100 para 160 mmHg, mas ela volta ao normal em ≈ 2 dias. É *aguda*, não crônica.

*Monogênica:* rara (< 1%); em todas as formas a via final é *prejuízo da função renal*.

= Hipertensão essencial

*90–95%* dos hipertensos têm *hipertensão primária (essencial)*, de causa desconhecida. O excesso de peso responde por *65–75%* do risco. Na obesidade:

- o *DC* aumenta (mais tecido para irrigar e mais metabolismo);
- a *atividade simpática renal* aumenta (leptina, menor sensibilidade dos barorreceptores, quimiorreceptores e apneia do sono);
- *angiotensina II e aldosterona* aumentam;
- a *natriurese por pressão* fica prejudicada: se a PA de quem tem 150 mmHg cair de repente a 100, há *anúria quase total*.

Os hipertensos essenciais têm a curva renal *deslocada para a direita*. Os *insensíveis ao sal* quase não mudam a PA com mais sal; nos *sensíveis ao sal*, mais sal piora muito a PA. A sensibilidade ao sal aumenta com a *idade* (perda de néfrons após os 50–60 anos).

*Tratamento:* primeiro *perda de peso e atividade física*. Depois, *vasodilatadores* (inibem o simpático renal, relaxam os vasos renais ou bloqueiam o sistema renina-angiotensina-aldosterona) e *diuréticos/natriuréticos*. Todos melhoram a natriurese por pressão.

= Integração dos mecanismos

A #vf("g19_16") mostra a potência de cada mecanismo ao longo do tempo depois de uma mudança brusca da PA, e a #vf("t-tempos") os agrupa: os reflexos nervosos garantem a sobrevivência na emergência, os mecanismos intermediários sustentam a PA e o *rim* define o nível final de longo prazo.

#fig("g19_16", largura: 7cm, [Ganho de cada mecanismo de controle da PA em segundos, minutos, horas e dias. O rim-volume tem ganho quase infinito.])

#tabela(rotulo: "t-tempos", titulo: [Mecanismos de controle da PA por tempo de ação.], (auto, 1fr), ([Tempo], [Mecanismos]),
  [*Segundos*], [Nervosos: *barorreceptores*, *quimiorreceptores* e *resposta isquêmica do SNC*. Rápidos e potentes, mas perdem força em horas a dias.],
  [*Minutos a horas*], [*Renina-angiotensina* (vasoconstrição), *relaxamento por estresse* dos vasos e *deslocamento de líquido* pelos capilares. Pesam após 30 min a horas.],
  [*Dias a anos*], [*Rim-volume* (diurese e natriurese por pressão), modulado pela *aldosterona* e pela angiotensina II. *Ganho quase infinito.*],
)

'''

VALORES = [
    ("Débito urinário com PA de 50 mmHg", "≈ 0", ""),
    ("Débito urinário com PA de 200 mmHg", "4–6 × o normal", ""),
    ("Infusão de 400 mL (cão sem reflexos)", "PA 205 mmHg; urina × 12", "Normal em ≈ 1 h"),
    ("Eliminação com PA de 150 mmHg", "≈ 3 × a ingestão", "Ponto B"),
    ("Sal × 6 com curva crônica normal", "PA quase igual", "Insensível ao sal"),
    ("Hipertensão", "PA média > 110 mmHg", "PAD > 90, PAS > 135"),
    ("PA média normal (Guyton)", "≈ 90 mmHg", ""),
    ("Hipertensão grave", "PA média 150–170", "PAD até 130, PAS até 250"),
    ("Cão com 30% de rim + salina", "PA + 40 mmHg", "Só com água: + 6"),
    ("Hipertensão por volume, 1ª fase", "DC e volume + 20–40%", ""),
    ("Hipertensão por volume, semanas", "RPT + 33%; PA + 40%", "DC quase normal"),
    ("Ang I / Ang II", "10 / 8 aminoácidos", ""),
    ("Meia-vida: renina / Ang II", "30–60 min / 1–2 min", ""),
    ("Renina-angiotensina pleno", "≈ 20 min", ""),
    ("Hemorragia (PA 50)", "Volta a 83 com o sistema", "60 sem o sistema"),
    ("Equilíbrio com Ang II zero / 2,5 ×", "75 / 115 mmHg", ""),
    ("Sal × 100 com sistema normal", "PA + 4–6 mmHg", "Com Ang II fixa: + 40"),
    ("Goldblatt: pico de renina", "1–2 h", "Normaliza em 5–7 dias"),
    ("Coarctação da aorta", "MMSS 40–50% > MMII", ""),
    ("Pré-eclâmpsia", "5–10% das gestantes", ""),
    ("Hipertensão essencial", "90–95% dos casos", "Peso: 65–75% do risco"),
    ("Hipertensão monogênica", "< 1%", ""),
    ("Secção dos barorreceptores", "PA 100 → 160", "Normal em ≈ 2 dias"),
]

CLINICA = [
    ("Inibidores da ECA e BRA", "Bloqueiam a angiotensina II: **deslocam a curva renal para a esquerda** e baixam a PA. Com dieta pobre em sal, a PA cai ainda mais."),
    ("Estenose de artéria renal", "Hipertensão **renovascular**: renina alta. Inibidor da ECA pode piorar a filtração do rim estenosado, que depende da Ang II na arteríola eferente."),
    ("Hiperaldosteronismo primário", "Tumor adrenal: aldosterona alta, **renina suprimida**, retenção de sódio e hipertensão (com hipocalemia)."),
    ("Coarctação da aorta", "PA alta nos **braços** e baixa nas **pernas**, pulsos femorais fracos; mecanismo semelhante ao Goldblatt."),
    ("Obesidade e hipertensão", "Simpático renal, Ang II e aldosterona elevados prejudicam a natriurese. **Perda de peso** é o primeiro tratamento."),
    ("Doença renal crônica", "A perda de néfrons achata a curva renal: a PA fica **sensível ao sal**; restringir sal ajuda."),
    ("Diálise", "Se o volume não é retirado na diálise, surge hipertensão por **sobrecarga de volume**."),
]

PEGADINHAS = [
    "Quem define a PA a **longo prazo** é o **rim** (ganho infinito), não os barorreceptores.",
    "Aumentar a **RPT fora do rim** não causa hipertensão crônica: o rim normaliza a PA em 1–2 dias.",
    "Na hipertensão por volume a **RPT alta é consequência** (autorregulação), não causa.",
    "A **renina é uma enzima**, não um vasoconstritor. Quem contrai é a **angiotensina II**.",
    "A ECA está sobretudo no **pulmão** e também **degrada a bradicinina**.",
    "O efeito mais potente da Ang II a longo prazo é a **retenção de sal e água**, não a vasoconstrição.",
    "A Ang II contrai mais a arteríola **eferente**.",
    "No Goldblatt, a renina **volta ao normal** em 5–7 dias, mas a hipertensão **persiste** (volume).",
    "Com rins e renina-angiotensina normais, a maioria é **insensível ao sal**.",
    "**Sal** eleva mais a PA que **água** pura.",
]

GLOSSARIO = [
    ("Diurese por pressão", "Aumento do débito urinário com a PA."),
    ("Natriurese por pressão", "Aumento da excreção de sódio com a PA."),
    ("Curva de débito renal", "Eliminação de sal e água em função da PA."),
    ("Ponto de equilíbrio", "PA em que a eliminação renal iguala a ingestão."),
    ("Ganho infinito", "Correção completa do erro pelo sistema rim-volume."),
    ("Sensibilidade ao sal", "Elevação da PA com o aumento da ingestão de sal."),
    ("Células justaglomerulares", "Células da arteríola aferente que secretam renina."),
    ("Mácula densa", "Células do túbulo distal que sentem o NaCl."),
    ("Angiotensinogênio", "Substrato da renina, produzido no fígado."),
    ("ECA", "Enzima conversora de angiotensina I em II."),
    ("Angiotensinases", "Enzimas que inativam a angiotensina II."),
    ("Goldblatt", "Hipertensão por constrição da artéria renal."),
    ("Hipertensão renovascular", "Hipertensão por estenose de artéria renal."),
    ("Hipertensão essencial", "Hipertensão de causa desconhecida (primária)."),
    ("Relaxamento por estresse", "Distensão lenta dos vasos que tampona a pressão."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 19 · PDF p. 716–731", "Rim-volume, diurese por pressão, equilíbrio, curva crônica, RPT, volume e sal (Fig. 19.1 a 19.6)"),
    ("Guyton & Hall", "Cap. 19 · PDF p. 732–739", "Hipertensão por sobrecarga de volume e aldosterona (Fig. 19.7 e 19.8)"),
    ("Guyton & Hall", "Cap. 19 · PDF p. 739–749", "Sistema renina-angiotensina (Fig. 19.9 a 19.13)"),
    ("Guyton & Hall", "Cap. 19 · PDF p. 750–759", "Goldblatt, coarctação, pré-eclâmpsia, neurogênica, genética (Fig. 19.14)"),
    ("Guyton & Hall", "Cap. 19 · PDF p. 759–764", "Hipertensão essencial e tratamento (Fig. 19.15)"),
    ("Guyton & Hall", "Cap. 19 · PDF p. 764–768", "Integração dos sistemas de controle (Fig. 19.16)"),
]

BASICOS = [
    ("Qual o principal mecanismo de controle da PA a longo prazo?", "O sistema **rim-volume** (diurese e natriurese por pressão)."),
    ("O que é diurese por pressão?", "Aumento do débito urinário quando a PA sobe.", "g19_01"),
    ("O que define o ponto de equilíbrio da PA a longo prazo?", "O cruzamento da **curva de débito renal** com a linha de **ingestão** de sal e água."),
    ("Por que o ganho do sistema rim-volume é quase infinito?", "Ele só para de agir quando a PA volta **exatamente** ao ponto de equilíbrio."),
    ("Quais os dois determinantes da PA a longo prazo?", "**Posição da curva de débito renal** e **ingestão de sal e água**.", "g19_03"),
    ("Por que a curva renal crônica é mais íngreme?", "A PA alta também **reduz simpático, Ang II e aldosterona**.", "g19_04"),
    ("Quem fica sensível ao sal?", "Quem tem **perda de néfrons** ou **excesso de Ang II/aldosterona**."),
    ("Aumentar a RPT fora do rim causa hipertensão crônica?", "**Não**: o rim normaliza a PA em 1–2 dias."),
    ("Sequência pela qual mais volume eleva a PA?", "Volume → **PES** → retorno venoso → **DC** → PA (e autorregulação → RPT).", "g19_06"),
    ("Por que o sal eleva mais a PA que a água?", "O sal aumenta a osmolaridade → **sede** e **ADH** → mais volume; a água pura é excretada rápido."),
    ("Definição de hipertensão pelo Guyton?", "PA média **> 110 mmHg** (PAD > 90 e PAS > 135)."),
    ("Três modos pelos quais a hipertensão mata?", "**Coração** (IC, coronariopatia), **AVC** e **insuficiência renal**."),
    ("Descreva as duas fases da hipertensão por volume.", "1ª: **DC e volume altos**. 2ª: autorregulação normaliza o DC e **eleva a RPT**."),
    ("Onde é produzida a renina?", "Nas **células justaglomerulares** da arteríola aferente."),
    ("Três estímulos para a liberação de renina?", "**PA baixa** no rim, **pouco NaCl na mácula densa** e **simpático (β)**."),
    ("Descreva a cascata renina-angiotensina.", "Angiotensinogênio → (renina) → **Ang I** → (**ECA**, pulmão) → **Ang II**.", "g19_09"),
    ("Dois efeitos principais da Ang II na PA?", "**Vasoconstrição** (rápida) e **retenção renal de sal e água** (lenta, mais potente)."),
    ("Como a Ang II retém sal diretamente no rim?", "Contrai a **arteríola eferente**, reduz a pressão peritubular e age nos túbulos."),
    ("Quanto tempo o sistema renina-angiotensina leva para ficar pleno?", "≈ **20 min**.", "g19_10"),
    ("Efeito da Ang II na curva de débito renal?", "Desloca para a **direita** (equilíbrio 75 → 115 mmHg).", "g19_11"),
    ("Por que a PA quase não muda com 100 × mais sal?", "O sal **suprime a renina** e a Ang II, e o rim elimina o excesso."),
    ("Mecanismo da hipertensão de Goldblatt de rim único?", "**Renina** (fase aguda) e depois **retenção de sal e água**.", "g19_14"),
    ("O que é a hipertensão de Goldblatt de dois rins?", "Estenose de **uma** artéria renal: a renina faz o rim **normal** também reter sal (renovascular)."),
    ("Por que a coarctação da aorta causa hipertensão nos braços?", "Os rins ficam distais à constrição e liberam **renina**, como no Goldblatt."),
    ("Mecanismo da hipertensão na pré-eclâmpsia?", "Placenta isquêmica → **disfunção endotelial** → menos NO, menos filtração, natriurese prejudicada."),
    ("Por que a hipertensão neurogênica por secção dos barorreceptores é aguda?", "O centro vasomotor se **reajusta** em ≈ 2 dias."),
    ("Principal fator de risco da hipertensão essencial?", "**Excesso de peso** (65–75% do risco)."),
    ("Mecanismos ligando obesidade e hipertensão?", "**Simpático renal**, **Ang II/aldosterona** altos e **natriurese por pressão** prejudicada."),
    ("Mecanismos de controle da PA em segundos, minutos e dias?", "**Nervosos**; **renina-angiotensina**, relaxamento por estresse, desvio capilar; **rim-volume**.", "g19_16"),
]

LACUNAS = [
    ("Com PA de {{c1::50}} mmHg o débito urinário é quase zero; com 200 mmHg é {{c2::4–6}} vezes o normal.", ""),
    ("O sistema rim-volume tem ganho por feedback {{c1::quase infinito}}.", ""),
    ("Os dois determinantes da PA a longo prazo são a {{c1::curva de débito renal}} e a {{c2::ingestão de sal e água}}.", ""),
    ("Na hipertensão por volume, primeiro sobe o {{c1::débito cardíaco}} e depois a {{c2::resistência periférica total}}.", ""),
    ("A renina é secretada pelas células {{c1::justaglomerulares}} da arteríola {{c2::aferente}}.", ""),
    ("A angiotensina I tem {{c1::10}} aminoácidos e a angiotensina II, {{c2::8}}.", ""),
    ("A ECA está sobretudo no endotélio {{c1::pulmonar}}.", ""),
    ("A angiotensina II dura {{c1::1–2}} min no sangue; a renina, {{c2::30–60}} min.", ""),
    ("A angiotensina II contrai principalmente a arteríola {{c1::eferente}}.", ""),
    ("Com angiotensina II zero o equilíbrio da PA fica em ≈ {{c1::75}} mmHg; com 2,5 × o normal, em ≈ {{c2::115}} mmHg.", ""),
    ("A hipertensão essencial corresponde a {{c1::90–95}}% dos casos.", ""),
    ("Hipertensão pelo Guyton: PA média > {{c1::110}} mmHg.", ""),
]

OCLUSOES = [
    ("g19_01", (115, 180, 205, 222), "Que ponto é este?", "Ponto de equilíbrio"),
    ("g19_04", "Crônico", "Que curva é esta?", "Curva renal crônica"),
    ("g19_09", "Renina", "O que está oculto?", "Renina (rim)"),
    ("g19_09", (162, 208, 280, 232), "O que está oculto?", "Angiotensina I"),
    ("g19_09", (228, 255, 315, 310), "Que enzima está oculta?", "Enzima de conversão (pulmão)"),
    ("g19_09", "Angiotensinase", "Que enzimas inativam a Ang II?", "Angiotensinases"),
    ("g19_06", "Autorregulação", "Que mecanismo está oculto?", "Autorregulação"),
    ("g19_16", (343, 28, 442, 212), "Que mecanismo tem ganho quase infinito?", "Controle de pressão rim-volume plasmático"),
    ("g19_16", "Barorreceptores", "Que mecanismo é este?", "Barorreceptores"),
    ("g19_16", (350, 258, 440, 282), "Que mecanismo é este?", "Aldosterona"),
]
