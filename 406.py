class Solution:
    def reconstructQueue(self, people):
        if len(people) == 0 or len(people) == 1:
            return people

        people.sort(key=lambda x: (x[1], x[0]))

        print(people)

        result = []
        for h, k in people:
            pos = 0
            if k == 0:
                result.append([h, k])
                continue
            else:
                insert_pos = 0
                rank = 0
                for i in range(len(result)):
                    if result[i][0] > h:
                        rank += 1
                    if rank > k:
                        insert_pos = i
                        break
                    else:
                        insert_pos = len(result)
                result.insert(insert_pos, [h, k])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))