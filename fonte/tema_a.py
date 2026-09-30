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
        ("fig", "fig_web/a/a5_discos_intercalares.jpg", "fig_livro/g9_02.png", "Discos intercalares e o sincício do músculo cardíaco.", 9),
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
        ("fig", "fig/a_potencial_acao.png", "fig_livro/g9_05.png", "Fases do potencial de ação da fibra ventricular e correntes iônicas.", 14.5),
        ("box", "O que a prova cobra", [
            "Platô = <b>Ca²⁺ entrando + K⁺ \"preso\"</b>. Por causa dele a contração dura até 15× a do músculo esquelético.",
            "<b>Período refratário absoluto do ventrículo: 0,25 a 0,30 s</b> (quase toda a contração) + relativo de 0,05 s. "
            "Resultado: <b>o coração não tetaniza</b> e as extrassístoles não somam força.",
            "Átrio tem refratário mais curto (≈ 0,15 s), por isso aguenta frequências muito altas (flutter, fibrilação).",
            "Condução: músculo <b>0,3 a 0,5 m/s</b>; Purkinje <b>até 4 m/s</b>.",
        ]),
    ]),
    ("3. Acoplamento excitação-contração", [
        ("fig", "fig/a_acoplamento.png", "fig_livro/g9_07.png", "Entrada de Ca²⁺ pelo túbulo T, liberação pelo RyR e recaptação pela SERCA2.", 15.5),
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
        ("fig", "fig/a_wiggers.png", "fig_livro/g9_08.png", "Eventos do ciclo cardíaco do lado esquerdo (diagrama de Wiggers).", 16.5),
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
        ("web", "fig_web/a/a2_wiggers_pulso_venoso.png", 7.5,
         "Pulso venoso (embaixo): onda a (contração atrial), c (abaulamento da tricúspide) e v (enchimento atrial com a tricúspide fechada)."),
        ("box", "Volumes normais (decorar)",
               "<b>VDF 110 a 120 mℓ</b> · <b>VS ≈ 70 mℓ</b> · <b>VSF 40 a 50 mℓ</b> · <b>FE = VS/VDF ≈ 60%</b>. "
               "ECG: P precede a contração atrial; QRS começa pouco antes da sístole; T ocorre pouco antes do fim da contração."),
    ]),
    ("5. Valvas e bulhas", [
        ("fig", None, "fig_livro/g9_09.png", "Valvas mitral e aórtica: cúspides, cordas tendíneas e músculos papilares.", 8),
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
        ("fig", "fig/a_focos.png", "fig_livro/g23_02.png", "Focos de ausculta. Pelo Porto: aórtico 2º EIC D; pulmonar 2º EIC E; "
                "aórtico acessório 3º-4º EIC E; tricúspide na base do apêndice xifoide; mitral no 5º EIC E na linha hemiclavicular (ictus).", 9),
        ("ul", [
            "<b>Curva aórtica</b>: sobe a ≈ 120 mmHg; a <b>incisura</b> marca o fechamento da aórtica (breve refluxo); cai lentamente até ≈ 80 mmHg. "
            "Pressões do lado direito ≈ 1/6 das esquerdas.",
            "<b>B3</b>: início do terço médio da diástole (enchimento rápido). Normal em crianças e jovens; em idosos sugere <b>IC sistólica</b>.",
            "<b>B4</b>: sístole atrial contra <b>ventrículo rígido</b> (HVE do idoso, hipertensão). <b>Some na fibrilação atrial</b>.",
            "Abertura das valvas normalmente não faz som.",
        ]),
    ]),
    ("6. Alça pressão-volume, pré e pós-carga", [
        ("fig", "fig/a_alca_pv.png", "fig_livro/g9_11.png", "Alça pressão-volume do VE. A área é o trabalho externo (TE).", 14),
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

MCQ = [
    dict(q="O potencial de ação da fibra muscular ventricular apresenta um platô prolongado. Esse platô se deve principalmente a:",
         opts=["Abertura prolongada dos canais rápidos de Na⁺ dependentes de voltagem",
               "Entrada de Ca²⁺ por canais tipo L associada à redução da permeabilidade ao K⁺",
               "Ativação da Na⁺/K⁺-ATPase, que gera corrente despolarizante",
               "Liberação de Ca²⁺ do retículo sarcoplasmático para o líquido extracelular",
               "Aumento da permeabilidade ao Cl⁻ durante a fase 2"],
         a=1, c="O platô (fase 2) resulta de duas diferenças em relação ao músculo esquelético: canais lentos de Ca²⁺ tipo L que "
                "ficam abertos por décimos de segundo e queda de cerca de 5 vezes da permeabilidade ao K⁺. Os canais rápidos de Na⁺ "
                "ficam abertos só por milésimos de segundo, por isso não sustentam o platô."),
    dict(q="Qual é a principal consequência funcional do longo período refratário do músculo ventricular?",
         opts=["Permitir a somação de ondas para aumentar a força",
               "Aumentar a velocidade de condução nas fibras de Purkinje",
               "Impedir a tetania, garantindo o relaxamento e o enchimento entre os batimentos",
               "Tornar o ventrículo capaz de responder a frequências maiores que o átrio",
               "Eliminar o período refratário relativo"],
         a=2, c="O período refratário absoluto ventricular (0,25 a 0,30 s) dura quase toda a contração. Por isso não há somação nem "
                "tetania, e o ventrículo relaxa e enche a cada ciclo. O átrio tem refratário mais curto (≈ 0,15 s) e aceita "
                "frequências mais altas, e não o ventrículo."),
    dict(q="Sobre o acoplamento excitação-contração no músculo cardíaco, assinale a alternativa correta:",
         opts=["O Ca²⁺ que inicia a contração vem exclusivamente do retículo sarcoplasmático, como no músculo esquelético",
               "Os túbulos T cardíacos têm diâmetro menor que os do músculo esquelético",
               "O Ca²⁺ que entra pelos canais tipo L do túbulo T ativa os receptores de rianodina, liberando Ca²⁺ do retículo sarcoplasmático",
               "A força de contração cardíaca é pouco afetada pela concentração extracelular de Ca²⁺",
               "O relaxamento depende exclusivamente da Na⁺/K⁺-ATPase"],
         a=2, c="É a liberação de Ca²⁺ induzida por Ca²⁺: o Ca²⁺ extracelular entra pelos canais L do túbulo T e abre os RyR2. "
                "Os túbulos T cardíacos são 5× mais largos, a força depende muito do Ca²⁺ extracelular e o relaxamento envolve "
                "SERCA2 e o trocador Na⁺/Ca²⁺ (com a Na⁺/K⁺-ATPase removendo o Na⁺)."),
    dict(q="Um coração isolado perfundido com solução sem cálcio para de bater rapidamente. A melhor explicação é:",
         opts=["O retículo sarcoplasmático cardíaco é pouco desenvolvido e a contração depende do Ca²⁺ que chega pelos túbulos T do meio extracelular",
               "Sem Ca²⁺ extracelular, os canais rápidos de Na⁺ não abrem",
               "O Ca²⁺ é necessário para abrir as junções comunicantes dos discos intercalares",
               "A falta de Ca²⁺ causa hiperpolarização e parada em sístole",
               "O Ca²⁺ extracelular é o principal determinante do potencial de repouso"],
         a=0, c="O retículo sarcoplasmático cardíaco não armazena Ca²⁺ suficiente para a contração completa. Os túbulos T, abertos ao "
                "interstício e ricos em mucopolissacarídeos que ligam Ca²⁺, fornecem o cálcio extracelular que dispara e complementa a contração."),
    dict(q="Os discos intercalares do miocárdio são importantes porque:",
         opts=["Isolam eletricamente cada cardiomiócito, impedindo arritmias",
               "Contêm junções comunicantes de baixa resistência que fazem o miocárdio funcionar como sincício",
               "São o local de armazenamento de Ca²⁺ para a contração",
               "Conduzem o impulso dos átrios para os ventrículos através do esqueleto fibroso",
               "Geram o potencial de ação espontâneo"],
         a=1, c="Nos discos intercalares as membranas se fundem em gap junctions, que permitem a difusão rápida de íons entre as "
                "células. Assim o potencial de ação passa de célula a célula (sincício funcional). A passagem átrio → ventrículo "
                "acontece apenas pelo feixe AV, e não pelo esqueleto fibroso."),
    dict(q="Por que átrios e ventrículos constituem dois sincícios funcionais separados?",
         opts=["Porque os átrios não têm discos intercalares",
               "Porque o nó sinusal fica no ventrículo",
               "Porque o potencial de ação atrial não tem fase 0",
               "Porque o tecido fibroso dos anéis AV isola os dois, e o impulso só atravessa pelo feixe AV",
               "Porque o miocárdio ventricular não tem junções comunicantes"],
         a=3, c="O esqueleto fibroso ao redor das valvas AV não conduz o impulso. A condução só ocorre pelo sistema especializado "
                "(feixe AV), o que permite que os átrios contraiam um pouco antes dos ventrículos."),
    dict(q="Qual evento do ciclo cardíaco corresponde ao período em que TODAS as valvas cardíacas estão fechadas e a pressão ventricular esquerda sobe de ≈ 8 para ≈ 80 mmHg?",
         opts=["Ejeção rápida", "Enchimento rápido", "Diástase", "Relaxamento isovolumétrico", "Contração isovolumétrica"],
         a=4, c="Na contração isovolumétrica (0,02 a 0,03 s), a mitral já fechou e a aórtica ainda não abriu. A tensão sobe sem "
                "mudança de volume até a pressão do VE superar a aórtica (≈ 80 mmHg)."),
    dict(q="Com relação às ondas de pressão atrial, a onda c é causada principalmente por:",
         opts=["Contração atrial",
               "Enchimento atrial pelas veias com as valvas AV fechadas",
               "Abaulamento das valvas AV em direção aos átrios no início da contração ventricular",
               "Abertura das valvas AV no início da diástole",
               "Fechamento das valvas semilunares"],
         a=2, c="A onda a é a contração atrial; a onda c ocorre no início da sístole ventricular, principalmente pelo abaulamento das "
                "valvas AV para os átrios (e leve refluxo); a onda v resulta do enchimento atrial com as AV fechadas, no fim da sístole."),
    dict(q="Em um adulto saudável em repouso, qual é a contribuição aproximada da contração atrial para o enchimento ventricular?",
         opts=["5%", "20%", "50%", "80%", "100%"], keep=True,
         a=1, c="Cerca de 80% do sangue passa passivamente dos átrios aos ventrículos; a contração atrial acrescenta ≈ 20%. Por isso "
                "a perda da contração atrial costuma dar sintomas só no esforço (reserva de 300 a 400%)."),
    dict(q="Um homem saudável tem volume diastólico final de 120 mℓ e volume sistólico final de 50 mℓ. Sua fração de ejeção e seu volume sistólico são, respectivamente:",
         opts=["42% e 50 mℓ", "58% e 70 mℓ", "70% e 120 mℓ", "60% e 50 mℓ", "41% e 70 mℓ"],
         a=1, c="VS = VDF − VSF = 120 − 50 = 70 mℓ. FE = VS/VDF = 70/120 ≈ 0,58 (≈ 60%, valor normal citado no Guyton)."),
    dict(q="Durante o período de ejeção ventricular:",
         opts=["O volume ejetado distribui-se igualmente ao longo de toda a ejeção",
               "Cerca de 70% do volume sistólico sai no primeiro terço do período de ejeção",
               "A valva mitral está aberta",
               "O ventrículo ejeta cerca de 100% do volume diastólico final",
               "A pressão ventricular é sempre menor que a aórtica"],
         a=1, c="O primeiro terço é a ejeção rápida (≈ 70% do volume ejetado); os dois terços finais, a ejeção lenta (≈ 30%). "
                "Normalmente sai ≈ 60% do VDF."),
    dict(q="Um estudante afirma que os músculos papilares se contraem para fechar as valvas mitral e tricúspide. Sobre essa afirmação:",
         opts=["Está correta, pois sem eles as valvas AV ficariam abertas na sístole",
               "Está incorreta: os músculos papilares puxam as cúspides para o ventrículo, evitando o abaulamento excessivo para os átrios",
               "Está correta apenas para a valva tricúspide",
               "Está incorreta, pois os músculos papilares só se contraem na diástole",
               "Está incorreta, pois os músculos papilares estão ligados às valvas semilunares"],
         a=1, c="As valvas fecham passivamente pelo gradiente de pressão. Os músculos papilares contraem junto com a parede e, pelas "
                "cordas tendíneas, impedem que as cúspides prolapsem para os átrios. Sua disfunção (infarto) causa insuficiência mitral."),
    dict(q="Qual característica é das valvas semilunares, e não das valvas AV?",
         opts=["São sustentadas por cordas tendíneas",
               "Fecham-se de forma suave, quase sem refluxo",
               "Por elas o sangue passa com menor velocidade",
               "Fecham-se abruptamente e sofrem maior abrasão mecânica",
               "Seu fechamento gera a primeira bulha"],
         a=3, c="As semilunares fecham abruptamente pela alta pressão arterial no fim da sístole, têm orifício menor (maior velocidade) "
                "e sofrem mais abrasão. Não têm cordas tendíneas. B1 vem do fechamento das AV."),
    dict(q="A incisura (nó dicrótico) da curva de pressão aórtica corresponde a:",
         opts=["Abertura da valva aórtica",
               "Contração atrial",
               "Breve refluxo de sangue seguido da interrupção súbita quando a valva aórtica se fecha",
               "Pico da ejeção rápida",
               "Abertura da valva mitral"],
         a=2, c="Logo antes do fechamento da valva aórtica ocorre um pequeno refluxo, interrompido bruscamente pelo fechamento; isso "
                "produz a incisura, que coincide com B2."),
    dict(q="A primeira bulha cardíaca (B1):",
         opts=["É causada pela abertura das valvas semilunares",
               "É mais aguda e mais curta que B2",
               "Ocorre no fim da diástole por contração atrial",
               "É causada pelo fechamento das valvas AV e é grave e relativamente longa",
               "É normalmente inaudível ao estetoscópio"],
         a=3, c="B1 = fechamento das AV no início da sístole: grave e com ≈ 0,14 s. B2 (semilunares) é mais aguda e curta (≈ 0,11 s). "
                "A abertura das valvas não produz som."),
    dict(q="Em um idoso com hipertrofia ventricular esquerda por hipertensão, ausculta-se um som de baixa frequência imediatamente antes de B1. Esse som:",
         opts=["É B3 e indica sobrecarga de volume",
               "É B4, gerado pela contração atrial contra um ventrículo pouco complacente",
               "É um estalido de abertura mitral",
               "É B2 desdobrado",
               "Estaria presente mesmo em fibrilação atrial"],
         a=1, c="B4 ocorre na sístole atrial (fim da diástole, logo antes de B1) quando o ventrículo tem complacência reduzida, como na "
                "HVE do idoso. Como depende da contração atrial, desaparece na fibrilação atrial."),
    dict(q="Qual afirmação sobre a terceira bulha (B3) está correta segundo o Guyton?",
         opts=["Ocorre no início do terço médio da diástole e pode ser normal em crianças e adultos jovens",
               "Resulta do fechamento das valvas semilunares",
               "Ocorre durante a contração isovolumétrica",
               "É sempre patológica",
               "É causada pela contração atrial"],
         a=0, c="B3 ocorre no início do terço médio da diástole, pela oscilação do sangue que entra no ventrículo. É normal em jovens; "
                "em idosos geralmente indica insuficiência cardíaca sistólica."),
    dict(q="Quando a frequência cardíaca aumenta muito (por exemplo, triplica), o que acontece com o ciclo cardíaco?",
         opts=["Sístole e diástole encurtam na mesma proporção",
               "Só a sístole encurta",
               "A diástole encurta proporcionalmente mais, e a sístole passa a ocupar ≈ 65% do ciclo",
               "A duração do potencial de ação aumenta",
               "O enchimento ventricular melhora"],
         a=2, c="A sístole ocupa ≈ 40% do ciclo a 72 bpm e ≈ 65% com FC três vezes maior. A diástole encurta mais, e o enchimento pode "
                "ficar incompleto em taquicardias muito altas."),
    dict(q="Na alça pressão-volume do ventrículo esquerdo, a área interna da alça representa:",
         opts=["A fração de ejeção",
               "O trabalho sistólico externo do ventrículo",
               "O consumo total de O₂ do miocárdio",
               "A complacência ventricular",
               "A energia potencial"],
         a=1, c="A área da alça (TE) é o trabalho externo líquido por batimento. O consumo de O₂ é proporcional a TE + EP (energia potencial)."),
    dict(q="Em qual situação a energia cinética do fluxo sanguíneo pode representar mais de 50% do trabalho do ventrículo esquerdo?",
         opts=["Exercício físico moderado", "Insuficiência mitral", "Estenose aórtica", "Bradicardia sinusal", "Hipovolemia"],
         a=2, c="Normalmente a energia cinética é ≈ 1% do trabalho do VE. Na estenose aórtica o sangue atravessa o orifício estreito com "
                "velocidade muito alta, e como a energia cinética é proporcional a massa × velocidade², ela pode passar de 50%."),
    dict(q="Segundo o Guyton, a pré-carga e a pós-carga ventriculares são, respectivamente:",
         opts=["Pressão aórtica e pressão diastólica final",
               "Volume sistólico e resistência periférica",
               "Pressão diastólica final e pressão na artéria de saída do ventrículo",
               "Frequência cardíaca e contratilidade",
               "Pressão atrial média e pressão venosa central"],
         a=2, c="Pré-carga = tensão ao iniciar a contração, representada pela pressão diastólica final. Pós-carga = carga contra a qual o "
                "ventrículo contrai, a pressão na aorta (ou artéria pulmonar)."),
    dict(q="De acordo com a lei de Laplace aplicada ao ventrículo, qual situação aumenta mais o consumo de O₂ para gerar a mesma pressão sistólica?",
         opts=["Ventrículo com hipertrofia concêntrica",
               "Ventrículo dilatado (raio aumentado)",
               "Redução do volume diastólico final",
               "Bradicardia",
               "Redução da pressão arterial"],
         a=1, c="T = P × r. Com o raio maior (ventrículo dilatado), a tensão da parede e o gasto de energia sobem para a mesma pressão. "
                "A hipertrofia concêntrica, ao contrário, reduz o raio e alivia a tensão."),
    dict(q="O principal substrato energético do miocárdio em repouso e a eficiência máxima do coração normal são:",
         opts=["Glicose; 50%", "Ácidos graxos; 20 a 25%", "Lactato; 5%", "Corpos cetônicos; 40%", "Aminoácidos; 20 a 25%"],
         a=1, c="70 a 90% da energia vem da oxidação de ácidos graxos. A eficiência (trabalho/energia química) é de 20 a 25%; na "
                "insuficiência cardíaca pode cair a 5%."),
    dict(q="O mecanismo de Frank-Starling é explicado principalmente por:",
         opts=["Aumento da frequência cardíaca pelo estiramento atrial",
               "Liberação de noradrenalina pelo estiramento ventricular",
               "Aproximação da sobreposição de actina e miosina ao grau ideal quando a fibra é distendida",
               "Aumento da condução no feixe AV",
               "Redução da pós-carga com o aumento do volume"],
         a=2, c="Mais enchimento distende as fibras e leva a sobreposição actina-miosina a um ponto mais próximo do ótimo, aumentando a "
                "força. O aumento da FC pelo estiramento atrial (10 a 20%) e o reflexo de Bainbridge são efeitos adicionais e menores."),
    dict(q="Sobre o controle autonômico do coração, assinale a correta:",
         opts=["A estimulação vagal reduz principalmente a força de contração ventricular, pois o vago inerva sobretudo os ventrículos",
               "A estimulação simpática pode dobrar a força de contração e elevar a FC para 180 a 200 bpm",
               "Sem tônus simpático basal, o bombeamento aumenta 30%",
               "A estimulação vagal intensa mantida causa parada cardíaca definitiva",
               "O simpático não altera a curva de função cardíaca"],
         a=1, c="O simpático pode dobrar a força e levar a FC a 180 a 200 bpm, aumentando o débito 2 a 3 vezes. O vago inerva sobretudo "
                "os átrios (efeito principal na FC). Após parada vagal, o coração \"escapa\" a 20 a 40 bpm. O tônus simpático basal "
                "mantém o bombeamento ≈ 30% acima do que seria sem ele."),
    dict(q="O reflexo de Bainbridge:",
         opts=["Reduz a FC quando a pressão arterial aumenta",
               "Aumenta a FC em resposta ao estiramento atrial, por via vagal aferente",
               "Aumenta a contratilidade pelo estiramento ventricular",
               "É mediado por quimiorreceptores carotídeos",
               "Diminui o retorno venoso"],
         a=1, c="O estiramento atrial ativa receptores que, por via do vago, aumentam a FC em 40 a 60%, ajudando o coração a bombear o "
                "volume extra que chega. Quem reduz a FC com PA alta é o barorreflexo, não o Bainbridge."),
    dict(q="Paciente com insuficiência renal apresenta K⁺ sérico de 9 mEq/ℓ. O efeito esperado sobre o coração é:",
         opts=["Contração espástica e taquicardia",
               "Coração dilatado e flácido, bradicardia e possível bloqueio AV",
               "Aumento da amplitude do potencial de ação",
               "Hiperpolarização do potencial de repouso",
               "Nenhum efeito relevante"],
         a=1, c="O K⁺ extracelular alto despolariza parcialmente o repouso, diminui a amplitude do potencial de ação e enfraquece a "
                "contração. O coração fica dilatado e flácido, a FC cai e pode haver bloqueio AV. Com 8 a 12 mEq/ℓ pode haver morte."),
    dict(q="O excesso de Ca²⁺ no líquido extracelular tende a causar:",
         opts=["Contração espástica", "Coração flácido", "Aumento do período refratário atrial", "Bloqueio AV total", "Redução da FC por febre"],
         a=0, c="O Ca²⁺ em excesso tem efeito quase oposto ao do K⁺ alto, levando o coração à contração espástica. A hipocalcemia causa fraqueza."),
    dict(q="Um paciente tem febre de 39,5 °C. Espera-se:",
         opts=["Bradicardia pela redução da permeabilidade iônica",
               "Aumento da FC, pois o calor aumenta a permeabilidade da membrana e acelera a autoexcitação",
               "Nenhuma alteração da FC",
               "Redução imediata e permanente da força de contração",
               "Bloqueio AV por hiperpotassemia"],
         a=1, c="A febre aumenta muito a FC (às vezes até o dobro). Elevação moderada aumenta temporariamente a força; elevação "
                "prolongada esgota o metabolismo e enfraquece o coração."),
    dict(q="Segundo o Guyton, o aumento da pressão arterial (pós-carga) passa a reduzir significativamente o débito cardíaco de um coração normal quando a pressão arterial média ultrapassa cerca de:",
         opts=["80 mmHg", "100 mmHg", "120 mmHg", "140 mmHg", "160 mmHg"], keep=True,
         a=4, c="O débito cardíaco se mantém até a pressão média ≈ 160 mmHg. Na faixa normal, quem determina o débito é o retorno venoso "
                "(fluxo pelos tecidos), não a pós-carga."),
    dict(q="Qual das afirmações sobre a torção do ventrículo esquerdo é correta?",
         opts=["As fibras subepicárdicas e subendocárdicas têm a mesma orientação",
               "Na sístole, o ápice gira em sentido anti-horário e a base em sentido horário",
               "A destorção na diástole funciona como mola e favorece a entrada rápida de sangue",
               "A torção dificulta a ejeção",
               "A torção ocorre apenas no ventrículo direito"],
         a=2, c="Subepicárdicas em hélice à esquerda e subendocárdicas à direita. Na sístole o ápice gira no sentido horário e a base no "
                "anti-horário, puxando a base ao ápice. Na diástole o VE \"destorce\" como uma mola comprimida, ajudando o enchimento rápido."),
    dict(q="Na curva de pressão diastólica do VE (relação volume-pressão passiva), a pressão sobe acentuadamente quando o volume ultrapassa ≈ 150 mℓ. Isso ocorre porque:",
         opts=["As valvas AV se fecham",
               "O tecido fibroso cardíaco não se estica mais e o pericárdio chega perto do seu limite",
               "A actina e a miosina se sobrepõem demais",
               "Aumenta a atividade simpática",
               "A valva aórtica se abre"],
         a=1, c="Até ≈ 150 mℓ o ventrículo enche com pouca variação de pressão. Acima disso, o tecido fibroso e o pericárdio limitam a "
                "distensão, e a pressão diastólica sobe rapidamente."),
    dict(q="O atraso de mais de 0,1 s na passagem do impulso dos átrios para os ventrículos tem como função:",
         opts=["Permitir que o nó sinusal repolarize",
               "Permitir que os átrios contraiam e completem o enchimento ventricular antes da sístole ventricular",
               "Gerar a onda T",
               "Reduzir a velocidade das fibras de Purkinje",
               "Evitar a abertura das valvas semilunares"],
         a=1, c="O atraso AV faz os átrios funcionarem como bombas de escorva, contraindo antes dos ventrículos e acrescentando ≈ 20% ao enchimento."),
    dict(q="Qual afirmação sobre as pressões do lado direito do coração está correta?",
         opts=["A valva pulmonar abre quando a pressão do VD ultrapassa ≈ 80 mmHg",
               "As pressões do VD e da artéria pulmonar são ≈ 1/6 das pressões do lado esquerdo",
               "O trabalho externo do VD é igual ao do VE",
               "A pressão sistólica máxima do VD normal é de 250 a 300 mmHg",
               "A onda a do átrio direito é maior que a do esquerdo"],
         a=1, c="A pulmonar abre com PVD acima de ≈ 8 mmHg. As pressões direitas são ≈ 1/6 das esquerdas, e o trabalho externo do VD "
                "também. O pico isovolumétrico do VD é 60 a 80 mmHg. A onda a é de 4 a 6 mmHg no AD e 7 a 8 mmHg no AE."),
    dict(q="Sobre a relação entre ECG e ciclo mecânico, é correto afirmar que:",
         opts=["O QRS ocorre depois do início da ejeção",
               "A onda T coincide com a abertura da valva aórtica",
               "O QRS começa um pouco antes da sístole ventricular, e a onda T ocorre um pouco antes do fim da contração ventricular",
               "A onda P é seguida da contração ventricular",
               "O intervalo entre o início da P e o QRS é de 0,5 s"],
         a=2, c="A P precede a contração atrial; o QRS surge ≈ 0,16 s após o início da P e precede a sístole ventricular; a T "
                "(repolarização) ocorre um pouco antes do fim da contração."),
    dict(q="Quanto à velocidade de condução do potencial de ação no coração:",
         opts=["É maior no músculo ventricular (4 m/s) que nas fibras de Purkinje",
               "É de 0,3 a 0,5 m/s no músculo atrial e ventricular e chega a 4 m/s nas fibras de Purkinje",
               "É igual à dos nervos mielinizados grandes",
               "É 10 vezes maior que no músculo esquelético",
               "Não depende das junções comunicantes"],
         a=1, c="Músculo cardíaco: 0,3 a 0,5 m/s (≈ 1/250 dos nervos grandes e ≈ 1/10 do músculo esquelético). Purkinje: até 4 m/s, "
                "permitindo a ativação quase simultânea dos ventrículos."),
    dict(q="Qual é a valva mais frequentemente lesada na febre reumática, e por quê?",
         opts=["Tricúspide, por receber o sangue venoso",
               "Pulmonar, por ser a mais fina",
               "Mitral, por sofrer maior traumatismo mecânico sob alta pressão",
               "Aórtica, por ter cordas tendíneas",
               "Todas são afetadas igualmente"],
         a=2, c="A mitral sofre mais trauma durante sua ação e é a mais lesada; a aórtica é a segunda. As valvas direitas, sob baixa "
                "pressão, são muito menos afetadas."),
]

OPEN = [
    dict(q="Mulher de 74 anos, hipertensa há 20 anos, procura o pronto-socorro com dispneia intensa e palpitações há 6 horas. "
           "Estava bem, apenas com cansaço aos grandes esforços. ECG: fibrilação atrial com resposta ventricular de 150 bpm. "
           "Ecocardiograma prévio: hipertrofia concêntrica do VE, fração de ejeção de 65%. Antes do episódio, ao exame, "
           "ouvia-se uma B4. (a) Explique, com base na fisiologia do ciclo cardíaco, por que ela descompensou com a FA de alta "
           "resposta, mesmo com fração de ejeção normal. (b) O que se espera da B4 durante a FA? Justifique. (c) Por que a "
           "hipertensão crônica levou a hipertrofia concêntrica?",
         a=["(a) Duas perdas simultâneas: <b>perda da contração atrial</b> (normalmente ≈ 20% do enchimento, e bem mais em ventrículo "
            "rígido, que enche pouco no início da diástole) e <b>encurtamento da diástole</b> pela taquicardia (a sístole passa de "
            "≈ 40% do ciclo para uma fração muito maior, e a diástole encurta mais que a sístole). Resultado: VDF e volume sistólico "
            "caem, e a pressão diastólica final e a do átrio esquerdo sobem (curva diastólica íngreme do ventrículo pouco complacente), "
            "com congestão pulmonar e dispneia. A fração de ejeção normal não protege porque o problema é de enchimento (diastólico).",
            "(b) A B4 <b>desaparece</b>, porque é gerada pela contração atrial empurrando sangue para um ventrículo pouco complacente. "
            "Na FA não há contração atrial organizada.",
            "(c) Lei de Laplace (T = P × r): a pressão sistólica cronicamente alta eleva a tensão da parede e o consumo de O₂. O "
            "espessamento da parede com redução do raio (hipertrofia concêntrica) alivia parcialmente essa tensão, mas deixa o "
            "ventrículo mais rígido e fibrótico."]),
    dict(q="Homem de 62 anos, 3 dias após infarto agudo do miocárdio inferior, apresenta dispneia súbita, estertores em ambos os "
           "campos pulmonares, hipotensão e um sopro sistólico novo no foco mitral. A monitorização da pressão capilar pulmonar "
           "mostra ondas v gigantes. (a) Qual estrutura provavelmente falhou e qual é a função normal dela? (b) Explique a origem "
           "das ondas v gigantes. (c) Como fica o volume sistólico efetivo que chega à aorta e por quê?",
         a=["(a) <b>Músculo papilar</b> (isquemia ou ruptura) ou corda tendínea, levando a <b>insuficiência mitral aguda</b>. "
            "Normalmente os papilares contraem com a parede e, pelas cordas tendíneas, <b>impedem o prolapso das cúspides para o átrio</b> "
            "na sístole. Eles não fecham a valva, que fecha passivamente pelo gradiente de pressão.",
            "(b) A onda v normal reflete o enchimento atrial com as valvas AV fechadas durante a sístole ventricular. Com a mitral "
            "incompetente, parte do volume do VE volta ao átrio na sístole. Como o átrio esquerdo não teve tempo de dilatar (quadro "
            "agudo, baixa complacência), a pressão sobe muito: <b>onda v gigante</b>, transmitida aos capilares pulmonares (edema).",
            "(c) O volume sistólico <b>efetivo cai</b>, porque parte do volume ejetado segue para o átrio de baixa pressão em vez da "
            "aorta. Pode haver regurgitação até durante a contração isovolumétrica, que deixa de ser realmente isovolumétrica. "
            "Resultado: baixo débito e hipotensão, com congestão pulmonar."]),
    dict(q="Paciente de 58 anos, com doença renal crônica e em uso de espironolactona, chega com fraqueza e bradicardia (38 bpm). "
           "Potássio sérico: 8,8 mEq/ℓ. (a) Explique o mecanismo pelo qual a hiperpotassemia altera o potencial de ação e a "
           "contração cardíaca. (b) Que efeitos sobre o coração o Guyton descreve para essa faixa de K⁺? (c) Por que o gluconato "
           "de cálcio é usado nessa situação, considerando o efeito do Ca²⁺ sobre o coração?",
         a=["(a) O K⁺ extracelular alto reduz o gradiente de K⁺ e <b>despolariza parcialmente o potencial de repouso</b> (fica menos negativo). "
            "Com isso a amplitude do potencial de ação diminui (menos canais de Na⁺ disponíveis), a condução fica lenta e a contração enfraquece.",
            "(b) Coração <b>dilatado e flácido</b>, <b>queda da frequência</b>, <b>bloqueio da condução AV</b> e, com 8 a 12 mEq/ℓ (2 a 3× o "
            "normal), fraqueza grave, arritmias e morte.",
            "(c) O Ca²⁺ tem efeito quase oposto ao do K⁺ alto sobre o coração (tende à contração mais forte, até espástica) e estabiliza a "
            "membrana, contrapondo o efeito do K⁺ enquanto se trata a causa e se retira o potássio. (A estabilização de membrana é conhecimento "
            "clínico complementar ao cap. 9.)"]),
]


# versão enxuta: mantém 26 das 37 questões originais e acrescenta uma de focos de ausculta
_FORA = {3, 5, 10, 13, 22, 27, 28, 30, 31, 32, 35}
MCQ = [q for i, q in enumerate(MCQ) if i not in _FORA] + [
    dict(q="Segundo o Porto, o foco tricúspide de ausculta localiza-se:",
         opts=["No 2º espaço intercostal direito, junto ao esterno",
               "No 2º espaço intercostal esquerdo, junto ao esterno",
               "Na base do apêndice xifoide, ligeiramente à esquerda",
               "No 5º espaço intercostal esquerdo, na linha hemiclavicular",
               "No 3º-4º espaço intercostal esquerdo, junto ao esterno"],
         a=2, c="Aórtico: 2º EIC direito justaesternal. Pulmonar: 2º EIC esquerdo. Aórtico acessório: 3º-4º EIC esquerdo. "
                "Tricúspide: base do apêndice xifoide, ligeiramente à esquerda. Mitral: 5º EIC esquerdo na linha hemiclavicular (ictus). "
                "Os focos não correspondem à projeção anatômica das valvas."),
]

OPEN_EXTRA = [
    ("Explique por que o músculo cardíaco não pode ser tetanizado.",
     "O potencial de ação ventricular tem um platô longo (entrada de Ca²⁺ por canais tipo L e redução da permeabilidade ao K⁺). "
     "O período refratário absoluto (0,25 a 0,30 s) cobre quase toda a contração, então um novo estímulo não consegue somar "
     "contrações. Isso garante relaxamento e enchimento entre os batimentos."),
    ("Descreva o acoplamento excitação-contração no músculo cardíaco e diga por que ele depende do cálcio extracelular.",
     "O potencial entra pelos túbulos T e abre canais de Ca²⁺ tipo L; esse Ca²⁺ ativa os receptores de rianodina do retículo "
     "sarcoplasmático, que liberam mais Ca²⁺ (liberação induzida por Ca²⁺). O Ca²⁺ liga-se à troponina C e forma pontes "
     "cruzadas. No relaxamento, SERCA2 recapta e o trocador Na⁺/Ca²⁺ expulsa o Ca²⁺. Como o retículo cardíaco é pouco "
     "desenvolvido e os túbulos T são largos e abertos ao interstício, a força depende do Ca²⁺ extracelular."),
    ("Descreva as fases do ciclo cardíaco do ventrículo esquerdo, dizendo o estado das valvas em cada uma.",
     ["Enchimento (rápido, diástase, sístole atrial): mitral aberta, aórtica fechada; a sístole atrial acrescenta ≈ 20%.",
      "Contração isovolumétrica: todas fechadas; pressão sobe até ≈ 80 mmHg.",
      "Ejeção (rápida e lenta): aórtica aberta, mitral fechada; saem ≈ 70 mℓ (FE ≈ 60%).",
      "Relaxamento isovolumétrico: todas fechadas; pressão cai até abrir a mitral."]),
    ("Enuncie o mecanismo de Frank-Starling e explique sua base celular.",
     "Dentro dos limites fisiológicos, quanto maior o enchimento (estiramento das fibras), maior a força de contração e o "
     "volume ejetado: o coração bombeia o que recebe. O estiramento leva actina e miosina a um grau de sobreposição mais "
     "próximo do ideal. Assim o débito acompanha o retorno venoso."),
    ("Diferencie B3 e B4 quanto ao momento no ciclo, mecanismo e significado clínico.",
     "B3: início do terço médio da diástole, pelo sangue do enchimento rápido; normal em jovens, em idosos indica IC sistólica. "
     "B4: fim da diástole, pela contração atrial contra ventrículo pouco complacente (HVE, hipertensão, idoso); desaparece na FA."),
    ("Defina pré-carga e pós-carga e dê um exemplo clínico de aumento de cada uma.",
     "Pré-carga: pressão diastólica final (grau de estiramento antes da contração); aumenta na hipervolemia ou na insuficiência "
     "aórtica. Pós-carga: pressão arterial contra a qual o ventrículo ejeta; aumenta na hipertensão e na estenose aórtica."),
]

G = "fig_livro/"
CARDS = [
    ("b", "No diagrama de Wiggers, onde caem B1 e B2?", "<b>B1</b>: início da sístole (fecham mitral e tricúspide). "
          "<b>B2</b>: início da diástole (fecham aórtica e pulmonar).", "fig/a_wiggers.png"),
    ("c", "Pulso venoso: onda {{c1::a}} = contração atrial; onda {{c2::c}} = abaulamento da tricúspide; onda {{c3::v}} = enchimento atrial "
          "com a tricúspide fechada.", "", "fig_web/a/a2_wiggers_pulso_venoso.png"),
    # ---------- lacunas (cloze)
    ("c", "O miocárdio funciona como {{c1::sincício}} porque os {{c2::discos intercalares}} têm {{c3::junções comunicantes (gap junctions)}}."),
    ("c", "Átrios e ventrículos são separados pelo {{c1::esqueleto fibroso}}; o impulso só passa pelo {{c2::feixe AV}}."),
    ("c", "Potencial ventricular: repouso ≈ {{c1::−85 mV}}, pico ≈ {{c2::+20 mV}}, platô de ≈ {{c3::0,2 s}}."),
    ("c", "Fase 0 = entrada de {{c1::Na⁺}} pelos canais {{c2::rápidos}}."),
    ("c", "O platô (fase 2) resulta da entrada de {{c1::Ca²⁺ por canais tipo L}} e da {{c2::queda (~5×) da permeabilidade ao K⁺}}.",
     "", "fig/a_potencial_acao.png"),
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
    ("c", "VDF {{c1::110 a 120 mℓ}}, VS {{c2::70 mℓ}}, VSF {{c3::40 a 50 mℓ}}, FE {{c4::≈ 60%}}.", "", "fig/a_wiggers.png"),
    ("c", "Fração de ejeção = {{c1::VS / VDF}}."),
    ("c", "Os músculos papilares {{c1::não fecham}} as valvas; eles {{c2::impedem o prolapso das cúspides para o átrio}}.",
     "", G + "g9_09.png"),
    ("c", "Ruptura de corda tendínea ou isquemia do papilar causa {{c1::insuficiência mitral aguda}}."),
    ("c", "A {{c1::incisura}} da curva aórtica marca o {{c2::fechamento da valva aórtica}}."),
    ("c", "Pressão aórtica ≈ {{c1::120/80 mmHg}}; lado direito ≈ {{c2::1/6}} disso."),
    ("c", "B1 = fechamento das {{c1::valvas AV}}; B2 = fechamento das {{c2::semilunares}}."),
    ("c", "B3 ocorre no {{c1::início do terço médio da diástole}}; em idosos indica {{c2::insuficiência cardíaca sistólica}}."),
    ("c", "B4 ocorre na {{c1::sístole atrial}} contra ventrículo {{c2::pouco complacente}} e {{c3::some na fibrilação atrial}}."),
    ("c", "Pré-carga = {{c1::pressão diastólica final}}; pós-carga = {{c2::pressão na aorta}}.", "", "fig/a_alca_pv.png"),
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
    ("c", "Foco mitral: {{c1::5º EIC esquerdo na linha hemiclavicular}} (ictus cordis).", "", "fig/a_focos.png"),
    ("c", "Foco tricúspide: {{c1::base do apêndice xifoide, ligeiramente à esquerda}}.", "", "fig/a_focos.png"),
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

TOPIC = dict(
    code="a", slug="a-musculo-cardiaco-e-valvas", title="Músculo cardíaco e valvas cardíacas",
    source="Guyton & Hall, Tratado de Fisiologia Médica, cap. 9 (bulhas: cap. 23; focos: Porto)",
    sections=SECTIONS, mcq=MCQ, open=OPEN, open_extra=OPEN_EXTRA, cards=CARDS, occ="dia_a",
)
