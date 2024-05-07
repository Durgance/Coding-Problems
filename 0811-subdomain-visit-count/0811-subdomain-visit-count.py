class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for domains in cpdomains:
            count, domain = domains.split(" ")
            domain = domain.split(".")
            count = int(count)
            s = ""
            for i in range(1,len(domain)+1):
                s = "." + domain[-i] + s
                if not d.get(s[1:]):
                    d[s[1:]] = 0
                d[s[1:]] += count
                
                # print(d)
            
        ans = []
        for key, value in d.items():
            ans.append(f"{value} {key}")
        return ans