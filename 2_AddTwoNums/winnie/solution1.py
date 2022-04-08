class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result_ls = []
        residual = 0

        if len(l1) > len(l2):
            lower_len = len(l2)
        else:
            lower_len = len(l1)

        for i in range(-1, -lower_len-1, -1):
            temp = l1[i] + l2[i] + residual
            result_ls.append(temp % 10)
            residual = temp // 10

        print(result_ls)


Solution.addTwoNumbers(Solution, [2, 4, 3], [5, 6, 4])
