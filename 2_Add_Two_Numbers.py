class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def extract_values(node):
            values = []
            while node:
                values.append(node.val)
                node = node.next
            return values
        
        values_l1 = extract_values(l1)
        values_l2 = extract_values(l2)
        
        int_l1 = int(''.join(map(str, values_l1[::-1])))
        int_l2 = int(''.join(map(str, values_l2[::-1])))
        
        main_num = int_l1 + int_l2
        
        result_list = list(map(int, str(main_num)))
        result_list.reverse()
        
        result = ListNode(result_list[0])
        current = result
        for digit in result_list[1:]:
            current.next = ListNode(digit)
            current = current.next
        
        return result
