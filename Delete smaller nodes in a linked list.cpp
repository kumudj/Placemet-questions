/******************************************************************************

Delete smaller nodes in a linked list

Problem statement

There is a singly linked list represented by the following structure:

struct node

{

int data;

struct node* next;

};

Implement the following function:

struct node* Deletenodes ( struct node* head);

The function accepts a pointer to the start of the linked list, ‘ head ’ as its argument. Delete all such nodes from the input list whose adjacent node on the right side has greater value and return the modified linked list.

Note

·        Return null if the list is empty ( Incase of python if the list is none return none).

·        Do not create a new linked list, just modify the input linked list and return it.

Example

Input

6-> 2 -> 5 -> 4 -> 9 -> 7 -> 2 -> 1 -> 5 -> 9

Output

6 -> 5 -> 9 -> 7 -> 2 -> 9

Explanation

Node ‘2’ is deleted as ‘2’ < ‘5’ then ‘4’ is deleted as ‘4’ < ‘9’ then ‘1’ is deleted as ‘1’ < ‘5’ then ‘5’ is deleted as ‘5’ < ‘9’.

*******************************************************************************/

#include<bits/stdc++.h>
using namespace std ;
struct Node
{
    int data ;
    struct Node *next = NULL ;
}*head = NULL, *tail = NULL, *temp ;
void create(int n)
{
    struct Node *new_node = (struct Node*)malloc(sizeof(struct Node)) ;
    new_node ->data = n ;
    if(head == NULL) head = new_node ;
    else tail->next = new_node ;
    tail = new_node ;
}
struct Node* DeleteNodes(struct Node *head) 
{ 
    while(head->data < head->next->data) 
    { 
        temp = head ; 
        head = head->next ; 
        free(temp) ; 
    } 
    struct Node *prev , *temp1 ; 
    prev = head ; temp = head->next ;   
    int flag ; 
    while(temp != NULL) 
    { 
        flag = 1 ; 
        if((temp->next != NULL)&&(temp->data < temp->next->data)) 
        { 
            temp1 = temp ; 
            prev->next = temp->next ; temp = temp -> next ; 
            free(temp1) ; 
            flag = 0 ; 
        } 
        if(flag == 1) 
        { 
            prev = prev->next ; 
            temp = temp->next ; 
        } 
    } 
    return head ; 
} 
void display()
{
    temp = head ;
    while(temp -> next)
    {
        cout << temp -> data << " -> " ;
        temp = temp->next ;
    }
    cout << temp -> data ;
}
int main()
{
    int n ;
    while(true)
    {
        cin >> n ;
        if(n<1) break ;
        create(n) ;
    }
    head = DeleteNodes(head) ;
    display() ;
    return 0 ; 
}