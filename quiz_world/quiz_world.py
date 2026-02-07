import random
from pathlib import Path

capitals = {
    'afganistán': 'kabul', 'albania': 'tirana', 'alemania': 'berlín',
    'andorra': 'andorra la vieja', 'angola': 'luanda', 'antigua y barbuda': 'saint john\'s',
    'arabia saudita': 'riad', 'argelia': 'argel', 'argentina': 'buenos aires',
    'armenia': 'ereván', 'australia': 'canberra', 'austria': 'viena',
    'azerbaiyán': 'bakú', 'bahamas': 'nasáu', 'barbados': 'bridgetown',
    'baréin': 'manama', 'bélgica': 'bruselas', 'belice': 'belmopán',
    'benín': 'porto novo', 'bielorrusia': 'minsk', 'botsuana': 'gaborone',
    'brasil': 'brasilia', 'brunéi': 'bandar seri begawan', 'bulgaria': 'sofía',
    'burkina faso': 'uagadugú', 'burundi': 'gitega', 'bután': 'timbu',
    'cabo verde': 'praia', 'camboya': 'nom pen', 'camerún': 'yaundé',
    'canadá': 'ottawa', 'catar': 'doha', 'chad': 'yamena',
    'chile': 'santiago', 'china': 'pekin', 'chipre': 'nicosia',
    'colombia': 'bogotá', 'comoras': 'moroni', 'república del congo': 'brazzaville',
    'república democrática del congo': 'kinsasa', 'corea del norte': 'pionyang',
    'corea del sur': 'seúl', 'costa de marfil': 'yamusukro', 'costa rica': 'san josé',
    'croacia': 'zagreb', 'cuba': 'la habana', 'dinamarca': 'copenhague',
    'djibouti': 'djibouti', 'dominica': 'roseau', 'república dominicana': 'santo domingo',
    'ecuador': 'quito', 'egipto': 'el cairo', 'el salvador': 'san salvador',
    'emiratos árabes unidos': 'abu dabi', 'eritrea': 'asmara', 'eslovaquia': 'bratislava',
    'eslovenia': 'liubliana', 'españa': 'madrid', 'estonia': 'tallin',
    'etiopía': 'adís abeba', 'filipinas': 'manila', 'finlandia': 'helsinki',
    'francia': 'parís', 'gabón': 'libreville', 'gambia': 'banjul',
    'georgia': 'tiflis', 'ghaná': 'acra', 'grecia': 'atenas',
    'granada': 'saint georges', 'guatemala': 'ciudad de guatemala', 'guinea': 'conakri',
    'guinea-bisáu': 'bisáu', 'guinea ecuatorial': 'malabo', 'haití': 'puerto príncipe',
    'honduras': 'tegucigalpa', 'hungría': 'budapest', 'india': 'nueva delhi',
    'indonesia': 'yakarta', 'irán': 'teherán', 'iraq': 'bagdad',
    'irlanda': 'dublín', 'israel': 'jerusalén', 'italia': 'roma',
    'jamaica': 'kingston', 'japón': 'tokio', 'jordania': 'amman',
    'kazajistán': 'nur-sultán', 'kenia': 'nairobi', 'kiribati': 'tarawa',
    'kosovo': 'pristina', 'kuwait': 'ciudad de kuwait', 'kirguistán': 'bishkek',
    'laos': 'vientiane', 'letonia': 'riga', 'líbano': 'beirut',
    'lesoto': 'maseru', 'liberia': 'monrovia', 'libia': 'trípoli',
    'liechtenstein': 'vaduz', 'lituania': 'vilna', 'luxemburgo': 'luxemburgo',
    'madagascar': 'antananarivo', 'malasia': 'kuala lumpur', 'malaui': 'lilongüe',
    'maldivas': 'male', 'mali': 'bamako', 'malta': 'valletta',
    'marruecos': 'rabat', 'mauricio': 'port louis', 'mauritania': 'nouakchott',
    'méxico': 'ciudad de méxico', 'micronesia': 'palikir', 'moldavia': 'chisináu',
    'mónaco': 'mónaco', 'mongolia': 'ulán bator', 'montenegro': 'podgorica',
    'mozambique': 'maputo', 'myanmar': 'naypyidaw', 'namibia': 'windhoek',
    'nauru': 'yaren', 'nepal': 'katmandú', 'nicaragua': 'managua',
    'níger': 'niamey', 'nigeria': 'abuya', 'noruega': 'oslo',
    'nueva zelanda': 'wellington', 'omán': 'mascate', 'países bajos': 'amsterdam',
    'pakistán': 'islamabad', 'palaos': 'melekeok', 'panamá': 'ciudad de panamá',
    'papúa nueva guinea': 'port moresby', 'paraguay': 'asunción', 'perú': 'lima',
    'polonia': 'varsovia', 'portugal': 'lisboa', 'qatar': 'doha',
    'rumanía': 'bucarest', 'rusia': 'moscú', 'ruanda': 'kigali',
    'samoa': 'apia', 'san marino': 'san marino', 'santo tomé y príncipe': 'santo tomé',
    'serbia': 'belgrado', 'seychelles': 'victoria', 'sierra leona': 'freetown',
    'singapur': 'singapur', 'siría': 'damasco', 'sudáfrica': 'pretoria',
    'sudán': 'jartum', 'sudán del sur': 'yuba', 'suecia': 'estocolmo',
    'suiza': 'berna', 'tailandia': 'bangkok', 'tanzania': 'dodoma',
    'togo': 'lomé', 'tonga': 'nukualofa', 'túnez': 'túnez',
    'turquía': 'ankara', 'turkmenistán': 'ashgabat', 'tuvalu': 'funafuti',
    'ucrania': 'kiyv', 'uganda': 'kampala', 'emiratos árabes unidos': 'abu dabi',
    'reino unido': 'londres', 'estados unidos': 'washington d. c.',
    'uruguay': 'montevideo', 'uzbekistán': 'taskent', 'vanuatu': 'port vila',
    'vaticano': 'ciudad del vaticano', 'venezuela': 'caracas',
    'viet nam': 'hanói', 'yemen': 'saná', 'zambia': 'lusaka', 'zimbabue': 'harare'
}

#input user for output folder and number of quizzes
output_folder = input("Ingrese la ruta de la carpeta donde se guardarán los archivos del quiz: ")
number_of_quizzes = int(input("Ingrese el número de quizzes a generar: "))
number_of_questions = int(input("Ingrese la cantidad de preguntas por quiz: "))

#create output folder if it doesn't exist
output_folder_path = Path(output_folder)
output_folder_path.mkdir(parents=True, exist_ok=True)

if number_of_questions > len(capitals):
    raise ValueError(
        f"No se pueden generar {number_of_questions} preguntas. "
        f"Solo hay {len(capitals)} países disponibles."
    )

#generate quizzes
for quizNum in range(number_of_quizzes):

    # Abrir archivos de quiz y respuestas
    quiz_path = output_folder_path / f'capitalworld{quizNum + 1}.txt'
    answer_path = output_folder_path / f'capitalworld_answers{quizNum + 1}.txt'

    with open(quiz_path, 'w', encoding='utf-8') as quizFile, \
        open(answer_path, 'w', encoding='utf-8') as answerKeyFile:

        # Encabezado
        quizFile.write('Nombre:\nFecha:\n\nPeriodo:\n\n')
        quizFile.write((' ' * 20) + f'Quiz de Capitales del Mundo (Formulario {quizNum + 1})\n\n')

        # Mezclar países
        countries = list(capitals.keys())
        random.shuffle(countries)

        # Generar preguntas
        for questionNum in range(number_of_questions):

            correctAnswer = capitals[countries[questionNum]]

            wrongAnswers = list(set(capitals.values()) - {correctAnswer})
            wrongAnswers = random.sample(wrongAnswers, 3)

            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Escribir pregunta
            quizFile.write(f'{questionNum + 1}. ¿Cuál es la capital de {countries[questionNum]}?\n')
            for i in range(4):
                quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')

            # Escribir clave de respuestas
            answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")


print("✔️ Quizzes generados correctamente.")