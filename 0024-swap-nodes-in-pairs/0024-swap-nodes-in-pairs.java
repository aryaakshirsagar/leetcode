class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node to simplify swapping at the head
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        // Loop through the list in pairs
        while (head != null && head.next != null) {
            ListNode first = head;
            ListNode second = head.next;

            // Swapping nodes
            prev.next = second;
            first.next = second.next;
            second.next = first;

            // Move pointers forward
            prev = first;
            head = first.next;
        }

        return dummy.next;
    }
}
