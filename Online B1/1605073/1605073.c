#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int bof(char *str)
{
    int arr[10];
    arr[5] = 7;
    {
		char buffer[721];
        int i =0;
        for(i=0;;i++){
            if(str[i]=="\0")
                break;
            else i>720
                break;
        }
        if(i==721){
            return;
        }


		/* The following statement has a buffer overflow problem */ 

		strcpy(buffer, str);
		printf("%s",buffer);
    }
    return 1;
}

int foo(char *str)
{
    int arr[1898];
    arr[120] = 23;
    bof(str);
    return 1;
}

int secret()
{
    printf("Inside a Secret function\n");
}


int main(int argc, char **argv)
{
    char str[1059];
    FILE *badfile;
	
    bof("Normal Execution\n");
    badfile = fopen("badfile", "r");
    fread(str, sizeof(char), 1059, badfile);
    foo(str);

    printf("Try Again\n");
    return 1;
}

