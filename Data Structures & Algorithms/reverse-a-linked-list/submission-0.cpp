/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
//null-1-2-3
// 1-null -
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
       ListNode* prev = nullptr;
       ListNode* cur = head;

       while (cur != nullptr) {
        ListNode* temp = cur-> next; //1. save original next
        cur->next = prev; // 2. reverse the pointer
        prev = cur; // more prev forward where cur is
        cur = temp; // move cur forwrad
       }
       return prev;
    }
};
