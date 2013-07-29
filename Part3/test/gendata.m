function  result = gendata(file_name)
	file_read = fopen(file_name,'r');
	i =0;

	a = 0;

	while (i == 0)

		file_line = fgetl(file_read);

		if file_line != -1

			if a >=2
				space = findstr(file_line,"\t");
				initial_matrix = [str2num(file_line(1:space(1))) str2num(file_line(space(1)+2:space(3))) str2num(file_line(space(3)+2:length(file_line)))];
				city_space = [str2num(file_line(1:space(1))) str2num(file_line(space(3)+2:length(file_line)))];

				result(a-1,1) = initial_matrix(1);
				result(a-1,2) = initial_matrix(2);
				result(a-1,3) = initial_matrix(3);
			endif

				a = a +1;
			else
				i = 1;
		endif
	endwhile

endfunction


