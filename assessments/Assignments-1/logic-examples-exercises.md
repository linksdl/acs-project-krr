### 1 Translating from English into First-Order Logic
#### Batch 1

Formulate the following English sentences as formulae in classical 1st-order logic
(answers are given at the end of this document).

1. All purple mushrooms are poisonous.

%% ∀x[(Mushroom(x) ∧ Purple(x)) → Poisonous(x)]

all x (Mushroom(x) & Purple(x) -> Poisonous(x).


2. No student likes every lecture.

%% ¬∃x[Student(x) ∧ ∀y[Lecture(y) → Likes(x, y)]]

- (exists x (Student(x) & (all y (Lecture(y) -> Likes(x, y)))).
 
3. Everest is the highest mountain on Earth.

%% Mountain(everest) ∧ ¬∃x[Mountain(x) ∧ Higher(x, everest) ∧ On(x, earth)]
  
   - (exists x (Mountain(everest) & Mountain(x) & Higher(x, everest) & On(x, earth))).

4. There are at least two apples in a barrel.

%% ∃x∃y∃z[Apple(x) ∧ Apple(y) ∧ ¬(x = y) ∧ Barrel(z) ∧ In(x, z) ∧ In(y, z)]

   exists x exists y exists z (Apple(x) & Apple(y) & -( x = y) & Barrel(z) & In(x, z) & In(y, z)).
   
5. There are at least two apples in every barrel.

%% ∀z∃x∃y[Barrel(z) → (Apple(x) ∧ Apple(y) ∧ ¬(x = y) ∧ In(x, z) ∧ In(y, z))]

   all z exists x exists y (Barrel(z) -> (Apple(x) & Apple(y) & -(x = y) & In(x, z) & In(y, z))
  
## (Note that the universal quantification over barrels comes before the existential quantifiers over apples. 
## If we had ∃x∃y∀z[. . .] this would mean that the same two apples were present in every barrel.

6. x is part of y just in case everything that is connected to x is also connected to
y (this is a fundamental definition used in certain theories of spatial relations).

%% P(x, y) ↔ ∀z[C(z, x) → C(z, y)]
   
   exists x exists y all z (P(x ,y) <-> (C(z, x) -> C(z, y)))).

## (In this formula, the connective α ↔ β is logical equivalence and means the same as (α → β) ∧ (β → α).)

7. No region is part of each of two disjoint regions.

%% ¬∃x∃y∃z[Reg(x) ∧ Reg(y) ∧ Reg(z) ∧ P(x, y) ∧ P(x, z) ∧ Disjoint(y, z)]
- (exists x exists y exists z (Reg(x) & Reg(y) & Reg(z) & P(x, y) & P(x, z) & Disjoint(y, z))).

8. Nothing can be inside two different boxes unless one box is inside the other.
(Quite hard)

%% ∀x∀b1∀b2[(Box(b1) ∧ Box(b2) ∧ ¬(b1 = b2) ∧ In(x, b1) ∧ In(x, b2)) → (In(b1, b2) ∨ In(b2, b1))]

all x all b1 all b2 ( (Box(b1) & box(b2) & -(b1 = b2) & In(x, b1) & In(x, b2)) -> (In(b1, b2) | In(b1, b2)).

(There are many equivalent alternative formulations; but there are also many
similar formulae which are incorrect.)

#### Batch 2

1. Jane ate a mushroom that she had picked herself.
∃x[Mushroom(x) ∧ Ate(jane, x) ∧ Picked(jane, x)]

exists x (Mushroom(x) & Ate(Jane, x) & Picked(Jane, x)).

2. No yellow frogs are edible.
¬∃x[Frog(x) ∧ Yellow(x) ∧ Edible(x)]

- (exists x (Frog(x) & Yellow(x) & Edible(x))).

3. All students that had missed a lecture answered at least one question incorrectly.


4. Young creatures who go up in balloons are liable to giddiness.
∀x[(Y y ∧ Cx ∧ Bx) → Gx]
(Illustrates a concise representation for the logical form of the sentence.)


5. Every bag contains at least one coin.

∀x[Bag(x) → ∃y[Coin(y) ∧ Contains(x, y)]]

all x exists y (Bag(x) -> (Coin(y) & Contains(x, y)).


6. The father of a mother or father is a grandfather.
This is quite tricky and it is debatable what is the best representation.
One possibility is to represent all the family terms using relations:

∀x∀y[ ∃z[IsFatherOf(x, z) ∧ (IsMotherOf(z, y) ∨ IsFatherOf(z, y))] ↔ IsGrandfatherOf(x, y)]

Also we could treat some of the terms as single-argument properties:
∀x∃y[IsFatherOf(x, y) ∧ (Father(y) ∨ Mother(y))] ↔ Grandfather(x)]

But then the connection between the Father property and the IsFatherOf relation
is not made explicit. We could make this explicit with an additional formula:

∀x[Father(x) ↔ ∃y[IsFatherOf(x, y)]]

(Similar definitions could be given for the Mother and Grandfather properties.)


7. Tom’s sister knows Mary’s brother.
%% ∃x∃y[IsSisterOf(x,tom) ∧ IsBrotherOf(y, mary) ∧ Knows(x, y)]

exists x exists y (IsSisterOf(x, tom) & IsBrotherOf(y, Mary) & Knows (x, y)).

8. A careless soldier killed himself.
%% ∃x[Soldier(x) ∧ Careless(x) ∧ Killed(x, x)]

exists x (Solder(x) & Careless(x) & Killed(x, x)).


9. No happy girl despises all animals.
%% ¬∃x[Happy(x) ∧ Girl(x) ∧ ∀y[Animal(y) → Dispises(x, y)]]

-(exists x all y(Happy(x) & Girl(x) & Animal(y) -> Dispises(x, y))).

10. Every boy baked at least two cakes.
%% ∀x[Boy(x) → ∃y∃z[¬(y = z) ∧ Baked(x, y) ∧ Baked(x, z)]]

all x exists y exists z(Boy(x) -> Baked(x, y) & Baked(x, z) &-(y=z) )

11. Two regions overlap just in case they share a common part.
∀x∀y[(Reg(x) ∧ Reg(y)) → (Overlap(x, y) ↔ ∃z[Part(z, x) ∧ Part(z, y)])]


12. If three convex regions all overlap each other they share a common part.
????


13. If a cake is from France then it has more sugar if it is made with chocolate than
when it is made with cream but if a cake is from Italy then it has more sugar
if it is made with cream than if it is made of chocolate”.



#### Batch 3
1. Every person loves themself.
%% ∀x[Person(x) → Loves(x, x)]

all x(Person(x) -> Loves(x, x).


2. Everyone loves some person who loves themself.
%% ∀x[Person(x) → ∃y[Person(y) ∧ Loves(x, y) ∧ Loves(y, y)]]

all x exists y (Person(x) -> Loves(y) & Person(y) & Loves(y, y)).

3. All gardeners like the sun.
%% ∀x[Gardener(x) → Loves(x,sun)]

all x(Gardener(x) -> Loves(x, sum)).

(Since ‘sun’ refers to a unique object, it is most straightforwardly represented
by a constant (sun).)

4. Some person loves no one except themself.


5. Toby loves everyone who loves him.



6. Love is never requited. (Expand out the meaning of requited.)


7. Brown frogs are bigger than green frogs.


8. No natural food is blue.


9. Mary gave an apple to Tom.


10. One of the apples that Mary gave to Tom is Rotten.