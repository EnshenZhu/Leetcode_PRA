from LinkList import LinkedList, ListNode


def build_linked_list(arr):
    ll = LinkedList()
    for num in arr:
        ll.append(num)
    return ll


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head

        # determine the middle point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare first half with reversed second half
        left, right = head, prev
        while right:  # Only need to check the second half
            if left.value != right.value:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 3, 2, 1]
    arr3 = [1, 2, 3, 4, 3, 2, 1]

    sample = build_linked_list(arr1)

    solution = Solution()
    result = solution.isPalindrome(sample.head)
    print(f"Is palindrome: {result}")
