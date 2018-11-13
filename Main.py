from random import randint
import random
class Chromosome:
    def __init__(self, fenotyp):
        self.fenotype = fenotyp
        self.gens = intToBin(fenotyp)
        self.adoption_value = self.adoption_function()
        self.percent_sector_start = 0
    def adoption_function(self):
        return 2 * (self.fenotype * self.fenotype + 1)
    def __str__(self):
        return str(self.gens) + "(" + str(self.fenotype) + ")" + " - " + str(self.adoption_value) + " - " + str(self.percent_sector_start) + "%"
def intToBin(x):
    return [int(x) for x in bin(x)[2:]]
def binToInt(bin):
    out = 0
    for bit in bin:
        out = (out << 1) | bit
    return out
def crossing(mom, dad):
    dad, mom = fillBinZeros(dad, mom)
    arrayLen = len(dad)
    locus = randint(0, arrayLen)
    for i in range(0, arrayLen):
        if(i >= locus):
            temp_dad = dad[i]
            dad[i] = mom[i]
            mom[i] = temp_dad
    return mom, dad
def mutating(gen):
    rand = randint(0, len(gen) - 1)
    if(gen[rand] == 0):
        gen[rand] = 1
    else:
        gen[rand] = 0
    return gen

def fillBinZeros(mom, dad):
    dad_ref = dad
    mom_ref = mom
    if (len(mom) != len(dad)):
        while (len(mom_ref) > len(dad_ref)):
            dad_ref = [0] + dad_ref
        while (len(dad_ref) > len(mom_ref)):
            mom_ref = [0] + mom_ref
    return mom_ref, dad_ref
def fillPercentPopulation(pop):
    sumOfVals = 0
    genSum = 0.0
    for gen in pop:
        sumOfVals = sumOfVals + gen.adoption_value
    for gen in pop:
        genSum = genSum + (gen.adoption_value / sumOfVals * 100.0)
        # print(genSum)
        gen.percent_sector_start = int(genSum)
def buildPupulation(n):
    population = []
    for i in range(0, n):
        population.append(Chromosome(randint(0, 127)))
    fillPercentPopulation(population)
    return population
def chooseBestChromosome(pop, randPerc):
    for gen in pop:
        if(gen.percent_sector_start > randPerc):
            return gen
def selection(pop):
    pop_temp = []
    for i in range(0, len(pop)):
        randPerc = randint(0, 100)
        pop_temp.append(chooseBestChromosome(pop, randPerc))
    return pop_temp
oneTrue = True
def conditionOfAdoption():
    return oneTrue
pop = buildPupulation(6)
# for gen in pop:
#     print(gen)
# randPerc = randint(0,100)
# print(randPerc)
# print((chooseBestChromosome(pop, randPerc)))

for gen in pop:
    print(gen)
print("population generated")

while conditionOfAdoption() == True:
    pop = selection(pop)
    for gen in pop:
        print(gen)
    print("population selected")
    pop2 = pop.copy()
    random.shuffle(pop2)
    for gen in pop2:
        print(gen)
    print("population 2 shuffled")
    for i in range(0, len(pop)):
        mom = pop[i]
        dad = pop2[i]
        print("mom " + str(mom))
        print("dad " + str(dad))
        mom_gens, dad_gens = crossing(mom.gens, dad.gens)
        mom.gens = mom_gens
        dad.gens = dad_gens
        print("crossed mom " + str(mom))
        print("crossed dad " + str(dad))
        mom_gens = mutating(mom.gens)
        dad_gens = mutating(dad.gens)
        mom.gens = mom_gens
        dad.gens = dad_gens
        print("mutated mom " + str(mom))
        print("mutated dad " + str(dad))
        pop[i] = mom
        pop2[i] = dad
    oneTrue = False
