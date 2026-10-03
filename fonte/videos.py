"""Vídeos recomendados para os temas de Semiologia (S, T e U) e bibliotecas
gratuitas de sons cardíacos, usados por build.py na página (README) de cada tema.

Cada vídeo foi aberto e conferido em 03/10/2026: existe, está disponível, o
título e o canal são estes, a duração é esta e o assunto bate com o subtema.

VIDEOS[código] = [(subtema, [(idioma, id no YouTube, título, canal, duração,
                              por que ver), ...]), ...]
Na página, cada subtema lista primeiro os vídeos em português e depois os em
inglês, do mais curto ao mais longo.
"""

CONFERIDO = "03/10/2026"

VIDEOS = {
    "s": [
        ("Dor torácica", [
            ("PT", "sn6cDa4v0lw", "Cardiologia: abordagem à dor torácica", "Jaleko Acadêmicos", "18:18",
             "Diferencia a dor da síndrome coronariana aguda, da dissecção de aorta, do TEP, da pericardite, "
             "do espasmo esofágico e da costocondrite."),
            ("PT", "Oi5qW38b2j8", "Dor torácica: diagnósticos diferenciais", "Medicina Resumida", "40:24",
             "As causas graves de dor no peito, uma por uma, e a abordagem inicial."),
            ("EN", "eiRIm6BOzP4", "Chest Pain History Taking - OSCE Guide", "Geeky Medics", "8:41",
             "A anamnese da dor torácica feita do início ao fim com o roteiro SOCRATES (local, início, caráter, "
             "irradiação, sintomas associados, tempo, fatores de piora e melhora, intensidade)."),
        ]),
        ("Dispneia, ortopneia e dispneia paroxística noturna", [
            ("PT", "PCKXLBxmAJg", "Dispneia: ortopneia, platipneia, trepopneia?", "Gabriel Pereira", "2:24",
             "Conceito rápido dos tipos de dispneia ligados à posição do corpo."),
            ("EN", "q2t9sFITAIY", "Understanding Heart Failure: Visual Explanation for Students", "Zero To Finals", "9:43",
             "Insuficiência cardíaca ilustrada, com atenção especial à dispneia paroxística noturna."),
            ("EN", "9Oubwtvu_TI", "Dyspnea, PND & Orthopnea", "AETCM Emergency Medicine", "32:15",
             "Mecanismo da ortopneia e da DPN e como separar a dispneia cardíaca da respiratória."),
        ]),
        ("Síncope", [
            ("PT", "2uuSn6wYggU", "Síncope cardíaca e suas características e procedimentos", "Medcel", "8:49",
             "Resumo das causas cardíacas de síncope (estruturais e arrítmicas) e dos achados de alto risco."),
            ("PT", "dv0jFSToKf8", "Síncope de etiologia cardíaca", "Medicina Interna", "47:39",
             "Aula completa: classificação, avaliação inicial, critérios de alto risco e papel do ECG."),
            ("EN", "iJ6g5rsQKaM", "An Approach to Syncope", "Strong Medicine", "15:32",
             "Compara síncope reflexa (vasovagal), cardiogênica e ortostática, e síncope × crise convulsiva."),
            ("EN", "nTcI1cITnI0", "Syncope | Clinical Medicine", "Ninja Nerd", "31:42",
             "A fisiopatologia de cada tipo de síncope, passo a passo, e a diferença com crise convulsiva."),
        ]),
        ("Cianose", [
            ("PT", "o8IDbxnQklY", "Inspeção geral: cianose", "RABISCANDO", "28:40",
             "Definição clínica e fisiopatologia da cianose (aula do exame respiratório que vale também para o cardíaco)."),
            ("EN", "s5UQ_JpvFqc", "Cyanosis", "Dr Matt & Dr Mike", "17:06",
             "Mecanismo da cianose central e da periférica, com a curva de dissociação da hemoglobina."),
        ]),
        ("Arritmias no exame clínico", [
            ("PT", "CAXJmVU20-I", "O que esperar no exame físico do paciente com FA?", "Plantão Médico Curso", "2:11",
             "Os achados de exame físico que sugerem fibrilação atrial."),
            ("PT", "9ABVkqpdwQ8", "Pausa compensatória", "Arritmia Na Prática", "6:04",
             "Como reconhecer a pausa compensatória da extrassístole (a “falha” que o paciente sente) e diferenciá-la de bloqueio AV."),
            ("EN", "EYZJXh9cups", "What is pulse deficit?", "Johnson's Cardiology", "1:48",
             "O que é déficit de pulso e por que ele aparece na fibrilação atrial."),
        ]),
        ("Visão geral e aulas completas", [
            ("PT", "2utpvJ6FCAM", "Semiologia cardiovascular", "Prática Enfermagem", "7:43",
             "Panorama curto da semiologia cardiovascular."),
            ("PT", "gJ_ugrpJGZU", "Semiologia cardiovascular", "MEDsimple", "34:11",
             "Aula de semiologia cardiovascular para a graduação."),
            ("PT", "BdFdGr77Es0", "Aula 02: semiologia cardiovascular", "Liga Acadêmica de Cardiologia de Paulo Afonso", "1:05:45",
             "Aula de semiologia dada por uma liga acadêmica de cardiologia."),
            ("PT", "5NTRLH2Rrvc", "Semiologia cardiovascular", "Fabricio Fortuna", "1:44:46",
             "Aula teórica completa de semiologia cardiocirculatória do curso de Medicina da Universidade de Caxias do Sul."),
            ("PT", "zW24HGh4yWU", "Semiologia cardiovascular: aula teórica, parte 1", "Semiologia Descomplicada", "1:49:29",
             "Aula teórica longa (parte 1) de semiologia cardiovascular."),
            ("EN", "XU_xeUMJ3Zc", "Cardiovascular Examination - OSCE Guide", "Geeky Medics", "8:05",
             "O exame cardiovascular inteiro em 8 minutos: mãos, pulsos, jugular, ictus, frêmitos, ausculta e manobras."),
            ("EN", "r9uo6Ljza6U", "The Cardiovascular Exam / Heart Sounds (Strong Exam)", "Strong Medicine", "48:36",
             "O exame cardiovascular essencial em profundidade: pulsos, edema, jugular, sopro carotídeo e ausculta."),
        ]),
    ],
    "t": [
        ("Inspeção e palpação do precórdio", [
            ("PT", "9d5xjYtgsu0", "Palpação do ictus cordis e focos da ausculta cardíaca", "Semiotécnica UEA", "2:52",
             "Como localizar o ictus e os focos de ausculta, com base no Porto."),
            ("PT", "4jpgwsRvQvI", "Inspeção do precórdio | Exame físico do aparelho cardiovascular 1/4", "PED+", "7:27",
             "Inspeção do precórdio e do ictus, sinal de Levine e posição de Blechmann."),
            ("PT", "qzVWmGd_WVY", "Semiologia 16: exame do aparelho cardiovascular, parte 1/2", "Medicina Resumida", "15:17",
             "Exame periférico (pulso, jugular, edema) e inspeção e palpação do precórdio."),
            ("PT", "2NtkWjUHR1E", "Semiologia cardiovascular: inspeção e palpação", "PET Medicina UFC - Sobral", "15:28",
             "Demonstração da primeira parte do exame físico cardiovascular."),
            ("EN", "jhUgnuVe_jU", "Precordial Movements: The Double Impulse", "Stanford Medicine 25", "1:55",
             "Paciente real: como palpar o ictus e reconhecer um impulso duplo."),
        ]),
        ("Bulhas: B1, B2, desdobramentos, B3 e B4", [
            ("PT", "zQtwZ4iyfgM", "Ausculta cardíaca normal: aprenda em 5 minutos", "MedTV - DrJulioMassao", "5:32",
             "B1, B2 e desdobramento em 5 minutos."),
            ("PT", "e_PUxfy61qY", "Ausculta do coração: bulhas cardíacas B3 e B4", "Semiologia Simples", "6:34",
             "B3 e B4 com os sons, para treinar o ouvido."),
            ("PT", "R8URksXmmUw", "Ausculta cardíaca anormal: B3, B4 e ritmos de galope", "MedTV - DrJulioMassao", "6:39",
             "B3, B4 e ritmos de galope em aula curta."),
            ("PT", "hAGcp57aGr0", "Semiologia médica: ausculta cardíaca (com sons)", "Enfermagem Total", "11:52",
             "Revisão da ausculta cardíaca com os sons."),
            ("PT", "Rg4whidnau0", "Ausculta do coração: bulhas cardíacas B1 e B2", "Semiologia Simples", "15:02",
             "B1 e B2 a fundo, com os sons."),
            ("PT", "NWmnE41Od6E", "Semiologia 17: exame do aparelho cardiovascular, parte 2/2", "Medicina Resumida", "17:20",
             "A ausculta cardíaca, continuação da parte 1."),
            ("EN", "cE8X1nwZWC4", "Heart Sounds", "Strong Medicine", "31:28",
             "Bulhas normais e anormais com muitos exemplos de áudio: intensidade de B1, desdobramentos de B2, B3, B4 e cliques."),
        ]),
        ("Sopros", [
            ("PT", "KOm8e4rAaC4", "Ausculta cardíaca na estenose e insuficiência valvares", "MedTV - DrJulioMassao", "6:55",
             "Ausculta das estenoses e das insuficiências valvares em aula curta."),
            ("PT", "4e0TQJMO7EY", "Sopro cardíaco: conheça os seus diferentes tipos", "Afya Cardiopapers", "13:58",
             "Sopro sistólico × diastólico e sopro inocente × patológico."),
            ("PT", "BIQ3wq6SI_I", "Ausculta cardíaca (parte 2): sopros cardíacos", "Precisa Desenhar?", "31:52",
             "Graus dos sopros e as quatro valvopatias clássicas: IM, EAo, IAo e EM."),
            ("PT", "3nvjiRkzK8M", "Semiologia cardíaca | Super Revisão de Cardiologia", "Estratégia MED", "42:22",
             "Revisão de focos, bulhas, desdobramentos, sopros e manobras (Valsalva) com foco em prova."),
            ("PT", "cwJfvMEJjy0", "Sopros cardíacos na ausculta do coração", "Semiologia Simples", "43:35",
             "Sopros sistólicos e diastólicos como porta de entrada para as valvopatias."),
            ("EN", "Q5-0mSydRR4", "Heart murmur sounds (cardiac auscultation sounds)", "Geeky Medics", "2:03",
             "O sopro típico de cada foco em 2 minutos, com as manobras que o acentuam."),
            ("EN", "9u0bhcYYd-8", "Approach to the Exam of Diastolic Murmurs (Real Patient and Sounds!)", "Stanford Medicine 25", "4:28",
             "Como procurar sopros diastólicos, com paciente e sons reais."),
            ("EN", "Cb-EXdLlGGs", "Approach to the Exam for Aortic Regurgitation (Real Patient and Sounds!)", "Stanford Medicine 25", "8:55",
             "Insuficiência aórtica em paciente real: sopro, sopro de Austin Flint e pulso em martelo d’água."),
            ("EN", "wYZbMoWjLEg", "Heart Murmurs and Heart Sounds: Visual Explanation for Students", "Zero To Finals", "19:10",
             "Bulhas e sopros com animações: EM, IM, EAo e IAo."),
            ("EN", "teJcTTVZnzs", "Heart Murmurs | Locations, Maneuvers, Buzzwords", "Dirty Medicine", "22:17",
             "Local, manobras e palavras-chave de prova de cada sopro, incluindo o prolapso mitral."),
            ("EN", "lFcf5a6BZGw", "Heart Murmurs", "Strong Medicine", "36:39",
             "Como caracterizar um sopro (tempo, forma, timbre, intensidade e manobras), com casos."),
            ("EN", "9DzhhagWeNc", "Heart Sounds & Murmurs | Clinical Medicine", "Ninja Nerd", "43:59",
             "Aula completa: B1 a B4, os quatro desdobramentos de B2, sopros sistólicos, diastólicos e contínuos, manobras."),
        ]),
        ("Estalidos e pericardite", [
            ("PT", "Rb6QzBpv3fU", "O que procurar no exame físico da pericardite aguda?", "Afya Cardiopapers", "3:01",
             "Os achados de exame físico na pericardite aguda."),
            ("PT", "ZK05CU3Layo", "Estalido diastólico", "videoaulasuff", "4:36",
             "Aula curta sobre o estalido diastólico."),
        ]),
    ],
    "u": [
        ("Pulso arterial", [
            ("PT", "mf3M2ZVnCEI", "Análise de pulso arterial, parte 1 | Semiologia do Zero", "Estratégia MED", "2:46",
             "Início direto da análise do pulso arterial."),
            ("PT", "agIi_n5mxUM", "Exame das pulsações arteriais", "Semiotécnica UEA", "9:08",
             "Onde palpar cada pulso (radial, carotídeo, femoral, poplíteo, tibial posterior, pedioso) e a manobra de Allen."),
            ("PT", "_CXH5NXMIMU", "Semiologia do pulso arterial", "Dr. Wagner Pádua", "11:34",
             "Os principais tópicos da semiologia do pulso arterial para estudantes de Medicina."),
            ("EN", "jTsjCZ9QxW8", "Pulsus Paradoxus Video", "Stanford Medicine 25", "2:59",
             "Como medir o pulso paradoxal na suspeita de tamponamento cardíaco."),
            ("EN", "o8VdWslTWfk", "Alternans, Anacrotic, parvus, tardus, dicrotic & normal Pulse", "USMLE exam gym", "4:10",
             "Pulso alternante, anacrótico, parvus et tardus e dicrótico em 4 minutos."),
            ("EN", "1kfg1mYRJ-g", "Peripheral Vascular Examination - OSCE Guide", "Geeky Medics", "7:05",
             "Exame vascular periférico: pulsos dos membros, carotídeo e aórtico."),
            ("EN", "nhAz84srBvg", "Clinical Skills: Pulses assessment", "Osmosis from Elsevier", "8:29",
             "Como palpar os pulsos radial, apical e femoral."),
            ("EN", "zDPw13FMEBs", "Types of arterial pulses", "Medic Notes", "8:31",
             "Pulso anacrótico, bigeminado, dicrótico, alternante, bisferiens e parvus et tardus, com o mecanismo."),
        ]),
        ("Pulso venoso jugular", [
            ("PT", "O-KfgwnJqZo", "Exame cardiovascular (pulso venoso) | Semiologia do Zero", "Estratégia MED", "8:08",
             "O pulso venoso no exame cardiovascular, do zero."),
            ("PT", "yVMjAe_7LRI", "Ondas de pulso venoso anormais", "RABISCANDO", "9:47",
             "Descensos X e Y alterados, onda A gigante e onda A em canhão."),
            ("PT", "bQ66G-1uOG0", "Inspeção das veias do pescoço III: a onda do pulso venoso jugular", "RABISCANDO", "11:04",
             "O que é a onda do pulso jugular e como diferenciá-la do pulso carotídeo."),
            ("EN", "NU0-uD4REek", "Examination of the Jugular Venous Pressure (JVP)", "Dr James Gill", "2:36",
             "Demonstração rápida do exame da pressão venosa jugular."),
            ("EN", "Z4yRBhlK0uY", "Understanding Jugular Venous Pressure (JVP)", "Zero To Finals", "11:25",
             "O que a jugular mostra do coração direito e o significado de cada onda."),
        ]),
        ("Pressão arterial e sons de Korotkoff", [
            ("PT", "DzlXZrXgeJA", "Pressão arterial e sons de Korotkoff", "MedTV - DrJulioMassao", "4:30",
             "Os sons de Korotkoff para ouvir. Use fone de ouvido."),
            ("PT", "0KQw7IQoZjk", "Fases de Korotkoff (hiato auscultatório)", "PRAXYS", "6:40",
             "As fases de Korotkoff e o hiato auscultatório."),
            ("PT", "lP0_6xRYfuA", "Como medir a pressão", "Professor Emerson Marques", "7:32",
             "Medida da PA com esfigmomanômetro, passo a passo."),
            ("PT", "JYcU8Uz65T8", "Como medir a pressão arterial? Aprenda a aferir da forma certa", "Descomplica Enfermagem", "8:18",
             "A técnica correta de aferição na prática."),
            ("PT", "yNyXdjNl0JY", "Método palpatório para verificar a pressão arterial", "Prática Enfermagem", "8:59",
             "Método palpatório, sons de Korotkoff e o erro mais comum ao aferir a sistólica."),
            ("EN", "UGOoeqSo_ws", "Blood Pressure Measurement: How to Check Blood Pressure Manually", "RegisteredNurseRN", "5:17",
             "Medida manual da PA passo a passo, com a estimativa da sistólica antes de auscultar."),
        ]),
    ],
}

# Aulas longas que cobrem S, T e U ficam no tema S; T e U apontam para elas.
AULAS_COMPLETAS = ("s", "Visão geral e aulas completas")

BARALHO_SONS = "anki/LIMAC-Sons-cardiacos.apkg"

# Bibliotecas gratuitas de sons cardíacos (tema T): nome, instituição, link, o que tem
BIBLIOTECAS = [
    ("Physical Diagnosis: heart sounds", "Universidade de Washington",
     "https://depts.washington.edu/physdx/heart/demo.html",
     "bulhas normais, estenose aórtica (pico precoce e pico tardio), insuficiência mitral, estenose pulmonar, "
     "insuficiência aórtica, estenose mitral, sopro inocente, CIA, CIV, PCA, desdobramento de B2, B3, B4 e "
     "atrito pericárdico (de 2 e de 3 componentes), em 16 gravações curtas. Em inglês."),
    ("Easy Auscultation", "MedEdu",
     "https://www.easyauscultation.com/heart-sounds",
     "aulas curtas com sons reais e simulados de bulhas, desdobramentos de B2 (fisiológico, persistente e fixo), "
     "estalido de abertura, B3, B4 e galopes, sopros sistólicos e diastólicos, pericardite aguda e cardiopatias "
     "congênitas, mais testes e treino por repetição. Quase todo o conteúdo é gratuito. Em inglês."),
]

# Linha final da seção de vídeos, dizendo onde ouvir os sons de cada tema
OUVIR = {
    "s": "Para ouvir as arritmias (fibrilação atrial, taquicardias, bradicardia do atleta), use o "
         "[baralho de sons](../../{baralho}).",
    "t": "Para treinar o ouvido, veja a seção [Sons cardíacos](#sons-cardíacos) logo abaixo.",
    "u": "Os sons de Korotkoff estão no vídeo da MedTV acima. O sopro carotídeo está no "
         "[baralho de sons](../../{baralho}).",
}
