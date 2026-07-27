class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        curr = 1

        for n in nums:
            curr *= n
            prefix_product.append(curr)

        answer = []

        right_prefix = 1

        for iter in range(len(nums)-1,-1,-1):
            if iter-1 >= 0:
                to_append = prefix_product[iter-1] * right_prefix
            else:
                to_append = right_prefix

            answer.append(to_append)
            right_prefix *= nums[iter]

        return answer[::-1]
