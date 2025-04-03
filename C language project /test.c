#include <stdio.h>

int main() {
  int num, digit, even=0,odd=0;

  scanf("%d", &num);

  

  if (num == 0) {
    printf("0\n");
  } else {
    while (num != 0) {
      digit = num % 10;
      if (digit % 2 ==0)
      {
         even = even+digit;
      }
      else
      {
         odd =odd+digit;
      }
      
      
      num /= 10;
    }
  }
  printf("Sum even: %d\n",odd);
  printf("Sum odd: %d\n",even);
  return 0;
}