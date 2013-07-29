#Author Wen Shen
import zenogenerator
import search_engine
import search
import sys



if __name__ == "__main__":
    if len(sys.argv)!=6:
        print "Command Line Error!\n"
        print "Usage: python genstat.py -domain <domain.pddl> -problems <#problem1> <#problems>"
        sys.exit()
    domain_name = sys.argv[2]
    problems_num1= int(sys.argv[4])
    problems_num = int(sys.argv[5])
    stat_bfs= "IDS_Statistics.txt"
    file1 = open(stat_bfs, "w")
    file1.write("Statistics for Iterative Deepening Search Algorithm\n")
    file1.write("City\t\tTime\t\tSpace\n")
    stat_astar= "ASTAR_Statistics.txt"
    file2 = open(stat_astar, "w")
    file2.write("Statistics for Astar Search Algorithm\n")
    file2.write("City\t\tTime\t\tSpace\n")
    for i in range(problems_num1, problems_num):
        print i+1
        domain_file = domain_name
        problem_file = "problem"+str(i+1)+".pddl"
        task= search_engine.loadIntoProblem(domain_file,problem_file)
        result = None
        search.astar_count=0
        search.astar_num=0
        search.ids_count=0
        search.ids_num=1
        
        result = search_engine.iterative_deepening_search(task)
        file1.write(str(search_engine.city_for_count)+"\t\t"+str(search.ids_count)+"\t\t"+str(search.ids_num)+"\n")

        search.ids_count = 0
        search.ids_num = 1
        result = search_engine.astar_search(task)
        file2.write(str(search_engine.city_for_count)+"\t\t"+str(search.astar_count)+"\t\t"+str(search.astar_num)+"\n")

        search.astar_count=0
        search.astar_num=0
    file1.close()
    file2.close()
            
