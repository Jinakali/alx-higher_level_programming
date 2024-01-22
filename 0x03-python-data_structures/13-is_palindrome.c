#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of first node
 *
 * Return: 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int equal = 0;
	listint_t *rev_head = NULL;
	listint_t *normal_head = *head;
	listint_t *current = *head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	if (*head == NULL)
		return (0);
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	rev_head = prev;

	while (rev_head != NULL && normal_head != NULL)
	{
		printf("%d\n", equal);
		if (rev_head->n == normal_head->n)
		{
			equal = 1;
			rev_head = rev_head->next;
			normal_head = normal_head->next;
		}
		else
		{
			equal = 0;
			break;
		}
	}
	if (equal)
		return (1);
	else
		return (0);

}
