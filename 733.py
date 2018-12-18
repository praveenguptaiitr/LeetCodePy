class Solution(object):

    def dfs(self, image,visited ,sr, sc, newColor, oldCol):
        if sr<0 or sr> len(image)-1:
            return
        if sc<0 or sc> len(image[0])-1:
            return

        if visited[sr][sc]==1:
            return
        visited[sr][sc]=1
        if image[sr][sc]==oldCol:
            image[sr][sc]=newColor
            self.dfs(image,visited ,sr+1, sc, newColor, oldCol)
            self.dfs(image, visited, sr - 1, sc, newColor, oldCol)
            self.dfs(image, visited, sr, sc+1, newColor,oldCol)
            self.dfs(image, visited, sr, sc-1, newColor,oldCol)

        return

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        r = len(image)
        c = len(image[0])

        visited = [[0]*c for r1 in range(r)]
        oldCol = image[sr][sc]
        self.dfs(image,visited,sr,sc,newColor, oldCol)
        return image



if __name__=="__main__":
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))
