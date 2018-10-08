class Solution:
    def pick(self, arr, l, h, turn, alex, lee, tbl):
        #turn = 0 , alex, turn=1 lee
        if l > h :
            return alex>lee
        if l==h:
            if turn == 0:
                return alex+arr[h]> lee
            else:
                return  alex > lee + arr[h]

        if (tbl[l][h]!=-1):
            return tbl[l][h]

        if turn == 0 :
            tbl[l][h]= self.pick(arr,l+1,h, 1, alex+arr[l], lee, tbl) or self.pick(arr,l,h-1, 1, alex + arr[h], lee, tbl)
        else:
            tbl[l][h] = self.pick(arr, l + 1, h, 0, alex, lee + arr[l], tbl) or self.pick(arr, l, h - 1, 0,
                                                                                          alex, lee + arr[h], tbl)

        return tbl[l][h]


    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        tbl = [[-1 for i in range(len(piles))] for i in range(len(piles))]
        self.pick(piles, 0, len(piles)-1, 0, 0,0, tbl)
        return tbl[0][len(arr)-1]



if __name__ == '__main__':
    arr =[5, 3, 4, 5]
    s = Solution()
    print(s.stoneGame(arr))
