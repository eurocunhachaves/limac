"""Tema b: Excitação rítmica do coração (Guyton & Hall, cap. 10)."""

SECTIONS = [
    ("1. O sistema excitocondutor", [
        ("fig", None, "fig_livro/g10_01.png", "Nó sinusal, vias internodais, nó AV, feixe AV e ramos (sistema de Purkinje).", 9),
        ("p", "Duas funções: <b>gerar</b> o impulso rítmico e <b>conduzi-lo</b> rápido. Resultado: os átrios contraem ≈ 1/6 s antes dos "
              "ventrículos, e todas as partes dos ventrículos contraem <b>quase ao mesmo tempo</b>. É um sistema sensível à isquemia."),
        ("table", [
            ["Estrutura", "Onde / como", "Detalhe que cai"],
            ["<b>Nó sinusal (SA)</b>", "Parede posterolateral superior do AD, logo abaixo e lateral à veia cava superior",
             "3 × 15 × 1 mm; fibras de 3 a 5 µm, quase sem miofibrilas; ligadas direto ao músculo atrial"],
            ["<b>Vias internodais</b>", "Anterior, média e posterior; <b>feixe de Bachmann</b> (interatrial anterior) leva ao AE",
             "≈ 1 m/s (músculo atrial comum ≈ 0,3 m/s)"],
            ["<b>Nó AV</b>", "Parede posterior do AD, atrás da valva tricúspide", "<b>Retarda</b> o impulso"],
            ["<b>Feixe AV (His)</b>", "Atravessa o esqueleto fibroso; desce 5 a 15 mm no septo", "<b>Condução unidirecional</b> (átrio → ventrículo)"],
            ["<b>Ramos e Purkinje</b>", "Ramos direito e esquerdo subendocárdicos → ápice → voltam à base; penetram 1/3 da parede",
             "Fibras grandes, <b>1,5 a 4 m/s</b>"],
        ], [3.2, 7.4, 6.8]),
    ]),
    ("2. Por que o nó sinusal dispara sozinho", [
        ("fig", None, "fig_livro/g10_02.png", "Potencial do nó sinusal comparado com o da fibra ventricular.", 8),
        ("ul", [
            "\"Repouso\" de <b>−55 a −60 mV</b> (ventrículo: −85 a −90), porque a membrana é naturalmente permeável a <b>Na⁺ e Ca²⁺</b>.",
            "A −55 mV os <b>canais rápidos de Na⁺ estão inativados</b>: quem faz o potencial são os <b>canais de Ca²⁺ tipo L (lentos)</b>. "
            "Por isso a subida e a repolarização são lentas.",
            "Entre os batimentos, o Na⁺ entra pela <b>corrente funny</b> e o potencial sobe devagar até o <b>limiar ≈ −40 mV</b>: abrem os canais tipo L e dispara.",
            "Fim: os canais de Ca²⁺ <b>inativam em 100 a 150 ms</b> e <b>abrem canais de K⁺</b> → repolariza e <b>hiperpolariza</b>. "
            "Os canais de K⁺ vão fechando, o vazamento de Na⁺/Ca²⁺ vence de novo e o ciclo recomeça.",
        ]),
        ("box", "Resumo em uma linha",
               "<b>Vazamento de Na⁺ (funny) → limiar −40 mV → Ca²⁺ tipo L dispara → K⁺ repolariza/hiperpolariza → recomeça.</b>"),
    ]),
    ("3. Condução: onde atrasa e onde acelera", [
        ("fig", None, "fig_livro/g10_04.png", "Tempo (em segundos) de chegada do impulso a cada região do coração.", 7),
        ("table", [
            ["Trecho", "Tempo acumulado", "Por quê"],
            ["Nó sinusal → nó AV", "0,03 s", "Vias internodais"],
            ["Dentro do nó AV", "+0,09 s (→ 0,12 s)", "Atraso nodal"],
            ["Feixe AV penetrante", "+0,04 s (→ 0,16 s)", "Atravessa o tecido fibroso"],
            ["Ramos → fim do Purkinje", "+0,03 s (→ ≈ 0,19 s)", "Purkinje 1,5 a 4 m/s"],
            ["Endocárdio → epicárdio", "+0,03 s (→ ≈ 0,22 s)", "Músculo 0,3 a 0,5 m/s, em espiral"],
        ], [5.0, 4.6, 7.8]),
        ("box", "O que a prova cobra", [
            "<b>Atraso AV total = 0,13 s</b> no nó + feixe; somando as vias internodais, <b>0,16 s</b> até o ventrículo. Serve para o átrio esvaziar antes da sístole.",
            "Causa do atraso: <b>poucas junções comunicantes</b> entre as células do nó (alta resistência).",
            "Causa da rapidez do Purkinje: fibras <b>grossas</b> e <b>junções comunicantes muito permeáveis</b>. Velocidade ≈ 6× o músculo e ≈ 150× algumas fibras do nó AV.",
            "Dos ramos até a última fibra ventricular: <b>≈ 0,06 s</b>. Contração <b>síncrona</b>; condução lenta nos ventrículos reduz o bombeamento em 20 a 30%.",
            "A <b>barreira fibrosa</b> isola átrio de ventrículo. Uma <b>via acessória</b> que a atravesse permite <b>reentrada</b> e arritmias graves.",
        ]),
    ]),
    ("4. Hierarquia dos marca-passos", [
        ("ul", [
            "Nó sinusal <b>70 a 80</b>/min · nó AV <b>40 a 60</b>/min · Purkinje <b>15 a 40</b>/min.",
            "O nó sinusal comanda porque é o <b>mais rápido</b>: descarrega o nó AV e o Purkinje antes que eles atinjam o próprio limiar.",
            "<b>Marca-passo ectópico</b>: outro local passa a disparar mais rápido que o sinusal (ou o impulso sinusal é bloqueado). Contração em sequência anormal.",
            "<b>Bloqueio AV total</b>: átrios seguem o sinusal; ventrículos passam a um ritmo do Purkinje de <b>15 a 40 bpm</b>.",
        ]),
        ("box", "Síndrome de Stokes-Adams",
               "No bloqueio AV súbito, o Purkinje estava <b>suprimido</b> pelo ritmo sinusal rápido (supressão por sobrecarga) e só assume após "
               "<b>5 a 20 s</b>. Sem bombeamento, a pessoa <b>desmaia após 4 a 5 s</b>. Se a pausa for longa, pode morrer."),
    ]),
    ("5. Controle autonômico do ritmo e da condução", [
        ("fig", None, "fig_livro/g9_14.png", "Inervação autonômica do coração: vagos sobre os nós SA e AV; simpáticos em todo o coração.", 7),
        ("table", [
            ["", "Parassimpático (vago)", "Simpático"],
            ["Distribuição", "<b>Nós SA e AV</b>; pouco músculo atrial; quase nada no ventrículo", "Todo o coração, forte no <b>ventrículo</b>"],
            ["Mediador", "<b>Acetilcolina</b>", "<b>Noradrenalina</b> → receptores <b>β1</b>"],
            ["Mecanismo", "↑ permeabilidade ao <b>K⁺</b> → <b>hiperpolariza</b> (SA vai a −65 a −75 mV) → demora a chegar ao limiar",
             "↑ permeabilidade a <b>Na⁺ e Ca²⁺</b> → rampa diastólica mais íngreme"],
            ["Nó sinusal", "FC ↓ (vago moderado: até metade); forte: para", "FC ↑ (máximo: quase <b>triplica</b>)"],
            ["Nó AV", "↓ excitabilidade da junção AV → atrasa; forte: <b>bloqueia</b>", "Condução AV mais rápida"],
            ["Força", "Pouco efeito", "Até <b>2×</b> (mais Ca²⁺)"],
        ], [2.8, 7.6, 7.0]),
        ("box", "Escape ventricular",
               "Com estímulo vagal muito forte o ventrículo pode parar por 5 a 20 s. Depois, um ponto do Purkinje (geralmente na porção "
               "septal do feixe AV) assume a <b>15 a 40 bpm</b>: é o <b>escape ventricular</b>."),
    ]),
]


G = "fig_livro/"
CARDS = [
    ("c", "O nó sinusal fica na parede {{c1::posterolateral superior do átrio direito}}, junto à {{c2::veia cava superior}}.", "", G + "g10_01.png"),
    ("c", "O nó AV fica na parede {{c1::posterior do átrio direito}}, atrás da valva {{c2::tricúspide}}."),
    ("c", "Repouso do nó sinusal: {{c1::−55 a −60 mV}}; do músculo ventricular: {{c2::−85 a −90 mV}}."),
    ("c", "O repouso do nó sinusal é menos negativo porque a membrana é permeável a {{c1::Na⁺ e Ca²⁺}}."),
    ("c", "A −55 mV os canais {{c1::rápidos de Na⁺}} estão {{c2::inativados}}; o potencial nodal depende dos canais {{c3::de Ca²⁺ tipo L}}."),
    ("c", "A despolarização diastólica lenta vem da {{c1::corrente funny}} (vazamento de {{c2::Na⁺}})."),
    ("c", "Limiar de disparo do nó sinusal: ≈ {{c1::−40 mV}}."),
    ("c", "Os canais de Ca²⁺ tipo L do nó inativam em {{c1::100 a 150 ms}}, e abrem canais de {{c2::K⁺}}, que causam {{c3::hiperpolarização}}."),
    ("c", "Velocidade no músculo atrial ≈ {{c1::0,3 m/s}}; nas vias internodais ≈ {{c2::1 m/s}}."),
    ("c", "O feixe {{c1::de Bachmann}} (interatrial anterior) leva o impulso ao {{c2::átrio esquerdo}}."),
    ("c", "Vias internodais: {{c1::anterior, média e posterior}}."),
    ("c", "Tempos: nó AV {{c1::0,03 s}}; atraso nodal {{c2::0,09 s}}; feixe penetrante {{c3::0,04 s}}; chegada ao septo {{c4::0,16 s}}.",
     ""),
    ("c", "O atraso AV se deve a {{c1::poucas junções comunicantes}} entre as células nodais.", "", G + "g10_03.png"),
    ("c", "Purkinje conduz a {{c1::1,5 a 4 m/s}}: ≈ {{c2::6×}} o músculo e ≈ {{c3::150×}} o nó AV."),
    ("c", "A condução rápida no Purkinje se deve a fibras {{c1::grandes}} com junções comunicantes {{c2::muito permeáveis}}."),
    ("c", "O feixe AV conduz de forma {{c1::unidirecional}} (átrio → ventrículo)."),
    ("c", "Fora do feixe AV, átrio e ventrículo são isolados pela {{c1::barreira fibrosa}}; uma {{c2::via acessória}} permite {{c3::reentrada}}."),
    ("c", "O feixe AV desce {{c1::5 a 15 mm}} no septo antes de se dividir nos ramos {{c2::direito e esquerdo}}."),
    ("c", "As fibras de Purkinje penetram ≈ {{c1::1/3}} da espessura do músculo ventricular."),
    ("c", "Dos ramos até a última fibra ventricular: ≈ {{c1::0,06 s}}; endocárdio → epicárdio: {{c2::0,03 s}}.", "", G + "g10_04.png"),
    ("c", "Frequências intrínsecas: nó SA {{c1::70 a 80}}/min; nó AV {{c2::40 a 60}}/min; Purkinje {{c3::15 a 40}}/min."),
    ("c", "Um marca-passo fora do nó sinusal é chamado {{c1::ectópico}}."),
    ("c", "No bloqueio AV súbito o Purkinje leva {{c1::5 a 20 s}} para assumir; o desmaio ocorre após {{c2::4 a 5 s}}: síndrome de {{c3::Stokes-Adams}}."),
    ("c", "A demora do Purkinje em assumir se deve à {{c1::supressão por sobrecarga}} pelo ritmo sinusal."),
    ("c", "Condução ventricular lenta reduz o bombeamento em {{c1::20 a 30%}}; trata-se com {{c2::ressincronização}}."),
    ("c", "O vago inerva principalmente os {{c1::nós SA e AV}}; o simpático, {{c2::todo o coração (forte no ventrículo)}}."),
    ("c", "A acetilcolina aumenta a permeabilidade ao {{c1::K⁺}} e leva o nó sinusal a {{c2::−65 a −75 mV}}.", "", "fig_livro/g9_14.png"),
    ("c", "Vago moderado reduz a FC até {{c1::a metade}}; vago forte pode {{c2::parar o nó sinusal ou bloquear o nó AV}}."),
    ("c", "Após parada vagal, o ritmo do Purkinje a 15 a 40 bpm é o {{c1::escape ventricular}}."),
    ("c", "Noradrenalina age em receptores {{c1::β1}} e aumenta a permeabilidade a {{c2::Na⁺ e Ca²⁺}}."),
    ("c", "Simpático máximo: FC quase {{c1::triplica}} e força até {{c2::dobra}}."),
    ("b", "Quais as duas funções do sistema excitocondutor?", "<b>Gerar</b> o impulso rítmico e <b>conduzi-lo</b> rápido, com átrio antes do ventrículo e ventrículos síncronos."),
    ("b", "Por que o potencial do nó sinusal sobe e desce devagar?", "Depende de <b>canais de Ca²⁺ tipo L</b> (lentos); os rápidos de Na⁺ estão inativados."),
    ("b", "Por que o nó sinusal comanda o ritmo?", "É o <b>mais rápido</b>: descarrega nó AV e Purkinje antes que atinjam o próprio limiar."),
    ("b", "Bloqueio AV total: o que fazem átrios e ventrículos?", "Átrios no ritmo <b>sinusal</b>; ventrículos no ritmo do <b>Purkinje</b> (15 a 40 bpm), sem relação."),
    ("b", "Qual o efeito do vago no nó AV?", "Reduz a excitabilidade das fibras de transição (<b>menor fator de segurança</b>): atrasa ou bloqueia."),
    ("b", "Qual o efeito do simpático no nó AV?", "<b>Acelera</b> a condução (↑ permeabilidade a Na⁺ e Ca²⁺)."),
    ("b", "Por que a via acessória causa arritmias?", "Atravessa a barreira fibrosa e permite <b>reentrada</b> do ventrículo para o átrio."),
]

# oclusão sobre a Figura 10.1 do Guyton (coordenadas em pixels da imagem original, 469 × 453)
OCC_IMG = [
    (G + "g10_01.png", (10, 158, 78, 202), "Qual estrutura?", "<b>Nó sinusal</b>."),
    (G + "g10_01.png", (0, 232, 86, 274), "Qual estrutura?", "<b>Feixes (vias) internodais</b>."),
    (G + "g10_01.png", (16, 299, 74, 323), "Qual estrutura?", "<b>Nó AV</b>."),
    (G + "g10_01.png", (348, 156, 424, 181), "Qual estrutura?", "<b>Feixe AV</b> (His)."),
    (G + "g10_01.png", (393, 230, 469, 291), "Qual estrutura?", "<b>Ramo esquerdo do feixe</b>."),
    (G + "g10_01.png", (407, 314, 469, 376), "Qual estrutura?", "<b>Ramo direito do feixe</b>."),
    (G + "g10_02.png", 'Fibra nodal sinusal', 'Qual registro?', '<b>Fibra do nó sinusal</b>: repouso −55 a −60 mV, despolarização lenta.'),
    (G + "g10_02.png", 'Limiar de descarga', 'Qual nível?', '<b>Limiar de descarga</b> (≈ −40 mV).'),
    (G + "g9_14.png", 'Vagos', 'Quais nervos?', '<b>Vagos</b>: parassimpático, sobretudo nos nós SA e AV.'),
    (G + "g9_14.png", 'Nervos simpáticos', 'Quais nervos?', '<b>Simpáticos</b>: átrios e ventrículos.'),
]

TOPIC = dict(
    code="b", slug="b-excitacao-ritmica", title="Excitação rítmica do coração",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 10",
    sections=SECTIONS, cards=CARDS, occ_img=OCC_IMG,
)
