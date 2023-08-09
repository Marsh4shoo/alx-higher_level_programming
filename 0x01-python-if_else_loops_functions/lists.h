#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Singly linked list
 * @n: integer
 * @next: point The next node
 *
 * Description: Singly linked list Node structure
 *
 */
typedef struct listint_ss
{
	int n;
	struct listint_ss *next;
} listint_tt;

size_t print_listint(const listint_tt *h);
listint_tt *add_nodeint_end(listint_tt **head, const int n);
void free_listint(listint_tt *head);
listint_t *insert_node(listint_tt **head, int number);

#endif /* LISTS_H */

