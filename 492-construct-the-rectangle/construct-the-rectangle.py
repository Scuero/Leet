class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        pares = []
        for i in range(1, int(math.sqrt(area)+1)):
            if area%i == 0:
                pares.append((area//i,i))
        return pares[-1]