# Paper-on-Immutability
Growing demand for fault-tolerant, scalable, distributed systems has made some mainstream software architectures and patterns obsolete or rather harder to come by, Thus came the rise of stateless and functional solutions based on data immutability which has already been the cornerstone of Big Data. We'll take a deep look at immutability and how it should look like in a system, then we will view four emerging technologies that implement immutability in some form and how it made them standout in the industry.

## Introduction
Unintended mutations of a program’s state cause inconsistent behavior and bugs of the
program. These mutations might have been introduced by side-effects of functions that developers
were unaware of during the program’s implementation. Some programming languages do, for example,
allow arguments of a function to be mutated. The fact that a third-party function can mutate the
state of its argument can go undetected. The problem of rogue and complicated state mutations can
become difficult to handle when states are shared among objects. One way to avoid undesired mutations
is to use immutable data instead of mutable data. Immutable data cannot be mutated once created
and instead of mutating shared data in memory, data would have to be re-created to include the modifications
needed. Programmers can then safely share data without the possibility of having it mutate to
something else, which is crucial to avoid, for example, race conditions in concurrent programs.
