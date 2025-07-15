# Trip Service Kata

---
Kata for legacy code hands-on session. The objective is to test and refactor legacy code related to user trips. The end result should be well-crafted code that expresses the domain.

## Business Rules

---
Imagine a social networking website for travellers:
- You need to be logged in to see the content
- You need to be a friend to see someone else's trips
- If you are not logged in, the code throws an exception

## Exercise Rules

---
- Our job is to write tests for the legacy code until we have 100% coverage.
- Once we have 100% coverage, we need to refactor and make the code better.
- At the end of the refactoring, both tests and production code should clearly describe the business rules.

## Exercise Constraints

---
- We cannot manually change production code that is not covered by tests. That means:
  - We cannot refactor logic unless it is covered by tests.
- If we need to change a function (or introduce a class/service) in order to make it testable, you can do so using automated refactorings via your IDE.
- We CANNOT change the public interface of the main trip-related function(s):
  - We cannot change function signatures (input parameters, output values, etc.).
  - Such changes might break other code using these functions, which is not desirable right now.
- We CANNOT introduce state (i.e., global or class-level mutable variables) to the trip-related logic.
  - The code is intended to be stateless. Introducing state may cause issues, especially in concurrent scenarios.