class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        extra = 0
        output_arr = []

        def len_link(listNode):
            temp = listNode.head
            count = 0
            while temp:
                count += 1
                temp = temp.next
            return count

        len_l1 = len_link(l1)
        len_l2 = len_link(l2)



        return output_arr


print(Solution.addTwoNumbers(Solution, [2, 4, 3], [5, 6, 4, 7]))
print(Solution.addTwoNumbers(Solution, [5, 4, 1], [2, 3, 2]))
print(145 + 232)
