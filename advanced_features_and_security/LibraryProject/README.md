## Django Permissions and Groups Setup

### Custom Permissions:
- `can_view`: Permission to view an article.
- `can_create`: Permission to create an article.
- `can_edit`: Permission to edit an article.
- `can_delete`: Permission to delete an article.

### User Groups:
- **Editors**: Can create and edit articles.
- **Viewers**: Can only view articles.
- **Admins**: Full access to all permissions.

### How to Assign Permissions:
1. Create the appropriate groups (`Editors`, `Viewers`, `Admins`) in the Django admin.
2. Assign the custom permissions to the groups based on the roles.
3. Use the `@permission_required` decorator in views to restrict access to certain actions.
