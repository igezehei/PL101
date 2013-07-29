To run the ZenoGenerator, please use the following command line:
python zenogenerator.py -problem <#problem> -city <#max_city>

For example, to generate 5 problem pddl files, and the maximium 
number of the cities are 4, you should input:

python zenogenerator.py -problem 5 -city 4

---------------------------------------------------

To run the genstat, please use the following command line:
genstat.py -domain <domain.pddl> -problems <#problems>

For example, to generate the results of 5 problems, you should input:
python genstat.py -domain domain.pddl -problems 5
