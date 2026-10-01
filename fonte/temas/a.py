CODIGO = "a"
SLUG = "a-musculo-cardiaco-e-valvas"
TITULO = "O músculo cardíaco e as valvas cardíacas"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 9 (PDF p. 363–405)",
    "Porto, Semiologia Médica, 8ª ed., cap. 46 (ciclo cardíaco e bulhas)",
]

ESSENCIAL = [
    "O miocárdio é um **sincício funcional**: os discos intercalados têm junções comunicantes, e o estímulo passa de célula a célula. Átrios e ventrículos são dois sincícios separados pelo esqueleto fibroso; só o **feixe AV** os conecta.",
    "O potencial de ação ventricular tem **platô** (≈0,2–0,3 s) graças aos **canais lentos de Ca²⁺ (tipo L)** e à queda da permeabilidade ao K⁺. O platô gera um **período refratário longo**, que impede o tétano.",
    "**Acoplamento excitação-contração:** o Ca²⁺ que entra pelos túbulos T dispara a liberação de mais Ca²⁺ do retículo sarcoplasmático (receptor de rianodina). O Ca²⁺ extracelular é indispensável à força.",
    "Ciclo cardíaco: **contração isovolumétrica → ejeção → relaxamento isovolumétrico → enchimento** (rápido, lento, sístole atrial = 20%). Nas fases isovolumétricas, **todas as valvas estão fechadas**.",
    "Volumes do VE: **VDF 110–120 mL, VS ≈70 mL, VSF 40–50 mL, FE ≈60%**.",
    "**Frank-Starling:** quanto mais o ventrículo se enche (pré-carga), mais forte se contrai e mais sangue ejeta. O simpático aumenta FC e força; o vago reduz sobretudo a FC.",
]

CORPO = r'''
= O miocárdio como sincício

O coração tem três tipos de músculo: *atrial*, *ventricular* e as *fibras excitatórias e condutoras* (nó sinusal, feixe AV, Purkinje), que contraem pouco e servem para gerar e conduzir o impulso. As fibras atriais e ventriculares são estriadas e contraem como o músculo esquelético, mas por mais tempo.

As células são separadas por *discos intercalados* (#vf("g9_02")), membranas com *junções comunicantes* (gap) de baixíssima resistência. Os íons passam livremente e o potencial de ação se espalha de célula a célula. Por isso o miocárdio funciona como um *sincício*: estimular uma célula excita todas.

#fig("g9_02", [Fibras do miocárdio unidas por discos intercalados.])

São *dois sincícios*, o atrial e o ventricular, separados pelo *tecido fibroso* que circunda os anéis valvares. O impulso só passa dos átrios aos ventrículos pelo *feixe AV*. Assim, os átrios contraem um pouco antes dos ventrículos, o que melhora o enchimento.

= Potencial de ação do músculo ventricular

O potencial de repouso é de *−85 a −90 mV*. No pico chega a *+20 mV* e permanece despolarizado por *0,2 s no átrio e 0,3 s no ventrículo*. Esse *platô* não existe no músculo esquelético. As fases e as correntes de cada uma estão na #vf("g9_05") e na #vf("t-fases-pa").

#fig("g9_05", [Fases 0–4 do potencial de ação ventricular (em cima) e as correntes iônicas de cada fase (embaixo).])

#tabela(rotulo: "t-fases-pa", titulo: [O que acontece em cada fase do potencial de ação ventricular.], (auto, 1fr), ([Fase], [O que acontece]),
  [*0*], [Despolarização: abrem os *canais rápidos de Na⁺*.],
  [*1*], [Repolarização inicial: fecham os canais de Na⁺ e sai um pouco de K⁺.],
  [*2*], [*Platô*: abrem os *canais lentos de Ca²⁺ (tipo L)* e cai a permeabilidade ao K⁺.],
  [*3*], [Repolarização rápida: fecham os canais de Ca²⁺ e abrem os de K⁺.],
  [*4*], [Repouso, em cerca de −90 mV.],
)

== Por que existe o platô

- Os *canais lentos de Ca²⁺* abrem devagar e ficam abertos por décimos de segundo, deixando entrar Ca²⁺ (e Na⁺).
- Logo após a despolarização, a *permeabilidade ao K⁺ cai cerca de cinco vezes*, o que segura a repolarização.

Quando os canais de Ca²⁺ fecham e o K⁺ volta a sair, a membrana repolariza.

== Período refratário

Durante o platô a célula não responde a novo estímulo. O *período refratário absoluto* do ventrículo dura *0,25–0,30 s*, quase toda a contração, e o *relativo* mais *0,05 s*. No átrio o refratário é menor, cerca de *0,15 s*. Consequência prática: o coração *não entra em tétano*, porque relaxa antes de poder contrair de novo (#vf("g9_06")).

#fig("g9_06", [Força de contração e períodos refratários: uma contração prematura só é possível depois do período refratário absoluto.])

== Velocidade de condução

No músculo atrial e ventricular o impulso caminha a *0,3–0,5 m/s*. Nas fibras de Purkinje chega a *4 m/s*, o que faz os ventrículos contraírem quase ao mesmo tempo.

= Acoplamento excitação-contração

O potencial de ação percorre o sarcolema e entra pelos *túbulos T*, onde abre os *canais de Ca²⁺ do tipo L* (receptores di-hidropiridínicos). O Ca²⁺ que entra ativa os *receptores de rianodina* do retículo sarcoplasmático, que liberam muito mais Ca²⁺. É a *liberação de cálcio induzida por cálcio*. O Ca²⁺ se liga à troponina C e a actina e a miosina deslizam (#vf("g9_07"), à esquerda).

#fig("g9_07", [Acoplamento excitação-contração e relaxamento. À esquerda, a entrada de Ca²⁺ pelos canais tipo L dispara a liberação pelo RyR; à direita, a recaptação pela SERCA2 e a saída pelo trocador Na⁺/Ca²⁺.])

O *relaxamento* começa quando o Ca²⁺ é bombeado de volta ao retículo pela *SERCA2* (gasta ATP) e expulso da célula pelo *trocador Na⁺/Ca²⁺* e pela bomba de Ca²⁺ da membrana. O Na⁺ que entra pelo trocador sai pela Na⁺/K⁺-ATPase.

#atencao[
  O retículo sarcoplasmático cardíaco é pouco desenvolvido, então a *força depende muito do Ca²⁺ extracelular* que entra pelos túbulos T. Esses túbulos são cinco vezes mais largos que os do músculo esquelético e cheios de mucopolissacarídeos que guardam Ca²⁺. Por isso o Ca²⁺ do sangue mexe na força do coração e quase nada na do músculo esquelético.
]

= Ciclo cardíaco

O *ciclo cardíaco* vai do início de um batimento ao início do seguinte e começa com um potencial de ação no *nó sinusal*. O atraso de mais de *0,1 s* no nó AV deixa os átrios contraírem antes dos ventrículos. A *diástole* é o relaxamento e o enchimento; a *sístole*, a contração e a ejeção.

A *72 bpm* o ciclo dura *0,833 s* e a sístole ocupa cerca de *0,4 do ciclo*. Quando a FC sobe, a *diástole encurta mais que a sístole*: em FC muito alta o ventrículo não tem tempo de se encher. Todos os eventos do ciclo aparecem juntos no diagrama de Wiggers (#vf("g9_08")), a figura mais cobrada do tema.

#fig("g9_08", [Eventos do ciclo cardíaco no lado esquerdo (diagrama de Wiggers): pressões aórtica, ventricular e atrial, volume ventricular, ECG e fonocardiograma.])

== Pressões atrial e aórtica

- *Onda a:* contração atrial (AD sobe 4–6 mmHg; AE, 7–8 mmHg).
- *Onda c:* início da contração ventricular; as valvas AV abaulam para dentro dos átrios.
- *Onda v:* fim da sístole; o átrio se enche com as AV fechadas. Desaparece quando elas abrem.
- *Aorta:* sobe com a ejeção até *≈120 mmHg*. O fechamento da valva aórtica produz a *incisura* (refluxo breve). Na diástole a pressão cai devagar, porque as artérias elásticas devolvem o sangue armazenado, até *≈80 mmHg*. Na artéria pulmonar as pressões são cerca de *1/6* das aórticas.

As ondas a, c e v são as mesmas do *pulso venoso jugular* da Semiologia.

== As fases, uma a uma

A #vf("t-fases-ciclo") resume cada fase, com a posição das valvas. Repare que nas duas fases *isovolumétricas* as quatro valvas estão fechadas.

#tabela(rotulo: "t-fases-ciclo", titulo: [As fases do ciclo cardíaco e a posição das valvas.], (1.3fr, auto, auto, 2.2fr), ([Fase], [Valvas AV], [Semilunares], [O que acontece]),
  [*Enchimento rápido*], [abertas], [fechadas], [Primeiro terço da diástole. O sangue acumulado nos átrios durante a sístole entra rápido no ventrículo.],
  [*Enchimento lento (diástase)*], [abertas], [fechadas], [Terço médio. Passa só o sangue que continua chegando das veias.],
  [*Sístole atrial*], [abertas], [fechadas], [Último terço da diástole. Completa *cerca de 20%* do enchimento.],
  [*Contração isovolumétrica*], [*fechadas*], [*fechadas*], [*0,02–0,03 s.* A pressão sobe sem mudar o volume. Começa com o fechamento das AV (B1).],
  [*Ejeção rápida*], [fechadas], [abertas], [A aórtica abre quando o VE passa de *≈80 mmHg* (o VD, de ≈8 mmHg). Sai *70%* do volume no primeiro terço da ejeção.],
  [*Ejeção lenta*], [fechadas], [abertas], [Sai o restante (30%) nos dois terços finais.],
  [*Relaxamento isovolumétrico*], [*fechadas*], [*fechadas*], [*0,03–0,06 s.* Começa com o fechamento das semilunares (B2) e termina quando as AV abrem.],
  tamanho: 9pt,
)

== Volumes e fração de ejeção

No fim da diástole o VE tem cerca de 120 mL; ejeta ≈70 mL e sobram ≈50 mL. A razão entre o que sai e o que havia é a *fração de ejeção*, ≈60% (#vf("t-volumes")).

#tabela(rotulo: "t-volumes", titulo: [Volumes do ventrículo esquerdo.], (1fr, auto, 1.3fr), ([Volume do VE em repouso], [Valor], [Pode chegar a]),
  [Volume diastólico final (VDF)], [*110–120 mL*], [150–180 mL com grande enchimento],
  [Débito sistólico (VS)], [*≈70 mL*], [Mais que o dobro, mexendo nos dois lados],
  [Volume sistólico final (VSF)], [*40–50 mL*], [10–20 mL com contração forte],
  [Fração de ejeção (VS/VDF)], [*≈60%*], [É o índice clínico mais usado da função sistólica (ecocardiograma)],
)

= Valvas cardíacas

As valvas AV têm cúspides presas por *cordas tendíneas* aos *músculos papilares*; as semilunares não têm cordas (#vf("g9_09")).

#fig("g9_09", [Valvas mitral e aórtica: cúspides, cordas tendíneas e músculos papilares.])

- *Atrioventriculares (tricúspide e mitral):* impedem o refluxo do ventrículo para o átrio na sístole. São finas e quase não precisam de refluxo para fechar.
- *Músculos papilares e cordas tendíneas:* contraem junto com o ventrículo, mas *não ajudam a fechar a valva*. Eles puxam as cúspides para baixo e *impedem que abaulem demais* para o átrio. Ruptura de corda ou de papilar causa *insuficiência mitral* grave.
- *Semilunares (aórtica e pulmonar):* trabalham sob pressão alta, fecham de forma *abrupta* e deixam passar o sangue em *alta velocidade*. Sofrem mais desgaste mecânico.

#essencial(titulo: "Bulhas: a ponte com a Semiologia")[
  *B1* é o fechamento das valvas AV: início da sístole, coincide com o ictus e o pulso carotídeo. *B2* é o fechamento das semilunares, no fim da sístole. A abertura das valvas normais não faz som. *B3* é o enchimento rápido; *B4*, a sístole atrial contra um ventrículo rígido.
]

= Alça pressão-volume

A alça pressão-volume (#vf("g9_11")) resume o ciclo do VE em quatro lados:

+ *Enchimento* (A→B): o volume sobe de ≈50 para ≈120 mL com pouca pressão.
+ *Contração isovolumétrica* (B→C): a pressão sobe a ≈80 mmHg com volume constante.
+ *Ejeção* (C→D): o volume cai ≈70 mL e a pressão chega a ≈120 mmHg.
+ *Relaxamento isovolumétrico* (D→A): a pressão cai com volume constante.

#fig("g9_11", [Alça pressão-volume do VE. A área interna é o trabalho sistólico externo.])

*Pré-carga* é a tensão no fim da diástole (VDF ou pressão diastólica final). *Pós-carga* é a pressão contra a qual o ventrículo ejeta (pressão arterial). A área da alça é o *trabalho sistólico externo*.

= Regulação do bombeamento

O coração em repouso bombeia *4–6 L/min* e, no exercício intenso, *4 a 7 vezes* mais. Dois mecanismos regulam isso: a regulação *intrínseca* (Frank-Starling) e o *sistema nervoso autônomo* (#vf("t-autonomico")).

== Mecanismo de Frank-Starling

*Quanto mais o músculo é estirado no enchimento, maior a força de contração e maior o volume ejetado.* O estiramento aproxima actina e miosina do grau ótimo de sobreposição. Na prática, o coração *bombeia todo o sangue que chega* das veias, dentro dos limites fisiológicos. O estiramento do átrio direito ainda *aumenta a FC em 10–20%*. As curvas de função ventricular mostram isso (#vf("g9_13")).

#fig("g9_13", [Curvas de função ventricular: o débito de cada ventrículo cresce com a pressão atrial (pré-carga).])

#tabela(rotulo: "t-autonomico", titulo: [Efeitos do simpático e do vago sobre o coração.], (auto, 1fr, 1fr), ([], [Simpático], [Parassimpático (vago)]),
  [*Frequência*], [70 → *180–200 bpm* (raro 250)], [Pode parar por segundos; o coração *escapa* a *20–40 bpm*],
  [*Força*], [*Dobra* a força de contração], [Reduz só *20–30%* (as fibras vagais vão mais aos *átrios*)],
  [*Débito*], [Aumenta *2–3 vezes* além do Frank-Starling], [Pode cair *50% ou mais*],
  [*Tônus basal*], [Mantém o bombeamento ≈30% acima do que seria sem ele], [Predomina em repouso no nó sinusal],
)

== Íons e temperatura

- *Hiperpotassemia:* coração *dilatado e flácido*, FC menor e bloqueio AV. K⁺ de *8–12 mEq/L* (2–3 vezes o normal) pode matar. O K⁺ alto despolariza parcialmente a membrana e enfraquece o potencial de ação.
- *Ca²⁺ e temperatura:* hipercalcemia leva à *contração espástica*; febre aumenta a FC até o dobro e hipotermia a reduz muito.
'''

VALORES = [
    ("Potencial de repouso ventricular", "−85 a −90 mV", "Pico do PA ≈ +20 mV"),
    ("Duração do potencial de ação", "0,2 s (átrio) · 0,3 s (ventrículo)", "Platô pelos canais lentos de Ca²⁺"),
    ("Período refratário absoluto", "0,25–0,30 s (ventrículo)", "Relativo: +0,05 s · átrio: 0,15 s"),
    ("Velocidade de condução", "0,3–0,5 m/s (músculo) · 4 m/s (Purkinje)", ""),
    ("Duração do ciclo a 72 bpm", "0,833 s", "Sístole ≈ 0,4 do ciclo"),
    ("Contração isovolumétrica", "0,02–0,03 s", "Valvas todas fechadas"),
    ("Relaxamento isovolumétrico", "0,03–0,06 s", "Valvas todas fechadas"),
    ("Pressão para abrir a aórtica", "≈ 80 mmHg (VE) · ≈ 8 mmHg (VD)", ""),
    ("Contribuição da sístole atrial", "≈ 20% do enchimento", "80% entra antes da contração atrial"),
    ("VDF · VS · VSF", "110–120 · 70 · 40–50 mL", "FE ≈ 60%"),
    ("Pressão aórtica", "120/80 mmHg", "Pulmonar ≈ 1/6 da aórtica"),
    ("Onda a atrial", "AD 4–6 · AE 7–8 mmHg", ""),
    ("Débito cardíaco em repouso", "4–6 L/min", "Exercício: 4–7 vezes mais"),
    ("FC máxima por simpático", "180–200 bpm", "Escape vagal: 20–40 bpm"),
    ("K⁺ que pode matar", "8–12 mEq/L", "2–3 vezes o normal"),
]

CLINICA = [
    ("Insuficiência cardíaca e fração de ejeção", "A **FE** do ecocardiograma separa a insuficiência cardíaca com FE reduzida (contração fraca, VSF alto) da com FE preservada (ventrículo rígido, enche mal). A queda da FE é um dos marcadores de pior prognóstico."),
    ("Ruptura de músculo papilar", "No infarto da parede inferior ou posterior, a necrose do músculo papilar faz a cúspide mitral abaular para o átrio na sístole: **insuficiência mitral aguda**, edema agudo de pulmão e sopro holossistólico novo."),
    ("Hiperpotassemia", "Na insuficiência renal o K⁺ sobe e o coração fica flácido, com bradicardia e bloqueios. No ECG: **onda T apiculada**, depois QRS alargado. É emergência."),
    ("Taquicardia e enchimento", "Como a diástole encurta mais que a sístole, FC muito alta reduz o enchimento e o débito. Isso explica sintomas de baixo débito nas taquiarritmias (Porto, Fig. 47.6)."),
]

PEGADINHAS = [
    "Músculos papilares **não fecham** a valva AV: eles impedem o abaulamento excessivo das cúspides.",
    "Nas fases **isovolumétricas** todas as quatro valvas estão fechadas.",
    "A contração atrial contribui só com **≈20%** do enchimento; o grosso entra na fase de enchimento rápido.",
    "A taquicardia encurta **mais a diástole** que a sístole.",
    "O vago age sobretudo nos **átrios** (FC); o simpático, em átrios e ventrículos (FC e força).",
    "A onda **c** atrial é o abaulamento das valvas AV; a **v**, o enchimento atrial com as AV fechadas.",
    "Hiperpotassemia: coração **flácido**. Hipercalcemia: contração **espástica**.",
]

GLOSSARIO = [
    ("Sincício funcional", "Conjunto de células que se comportam como uma só, porque o estímulo passa livre entre elas pelas junções comunicantes."),
    ("Disco intercalado", "Membrana entre duas células miocárdicas, com junções comunicantes e desmossomos."),
    ("Platô", "Fase 2 do potencial de ação: membrana despolarizada por 0,2–0,3 s."),
    ("Período refratário", "Intervalo em que a célula não responde a novo estímulo (absoluto) ou só a estímulo forte (relativo)."),
    ("Túbulos T", "Invaginações do sarcolema que levam o potencial de ação para dentro da célula."),
    ("Receptor de rianodina (RyR)", "Canal do retículo sarcoplasmático que libera Ca²⁺ quando estimulado pelo Ca²⁺ que entra."),
    ("SERCA2", "Bomba de Ca²⁺ do retículo sarcoplasmático; recapta Ca²⁺ e permite o relaxamento."),
    ("Pré-carga", "Grau de estiramento do músculo no fim da diástole (VDF, pressão diastólica final)."),
    ("Pós-carga", "Pressão contra a qual o ventrículo ejeta (pressão na aorta)."),
    ("Fração de ejeção", "Fração do VDF ejetada a cada sístole (VS/VDF), normal ≈ 60%."),
    ("Diástase", "Fase de enchimento lento, no terço médio da diástole."),
    ("Incisura", "Pequeno entalhe na curva de pressão aórtica no fechamento da valva aórtica."),
    ("Frank-Starling", "Lei intrínseca: mais enchimento → mais força → mais volume ejetado."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 9 · PDF p. 365–377", "Fisiologia do músculo cardíaco: sincício, potencial de ação, acoplamento"),
    ("Guyton & Hall", "Cap. 9 · PDF p. 377–395", "Ciclo cardíaco (Fig. 9.8), valvas (Fig. 9.9), alça pressão-volume (Fig. 9.11)"),
    ("Guyton & Hall", "Cap. 9 · PDF p. 395–405", "Regulação: Frank-Starling, autonômico, íons, temperatura"),
    ("Porto", "Cap. 46 · PDF p. 520–536", "Revisão clínica do ciclo e correlação com bulhas (Fig. 46.6 e 46.7)"),
]

BASICOS = [
    ("Por que o miocárdio funciona como sincício?", "Os **discos intercalados** têm **junções comunicantes** de baixa resistência; o potencial de ação passa livre de célula a célula.", "g9_02"),
    ("O que liga eletricamente o sincício atrial ao ventricular?", "Somente o **feixe AV**. O resto é separado por tecido fibroso ao redor das valvas."),
    ("Quais canais produzem o platô do potencial de ação ventricular?", "**Canais lentos de Ca²⁺ (tipo L)** abertos + **queda da permeabilidade ao K⁺** (cerca de 5 vezes).", "g9_05"),
    ("Qual a importância do período refratário longo do miocárdio?", "Impede a **somação e o tétano**: o coração relaxa antes de poder contrair de novo.", "g9_06"),
    ("Explique a liberação de cálcio induzida por cálcio.", "O Ca²⁺ que entra pelos canais tipo L dos túbulos T ativa os **receptores de rianodina** do retículo sarcoplasmático, que liberam muito mais Ca²⁺.", "g9_07"),
    ("Por que a força cardíaca depende do Ca²⁺ extracelular?", "O retículo sarcoplasmático cardíaco é pouco desenvolvido; parte importante do Ca²⁺ vem do **líquido extracelular** pelos túbulos T."),
    ("Quais mecanismos retiram o Ca²⁺ do citosol no relaxamento?", "**SERCA2** (volta ao retículo), **trocador Na⁺/Ca²⁺** e **bomba de Ca²⁺** da membrana."),
    ("Estado das valvas na contração isovolumétrica?", "**Todas fechadas**: AV já fecharam (B1) e semilunares ainda não abriram."),
    ("Quando abre a valva aórtica?", "Quando a pressão do VE passa de **≈80 mmHg** (a diastólica aórtica). A pulmonar abre com ≈8 mmHg no VD."),
    ("Quanto do enchimento ventricular vem da sístole atrial?", "Cerca de **20%**. 80% entram antes, sobretudo no enchimento rápido."),
    ("Dê VDF, VS, VSF e FE normais do VE.", "**VDF 110–120 mL · VS ≈70 mL · VSF 40–50 mL · FE ≈60%**."),
    ("O que causam as ondas a, c e v da pressão atrial?", "**a** = contração atrial · **c** = abaulamento das AV no início da sístole · **v** = enchimento atrial com AV fechadas.", "g9_08"),
    ("Qual a função dos músculos papilares?", "Puxar as cúspides AV para **impedir que abaulem** demais para o átrio na sístole. Não fecham a valva.", "g9_09"),
    ("Enuncie o mecanismo de Frank-Starling.", "Quanto **maior o enchimento** (estiramento), **maior a força** de contração e o volume ejetado: o coração bombeia o que recebe.", "g9_13"),
    ("Efeito máximo do simpático sobre a FC e o débito?", "FC até **180–200 bpm**; força dobra; débito **2–3 vezes** maior.", "g9_15"),
    ("Por que o vago reduz pouco a força de contração?", "As fibras vagais vão principalmente aos **átrios**; reduzem a força só **20–30%**."),
    ("Efeito da hiperpotassemia no coração?", "Coração **dilatado e flácido**, bradicardia, bloqueio AV; 8–12 mEq/L pode matar."),
    ("O que significa a área dentro da alça pressão-volume?", "O **trabalho sistólico externo** do ventrículo.", "g9_11"),
    ("Defina pré-carga e pós-carga.", "**Pré-carga:** estiramento no fim da diástole (VDF). **Pós-carga:** pressão contra a qual o ventrículo ejeta (pressão arterial)."),
]

LACUNAS = [
    ("O potencial de ação do ventrículo dura cerca de {{c1::0,3}} s, e o do átrio cerca de {{c2::0,2}} s.", ""),
    ("O período refratário absoluto do ventrículo dura {{c1::0,25–0,30 s}}; o relativo, mais {{c2::0,05 s}}.", ""),
    ("A condução no músculo é de {{c1::0,3–0,5}} m/s; nas fibras de Purkinje chega a {{c2::4}} m/s.", ""),
    ("A 72 bpm o ciclo cardíaco dura {{c1::0,833}} s e a sístole ocupa cerca de {{c2::40%}} do ciclo.", ""),
    ("A contração isovolumétrica dura {{c1::0,02–0,03}} s e o relaxamento isovolumétrico {{c2::0,03–0,06}} s.", ""),
    ("No primeiro terço da ejeção sai cerca de {{c1::70%}} do volume ejetado (ejeção {{c2::rápida}}).", ""),
    ("Fração de ejeção = {{c1::volume sistólico}} / {{c2::volume diastólico final}} ≈ {{c3::60%}}.", ""),
    ("B1 corresponde ao fechamento das valvas {{c1::atrioventriculares}}; B2, ao das {{c2::semilunares}}.", ""),
    ("A pressão na artéria pulmonar é cerca de {{c1::1/6}} da pressão aórtica.", ""),
    ("O estiramento do átrio direito aumenta a FC em {{c1::10–20%}}, somando-se ao Frank-Starling.", ""),
    ("O débito cardíaco só cai com o aumento da pós-carga quando a PA média passa de {{c1::160}} mmHg.", ""),
]

OCLUSOES = [
    ("g9_08", "Contração isovolumétrica", "Que fase do ciclo está oculta?", "Contração isovolumétrica"),
    ("g9_08", "Ejeção", "Que fase do ciclo está oculta?", "Ejeção"),
    ("g9_08", "Relaxamento isovolumétrico", "Que fase do ciclo está oculta?", "Relaxamento isovolumétrico"),
    ("g9_08", "Enchimento rápido", "Que fase do ciclo está oculta?", "Enchimento rápido"),
    ("g9_08", "Sístole atrial", "Que fase do ciclo está oculta?", "Sístole atrial"),
    ("g9_09", "Cordas tendíneas", "Que estrutura está oculta?", "Cordas tendíneas"),
    ("g9_09", "Músculos papilares", "Que estrutura está oculta?", "Músculos papilares"),
    ("g9_11", "Período de ejeção", "Que fase da alça está oculta?", "Período de ejeção"),
    ("g9_11", "Relaxamento isovolumétrico", "Que fase da alça está oculta?", "Relaxamento isovolumétrico"),
    ("g9_11", "Período de enchimento", "Que fase da alça está oculta?", "Período de enchimento"),
    ("g9_01", "Valva mitral", "Que valva está oculta?", "Valva mitral"),
    ("g9_01", "Valva tricúspide", "Que valva está oculta?", "Valva tricúspide"),
    ("g9_01", "Valva aórtica", "Que valva está oculta?", "Valva aórtica"),
    ("g9_01", "Valva pulmonar", "Que valva está oculta?", "Valva pulmonar"),
]
