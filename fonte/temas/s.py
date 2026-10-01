CODIGO = "s"
SLUG = "s-semiologia-anamnese-sintomas-arritmias"
TITULO = "Semiologia: anamnese, sintomas e arritmias"
AREA = "Semiologia"
FONTES = [
    "Porto, Semiologia Médica, 8ª ed., cap. 47 (PDF p. 537–550 e 556–560)",
]

ESSENCIAL = [
    "**Dor anginosa:** retroesternal, **constritiva** (mão fechada no peito), irradia para mandíbula, MMSS, epigástrio e dorso; vem com **esforço**, emoção, frio ou refeição; alivia com **repouso** e **nitrato em 3–4 min**.",
    "**Duração da dor:** angina **2–3 min** (raro > 10); angina instável até **20 min**; infarto **> 20 min**, começa em repouso, com sudorese, náuseas e vômitos.",
    "**Pericardite:** dor contínua por horas, piora com **respiração e decúbito dorsal**, melhora ao **inclinar o tórax para frente**. **Dissecção aórtica:** súbita, **lancinante**, irradia para o **dorso (interescapular)**.",
    "**Dispneia da IVE:** de esforço (grandes → médios → pequenos, **progressão rápida**), **ortopneia**, **dispneia paroxística noturna** (asma cardíaca) e **edema agudo de pulmão** (expectoração **rósea e espumosa**). Causa básica: **congestão pulmonar**.",
    "**Palpitações:** “falhas” e “arrancos” = **extrassístoles**; início e fim **súbitos** = **taquicardia paroxística** (FC > 150); irregular e rápida = **fibrilação atrial**.",
    "**Síncope cardíaca:** bradicardia **< 30–40** ou taquicardia **> 150 bpm**. **Stokes-Adams** = síncope com convulsão por arritmia (Chagas com BAV). A **vasovagal** é a mais comum e melhora ao **deitar**.",
    "**Cianose:** Hb reduzida **≥ 5 g/dL** (anêmico grave não fica cianótico). **Central** (melhora com O₂) × **periférica** (pele fria, melhora ao aquecer ou elevar o membro).",
    "**Edema cardíaco (IVD):** começa nos **maléolos**, bilateral, **vespertino**, com **jugulares túrgidas** e **hepatomegalia**; generalizado = **anasarca**.",
    "**FA:** ritmo **completamente irregular**, B1 de intensidade variável (**delirium cordis**) e **déficit de pulso**. **BAVT:** FC **30–40**, regular, B1 variável com **bulha em canhão**.",
]

CORPO = r'''
= Anamnese

Identificação e antecedentes já sugerem o diagnóstico:

- *Idade:* crianças e jovens têm *cardiopatias congênitas* e *febre reumática*; de 20 a 50 anos, *Chagas* e *hipertensão*; acima de 50, *doença coronariana*.
- *Sexo:* *estenose mitral* e *prolapso mitral* são mais comuns em *mulheres jovens*; a aterosclerose coronária predomina nos homens até os 45 anos.
- *Naturalidade e moradia:* habitação rural precária em área endêmica lembra *doença de Chagas*.
- *Antecedentes:* *amigdalite estreptocócica* (lesão valvar reumática), dieta rica em gordura (aterosclerose), doença renal (hipertensão).
- *Hábitos:* *tabagismo*, álcool e sedentarismo.

= Dor torácica

Dor precordial *não* é sinônimo de dor cardíaca: pode vir da parede torácica, pleura, esôfago, estômago, aorta, mediastino ou ser psicogênica (Quadro 47.1 do Porto). Avalie *localização, irradiação, caráter, intensidade, duração, fatores desencadeantes e de alívio e sintomas associados*. As quatro dores mais cobradas estão na #vf("t-dor").

#tabela(rotulo: "t-dor", titulo: [Dores torácicas de origem cardiovascular e psicogênica (Porto, cap. 47).], (auto, 1fr), ([Tipo], [Características]),
  [*Isquêmica (angina)*], [Retroesternal, *constritiva* (“aperto”, “peso”, “queimação”; mão fechada no peito). Irradia para pescoço, *mandíbula*, ombros, *membros superiores*, epigástrio e região interescapular. Vem com *esforço*, emoção, frio, taquicardia ou refeição copiosa; alivia com *repouso* e *nitrato sublingual em 3–4 min*.],
  [*Infarto agudo*], [Mesmo caráter, porém *> 20 min* (até horas), começa *em repouso*, intensa, com *sudorese fria, náuseas, vômitos*, palidez e sensação de morte iminente.],
  [*Pericárdica*], [Retroesternal junto à borda esternal esquerda, irradia para pescoço e costas; *contínua* por horas; piora com *respiração, tosse, deglutição e decúbito dorsal*; alivia ao *inclinar o tórax para frente* ou na posição genupeitoral.],
  [*Aórtica (dissecção)*], [*Súbita*, muito intensa, *lancinante*, retroesternal, irradia para pescoço, *região interescapular* e ombros; paciente inquieto. O aneurisma sem dissecção quase não dói.],
  [*Psicogênica*], [Na *ponta* do coração (perimamilar), *surda*, dura horas ou semanas, sem relação com esforço; vem com palpitações e *dispneia suspirosa*.],
)

#essencial(titulo: "Duração da dor isquêmica")[
  *Angina estável:* 2–3 min, raramente > 10 min (só hipóxia). *Angina instável:* até 20 min. *Infarto:* > 20 min (necrose). Se o nitrato leva 5–10 min para aliviar, pense em angina instável.
]

Outras pistas: dor que piora à *palpação das articulações condroesternais* é a *síndrome de Tietze*; dor com mudanças de decúbito ou movimentos do pescoço vem da *coluna*; dor retroesternal ao *deglutir* vem do *esôfago*.

= Palpitações

Palpitação é a *percepção incômoda dos batimentos* e nem sempre significa arritmia (exercício, emoção, anemia, hipertireoidismo, café, drogas). Pergunte frequência, ritmo, modo de *início e término* e uso de estimulantes.

- *“Falhas”, “arrancos”, “tremor”:* *extrassístoles*. O paciente sente mais o batimento *pós-extrassistólico*; o “coração parou” é a *pausa compensadora*.
- *Início e fim súbitos:* *taquicardia paroxística*. Início súbito e fim gradual: taquicardia sinusal ou ansiedade.
- *FC 100–150* sugere taquicardia *sinusal*; *> 150* sugere *paroxística*.
- *Rápidas e irregulares:* *fibrilação atrial*.
- *De esforço:* têm o mesmo valor da dispneia de esforço.

= Dispneia

Na cardiopatia, dispneia significa *congestão pulmonar*: a pressão alta no átrio esquerdo passa às veias e capilares pulmonares, o líquido vai ao interstício e o pulmão fica mais rígido. Os tipos estão na #vf("t-dispneia").

#tabela(rotulo: "t-dispneia", titulo: [Tipos de dispneia na insuficiência ventricular esquerda (Porto, cap. 47).], (auto, 1fr), ([Tipo], [Características]),
  [*De esforço*], [A mais comum. Aos *grandes* (subir escadas, andar depressa), *médios* (andar no plano, poucos degraus) e *pequenos esforços* (banho, vestir-se, falar). Na IVE progride *rápido*; na doença pulmonar e na anemia, devagar.],
  [*De decúbito (ortopneia)*], [Surge *logo ao deitar* (mais sangue dos membros inferiores e do leito esplâncnico chega ao pulmão). O paciente usa vários travesseiros ou dorme sentado.],
  [*Paroxística noturna*], [O paciente *acorda* sufocado, com tosse seca, e precisa sentar ou levantar. Com sibilos por congestão da mucosa brônquica: *asma cardíaca*.],
  [*Edema agudo de pulmão*], [Forma grave: dispneia intensa, *expectoração espumosa rósea*, cianose, sibilos e *estertores*. Típico do *infarto* e da *estenose mitral*.],
  [*Cheyne-Stokes*], [*Apneia* (15–30 s, até 60 s) seguida de respirações que crescem e depois diminuem. Na IVE, hipertensão, coronariopatia e lesões neurológicas; pode ocorrer no sono de idosos e crianças.],
)

*Asma cardíaca × brônquica:* a cardíaca surge *deitado* e melhora ao sentar, com taquicardia, *galope* e *estertores finos nas bases*; na brônquica a posição não alivia e os *sibilos* predominam. A radiografia mostra *congestão* na cardíaca e *hiperinsuflação* na brônquica.

= Tosse, hemoptise e chiado

A *tosse da IVE* é *seca* e *noturna*, por congestão; no edema agudo vem com *expectoração rósea espumosa*. Aneurisma de aorta e átrio esquerdo grande causam tosse por compressão brônquica ou do nervo laríngeo recorrente. Lembre que os *inibidores da ECA* causam tosse seca.

*Hemoptise* é a eliminação de *mais de 2 mL* de sangue pelas vias aéreas (sangue vivo, arejado, com tosse). Na hematêmese o sangue é escuro, em “borra de café”, com restos alimentares. O aspecto ajuda:

- *Espumosa e rósea:* edema agudo de pulmão.
- *“Cor de tijolo”:* pneumonia pneumocócica.
- *“Geleia de framboesa”:* infarto pulmonar.
- *Volumosa, sangue vivo:* ruptura de veias brônquicas dilatadas, como na *estenose mitral*.

= Síncope e lipotimia

*Síncope* é a perda súbita e transitória da consciência e do tônus postural; *lipotimia* (pré-síncope) é a perda parcial. A causa é a *queda transitória do fluxo cerebral*. A anamnese do episódio orienta a causa (#vf("t-sincope")).

#tabela(rotulo: "t-sincope", titulo: [Dados da anamnese que sugerem a causa da síncope (Porto, Quadro 47.6).], (auto, 1fr), ([Dado], [Causa provável]),
  [Início súbito, sem pródromos], [Arritmia cardíaca, causa neurológica],
  [Pródromos (palidez, sudorese, náusea)], [*Vasovagal*],
  [Ao levantar-se], [*Hipotensão ortostática* (anti-hipertensivos, diuréticos)],
  [Muito tempo em pé, dor, emoção, sangue], [Vasovagal],
  [Ao virar a cabeça ou apertar o colarinho], [*Hipersensibilidade do seio carotídeo*],
  [Durante o *exercício*], [*Obstrução da via de saída do VE* (estenose aórtica)],
  [Exercício com os braços], [Roubo da subclávia],
  [Convulsão, mordedura da língua, incontinência; recuperação lenta], [Causa neurológica],
)

*Causas cardíacas:* arritmias com FC *< 30–40* ou *> 150 bpm*, estenose aórtica, infarto, embolia pulmonar, mixoma atrial e trombose de prótese. A *síndrome de Stokes-Adams* é a síncope por *parada, bradi ou taquiarritmia grave*, com *convulsões*; é comum na *cardiopatia chagásica com BAV de 2º ou 3º grau*. A tontura surge 2–5 s após a arritmia, a perda da consciência em 10–15 s e as convulsões em 20–40 s.

*Causas extracardíacas:* a *vasovagal* (neurogênica) é a *mais comum*: vasodilatação com inibição simpática e aumento vagal, e *melhora rápida ao deitar*. Outras: *hipotensão postural*, seio carotídeo, síncope pós-tosse e pós-micção, hiperventilação e *hipoglicemia*.

= Cianose

Cianose é a cor azulada da pele e mucosas quando a *hemoglobina reduzida* chega a *5 g/dL* nos capilares (normal ≈ 2,6). Por isso o *anêmico grave não fica cianótico*. Examine à luz do dia lábios, nariz, orelhas, língua e extremidades. Os tipos estão na #vf("t-cianose").

#tabela(rotulo: "t-cianose", titulo: [Tipos de cianose (Porto, cap. 47).], (auto, 1fr), ([Tipo], [Mecanismo e exemplos]),
  [*Central*], [Sangue arterial mal oxigenado: altitude, doença pulmonar, *shunt direita-esquerda* (*tetralogia de Fallot*, Eisenmenger, transposição). Generalizada, inclusive nas mucosas; *melhora com O₂*.],
  [*Periférica*], [Perda exagerada de O₂ nos capilares por *estase* ou *vasoconstrição* (frio, IC, choque, flebite). Áreas distais, *pele fria*; melhora ao *aquecer ou elevar* o membro.],
  [*Mista*], [Central + periférica, como na *IC congestiva grave*.],
  [*Por alteração da Hb*], [*Meta-hemoglobina* (> 20% da Hb) por nitritos, anilinas, sulfas: cor azul-acinzentada.],
)

*Baqueteamento digital* (dedos em baqueta de tambor, unhas em vidro de relógio) com cianose sugere *cardiopatia congênita cianótica* ou doença pulmonar crônica; sem cianose, lembre *endocardite infecciosa subaguda*. Cianose desde o nascimento sugere cardiopatia congênita.

= Edema, astenia e cócoras

O *edema cardíaco* vem da *insuficiência ventricular direita*: a pressão venosa alta aumenta a pressão hidrostática nos capilares e o *sistema renina-angiotensina-aldosterona* retém sódio e água.

- Começa nos *maléolos*, sobe para pernas e coxas; é *bilateral* (assimetria sugere varizes ou trombose associada).
- É *vespertino*: piora ao longo do dia e melhora com o repouso noturno. No acamado, fica na região *sacral*.
- Deixa *fóvea* à compressão. Edema generalizado com serosas é a *anasarca*.
- Vem com *jugulares túrgidas*, *refluxo hepatojugular* e *hepatomegalia*. Na *pericardite constritiva* e na lesão tricúspide, a *ascite* predomina.
- O peso pode subir *até 10%* antes de surgir fóvea.

*Astenia* (fraqueza) é comum na IC e no infarto, por baixo débito; piora com diurético em excesso e *hipopotassemia* (cãibras). A *posição de cócoras* é adotada por crianças com *cardiopatia congênita cianótica* (tetralogia de Fallot): a compressão das femorais *eleva a resistência sistêmica*, reduz o shunt direita-esquerda e melhora a saturação.

= Arritmias ao exame clínico

A arritmia é suspeitada pelos sintomas, pelo *pulso radial*, pelo *pulso venoso* e pela *ausculta*. DC = VS × FC: abaixo de *40* ou acima de *160 bpm* a compensação falha e o DC cai. As taquiarritmias encurtam a diástole (#vf("p47_06")); as bradiarritmias reduzem a frequência (#vf("p47_07")). As duas podem causar síncope e *Stokes-Adams*; as causas mais frequentes são a *doença de Chagas* e a *cardiopatia isquêmica*. Os achados de cada arritmia estão na #vf("t-arritmias").

#fig("p47_06", largura: 7.5cm, [Repercussões das taquiarritmias: diástole curta, menor volume sistólico, restrição diastólica e insuficiência circulatória cerebral, coronariana e periférica.])

#fig("p47_07", largura: 7.5cm, [Repercussões das bradiarritmias: frequência baixa, baixo débito (suficiente em repouso, insuficiente aos esforços) e insuficiência circulatória cerebral.])

#tabela(rotulo: "t-arritmias", titulo: [Arritmias reconhecíveis ao exame clínico (Porto, cap. 47).], (auto, 1fr), ([Arritmia], [Achados]),
  [*Taquicardia sinusal*], [FC > 100 (até 150 no adulto), por simpático; esforço, emoção, febre, anemia, hipertireoidismo, IC. *B1 hiperfonética*.],
  [*Bradicardia sinusal*], [FC < 60 (40–50), por vagal; atletas, sono, hipotireoidismo, hipertensão intracraniana, betabloqueador, digital. *Aumenta com o exercício*; B1 hipofonética.],
  [*Arritmia sinusal*], [FC *aumenta na inspiração* e diminui na expiração; normal em crianças e jovens; some com exercício e apneia.],
  [*Extrassístoles*], [Batimento *prematuro* seguido de *pausa compensadora*. A ventricular não gera onda de pulso; o batimento seguinte é mais forte. Bigeminismo: 1 extra após cada normal.],
  [*Taquicardia paroxística*], [Foco ectópico a *150–250/min*, início e fim *súbitos*. Supraventricular em geral > 180 bpm; ventricular é mais grave.],
  [*Fibrilação atrial*], [Átrios a *400–600/min*, ventrículos irregulares: ritmo *completamente irregular*, B1 variável (*delirium cordis*), *déficit de pulso*. Causas: *estenose mitral*, Chagas, isquemia, hipertireoidismo.],
  [*BAV total (3º grau)*], [Átrios e ventrículos independentes, FC *30–40*, pulso amplo, lento e regular; *B1 de intensidade variável* com *bulha em canhão*; *não acelera* com exercício.],
)

A extrassístole ventricular isolada, o bigeminismo e a salva estão na #vf("p47_08"): no batimento prematuro ouve-se só a B1 e falta a onda de pulso.

#fig("p47_08", largura: 8.5cm, [A, extrassístole ventricular isolada com pausa compensadora; B, bigeminismo; C, extrassístoles em salva. Bulhas (TUM-TA) e ondas de pulso.])

Na *fibrilação atrial* (#vf("p47_09")) não há onda P e as bulhas e os pulsos variam em intervalo e intensidade.

#fig("p47_09", largura: 8.5cm, [Fibrilação atrial: sem onda P, bulhas e ondas de pulso irregulares em ritmo e amplitude.])

No *BAV total* (#vf("p47_10")) as ondas P não se relacionam com o QRS e, de vez em quando, surge a *bulha em canhão* (sístole atrial 0,10–0,12 s antes da ventricular, valvas bem abertas).

#fig("p47_10", largura: 8.5cm, [Bloqueio atrioventricular total: ritmo lento e regular, B1 variável e bulha em canhão (seta).])

#essencial(titulo: "Bradicardia sinusal × BAV total")[
  Ambos têm pulso lento e regular. No *BAVT* a FC é *< 40*, a *B1 varia* (bulha em canhão) e a FC *não sobe* com exercício. Na *bradicardia sinusal* a FC costuma ser *> 40*, a B1 é constante e a FC *sobe* com exercício.
]
'''

VALORES = [
    ("Angina estável", "2–3 min", "Raro > 10 min"),
    ("Angina instável", "Até 20 min", ""),
    ("Infarto agudo", "> 20 min", "Começa em repouso"),
    ("Alívio da angina com nitrato", "3–4 min", "5–10 min: instável"),
    ("Palpitação: taquicardia sinusal", "FC 100–150", ""),
    ("Palpitação: taquicardia paroxística", "FC > 150", "Foco a 150–250/min"),
    ("Apneia do Cheyne-Stokes", "15–30 s", "Até 60 s"),
    ("Hemoptise", "> 2 mL de sangue", ""),
    ("Síncope por arritmia", "FC < 30–40 ou > 150", ""),
    ("Stokes-Adams: perda da consciência", "10–15 s após a arritmia", "Convulsão em 20–40 s"),
    ("Hb reduzida para cianose", "≥ 5 g/dL", "Normal ≈ 2,6"),
    ("Meta-hemoglobina com cianose", "> 20% da Hb", ""),
    ("Peso retido antes da fóvea", "Até 10%", ""),
    ("DC compensado", "FC entre 40 e 160", ""),
    ("Fibrilação atrial (átrios)", "400–600/min", ""),
    ("BAV total", "FC 30–40", ""),
    ("Bulha em canhão", "Sístole atrial 0,10–0,12 s antes", ""),
]

CLINICA = [
    ("Síndrome coronariana aguda", "Dor constritiva **> 20 min**, em repouso, com sudorese e náuseas: pensar em **infarto** e fazer ECG imediato."),
    ("Pericardite aguda", "Dor que **melhora inclinando para frente** e piora deitado; ao exame, **atrito pericárdico**."),
    ("Dissecção de aorta", "Dor **lancinante** irradiada para o dorso, em hipertenso; pulsos e PA assimétricos."),
    ("Insuficiência cardíaca esquerda", "Dispneia progressiva, **ortopneia**, **DPN**, tosse noturna, **estertores** nas bases e **B3**."),
    ("Insuficiência cardíaca direita", "**Edema vespertino** de membros inferiores, **jugulares túrgidas**, **hepatomegalia** e ascite."),
    ("Doença de Chagas", "Natural de zona endêmica com **BAV**, extrassístoles, **Stokes-Adams** e IC."),
    ("Estenose mitral", "Mulher jovem com dispneia, **hemoptise**, **FA** e edema agudo de pulmão."),
    ("Tetralogia de Fallot", "Criança com **cianose central**, **baqueteamento** e **posição de cócoras**."),
]

PEGADINHAS = [
    "Dor precordial **não** é sinônimo de dor cardíaca.",
    "Dor **perimamilar** ou na **ponta** quase nunca é cardíaca (psicogênica).",
    "Angina que dura **mais de 20 min** já não é angina estável.",
    "**Ortopneia** surge **logo ao deitar**; a **paroxística noturna** acorda o paciente depois de horas.",
    "**Anemia grave** impede a cianose (falta Hb reduzida).",
    "Cianose **periférica** tem pele **fria**; a **central** melhora com **O₂**.",
    "Na extrassístole o paciente sente o batimento **após** a pausa, não o prematuro.",
    "Síncope **ao esforço** sugere **estenose aórtica**.",
    "**Bradicardia sinusal** acelera com exercício; o **BAVT** não.",
    "**Inibidores da ECA** causam tosse seca.",
]

GLOSSARIO = [
    ("Angina de peito", "Dor por isquemia miocárdica transitória."),
    ("Síndrome de Tietze", "Osteocondrite condroesternal dolorosa."),
    ("Palpitação", "Percepção incômoda dos batimentos cardíacos."),
    ("Ortopneia", "Dispneia ao deitar, aliviada sentado."),
    ("Dispneia paroxística noturna", "Crise de dispneia que acorda o paciente."),
    ("Asma cardíaca", "DPN com broncospasmo e sibilos."),
    ("Cheyne-Stokes", "Respiração periódica com apneias."),
    ("Hemoptise", "Eliminação de sangue das vias aéreas pela tosse."),
    ("Síncope", "Perda súbita e transitória da consciência."),
    ("Lipotimia", "Pré-síncope: perda parcial da consciência."),
    ("Stokes-Adams", "Síncope com convulsão por arritmia grave."),
    ("Cianose", "Cor azulada por Hb reduzida ≥ 5 g/dL."),
    ("Baqueteamento digital", "Dedos em baqueta e unhas em vidro de relógio."),
    ("Anasarca", "Edema generalizado com derrames cavitários."),
    ("Pausa compensadora", "Pausa longa após a extrassístole."),
    ("Déficit de pulso", "Menos pulsos radiais que batimentos cardíacos."),
    ("Delirium cordis", "Irregularidade total da fibrilação atrial."),
    ("Bulha em canhão", "B1 muito intensa no BAV total."),
]

LEITURA = [
    ("Porto", "Cap. 47 · PDF p. 537–540", "Anamnese e dor torácica (Quadro 47.1)"),
    ("Porto", "Cap. 47 · PDF p. 540–545", "Palpitações, dispneia, tosse, chiado e hemoptise (Quadros 47.2 a 47.5)"),
    ("Porto", "Cap. 47 · PDF p. 545–548", "Síncope e lipotimia (Quadro 47.6)"),
    ("Porto", "Cap. 47 · PDF p. 548–550", "Cianose, edema, astenia e posição de cócoras"),
    ("Porto", "Cap. 47 · PDF p. 556–560", "Ritmo, frequência e arritmias (Quadro 47.7, Fig. 47.6 a 47.10)"),
]

BASICOS = [
    ("Localização e caráter típicos da dor anginosa?", "**Retroesternal** e **constritiva** (aperto, peso), com a mão fechada no peito."),
    ("Irradiações da dor isquêmica?", "**Mandíbula**, pescoço, ombros, **membros superiores**, epigástrio e região interescapular."),
    ("Fatores que desencadeiam a angina?", "**Esforço**, emoção, frio, taquicardia, refeição copiosa."),
    ("Quanto dura a angina estável, a instável e o infarto?", "**2–3 min** (raro > 10); até **20 min**; **> 20 min**."),
    ("Em quanto tempo o nitrato alivia a angina estável?", "**3–4 min**."),
    ("Características da dor pericárdica?", "Contínua, piora com **respiração e decúbito dorsal**, melhora **inclinando o tórax para frente**."),
    ("Características da dor da dissecção aórtica?", "**Súbita**, **lancinante**, irradiada para a **região interescapular**."),
    ("Características da dor psicogênica?", "Na **ponta**, surda, por horas a semanas, sem relação com esforço, com dispneia suspirosa."),
    ("O que sugere a palpitação descrita como “falhas” ou “arrancos”?", "**Extrassístoles**."),
    ("Palpitação com início e fim súbitos e FC > 150 sugere?", "**Taquicardia paroxística**."),
    ("Qual a causa básica da dispneia na cardiopatia?", "**Congestão pulmonar** (pressão alta no átrio esquerdo)."),
    ("Como evolui a dispneia de esforço da IVE?", "Passa **rápido** dos grandes aos pequenos esforços."),
    ("Diferença entre ortopneia e dispneia paroxística noturna?", "Ortopneia surge **ao deitar**; a DPN **acorda** o paciente após horas de sono."),
    ("Sinais do edema agudo de pulmão?", "Dispneia intensa, **expectoração rósea espumosa**, cianose, sibilos e **estertores**."),
    ("Descreva a respiração de Cheyne-Stokes.", "**Apneia** (15–30 s) e respirações que crescem e diminuem de amplitude."),
    ("Asma cardíaca × brônquica?", "Cardíaca melhora **sentado**, com galope e **estertores**; brônquica não muda com a posição, **sibilos** predominam."),
    ("Volume mínimo para hemoptise?", "**> 2 mL** de sangue."),
    ("Hemoptise “cor de tijolo” e “geleia de framboesa”?", "**Pneumonia pneumocócica** e **infarto pulmonar**."),
    ("Qual a síncope mais comum e o que a alivia?", "**Vasovagal**; melhora ao **deitar**."),
    ("O que é a síndrome de Stokes-Adams?", "Síncope com **convulsão** por arritmia grave (comum no **Chagas com BAV**)."),
    ("Síncope durante o exercício sugere?", "**Obstrução da saída do VE** (estenose aórtica)."),
    ("Quanto de Hb reduzida é preciso para cianose?", "**5 g/dL**."),
    ("Como diferenciar cianose central de periférica?", "Central: **melhora com O₂**. Periférica: **pele fria**, melhora ao aquecer ou elevar."),
    ("Três exemplos de cianose central por shunt?", "**Tetralogia de Fallot**, Eisenmenger, transposição dos grandes vasos."),
    ("Características do edema cardíaco?", "Começa nos **maléolos**, bilateral, **vespertino**, com jugulares túrgidas e hepatomegalia."),
    ("Por que a criança com Fallot fica de cócoras?", "**Eleva a resistência sistêmica**, reduz o shunt D-E e melhora a saturação."),
    ("Abaixo e acima de que FC o DC cai?", "**< 40** e **> 160 bpm**.", "p47_07"),
    ("Achados da extrassístole ventricular na ausculta e no pulso?", "Só a **B1**, **sem onda de pulso**, seguida de **pausa compensadora**.", "p47_08"),
    ("Achados da fibrilação atrial ao exame?", "Ritmo **totalmente irregular**, B1 variável e **déficit de pulso**.", "p47_09"),
    ("Achados do BAV total ao exame?", "FC **30–40**, pulso regular, **B1 variável** e **bulha em canhão**.", "p47_10"),
    ("Como a arritmia sinusal varia com a respiração?", "FC **sobe na inspiração** e cai na expiração."),
    ("Principais causas de fibrilação atrial?", "**Estenose mitral**, Chagas, cardiopatia isquêmica, hipertireoidismo."),
]

LACUNAS = [
    ("A dor da angina estável dura {{c1::2–3}} minutos e a do infarto mais de {{c2::20}} minutos.", ""),
    ("A dor da pericardite melhora quando o paciente {{c1::inclina o tórax para frente}}.", ""),
    ("A dor da dissecção aórtica é {{c1::lancinante}} e irradia para a região {{c2::interescapular}}.", ""),
    ("Palpitação descrita como “falhas” sugere {{c1::extrassístoles}}.", ""),
    ("A dispneia que acorda o paciente é a {{c1::dispneia paroxística noturna}}.", ""),
    ("No edema agudo de pulmão a expectoração é {{c1::rósea}} e {{c2::espumosa}}.", ""),
    ("No Cheyne-Stokes as apneias duram {{c1::15–30}} segundos.", ""),
    ("Hemoptise é a eliminação de mais de {{c1::2}} mL de sangue.", ""),
    ("A síncope com convulsão por arritmia grave é a síndrome de {{c1::Stokes-Adams}}.", ""),
    ("A síncope mais comum é a {{c1::vasovagal}}.", ""),
    ("Cianose aparece com hemoglobina reduzida de {{c1::5}} g/dL.", ""),
    ("A cianose {{c1::periférica}} acompanha-se de pele fria.", ""),
    ("O edema cardíaco piora à tarde: é chamado {{c1::vespertino}}.", ""),
    ("Na fibrilação atrial, o número de pulsos menor que o de batimentos é o {{c1::déficit de pulso}}.", ""),
    ("No BAV total a FC fica entre {{c1::30}} e {{c2::40}} bpm.", ""),
]

OCLUSOES = [
    ("p47_06", (133, 2, 218, 45), "Qual o primeiro efeito da taquiarritmia?", "Encurtamento da diástole"),
    ("p47_06", (117, 81, 242, 125), "Que síndrome está oculta?", "Síndrome de restrição diastólica"),
    ("p47_07", (149, 95, 222, 140), "O que está oculto?", "Diástole alongada"),
    ("p47_07", (2, 178, 128, 224), "Que síndrome está oculta?", "Síndrome de baixo débito cardíaco"),
    ("p47_07", (186, 178, 352, 222), "O que está oculto?", "Suficiente em repouso, insuficiência aos esforços"),
]
