#include <stdio.h>

int main(void)
{
	char filename[] = "./h.c";
	FILE *fp;
	int f_size;
	
	fp = fopen(filename,"r");
	fseek(fp,0,SEEK_END);
	f_size = ftell(fp);
	printf("%s 文件的大小是%d\r\n",filename,f_size);
	return 0;

}
