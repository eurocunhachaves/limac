#!/usr/bin/env python3
"""Baralho de sons cardíacos: só cartões de áudio, separado dos baralhos dos temas
(não entra no baralho completo).

Cada cartão toca uma gravação real e pergunta o que se ouve. O verso traz a
resposta, a parte "Para associar", que liga o som a outro tema do material
(fisiologia A–H e semiologia S–U), e a fonte da gravação. Todas as gravações têm
licença livre; autoria, licença e o que foi alterado em cada uma ficam em
fonte/sons/CREDITOS.md, gerado junto com o baralho.

Cada gravação foi conferida pelo laudo da fonte e pelo traçado do som (envelope
e espectrograma): ritmo, frequência e posição de cada ruído no ciclo.

Uso:  python3 fonte/anki_sons.py                  gera anki/LIMAC-Sons-cardiacos.apkg e CREDITOS.md
      python3 fonte/anki_sons.py recorta <pasta>  refaz fonte/sons/*.mp3 a partir das gravações
                                                  originais em <pasta> (precisa de ffmpeg)
"""
import json, re, shutil, subprocess, sys
from pathlib import Path
from urllib.parse import quote

import genanki

FONTE = Path(__file__).resolve().parent
REPO = FONTE.parent
SONS = FONTE / "sons"
SAIDA = REPO / "anki" / "LIMAC-Sons-cardiacos.apkg"
SAIDA_PROJETO = Path("/mnt/project-files/liga-cardio-v2") / "Anki Sons - Ausculta cardíaca (áudio).apkg"

sys.path.insert(0, str(FONTE))
from anki import CSS, _id          # noqa: E402  (mesmo visual dos outros baralhos)
from build import md2html, ref_livro  # noqa: E402

LICENCAS = {
    "CC BY-SA 3.0": "https://creativecommons.org/licenses/by-sa/3.0/deed.pt-br",
    "CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br",
    "CC0 (domínio público)": "https://creativecommons.org/publicdomain/zero/1.0/deed.pt-br",
    "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/deed.pt-br",
    "ODC-By 1.0": "https://opendatacommons.org/licenses/by/1-0/",
}

# Bancos de gravações: nome, licença, link e como citar
HLS = ("banco HLS-CMDS (manequim clínico, estetoscópio digital)", "CC BY 4.0",
       "https://doi.org/10.6084/m9.figshare.29000189.v1", "Torabi, Shirani e Reilly")
CIRCOR = ("banco CirCor DigiScope, PhysioNet (crianças e adolescentes)", "ODC-By 1.0",
          "https://physionet.org/content/circor-heart-sound/1.0.3/", "Oliveira e colaboradores")
CITACOES = {
    HLS[0]: "Torabi Y, Shirani S, Reilly JP. Descriptor: Heart and Lung Sounds Dataset Recorded From a "
            "Clinical Manikin Using Digital Stethoscope (HLS-CMDS). *IEEE Data Descriptions*, 2025. "
            "doi:10.1109/IEEEDATA.2025.3566012. Dados: doi:10.6084/m9.figshare.29000189.v1 "
            "(também no UCI Machine Learning Repository, conjunto 1202).",
    CIRCOR[0]: "Oliveira J, Renna F, Costa P, Nogueira M, Oliveira AC, Elola A, Ferreira C, Jorge A, "
               "Bahrami Rad A, Reyna M, Sameni R, Clifford G, Coimbra M. The CirCor DigiScope Phonocardiogram "
               "Dataset (versão 1.0.3). PhysioNet, 2022. doi:10.13026/tshs-mw03. Artigo: Oliveira J et al. "
               "The CirCor DigiScope Dataset: From Murmur Detection to Murmur Classification. *IEEE Journal of "
               "Biomedical and Health Informatics*, 2022. doi:10.1109/JBHI.2021.3137048. Citação padrão do "
               "PhysioNet: Pollard T et al. PhysioNet as a global platform for biomedical research. "
               "*Nature Health*, 2026. doi:10.1038/s44360-026-00096-z.",
}


def commons(titulo, autor, licenca):
    """Gravação do Wikimedia Commons: (obra, autor, acervo, licença, link)."""
    return (f"“{titulo}”", autor, "Wikimedia Commons", licenca,
            "https://commons.wikimedia.org/wiki/File:" + quote(titulo.replace(" ", "_")))


def banco(registro, b):
    """Gravação de um banco de dados: (obra, autor, acervo, licença, link)."""
    return (f"“{registro}”", None, b[0], b[1], b[2])


# ------------------------------------------------------------ cartões
# trecho = (início, duração) em segundos na gravação original; inteira = usa a gravação toda
CARTOES = [
    # ---- bulhas e ritmo
    dict(chave="bulhas-normais", grupo="Bulhas normais",
         arquivo="commons/HROgg_Louder.ogg", trecho=(1.0, 15.0),
         origem=commons("HROgg Louder.ogg", "James Heilman, MD (versão mais alta por Natural Philo)", "CC BY-SA 3.0"),
         laudo="descrição: bulhas normais a cerca de 70 bpm",
         pergunta="Ritmo regular em dois tempos. Qual é a B1 e qual é a B2?",
         resposta="Coração normal (≈ 70 bpm), o **TUM-TA**. A **B1** (TUM) abre a sístole: é o fechamento da "
                  "**mitral e da tricúspide**, mais grave e um pouco mais longa. A **B2** (TA) fecha a sístole: "
                  "fechamento da **aórtica e da pulmonar**, mais aguda e mais curta. O intervalo B1 → B2 "
                  "(**pequeno silêncio**, a sístole) é **mais curto** que o B2 → B1 (**grande silêncio**, a diástole).",
         associar="**Tema A (ciclo cardíaco):** a B1 marca o início da **contração isovolumétrica** e a B2 o do "
                  "**relaxamento isovolumétrico**; nas duas fases as quatro valvas estão fechadas. **Tema T:** a B1 "
                  "coincide com o **ictus** e com o **pulso carotídeo**; palpe a carótida enquanto ausculta para saber "
                  "o que é sístole.",
         figura="p47_03"),
    dict(chave="frequencia-normal", grupo="Bulhas normais",
         arquivo="commons/Emilys_heartbeat.wav", trecho=(2.0, 12.0),
         origem=commons("Emily's heartbeat.wav", "EmilyHopeS", "CC BY-SA 4.0"),
         laudo="descrição: adolescente saudável, foco tricúspide, deitada e em apneia, cerca de 66 bpm",
         pergunta="Conte os batimentos (cada TUM-TA é um) e estime a frequência. Está normal?",
         resposta="≈ **66 bpm**, ritmo **regular**: frequência **normal** (**60–100 bpm**). Para contar, reconheça "
                  "primeiro o par TUM-TA e conte só as B1.",
         associar="**Tema B:** quem dita a frequência é o **nó sinusal**, que dispara sozinho a **70–80/min**; em "
                  "repouso predomina o **tônus vagal**, que pode deixá-la um pouco abaixo disso. **Tema U:** no pulso "
                  "radial, conte **1 minuto inteiro** e compare com a FC auscultada, para não perder um **déficit de pulso**."),
    dict(chave="bradicardia-atleta", grupo="Ritmo e frequência",
         arquivo="commons/Athletic_bradycardia_wav.wav", trecho=(1.0, 15.0),
         origem=commons("Athletic bradycardia wav.wav", "Athletearrhythmia", "CC0 (domínio público)"),
         laudo="descrição: atleta de elite em repouso, bradicardia de 42 bpm",
         pergunta="Atleta jovem, sem queixas, em repouso. Conte a frequência: que ritmo é este?",
         resposta="**Bradicardia sinusal** (≈ **42 bpm**, regular), comum em **atletas**. O diferencial é o **BAVT**, "
                  "que também fica em 30–40 bpm: a bradicardia sinusal **acelera com o exercício** e tem B1 de "
                  "intensidade constante; no BAVT a B1 varia e aparece a **bulha em canhão**.",
         associar="**Tema B:** o atleta tem **tônus vagal** alto; a acetilcolina abre canais de K⁺ e **hiperpolariza** "
                  "o nó sinusal, que demora mais para chegar ao limiar. **Tema G:** o débito se mantém porque o "
                  "**volume sistólico** do coração treinado é maior (DC = VS × FC)."),
    dict(chave="taquicardia", grupo="Ritmo e frequência",
         arquivo="hls-cmds/F_T_A.wav", trecho=(0.0, 12.0),
         origem=banco("F_T_A.wav", HLS),
         laudo="rótulo do banco: taquicardia",
         pergunta="Ritmo regular e rápido. Estime a frequência. Por que aqui é difícil saber qual bulha é a B1?",
         resposta="**Taquicardia** regular (≈ **150 bpm**). Com a FC alta a **diástole encurta** e fica do tamanho da "
                  "sístole: os intervalos entre as bulhas ficam **quase iguais** e o TUM-TA perde a cadência. Para achar a "
                  "B1, **palpe o pulso carotídeo**: a B1 coincide com ele.",
         associar="**Tema A:** a taquicardia encurta **mais a diástole que a sístole**, e com ela o tempo de "
                  "**enchimento** do ventrículo; em FC muito alta o débito cai. **Tema S:** palpitação com FC de "
                  "**100 a 150** costuma ser **taquicardia sinusal**; **acima de 150**, com início e fim súbitos, "
                  "pense em **taquicardia paroxística**."),
    # ---- arritmias
    dict(chave="taquicardia-paroxistica", grupo="Arritmias",
         arquivo="commons/Ash-SVT.ogg", trecho=(5.0, 12.0),
         origem=commons("Ash-SVT.ogg", "Ashquacks", "CC BY-SA 4.0"),
         laudo="descrição: homem de 20 anos durante uma crise de taquicardia supraventricular paroxística",
         pergunta="Rapaz de 20 anos com palpitação que começou de repente. Estime a frequência: que arritmia é esta?",
         resposta="**Taquicardia paroxística supraventricular**: ritmo **regular** e muito rápido (≈ **200 bpm**, acima "
                  "de 150). O paciente conta que a palpitação **começa e termina de repente**.",
         associar="**Tema A:** a ≈ 200 bpm sobra pouquíssimo tempo de **diástole** para encher o ventrículo; o "
                  "**débito cai** e podem surgir tontura, dispneia e até **síncope** (tema S: síncope arrítmica com FC "
                  "acima de 150). **Tema F:** a **massagem do seio carotídeo** aumenta o tônus vagal e pode reverter "
                  "esta taquicardia.",
         figura="p47_06"),
    dict(chave="fibrilacao-atrial", grupo="Arritmias",
         arquivo="hls-cmds/M_AF_LC.wav", trecho=(0.0, 15.0),
         origem=banco("M_AF_LC.wav", HLS),
         laudo="rótulo do banco: fibrilação atrial", inteira=True,
         pergunta="Preste atenção aos intervalos entre os batimentos. Que ritmo é este?",
         resposta="**Fibrilação atrial**: ritmo **completamente irregular**, sem nenhum padrão (*delirium cordis*). Na "
                  "FA a **B1 varia de intensidade** de um batimento para outro e o pulso tem **déficit**.",
         associar="**Tema C:** no ECG **não há onda P** (os átrios não se contraem de forma organizada) e os intervalos "
                  "RR são irregulares. **Tema T:** sem contração atrial **não há B4** e some o **reforço pré-sistólico** "
                  "da estenose mitral. **Tema U:** no pulso venoso falta o **descenso X**.",
         figura="p47_09"),
    dict(chave="fibrilacao-atrial-rapida", grupo="Arritmias",
         arquivo="commons/AfibO.ogg", trecho=(0.0, 11.33),
         origem=commons("AfibO.ogg", "James Heilman, MD", "CC BY-SA 3.0"),
         laudo="descrição: fibrilação atrial rápida", inteira=True,
         pergunta="Ritmo rápido e irregular. Se você contasse o pulso radial ao mesmo tempo, o que esperaria encontrar?",
         resposta="**Fibrilação atrial de resposta ventricular rápida** (≈ **140 bpm**, irregular). Espere **déficit de "
                  "pulso**: os batimentos que vêm logo depois de um ciclo curto encontram o ventrículo pouco cheio e não "
                  "geram onda de pulso palpável, então o pulso radial conta **menos** batimentos que a ausculta.",
         associar="**Tema A (Frank-Starling):** ciclo curto = **pouco enchimento** = pouco estiramento = **volume "
                  "sistólico pequeno**. **Tema U:** por isso o pulso se conta por **1 minuto inteiro**, comparando com "
                  "a FC auscultada."),
    # ---- bulhas extras e cliques
    dict(chave="b3", grupo="Bulhas extras",
         arquivo="hls-cmds/M_S3_LLSB.wav", trecho=(0.0, 15.0),
         origem=banco("M_S3_LLSB.wav", HLS),
         laudo="rótulo do banco: 3ª bulha", inteira=True,
         pergunta="Há um terceiro ruído em cada ciclo. Ele vem logo depois da B2 ou logo antes da B1? Qual é?",
         resposta="**B3**: ruído **grave** logo **depois da B2**, no início da diástole (**protodiastólica**), formando "
                  "um ritmo em três tempos. Ouça com a **campânula** no ictus, em **decúbito lateral esquerdo**. É "
                  "normal em **crianças e jovens**; no adulto com cardiopatia é o **galope ventricular**, o “grito de "
                  "socorro do miocárdio”.",
         associar="**Tema A:** a B3 cai na fase de **enchimento rápido**: o sangue acumulado no átrio entra de uma vez "
                  "e faz vibrar a parede do ventrículo. **Tema S:** no adulto, B3 + dispneia de esforço, ortopneia e "
                  "edema compõem o quadro da **insuficiência cardíaca**.",
         figura="p47_11"),
    dict(chave="b4", grupo="Bulhas extras",
         arquivo="hls-cmds/M_S4_LUSB.wav", trecho=(2.5, 12.5),
         origem=banco("M_S4_LUSB.wav", HLS),
         laudo="rótulo do banco: 4ª bulha",
         pergunta="Há um ruído extra colado à B1. Ele vem antes ou depois dela? Qual é?",
         resposta="**B4**: ruído fraco e grave logo **antes da B1** (**pré-sistólico**), no fim da diástole, formando um "
                  "ritmo em três tempos. É a **contração atrial** contra um ventrículo **pouco complacente** "
                  "(hipertensão, doença coronariana, hipertrofia, estenose aórtica): o **galope atrial**.",
         associar="**Tema A:** a sístole atrial completa só **≈ 20%** do enchimento, mas no ventrículo rígido ela pesa "
                  "muito mais. **Tema C:** a B4 vem logo depois da **onda P** do ECG. **Tema U:** é o mesmo momento da "
                  "**onda A** do pulso venoso. E na **fibrilação atrial não há B4**."),
    dict(chave="clique-mesossistolico", grupo="Bulhas extras",
         arquivo="commons/Mitral_Valve_Prolapse.wav", trecho=(0.0, 11.85),
         origem=commons("Mitral Valve Prolapse.wav", "EmilyHopeS", "CC BY-SA 4.0"),
         laudo="descrição: moça de 16 anos, sem sintomas, com prolapso da valva mitral e insuficiência mitral; ouvem-se "
               "clique e sopro sistólicos", inteira=True,
         pergunta="Moça de 16 anos, sem sintomas. Há um ruído seco e agudo no meio da sístole. O que é e o que indica?",
         resposta="**Clique mesossistólico**, do **prolapso da valva mitral**. É seco e agudo, nas áreas mitral ou "
                  "tricúspide, e **varia com a respiração e a posição**. Esta paciente também tem **insuficiência "
                  "mitral**, por isso o clique vem acompanhado de sopro sistólico.",
         associar="**Tema A:** quem impede a cúspide de abaular para o átrio são as **cordas tendíneas** e os **músculos "
                  "papilares**. No prolapso a cúspide passa do ponto na sístole e o clique é o **tensionamento brusco** "
                  "das cordas; se ela não veda, surge o sopro da **insuficiência mitral**. **Tema S:** o prolapso mitral "
                  "é mais comum em **mulheres jovens**."),
    # ---- sopros
    dict(chave="sopro-ejecao-aortico", grupo="Sopros",
         arquivo="circor/69079_AV.wav", trecho=(6.2, 4.95),
         origem=banco("69079_AV.wav", CIRCOR),
         laudo="laudo do banco: criança, foco aórtico (onde o sopro é mais audível), sopro mesossistólico em diamante, "
               "grau III/VI, rude",
         pergunta="Gravação no foco aórtico. O sopro começa junto com a B1 ou logo depois dela? Que forma ele tem?",
         resposta="**Sopro sistólico de ejeção**: começa **logo depois da B1**, cresce e decresce (**crescendo-"
                  "decrescendo**, em diamante) e termina **antes da B2**. Timbre rude. No foco aórtico, é o padrão da "
                  "**estenose aórtica**, que **irradia para o pescoço**.",
         associar="**Tema D:** sopro é **fluxo turbulento**: o orifício estreito aumenta a **velocidade** e o **número de "
                  "Reynolds** passa do limite. **Tema A:** a forma em diamante acompanha o gradiente de pressão da "
                  "**ejeção**, que só começa quando a valva abre, no fim da **contração isovolumétrica**. **Tema U:** na "
                  "estenose aórtica o pulso é **parvus** e **anacrótico**.",
         figura="p47_15"),
    dict(chave="sopro-ejecao-pulmonar", grupo="Sopros",
         arquivo="circor/40840_PV.wav", trecho=(2.0, 12.0),
         origem=banco("40840_PV.wav", CIRCOR),
         laudo="laudo do banco: adolescente, foco pulmonar (onde o sopro é mais audível), sopro mesossistólico em "
               "diamante, grau III/VI, agudo e rude",
         pergunta="Gravação no foco pulmonar (2º espaço intercostal esquerdo). Que parte do ciclo o sopro ocupa?",
         resposta="**Sopro sistólico de ejeção** no foco pulmonar: **mesossistólico**, em diamante, com a diástole "
                  "silenciosa. Pense em **estenose pulmonar** ou em **hiperfluxo** pela valva pulmonar, como na **CIA**, "
                  "que também dá **desdobramento fixo da B2**.",
         associar="**Temas A e T:** o sopro de ejeção nunca encobre a B1, porque entre a B1 e a abertura da valva há a "
                  "**contração isovolumétrica**, sem fluxo; o de **regurgitação** começa junto com a B1 e a recobre. "
                  "**Tema D:** fluxo alto por uma valva normal também gera turbulência; por isso muitas crianças têm "
                  "sopro de ejeção **inocente**."),
    dict(chave="sopro-holossistolico-mitral", grupo="Sopros",
         arquivo="circor/50233_MV.wav", trecho=(2.0, 12.0),
         origem=banco("50233_MV.wav", CIRCOR),
         laudo="laudo do banco: criança, foco mitral (onde o sopro é mais audível), sopro holossistólico em platô, grau "
               "III/VI, agudo e rude",
         pergunta="Gravação no foco mitral. Sobra algum intervalo silencioso entre a B1 e a B2?",
         resposta="Não: o sopro ocupa a sístole inteira, de B1 a B2, em platô. É **holossistólico**, um sopro de "
                  "**regurgitação** (começa junto com a B1 e a recobre). No foco mitral, é o padrão da **insuficiência "
                  "mitral**, que **irradia para a axila**.",
         associar="**Tema A:** na insuficiência mitral **não há contração isovolumétrica de verdade**: assim que a "
                  "pressão do VE passa a do átrio esquerdo, o sangue já volta para o átrio, até o fim da sístole. "
                  "**Tema T:** sopro **holossistólico nunca é inocente**. **Tema S:** o átrio esquerdo congesto leva à "
                  "**dispneia**.",
         figura="p47_16"),
    dict(chave="sopro-holossistolico-tricuspide", grupo="Sopros",
         arquivo="circor/49574_TV.wav", trecho=(2.0, 12.0),
         origem=banco("49574_TV.wav", CIRCOR),
         laudo="laudo do banco: criança, foco tricúspide (onde o sopro é mais audível), sopro holossistólico em platô, "
               "grau III/VI, agudo e rude",
         pergunta="Sopro holossistólico no foco tricúspide. Que manobra diz se ele é tricúspide ou um sopro mitral "
                  "propagado?",
         resposta="A manobra de **Rivero-Carvallo**: peça uma **inspiração profunda**. Se o sopro **aumenta**, é "
                  "**tricúspide** (insuficiência tricúspide); se não muda ou diminui, é **mitral** propagado. Na borda "
                  "esternal esquerda baixa, um holossistólico também pode ser **CIV**.",
         associar="**Temas G e U:** na inspiração a pressão intrapleural fica **mais negativa** e puxa **mais sangue para "
                  "o coração direito**; é por isso que a jugular **colaba na inspiração**. Mais volume no VD, mais "
                  "refluxo pela tricúspide, sopro mais alto."),
    dict(chave="sopro-inocente", grupo="Sopros",
         arquivo="commons/Stills_Murmur_in_a_Toddler.ogg", trecho=(20.0, 12.0),
         origem=commons("Stills Murmur in a Toddler.ogg", "Lars Erickson, MD", "CC BY-SA 3.0"),
         laudo="descrição: sopro inocente de Still em criança pequena",
         pergunta="Criança pequena saudável, sem sintomas. Sopro sistólico suave e vibratório. O que é e o que você "
                  "conferiria?",
         resposta="**Sopro inocente** (o sopro de **Still**, comum na infância). Confira: **sistólico**, proto ou "
                  "mesossistólico (**nunca holossistólico**), suave (+ a ++), **sem frêmito** e **sem irradiação**, "
                  "na **borda esternal esquerda** e no mesocárdio, e **o resto do exame normal**. Sopro inocente é "
                  "uma conclusão, depois de examinar a criança.",
         associar="**Tema D:** sopro é turbulência, e turbulência depende da **velocidade** do sangue; na criança, de "
                  "parede torácica fina, um fluxo **normal** já pode ser ouvido. **Tema T:** sopro diastólico, "
                  "holossistólico ou com frêmito **nunca** é inocente.",
         figura="p47_18"),
    dict(chave="sopro-presistolico", grupo="Sopros",
         arquivo="hls-cmds/M_LDM_LC.wav", trecho=(0.0, 15.0),
         origem=banco("M_LDM_LC.wav", HLS),
         laudo="rótulo do banco: sopro telediastólico", inteira=True,
         pergunta="O sopro fica no fim da diástole e cresce até uma B1 forte. Que reforço é este e em que doença ele "
                  "aparece?",
         resposta="**Sopro pré-sistólico** (telediastólico) em **crescendo** até uma **B1 hiperfonética**: é o **reforço "
                  "pré-sistólico** do **ruflar** da **estenose mitral**, causado pela **contração atrial**. Ausculte no "
                  "foco mitral com a **campânula**, em **decúbito lateral esquerdo**.",
         associar="**Tema A:** é a **sístole atrial** empurrando sangue por uma valva estreita, no último terço da "
                  "diástole. Por isso o reforço **some na fibrilação atrial** (temas S e C: sem contração atrial e sem "
                  "onda P). **Tema S:** a estenose mitral é mais comum em **mulheres jovens** e vem da **febre reumática**.",
         figura="p47_17"),
    # ---- vasos
    dict(chave="sopro-carotideo", grupo="Vasos",
         arquivo="commons/MurmurO.ogg", trecho=(0.0, 5.57),
         origem=commons("MurmurO.ogg", "James Heilman, MD", "CC BY-SA 3.0"),
         laudo="descrição: sopro na carótida esquerda de um homem com estenose de 70%", inteira=True,
         pergunta="Estetoscópio sobre a carótida de um homem. O que se ouve e quais são as duas origens possíveis?",
         resposta="**Sopro carotídeo**, um ruído a cada batimento, em geral sistólico. Pode nascer na **própria "
                  "carótida** (estenose por **aterosclerose**; nesta gravação, obstrução de **70%**) ou ser o sopro da "
                  "**estenose aórtica irradiado** para o pescoço.",
         associar="**Tema D:** a placa estreita a luz, a **velocidade** sobe e o fluxo fica **turbulento** (número de "
                  "Reynolds alto): é a mesma física de todo sopro. **Tema F:** logo acima da bifurcação fica o **seio "
                  "carotídeo**, com os **barorreceptores**. Massageá-lo aumenta o tônus vagal (é a manobra das "
                  "taquicardias supraventriculares), mas uma carótida com sopro não se massageia, pelo risco de soltar "
                  "a placa."),
]


# ------------------------------------------------------------ recorte dos áudios
ALVO_LUFS, PICO_DBTP = -20.0, -1.5


def _pico(arq: Path) -> float:
    """Pico verdadeiro (dBTP) de um arquivo de áudio."""
    saida = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(arq), "-af", "ebur128=peak=true", "-f", "null", "-"],
                           capture_output=True, text=True, check=True).stderr
    return float(re.findall(r"Peak:\s+(\S+) dBFS", saida)[-1])


def recorta(originais: Path):
    """Refaz fonte/sons/<chave>.mp3: recorte, mono de 22,05 kHz, passa-alta de 20 Hz,
    entrada e saída suaves e ganho fixo (sem compressão) para ≈ -20 LUFS, sem passar
    de -1,5 dBTP no MP3 final (96 kbps)."""
    SONS.mkdir(exist_ok=True)
    for c in CARTOES:
        ini, dur = c["trecho"]
        entrada = ["-ss", f"{ini}", "-t", f"{dur}", "-i", str(originais / c["arquivo"])]
        filtro = (f"aformat=channel_layouts=mono,aresample=22050,highpass=f=20,"
                  f"afade=t=in:d=0.05,afade=t=out:st={dur - 0.25:.2f}:d=0.25")
        med = subprocess.run(["ffmpeg", "-hide_banner", *entrada, "-af", filtro + ",loudnorm=print_format=json",
                              "-f", "null", "-"], capture_output=True, text=True, check=True).stderr
        m = json.loads(med[med.rindex("{"):med.rindex("}") + 1])
        ganho = min(ALVO_LUFS - float(m["input_i"]), PICO_DBTP - float(m["input_tp"]))
        mp3 = SONS / f"{c['chave']}.mp3"
        for _ in range(4):  # a codificação em MP3 pode subir o pico; reduz o ganho e refaz
            subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *entrada,
                            "-af", f"{filtro},volume={ganho:.2f}dB", "-c:a", "libmp3lame", "-b:a", "96k", str(mp3)],
                           check=True)
            pico = _pico(mp3)
            if pico <= PICO_DBTP + 0.3:
                break
            ganho -= pico - PICO_DBTP
        print(f"{c['chave']}: {dur:.1f} s, ganho {ganho:+.1f} dB, pico {pico:.1f} dBTP")


# ------------------------------------------------------------ baralho
SOM = genanki.Model(
    _id("limac-som-v1"), "LIMAC · Som",
    fields=[{"name": "Tema"}, {"name": "Som"}, {"name": "Pergunta"}, {"name": "Resposta"},
            {"name": "Associar"}, {"name": "Imagem"}, {"name": "Fonte"}],
    templates=[{
        "name": "Som",
        "qfmt": '<span class="tag">{{Tema}}</span><div class="q">{{Pergunta}}</div>{{Som}}'
                '<div class="dica">Use fone de ouvido e repita o som quantas vezes precisar.</div>',
        "afmt": '<span class="tag">{{Tema}}</span><div class="q">{{Pergunta}}</div>{{Som}}'
                '<hr id="answer"><div class="a">{{Resposta}}</div>'
                '{{#Associar}}<div class="assoc"><span class="rot">Para associar</span>{{Associar}}</div>{{/Associar}}'
                '{{#Imagem}}{{Imagem}}{{/Imagem}}<div class="fonte">{{Fonte}}</div>',
    }],
    css=CSS + """
.dica { margin-top: 10px; font-size: 13px; color: #7a7f88; }
.assoc { margin-top: 12px; padding: 10px 14px; border-left: 4px solid #2e6b46; background: #edf5ef;
  border-radius: 0 6px 6px 0; font-size: 17px; }
.nightMode .assoc, .night_mode .assoc { background: #23322a; }
.assoc .rot { display: block; font-size: 11px; letter-spacing: .08em; text-transform: uppercase;
  font-weight: 700; color: #2e6b46; margin-bottom: 4px; }
.nightMode .assoc .rot, .night_mode .assoc .rot { color: #8fd1a6; }
""")


def credito(c) -> str:
    obra, autor, acervo, licenca, _ = c["origem"]
    quem = f", de {autor}" if autor else ""
    alterou = "Volume ajustado" if c.get("inteira") else "Recortada e com volume ajustado"
    return f"Gravação {obra}{quem}, {acervo}, {licenca}. {c['laudo'][0].upper() + c['laudo'][1:]}. {alterou}."


def monta():
    deck = genanki.Deck(_id("limac-deck-sons"), "LIMAC Cardiologia::Sons · Ausculta cardíaca",
                        description="Cartões só de áudio com gravações reais. Use fone de ouvido. No verso, a parte "
                                    "<b>Para associar</b> liga cada som a outro tema do material.")
    tmp = FONTE / "_build" / "anki" / "sons"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    midia = []
    for c in CARTOES:
        nome = f"limac_som_{c['chave']}.mp3"
        shutil.copy(SONS / f"{c['chave']}.mp3", tmp / nome)
        midia.append(str(tmp / nome))
        img, ref = "", ""
        if c.get("figura"):
            k = c["figura"]
            fig = f"limac_{k}.png"
            shutil.copy(FONTE / "figuras" / "porto" / f"{k}.png", tmp / fig)
            midia.append(str(tmp / fig))
            img, ref = f'<img src="{fig}">', f" Figura: {ref_livro(k)}."
        nota = genanki.Note(model=SOM, fields=[f"Sons · {c['grupo']}", f"[sound:{nome}]", md2html(c["pergunta"]),
                                               md2html(c["resposta"]), md2html(c["associar"]), img,
                                               md2html(credito(c)) + ref],
                            guid=genanki.guid_for("som", c["chave"]), tags=["sons", "sons_" + c["chave"]])
        deck.add_note(nota)
    return deck, midia


def creditos() -> str:
    L = ["# Créditos das gravações", "",
         "Gravações do baralho de sons ([`anki/LIMAC-Sons-cardiacos.apkg`](../../anki/LIMAC-Sons-cardiacos.apkg)). "
         "Todas têm licença livre. Em todas foram feitas as mesmas alterações: recorte do trecho indicado (quando "
         "houve), conversão para MP3 mono de 22,05 kHz, filtro passa-alta de 20 Hz, entrada e saída suaves e ganho "
         "fixo de volume, sem compressão. As versões alteradas de gravações CC BY-SA seguem sob a mesma licença.",
         "", "| Arquivo | Gravação original | Autor | Acervo | Licença | O que a fonte diz | Trecho usado |",
         "|---|---|---|---|---|---|---|"]
    autores = {HLS[0]: HLS[3], CIRCOR[0]: CIRCOR[3]}
    for c in CARTOES:
        obra, autor, acervo, licenca, url = c["origem"]
        ini, dur = c["trecho"]
        trecho = "inteira" if c.get("inteira") else f"{ini:.1f}–{ini + dur:.1f} s".replace(".", ",")
        L.append(f"| `{c['chave']}.mp3` | [{obra}]({url}) | {autor or autores[acervo]} | {acervo} | "
                 f"[{licenca}]({LICENCAS[licenca]}) | {c['laudo'].split(': ', 1)[1]} | {trecho} |")
    L += ["", "## Como citar os bancos de dados", ""]
    L += [f"- **{nome[0].upper() + nome[1:]}:** {cit}" for nome, cit in CITACOES.items()]
    L += ["", "As figuras que aparecem no verso de alguns cartões são do Porto (*Semiologia Médica*, 8ª ed., cap. 47), "
          "reproduzidas para uso pessoal de estudo, como no resto do material.", ""]
    return "\n".join(L)


def main():
    if sys.argv[1:2] == ["recorta"]:
        recorta(Path(sys.argv[2]))
        return
    deck, midia = monta()
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    pacote = genanki.Package(deck)
    pacote.media_files = midia
    pacote.write_to_file(str(SAIDA))
    (SONS / "CREDITOS.md").write_text(creditos(), encoding="utf-8")
    if SAIDA_PROJETO.parent.exists():
        shutil.copy(SAIDA, SAIDA_PROJETO)
    print(f"baralho de sons: {len(CARTOES)} cartões em {SAIDA.relative_to(REPO)}")


if __name__ == "__main__":
    main()
