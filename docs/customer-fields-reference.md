# Customer fields reference

The following fields are available when creating or editing a customer.

| Field | Description | Required |
| --- | --- | --- |
| Customer name | The organisation or customer name. | Yes |
| Primary email | Main contact email address. | Yes |
| Account owner | User responsible for the customer. | No |
| Status | Current customer status. | Yes |
| Telephone | Primary contact telephone number. | No |
| Notes | Additional information about the customer. | No |

## Customer statuses

| Status | Description |
| --- | --- |
| Prospect | Potential customer that has not yet purchased. |
| Active | Current customer with an active account. |
| On hold | Account temporarily suspended. |
| Closed | Customer account is no longer active. |

!!! warning
    Changing a customer to **Closed** may prevent users from creating new activity against the account.

!!! note
    Status names may be configured differently by your organisation.
