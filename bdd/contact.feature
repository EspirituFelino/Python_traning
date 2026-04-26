Scenario Outline: Add a new contact
  Given a contact list
  Given a contact with <first_name>, <last_name>, <workphone>, <email>, <address>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact

  Examples:
  | first_name  | last_name  | workphone  | email  | address  |
  | first_name1 | last_name1 | workphone1 | email1 | address1 |
  | first_name2 | last_name2 | workphone2 | email2 | address2 |

Scenario: Delete some contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal old contact list without deleted contact

Scenario: Modify some contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <first_name>, <last_name>, <workphone>, <email>, <address>
  When I modify random contact with the contacts attributes
  Then the new contact list is equal to the old contact list with replaced contact

  Examples:
  | first_name  | last_name  | workphone  | email  | address  |
  | first_name1 | last_name1 | workphone1 | email1 | address1 |
