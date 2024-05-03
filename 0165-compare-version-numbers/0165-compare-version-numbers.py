class Solution:
    def checkVer(self, ver1,ver2):
        for i in range(len(ver1)):
            if i>=len(ver2):
                if ver1[i] > 0:
                    return 1
                continue
            if ver1[i]>ver2[i]:
                return 1
            elif ver1[i]<ver2[i]:
                return -1
        return 0


    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int,version1.split(".")))
        ver2 = list(map(int,version2.split(".")))
        if ver1[0]>ver2[0]:
            return 1
        elif ver1[0]<ver2[0]:
            return -1
        if len(ver1)>= len(ver2):
            return self.checkVer(ver1,ver2)
        else:
            return -1*self.checkVer(ver2,ver1)

        