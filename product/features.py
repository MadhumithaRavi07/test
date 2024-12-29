# features/products.feature

Feature: Product Management

  Scenario: Reading a product by ID
    Given I have a product with ID 1
    When I read the product details
    Then I should see the product's name is "Test Product 1"
