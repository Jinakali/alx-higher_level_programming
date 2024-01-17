#include "lists.h"
#include <stdlib.h>
/**
 *insert_node- inserts a number into a sorted singly linked list
 *@head: address of first node of list
 *@number: data to insert
 *Return: the address of the new node, or NULL if it failed
 *
 * Description: compare data in each node with number before
 * add new node before value greater than number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	if (number <= current->n)
	{
		new->next = current;
		*head = new;
		return (*head);
	}

	while (current->next != NULL)
	{
		if (number >= current->n && number <= current->next->n)
		{
			temp = current->next;
			current->next = new;
			new->next = temp;
			return (*head);
		}
		current = current->next;
	}
	current->next = new;
	return (*head);
}
