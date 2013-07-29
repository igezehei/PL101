(define (problem ZTRAVEL-88)
(:domain zeno-travel)
(:requirements :typing)
(:objects
	plane1 - aircraft
	person1 - person
	person2 - person
	city0 - city
	city1 - city
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
