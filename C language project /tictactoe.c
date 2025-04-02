#include <stdio.h>
#include <string.h>

char board[3][3];

int check_winner() {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return board[i][0];
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return board[0][i];
    }

    // Check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return board[0][2];

    return 'D'; // Draw
}

int main() {
    printf("Enter the Tic-Tac-Toe board (3x3) with X or O:\n");
    
    for (int i = 0; i < 3; i++)
        scanf(" %c %c %c", &board[i][0], &board[i][1], &board[i][2]);

    char winner = check_winner();
    
    if (winner == 'X')
        printf("X is the winner\n");
    else if (winner == 'O')
        printf("O is the winner\n");
    else
        printf("Draw\n");

    return 0;
}
