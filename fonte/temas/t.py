CODIGO = "t"
SLUG = "t-semiologia-precordio-bulhas-sopros"
TITULO = "Semiologia: precórdio, bulhas e sopros"
AREA = "Semiologia"
FONTES = [
    "Porto, Semiologia Médica, 8ª ed., cap. 47 (PDF p. 550–556 e 560–569)",
]

ESSENCIAL = [
    "**Ictus cordis:** 5º EIC na linha hemiclavicular esquerda (mediolíneo), **1–2 polpas digitais**, desloca **1–2 cm** com o decúbito. **Difuso** (≥ 3 polpas) = **dilatação**; **propulsivo** = **hipertrofia**. Deslocado para baixo e para fora = **VE**.",
    "**Hipertrofia do VD** não desloca o ictus: dá **levantamento em massa** paraesternal, **retração sistólica apical** e **pulsação epigástrica**.",
    "**Focos:** mitral = 5º EIC LHCE (ictus); tricúspide = base do apêndice xifoide; pulmonar = 2º EIC esquerdo; aórtico = 2º EIC direito; **aórtico acessório = 3º–4º EIC esquerdo**. Não coincidem com a projeção das valvas.",
    "**B1** = fechamento **mitral e tricúspide**, coincide com o **ictus e o pulso carotídeo** (TUM). **B2** = fechamento **aórtico e pulmonar** (TA); **desdobra na inspiração** (fisiológico).",
    "**B3:** protodiastólica, **enchimento rápido**, baixa frequência (campânula, DLE); normal em crianças e jovens. **B4:** pré-sistólica, **contração atrial** contra ventrículo **pouco complacente**.",
    "**Galope ventricular** (B3 patológica) = **sofrimento miocárdico / IC**, o “grito de socorro do miocárdio”. **Galope atrial** (B4): HAS grave, coronariopatia (disfunção diastólica).",
    "**Desdobramentos de B2:** **constante e variável** = **BRD**; **fixo** = **CIA**; **paradoxal** (na expiração) = **BRE** ou estenose aórtica grave.",
    "**Sopro sistólico de ejeção** (estenose aórtica/pulmonar): começa **após B1**, **crescendo-decrescendo**, termina antes de B2. **De regurgitação** (IM, IT, CIV): **holossistólico**, **mascara B1**.",
    "**Estenose mitral:** B1 hiperfonética, **estalido de abertura** e **ruflar diastólico** com reforço pré-sistólico, melhor em **DLE com campânula**. **Insuficiência aórtica:** sopro **protodiastólico aspirativo**, melhor **sentado e inclinado para frente**.",
    "**Irradiação:** estenose aórtica → **pescoço**; insuficiência mitral → **axila**. **Rivero-Carvallo:** sopro que **aumenta na inspiração** é **tricúspide**.",
]

CORPO = r'''
= Inspeção e palpação do precórdio

Inspeção e palpação são feitas juntas, com o paciente em decúbito dorsal e o examinador à sua *direita*. Procure *abaulamento*, analise o *ictus cordis*, outros *batimentos* e *frêmitos*.

*Abaulamento precordial* sugere aneurisma da aorta, cardiomegalia ou derrame pericárdico. Em crianças, cuja parede é flexível, é quase sempre por *dilatação do VD* (cardiopatias congênitas e reumáticas), a câmara que forma a face anterior do coração.

O *ictus cordis* (choque da ponta) é avaliado quanto a localização, extensão, mobilidade, intensidade e tipo de impulsão (#vf("t-ictus")).

#tabela(rotulo: "t-ictus", titulo: [Análise do ictus cordis (Porto, cap. 47).], (auto, 1fr), ([Parâmetro], [Normal e alterações]),
  [*Localização*], [*Mediolíneo:* 5º EIC na linha hemiclavicular esquerda. *Brevilíneo:* 4º EIC, ≈ 2 cm para fora. *Longilíneo:* 6º EIC, 1–2 cm para dentro. Desvio para baixo e para fora indica *dilatação e/ou hipertrofia do VE*. Pode ser impalpável no enfisema, na obesidade e com mamas grandes.],
  [*Extensão*], [Normal: *1–2 polpas digitais*. Hipertrofia: *3 ou mais*; grande dilatação: a palma inteira.],
  [*Mobilidade*], [Desloca *1–2 cm* nos decúbitos laterais. *Não se desloca* na *sínfise pericárdica*.],
  [*Intensidade e tipo*], [Mais forte em magros, após exercício e no hipertireoidismo. *Difuso* (≥ 3 polpas) indica *dilatação*; *propulsivo* (levanta a mão) indica *hipertrofia*.],
)

#essencial(titulo: "Hipertrofia do VE × do VD")[
  *VE com dilatação* (insuficiência aórtica): ictus no 6º–8º EIC, até a linha axilar anterior, *difuso e propulsivo*. *VE sem dilatação* (hipertensão, estenose aórtica): ictus pouco deslocado, até 2 polpas, *propulsivo*. *VD:* não muda o ictus; dá *levantamento em massa* paraesternal (impulsão sistólica), *retração sistólica apical* e *pulsação epigástrica*.
]

Outros achados palpáveis:

- *Choque valvar:* bulha hiperfonética sentida pela mão.
- *Pulsação epigástrica:* transmissão da aorta, ou *hipertrofia do VD*, ou pulso hepático (insuficiência tricúspide).
- *Pulsação supraesternal* intensa: hipertensão, aneurisma de aorta, insuficiência aórtica.
- *Frêmito cardiovascular* (frêmito *catário*, como o ronronar do gato): é o *sopro palpável*. Descreva localização (pelos focos), fase do ciclo (comparando com o ictus ou o pulso carotídeo) e intensidade (+ a ++++).

= Focos de ausculta e técnica

Os focos são pontos de referência e *não coincidem* com a projeção anatômica das valvas, que fica na metade inferior do esterno (#vf("p47_01")). Todo o precórdio, a axila, o dorso e o pescoço devem ser auscultados. As localizações estão na #vf("t-focos").

#fig("p47_01", largura: 7cm, [Focos de ausculta (aórtico, pulmonar, tricúspide e mitral) e projeção das valvas, que não coincidem.])

#tabela(rotulo: "t-focos", titulo: [Focos de ausculta (Porto, cap. 47).], (auto, 1fr), ([Foco], [Localização e uso]),
  [*Mitral*], [*5º EIC esquerdo na linha hemiclavicular*, no ictus (localize o ictus antes, pois se desloca na cardiomegalia).],
  [*Pulmonar*], [*2º EIC esquerdo*, junto ao esterno. Melhor lugar para o *desdobramento de B2*.],
  [*Aórtico*], [*2º EIC direito*, junto ao esterno.],
  [*Aórtico acessório*], [*3º–4º EIC esquerdo*, junto ao esterno; muitas vezes ouve melhor os fenômenos aórticos.],
  [*Tricúspide*], [*Base do apêndice xifoide*, ligeiramente à esquerda. Sopros tricúspides aumentam na *inspiração profunda*.],
)

*Posições:* decúbito dorsal (padrão); *sentado com o tórax inclinado para frente*, para os ruídos da base (*insuficiência aórtica*); *decúbito lateral esquerdo* com a mão na cabeça, para a área mitral (*B3* e *ruflar da estenose mitral*); de pé debruçado, quando as bulhas estão abafadas.

*Receptores:* o *diafragma* ouve sons de *alta frequência*; a *campânula*, os de *baixa frequência* (B3, B4, ruflar), apoiada levemente, pois comprimida vira diafragma. Ausculte sempre sobre a pele, em silêncio.

= Bulhas cardíacas

A #vf("p47_03") mostra o ritmo normal de dois tempos (TUM-TA) e o ritmo com B3 (TUM-TA-TU).

#fig("p47_03", largura: 8.5cm, [Bulhas em relação ao ECG. A, ritmo binário (B1 e B2). B, ritmo tríplice com B3 na protodiástole.])

- *B1:* fechamento da *mitral* (M) e depois da *tricúspide* (T). Coincide com o *ictus* e o *pulso carotídeo*. Timbre grave, um pouco mais longa: *TUM*. Mais intensa no foco *mitral*. Em metade das pessoas normais ouvem-se M e T separados (TLUM), sem relação com a respiração.
- *B2:* fechamento da *aórtica* (A) e depois da *pulmonar* (P). Vem depois do *pequeno silêncio* (sístole), é mais aguda e seca: *TA*. Mais intensa na *base*; na criança, mais forte no foco pulmonar, no adulto e idoso, no aórtico.
- *B3:* ruído *protodiastólico* de *baixa frequência*, pela vibração da parede no *enchimento ventricular rápido*. Normal em *crianças e adultos jovens*. Melhor na área mitral, em *decúbito lateral esquerdo*, com a *campânula*: *TU*.
- *B4:* ruído débil *pré-sistólico* (telediástole), pela desaceleração do sangue impulsionado pela *contração atrial* contra o ventrículo. Rara em normais.

O *desdobramento fisiológico de B2* (#vf("p47_04")) ocorre na *inspiração*: mais sangue chega ao VD, a sístole direita se prolonga e P atrasa (TLA). Na expiração A e P se fundem. Ausculta-se no *foco pulmonar*, porque P só se ouve ali.

#fig("p47_04", largura: 8.5cm, [A, bulhas sem desdobramento. B, desdobramento de B1 (TLUM), sem relação com a respiração. C, desdobramento fisiológico de B2 (TLA) na inspiração.])

#decore(titulo: "Divisão do ciclo")[
  Sístole e diástole se dividem em terços: *proto*, *meso* e *tele* (sístole ou diástole). A telediástole é a *pré-sístole*. *Holossístole* e *holodiástole* ocupam a fase inteira. A FC normal no adulto é *60–100 bpm*.
]

= Ritmos tríplices e galope

Uma terceira bulha na diástole forma o *ritmo tríplice*. A *B3 fisiológica* não tem som diferente da patológica: só é patológica se houver cardiopatia (insuficiência mitral, miocardite, miocardiopatia, shunt esquerda-direita).

O *ritmo de galope* lembra as patas de um cavalo, *PA-TA-TA* (#vf("p47_11")). Ouve-se melhor na ponta, em decúbito lateral esquerdo, com a campânula apoiada de leve; às vezes é mais *palpável* que audível.

#fig("p47_11", largura: 8.5cm, [Ritmo de galope ventricular: em vez do TUM-TA, três ruídos (PA-TA-TA).])

- *Galope ventricular:* ritmo tríplice por *B3 patológica*, quase sempre com taquicardia. Indica *sofrimento miocárdico* ou *insuficiência cardíaca*: é o “*grito de socorro do miocárdio*”.
- *Galope atrial:* por *B4*; menos nítido. Indica *insuficiência iminente* por *disfunção diastólica*: *hipertensão grave* e *insuficiência coronária crônica*.
- *Galope de soma:* fusão de B3 e B4 na taquicardia.

= Alterações das bulhas

A intensidade de B1 depende sobretudo da *posição das valvas AV* no início da sístole: quanto *mais abertas* (mais baixas), *mais forte* o fechamento. B2 depende da pressão na aorta e na pulmonar e do estado das sigmoides (#vf("t-bulhas")).

#tabela(rotulo: "t-bulhas", titulo: [Alterações de intensidade de B1 e B2 (Porto, cap. 47).], (auto, 1fr, 1fr), ([Bulha], [Hiperfonese], [Hipofonese]),
  [*B1*], [*PR curto*, taquicardia, exercício, febre, *hipertireoidismo*, extrassístole, *estenose mitral* com valva flexível (timbre metálico), tórax delgado.], [*PR longo*, miocardite, miocardiopatia, infarto, IC, choque cardiogênico, *estenose mitral calcificada*, obesidade, enfisema, derrame pericárdico.],
  [*B2*], [*Hipertensão arterial* (no foco aórtico), *hipertensão pulmonar* (no foco pulmonar), CIA e canal arterial (pulmonar).], [*Estenose aórtica calcificada*, estenose pulmonar, extrassístoles, miocardiopatias, obesidade, enfisema.],
)

Na *fibrilação atrial* a B1 varia de batimento a batimento (*delirium cordis*); no *BAV total* também varia, com a *bulha em canhão*. Um *sopro de regurgitação* pode *mascarar* a B1.

Os *desdobramentos patológicos de B2* (#vf("t-desdobra")) são estudados no *foco pulmonar*.

#tabela(rotulo: "t-desdobra", titulo: [Desdobramentos de B2 (Porto, Fig. 47.12).], (auto, 1fr), ([Tipo], [Quando aparece e causa]),
  [*Fisiológico*], [Só na *inspiração* (P atrasa pelo maior enchimento do VD). Normal, quase todas as crianças.],
  [*Constante e variável*], [Na expiração e na inspiração, *acentua-se na inspiração*: *bloqueio de ramo direito* (P atrasa). Também na estenose pulmonar.],
  [*Fixo*], [Mesmo intervalo na inspiração e na expiração: *comunicação interatrial* (CIA).],
  [*Invertido ou paradoxal*], [*Só na expiração* (A vem depois de P): *bloqueio de ramo esquerdo* e *estenose aórtica grave*.],
)

A *B4 patológica* aparece quando a *complacência ventricular cai*: estenose aórtica e pulmonar, *hipertensão*, *doença coronariana* e *miocardiopatia hipertrófica*.

= Estalidos e cliques

O *estalido de abertura mitral* (EAM) é o sinal mais indicativo de *estenose mitral*: ruído *seco, agudo, protodiastólico* (TÉ), logo após B2, que *precede o ruflar* (#vf("p47_13")). Ouve-se no foco mitral e na borda esternal esquerda, em decúbito lateral esquerdo. Exige valva flexível: *desaparece* com *calcificação intensa* ou *hipertensão pulmonar* muito grave.

#fig("p47_13", largura: 8.5cm, [Estalido de abertura mitral (EAM, TÉ) após B2, seguido do ruflar; foco mitral (FM) e borda esternal esquerda (BEE).])

- *EAM × B2 desdobrada:* o desdobramento é mais notado no foco pulmonar; o estalido, no 3º–4º EIC esquerdo e no foco mitral, é mais agudo e seco.
- *EAM × B3:* a B3 é *grave* e só na ponta, e fica *mais longe* de B2; o estalido é agudo, metálico e mais próximo de B2.
- *Estalidos protossistólicos* (ruídos de *ejeção*): agudos, logo após B1, na artéria pulmonar ou na aorta (estenose valvar, dilatação, hipertensão pulmonar).
- *Clique mesossistólico ou telessistólico:* seco, agudo, no meio ou fim da sístole, nas áreas mitral ou tricúspide, varia com a respiração e a posição. Indica *prolapso da valva mitral* (ou tricúspide), mesmo sem sopro.

= Sopros

Sopros são vibrações produzidas quando o fluxo deixa de ser *laminar* e vira *turbilhonar*. Mecanismos: *aumento da velocidade* (exercício, anemia, febre, hipertireoidismo), *queda da viscosidade* (anemia), passagem por *zona estreitada*, passagem para *zona dilatada* e vibração de *membrana de borda livre*.

Analise: *situação no ciclo*, *localização*, *irradiação*, *intensidade*, *timbre e tonalidade* e variação com *respiração, posição e exercício*. Para saber o que é sístole, *palpe o pulso carotídeo* enquanto ausculta.

#essencial(titulo: "Sistólico de ejeção × de regurgitação")[
  *Ejeção* (estenose aórtica ou pulmonar): começa *após B1* (depois da contração isovolumétrica), em *crescendo-decrescendo* e termina *antes de B2*. *Regurgitação* (insuficiência mitral ou tricúspide, CIV): começa *com B1*, *mascarando-a*, ocupa *toda a sístole* (holossistólico) com intensidade constante e vai até B2.
]

A #vf("p47_15") resume a posição dos sopros no ciclo.

#fig("p47_15", largura: 12cm, [A, hemodinâmica do sopro sistólico de ejeção (a) e de regurgitação (b). B, sopros sistólicos, diastólicos e contínuo representados em relação a B1 e B2.])

#block(breakable: false)[
Os *sopros diastólicos* são de dois grupos:

- *Estenose mitral ou tricúspide:* sopro *mesodiastólico* (enchimento rápido), com *intervalo após B2*, *baixa frequência* e tom grave, o *ruflar*, com *reforço pré-sistólico* pela contração atrial (some na FA).
- *Insuficiência aórtica ou pulmonar:* começa *logo após B2*, *protodiastólico*, *decrescendo*, de *alta frequência*: caráter *aspirativo*.
]

Os *sopros contínuos* (sistodiastólicos) atravessam B2 sem interrupção e são mais fortes na sístole: o sopro *em maquinaria* da *persistência do canal arterial*, das fístulas arteriovenosas e o rumor venoso.

As duas lesões que dão sopro sistólico estão na #vf("p47_16"), e as duas que dão sopro diastólico, na #vf("p47_17"). A #vf("t-valvas") reúne as quatro.

#fig("p47_16", largura: 10cm, [Sopros sistólicos. A, estenose aórtica: ejeção no foco aórtico, irradiando para o pescoço. B, insuficiência mitral: regurgitação no foco mitral, irradiando para a axila.])

#fig("p47_17", largura: 10cm, [Sopros diastólicos. A, estenose mitral: ruflar com reforço pré-sistólico no foco mitral. B, insuficiência aórtica: sopro aspirativo no foco aórtico ou aórtico acessório, irradiando para a ponta.])

#tabela(rotulo: "t-valvas", titulo: [Sopros das quatro valvopatias clássicas (Porto, Fig. 47.16 e 47.17).], (auto, auto, 1fr), ([Lesão], [Tipo], [Foco, irradiação e timbre]),
  [*Estenose aórtica*], [Sistólico de *ejeção*], [Foco aórtico e aórtico acessório, irradia para o *pescoço* (carótidas); *rude, granuloso*.],
  [*Insuficiência mitral*], [Sistólico de *regurgitação* (holossistólico)], [Foco mitral, irradia para a *axila*.],
  [*Estenose mitral*], [*Mesodiastólico* com reforço pré-sistólico], [Foco mitral, pouca irradiação; *ruflar* (bater de asas), melhor em *DLE com campânula*.],
  [*Insuficiência aórtica*], [*Protodiastólico*, decrescendo], [Foco aórtico ou *aórtico acessório*, irradia para a ponta; *aspirativo*, melhor *sentado e inclinado para frente*.],
)

*Intensidade:* *+* débil (só com atenção), *++* moderado, *+++* intenso, *++++* audível com o estetoscópio *afastado* do tórax. Quanto mais intenso, maior a área de irradiação. Um defeito pequeno pode dar sopro intenso: a *CIV pequena* (fluxo rápido) soa mais que a grande. Algumas manobras ajudam a identificar a origem do sopro (#vf("t-manobras")).

#tabela(rotulo: "t-manobras", titulo: [Manobras que modificam os sopros (Porto, cap. 47).], (auto, 1fr), ([Manobra], [Efeito]),
  [*Inspiração profunda (Rivero-Carvallo)*], [Na área tricúspide: se o sopro *aumenta*, é *tricúspide*; se não muda ou diminui, é *mitral* propagado. Mais sangue chega ao VD.],
  [*Expiração forçada*], [Intensifica os sopros *aórticos*.],
  [*Sentado, tórax para frente*], [Sopros da base, sobretudo a *insuficiência aórtica*.],
  [*Decúbito lateral esquerdo*], [*Ruflar da estenose mitral* e B3.],
  [*Exercício*], [Intensifica quase todos os sopros; útil para revelar o ruflar da estenose mitral.],
  [*Sentar ou ficar de pé*], [Intensifica o *rumor venoso*, que some ao deitar.],
)

O *sopro inocente* é uma *conclusão diagnóstica* (após exame e exames complementares), não um tipo de sopro (#vf("p47_18")).

#fig("p47_18", largura: 8cm, [Sopros inocentes: sistólicos proto (A) ou mesossistólicos (B), nunca holossistólicos, suaves, sem irradiação, na borda esternal esquerda e mesocárdio.])

#essencial(titulo: "Sopro inocente")[
  *Sistólico* (nunca holossistólico), *+ a ++*, *suave*, *sem irradiação*, no *foco pulmonar e mesocárdio*, varia com a *posição*, *sem frêmito*, sem alteração de bulhas e sem aumento de câmaras. Mais comum em *crianças*; afaste antes *febre e anemia*. Sopro *+++/++++*, com *frêmito* e irradiação é *orgânico*.
]

= Atrito e outros ruídos

O *atrito pericárdico* vem do roçar dos folhetos do pericárdio inflamado, sobretudo na *pericardite fibrinosa* (#vf("p47_19")). Características:

- Ouvido na *sístole e na diástole*, *sem relação fixa* com as bulhas; em geral contínuo com reforço sistólico.
- Entre a *ponta* e a *borda esternal esquerda*, *não se irradia*.
- Som de *couro novo friccionado*; muda com a posição e com a *pressão do estetoscópio*.
- *Mutabilidade:* muda de intensidade e qualidade em horas ou dias, o que não ocorre com sopros.

#fig("p47_19", largura: 7cm, [Atrito pericárdico entre a borda esternal esquerda e a ponta, recobrindo B1 e parte da sístole.])

O *ruído da pericardite constritiva* é *protodiastólico*, seco e alto, um pouco antes do momento da B3, restrito à área mitral, endoápex e tricúspide. O *rumor venoso* é *contínuo* e grave, *acima da clavícula direita*; aumenta sentado e *desaparece ao deitar*, ao *comprimir a jugular* ou ao girar o pescoço. Não indica doença e deve ser diferenciado do sopro do *canal arterial*.
'''

VALORES = [
    ("Ictus no mediolíneo", "5º EIC, LHCE", ""),
    ("Ictus no brevilíneo", "4º EIC", "≈ 2 cm para fora"),
    ("Ictus no longilíneo", "6º EIC", "1–2 cm para dentro"),
    ("Extensão normal do ictus", "1–2 polpas", "≥ 3: difuso"),
    ("Mobilidade normal do ictus", "1–2 cm", "Fixo na sínfise pericárdica"),
    ("Ictus na insuficiência aórtica", "6º–8º EIC", "Até a linha axilar anterior"),
    ("Foco mitral", "5º EIC esquerdo, LHC", "Ictus"),
    ("Foco pulmonar", "2º EIC esquerdo", "Paraesternal"),
    ("Foco aórtico", "2º EIC direito", "Paraesternal"),
    ("Foco aórtico acessório", "3º–4º EIC esquerdo", "Paraesternal"),
    ("Foco tricúspide", "Base do apêndice xifoide", "Levemente à esquerda"),
    ("FC normal no adulto", "60–100 bpm", ""),
    ("Galope com FC baixa", "Exercício até ≈ 100 bpm", "Para evidenciar"),
    ("Intensidade dos sopros", "+ a ++++", "++++: estetoscópio afastado"),
    ("Sopro inocente", "+ a ++", "Sistólico, sem frêmito"),
    ("Campânula", "≈ 2,5 cm", "Baixa frequência"),
    ("Diafragma", "3–3,5 cm", "Alta frequência"),
]

CLINICA = [
    ("Estenose mitral", "B1 **hiperfonética**, **estalido de abertura** e **ruflar** com reforço pré-sistólico; FA frequente. Causa: **febre reumática**."),
    ("Insuficiência aórtica", "Ictus **difuso e propulsivo** deslocado, sopro **diastólico aspirativo**, pulso célere e PA divergente."),
    ("Estenose aórtica", "Sopro **sistólico de ejeção** rude irradiado para o **pescoço**, B2 hipofonética, pulso **parvus**, síncope e angina ao esforço."),
    ("Insuficiência mitral", "Sopro **holossistólico** no foco mitral irradiado para a **axila**, com B3."),
    ("Insuficiência cardíaca", "**Galope ventricular** (B3) com taquicardia: sinal de **sofrimento miocárdico**."),
    ("Comunicação interatrial", "**Desdobramento fixo de B2** e sopro sistólico pulmonar por hiperfluxo."),
    ("Persistência do canal arterial", "Sopro **contínuo em maquinaria** perto do foco pulmonar e na região interescapulovertebral esquerda."),
    ("Pericardite aguda", "**Atrito pericárdico** mutável, que não se irradia."),
    ("Prolapso da valva mitral", "**Clique mesossistólico**, com ou sem sopro telessistólico."),
]

PEGADINHAS = [
    "Os focos de ausculta **não** correspondem à posição anatômica das valvas.",
    "Hipertrofia do **VD não desloca o ictus**.",
    "Ictus **difuso** = dilatação; **propulsivo** = hipertrofia.",
    "B1 coincide com o **ictus** e o **pulso carotídeo**.",
    "O desdobramento **fisiológico** de B2 é na **inspiração**; o **paradoxal**, na **expiração**.",
    "Desdobramento **fixo** = **CIA**; **constante e variável** = **BRD**.",
    "B3 normal e patológica **soam iguais**: o contexto decide.",
    "Ruflar da EM é de **baixa frequência**: use a **campânula** sem comprimir.",
    "Sopro **holossistólico nunca** é inocente.",
    "O sopro aumenta na **inspiração**? É do **lado direito** (Rivero-Carvallo).",
    "O **rumor venoso** some ao **deitar** ou comprimir a jugular.",
]

GLOSSARIO = [
    ("Ictus cordis", "Choque da ponta do coração na parede torácica."),
    ("Ictus difuso", "Ictus que ocupa 3 ou mais polpas digitais."),
    ("Ictus propulsivo", "Ictus que levanta a mão a cada sístole."),
    ("Levantamento em massa", "Impulsão sistólica paraesternal (hipertrofia do VD)."),
    ("Frêmito catário", "Vibração palpável de um sopro."),
    ("Sínfise pericárdica", "Aderência dos folhetos pericárdicos."),
    ("Foco aórtico acessório", "3º–4º EIC esquerdo junto ao esterno."),
    ("Pequeno silêncio", "Intervalo entre B1 e B2 (sístole)."),
    ("Grande silêncio", "Intervalo entre B2 e B1 (diástole)."),
    ("Ritmo de galope", "Ritmo tríplice que lembra o galope (PA-TA-TA)."),
    ("Desdobramento paradoxal", "B2 desdobrada só na expiração."),
    ("Estalido de abertura mitral", "Ruído seco protodiastólico da estenose mitral."),
    ("Clique mesossistólico", "Ruído seco sistólico do prolapso valvar."),
    ("Ruflar", "Sopro diastólico grave da estenose mitral."),
    ("Sopro aspirativo", "Sopro diastólico agudo da insuficiência aórtica."),
    ("Sopro em maquinaria", "Sopro contínuo do canal arterial."),
    ("Rivero-Carvallo", "Aumento do sopro tricúspide na inspiração."),
    ("Sopro inocente", "Sopro sem alteração estrutural do coração."),
    ("Atrito pericárdico", "Ruído de couro do pericárdio inflamado."),
    ("Rumor venoso", "Ruído contínuo venoso cervical, benigno."),
]

LEITURA = [
    ("Porto", "Cap. 47 · PDF p. 550–551", "Inspeção e palpação: abaulamento, ictus, batimentos, frêmito, hipertrofias"),
    ("Porto", "Cap. 47 · PDF p. 551–553", "Focos de ausculta e semiotécnica (Fig. 47.1 e 47.2)"),
    ("Porto", "Cap. 47 · PDF p. 553–556", "Bulhas cardíacas (Fig. 47.3 a 47.5)"),
    ("Porto", "Cap. 47 · PDF p. 560–563", "Ritmos tríplices, galope e alterações das bulhas (Fig. 47.11 e 47.12)"),
    ("Porto", "Cap. 47 · PDF p. 563–564", "Estalidos e cliques (Fig. 47.13 e 47.14)"),
    ("Porto", "Cap. 47 · PDF p. 564–569", "Sopros, sopros inocentes, atrito pericárdico e rumor venoso (Fig. 47.15 a 47.19)"),
]

BASICOS = [
    ("Localização normal do ictus cordis no mediolíneo?", "**5º EIC** na linha hemiclavicular esquerda."),
    ("Extensão normal do ictus?", "**1–2 polpas digitais**."),
    ("O que significa ictus difuso e ictus propulsivo?", "Difuso: **dilatação**. Propulsivo: **hipertrofia**."),
    ("Ictus que não se desloca com o decúbito sugere?", "**Sínfise pericárdica**."),
    ("Sinais de hipertrofia do VD ao exame do precórdio?", "**Levantamento em massa** paraesternal, retração sistólica apical, pulsação epigástrica."),
    ("O que é o frêmito catário?", "Vibração palpável de um **sopro** (como o ronronar do gato)."),
    ("Onde ficam os focos mitral e tricúspide?", "Mitral: **5º EIC LHCE**. Tricúspide: **base do apêndice xifoide**.", "p47_01"),
    ("Onde ficam os focos aórtico, pulmonar e aórtico acessório?", "Aórtico: **2º EIC D**. Pulmonar: **2º EIC E**. Acessório: **3º–4º EIC E**.", "p47_01"),
    ("Diafragma × campânula?", "Diafragma: **alta frequência**. Campânula: **baixa** (B3, B4, ruflar)."),
    ("Melhor posição para o ruflar da estenose mitral?", "**Decúbito lateral esquerdo**."),
    ("Melhor posição para o sopro da insuficiência aórtica?", "**Sentado com o tórax inclinado para frente**."),
    ("O que forma a B1 e com o que ela coincide?", "Fechamento **mitral e tricúspide**; coincide com o **ictus** e o **pulso carotídeo**.", "p47_03"),
    ("O que forma a B2?", "Fechamento das valvas **aórtica e pulmonar**."),
    ("Por que B2 desdobra na inspiração?", "Mais sangue chega ao VD, a sístole direita se prolonga e o **componente pulmonar atrasa**.", "p47_04"),
    ("Origem e momento da B3?", "Vibração da parede no **enchimento ventricular rápido**; **protodiastólica**."),
    ("Origem e momento da B4?", "**Contração atrial** contra ventrículo pouco complacente; **pré-sistólica**."),
    ("O que significa o ritmo de galope ventricular?", "**Sofrimento miocárdico / insuficiência cardíaca**.", "p47_11"),
    ("Onde aparece o galope atrial (B4)?", "**Hipertensão grave** e **insuficiência coronária** (disfunção diastólica)."),
    ("Principal determinante da intensidade de B1?", "A **posição das valvas AV** no início da sístole (PR curto → B1 forte)."),
    ("B1 hiperfonética e B1 hipofonética na estenose mitral?", "Hiperfonética com valva **flexível**; hipofonética com valva **calcificada**."),
    ("Hiperfonese de B2 no foco aórtico e no pulmonar?", "**Hipertensão arterial** e **hipertensão pulmonar**."),
    ("Causa do desdobramento constante e variável de B2?", "**Bloqueio de ramo direito**."),
    ("Causa do desdobramento fixo de B2?", "**Comunicação interatrial**."),
    ("Causas do desdobramento paradoxal de B2?", "**Bloqueio de ramo esquerdo** e **estenose aórtica grave**."),
    ("Características do estalido de abertura mitral?", "Seco, agudo, **protodiastólico**, precede o ruflar; some com **calcificação**.", "p47_13"),
    ("Clique mesossistólico indica?", "**Prolapso da valva mitral**."),
    ("Características do sopro sistólico de ejeção?", "Começa **após B1**, **crescendo-decrescendo**, termina antes de B2 (estenose aórtica/pulmonar).", "p47_15"),
    ("Características do sopro sistólico de regurgitação?", "**Holossistólico**, começa **com B1** e a mascara (IM, IT, CIV)."),
    ("Para onde irradiam os sopros da estenose aórtica e da insuficiência mitral?", "EAo: **pescoço**. IM: **axila**.", "p47_16"),
    ("Sopro da estenose mitral?", "**Mesodiastólico**, **ruflar** grave, com **reforço pré-sistólico**.", "p47_17"),
    ("Sopro da insuficiência aórtica?", "**Protodiastólico**, decrescendo, **aspirativo**, no foco aórtico acessório."),
    ("Sopro contínuo em maquinaria?", "**Persistência do canal arterial** (e fístulas AV)."),
    ("O que é a manobra de Rivero-Carvallo?", "Na inspiração profunda, sopro que **aumenta** é **tricúspide**."),
    ("Graduação da intensidade dos sopros?", "**+** a **++++** (++++: audível com o estetoscópio afastado)."),
    ("Características do sopro inocente?", "**Sistólico**, + a ++, suave, **sem irradiação nem frêmito**, varia com a posição.", "p47_18"),
    ("Características do atrito pericárdico?", "Sístole e diástole, **couro novo**, **não irradia**, **mutável**.", "p47_19"),
    ("Características do rumor venoso?", "Contínuo, supraclavicular direito, **some ao deitar** ou comprimir a jugular."),
]

LACUNAS = [
    ("O ictus cordis normal ocupa {{c1::1–2}} polpas digitais.", ""),
    ("Ictus {{c1::difuso}} indica dilatação; ictus {{c2::propulsivo}}, hipertrofia.", ""),
    ("O foco aórtico acessório fica no {{c1::3º–4º}} espaço intercostal esquerdo.", ""),
    ("O foco tricúspide fica na base do {{c1::apêndice xifoide}}.", ""),
    ("A B1 coincide com o {{c1::ictus cordis}} e com o pulso {{c2::carotídeo}}.", ""),
    ("O desdobramento fisiológico de B2 ocorre na {{c1::inspiração}}.", ""),
    ("A B3 ocorre na fase de {{c1::enchimento ventricular rápido}}.", ""),
    ("A B4 decorre da {{c1::contração atrial}}.", ""),
    ("O galope ventricular é o “{{c1::grito de socorro}}” do miocárdio.", ""),
    ("O desdobramento fixo de B2 é típico da {{c1::comunicação interatrial}}.", ""),
    ("O desdobramento paradoxal de B2 ocorre no bloqueio de ramo {{c1::esquerdo}}.", ""),
    ("O sopro da estenose mitral tem caráter de {{c1::ruflar}}; o da insuficiência aórtica, {{c2::aspirativo}}.", ""),
    ("O sopro da estenose aórtica irradia para o {{c1::pescoço}}; o da insuficiência mitral, para a {{c2::axila}}.", ""),
    ("O sopro sistólico de {{c1::regurgitação}} mascara a B1.", ""),
    ("A manobra de {{c1::Rivero-Carvallo}} diferencia o sopro tricúspide do mitral.", ""),
    ("O sopro contínuo em maquinaria é típico da {{c1::persistência do canal arterial}}.", ""),
]

OCLUSOES = [
    ("p47_01", (18, 10, 70, 48), "Que foco é este?", "Foco aórtico (2º EIC direito)"),
    ("p47_01", (343, 10, 410, 48), "Que foco é este?", "Foco pulmonar (2º EIC esquerdo)"),
    ("p47_01", (0, 243, 82, 282), "Que foco é este?", "Foco tricúspide (base do apêndice xifoide)"),
    ("p47_01", (343, 243, 388, 280), "Que foco é este?", "Foco mitral (5º EIC, linha hemiclavicular)"),
    ("p47_16", (583, 186, 628, 210), "Para onde irradia o sopro da insuficiência mitral?", "Axila"),
]
