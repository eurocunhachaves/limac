"""Tema a: O músculo cardíaco e as valvas cardíacas (Guyton & Hall, cap. 9; bulhas do cap. 23; focos: Porto)."""

SECTIONS = [
    ("1. O miocárdio em 5 linhas", [
        ("ul", [
            "Coração = <b>duas bombas em série</b> (direita → pulmão; esquerda → corpo). Átrio é bomba fraca de escorva; ventrículo é a força principal.",
            "Três tipos de músculo: <b>atrial</b>, <b>ventricular</b> (contraem como o esquelético, porém por mais tempo) e <b>fibras "
            "condutoras especializadas</b> (quase não contraem; geram e conduzem o impulso, tema b).",
            "<b>Discos intercalares</b> com <b>junções comunicantes (gap junctions)</b>: o potencial passa de célula a célula, então o miocárdio é um <b>sincício funcional</b>.",
            "São <b>dois sincícios</b> (atrial e ventricular) separados pelo <b>esqueleto fibroso</b>. A única ponte elétrica é o <b>feixe AV</b>, o que permite ao átrio contrair antes.",
            "<b>Torção do VE</b>: na sístole o ápice gira no sentido horário e a base no anti-horário; na diástole a \"destorção\" ajuda a sugar sangue.",
        ]),
        ("fig", None, "fig_livro/g9_02.png", "Discos intercalares e o sincício do músculo cardíaco.", 8),
    ]),
    ("2. Potencial de ação ventricular", [
        ("table", [
            ["Fase", "O que acontece"],
            ["0", "Abrem os <b>canais rápidos de Na⁺</b>: de −85 a ≈ +20 mV"],
            ["1", "Canais de Na⁺ fecham; saída transitória de K⁺"],
            ["2 · platô", "<b>Entra Ca²⁺ (canais tipo L, lentos)</b> e a <b>permeabilidade ao K⁺ cai ~5×</b>. Dura ≈ 0,2 s"],
            ["3", "Canais de Ca²⁺ fecham; K⁺ sai rápido e a fibra repolariza"],
            ["4", "Repouso ≈ −85 mV (−80 a −90)"],
        ], [2.4, 15.0]),
        ("fig", None, "fig_livro/g9_05.png", "Fases do potencial de ação da fibra ventricular e correntes iônicas.", 7),
        ("box", "O que a prova cobra", [
            "Platô = <b>Ca²⁺ entrando + K⁺ \"preso\"</b>. Por causa dele a contração dura até 15× a do músculo esquelético.",
            "<b>Período refratário absoluto do ventrículo: 0,25 a 0,30 s</b> (quase toda a contração) + relativo de 0,05 s. "
            "Resultado: <b>o coração não tetaniza</b> e as extrassístoles não somam força.",
            "Átrio tem refratário mais curto (≈ 0,15 s), por isso aguenta frequências muito altas (flutter, fibrilação).",
            "Condução: músculo <b>0,3 a 0,5 m/s</b>; Purkinje <b>até 4 m/s</b>.",
        ]),
    ]),
    ("3. Acoplamento excitação-contração", [
        ("fig", None, "fig_livro/g9_07.png", "Entrada de Ca²⁺ pelo túbulo T, liberação pelo RyR e recaptação pela SERCA2.", 12),
        ("ul", [
            "Potencial desce pelos <b>túbulos T</b> → abre <b>canais de Ca²⁺ tipo L</b> → o Ca²⁺ extracelular ativa os <b>receptores de "
            "rianodina (RyR2)</b> do retículo sarcoplasmático → liberação de muito mais Ca²⁺ (<b>liberação de Ca²⁺ induzida por Ca²⁺</b>).",
            "Ca²⁺ + <b>troponina C</b> → pontes cruzadas actina-miosina → contração.",
            "Relaxamento: <b>SERCA2</b> devolve Ca²⁺ ao retículo; o <b>trocador Na⁺/Ca²⁺</b> expulsa Ca²⁺ da célula; a <b>Na⁺/K⁺-ATPase</b> tira o Na⁺.",
        ]),
        ("box", "Diferenças em relação ao músculo esquelético",
               "O retículo sarcoplasmático cardíaco é <b>pouco desenvolvido</b>; os túbulos T são <b>5× mais largos (25× o volume)</b> e "
               "guardam Ca²⁺ em mucopolissacarídeos. Por isso a <b>força depende do Ca²⁺ extracelular</b>: sem Ca²⁺ no meio, o coração para."),
    ]),
    ("4. Ciclo cardíaco", [
        ("fig", None, "fig_livro/g9_08.png", "Eventos do ciclo cardíaco do lado esquerdo (diagrama de Wiggers).", 12.5),
        ("p", "O ciclo começa no <b>nó sinusal</b>. Há um <b>atraso &gt; 0,1 s</b> no nó AV, então o átrio contrai antes do ventrículo. "
              "Duração = 1/FC (72 bpm → 0,83 s). Quando a FC sobe, <b>a diástole encurta mais que a sístole</b> "
              "(sístole ≈ 40% do ciclo a 72 bpm e ≈ 65% com FC 3×), e o enchimento pode ficar incompleto."),
        ("table", [
            ["Fase", "Valvas", "Detalhe que cai"],
            ["Enchimento rápido", "AV abertas", "1º terço da diástole; o sangue acumulado no átrio entra de uma vez"],
            ["Diástase", "AV abertas", "Terço médio; pouco fluxo"],
            ["Sístole atrial", "AV abertas", "Último terço; <b>≈ 20% do enchimento</b> (80% é passivo)"],
            ["Contração isovolumétrica", "<b>todas fechadas</b>", "0,02 a 0,03 s; termina quando PVE &gt; ≈ 80 mmHg (PVD &gt; ≈ 8)"],
            ["Ejeção", "semilunares abertas", "≈ 70% do volume sai no 1º terço (ejeção rápida)"],
            ["Relaxamento isovolumétrico", "<b>todas fechadas</b>", "0,03 a 0,06 s; termina quando as AV abrem"],
        ], [4.2, 3.4, 9.8]),
        ("table", [
            ["Onda atrial", "Causa"],
            ["<b>a</b>", "Contração atrial (AD +4 a 6 mmHg; AE +7 a 8 mmHg)"],
            ["<b>c</b>", "Início da sístole ventricular: <b>abaulamento das valvas AV</b> para o átrio"],
            ["<b>v</b>", "Fim da sístole: átrio enchendo pelas veias com as AV fechadas"],
        ], [2.6, 14.8]),
        ("box", "Volumes normais (decorar)",
               "<b>VDF 110 a 120 mℓ</b> · <b>VS ≈ 70 mℓ</b> · <b>VSF 40 a 50 mℓ</b> · <b>FE = VS/VDF ≈ 60%</b>. "
               "ECG: P precede a contração atrial; QRS começa pouco antes da sístole; T ocorre pouco antes do fim da contração."),
    ]),
    ("5. Valvas e bulhas", [
        ("fig", None, "fig_livro/g9_09.png", "Valvas mitral e aórtica: cúspides, cordas tendíneas e músculos papilares.", 7),
        ("table", [
            ["", "AV (mitral, tricúspide)", "Semilunares (aórtica, pulmonar)"],
            ["Estrutura", "Finas, com <b>cordas tendíneas e papilares</b>", "Fibrosas e resistentes, <b>sem cordas</b>"],
            ["Fechamento", "Suave", "<b>Abrupto</b> (alta pressão arterial)"],
            ["Fluxo e desgaste", "Orifício grande, fluxo lento", "Orifício menor: <b>fluxo rápido e mais abrasão</b>"],
            ["Som", "<b>B1</b>: grave e mais longo", "<b>B2</b>: agudo e curto"],
        ], [3.2, 7.0, 7.2]),
        ("box", "Pegadinha clássica: músculos papilares",
               "As valvas abrem e fecham <b>passivamente</b> pelo gradiente de pressão. Os papilares <b>não fecham a valva</b>: puxam as "
               "cúspides para o ventrículo e <b>impedem o prolapso</b> para o átrio. Isquemia do papilar ou ruptura de corda no infarto → "
               "<b>insuficiência mitral aguda</b>."),
        ("fig", None, "fig_livro/g23_02.png", "Focos de ausculta. Pelo Porto: aórtico 2º EIC D; pulmonar 2º EIC E; "
                "aórtico acessório 3º-4º EIC E; tricúspide na base do apêndice xifoide; mitral no 5º EIC E na linha hemiclavicular (ictus).", 7),
        ("ul", [
            "<b>Curva aórtica</b>: sobe a ≈ 120 mmHg; a <b>incisura</b> marca o fechamento da aórtica (breve refluxo); cai lentamente até ≈ 80 mmHg. "
            "Pressões do lado direito ≈ 1/6 das esquerdas.",
            "<b>B3</b>: início do terço médio da diástole (enchimento rápido). Normal em crianças e jovens; em idosos sugere <b>IC sistólica</b>.",
            "<b>B4</b>: sístole atrial contra <b>ventrículo rígido</b> (HVE do idoso, hipertensão). <b>Some na fibrilação atrial</b>.",
            "Abertura das valvas normalmente não faz som.",
        ]),
    ]),
    ("6. Alça pressão-volume, pré e pós-carga", [
        ("fig", None, "fig_livro/g9_11.png", "Alça pressão-volume do VE. A área é o trabalho externo (TE).", 8.5),
        ("ul", [
            "<b>I</b> enchimento (50 → 120 mℓ) · <b>II</b> contração isovolumétrica (até ≈ 80 mmHg) · <b>III</b> ejeção (sai ≈ 70 mℓ) · "
            "<b>IV</b> relaxamento isovolumétrico.",
            "<b>Pré-carga</b> = <b>pressão diastólica final</b>. <b>Pós-carga</b> = <b>pressão na aorta</b> (artéria de saída).",
            "Trabalho: quase todo é pressão-volume; energia cinética é ≈ 1%, mas passa de <b>50% na estenose aórtica</b>.",
            "Energia: <b>70 a 90% de ácidos graxos</b>; eficiência de <b>20 a 25%</b> (na IC, até 5%).",
            "<b>Laplace: T = P × r</b>. Pressão alta crônica → <b>hipertrofia concêntrica</b> (reduz o raio e a tensão). "
            "Ventrículo dilatado gasta mais O₂ para a mesma pressão.",
        ]),
    ]),
    ("7. Regulação do bombeamento", [
        ("box", "Frank-Starling",
               "Quanto mais o músculo é distendido no enchimento, maior a força: <b>o coração bombeia todo o sangue que volta a ele</b>. "
               "Motivo: sobreposição actina-miosina mais próxima do ideal. O débito é determinado pelo <b>retorno venoso</b>."),
        ("ul", [
            "Estiramento do AD: FC ↑ 10 a 20% (direto no nó sinusal) + <b>reflexo de Bainbridge</b> (via vagal) FC ↑ 40 a 60%.",
            "<b>Simpático</b>: FC até 180 a 200 bpm, força até <b>dobra</b>, débito 2 a 3×. O tônus basal mantém o bombeamento 30% acima.",
            "<b>Vago</b>: age sobretudo nos <b>átrios</b> → reduz muito a FC (pode parar e depois \"escapar\" a 20 a 40 bpm) e pouco a força (20 a 30%).",
            "Débito de repouso 4 a 6 ℓ/min; no exercício, 4 a 7×. A pós-carga só reduz o débito com pressão média &gt; ≈ <b>160 mmHg</b>.",
        ]),
        ("table", [
            ["Situação", "Efeito no coração"],
            ["<b>K⁺ alto</b>", "Coração <b>dilatado e flácido</b>, FC ↓, <b>bloqueio AV</b>; 8 a 12 mEq/ℓ pode matar (despolariza o repouso → potencial menor)"],
            ["<b>Ca²⁺ alto / baixo</b>", "Alto: contração <b>espástica</b>. Baixo: fraqueza"],
            ["<b>Febre / hipotermia</b>", "Febre ↑ FC (até o dobro). Hipotermia ↓ muito a FC"],
        ], [3.6, 13.8]),
    ]),
]


G = "fig_livro/"
CARDS = [
    ("b", "No diagrama de Wiggers, onde caem B1 e B2?", "<b>B1</b>: início da sístole (fecham mitral e tricúspide). "
          "<b>B2</b>: início da diástole (fecham aórtica e pulmonar)."),
    ("c", "Pulso venoso: onda {{c1::a}} = contração atrial; onda {{c2::c}} = abaulamento da tricúspide; onda {{c3::v}} = enchimento atrial "
          "com a tricúspide fechada."),
    # ---------- lacunas (cloze)
    ("c", "O miocárdio funciona como {{c1::sincício}} porque os {{c2::discos intercalares}} têm {{c3::junções comunicantes (gap junctions)}}."),
    ("c", "Átrios e ventrículos são separados pelo {{c1::esqueleto fibroso}}; o impulso só passa pelo {{c2::feixe AV}}."),
    ("c", "Potencial ventricular: repouso ≈ {{c1::−85 mV}}, pico ≈ {{c2::+20 mV}}, platô de ≈ {{c3::0,2 s}}."),
    ("c", "Fase 0 = entrada de {{c1::Na⁺}} pelos canais {{c2::rápidos}}."),
    ("c", "O platô (fase 2) resulta da entrada de {{c1::Ca²⁺ por canais tipo L}} e da {{c2::queda (~5×) da permeabilidade ao K⁺}}.",
     ""),
    ("c", "Fase 3: canais de {{c1::Ca²⁺}} fecham e sai {{c2::K⁺}}."),
    ("c", "Período refratário absoluto ventricular: {{c1::0,25 a 0,30 s}}; relativo: {{c2::0,05 s}}; atrial: {{c3::0,15 s}}."),
    ("c", "Como o refratário cobre a contração, o coração {{c1::não entra em tetania}}."),
    ("c", "Velocidade de condução: músculo {{c1::0,3 a 0,5 m/s}}; Purkinje {{c2::até 4 m/s}}."),
    ("c", "O Ca²⁺ que entra pelo túbulo T ativa os {{c1::receptores de rianodina (RyR2)}}: é a {{c2::liberação de Ca²⁺ induzida por Ca²⁺}}.",
     "", G + "g9_07.png"),
    ("c", "No relaxamento, o Ca²⁺ volta ao retículo pela {{c1::SERCA2}} e sai da célula pelo {{c2::trocador Na⁺/Ca²⁺}}."),
    ("c", "Túbulos T cardíacos: diâmetro {{c1::5×}} e volume {{c2::25×}} maiores que os do esquelético."),
    ("c", "Atraso AV: {{c1::&gt; 0,1 s}}, para que os átrios contraiam antes dos ventrículos."),
    ("c", "Com FC alta, encurta mais a {{c1::diástole}}; a sístole passa de ≈ 40% para ≈ {{c2::65%}} do ciclo (FC 3×)."),
    ("c", "A contração atrial contribui com ≈ {{c1::20%}} do enchimento ventricular."),
    ("c", "Onda {{c1::a}} = contração atrial; onda {{c2::c}} = abaulamento das AV; onda {{c3::v}} = enchimento atrial com AV fechadas."),
    ("c", "Diástole: 1º terço {{c1::enchimento rápido}}; terço médio {{c2::diástase}}; último terço {{c3::sístole atrial}}."),
    ("c", "Contração isovolumétrica dura {{c1::0,02 a 0,03 s}}; a aórtica abre com PVE &gt; {{c2::80 mmHg}} e a pulmonar com PVD &gt; {{c3::8 mmHg}}."),
    ("c", "Na ejeção rápida (1º terço) sai ≈ {{c1::70%}} do volume sistólico."),
    ("c", "VDF {{c1::110 a 120 mℓ}}, VS {{c2::70 mℓ}}, VSF {{c3::40 a 50 mℓ}}, FE {{c4::≈ 60%}}."),
    ("c", "Fração de ejeção = {{c1::VS / VDF}}."),
    ("c", "Os músculos papilares {{c1::não fecham}} as valvas; eles {{c2::impedem o prolapso das cúspides para o átrio}}.",
     "", G + "g9_09.png"),
    ("c", "Ruptura de corda tendínea ou isquemia do papilar causa {{c1::insuficiência mitral aguda}}."),
    ("c", "A {{c1::incisura}} da curva aórtica marca o {{c2::fechamento da valva aórtica}}."),
    ("c", "Pressão aórtica ≈ {{c1::120/80 mmHg}}; lado direito ≈ {{c2::1/6}} disso."),
    ("c", "B1 = fechamento das {{c1::valvas AV}}; B2 = fechamento das {{c2::semilunares}}."),
    ("c", "B3 ocorre no {{c1::início do terço médio da diástole}}; em idosos indica {{c2::insuficiência cardíaca sistólica}}."),
    ("c", "B4 ocorre na {{c1::sístole atrial}} contra ventrículo {{c2::pouco complacente}} e {{c3::some na fibrilação atrial}}."),
    ("c", "Pré-carga = {{c1::pressão diastólica final}}; pós-carga = {{c2::pressão na aorta}}."),
    ("c", "Energia cinética é ≈ {{c1::1%}} do trabalho do VE, mas pode passar de {{c2::50%}} na {{c3::estenose aórtica}}."),
    ("c", "O miocárdio usa {{c1::ácidos graxos}} (70 a 90%) e tem eficiência de {{c2::20 a 25%}}."),
    ("c", "Lei de Laplace: {{c1::T = P × r}}. Pressão alta crônica → hipertrofia {{c2::concêntrica}}."),
    ("c", "Frank-Starling: quanto maior o {{c1::estiramento no enchimento}}, maior a {{c2::força de contração}}."),
    ("c", "Reflexo de {{c1::Bainbridge}}: estiramento atrial → FC ↑ {{c2::40 a 60%}}."),
    ("c", "Simpático: FC até {{c1::180 a 200 bpm}} e força até {{c2::o dobro}}."),
    ("c", "O vago inerva sobretudo os {{c1::átrios}}, por isso reduz mais a {{c2::FC}} que a força."),
    ("c", "Hiperpotassemia deixa o coração {{c1::dilatado e flácido}}, com {{c2::bradicardia e bloqueio AV}}."),
    ("c", "O excesso de Ca²⁺ leva à contração {{c1::espástica}}."),
    ("c", "A pós-carga só reduz o débito cardíaco com pressão média acima de ≈ {{c1::160 mmHg}}."),
    ("c", "Foco mitral: {{c1::5º EIC esquerdo na linha hemiclavicular}} (ictus cordis)."),
    ("c", "Foco tricúspide: {{c1::base do apêndice xifoide, ligeiramente à esquerda}}."),
    # ---------- pergunta e resposta
    ("b", "Por que o potencial de ação cardíaco é longo? (2 motivos)",
     "1) <b>Canais lentos de Ca²⁺ tipo L</b> abertos por décimos de segundo; 2) <b>queda da permeabilidade ao K⁺</b>."),
    ("b", "Por que a força do coração depende do Ca²⁺ extracelular, e a do esquelético não?",
     "Retículo sarcoplasmático cardíaco <b>pouco desenvolvido</b>; o Ca²⁺ dos <b>túbulos T</b> (vem do meio extracelular) dispara e complementa a contração."),
    ("b", "O que acontece com um coração em solução sem Ca²⁺?", "<b>Para de bater</b> rapidamente."),
    ("b", "Quais valvas estão abertas na contração isovolumétrica?", "<b>Nenhuma</b>: todas fechadas."),
    ("b", "Por que a perda da contração atrial (FA) costuma dar sintomas só no esforço?",
     "Ela contribui só com ≈ 20% do enchimento e o coração tem reserva de 300 a 400%. Ventrículos rígidos dependem mais dela."),
    ("b", "Diferenças das semilunares em relação às AV (4)",
     "Fechamento <b>abrupto</b>; fluxo mais <b>rápido</b>; mais <b>abrasão</b>; <b>sem cordas tendíneas</b>."),
    ("b", "Qual a valvopatia mais comum hoje e sua tríade clínica?",
     "<b>Estenose aórtica calcificada senil</b>: angina, síncope e dispneia aos esforços."),
    ("b", "Valvas mais lesadas na febre reumática", "<b>Mitral</b>, depois <b>aórtica</b> (alta pressão)."),
    ("b", "O que representa a área da alça pressão-volume?", "O <b>trabalho sistólico externo</b>.", G + "g9_11.png"),
    ("b", "Ventrículo dilatado × hipertrofia concêntrica: qual gasta mais O₂ para a mesma pressão?",
     "O <b>dilatado</b> (raio maior → mais tensão pela lei de Laplace)."),
    ("b", "Efeito do vago muito forte no coração", "Para por segundos e <b>escapa</b> a 20 a 40 bpm; força cai 20 a 30%."),
    ("b", "Por que a hiperpotassemia enfraquece o coração?",
     "Despolariza parcialmente o repouso → <b>potencial de ação menor</b> → contração fraca; também bloqueia a condução AV."),
    ("b", "Quem determina o débito cardíaco em condições normais?", "O <b>retorno venoso</b> (soma dos fluxos locais dos tecidos)."),
    ("b", "Onde auscultar cada foco (Porto)?",
     "Aórtico 2º EIC D · Pulmonar 2º EIC E · Aórtico acessório 3º-4º EIC E · Tricúspide base do xifoide · Mitral 5º EIC E LHC.",
     G + "g23_02.png"),
    ("b", "Fonocardiograma: qual sopro é sistólico em diamante no foco aórtico?", "<b>Estenose aórtica</b>.", G + "g23_03.png"),
]

OCC_IMG = [
    (G + "g9_08.png", 'Contração isovolumétrica', 'Qual fase do ciclo?', '<b>Contração isovolumétrica</b>: todas as valvas fechadas.'),
    (G + "g9_08.png", 'Ejeção', 'Qual fase do ciclo?', '<b>Ejeção</b>: valva aórtica aberta.'),
    (G + "g9_08.png", 'Relaxamento isovolumétrico', 'Qual fase do ciclo?', '<b>Relaxamento isovolumétrico</b>.'),
    (G + "g9_08.png", 'Enchimento rápido', 'Qual fase do ciclo?', '<b>Enchimento rápido</b> (≈ 1/3 inicial da diástole).'),
    (G + "g9_08.png", 'Diástase', 'Qual fase do ciclo?', '<b>Diástase</b>: enchimento lento, terço médio da diástole.'),
    (G + "g9_08.png", 'Sístole atrial', 'Qual fase do ciclo?', '<b>Sístole atrial</b>: completa ≈ 20% do enchimento.'),
    (G + "g9_08.png", 'Pressão aórtica', 'Qual curva?', '<b>Pressão aórtica</b> (120/80, incisura no fechamento da valva).'),
    (G + "g9_08.png", 'Volume ventricular', 'Qual curva?', '<b>Volume ventricular</b> (VDF ≈ 110–120; VSF ≈ 40–50 mℓ).'),
    (G + "g9_09.png", 'Cordas tendíneas', 'Qual estrutura?', '<b>Cordas tendíneas</b>.'),
    (G + "g9_09.png", 'Músculos papilares', 'Qual estrutura?', '<b>Músculos papilares</b>: contraem na sístole e evitam o abaulamento das cúspides.'),
    (G + "g9_11.png", 'Período de ejeção', 'Qual fase da alça?', '<b>Período de ejeção</b> (fase III).'),
    (G + "g9_11.png", 'Contração isovolumétrica', 'Qual fase da alça?', '<b>Contração isovolumétrica</b> (fase II).'),
    (G + "g9_11.png", 'Relaxamento isovolumétrico', 'Qual fase da alça?', '<b>Relaxamento isovolumétrico</b> (fase IV).'),
    (G + "g9_11.png", 'Período de enchimento', 'Qual fase da alça?', '<b>Período de enchimento</b> (fase I).'),
    (G + "g9_11.png", 'Volume sistólico', 'O que é a largura da alça?', '<b>Volume sistólico</b> (≈ 70 mℓ).'),
    (G + "g23_02.png", 'Area pulmonar', 'Qual área de ausculta?', '<b>Área pulmonar</b>: 2º espaço intercostal esquerdo.'),
    (G + "g23_02.png", 'Área tricúspide', 'Qual área de ausculta?', '<b>Área tricúspide</b>: borda esternal esquerda baixa.'),
    (G + "g23_02.png", 'Area mitral', 'Qual área de ausculta?', '<b>Área mitral</b>: ápice (5º EIC E, linha hemiclavicular).'),
]

TOPIC = dict(
    code="a", slug="a-musculo-cardiaco-e-valvas", title="Músculo cardíaco e valvas cardíacas",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 9 (bulhas: cap. 23; focos: Porto)",
    sections=SECTIONS, cards=CARDS, occ_img=OCC_IMG, 
)
