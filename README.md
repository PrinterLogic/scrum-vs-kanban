# scrum-vs-kanban
This is a test repository.
It is designed to simulate and benchmark the differences between a scrum and a kanban environment.

## Assumptions

### Engineers/Workers
A team will be made up of 5 engineers:
1 Staff Engineer
2 Senior Engineers
1 Mid Level Engineer
1 Junior Engineer
This will be simulating a real team by adding a multiplier to how long an engineer worker will take to do a task.
These are estimates and don't reflect the work of any particular engineers.
Here are the multipliers:
Staff = 1x
Senior = 1.25x
Mid Level = 1.5x
Junior = 2x

### Agile Types
Kanban works by assigning all workers one ticket and when a worker is done with a ticket, assigns a new ticket immediately.
Scrum works by assigning all estimated tickets to workers to fill up a sprint log. All workers work to complete the sprint and move to the next sprint when complete. Due to the makeup of the teams above, we are going to be using 32 points for a sprint.

### Scrum specific assumptions
1* Most people don't let their teammembers struggle with overloaded work.
Instead, if someone has fallen behind, a member of the team usually picks up work that is still left hanging.
We will simulate this by letting every worker go through the sprint "backlog" until the sprint is complete.
2* Instead of defining a sprint interval as a set time, instead we accept that a sprint is complete when all task work in a sprint is done and allow the workers to move to the next sprint.
Otherwise, the time to complete would be calculable by the formula: `SUM(totalWork) * sprintTime / sprintSize`

## How to Run
Could probably use any 3.X Python version, but to be safe, please use Python 3.10.12+
Run the createTestData.py file with the following arguments:
Args[0] = size of test data
Args[1:] = numbers randomly chosen to place in test data
Set the environment variable `$SVK_TEST_AGILE` to either `kanban` or `scrum` (default is `kanban`)
Run the main.py file.