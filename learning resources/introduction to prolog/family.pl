

add( 1, 1, 2 ).

test( yes, ok ) :- !.
test( _,  not_ok ).
 


fizz_buzz( X, fizz_buzz ) :- 3 is mod( 3, X ),
                             5 is mod( 5, X ), 
                             !,
                             ( write(a); write(b) ).


fizz_buzz( X, fizz ) :- 3 is mod( 3, X ).

fizz_buzz( X, buzz ) :- 5 is mod( 5, X ).




in_list( X, [X | _] ).
in_list( X, [_ | Tail ] ) :- in_list( X, Tail ).

    


likes( X, X ).
likes( me, mary ).

male( john ).
male( sirus ).
male( sam).
female( jill ).
female( mary ).

parent_of( sirus, john ).
parent_of( john, mary ). 
parent_of( mary, tom ).
parent_of( mary, sue ).
parent_of( john, sam ).
parent_of( sam, jill ).


grandfather_of( X, Y ) :-
       male( X ),
       parent_of( X, Z ),
       parent_of( Z, Y ).


sibling_of( X, Y ) :-
        parent_of( Z, X ),
        parent_of( Z, Y ),
        \+( X = Y).


% red_or_green( X ) :-  X = red ; X = green.

red_or_green( red ).
red_or_green( green ).
red_or_green( green ).




% The following code defines a predicate that enables
%% you to quickly relode this file after you modify it.
%% Just type "lf." at the Prolog prompt to reload.
lf :- [family].
