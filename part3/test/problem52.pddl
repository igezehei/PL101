(define (problem ZTRAVEL-52)
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
	city8 - city
	city9 - city
	city10 - city
	city11 - city
	city12 - city
	)
(:init
	(at plane1 city0)
	(at person1 city1)
	(at person2 city0)
)
(:goal (and
	(at plane1 city9)
	(at person1 city1)
	(at person2 city9)
	))

)
