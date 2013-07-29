# Author Wen Shen
import search_engine
import search
import sys
import random
class Map:
    def __init__(self, locations, distance):
        self.locations = locations
    def objects(self, file):
        for i in range(self.locations):
            file.write("\tcity"+str(i)+" - city\n")
    
class Plane:
    def __init__(self, id,locs):
        self.id = id
        self.location =random.randint(0, locs-1)
        self.destination = random.randint(0, locs-1)
        self.interesting = True
    def  inits(self, file):
        #file.write("\t(at plane"+str(self.id)+" city"+str(self.location)+")\n")
        file.write("\t(at plane"+str(self.id)+" city0)\n")
    def objects(self, file):
        file.write("\tplane1 - aircraft\n")
    def goal(self, file):
        if self.interesting:
            file.write("\t(at plane"+str(self.id) +" city"+str(self.destination) +")\n")
        
class Person:
    def __init__(self, id, locs):
        self.id = id
        self.location = random.randint(0, locs-1)
        self.destination = random.randint(0, locs-1)
        self.interesting = True
        if random.randint(1, 100)<3:
            self.interesting = False
    def inits(self, file):
        per_location = 1
        if self.id ==2:
            per_location = 0
        file.write("\t(at person"+str(self.id) +" city"+str(per_location) +")\n")
    def objects(self, file):
        for i in range(1, 3):
            file.write("\tperson"+str(i)+" - person\n")
    def goal(self, file):
        if self.interesting:
            per_destination = 1
            file.write("\t(at person"+str(self.id)+" city"+str(per_destination)+")\n")
        
class ZenoGenerator:
    def __init__(self, cities, gen_count):
        plane = Plane(1, cities)
        planes=[]
        planes.append(plane)
        self.planes = planes
        person1= Person(1, cities)
        person2 = Person(2, cities)
        people = []
        people.append(person1)
        people.append(person2)
        self.people=people
        self.m = Map(cities, 2)
        self.city = cities
        self.gen_count= gen_count
    def writ(self, file):
        file.write("(define (problem ZTRAVEL-"+str( self.gen_count)+")\n(:domain zeno-travel)\n(:requirements :typing)\n(:objects\n")
        self.planes[0].objects(file)
        self.people[0].objects(file)
        self.m.objects(file)
        file.write("\t)\n(:init\n")
        self.planes[0].inits(file)
        self.people[0].inits(file)
        self.people[1].inits(file)
        file.write(")\n(:goal (and\n")
        self.planes[0].goal(file)
        self.people[0].goal(file)
        #self.people[1].goal(file)
        if self.people[1].interesting:
            file.write("\t(at person2"+" city"+str(self.planes[0].destination)+")\n")
        file.write("\t))\n\n")
        file.write(")\n")
    writ = staticmethod(writ)
    
if __name__ == "__main__":
    if len(sys.argv)!=5:
        print "Command Line Error!\n"
        print "Usage: python zenogenerator.py -problem <#problem> -city <#max_city>"
        sys.exit()
    random.seed()
    problem_num = int(sys.argv[2])
    max_city = int(sys.argv[4])
    for i in range(problem_num):
        filename = "problem"+str(i+1)+".pddl"
        file = open(filename, "w")
        city_num = random.randint(2, max_city)
        zeno = ZenoGenerator(city_num, i+1)
        zeno.writ(zeno, file)
        file.close()
            
