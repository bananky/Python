############################
# autor: Paulina Wojnarska #
# GRA W STATKI             #
############################
import tkinter as tk
import random
import time

tableHeight = 10  # wysokosc
tableWidth = 10  # szerokosc
cellSize = 60  # rozmiar kratki (guzika)

board = [[0 for row in range(tableHeight)] for col in range(tableWidth)]
messages = ["STRZELAJ!", "PUDŁO!", "TRAFIONY!", "TRAFIONY - ZATOPIONY!", "WSZYSTKO ZATOPIONE!"]
shipNames = ["Carrier", "Battleship", "Cruiser", "Destroyer"]
symbol = ["C", "B", "Cr", "D"]
lengthOfShips = [5, 4, 3, 2]
numberOfShips = [1, 1, 2, 1]

ships = [[name, len, number, symb] for name, len, number, symb in zip(shipNames, lengthOfShips, numberOfShips, symbol)]
print(list(ships))

def timeConvert(sec):
    """Funkcja przyjmuje jako argument obliczony czas rozgrywki w sekundach i zamienia
    je na czas w minutach i sekundach, który jest wyświatlany przy zakończeniu rozgrywki. """
    mins = int(sec // 60)
    sec = int(sec % 60)
    lbl2.configure(text="Gra ukończona w czasie = " + str(mins) + " min i " + str(sec) + " sek!")

def clickGrid(event):
    """Funkcja obsługująca lokalizację kratki, którą klikamy oraz dodająca tą kratkę
    do listy ruchów już wykonanych. """
    global case
    case = canvas2.find_closest(event.x, event.y)[0]
    if case not in playedList:
        playedList.append(case)
        print(playedList)
        root.after(500, fire)

def initGrid():
    """Funkcja ustawiająca wszystkie kratki na planszy jako puste. """
    global tableWidth, tableHeight
    grid = [['Empty' for i in range(tableWidth)] for j in range(tableHeight)]
    return grid

def placeShipHorizontally(row, col, length, grid, symbol):
    """Funkcja służąca do ustawiania statków w pozycji poziomej oraz pilnująca, aby
    kratki naokoło statku były ustawione jako niedostępne dla innych statków. """
    isAvailable = True
    if col + length > 10:
        isAvailable = False
    else:
        for count in range(length):
            if grid[row][col + count] != "Empty":
                isAvailable = False
    if isAvailable:
        for count in range(length):
            grid[row][col + count] = symbol
            if row != 0 and row != 9:
                grid[row - 1][col + count] = 'Unavailable'
                grid[row + 1][col + count] = 'Unavailable'
            elif row == 0:
                grid[row + 1][col + count] = 'Unavailable'
            else:
                grid[row - 1][col + count] = 'Unavailable'

            if col != 0:
                if row == 0:
                    grid[row][col - 1] = 'Unavailable'
                    grid[row + 1][col - 1] = 'Unavailable'
                elif row == 9:
                    grid[row][col - 1] = 'Unavailable'
                    grid[row - 1][col - 1] = 'Unavailable'
                else:
                    grid[row][col - 1] = 'Unavailable'
                    grid[row - 1][col - 1] = 'Unavailable'
                    grid[row + 1][col - 1] = 'Unavailable'

            if count == length - 1:
                if col + count != 9:
                    if row == 0:
                        grid[row][col + length] = 'Unavailable'
                        grid[row + 1][col + length] = 'Unavailable'
                    elif row == 9:
                        grid[row][col + length] = 'Unavailable'
                        grid[row - 1][col + length] = 'Unavailable'
                    else:
                        grid[row][col + length] = 'Unavailable'
                        grid[row - 1][col + length] = 'Unavailable'
                        grid[row + 1][col + length] = 'Unavailable'

    return isAvailable

def placeShipVertically(row, col, length, grid, symbol):
    """ Funkcja służąca do ustawiania statków w pozycji pionowej oraz pilnująca, aby
    kratki naokoło statku były ustawione jako niedostępne dla innych statków. """
    isAvailable = True
    if row + length > 10:
        isAvailable = False
    else:
        for count in range(length):
            if grid[row + count][col] != "Empty":
                isAvailable = False
    if isAvailable:
        for count in range(length):
            grid[row + count][col] = symbol
            if col != 0 and col != 9:
                grid[row + count][col - 1] = 'Unavailable'
                grid[row + count][col + 1] = 'Unavailable'
            elif col == 0:
                grid[row + count][col + 1] = 'Unavailable'
            else:
                grid[row + count][col - 1] = 'Unavailable'
            if row != 0:
                if col == 0:
                    grid[row - 1][col + 1] = 'Unavailable'
                    grid[row - 1][col] = 'Unavailable'
                elif col == 9:
                    grid[row - 1][col - 1] = 'Unavailable'
                    grid[row - 1][col] = 'Unavailable'
                else:
                    grid[row - 1][col + 1] = 'Unavailable'
                    grid[row - 1][col - 1] = 'Unavailable'
                    grid[row - 1][col] = 'Unavailable'
            if count == length - 1:
                if row + count != 9:
                    if col == 0:
                        grid[row + length][col] = 'Unavailable'
                        grid[row + length][col + 1] = 'Unavailable'
                    elif col == 9:
                        grid[row + length][col] = 'Unavailable'
                        grid[row + length][col - 1] = 'Unavailable'
                    else:
                        grid[row + length][col] = 'Unavailable'
                        grid[row + length][col - 1] = 'Unavailable'
                        grid[row + length][col + 1] = 'Unavailable'

    return isAvailable

def randomShipLocation(length, grid, symbol):
    """Funkcja losująca w jakiej pozycji i miejscu zostanie położony statek. """
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    choosePosition = random.randint(0, 1)
    if choosePosition == 0:
        isAvailable = placeShipHorizontally(row, col, length, grid, symbol)
    else:
        isAvailable = placeShipVertically(row, col, length, grid, symbol)
    return isAvailable

def randomGridShips():
    """Funkcja ustawiająca i zapisująca położenie statków. """
    global ships, grid
    grid = initGrid()
    shipDictionary = {}
    for ship in ships:
        for nb in range(ship[2]):
            isAvailable = False
            while not isAvailable:
                isAvailable = randomShipLocation(ship[1], grid, ship[3] + str(nb))
            shipDictionary[ship[3] + str(nb)] = ship[1]
    return shipDictionary

def resetLabel():
    """Funkcja resetująca wyświetlany użytkownikowi komunikat."""
    global lbl
    lbl.configure(text=messages[0])

def winner():
    """Funkcja wyświetlająca wyniki użytkownika, używana po zakończeniu rozgrywki. """
    global endTime
    endTime = time.time()
    timeLapsed = endTime - startTime
    timeConvert(timeLapsed)
    lbl.configure(text=messages[4])

def fire():
    """Funkcja obsługująca strzelanie, sprawdza czy trafiona kratka zawiera statek,
    jeśli tak - oznacza statek jako trafiony. Zmienia kolor kratki w zależności od jej
    zawartości, niebieski - pudło, czerwony - trafiony. """
    global shipDictionary, remainingShips, lbl, frame, grid
    row = (case - 1) // 10
    col = (case - 1) % 10
    status = grid[col][row]
    if status == 'Empty' or status == 'Unavailable':
        lbl.configure(text=messages[1])
        colour = 'blue'
    else:
        shipDictionary[status] -= 1
        print(shipDictionary)
        if shipDictionary[status] > 0:
            lbl.configure(text=messages[2])
        else:
            lbl.configure(text=messages[3])
            remainingShips -= 1
            lbl2.configure(text='Zostało staków : ' + str(remainingShips))
        colour = "red"
    canvas2.itemconfig(board[col][row], fill=colour)
    if remainingShips == 0:
        root.after(500, winner)
    else:
        root.after(500, resetLabel)

def game():
    """ Funkcja uruchamiająca rozgrywkę. """
    global shipDictionary, playedList, startTime, remainingShips, lbl2
    for y in range(tableHeight):
        for x in range(tableWidth):
            canvas2.itemconfig(board[x][y], fill='white')
    resetLabel()
    remainingShips = sum(numberOfShips)
    lbl2.configure(text='Zostało staków : ' + str(remainingShips))
    playedList = [0]
    shipDictionary = randomGridShips()
    startTime = time.time()

############################################################################

root = tk.Tk()
root.title('Gra w statki')
# Wyświetlanie zakładki "Gra"
top = tk.Menu(root)
root.config(menu=top)
gameMenu = tk.Menu(top, tearoff=False)
helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Gra', menu=gameMenu)
gameMenu.add_command(label='Nowa gra', command=game)
gameMenu.add_command(label='Zamknij', command=root.destroy)


frame = tk.Frame(root)
frame.pack(side=tk.TOP)
lbl = tk.Label(frame, text=messages[0], font='Arial 18')
lbl.pack(side=tk.TOP)
frame2 = tk.Frame(root)
frame2.pack()
canvas2 = tk.Canvas(frame2, width=cellSize * tableWidth, height=cellSize * tableHeight, highlightthickness=0)
canvas2.pack()
for y in range(tableHeight):
    for x in range(tableWidth):
        board[x][y] = canvas2.create_rectangle((x * cellSize, y * cellSize, (x + 1) * cellSize, (y + 1) * cellSize), outline="gray",
                                               fill="white")

canvas2.bind("<Button-1>", clickGrid)
lbl2 = tk.Label(frame, text='', font='Arial 18')
lbl2.pack(side=tk.BOTTOM)

game()

root.mainloop()

