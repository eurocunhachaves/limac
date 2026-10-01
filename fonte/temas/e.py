CODIGO = "e"
SLUG = "e-vasos-e-microcirculacao"
TITULO = "Vasos, pulso e microcirculação"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 15 (PDF p. 569–602)",
    "Guyton & Hall, 14ª ed., cap. 16 (PDF p. 603–641)",
]

ESSENCIAL = [
    "**Veias:** ≈ **8 vezes mais distensíveis** e ≈ **24 vezes mais complacentes** que as artérias (8 × volume 3 vezes maior). Por isso são o **reservatório** de sangue.",
    "**Pressão de pulso** = sistólica − diastólica (≈ 40 mmHg) ≈ **volume sistólico ÷ complacência arterial**. Artéria rígida (idoso) aumenta a pressão de pulso.",
    "**PA média** ≈ **60% diastólica + 40% sistólica**: fica mais perto da diastólica.",
    "**Korotkoff:** o primeiro som marca a **sistólica**; o abafamento ou o desaparecimento, a **diastólica**.",
    "**Pressão venosa central** (átrio direito) ≈ **0 mmHg**. De pé e parado, a veia do pé chega a **+90 mmHg**; andando, a **bomba muscular** a mantém **< 20 mmHg**.",
    "**Starling:** filtração = Kf × (**Pc − Pi − πp + πi**). Na ponta arterial sai líquido (**+13**), na venosa volta (**−7**); no balanço sobram **0,3 mmHg** de filtração, que a **linfa** devolve.",
    "**Pressão oncótica do plasma ≈ 28 mmHg**, ≈ 80% dela pela **albumina**. Linfa ≈ **2–3 L/dia**.",
]

CORPO = r'''
= Distensibilidade e complacência

Todos os vasos são distensíveis. A elasticidade das artérias absorve o jato de cada sístole e mantém o fluxo contínuo nos tecidos. As *veias* são as mais distensíveis: pequenos aumentos de pressão fazem elas guardarem 0,5 a 1 L de sangue a mais.

- *Distensibilidade* = aumento de volume ÷ (aumento de pressão × volume original). Ex.: se 1 mmHg faz um vaso de 10 mL ganhar 1 mL, a distensibilidade é 0,1 (10%) por mmHg.
- *Complacência* (capacitância) = aumento de volume ÷ aumento de pressão. É a *distensibilidade × volume*: mede quanto sangue um leito inteiro guarda por mmHg.

As veias são cerca de *8 vezes mais distensíveis* que as artérias e têm volume cerca de *3 vezes maior*. Por isso a complacência de uma veia sistêmica é ≈ *24 vezes* a da artéria correspondente (8 × 3). As artérias pulmonares, que trabalham com pressões ≈ 1/6 das sistêmicas, são ≈ 6 vezes mais distensíveis que as artérias sistêmicas.

*Complacência tardia (estresse-relaxamento):* um vaso que recebe volume extra tem um pico de pressão que cai em minutos a horas, porque o músculo liso da parede se alonga. É assim que a circulação acomoda uma transfusão grande e, no sentido inverso, se ajusta após uma hemorragia.

== Curvas de volume-pressão

A #vf("g15_01") mostra que o sistema arterial com ≈ *700 mL* tem pressão média de 100 mmHg, mas com 400 mL a pressão cai a zero. O sistema venoso guarda *2.000 a 3.500 mL*, e são precisas várias centenas de mL para mudar a pressão venosa em só 3 a 5 mmHg. Por isso meio litro de sangue pode ser transfundido em minutos sem grande efeito.

#fig("g15_01", [Curvas de volume-pressão dos sistemas arterial e venoso, com o efeito da estimulação e da inibição simpáticas.])

O *simpático* aumenta a pressão em cada volume (curva desloca para cima), transfere sangue dos vasos para o coração e aumenta o bombeamento. Na hemorragia, a contração simpática das veias deixa a circulação funcionar quase normal mesmo com perda de até 20–25% do volume.

= Pulso da pressão arterial

Sem a complacência das artérias, todo o sangue ejetado passaria pelos tecidos só na sístole. Com ela, o pulso de pressão quase some até os capilares e o fluxo nos tecidos é contínuo. A #vf("g15_03") mostra o pulso na aorta ascendente: *sistólica ≈ 120*, *diastólica ≈ 80* e *pressão de pulso ≈ 40 mmHg*.

#fig("g15_03", [Pulso de pressão na aorta ascendente, com a incisura do fechamento da valva aórtica.])

#essencial(titulo: "Pressão de pulso")[
  *Pressão de pulso ≈ volume sistólico ÷ complacência arterial.* Sobe com volume sistólico maior e com artérias mais rígidas (complacência menor). Um fator menor é a forma da ejeção.
]

== Pulsos anormais

Algumas doenças mudam a forma e a amplitude do pulso (#vf("g15_04")):

- *Arteriosclerose (idoso):* artérias rígidas, pressão de pulso até *2 vezes* o normal.
- *Estenose aórtica:* pouco sangue passa pela valva estreita e o pulso fica *muito diminuído*.
- *Persistência do canal arterial:* 50% ou mais do sangue ejetado volta pela artéria pulmonar, a diastólica *cai muito* e a pressão de pulso aumenta.
- *Insuficiência aórtica:* o sangue volta ao ventrículo, a pressão aórtica pode cair *até zero* entre os batimentos e *não há incisura*, porque a valva não fecha.

#fig("g15_04", [Pulso aórtico na arteriosclerose, na estenose aórtica, na persistência do canal arterial e na insuficiência aórtica.])

== Transmissão e amortecimento

A onda de pressão viaja muito mais rápido que o sangue: *3–5 m/s na aorta*, 7–10 m/s nos grandes ramos e *15–35 m/s nas pequenas artérias*. Quanto *maior a complacência*, *mais lenta* a transmissão. Na periferia o pulso vai sendo *amortecido* até quase sumir nos capilares. O amortecimento é proporcional a *resistência × complacência*.

= Medida da pressão arterial

No *método auscultatório* (#vf("g15_07a")), o manguito é inflado acima da sistólica e o estetoscópio fica sobre a artéria antecubital.

#fig("g15_07a", largura: 8cm, [Método auscultatório: a pressão do manguito (reta) cai sobre o pulso arterial. Os sons de Korotkoff vão de B (sistólica) a C (diastólica).])

- Manguito *acima da sistólica*: artéria fechada, *sem som*.
- Manguito *logo abaixo da sistólica* (ponto B): o sangue passa em jatos no pico da sístole, com turbulência, e surgem os *sons de Korotkoff*. Primeiro som = *pressão sistólica*.
- Perto da diastólica (ponto C) os sons ficam *abafados*; logo abaixo, *desaparecem*. O abafamento ou o desaparecimento marca a *pressão diastólica*. Em fístula arteriovenosa e insuficiência aórtica os sons podem continuar até o manguito vazio.

O *método oscilométrico* (aparelho automático) lê as oscilações no manguito. A *oscilação máxima* corresponde à *pressão arterial média*; sistólica e diastólica são calculadas por algoritmo. Evita o efeito do jaleco branco, mas erra com manguito de tamanho errado e com artérias muito rígidas.

== Pressão arterial média e idade

A pressão sobe com a idade, sobretudo pelas mudanças dos rins após os 50 anos. Depois dos 60 a sistólica sobe mais, pela rigidez das artérias (aterosclerose), e a pressão de pulso aumenta.

A *pressão arterial média* não é a média simples de sistólica e diastólica, porque a diástole dura mais. Ela é ≈ *60% da diastólica + 40% da sistólica*. Em frequência muito alta, a diástole encurta e a média se aproxima da média simples.

= Veias

As veias levam o sangue de volta, *armazenam* sangue, impulsionam o sangue pela *bomba venosa* e ajudam a regular o débito cardíaco.

== Pressão venosa central

A pressão no *átrio direito* é a *pressão venosa central*. Normal ≈ *0 mmHg* (igual à atmosférica). Ela depende do equilíbrio entre o bombeamento do coração direito e o retorno de sangue das veias periféricas:

- Sobe com *coração fraco*, *mais volume de sangue*, *mais tônus venoso* e *dilatação das arteríolas*. Chega a 20–30 mmHg na insuficiência cardíaca grave ou após transfusão maciça.
- Cai a −3 a −5 mmHg (pressão do tórax) com coração muito vigoroso ou após hemorragia grave.

As grandes veias que entram no tórax são comprimidas em vários pontos (sobre a 1ª costela, pela pressão atmosférica no pescoço, pelos órgãos no abdome). Por isso as veias periféricas, deitado, ficam *4 a 6 mmHg acima* do átrio direito. A pressão intra-abdominal (≈ +6 mmHg, até 15–30 na gestação, obesidade, tumores e ascite) também eleva a pressão nas veias das pernas.

== Gravidade

A pressão hidrostática aumenta 1 mmHg a cada 13,6 mm abaixo da superfície. Na pessoa *de pé e parada*, o átrio direito continua em ≈ 0 mmHg, mas as *veias dos pés* chegam a ≈ *+90 mmHg* (#vf("g15_10")).

#fig("g15_10", [Pressões venosas (mmHg) em cada nível do corpo na pessoa de pé e parada.])

- *Mão:* ≈ +35 mmHg (6 da compressão na 1ª costela + 29 da gravidade).
- *Pescoço:* veias colapsadas pela pressão atmosférica, pressão ≈ 0.
- *Seio sagital:* ≈ *−10 mmHg*, porque o crânio é rígido. Aberto em cirurgia, pode aspirar ar e causar embolia gasosa.
- *Artérias:* também somam a gravidade. Com média de 100 mmHg no coração, a pressão arterial nos pés é ≈ 190 mmHg.

O ponto de referência para medir pressões é o nível da *valva tricúspide*, onde a mudança de posição altera a pressão em no máximo 1–2 mmHg. O próprio coração regula a pressão nesse ponto.

== Válvulas e bomba venosa

As *válvulas venosas* só deixam o sangue subir. A cada contração dos músculos da perna, o sangue é empurrado para o coração: é a *bomba venosa (muscular)*. Andando, a pressão nas veias do pé fica *abaixo de 20 mmHg*. Parado, ela sobe aos 90 mmHg em ≈ 30 s, os capilares filtram mais, as pernas incham e até *10–20% do volume* pode sair da circulação em 15–30 min, com risco de desmaio (soldado em posição de sentido).

*Varizes:* a distensão crônica das veias (gestação, ficar muito em pé) torna as válvulas incompetentes, a bomba falha e a pressão sobe ainda mais. Surgem edema, dor, fraqueza e úlceras. Tratamento: *elevar as pernas* e *meias de compressão*.

*Estimativa clínica:* sentado e em repouso, as veias do pescoço normalmente *não estão distendidas*. Com pressão atrial direita de *+10 mmHg* as veias da base do pescoço começam a saltar; com *+15 mmHg* praticamente todas estão distendidas.

== Reservatórios de sangue

Mais de 60% do sangue fica nas veias. Na hemorragia, o simpático contrai as veias e a circulação funciona quase normal mesmo com perda de até 20% do volume. Os maiores reservatórios são o *baço* (sua polpa vermelha guarda hemácias concentradas), o *fígado*, as *grandes veias abdominais* e o *plexo venoso da pele*.

= Microcirculação

O corpo tem ≈ *10 bilhões de capilares*, com 500 a 700 m² de superfície. Quase nenhuma célula fica a mais de 20–30 µm de um capilar. A organização típica está na #vf("g16_01"):

- *Arteríolas* (10–15 µm): muito musculares, mudam muito o diâmetro.
- *Metarteríolas:* músculo liso em pontos intermitentes.
- *Esfíncter pré-capilar:* fibra muscular na entrada de cada capilar, que abre e fecha o capilar.
- *Vênulas:* maiores que as arteríolas, com músculo fraco, mas ainda contráteis pela pressão baixa.

#fig("g16_01", [Componentes da microcirculação: arteríola, metarteríolas, esfíncteres pré-capilares, capilares e vênulas.])

== Parede capilar

A parede é uma *camada única de endotélio* com membrana basal, com ≈ 0,5 µm de espessura. O diâmetro interno é de 4 a 9 µm, o bastante para as hemácias passarem. Água e solutos atravessam pelas *fendas intercelulares* (6–7 nm, um pouco menores que a albumina), que são só 1/1.000 da superfície. Os poros variam conforme o órgão (#vf("t-capilares")).

#tabela(rotulo: "t-capilares", titulo: [Permeabilidade dos capilares em órgãos especiais.], (auto, 1fr), ([Órgão], [Característica dos capilares]),
  [*Cérebro*], [Junções oclusivas: só passam moléculas muito pequenas (água, O₂, CO₂). É a barreira hematoencefálica.],
  [*Fígado*], [Fendas quase totalmente abertas: passam até as proteínas plasmáticas.],
  [*Intestino*], [Poros intermediários entre músculo e fígado.],
  [*Glomérulo renal*], [*Fenestrações* no endotélio: filtram muita água e pequenos solutos, mas não as proteínas.],
)

*Vasomotricidade:* o fluxo no capilar é *intermitente*, porque metarteríolas e esfíncteres contraem e relaxam a cada poucos segundos ou minutos. O principal regulador é o *oxigênio* do tecido: com pouco O₂, os períodos de fluxo ficam mais frequentes e mais longos.

== Trocas por difusão

A *difusão* é o meio mais importante de troca entre plasma e interstício. A água do plasma se troca com a do interstício ≈ *80 vezes* enquanto o plasma percorre o capilar.

- *Lipossolúveis* (O₂, CO₂) atravessam toda a membrana do endotélio e se difundem muito rápido.
- *Hidrossolúveis* (água, Na⁺, Cl⁻, glicose) passam só pelas fendas. A permeabilidade cai com o tamanho: albumina passa ≈ 1/1.000 da água.
- A difusão é proporcional à *diferença de concentração*.

O *interstício* (≈ 1/6 do corpo) tem colágeno e filamentos de proteoglicanos que retêm o líquido como um *gel*; no edema cresce a fração de líquido livre.

= Forças de Starling

Quatro forças decidem se o líquido sai ou volta para o capilar (#vf("g16_05")):

- *Pc*, pressão hidrostática capilar: empurra para *fora*.
- *Pi*, pressão hidrostática intersticial: empurra para *dentro* se positiva e puxa para *fora* se negativa (normal ≈ −3 mmHg no subcutâneo).
- *πp*, pressão coloidosmótica (oncótica) do plasma: puxa para *dentro*.
- *πi*, pressão coloidosmótica do interstício: puxa para *fora*.

#fig("g16_05", [As quatro forças de Starling na membrana capilar.])

#essencial(titulo: "Equação de Starling")[
  *Pressão efetiva de filtração (PEF) = Pc − Pi − πp + πi*. *Filtração = Kf × PEF*, em que Kf é o coeficiente de filtração (número e tamanho dos poros e área capilar).
]

== Os valores das forças

- *Pc:* 30–40 mmHg na ponta arterial, 10–15 na venosa (micropipeta). A pressão capilar *funcional média* é ≈ *17 mmHg*. Glomérulo ≈ 60; capilares peritubulares ≈ 13.
- *Pi:* ≈ *−3 mmHg* no subcutâneo frouxo. É negativa porque a *linfa bombeia* o líquido para fora do interstício. Em tecidos encapsulados (cérebro, rim) é positiva. Espaço pleural ≈ −8 mmHg.
- *πp:* ≈ *28 mmHg* (19 das proteínas + 9 do efeito Donnan). ≈ *80% vem da albumina* (pressão osmótica depende do número de moléculas, e a albumina é a menor e mais abundante).
- *πi:* ≈ *8 mmHg* (interstício com ≈ 3 g/dL de proteína, 40% do plasma).

O balanço em cada ponto do capilar está na #vf("t-starling").

#tabela(rotulo: "t-starling", titulo: [Forças de Starling (mmHg) nas pontas arterial e venosa e na média do capilar.], (1fr, auto, auto, auto), ([Força], [Ponta arterial], [Ponta venosa], [Média]),
  [Pc (para fora)], [30], [10], [17,3],
  [Pi negativa (para fora)], [3], [3], [3],
  [πi (para fora)], [8], [8], [8],
  [*Total para fora*], [*41*], [*21*], [*28,3*],
  [πp (para dentro)], [28], [28], [28],
  [*Resultado*], [*13 para fora* (filtração)], [*7 para dentro* (reabsorção)], [*0,3 para fora*],
)

Cerca de 1/200 do plasma é filtrado a cada passagem. *Nove décimos* do filtrado voltam na ponta venosa (os capilares venosos são mais numerosos e permeáveis) e *um décimo* vai para a linfa. O desequilíbrio de 0,3 mmHg dá uma *filtração efetiva de ≈ 2 mL/min* no corpo todo (sem os rins). Kf do corpo ≈ *6,67 mL/min por mmHg*.

Se a pressão capilar média sobe 20 mmHg, a filtração aumenta *68 vezes*, além da capacidade da linfa, e surge *edema*. Se a pressão capilar cai, há reabsorção e o volume de sangue aumenta.

= Sistema linfático

A linfa devolve ao sangue o excesso de líquido e, principalmente, as *proteínas* e partículas grandes que não voltam pelos capilares. Sem essa função morreríamos em ≈ 24 horas. Quase todo o corpo drena para o *ducto torácico*, que desemboca na junção da *jugular interna esquerda com a subclávia esquerda*. O lado direito da cabeça, do pescoço, o braço direito e parte do tórax direito drenam pelo ducto linfático direito.

Os capilares linfáticos têm endotélio preso por *fibrilas de ancoragem*, com bordas sobrepostas que funcionam como *válvulas* que só abrem para dentro (#vf("g16_07")). Assim, proteínas e até bactérias entram, mas não saem.

#fig("g16_07", [Capilar linfático: células endoteliais com bordas sobrepostas (válvulas) e fibrilas de ancoragem.])

- *Fluxo:* ≈ *120 mL/h*, ou *2–3 L/dia* (100 mL/h pelo ducto torácico).
- *Proteína na linfa:* ≈ 2 g/dL na maioria dos tecidos e 3–5 g/dL no ducto torácico. A linfa também absorve quase toda a *gordura* da dieta.
- *Determinantes do fluxo:* fluxo ≈ *pressão do líquido intersticial × atividade da bomba linfática*. O fluxo aumenta mais de 20 vezes quando Pi sobe de −6 a 0 mmHg e atinge um máximo pouco acima de 0.
- *Bomba linfática:* cada segmento entre válvulas se contrai ao ser distendido (até 50–100 mmHg no ducto torácico). Também bombeiam a contração muscular, o movimento, o pulso das artérias e a compressão externa. No exercício o fluxo sobe 10–30 vezes.

A linfa controla a *concentração de proteínas*, o *volume* e a *pressão* do interstício. A pressão intersticial negativa mantém os tecidos unidos; quando ela é perdida, surge o *edema*.
'''

VALORES = [
    ("Distensibilidade: veia vs. artéria", "≈ 8 ×", ""),
    ("Complacência: veia vs. artéria", "≈ 24 ×", "8 × 3 (volume)"),
    ("Volume no sistema arterial", "≈ 700 mL", "Venoso 2.000–3.500 mL"),
    ("Pressão de pulso", "≈ 40 mmHg", "120 − 80"),
    ("PA média", "≈ 60% PAD + 40% PAS", ""),
    ("Velocidade do pulso", "Aorta 3–5 m/s", "Pequenas artérias 15–35 m/s"),
    ("Pressão venosa central", "≈ 0 mmHg", "IC grave: 20–30"),
    ("Veias periféricas (deitado)", "PVC + 4 a 6 mmHg", ""),
    ("Veia do pé de pé e parado", "≈ +90 mmHg", "Andando < 20 mmHg"),
    ("Seio sagital (de pé)", "≈ −10 mmHg", "Risco de embolia gasosa"),
    ("Pressão abdominal", "≈ +6 mmHg", "15–30 na gestação, ascite"),
    ("Jugulares distendidas", "PAD ≥ +10 mmHg", "Todas com +15 mmHg"),
    ("Capilares", "≈ 10 bilhões", "500–700 m²"),
    ("Fenda intercelular", "6–7 nm", "Pouco menor que a albumina"),
    ("Pc ponta arterial / venosa", "30 / 10 mmHg", "Média funcional ≈ 17"),
    ("Pi (subcutâneo)", "≈ −3 mmHg", "Pleura ≈ −8"),
    ("πp (oncótica do plasma)", "≈ 28 mmHg", "80% albumina"),
    ("πi", "≈ 8 mmHg", "Proteína ≈ 3 g/dL"),
    ("PEF ponta arterial / venosa", "+13 / −7 mmHg", "Média +0,3"),
    ("Filtração efetiva (corpo)", "≈ 2 mL/min", "Kf ≈ 6,67 mL/min/mmHg"),
    ("Fluxo de linfa", "≈ 120 mL/h", "2–3 L/dia"),
]

CLINICA = [
    ("Pulso e valvopatias", "**Estenose aórtica:** pulso de amplitude pequena. **Insuficiência aórtica:** pressão de pulso enorme, diastólica muito baixa, sem incisura. **Canal arterial:** diastólica baixa."),
    ("Hipertensão sistólica do idoso", "A rigidez arterial reduz a complacência: a **sistólica e a pressão de pulso sobem**, mesmo com diastólica normal ou baixa."),
    ("Turgência jugular", "Veias do pescoço distendidas com o paciente sentado indicam **pressão venosa central elevada** (≥ 10 mmHg), como na insuficiência cardíaca direita."),
    ("Varizes e edema", "Válvulas incompetentes impedem a bomba muscular; a pressão venosa e capilar sobe e surge **edema** de membros inferiores. Tratar com elevação e meias de compressão."),
    ("Edema pelas forças de Starling", "Edema surge com **Pc alta** (insuficiência cardíaca), **πp baixa** (hipoalbuminemia: cirrose, síndrome nefrótica, desnutrição), **mais permeabilidade** (inflamação) ou **bloqueio linfático**."),
]

PEGADINHAS = [
    "**Complacência ≠ distensibilidade:** complacência = distensibilidade × volume. A veia é 8 × mais distensível, mas 24 × mais complacente.",
    "A **PA média** fica mais perto da **diastólica**, não é (PAS + PAD) / 2.",
    "Quanto **mais complacente** o vaso, **mais lenta** a transmissão do pulso. O pulso viaja muito mais rápido que o sangue.",
    "No aparelho **oscilométrico**, a oscilação máxima é a **PA média**, não a sistólica.",
    "**Pi normal é negativa** (≈ −3 mmHg) no subcutâneo, por causa da bomba linfática.",
    "**πi** puxa líquido para **fora** do capilar; **πp** puxa para **dentro**.",
    "A pressão oncótica depende do **número** de moléculas: por isso a **albumina** (menor e mais abundante) gera ≈ 80% dela.",
    "Só **1/10** do filtrado vai para a linfa; 9/10 voltam na ponta venosa.",
]

GLOSSARIO = [
    ("Distensibilidade", "Aumento de volume por mmHg em relação ao volume original."),
    ("Complacência", "Aumento de volume por mmHg (distensibilidade × volume)."),
    ("Complacência tardia", "Queda lenta da pressão após aumento de volume, pelo alongamento do músculo liso."),
    ("Pressão de pulso", "Sistólica menos diastólica."),
    ("Incisura", "Entalhe no pulso aórtico pelo fechamento da valva aórtica."),
    ("Sons de Korotkoff", "Sons do jato turbulento sob o manguito, entre a sistólica e a diastólica."),
    ("Pressão venosa central", "Pressão no átrio direito."),
    ("Bomba venosa", "Compressão das veias pelos músculos, com válvulas que só deixam o sangue subir."),
    ("Metarteríola", "Arteríola terminal com músculo liso descontínuo."),
    ("Esfíncter pré-capilar", "Anel muscular na entrada do capilar."),
    ("Vasomotricidade", "Contração intermitente de metarteríolas e esfíncteres."),
    ("Pressão coloidosmótica", "Pressão osmótica das proteínas (oncótica)."),
    ("Kf", "Coeficiente de filtração capilar."),
    ("Efeito Donnan", "Cátions retidos pelas proteínas, que somam ≈ 9 mmHg à pressão oncótica."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 15 · PDF p. 569–580", "Distensibilidade, complacência, pulso e pulsos anormais (Fig. 15.1 a 15.6)"),
    ("Guyton & Hall", "Cap. 15 · PDF p. 580–587", "Medida da PA, PA média e idade (Fig. 15.7 e 15.8)"),
    ("Guyton & Hall", "Cap. 15 · PDF p. 587–601", "Veias, PVC, gravidade, bomba venosa, reservatórios (Fig. 15.9 a 15.13)"),
    ("Guyton & Hall", "Cap. 16 · PDF p. 603–616", "Microcirculação, parede capilar, difusão, interstício (Fig. 16.1 a 16.4)"),
    ("Guyton & Hall", "Cap. 16 · PDF p. 616–629", "Forças de Starling e seus valores (Fig. 16.5)"),
    ("Guyton & Hall", "Cap. 16 · PDF p. 629–639", "Sistema linfático (Fig. 16.6 a 16.9)"),
]

BASICOS = [
    ("Diferença entre distensibilidade e complacência?", "Complacência = **distensibilidade × volume**: quanto sangue o leito guarda por mmHg."),
    ("Quantas vezes a veia é mais complacente que a artéria? Por quê?", "≈ **24 vezes**: 8 vezes mais distensível × 3 vezes mais volume."),
    ("Efeito do simpático na curva volume-pressão?", "**Aumenta a pressão** em cada volume e transfere sangue para o coração.", "g15_01"),
    ("O que é complacência tardia?", "Queda gradual da pressão após aumento de volume, pelo **estresse-relaxamento** do músculo liso."),
    ("Dois determinantes da pressão de pulso?", "**Volume sistólico** e **complacência arterial** (PP ≈ VS / complacência).", "g15_03"),
    ("Como fica o pulso na insuficiência aórtica?", "Pressão de pulso enorme, diastólica podendo chegar a zero e **sem incisura**.", "g15_04"),
    ("Como fica o pulso na estenose aórtica?", "**Diminuído**, porque pouco sangue passa pela valva estreita."),
    ("Por que o pulso é transmitido mais rápido nas pequenas artérias?", "Porque são **menos complacentes**: mais complacência, transmissão mais lenta."),
    ("O que marca a sistólica e a diastólica no método auscultatório?", "**1º som de Korotkoff** = sistólica. **Abafamento/desaparecimento** = diastólica.", "g15_07"),
    ("O que causa os sons de Korotkoff?", "O **jato turbulento** pela artéria parcialmente fechada e a vibração da parede."),
    ("Como estimar a PA média?", "≈ **60% da diastólica + 40% da sistólica**."),
    ("Pressão venosa central normal? O que a eleva?", "≈ **0 mmHg**. Sobe com coração fraco, mais volume, mais tônus venoso e dilatação arteriolar."),
    ("Pressão nas veias do pé, de pé e parado? E andando?", "≈ **+90 mmHg** parado; **< 20 mmHg** andando (bomba venosa).", "g15_10"),
    ("Por que o seio sagital tem pressão negativa?", "O crânio é **rígido** e não deixa as veias colapsarem; de pé chega a ≈ −10 mmHg."),
    ("Com que PAD as jugulares começam a distender?", "≈ **+10 mmHg**; com +15 mmHg todas estão distendidas."),
    ("Ponto de referência para medir pressões?", "O nível da **valva tricúspide**."),
    ("Função do esfíncter pré-capilar?", "**Abrir e fechar** a entrada do capilar.", "g16_01"),
    ("Principal regulador da vasomotricidade?", "A concentração de **oxigênio** no tecido."),
    ("Como são os capilares do cérebro, fígado e glomérulo?", "Cérebro: **junções oclusivas**. Fígado: **fendas abertas**. Glomérulo: **fenestrações**."),
    ("Quais as quatro forças de Starling e o sentido de cada uma?", "**Pc** (fora), **Pi** (dentro se +), **πp** (dentro), **πi** (fora).", "g16_05"),
    ("Equação da pressão efetiva de filtração?", "**PEF = Pc − Pi − πp + πi**."),
    ("PEF na ponta arterial, venosa e na média?", "**+13** (filtra), **−7** (reabsorve), **+0,3** mmHg."),
    ("Por que Pi é negativa no subcutâneo?", "Porque a **bomba linfática** retira continuamente o líquido do interstício."),
    ("Quanto da pressão oncótica vem da albumina?", "≈ **80%** (21,8 de 28 mmHg)."),
    ("Por que o sistema linfático é vital?", "É a única via de retorno das **proteínas** do interstício para o sangue."),
    ("Onde desemboca o ducto torácico?", "Na junção da **jugular interna esquerda** com a **subclávia esquerda**."),
    ("Estrutura que deixa as proteínas entrarem no capilar linfático?", "Bordas endoteliais **sobrepostas** (válvulas) presas por **fibrilas de ancoragem**.", "g16_07"),
    ("Fluxo de linfa diário?", "≈ **2–3 L/dia** (≈ 120 mL/h)."),
]

LACUNAS = [
    ("As veias são ≈ {{c1::8}} vezes mais distensíveis e ≈ {{c2::24}} vezes mais complacentes que as artérias.", ""),
    ("Pressão de pulso ≈ {{c1::volume sistólico}} ÷ {{c2::complacência arterial}}.", ""),
    ("A PA média é ≈ {{c1::60}}% da diastólica + {{c2::40}}% da sistólica.", ""),
    ("O pulso viaja a {{c1::3–5}} m/s na aorta e {{c2::15–35}} m/s nas pequenas artérias.", ""),
    ("De pé e parado, a pressão nas veias do pé chega a ≈ {{c1::+90}} mmHg.", "Andando fica < 20 mmHg."),
    ("PEF = {{c1::Pc}} − {{c2::Pi}} − {{c3::πp}} + {{c4::πi}}.", ""),
    ("A pressão oncótica do plasma é ≈ {{c1::28}} mmHg e a do interstício ≈ {{c2::8}} mmHg.", ""),
    ("A pressão do líquido intersticial no subcutâneo é ≈ {{c1::−3}} mmHg.", ""),
    ("Na ponta arterial a PEF é de {{c1::+13}} mmHg e na venosa de {{c2::−7}} mmHg.", ""),
    ("Cerca de {{c1::9/10}} do filtrado é reabsorvido na ponta venosa e {{c2::1/10}} vai para a linfa.", ""),
    ("O fluxo de linfa é de ≈ {{c1::2–3}} L/dia.", ""),
    ("As fendas intercelulares medem {{c1::6–7}} nm.", ""),
]

OCLUSOES = [
    ("g15_03", "Incisura", "O que é este ponto do pulso aórtico?", "Incisura (fechamento da valva aórtica)"),
    ("g15_04", "Estenose aórtica", "Que condição produz este pulso?", "Estenose aórtica"),
    ("g15_04", "Arteriosclerose", "Que condição produz este pulso?", "Arteriosclerose"),
    ("g15_04", (358, 280, 472, 324), "Que condição produz este pulso?", "Insuficiência aórtica"),
    ("g15_04", (198, 280, 328, 324), "Que condição produz este pulso?", "Persistência do canal arterial"),
    ("g16_01", "Metarteríolas", "Que estrutura está oculta?", "Metarteríolas"),
    ("g16_01", "pré-capilares", "Que estrutura está oculta?", "Esfíncteres pré-capilares"),
    ("g16_05", (250, 6, 440, 76), "Que força é esta?", "Pressão coloidosmótica plasmática (πp)"),
    ("g16_05", (68, 172, 242, 233), "Que força é esta?", "Pressão do líquido intersticial (Pi)"),
    ("g16_07", (80, 336, 292, 361), "Que estruturas estão indicadas?", "Fibrilas de ancoragem"),
    ("g16_07", (398, 141, 468, 171), "Que estruturas estão indicadas?", "Válvulas (bordas endoteliais sobrepostas)"),
    ("g15_11", "Válvula", "Que estrutura está indicada?", "Válvula venosa"),
]
