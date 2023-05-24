class proteinAnalysis:
    def __init__(self, seq) -> None:
        self.seq = seq
        resList = list('ARNDCQEGHILKMFPSTWYV'+'OUBZJX')
        resList.sort()
        resDict = {}
        for i in resList:
            resDict.update({i: self.seq.upper().count(i)})
        maxOcc = max([resDict[x] for x in resDict])
        minOcc = min([resDict[x] for x in resDict if resDict[x] > 0])
        missingAA = []
        self.maxOccAA = []
        self.minOccAA = []
        for x in resDict:
            if resDict[x] == 0:
                missingAA.append(x)
            if resDict[x] == maxOcc:
                self.maxOccAA.append(x)
            if resDict[x] == minOcc:
                self.minOccAA.append(x)
        self.missAA = list("".join(missingAA).replace('B','').replace('J','').replace('O','').replace('U','').replace('X','').replace('Z',''))
        self.phoCount = 0
        for i in list('GAMLIVFWP'):
            for j in self.seq.upper():
                if i == j:
                    self.phoCount += 1
        self.phiCount = 0
        for i in list('RNDCQEHKSTY'):
            for j in self.seq.upper():
                if i == j:
                    self.phiCount += 1
        self.basicCount = 0
        for k in list('HRK'):
            for j in self.seq.upper():
                if k == j:
                    self.basicCount += 1
        self.acidicCount = 0
        for k in list('DE'):
            for j in self.seq.upper():
                if k == j:
                    self.acidicCount += 1
        self.modAAdict = {}
        self.modAAdictFreq = {}
        for i in list('OUBZJX'):
            couRec = 0
            for j in self.seq.upper():
                if i == j:
                    couRec += 1
            if couRec > 0:
                self.modAAdict.update({i: couRec})
                self.modAAdictFreq.update({i: couRec/len(self.seq)})
    def missingResidues(self) -> str: return f'{"; ".join(self.missAA)}'
    def mostOccuringResidues(self) -> str: return f'{"; ".join(self.maxOccAA)}'
    def lessOccuringResidues(self) -> str: return f'{"; ".join(self.minOccAA)}'
    def hydrophobicAACount(self) -> int: return self.phoCount
    def hydrophilicAACount(self) -> int: return self.phiCount
    def basicAACount(self) -> int: return self.basicCount
    def acidicAACount(self) -> int: return self.acidicCount
    def modifiedAACount(self) :
        if len(self.modAAdict) > 0: return self.modAAdict
        else : return 0
    def modifiedAAFrequency(self):
        if len(self.modAAdict) > 0: return self.modAAdictFreq
        else : return 0


if __name__ == "__main__":
    seq = 'GAoouuxxzzrneeee'
    obj = proteinAnalysis(seq)
    print(obj.missingResidues())
    print(obj.mostOccuringResidues())
    print(obj.lessOccuringResidues())
    print(obj.hydrophobicAACount())
    print(obj.hydrophilicAACount())
    print(obj.acidicAACount())
    print(obj.basicAACount())
    print(obj.modifiedAACount())
    print(obj.modifiedAAFrequency())