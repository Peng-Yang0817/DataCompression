import json
import numpy as np
import math as dog

def findTheCharFrequency(text):
    result = dict()
    
    with open("santaclaus.txt",'r') as f:
        for line in f.readlines():
          line = line.lower()
          for i in line:
            if i.isalpha():     
              if i in result:
                result[i] += 1
              else:
                result.update({i:1})
            elif i.isspace():    
              if i in result:
                result[i] += 1
              else:
                result.update({i:1})    
    return result

def setAnswer3(result):
  aswer = {}
  totalQuantity = 0
  entropy = 0
  for line in result:
    totalQuantity += result[line]    
  for i in result:
    result.update({i:result[i]/totalQuantity})
  for j in result:
    entropy += result[j] * np.log2(1/result[j])
  aswer = entropy  
  return aswer


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):    
    def __init__(self, char_Weights):
        self.Leaf = [Node(k,v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))
    
    def Hu_generate(self, tree, length, data):
        node = tree
        dataAll = {}        
        if (not node):
            return
        elif node.name:          
            string = ""
            for i in range(length):              
              if node.name in data:
                string += str(self.Buffer[i])
                data2 = {node.name:string}
                #data.update(data2)                                                
              else:
                string += str(self.Buffer[i])
                data[node.name] = string
            data.update(data2)  #將每次算完的data推進名為data2的dict內            
            return                   
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1, data)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1, data)        

    def get_code(self, answer3):
        dataAll = {}
        data = {}
        self.Hu_generate(self.root, 0, data)
        dataAll["answer_3"] = answer3
        dataAll["answer_4"] = data        
        #print(dataAll)
        with open('ans.json', 'w') as fp:
            json.dump(dataAll, fp)


if __name__=='__main__':
    text = r'123.txt'
    result = findTheCharFrequency(text)
    answer3 = setAnswer3(result)
    #print(answer3)
    tree = HuffmanTree(result)
    tree.get_code(answer3)