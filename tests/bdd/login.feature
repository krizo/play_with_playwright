Feature: Login to the website

Scenario Outline: Logging in with valid credentials
    Given I am on the login page
    When I log in with <username> and <password>
    Then I should <expected_result>

    Examples:
        | username      | password     | expected_result            |
        | student       | Password123  | see successful login       |



Scenario Outline: Logging in with invalid credentials
    Given I am on the login page
    When I log in with <username> and <password>
    Then I should <expected_result>

    Examples:
        | username      | password     | expected_result            |
        | invalid_user  | Password123  | see invalid username       |
        | student       | invalid_pass | see invalid password       |