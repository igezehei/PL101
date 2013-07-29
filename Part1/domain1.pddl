(define (domain typed-blocksworld)
(:requirements :typing)
(:typing block hand)
(:predicates (clear ?b - block)
	     (on-table ?b - block)
	     (empty ?h - hand)
	     (holding ?h - hand ?b - block)
	     (on ?b1 ?b2 - block))

(:action pickup
  :parameters (?h - hand ?b - block)
  :precondition (and (clear ?b) (on-table ?b) (empty ?h))
  :effect (and (holding ?h ?b) (not (clear ?b)) (not (on-table ?b))
               (not (empty ?h))))

(:action putdown
  :parameters (?h - hand ?b - block)
  :precondition (holding ?h ?b)
  :effect (and (clear ?b) (empty ?h) (on-table ?b)
               (not (holding ?h ?b))))

(:action stack
  :parameters (?h - hand ?b ?underb - block)
  :precondition (and (clear ?underb) (holding ?h ?b))
  :effect (and (empty ?h) (clear ?b) (on ?b ?underb)
               (not (clear ?underb)) (not (holding ?h ?b))))

(:action unstack
  :parameters (?h - hand ?b ?underb - block)
  :precondition (and (on ?b ?underb) (clear ?b) (empty ?h))
  :effect (and (holding ?h ?b) (clear ?underb)
               (not (on ?b ?underb)) (not (clear ?b)) (not (empty ?h)))))

