(define (problem ZTRAVEL-1-2)
(:domain zeno-travel)
(:requirements :typing)
(:objects
	plane1 - aircraft
	person1 - person
	person2 - person
	city0 - city
	city1 - city
	city2 - city
	city3 - city
	city4 - city
	city5 - city
	)
(:init
	(at plane1 city5)
	(at person1 city0)
	(at person2 city1)
)
(:goal (and
	(at plane1 city3)
	(at person2 city0)
	))

)

