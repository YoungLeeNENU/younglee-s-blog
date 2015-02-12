#include <stdio.h>
#include <string.h>

#define FLAG  int
#define FLASE 0
#define TRUE 1

FLAG Get_Line(char *prompt, char *buffer, int len)
{
    /* char *cptr = buffer; *\/ */
    /* int key; */

    /* if (len < 2) */
    /*     return FALSE; */
    /* printf("%s ", prompt); */
    /* for (;;) { */
    /*     key = KeyGet(); */
    /*     if (isprint(key)) */
    /*     { */
            
    /*     } */
    /* } */
    printf("%s ", prompt);
    printf("%s", buffer);
    
    return TRUE;
}

int main(int argc, char *argv[])
{
    char buf[1024];
    
    Get_Line(">", gets(buf), 3);
    
    return 0;
}
