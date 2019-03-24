class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        path = path.replace("//","/")
        path = path.replace("/./","/")

        l = path.split("/")
        s = []
        i=0
        for i in range(len(l)):

            e = l[i]
            if e =="" or e==".":
                continue
            if e == "..":
                if len(s)>0:
                    s.pop()
                else:
                    continue
            else:
                s.append(e)

        s= "/".join(s)
        return "/"+s


if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/a/../../b/../c//.//"))
    print(s.simplifyPath("/a//b////c/d//././/.."))