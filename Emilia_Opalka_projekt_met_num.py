import numpy as np
import matplotlib.pyplot as plt

def Opalka_Emilia_MNK(x, y, n):
    #sprawdzenie liczby punktów - czy w ogóle da się utworzyć dany wielomian
    if len(x) < n + 1:
        raise ValueError("Za mało punktów danych, aby utworzyć wielomian tego stopnia.")
    # zamiana x i y na tablice numpy
    x = np.array(x)
    y = np.array(y)  
    m = len(x) # liczba elementów tablicy x
    
    # utworzenie macierzy A i wektora b jako list
    A = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    b = [0 for _ in range(n + 1)]
    
    # wypełnianie macierzy A i wektora b
    for i in range(n + 1):
        for j in range(n + 1):
            A[i][j] = sum(x[k]**(i + j) for k in range(m))  #suma dla x^(i+j) (k iteruje po wszystkich danych pkt.)
        b[i] = sum(y[k] * (x[k]**i) for k in range(m))  #suma po y*x^i
    
    # rozkład Choleskyego macierzy A=L*L^T
    L = [[0 for _ in range(n + 1)] for _ in range(n + 1)] #macierz dolnotrójkątna L
    for i in range(n + 1):
        for j in range(i + 1):
            if i == j: #obliczanie wartosci elementow L na diagonali
                L[i][j] = (A[i][i] - sum(L[i][k]**2 for k in range(j)))**0.5
            else: #pozostałych (poniżej diagonali)
                L[i][j] = (A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]
    
    # rozwiązanie układu trójkątnego L*z=b
    # obliczamy tutaj z
    z = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        z[i] = (b[i] - sum(L[i][k] * z[k] for k in range(i))) / L[i][i]
    
    # rozwiązanie układu trójkątnego L^T*a=z
    # a-wspolczynniki wielomianu aproksymacyjnego (obliczamy je tu)
    a = [0 for _ in range(n + 1)]
    for i in range(n, -1, -1):
        a[i] = (z[i] - sum(L[k][i] * a[k] for k in range(i + 1, n + 1))) / L[i][i]
    
    # generowanie punktów do wykresu aproksymacji
    punkty_x = np.linspace(min(x), max(x), 500)  # generowanie pkt x potrzebnych do obliczenia wart. wielomianu
    punkty_y = sum(a[i] * punkty_x**i for i in range(n + 1))  # obliczenie wart y dla kazdego pkt x zgodnie z wialomianem
    
    # rysowanie wykresu
    plt.plot(punkty_x, punkty_y, label=f'Aproksymacja - wielomian stopnia {n}', color='red')
    plt.scatter(x, y, color='black', label='Punkty (x,y)')    
    plt.title('Aproksymacja średniokwadratowa - MNK')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()
    # zwracanie wspolczynnikow wielomianu zaokraglonych do 4 mjsc po przecinku    
    return [round(float(coeff), 4) for coeff in a]

# przykład użycia
x = [21,27,29,31,37,40,45]
y = [14,19,25,27,29,31,34]
n = 2  # stopień wielomianu

x1 = [21,27,29,31,37,40,45]
y1 = [14,19,25,27,29,31,34]
n1 = 3 

x2 = [21,27,29,31,37,40,45]
y2 = [14,19,25,27,29,31,34]
n2 = 5

wynik = Opalka_Emilia_MNK(x, y, n)
wynik1 = Opalka_Emilia_MNK(x1, y1, n1)
wynik2 = Opalka_Emilia_MNK(x2, y2, n2)

print(f"Współczynniki wielomianu stopnia {n} to:", wynik)
print(f"Współczynniki wielomianu stopnia {n1} to:", wynik1)
print(f"Współczynniki wielomianu stopnia {n2} to:", wynik2)

"""WNIOSKI:
1.Wraz z wzrostem stopnia wielomianu, rośnie jego dokładność dopasowania do danych punktów.
Dane są lepiej odwzorowane, mimo, że mają charakter nieliniowy.
2.Przy wysokich stopniach wielomianu wielomian może dokładnie przechodzić przez wszystkie
punkty,ale mogą wystąpić duże oscylacje pomiędzy nimi, co znaczy, że
model jest niestabilny - występuje efekt Rungego. Znaczy to, że wielomiany niższego
stopnia lepiej odwzorowywują zależność, mimo, że nie przechodzą przez wszystkie punkty.
"""



