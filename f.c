#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define FIFOPATH "./test1.fifo"

int main(void)
{
	char w_buf[64];
	char r_buf[64];
	
	int ret,fd;
	ret = mkfifo(FIFOPATH,0666);
	if(ret == -1)
	{
		perror("mkfifo failed\r\n");
		return -2;
	}
	else
	{
		printf("creat a new fifo:%s\r\n",FIFOPATH);
	}
	
	fd = open(FIFOPATH,O_RDWR);
	
	strcpy(w_buf,"hello name pipe\r\n");
	write(fd,w_buf,sizeof(w_buf));
	read(fd,r_buf,sizeof(r_buf));
	printf("r_buf:%s\r\n",r_buf);
	
	close(fd);
	remove(FIFOPATH);
}
