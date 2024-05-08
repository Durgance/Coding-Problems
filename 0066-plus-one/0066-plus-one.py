class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sys.set_int_max_str_digits(1000000000)
        temp = int("".join(list(map(str,digits))))
        temp = str(temp + 1)
        return list(map(int,temp))
        