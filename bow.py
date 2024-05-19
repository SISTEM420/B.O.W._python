# Bag of words v.03-052024
# Created by Rojas Lisandro & Jorge Arturo


from scipy import spatial
import string

def count_words_in_text(text):
    # Variables
    biggest_cosine_value = 0
    similaritie_values = []
    cosine_diff = spatial.distance.cosine
    word_count = {}
    word_number = []

    # Text type values (the ammount of times that every word appears on each text)
    science_values = [0.01316, 0.01316, 0.01316, 0.0, 0.01316, 0.05263, 0.02632, 0.0, 0.01316, 0.01316, 0.02632, 
                      0.01316, 0.0, 0.01316, 0.0, 0.01316, 0.01316, 0.0, 0.0, 0.01316, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    history_values = [0.0, 0.01299, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02597, 0.01299, 0.01299, 0.05195, 0.01299, 0.0, 0.01299, 
                      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01299, 0.01299, 0.0, 0.0, 0.0, 0.01299, 0.0, 0.01299, 0.01299, 0.01299]

    ambience_values = [0.01266, 0.0, 0.0, 0.01266, 0.0, 0.0, 0.0, 0.0, 0.01266, 0.02532, 0.01266, 0.0, 0.0, 0.02532, 0.02532, 
                       0.01266, 0.01266, 0.0, 0.01266, 0.01266, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01266]

    # Key words (THE BAG)
    word_tuple = ('Investigación', 'Desarrollo', 'Datos', 'Importante', 'Avances', 'Tecnología',
                  'Futuro', 'Historia', 'Mundo', 'Cambio', 'Sociedad', 'Humanidad', 'Descubrimiento',
                  'Impacto', 'Ambiente', 'Ciencia', 'Reto', 'Solución', 'Necesidad', 'Visión', 'Antigüedad',
                  'Civilización', 'Revolución', 'Imperio', 'Conquista', 'Renacimiento', 'Edad Media',
                  'Colonialismo', 'Independencia', 'Evolución')

    # Initialize counts for each word in the tuple to 0
    for word in word_tuple:
        word_count[word.lower()] = 0

    # Delete de comas and points
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words_in_text = text.lower().split()

    # Count occurrences of each word in the text
    for word in words_in_text:
        if word in word_count:
            word_count[word] += 1

    # Calculate the cosine difference with every reference text and the text used
    for word in word_count:
        word_number.append(float(word_count[word]))

    for i in range(len(word_number)):
        word_number[i] = round(float(word_number[i] / len(words_in_text)), 5)

    similarities = {"ciencia": 1 - cosine_diff(word_number, science_values),
                    "historia": 1 - cosine_diff(word_number, history_values),
                    "ambiente": 1 - cosine_diff(word_number, ambience_values)}

    text_to_compare = list(similarities.keys())
    cosine_compare_value = list(similarities.values())

    # Determine wich topyc is the most similar to the text used
    for i in range(3):
        similaritie_values.append(f"similitud con {text_to_compare[i]} : {cosine_compare_value[i]}: ")
        if cosine_compare_value[i] > biggest_cosine_value:
            biggest_cosine_value = cosine_compare_value[i]
            text_type = text_to_compare[i]

    return word_count, word_number, text_type, similaritie_values


# Save the data on a .txt
def save_word_count_to_file(word_count, text, filename, text_type, similaritie_values):
    with open(filename, 'w') as file:
        file.write("Texto original:\n")
        file.write(text + "\n\n")
        file.write(f"El texto es de: {text_type}\n\n")
        file.write("Los valores de similitud del texto son: \n")
        for text in similaritie_values:
            file.write(f"{text}\n")
        file.write("\nCantidad de palabras:\n")
        # Sort word count dictionary by count values
        sorted_word_count = sorted(
            word_count.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_word_count:
            file.write(f"{word}: {count}\n")


command = input(
    "Ingrese 0, 1 o 2 si quiere utilizar uno de los textos desconocidos texto, o 3 si quiere ingresar su propio texto: ")

if (command == "0"):
    text = """En la antigüedad la humanidad ha atravesado diferentes etapas de evolución y desarrollo 
    La historia es el registro de esos cambios marcados por descubrimientos importantes y revoluciones 
    que han tenido un impacto duradero en la sociedad y el mundo Desde el Renacimiento 
    hasta la Edad Media cada época ha dejado su huella en la civilización reflejando la 
    necesidad constante de adaptación y cambio La investigación histórica nos permite 
    comprender nuestro pasado y vislumbrar el futuro donde la visión de una sociedad más 
    justa y equitativa sigue siendo un reto
    """

elif (command == "1"):
    text = '''La ciencia es el motor que impulsa el avance de la humanidad hacia 
    un futuro lleno de posibilidades A través de la investigación y el desarrollo tecnológico hemos 
    logrado importantes avances que han transformado nuestro mundo Desde la conquista del espacio hasta
    el estudio del impacto humano en el medio ambiente la ciencia nos proporciona las soluciones necesarias para enfrentar
    los retos del siglo XXI Con una visión centrada en la innovación y el progreso la ciencia nos guía hacia un futuro donde 
    la tecnología y el conocimiento son herramientas clave para mejorar la calidad de vida de la sociedad 
    '''
elif (command == "2"):
    text = """En la sociedad actual el cambio es una constante que impulsa la evolución de nuestras 
    comunidades La independencia y la igualdad son valores importantes que han guiado nuestra 
    historia marcando el camino hacia una sociedad más justa y equitativa Sin embargo aún enfrentamos 
    retos significativos como la necesidad de proteger nuestro ambiente y promover el desarrollo sostenible 
    Con una visión orientada hacia el futuro podemos encontrar soluciones innovadoras que nos permitan 
    construir un mundo mejor para las generaciones venideras
    """

else:
    text = input(
        "Ingrese el texto del que quiere contar las palabras (sin puntos ni comas): ")

word_count, numbers, text_type, similaritie_values = count_words_in_text(text)

command = input("Ingrese el nombre del archivo .txt donde quiere guardar: ")

save_word_count_to_file(word_count, text, command+'.txt', text_type, similaritie_values)
