class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        if len(flowerbed) < n:
            return False

        if l == 1 and flowerbed[0] == 0:
            return True

        if l == 2 and n == 1 and (l[0] == 0 and l[1] == 0):
            return True

        if l == 2 and n == 1 and (l[0] == 1 or l[1] == 1):
            return False

        placed = 0

        for i in range(l):
            if flowerbed[i] == 0:
                if i == 0:
                    if i + 1 < l and flowerbed[i + 1] != 1 :
                        flowerbed[i] = 1
                        placed += 1

                elif i == l - 1:
                    if i - 1 >= 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        placed += 1
                elif (((i - 1 >= 0) and (i + 1 < l)) and ((flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0)) is True):
                        flowerbed[i] = 1
                        placed += 1

            if placed >= n:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    # print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    # print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(s.canPlaceFlowers([0,0,1,0,1],1))