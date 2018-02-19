import sys
import numpy
import random
import PyPluMA

# Scaling is done to make median=1
class CSVScalePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1].strip())
               self.ADJ[i].append(value)#[j] = value
            i += 1
  
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)
      for i in range(self.m):
         vec = []     
         minimum = 10000
         for j in range(self.n):
            vec.append((float(self.ADJ[i][j]), j))
            if (self.ADJ[i][j] != 0 and self.ADJ[i][j] < minimum):
               minimum = self.ADJ[i][j]
         # Set zero elements to the minimum value in the vector
         # Note I can't call min, because that can return 0
         for j in range(self.n):
            if (vec[j][0] == 0):
               vec[j] = (minimum, vec[j][1])
         vec.sort()
         median = vec[self.n/2][0]
         if (median == 0):
            PyPluMA.log("WARNING: ZERO MEDIAN")
            PyPluMA.log("VEC: "+str(vec))
         for j in range(self.n):
            self.ADJ[i][vec[j][1]] = vec[j][0] * 1.0/median

      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



