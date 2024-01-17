#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle-checks if there is a cycle in the linked list
 * @list:list to be checked
 *
 * Return: 0 if acyclic, 1 otherwise
 * Description:
 * using the floyd algorithm
 * transverse the list 2 ways, one way must be TWICE as fast as the other
 * the starting point of the 2 ways must also be different
 */
int check_cycle(listint_t *list)
{
	listint_t *faster_transverse;
	listint_t *normal_transverse;

	if (list == NULL)
		return (0);

	faster_transverse = list->next;
	normal_transverse = list;

	while (faster_transverse != NULL && faster_transverse->next != NULL)
	{
		if (faster_transverse == normal_transverse)
			return (1);
		faster_transverse = faster_transverse->next->next;
		normal_transverse = normal_transverse->next;
	}
	return (0);
}
