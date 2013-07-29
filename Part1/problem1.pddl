(define (problem typed-blocks1)
	 (:domain typed-blocksworld)
	 (:requirements :typing)
	 (:objects H - hand A - block  B - block C - block)
	 (:init (clear A) (on A B) (on B C) (on-table C) (empty H))
	 (:goal (and (on C B) (on B A))))

