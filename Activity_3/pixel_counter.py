import time
import multiprocessing as mp
import os
import sys

import numpy as np

## Funció original inclosa a l'enunciat
def count_white_pixels(image: np.ndarray, threshold: int = 200) -> int:
    """
    Counts how many pixels in a grayscale image are greater than a 
    given threshold.

    Args:
        image (np.ndarray): Image represented as a 2D NumPy array.
        threshold (int): Threshold value used to determine whether 
        a pixel is considered white.

    Returns:
        int: Number of pixels greater than the threshold.
    """
    count = 0
    rows, cols = image.shape

    for i in range(rows):
        for j in range(cols):
            if image[i, j] > threshold:
                count += 1

    return count

def count_white_pixels_sequential(images: list) -> list:
    """
    Aplica la funció count_white_pixels de forma seqüencial a una llista d'imatges.

    Args:
        images: Llista d'arrays 2D de NumPy representant imatges en escala de grisos.

    Returns:
        Llista de nombres de píxels blancs per a cada imatge.
    """
    # Inicialitzem el comptador de temps
    start_time = time.perf_counter()

    # Aplica count_white_pixels a cada imatge de la llista de manera seqüencial
    results = [count_white_pixels(image) for image in images]

    # Finalitza el comptador de temps i imprimeix per pantalla
    total_time = time.perf_counter() - start_time
    print(f"Temps seqüencial: {total_time:.4f} segons")

    return results


def count_white_pixels_parallel(images: list) -> list:
    """
    Aplica la funció count_white_pixels en paral·lel utilitzant multiprocessing

    Args:
        images: Llista d'arrays 2D de NumPy representant imatges en escala de grisos

    Returns:
        Llista de nombres de píxels blancs per a cada imatge
    """
    # Inicialitzem el comptador de temps
    start_time = time.perf_counter()

    # Calculem el nombre de processos com el mínim entre el nombre d'imatges o el 
    # nombre de CPUs lògiques
    num_processes = min(len(images), os.cpu_count())

    # La paral·lelització depèn del sistema operatiu, per tant el detectem 
    # en el moment d'execuxió i assignem el context "fork" per Linux/MacOS
    # i "spawn" per a Windows
    # Fonts: https://docs.python.org/3/library/multiprocessing.html 
    # https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods 
    mp_context = "fork" if sys.platform != "win32" else "spawn"

    # Generem un objecte de context multiprocessing per crear els processos fills
    ctx = mp.get_context(mp_context)

    # Crea un pool de num_processes workers i distribueix les imatges entre
    # ells. pool.map aplica count_white_pixels a cada imatge en paral·lel
    # i retorna els resultats en el mateix ordre que l'entrada.
    with ctx.Pool(processes=num_processes) as pool:
        results = pool.map(count_white_pixels, images)

    # Finalitza el comptador de temps i imprimeix per pantalla
    total_time = time.perf_counter() - start_time
    print(f"Temps paral·lel: {total_time:.4f} segons")

    return results


if __name__ == "__main__":
    # Generem una llista de 4 imatges amb pixels aleatoris
    images = [
        np.random.randint(0, 256, (2000, 2000), dtype=np.uint8),
        np.random.randint(0, 256, (2500, 2500), dtype=np.uint8),
        np.random.randint(0, 256, (3000, 3000), dtype=np.uint8),
        np.random.randint(0, 256, (3500, 3500), dtype=np.uint8),
    ]

    results_seq = count_white_pixels_sequential(images)
    results_par = count_white_pixels_parallel(images)

    assert results_seq == results_par
    print("Les dues versions produeixen el mateix resultat.")
