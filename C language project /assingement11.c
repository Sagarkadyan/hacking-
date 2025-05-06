#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct stu {
    char name[100];
    int maths, phy, chem, rank;
    float cutoff;
};

int main() {
    struct stu s[100], temp;
    int i, j, n;

    printf("\n\nNo. of Students: ");
    scanf("%d", &n);
    getchar(); // consume newline after number input

    for (i = 0; i < n; i++) {
        printf("\nEnter Student %d Name: ", i + 1);
        fgets(s[i].name, sizeof(s[i].name), stdin);
        s[i].name[strcspn(s[i].name, "\n")] = 0;  // remove trailing newline

        printf("Maths Mark: ");
        scanf("%d", &s[i].maths);

        printf("Physics Mark: ");
        scanf("%d", &s[i].phy);

        printf("Chemistry Mark: ");
        scanf("%d", &s[i].chem);

        s[i].cutoff = (s[i].maths / 2.0) + (s[i].phy / 4.0) + (s[i].chem / 4.0);
        getchar(); // to consume newline after int
    }

    // Sort in descending order of cutoff
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (s[i].cutoff < s[j].cutoff) {
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }

    // Assign ranks
    for (i = 0; i < n; i++) {
        s[i].rank = i + 1;
    }

    printf("\n\n%-5s %-15s %-7s %-8s %-10s %-7s\n", "Rank", "Name", "Maths", "Physics", "Chemistry", "Cutoff");
    for (i = 0; i < n; i++) {
        printf("%-5d %-15s %-7d %-8d %-10d %-7.2f\n", s[i].rank, s[i].name, s[i].maths, s[i].phy, s[i].chem, s[i].cutoff);
    }

    return 0;
}
