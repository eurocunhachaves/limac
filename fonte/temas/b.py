CODIGO = "b"
SLUG = "b-excitacao-ritmica"
TITULO = "Excitação rítmica do coração"
AREA = "Fisiologia"
FONTES = [
    "Guyton & Hall, 14ª ed., cap. 10 (PDF p. 406–426)",
    "Porto, Semiologia Médica, 8ª ed., cap. 46 (sistema excitocondutor, Fig. 46.5)",
]

ESSENCIAL = [
    "Caminho do impulso: **nó sinusal → vias internodais → nó AV → feixe AV (His) → ramos direito e esquerdo → fibras de Purkinje → miocárdio**.",
    "O **nó sinusal** é o marca-passo porque dispara mais rápido (**70–80/min**) que o nó AV (**40–60/min**) e as fibras de Purkinje (**15–40/min**).",
    "Automatismo: o repouso do nó sinusal é **−55 a −60 mV**, os canais rápidos de Na⁺ ficam inativados, e a entrada lenta de Na⁺ (**corrente funny**) leva a membrana ao limiar de **−40 mV**, quando abrem os **canais de Ca²⁺ tipo L**.",
    "O **nó AV retarda** o impulso (≈0,13 s no nó e no feixe; **0,16 s** desde o nó sinusal) para os átrios se esvaziarem antes da sístole ventricular. Causa: poucas junções comunicantes.",
    "**Purkinje** conduz a **1,5–4 m/s** e despolariza todo o ventrículo em ≈0,06 s: contração síncrona.",
    "**Vago (ACh):** abre canais de K⁺, hiperpolariza e reduz FC e condução AV. **Simpático (noradrenalina, β1):** aumenta a permeabilidade a Na⁺/Ca²⁺, acelera FC e condução e aumenta a força.",
]

CORPO = r'''
= O sistema excitatório e condutor

O coração bate cerca de 100.000 vezes por dia graças a um sistema especializado que *gera* o impulso e o *conduz* rapidamente. Esse sistema faz os átrios contraírem cerca de *1/6 de segundo antes* dos ventrículos e faz todas as partes dos ventrículos contraírem quase ao mesmo tempo. O caminho do impulso aparece na #vf("g10_01") e segue esta ordem:

+ *Nó sinusal (sinoatrial):* faixa de ≈3 × 15 × 1 mm na parede posterolateral superior do *átrio direito*, logo abaixo da desembocadura da *veia cava superior*. Suas fibras quase não têm filamentos contráteis e se ligam direto às fibras atriais.
+ *Vias internodais* (anterior, média e posterior) e *feixe interatrial anterior* (de Bachmann), que leva o impulso ao átrio esquerdo.
+ *Nó AV:* na parede posterior do átrio direito, *atrás da valva tricúspide*.
+ *Feixe AV (de His):* atravessa o tecido fibroso entre átrios e ventrículos e desce 5–15 mm no septo.
+ *Ramos direito e esquerdo* e *fibras de Purkinje*, sob o endocárdio, até o ápice e de volta à base.

#fig("g10_01", [O nó sinusal, as vias internodais, o nó AV, o feixe AV e seus ramos.])

= Automatismo do nó sinusal

A fibra do nó sinusal não tem um repouso estável. Entre um batimento e outro, o potencial sobe devagar até o limiar e dispara sozinho (#vf("g10_02")). Esse é o *automatismo* (autoexcitação). Três diferenças em relação à fibra ventricular explicam isso:

- Repouso menos negativo, *−55 a −60 mV*, porque a membrana é permeável a Na⁺ e Ca²⁺.
- Nesse nível os *canais rápidos de Na⁺ estão inativados*. Só os canais lentos de Ca²⁺ conseguem gerar o potencial de ação, que por isso sobe e desce mais devagar.
- Existe uma entrada contínua de Na⁺ pelos canais da *corrente funny* (I#sub[f]).

#fig("g10_02", [Descarga rítmica de uma fibra do nó sinusal comparada com uma fibra ventricular. Note o repouso mais alto e a subida lenta até o limiar.])

== O ciclo de uma célula marca-passo

#tabela((auto, 1fr), ([Etapa], [O que acontece]),
  [*1. Despolarização lenta (fase 4)*], [Entrada de Na⁺ pela corrente funny (e de Ca²⁺). O potencial sobe de −55/−60 mV até o *limiar de ≈−40 mV*.],
  [*2. Potencial de ação*], [No limiar abrem os *canais de Ca²⁺ do tipo L*. A subida é lenta, porque não há canal rápido de Na⁺ disponível.],
  [*3. Repolarização*], [Os canais de Ca²⁺ se inativam em *100–150 ms* e abrem muitos *canais de K⁺*.],
  [*4. Hiperpolarização*], [O K⁺ continua saindo por alguns décimos de segundo e leva a membrana a −55/−60 mV. Depois os canais de K⁺ fecham e o ciclo recomeça.],
)

= Condução pelo coração

== Átrios e nó AV

No músculo atrial o impulso anda a *0,3 m/s*; nas vias internodais e no feixe de Bachmann, a *≈1 m/s*. Ele chega ao nó AV *0,03 s* depois de sair do nó sinusal.

O nó AV existe para *retardar* o impulso e dar tempo de os átrios esvaziarem nos ventrículos. Os tempos de cada trecho estão na #vf("g10_03") e na #vf("t-atrasos"). O atraso vem de as fibras nodais e de transição terem *poucas junções comunicantes*, o que cria alta resistência à passagem dos íons. Algumas fibras nodais conduzem 150 vezes mais devagar que as de Purkinje.

#fig("g10_03", [Organização do nó AV. Os números são o tempo (s) desde a origem do impulso no nó sinusal.])

#tabela(rotulo: "t-atrasos", titulo: [Tempo que o impulso leva em cada trecho até o ventrículo.], (1fr, auto), ([Trecho], [Tempo]),
  [Nó sinusal → nó AV], [0,03 s],
  [Dentro do nó AV], [*0,09 s*],
  [Porção penetrante do feixe AV], [0,04 s],
  [*Total no sistema AV*], [*0,13 s*],
  [*Total do nó sinusal ao ventrículo*], [*0,16 s*],
)

== Feixe AV, ramos e Purkinje

- As fibras de *Purkinje* são muito grandes e têm junções comunicantes muito permeáveis. Conduzem a *1,5–4,0 m/s*, cerca de *6 vezes* o músculo ventricular. Quase não têm miofibrilas, então contraem pouco.
- O *feixe AV é unidirecional*: normalmente não conduz do ventrículo para o átrio, o que evita a reentrada.
- Fora do feixe AV, átrios e ventrículos são separados por uma *barreira fibrosa contínua* que funciona como isolante. Uma ponte muscular anormal (*via acessória*) permite a reentrada e causa arritmias graves.
- Do septo até as terminações de Purkinje passam só *0,03 s*. No músculo ventricular o impulso volta a 0,3–0,5 m/s e leva mais *0,03 s* do endocárdio ao epicárdio. Do início dos ramos à última fibra ventricular são *≈0,06 s* (#vf("g10_04")).

#fig("g10_04", [Tempo de chegada do impulso (s após o disparo do nó sinusal) em cada região. Note o atraso no nó AV e a ativação quase simultânea dos ventrículos.])

#essencial(titulo: "Por que a contração precisa ser síncrona")[
  Como a primeira e a última fibra ventricular se excitam com apenas *0,03–0,06 s* de diferença, os dois ventrículos contraem juntos e geram pressão de forma eficiente. Quando a condução fica lenta, como no bloqueio de ramo, a eficácia do bombeamento cai *20–30%*. Os *ressincronizadores* (marca-passos biventriculares) corrigem isso na insuficiência cardíaca.
]

= Hierarquia dos marca-passos

O nó sinusal comanda porque *dispara primeiro*: cada impulso sinusal descarrega o nó AV e o Purkinje antes que eles atinjam o próprio limiar (#vf("t-freq")). *Marca-passo ectópico* é qualquer marca-passo fora do nó sinusal. Aparece quando outro tecido fica mais rápido que o nó sinusal ou quando o impulso sinusal é bloqueado.

#tabela(rotulo: "t-freq", titulo: [Frequência de disparo próprio de cada tecido.], (1fr, 1fr), ([Tecido], [Frequência intrínseca]),
  [*Nó sinusal*], [*70–80/min*],
  [Nó AV], [40–60/min],
  [Fibras de Purkinje], [15–40/min],
)

== Bloqueio AV e síndrome de Stokes-Adams

No *bloqueio AV total*, os átrios seguem no ritmo sinusal e um novo marca-passo no *sistema de Purkinje* assume os ventrículos a *15–40 bpm*. Mas o Purkinje vinha sendo "sobrecarregado" pelos impulsos sinusais rápidos e está *suprimido*: demora *5–20 s* para começar a disparar. Nesse intervalo os ventrículos não bombeiam e a pessoa *desmaia após 4–5 s*. Isso é a *síndrome de Stokes-Adams*, que pode matar se o atraso for longo.

= Controle autonômico

Os dois sistemas chegam ao coração por caminhos diferentes (#vf("g9_14")):

- *Parassimpático (vago):* vai principalmente aos *nós SA e AV*, menos ao músculo atrial e muito pouco ao ventricular.
- *Simpático:* vai a *todas as partes* do coração, com forte presença no músculo ventricular.

Por isso o vago age sobretudo na *frequência* e na *condução AV*, enquanto o simpático muda também a *força de contração*. Em repouso predomina o tônus vagal. Os mecanismos estão na #vf("t-auto").

#fig("g9_14", [Inervação simpática e parassimpática (vagos) do coração.])

#tabela(rotulo: "t-auto", titulo: [Como o vago e o simpático agem no coração.], (auto, 1fr, 1fr), ([], [Vago (parassimpático)], [Simpático]),
  [*Mediador*], [Acetilcolina (receptor muscarínico)], [Noradrenalina (receptor *β1*)],
  [*Mecanismo*], [*↑ permeabilidade ao K⁺* → hiperpolarização: o nó sinusal vai a *−65 a −75 mV* e demora mais para chegar ao limiar], [*↑ permeabilidade ao Na⁺ e Ca²⁺* → repouso mais positivo e fase 4 mais rápida],
  [*Nó sinusal*], [↓ FC (pode cair à metade)], [↑ FC (pode quase *triplicar*)],
  [*Nó AV*], [↓ condução; estímulo forte *bloqueia*], [↑ condução, encurta o tempo AV],
  [*Força*], [Pouco efeito (poucas fibras no ventrículo)], [Até *2 vezes* mais força (mais Ca²⁺)],
  [*Estímulo forte*], [Ventrículos param 5–20 s e surge *escape ventricular* a 15–40 bpm], [Taquicardia e contração vigorosa],
)
'''

VALORES = [
    ("Nó sinusal: dimensões", "≈ 3 × 15 × 1 mm", "Átrio direito, junto à veia cava superior"),
    ("Repouso do nó sinusal", "−55 a −60 mV", "Ventrículo: −85 a −90 mV"),
    ("Limiar do nó sinusal", "≈ −40 mV", "Abrem os canais de Ca²⁺ tipo L"),
    ("Repouso do nó sinusal com vago", "−65 a −75 mV", "Hiperpolarização por K⁺"),
    ("Frequência intrínseca", "SA 70–80 · AV 40–60 · Purkinje 15–40/min", ""),
    ("Condução no músculo atrial", "0,3 m/s", "Vias internodais ≈ 1 m/s"),
    ("Condução no Purkinje", "1,5–4,0 m/s", "≈ 6 vezes o músculo ventricular"),
    ("Condução no músculo ventricular", "0,3–0,5 m/s", ""),
    ("Nó sinusal → nó AV", "0,03 s", ""),
    ("Atraso no nó AV + feixe penetrante", "0,09 + 0,04 = 0,13 s", ""),
    ("Nó sinusal → ventrículo", "0,16 s", "≈ intervalo PR"),
    ("Ramos → última fibra ventricular", "≈ 0,06 s", "Contração síncrona"),
    ("Supressão do Purkinje no bloqueio", "5–20 s", "Desmaio após 4–5 s (Stokes-Adams)"),
]

CLINICA = [
    ("Síndrome de Stokes-Adams", "No bloqueio AV total súbito, o Purkinje demora 5–20 s para assumir. O paciente perde a consciência e pode convulsionar. No Brasil a **doença de Chagas** é causa frequente de bloqueio AV e de Stokes-Adams (Porto)."),
    ("Via acessória (Wolff-Parkinson-White)", "Uma ponte muscular atravessa a barreira fibrosa fora do feixe AV. O impulso pula o retardo do nó AV (PR curto) e pode reentrar, causando taquicardias."),
    ("Marca-passo artificial e ressincronização", "O marca-passo trata bradicardias e bloqueios. O ressincronizador (biventricular) devolve a contração síncrona em corações dilatados."),
    ("Fármacos", "**Atropina** bloqueia o vago e acelera a FC. **Betabloqueadores** bloqueiam β1 e reduzem FC e condução AV. A **ivabradina** bloqueia a corrente funny e reduz a FC sem mexer na força."),
]

PEGADINHAS = [
    "No nó sinusal o potencial de ação depende de **Ca²⁺** (tipo L), não do canal rápido de Na⁺, que está inativado a −55 mV.",
    "O nó sinusal é o marca-passo por ser o **mais rápido**, não por ser o único com automatismo.",
    "O **maior atraso** está no nó AV (0,09 s), não no feixe de His.",
    "O vago age por **hiperpolarização** (↑ K⁺), e não por bloquear canais de Na⁺.",
    "O feixe AV conduz em **um só sentido** (átrio → ventrículo).",
    "Purkinje é a fibra **mais rápida**; nó AV, a **mais lenta**.",
]

GLOSSARIO = [
    ("Automatismo", "Capacidade de uma célula gerar potenciais de ação sozinha, sem estímulo externo."),
    ("Corrente funny (I-f)", "Entrada lenta de Na⁺ por canais HCN que despolariza a célula marca-passo na fase 4."),
    ("Limiar", "Potencial em que se abrem os canais que geram o potencial de ação (≈ −40 mV no nó sinusal)."),
    ("Hiperpolarização", "Potencial mais negativo que o repouso, por saída de K⁺."),
    ("Vias internodais", "Feixes atriais de condução rápida entre o nó sinusal e o nó AV (anterior, média, posterior)."),
    ("Feixe de Bachmann", "Feixe interatrial anterior; leva o impulso ao átrio esquerdo."),
    ("Feixe AV (de His)", "Única conexão elétrica normal entre átrios e ventrículos."),
    ("Marca-passo ectópico", "Marca-passo localizado fora do nó sinusal."),
    ("Escape ventricular", "Ritmo de 15–40 bpm gerado pelo Purkinje quando o impulso sinusal não chega."),
    ("Stokes-Adams", "Síncope por pausa ventricular no início de um bloqueio AV total."),
]

LEITURA = [
    ("Guyton & Hall", "Cap. 10 · PDF p. 407–418", "Nó sinusal e automatismo (Fig. 10.2), nó AV (Fig. 10.3), Purkinje (Fig. 10.4)"),
    ("Guyton & Hall", "Cap. 10 · PDF p. 418–425", "Marca-passos ectópicos, Stokes-Adams, controle autonômico"),
    ("Porto", "Cap. 46 · PDF p. 525–527", "Sistema excitocondutor e inervação (Fig. 46.5)"),
    ("Porto", "Cap. 47 · PDF p. 557–560", "Repercussões clínicas das bradi e taquiarritmias (Fig. 47.6 e 47.7)"),
]

BASICOS = [
    ("Ordem de condução do impulso cardíaco?", "Nó sinusal → vias internodais → **nó AV** → feixe AV → ramos D e E → **Purkinje** → miocárdio.", "g10_01"),
    ("Onde fica o nó sinusal?", "Parede posterolateral superior do **átrio direito**, logo abaixo da desembocadura da **veia cava superior**."),
    ("Onde fica o nó AV?", "Parede posterior do átrio direito, **atrás da valva tricúspide**."),
    ("Por que o nó sinusal não usa os canais rápidos de Na⁺?", "Seu repouso é de **−55 a −60 mV**; nesse nível as comportas de inativação dos canais rápidos de Na⁺ ficam **fechadas**.", "g10_02"),
    ("O que causa a despolarização lenta (fase 4) do nó sinusal?", "Entrada de **Na⁺** pela **corrente funny** (e de Ca²⁺), até o limiar de **≈ −40 mV**."),
    ("Qual canal gera o potencial de ação do nó sinusal?", "**Canal de Ca²⁺ do tipo L** (lento)."),
    ("Como termina o potencial de ação nodal?", "Os canais de Ca²⁺ se inativam em **100–150 ms** e abrem muitos canais de **K⁺** (com hiperpolarização)."),
    ("Por que o nó sinusal é o marca-passo normal?", "Porque **dispara mais rápido** (70–80/min) e descarrega os outros tecidos antes que atinjam o próprio limiar."),
    ("Frequências intrínsecas do nó AV e do Purkinje?", "Nó AV **40–60/min** · Purkinje **15–40/min**."),
    ("Qual o atraso total do impulso do nó sinusal até o ventrículo?", "**0,16 s** (0,03 até o nó AV + 0,09 no nó + 0,04 no feixe penetrante).", "g10_03"),
    ("Por que a condução no nó AV é lenta?", "**Poucas junções comunicantes** entre as células: alta resistência à passagem de íons."),
    ("Velocidade de condução no Purkinje?", "**1,5–4 m/s**, cerca de 6 vezes o músculo ventricular.", "g10_04"),
    ("O que impede a reentrada do impulso do ventrículo para o átrio?", "O **feixe AV é unidirecional** e a **barreira fibrosa** isola átrios e ventrículos no resto."),
    ("O que é marca-passo ectópico?", "Qualquer marca-passo **fora do nó sinusal** (nó AV, Purkinje ou músculo)."),
    ("Explique a síndrome de Stokes-Adams.", "No bloqueio AV súbito o Purkinje está **suprimido** e leva **5–20 s** para disparar; sem fluxo cerebral o paciente **desmaia após 4–5 s**."),
    ("Mecanismo do efeito vagal no nó sinusal?", "ACh **aumenta a permeabilidade ao K⁺** → hiperpolarização (**−65 a −75 mV**) → mais tempo até o limiar → ↓ FC.", "g9_14"),
    ("Mecanismo do efeito simpático no nó sinusal?", "Noradrenalina em **β1** → ↑ permeabilidade a **Na⁺/Ca²⁺** → fase 4 mais rápida → ↑ FC; também ↑ condução e força."),
    ("Qual o efeito da estimulação vagal forte?", "Para o nó sinusal ou bloqueia o nó AV; após 5–20 s surge **escape ventricular** a 15–40 bpm."),
]

LACUNAS = [
    ("O repouso do nó sinusal é de {{c1::−55 a −60}} mV e o limiar de disparo, cerca de {{c2::−40}} mV.", ""),
    ("O nó sinusal dispara a {{c1::70–80}}/min, o nó AV a {{c2::40–60}}/min e o Purkinje a {{c3::15–40}}/min.", ""),
    ("O impulso chega ao nó AV {{c1::0,03}} s após sair do nó sinusal e atrasa {{c2::0,09}} s dentro do nó.", ""),
    ("O atraso total até o músculo ventricular é de {{c1::0,16}} s.", "Corresponde aproximadamente ao intervalo PR."),
    ("O Purkinje conduz a {{c1::1,5–4,0}} m/s; o músculo atrial, a {{c2::0,3}} m/s.", ""),
    ("A primeira e a última fibra ventricular se excitam com apenas {{c1::0,03–0,06}} s de diferença.", ""),
    ("O vago libera {{c1::acetilcolina}}, que aumenta a permeabilidade ao {{c2::K⁺}}.", ""),
    ("O simpático libera {{c1::noradrenalina}}, que age em receptores {{c2::β1}}.", ""),
    ("O feixe interatrial anterior, que leva o impulso ao átrio esquerdo, é o feixe de {{c1::Bachmann}}.", ""),
]

OCLUSOES = [
    ("g10_01", "Nó sinusal", "Que estrutura está oculta?", "Nó sinusal"),
    ("g10_01", "Nó AV", "Que estrutura está oculta?", "Nó AV"),
    ("g10_01", "Feixe AV", "Que estrutura está oculta?", "Feixe AV (de His)"),
    ("g10_01", "Feixes intemodais", "Que estrutura está oculta?", "Feixes (vias) internodais"),
    ("g10_01", "Ramo do feixe esquerdo", "Que estrutura está oculta?", "Ramo esquerdo do feixe"),
    ("g10_01", "Ramo do feixe direito", "Que estrutura está oculta?", "Ramo direito do feixe"),
    ("g10_02", "Limiar de descarga", "O que indica o rótulo oculto?", "Limiar de descarga (≈ −40 mV)"),
    ("g10_03", "Porção penetrante do feixe AV", "Que estrutura está oculta?", "Porção penetrante do feixe AV"),
    ("g10_03", "Fibras de transição", "Que estrutura está oculta?", "Fibras de transição"),
]
