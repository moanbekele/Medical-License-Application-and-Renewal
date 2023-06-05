Feature: Employee registration

Scenario: Registering a new employee
  Given I am a logged in employee of OHO
  When I navigate to the employee registration page
  And I fill in the required information for a new employee
  And I submit the form
  Then the system should display a success message
  And the new employee should be able to log in with the provided credentials
