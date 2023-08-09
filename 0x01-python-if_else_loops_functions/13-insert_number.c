#include "lists.h"

/**
 * insert_node - Insert A nmber into A sorted singly-linked list.
 * @head: Pointer The Head Of The linked lists.
 * @number: Nmber To Insert.
 *
 * Return: If Function Fails - NULL.
 * Otherwise - Pointer To The New node.
 */
listint_tt *insert_node(listint_tt **head, int numbers)
{
	listint_tt *node = *head, *new;

	new = malloc(sizeof(listint_tt));
	if (new == NULL)
		return (NULL);
	new->n = numbers;

	if (node == NULL || node->n >= numbers)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < numbers)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
