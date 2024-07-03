Feature:
  Scenario: Basic first page verification
    Given the learning Elucidat page is displayed
    When the start button clicked
    Then the label text to be matched with "FINDING THE TRUTH"