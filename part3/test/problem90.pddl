(define (problem ZTRAVEL-90)
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
	city6 - city
	city7 - city
	)
(:init
	(at plane1 city0)
	(at person1 city1)
	(at person2 city0)
)
(:goal (and
	(at person1 city1)
	(at person2 city1)
	))

)
