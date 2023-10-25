Feature: Product Management

  Background:
    Given the following products exist
      | name          | description             | price | category    | availability  |
      | Product 1     | This is product 1      | 100   | Electronics | In Stock     |
      | Product 2     | This is product 2      | 150   | Clothing    | Out of Stock |
      | Product 3     | This is product 3      | 75    | Home        | In Stock     |

  Scenario: Read a Product
    When I view the details of "Product 1"
    Then I should see the product details
    And the name should be "Product 1"
    And the price should be 100

  Scenario: Update a Product
    When I update the name of "Product 2" to "New Product"
    Then I should see the updated product details
    And the name should be "New Product"

  Scenario: Delete a Product
    When I delete "Product 3"
    Then the product "Product 3" should not exist

  Scenario: List All Products
    When I list all products
    Then I should see a list of products
    And the list should contain "Product 1"
    And the list should contain "New Product"
    And the list should not contain "Product 3"

  Scenario: Search by Name
    When I search for products with the name "Product 2"
    Then I should see a list of products
    And the list should contain "New Product"

  Scenario: Search by Category
    When I search for products in the category "Electronics"
    Then I should see a list of products
    And the list should contain "Product 1"

  Scenario: Search by Availability
    When I search for products with availability "In Stock"
    Then I should see a list of products
    And the list should contain "Product 1"
    And the list should contain "Product 3"
    And the list should not contain "Product 2"
