from collections import Counter
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        c = Counter(tasks)
        d = dict(c)
        tot = sum(d.values())
        l = [ (-v,v,k) for k,v in d.items() ]
        heapq.heapify(l)
        temp = []
        tmr = n
        tm = 0
        ageCtr = {}
        poped = False
        while(tot>0):
            tm+=1
            poped = False
            if len(l)>0:
                a,b,c = heapq.heappop(l)
                print("Poped " + c)
                tot -= 1
                if b-1>0:
                    temp.append((-1*(b-1),b-1,c))
                    poped = True


            elif len(l)==0:
                print("Idle")

            for k,v in ageCtr.items():
                ageCtr[k]= ageCtr[k]+1
                if ageCtr[k]>=n:
                    i=0
                    while i < len(temp):
                        if k == temp[i][2]:
                            heapq.heappush(l, (temp[i][0],temp[i][1], temp[i][2]))
                            del temp[i]
                        else:
                            i+=1
                    del ageCtr[k]

            if poped == True:
                ageCtr[c]=0


        return tm




if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A","A","A","B","B","B"],2))
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
