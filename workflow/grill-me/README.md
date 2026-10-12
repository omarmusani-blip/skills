# grill-me

Stress-tests a plan before it's built. The plan is treated as a decision tree: each
question resolves one branch, comes with a recommended answer, and waits for a reply
before the next. Facts that can be looked up in the codebase are looked up, not asked;
decisions always go to the user. Nothing is enacted until both sides agree the tree is
resolved.

Trigger: "grill me", or any request to stress-test a plan or design.

Adapted from [Matt Pocock's `grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)
(MIT, see [LICENSE](LICENSE)). This copy predates upstream's switch to numbered rounds and
keeps the strict one-question-at-a-time pacing.
