Feature: Access Database for Logged Out Employee

  As a logged out employee of OHO,
  I want to access the database with my username and password
  So that I can add/remove and edit data in the database

  Background:
    Given the OHO database is up and running

  Scenario: Log in with valid credentials
    Given I am a logged out employee of OHO
    When I enter my valid username and password
    And I try to log in
    Then I should be successfully logged in
    And I should be able to add, remove, and edit data in the database

  Scenario: Log in with invalid credentials
    Given I am a logged out employee of OHO
    When I enter an invalid username or password
    And I try to log in
    Then I should not be logged in
    And I should see an error message indicating invalid credentials

  Scenario: Log in with empty credentials
    Given I am a logged out employee of OHO
    When I leave the username or password field empty
    And I try to log in
    Then I should not be logged in
    And I should see an error message indicating that the fields are required
