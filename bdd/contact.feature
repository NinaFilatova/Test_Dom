Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename> , <lastname>, <address>, <email> and <phone>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact

  Examples:
  | firstname   | middlename   | lastname   | address   | email        | phone   |
  | firstname1  | middlename1  | lastname1  | address1  | email1@mail  | 789456  |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact

Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a modify data with <firstname>, <middlename> , <lastname>, <address>, <email> and <phone>
  When I modify the contact from the list
  Then the modified contact list is equal to the old list with modified contact

Examples:
  | firstname   | middlename   | lastname   | address   | email          | phone   |
  | modified    | modified     | modified   | modified  | etrrterd@mail  | 989899  |