'''
Assignment: Tic Tac Toe
Author: José David Vega Varela
'''

def main():
    print("Welcome to Tic Tac Toe!\nFirst player marks with 'x' and second player with 'o'")
    matrix = build_matrix()
    start_game(matrix)

#Function to build the 3*3 matrix to start the game
def build_matrix():
    matrix = []
    row = []
    for i in range(1, 10):
        if i % 3 != 0:
            row.append(i)
        else:
            row.append(i)
            matrix.append(row)
            row = []
    return matrix

#Function to apply the user's selection to the matrix
def update_matrix(number, matrix, player):
    updated = False
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == number:
                matrix[i][j] = player
                updated = True
                break
    if updated == False:
        return False        
    print_matrix(matrix)
    return matrix

#Function to print the matrix in 3 rows and 3 columns
def print_matrix(matrix):
    element_1 = ''
    element_2 = ''
    element_3 = ''
    divider_counter = 1
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if element_1 == '':
                element_1 = matrix[i][j]
            elif element_2 == '':
                element_2 = matrix[i][j]
            else:
                element_3 = matrix[i][j]
        if divider_counter <3:
            print(f"{element_1}|{element_2}|{element_3}")
            print("-+-+-")
            element_1 = ''
            element_2 = ''
            element_3 = ''
            divider_counter += 1
        else:
            print(f"{element_1}|{element_2}|{element_3}\n")
    return

#Function to ask the players for the numbers.
def start_game(matrix):
    turns = 9
    player = 'x'
    choice = 0
    print_matrix(matrix)
    while turns > 0:
        choice = int(input(f"{player}'s turn to choose a square (1-9): "))
        #Validate the number chosen
        if choice < 1 and choice > 9:
            print("The number must be between 1 and 9")
        else:
            if update_matrix(choice, matrix, player) == False:
                print("The number has already been chosen by the other player")
            else:
                if turns < 6:
                    if verify_victory(matrix, player) == True:
                        print(f"Congratulations! Player '{player}' is the winner!")
                        return
                    elif player == 'x':
                        player = 'o'
                    else:
                        player = 'x'
                else:
                    if player == 'x':
                        player = 'o'
                    else:
                        player = 'x'
                turns -= 1
        
    print("It is a tie!")
    return

#Function to verify if a player has won
def verify_victory(matrix, player):
    spots_matrix = build_matrix()
    spots = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == player:
                spots.append(spots_matrix[i][j])
    for i in range(0, len(matrix)):
        if match(spots_matrix[i], spots):
            return True
    if match([1, 4, 7], spots) or match([2, 5, 8], spots) or match([3, 6, 9], spots) or match([1, 5, 9], spots) or match([3, 5, 7], spots):
        return True
    else:
        return False

#Function to verify if the choices the player made match any winning play
def match(list_a, list_b):
    correct = False
    for i in list_a:
        if i in list_b:
            correct = True
        else:
            return False
    return correct

if __name__ == "__main__":
    main()