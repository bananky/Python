<h1> Dokumentacja gry w statki </h1>
<h3> Paulina Wojnarska</h3>

<h3><u> Zasady gry </u> </h3>

Planszą jest kwadrat postaci 10 x 10 kratek.

Na planszy zostało ukrytych 5 statków o różnych długościach:
- Carrier o długości 5 kratek (jeden taki statek na planszy),
- Battleship o długości 4 kratek (jeden taki statek na planszy),
- Cruiser o długości 3 kratek (dwa takie statki na planszy),
- Destroyer o długości 2 kratek (jeden taki statek na planszy).

Statki mogą być ułożone pionowo jak i poziomo, ale nie mogą do siebie przylegać. 

Aby sprawdzić, czy w konkretnej kratce znajduje się statek, wystarczy najechać kursorem na kratkę i kliknąć. Jeśli kratka jest pusta,
zostanie wyświetlony komunikat "PUDŁO", a kratka zmieni kolor na niebieski. Jeśli udało nam się trafić, kratka zmieni kolor na
czerowny, a komunikat o treści "TRAFIONY" zostanie wyświetlony. Gdy uda nam się trafić wszystkie kratki składające się na jeden statek,
zostanie wyświetlony kominikat "TRAFIONY-ZATOPIONY".

Na każdym etepie pozostała liczba statków do zatopienia jest wyświetlana.

Naszym celem jest znalezienie wszystkich statków.

<h3> <u> Realizacja </u> </h3>

Program wykonany przy użyciu pakietu Tkinter. 

Każda kratka jest przyciskiem. 

Komputer losowo ustawia statki na planszy. 

<h3> <u> Utworzone funkcje:  </u> </h3>

- timeConvert(sec) - funkcja jako argument przyjmuje czas rozgrywki w sekundach i konwertuje go do
postaci w minutach i sekundach, która jest następnie wyświetlana użytkownikowi jako komunikat.

- clickGrid (event) - funkcja obsługuje kliknięcie - rozpoznaje klikniętą kratkę i zapisuje ją jako klikniętą (zabezpiecza to
przed wielokrotnym kliknięciem tego samego pola).

- initGrid() - funkcja ustawiająca całą planszę jako pustą, jest to wykorzystywane przy rozpoczęciu rozgrywki. 

- placeShipHorizontally(row, col, length, grid, symbol) - funkcja sprawdza czy statek może być położony w wylosowanym miejscu,
a następnie ustawia go w pozycji poziomej, jednocześnie zaznacza wszystkie pola naokoło jako niedostępne dla innych statków. 

- placeShipVertically(row, col, length, grid, symbol) - funkcja sprawdza czy statek może być położony w wylosowanym miejscu,
a następnie ustawia go w pozycji pionowej, jednocześnie zaznacza wszystkie pola naokoło jako niedostępne dla innych statków.

- randomShipLocation(length, grid, symbol) - funkcja losująca kratkę początkową oraz położenie statku. 

- randomGridShips() - funkcja ostatecznie ustawiająca i zapisująca położenie statku do shipDictionary. 

- resetLabel() - funkcja resetująca wyświetlany użytkownikowi komunikat z powrotem na "Strzelaj!". 

- winner() - funkcja obsługująca wyświetlanie odpowiednich komunikatów  w sytacji, gdy użytkownik zakończył rozgrywkę.

- fire() - funkkcja obsługująca strzelanie. Sprawdza, czy w danej kratce był statek i jeśli tak to zmniejsza liczbę pozostałych
kratek w danym statku. W sytuacji, gdy statek został trafiony i zatopiony, wyświetla odpowiedni komunikat. Zmienia kolor kratki 
na niebieski - w przypadku pudła oraz na czerwony w przypadku trafienia.

- game() - funkcja rozpoczynająca rozgrywkę. 


