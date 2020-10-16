list=[];
def printCombination(arr, n, r): 

    data = [0]*r; 
 
    combinationUtil(arr, data, 0,  
                    n - 1, 0, r); 

def combinationUtil(arr, data, start,  
                    end, index, r): 
    list2=[];
    if (index == r): 
        for j in range(r): 
            list2.append(data[j]); 
        list.append(list2);
        return; 
 
    i = start;  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i]; 
        combinationUtil(arr, data, i + 1,  
                        end, index + 1, r); 
        i += 1; 
  
class geeks:  
    def __init__(self, name, roll,p):  
        self.name = name  
        self.roll = roll
        self.p = p
        
arr=[];
# appending instances to list  
arr.append( geeks('qdk', "keep",9))
arr.append( geeks('karthik', "keep",8.5))
arr.append( geeks('kishan', "keep",8.5))
arr.append( geeks('rohit', "bat",10.5))
arr.append( geeks('gil', "bat",9.5))
arr.append( geeks('morgan', "bat",9.5))
arr.append( geeks('rana', "bat",9))
arr.append( geeks('hardik', "bat",9))
arr.append( geeks('surykumar', "bat",9))
arr.append( geeks('tripathi', "bat",8.5))
arr.append( geeks('russell', "all",10))
arr.append( geeks('pollard', "all",9.5))
arr.append( geeks('narine', "all",9))
arr.append( geeks('pandya', "all",8.5))
arr.append( geeks('cummins', "bowl",9))
arr.append( geeks('bumrah', "bowl",9))
arr.append( geeks('yadav', "bowl",8.5))
arr.append( geeks('mavi', "bowl",8.5))
arr.append( geeks('boult', "bowl",8.5))
arr.append( geeks('pattin', "bowl",8.5))
arr.append( geeks('chakrawarti', "bowl",8))
arr.append( geeks('krishna', "bowl",8))
r = 11; 
n = len(arr); 
printCombination(arr, n, r); 
def checkBowl(list):
    flag=0;
    for x in list:
        if x.roll == "bowl":
            flag+=1;
    return flag;
def checkBat(list):
    flag=0;
    for x in list:
        if x.roll == "bat":
            flag+=1;
    return flag;
def checkKeep(list):
    flag=0;
    for x in list:
        if x.roll == "keep":
            flag+=1;
    return flag;
def checkAll(list):
    flag=0;
    for x in list:
        if x.roll == "all":
            flag+=1;
    return flag;
def checkSum(list):
    flag=0;
    for x in list:
        z=x.p;
        flag+=z;
    return flag;

def myFilter(list):
    flag=1;
    if(checkBowl(list)<3 or checkBowl(list)>6 ):
        flag=0;
        return flag;
    if(checkBat(list)<3 or checkBat(list)>6 ):
        flag=0;
        return flag;
    if(checkKeep(list)<1 or checkKeep(list)>4 ):
        flag=0;
        return flag; 
    if(checkAll(list)<1 or checkAll(list)>4 ):
        flag=0;
        return flag;
    if(checkSum(list)>100):
        flag=0;
        return flag;
    return flag;
validList=[];
for x in list:
    if myFilter(x):
        validList.append(x)
print(len(validList));
for x in validList:
    for y in x:
        print(y.name,y.roll);
    print(checkSum(x));
    print(" ")