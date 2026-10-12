#noinspection CucumberUndefinedStep
Feature: lägga till spelare
  # User story:
  # Som en användare
  # vill jag lägga till namn på mig och min motspelare
  # så att vi kan ta tiden på våra drag.

  Scenario: lägga till två spelare

    Given vi är på startsidan
    When  jag klickar på "Lägg till spelare"
    And   jag skriver in spelarnamn "David"
    And   jag klickar på "Lägg till spelare"
    And   jag skriver in spelarnamn "Gustav"
    And   jag klickar på "Lägg till spelare"
    Then  spelarens namn "David" ska visas på sidan
    And   spelarens namn "Gustav" ska visas på sidan


