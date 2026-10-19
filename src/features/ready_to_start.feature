#noinspection CucumberUndefinedStep
Feature: redo att börja

  Scenario: redo att börja

    Given vi är på startsidan
    When  jag klickar på "Lägg till spelare"
    And   vi har spelaren "David"
    And   vi har spelaren "Emma"
    Then  knappen Börja ditt drag syns
