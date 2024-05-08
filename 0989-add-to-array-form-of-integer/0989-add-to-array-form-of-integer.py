class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(1000000000)
        temp = int("".join(list(map(str,num))))
        temp = str(temp + k)
        return list(map(int,temp))
        