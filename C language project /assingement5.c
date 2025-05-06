#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct student {
    int id;
    char name[30];
    float percentage; // data
};
struct student {
    int id;
    char name[30];
    float percentage; // data
};

int main() {
    int i;
    system("clear"); // This will clear the terminal screen (works on Unix/Linux)
    
    struct student record[3]; // Array of 3 student structures

    // 1st student's record
    record[0].id = 1;
    strcpy(record[0].name, "raju");
    record[0].percentage = 86.5;

    // 2nd student's record
    record[1].id = 2;
    strcpy(record[1].name, "surender"); // Fixed: should be record[1] instead of record[2]
    record[1].percentage = 90.5;

    // 3rd student's record
    record[2].id = 3;
    strcpy(record[2].name, "thiyagu");
    record[2].percentage = 81.5;

    // Displaying the records
    for (i = 0; i < 3; i++) {
        printf("\nRecord of student %d:\n", i + 1);
        printf("Id: %d\n", record[i].id);
        printf("Name: %s\n", record[i].name);
        printf("Percentage: %.2f\n\n", record[i].percentage); // Changed to %.2f for better formatting
    }

    return 0; // Added return statement for main
}

int main() {
    int i;
    system("clear"); // This will clear the terminal screen (works on Unix/Linux)
    
    struct student record[3]; // Array of 3 student structures

    // 1st student's record
    record[0].id = 1;
    strcpy(record[0].name, "raju");
    record[0].percentage = 86.5;

    // 2nd student's record
    record[1].id = 2;
    strcpy(record[1].name, "surender"); // Fixed: should be record[1] instead of record[2]
    record[1].percentage = 90.5;

    // 3rd student's record
    record[2].id = 3;
    strcpy(record[2].name, "thiyagu");
    record[2].percentage = 81.5;

    // Displaying the records
    for (i = 0; i < 3; i++) {
        printf("\nRecord of student %d:\n", i + 1);
        printf("Id: %d\n", record[i].id);
        printf("Name: %s\n", record[i].name);
        printf("Percentage: %.2f\n\n", record[i].percentage); // Changed to %.2f for better formatting
    }

    return 0; // Added return statement for main
}