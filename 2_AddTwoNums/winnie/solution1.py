class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        count = 0
        extra = 0
        output_arr = []

        def indexValidation(index, arr):
            try:
                return arr[index]
            except IndexError:
                return None

        while indexValidation(count, l1) and indexValidation(count, l2):
            unit_result = l1[count] + l2[count] + extra
            output_arr.append(unit_result % 10)
            extra = unit_result // 10
            count += 1

        while indexValidation(count, l1):
            unit_result = l1[count] + extra
            output_arr.append(unit_result % 10)
            extra = unit_result // 10
            count += 1

        while indexValidation(count, l2):
            unit_result = l2[count] + extra
            output_arr.append(unit_result % 10)
            extra = unit_result // 10
            count += 1

        return output_arr


print(Solution.addTwoNumbers(Solution, [2, 4, 3], [5, 6, 4,7]))
print(Solution.addTwoNumbers(Solution, [5, 4, 1], [2, 3, 2]))
print(145 + 232)
