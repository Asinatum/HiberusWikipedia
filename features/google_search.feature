Feature: Google Search
  As a user
  I want to perform a Google search
  So that I can find relevant information

  Scenario: Perform Google Search and Verify Wiki Link
    Given Estoy en la home page de google
    When Busco la palabra "automatizacion"
    Then Debería poder ver los resultados de la búsqueda
    When Clickeo en el link de wikipedia/automatización
    Then Debería poder ver la página de wikipedia
    When Hago un scroll hacía abajo
    Then Hago un screenshot sobre la fecha requerída
