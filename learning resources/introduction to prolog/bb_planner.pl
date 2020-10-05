 %% bb_planner.pl    Brandon Bennett (25/11/2014)
 %                   Updated 16/11/2018
 %                   
%% This code implements a breadth-first search strategy for
%% transition-based search/planning problems.
%% It has an option to automatically eliminate loops and redundant
%% diversions by discarding any path whose end state is the same as 
%% that of some shorter path.
%% To use the algorithm on a particular problem, you need to define
%% a number of problem-specific predicates that give the intitial
%% and goal states and describe the possible transitions between
%% states. This is explained in detail at the end of this file.

:- use_module( library(lists) ).

find_solution :-
          initial_state( Initial ),
          goal_state( Goal ),
          write( '== Starting Search ==' ), nl,
          solution( [[Initial]], Goal, StateList ),
          length( StateList, Len ),
          Transitions is Len -1, 
          format( '~n** FOUND SOLUTION of length ~p **', [Transitions] ), nl,
          showlist( StateList ).

%% Base case for finding solution.
%% Find a statelist whose last state is the goal or
%% or some state equivalent to the goal.
solution( StateLists, Goal, StateList ) :-
          member( StateList, StateLists ),
          last( StateList, Last ), 
          equivalent_states( Last, Goal ),
          report_progress( StateLists, final ).

%% Recursive rule that looks for a solution by extending
%% each of the generated state lists to add a further state.
solution( StateLists, Goal, StateList ) :-
          report_progress( StateLists, ongoing ),
          extend( StateLists, Extensions ), 
          solution( Extensions, Goal, StateList ).

%% Extend each statelist in a set of possible state lists.
%% If loopcheck(on) will not extend to any state previously reached
%% in any of the state lists, to avoid loops.
extend( StateLists, ExtendedStateLists ) :-
     setof( ExtendedStateList,
            StateList^Last^Next^( member( StateList, StateLists ),
                                  last( StateList, Last ),
                                  transition( Last, Next ), 
                                  legal_state( Next ),
                                  no_loop_or_loopcheck_off( Next, StateLists ),
                                  append( StateList, [Next], ExtendedStateList )
                                ),
             ExtendedStateLists
           ).

no_loop_or_loopcheck_off( _, _) :- loopcheck(off), !.
no_loop_or_loopcheck_off( Next, StateLists ) :- 
                        \+( already_reached( Next, StateLists ) ).

%% Check whether State (or some equivalent state) has already been
%% reached in any state list in StateLists.
already_reached( State,  StateLists ) :-
           member( StateList, StateLists ),
           member( State1, StateList ),
           equivalent_states( State, State1 ).

%% Print out list, each element on a separate line.          
showlist([]).
showlist([H | T]) :- write( H ), nl, showlist( T ).

%% Report progress after each cycle of the planner:
report_progress( StateLists, Status ) :-
      length( StateLists, NS ),
      member( L , StateLists ), length( L, N ),
      Nminus1 is N - 1,
      write( 'Found '), write( NS ), 
      write( ' states reachable in path length ' ), write(Nminus1), nl,
      ( Status = ongoing -> (write( 'Computing extensions of length : ' ), write(N), nl) ; true ).


%% To run this you need to define the following predicates:

% initial_state( SomeState ).
% goal_state( AnotherState ).

% Specify possible transitions from any state S1 
% transition( S1, S2 ) :- conditions.
%        :                   :         % specify as many as needed
% transition( S1, S2 ) :- conditions.

% You can add a further condition on what states are valid: 
% legal_state( S ) :- conditions.
% If no special conditions are needed just use:
% legal_state( _ ). % Allow any state
 
% You can tell the planner that some state representations are equivalent.
% equivalent_states( S1, S2 ) :- conditions.
% If all distinct state expressions represent different states, just use:
% equivalent_states( S, S ).

% You must tell the planner whether to check for and discard repeated states.
% Specify one of:
% loopcheck(off).
% loopcheck(on).
% Eliminating loops can greatly prune the search space.
% But looking for loops can use a lot of processing time, and may not be
% worth doing (especailly if loops cannot occur!).

% To run each time file is loaded, add the following command to the
% the end of your program file.
% :- find_solution.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Example:  A Measuring Jugs Problem
%%% 
%%% There are three jugs (a,b,c), whose capacity is respectively:
%%% 3 litres, 5 litres and 8 litres.
%%% Initially jugs a and b are empty and jug c is full of water.
%%% Find a sequence of pouring actions by which you can measure out
%%% 4 litres of water into one of the jugs without spilling any.

%%%  State representation will be as follows:
%%%  A state is a list:  [ how_reached, Jugstate1, Jugstate2, Jugstate3 ] 
%%%  Where each JugstateN is a lst of the form: [jugname, capcity, content]           
initial_state( [initial, [a,3,0], [b,5,0], [c,8,8]]).
goal_state( [_, [a,_,_], [b,_,B], [c,8,C]]) :- B=4 ; C=4.

%%% The state transitions are "pour" operations, where the contents of
%%% one jug is poured into another jug up to the limit of the capacity
%%% of the recipient jug:
transition( [_, A1,B1,C], [pour_a_to_b, A2,B2,C] ) :- pour(A1,B1,A2,B2).
transition( [_, A1,B,C1], [pour_a_to_c, A2,B,C2] ) :- pour(A1,C1,A2,C2).
transition( [_, A1,B1,C], [pour_b_to_a, A2,B2,C] ) :- pour(B1,A1,B2,A2).
transition( [_, A,B1,C1], [pour_b_to_c, A,B2,C2] ) :- pour(B1,C1,B2,C2).
transition( [_, A1,B,C1], [pour_c_to_a, A2,B,C2] ) :- pour(C1,A1,C2,A2).
transition( [_, A,B1,C1], [pour_c_to_b, A,B2,C2] ) :- pour(C1,B1,C2,B2).

%%% The pour operation is defined as follows:
pour( [J1,C1,IW1], [J2,C2,IW2], [J1,C1,FW1], [J2,C2,FW2] ):-
      RoomFor is C2-IW2,
      ( RoomFor >= IW1 ->
        (FW1 = 0, FW2 is IW1+IW2)
        ;
        (FW1 is IW1 - RoomFor, FW2 is C2)
      ). 


legal_state( _ ).               % All states that can be reached are legal
equivalent_states( X, X ).      % Only identical states are equivalent.
loopcheck(on).                  % Don't allow search to go into a loop. 

%% Call this goal to find a solution.
%:- find_solution.



