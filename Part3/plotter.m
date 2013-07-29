file_read = fopen('ASTAR_Statistics.txt','r');

i =0;

a = 0;

while (i == 0)

file_line = fgetl(file_read);


if file_line != -1


if a >=2

space = findstr(file_line,"\t");
city_time = [str2num(file_line(1:space(1))) str2num(file_line(space(1)+2:space(3)))];
city_space = [str2num(file_line(1:space(1))) str2num(file_line(space(3)+2:length(file_line)))];

time(a-1,1) = city_time(1);
time(a-1,2) =  city_time(2);
mem(a-1,1)= city_space(1);
mem(a-1,2)= city_space(2);
endif

a = a +1;

else
i = 1;
endif

endwhile

plot(time)
plot(mem)
