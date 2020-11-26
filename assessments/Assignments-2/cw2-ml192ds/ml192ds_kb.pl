% Daolin Sheng ml192ds
%% A Prolog knowledge base and inference system.

%% Preliminary Declarations
:- op( 950, xfx, ==>  ).  % Define a special operator to make the rules more readable.
:- dynamic fact/1.        % fact/1 predicate can be altered while program is running.

:- retractall( fact(_) ). % Clear previously stored facts.
:- use_module( library(lists) ).
:- discontiguous fact/1.

%% DEFINE SOME FACTS
%% First some general conceptual relationships.
fact( [china,   subclass_of, country] ).
fact( [india,   subclass_of, country] ).
fact( [us,      subclass_of, country] ).
fact( [uk,      subclass_of, country] ).
fact( [italy,   subclass_of, country] ).
fact( [country, subclass_of, world] ).


%% Advanced computer science (asc), krr-Knowledge Repre. Reasoning, ml-machine learning
%% ase- advanced software engineering, pds- programming for data science
%% sc- science computation
fact( [krr, subclass_of, module] ).
fact( [ml,  subclass_of, module] ).
fact( [ase, subclass_of, module] ).
fact( [pds, subclass_of, module] ).
fact( [sc,  subclass_of, module] ).
fact( [module, subclass_of, asc_project] ).

%% every module requres different skills
fact( [krr, requires, prolog] ).
fact( [krr, requires, logic] ).

fact( [ml,  requires, python] ).
fact( [ml,  requires, math] ).
fact( [ml,  requires, coding] ).

fact( [pds, requires, python] ).
fact( [pds, requires, coding] ).

fact( [sc,  requires, matlab] ).
fact( [sc,  requires, coding] ).

fact( [ase, requires, writing] ).

fact( [python,  subclass_of, language] ).
fact( [prolog,  subclass_of, language] ).
fact( [matlab,  subclass_of, language] ).

fact( [math,    subclass_of, skill] ).
fact( [logic,   sunclass_of, skill] ).
fact( [coding,  subclass_of, skill] ).
fact( [writing, subclass_of, skill] ).

%% facts for six students and teachers
fact( [alice, is, student] ).

fact( [alice, is_age, 25] ).
fact( [alice, is, male] ).
fact( [alice, comes_from, china] ).
fact( [alice, good_at, writing] ).
fact( [alice, good_at, math] ).
fact( [alcie, has_module, krr] ).
fact( [alcie, has_module, ml] ).
fact( [alcie, has_module, pds] ).
fact( [alcie, has_module, ads] ).

fact( [billy, is, student] ).
fact( [billy, is_age, 28] ).
fact( [billy, is, male] ).
fact( [billy, comes_from, china] ).
fact( [billy, good_at, coding] ).
fact( [billy, good_at, math] ).
fact( [billy, good_at, logic] ).
fact( [billy, has_module, krr] ).
fact( [billy, has_module, ml] ).
fact( [billy, has_module, pds] ).
fact( [billy, has_module, sc] ).

fact( [cola, is, student] ).
fact( [cola, is_age, 23] ).
fact( [cola, is, female] ).
fact( [cola, comes_from, us] ).
fact( [cola, good_at, logic] ).
fact( [cola, has_module, krr] ).
fact( [cola, has_module, ml] ).
fact( [cola, has_module, pds] ).
fact( [cola, has_module, sc] ).

fact( [dota, is, student] ).
fact( [dota, is_age, 23] ).
fact( [dota, is, female] ).
fact( [dota, comes_from, us] ).
fact( [dota, good_at, logic] ).
fact( [dota, has_module, krr] ).
fact( [dota, has_module, ml] ).
fact( [cola, has_module, pds] ).

fact( [echo, is, student] ).
fact( [echo, is_age, 22] ).
fact( [echo, is, female] ).
fact( [echo, comes_from, uk] ).
fact( [echo, good_at, coding] ).
fact( [echo, has_module, krr] ).
fact( [echo, has_module, ml] ).
fact( [echo, has_module, pds] ).
fact( [echo, has_module, sc] ).

fact( [harry, is, student] ).
fact( [harry, is_age, 25] ).
fact( [harry, is, female] ).
fact( [harry, comes_from, india] ).
fact( [harry, good_at, math] ).
fact( [harry, has_module, krr] ).
fact( [harry, has_module, ml] ).
fact( [harry, has_module, sc] ).

fact( [toni, teaches, sc] ).
fact( [toni, is, teacher] ).
fact( [toni, comes_from, india] ).

fact( [brandon, teaches, krr] ).
fact( [brandon, teaches, pds] ).
fact( [brandon, is, teacher] ).
fact( [brandon, comes_from, uk] ).

fact( [matteo, teaches, ml] ).
fact( [matteo, is, teacher] ).
fact( [matteo, comes_from, italy] ).

fact( [jack, teaches, ads] ).
fact( [jack, is, teacher] ).
fact( [jack, comes_from, us] ).
%% 

module_study_time_list([
                   ['alice','krr',8], ['alice','ml',16], ['alice','pds',12],['alice','ase',8],
                   ['billy','krr',7],  ['billy','ml',16], ['billy','pds',8], ['billy','sc',15],
                   ['cola', 'krr',8],  ['cola', 'ml',12], ['cola','pds',5],  ['cola','sc',12],
                   ['dota', 'krr',15], ['dota', 'ml',9],  ['dota','pds',4], 
                   ['echo', 'krr',9],  ['echo', 'ml',12], ['echo', 'pds', 13], ['echo', 'sc', 8],
                   ['harry', 'krr',6], ['harry','ml',12], ['harry', 'sc', 9]
                   ]).

fact( [Name, pay_time, Time, in, Module] ):- module_study_time_list(List),nth1(_,List,[Name,Module,Time]).


%% SPECIFY INFERENCE RULES
ruleset([_]). % This will allow any rule to work. Comment out this line if using a restricted specific set.
%ruleset([logic,taxonomy]). % Can restrict to a given ruleset.

%% General logical and set-theoretic rules
rule( logic, [[C1, subclass_of, C2], [C2, subclass_of, C3]] ==> [C1, subclass_of, C3] ).
rule( logic, [[X, is, C1], [C1, subclass_of, C2]]  ==>  [X, is, C2] ).

%% Taxanomic relationships regarding the concept vocabulary
rule( taxonomy,[[X,is,student],[Y,is,teacher],[X,has_module,S],[Y, teaches, S]]==>[Y,is_teacher_of,X]).

%% Other semantic relations holding among concepts.
rule( semantic,  [[X, comes_from, S], [Y, comes_from, S], test(different(X,Y))]
      ==> [X, and, Y, have_common_country] ).

rule( semantic,  [[X, is, student],[X, has_module, S], [Y, is, student],[Y, has_module, S], test(different(X,Y))]
      ==> [X, and, Y, have_common_module] ).

rule( semantic, [[X, is, student],[Y, is, student],[X, good_at, S],[Y, good_at, S],test(different(X,Y))]
      ==> [X, and, Y, have_common_skill] ).

rule( semantic,  [[X, is, student],[Y, is, student],[X, likes, S], [Y, likes, S], test(different(X,Y))]
      ==> [X, and, Y, have_common_interest] ).

%% Some domain specific inference rules:
rule(interest, [[X, is, student], [X, has_module, S],[S, requires, W], [X, good_at, W]] ==> [X, likes, W]).

rule(group, [[X, is, student], [X, likes, U], [Y, is, student], [Y, likes, U]] ==> [X, and, Y, have_same_group]).
rule(group, [[X, is, student], [Y, is, student], [X, and, Y, have_same_group]] ==> [X, and, Y, makes_friend]).


rule(performance, [[X, is, student], [X, pay_time, T, in, M], [X, has_module, M],test(T>=16) ]  
     ==> [X, perform_great, M]).

rule(performance, [[X, is, student], [X, pay_time, T, in, M], [X, has_module, M],test(T>=12),[M, requires, Y], [X, good_at, Y] ]  
     ==> [X, perform_great, M]).

rule(performance, [[X, is, student], [X, pay_time, T, in, M], [X, has_module, M],test(T>=12),test(T<16) ]  
     ==> [X, perform_good, M]).

rule(performance, [[X, is, student], [X, pay_time, T, in, M], [X, has_module, M],test(T>=8),test(T<12) ]  
     ==> [X, perform_normal, M]).

rule(performance, [[X, is, student], [X, pay_time, T, in, M], [X, has_module, M],test(T<8) ]  
     ==> [X, perform_bad, M]).

rule(best, [[X, is, student], [X, has_module, M], [X, perform_great, M]] ==> [X, is_best_student, _]).

rule(happy,[[X, is, student], [Y, is, teacher], [X, has_module, M], [Y, teaches, M], [X, perform_great, M]] 
     ==> [Y, happy_for, X]).

%% Default rules make inferences on condition that something is not provable.
%% Such rules should go after the positive inference rules.
rule( default,  [[X, and, Y, have_common_interest], \+(-[X, likes, Y]) ]  ==>  [X,likes,Y] ).

%% Define how to interpret 'test' conditions in rule preconditions:
test( X < Y )  :- X<Y.
test( X =< Y ) :- X=<Y.
test( X = Y )  :- X=Y.
test( X > Y )  :- X>Y.
test( X >= Y ) :- X>=Y.
test( different(X,Y) ) :- \+(X=Y).

%% THE INFERENCE MECHANISM

%% applyrule: check if premisses are satisfiable. If so assert the conclusion.

applyrule( T, [] ==> Conc ) :- % If no premisses, assert conclusion (unless already known).
    \+( fact( Conc ) ),
    assert( fact( Conc ) ),
    (show_inferences -> show_inference(Conc, T) ; true).

applyrule( T, [-(P) | Rest] ==> Conc ) :-   % Check strong negated premiss is a negative fact
    fact( -(P) ),
    applyrule( T, Rest ==> Conc ).

applyrule( T,  [\+(P) | Rest] ==> Conc ) :-   % Check weak negated premiss is not a fact
    \+(fact( P )),
    applyrule( T, Rest ==> Conc ).

applyrule( T, [test(Test) | Rest] ==> Conc ) :-  % Evaluate a test condition.
     ground(Test), test( Test ),
     applyrule( T, Rest ==> Conc ).

applyrule( T,[Prem | Rest] ==> Conc ) :-     % Look for fact matching first premiss
     fact( Prem ),
     applyrule( T, Rest ==> Conc ).

%% infer applies all rules to all currently stored facts.
infer :- ruleset(Rules),
         bagof( i, R^Type^( rule(Type, R), member(Type, Rules), applyrule(Type, R)), Infs ),
         length( Infs, Len ),
         write('*** Number of inferences carried out: '), write( Len ), nl, nl,
         Len > 0.  % fail if no inferences found.

%% infer/1 repeatedly calls infer up to a given inference depth limit.
infer( Limit ) :- infer( 1, Limit ).
infer( Depth, Limit ) :- Depth>Limit, !, write( '*** Max inference depth reached' ), nl, nl.
infer( Depth, Limit ) :- write( '*** Inference depth: ' ), write( Depth ),
                              write( ' ... ' ), nl,
                              infer, !,
                              Next is Depth + 1, infer( Next, Limit ).
infer( _, _ ) :- write( '*** No more inferences found' ), nl, nl.


%% Useful Display Predicates
%% Show all facts
allfacts :-  write('=== ALL KNOWN FACTS ==='), nl, (fact(F), write(F), nl, fail) ; true.
%% Show all facts involving terms in list L
describe(L) :- L=[] ; (L = [H|T], describe(H), describe(T)).
describe(X) :- write('=== Facts involving: '), write( X ), write(' ==='), nl,
              ( (fact(F), (member(X,F);(F= -(G), member(X,G))), write(F), nl, fail) ; true ).

show_inference( Conc, Type ) :-
    format( 'Infer: ~p ~50+  (~p)~n', [Conc, Type] ).

show_inferences :- true. %% Change this to false to hide inference output.

/** <examples>
 %% You can add your own queries here.

 %% Display known facts about a thing or list of things:
?- describe( billy ).
?- describe( [krr,,ml,sc] ).

?- allfacts. %% Display all known facts.

%% Compute inferences up to a given depth:
?- infer(1).
?- infer(2).
?- infer(3).
?- infer(4).
?- infer(5).

%% Compute inferences to a given level; then display known facts (including those inferred):
?- infer(2), describe([have_common_interest]).
?- infer(3), describe([likes]).
?- infer(3), describe([happy_for, is_best_student]).
?- infer(3), describe([billy]).
?- infer(5), allfacts.
*/
