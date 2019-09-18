#include <stdio.h> 
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

// Beni Young Assignment 1 for CSCI 4404


int main() 
{
  int process, n;
  FILE *fp;
  int cldProcess[100];

  // Make sure to put limit on number entered!
  // Takes in a number from user from 1-5
  printf("Enter a number between 1 and 5: ");
  scanf("%d", &n);
  
  fp = fopen("simplegraph.dot", "w");
  // Fork for the number of times user input
  for( int i = 0; i  < n; i++) {
    pid = fork();

    // This is suppose to grab the init Process ID that starts the forks()
    // not sure if thats the case though
    // This is test printout to see what is going to be stored
    if(pid > 0 && i == 0){
      waitpid(pid);
      printf("Process ID: %d \n", getpid());
      break;
    }
    else if(pid > 0){
	waitpid(pid);
	break;	
    }
    // If Process is zero than its a Child process and can print its Parent fork process 
    else if(pid == 0) {
      printf("Process ID: %d Parent ID: %d \n", getpid(), getppid());
    }
    
  }

  // Writes to file process.txt in partial graphviz dot format
  // "Parent ID: [numbers]" -> "Process ID: [numbers]"
  fprintf(fp, "\"Parent ID: %d\" -> \"Process ID: %d\" \n", getppid(), getpid());
  
  sleep(1);

  // fprintf(fp, "done\n");
  fclose(fp);
  return 0;
  
} 
