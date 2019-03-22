class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()
        i=0
        j= len(people)-1
        count = 0
        while(people[j]>limit):
            j-=1
        while(people[j]==limit):
            count+=1
            j-=1
        while(i<=j):
            if people[i]+people[j]>limit:
                count+=1
                j-=1
            if people[i]+people[j]<=limit:
                count+=1
                i+=1
                j-=1
            if i==j:
                count+=1
                break
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numRescueBoats([7,8], 8))
    print(s.numRescueBoats([3,2,2,1], 3))
    print(s.numRescueBoats([3,5,3,4],5))