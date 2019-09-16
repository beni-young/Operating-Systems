#include <stdio.h> 
#include <sys/types.h>
#include <unistd.h>


int main() 
{
  int process, n;
  FILE *fp;
  int cldProcess[100];

  // make sure to put limit on number entered!
  printf("Enter a number between 1 and 5: ");
  scanf("%d", &n);
  
  fp = fopen("process.txt", "w");
  // fprintf(fp, "digraph D {");
  
  for( int i = 0; i  < n; i++) {
    process = fork();

    if(process > 0 && i == 0){
      printf("Process ID: %d \n", getpid());
    }
    else if(process == 0) {
      printf("Process ID: %d Parent ID: %d \n", getpid(), getppid());
    }
    
  }

  
  fprintf(fp, "\"Parent ID: %d\" -> \"Process ID: %d\" \n", getppid(), getpid());
  
  sleep(1);

  // fprintf(fp, "done\n");
  fclose(fp);
  return 0;
  
} 
