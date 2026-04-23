class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = []
        suff_prod = []

        def get_prod(nums, prod=1):
            product = []
            prod = prod
            for x in nums:
                product.append(prod)
                prod *= x
            return product
        
        pref_prod = get_prod(nums, 1)
        suff_prod = get_prod(reversed(nums), 1)
        suff_prod[:] = suff_prod[::-1]
        # print(pref_prod)
        # print(suff_prod)
        prod_except_self = []
        for i in range(len(nums)):
            prod_except_self.append(pref_prod[i] * suff_prod[i])
        return prod_except_self

        