# This file need to import search.py
# Author: Wen Shen and Issak Gezehei
import copy
import itertools
import search

class UnreachableError(Exception):
    pass
class ParseError(Exception):
    pass
class Condition(object):
    def __init__(self, parts):
        self.parts = tuple(parts)
        self.hash = hash((self.__class__, self.parts))
    def __hash__(self):
        return self.hash
    def __ne__(self, other):
        return not self == other
    def printer(self, indent="  "):
        print "%s%s" % (indent, self._printer())
        for part in self.parts:
            part.printer(indent + "  ")
    def _printer(self):
        return self.__class__.__name__
    
class Literal(Condition):
    parts = []
    def __init__(self, predicate, args):
        self.predicate = predicate
        self.args = tuple(args)
        self.hash = hash((self.__class__, self.predicate, self.args))
    def __eq__(self, other):
        # Compare hash first for speed reasons.
        return (self.hash == other.hash and
                self.__class__ is other.__class__ and
                self.predicate == other.predicate and
                self.args == other.args)
    def __str__(self):
        return "%s %s(%s)" % (self.__class__.__name__, self.predicate,
                              ", ".join(map(str, self.args)))
    def _printer(self):
        return str(self)
    def change_parts(self, parts):
        return self
        
class Atom(Literal):
    negated = False
    def instantiate(self, var_mapping, init_facts, fluent_facts, result):
        args = [var_mapping.get(arg, arg) for arg in self.args]
        atom = Atom(self.predicate, args)
        if atom in fluent_facts:
            result.append(atom)
        elif atom not in init_facts:
            raise UnreachableError()
    def negate(self):
        return NegatedAtom(self.predicate, self.args)
    def positive(self):
        return self

class NegatedAtom(Literal):
   negated = True
   def instantiate(self, var_mapping, init_facts, fluent_facts, result):
        args = [var_mapping.get(arg, arg) for arg in self.args]
        atom = Atom(self.predicate, args)
        if atom in fluent_facts:
            result.append(NegatedAtom(self.predicate, args))
        elif atom in init_facts:
            #raise UnreachableError()
            pass
   def negate(self):
        return Atom(self.predicate, self.args)
   positive = negate

class Term(object):
    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)
    def printer(self, indent="  "):
        print "%s%s %s" % (indent, self._printer(), self.name)
        for arg in self.args:
            arg.printer(indent + "  ")
    def _printer(self):
        return self.__class__.__name__

class Variable(Term):
    args = []
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class ObjectTerm(Term):
    args = []
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class ConstantCondition(Condition):
    parts = ()
    def __init__(self):
        self.hash = hash(self.__class__)
    def change_parts(self, parts):
        return self
    def __eq__(self, other):
        return self.__class__ is other.__class__

class Falsity(ConstantCondition):
    def instantiate(self, var_mapping, init_facts, fluent_facts, result):
        raise UnreachableError()
    def negate(self):
        return Truth()
class Truth(ConstantCondition):
    def instantiate(self, var_mapping, init_facts, fluent_facts, result):
        pass
    def negate(self):
        return Falsity()
        
class JunctorCondition(Condition):
    def __eq__(self, other):
        return (self.hash == other.hash and
                self.__class__ is other.__class__ and
                self.parts == other.parts)
    def change_parts(self, parts):
        return self.__class__(parts)

class Conjunction(JunctorCondition):
    def _simplified(self, parts):
        result_parts = []
        for part in parts:
            if isinstance(part, Conjunction):
                result_parts += part.parts
            elif isinstance(part, Falsity):
                return Falsity()
            elif not isinstance(part, Truth):
                result_parts.append(part)
        if not result_parts:
            return Truth()
        if len(result_parts) == 1:
            return result_parts[0]
        return Conjunction(result_parts)
    def instantiate(self, var_mapping, init_facts, fluent_facts, result):
        assert not result, "Condition not simplified"
        for part in self.parts:
            part.instantiate(var_mapping, init_facts, fluent_facts, result)
    def negate(self):
        return Disjunction([p.negate() for p in self.parts])

class Disjunction(JunctorCondition):
    def _simplified(self, parts):
        result_parts = []
        for part in parts:
            if isinstance(part, Disjunction):
                result_parts += part.parts
            elif isinstance(part, Truth):
                return Truth()
            elif not isinstance(part, Falsity):
                result_parts.append(part)
        if not result_parts:
            return Falsity()
        if len(result_parts) == 1:
            return result_parts[0]
        return Disjunction(result_parts)
    def negate(self):
        return Conjunction([p.negate() for p in self.parts])
    def has_disjunction(self):
        return True

class Type(object):
    def __init__(self, name, basetype_name=None):
        self.name = name
        self.basetype_name = basetype_name
    def __str__(self):
        return self.name
    def __repr__(self):
        return "Type(%s, %s)" % (self.name, self.basetype_name)
        
class Effect(object):
    def __init__(self, parameters, condition, literal):
        self.parameters = parameters
        self.condition = condition
        self.literal = literal
    def __eq__(self, other):
        return (self.__class__ is other.__class__ and
                self.parameters == other.parameters and
                self.condition == other.condition and
                self.literal == other.literal)
    def printer(self):
        indent = "  "
        if self.parameters:
            print "%sforall %s" % (indent, ", ".join(map(str, self.parameters)))
            indent += "  "
        if self.condition != Truth():
            print "%sif" % indent
            self.condition.printer(indent + "  ")
            print "%sthen" % indent
            indent += "  "
        print "%s%s" % (indent, self.literal)
    
    def instantiate(self, var_mapping, init_facts, fluent_facts, result):
        condition = []
        try:
            self.condition.instantiate(var_mapping, init_facts, fluent_facts, condition)
        except  UnreachableError:
            return
        effects = []
        self.literal.instantiate(var_mapping, init_facts, fluent_facts, effects)
        assert len(effects) <= 1
        if effects:
            result.append((condition, effects[0]))
            
class CostEffect(object):
    def __init__(self, effect):
        self.effect = effect
    def dump(self, indent="  "):
        print "%s%s" % (indent, self.effect)
    def normalize(self):
        return self
    def extract_cost(self):
        return self, None 
    
class ConjunctiveEffect(object):
    def __init__(self, effects):
        flattened_effects = []
        for effect in effects:
            if isinstance(effect, ConjunctiveEffect):
                flattened_effects += effect.effects
            else:
                flattened_effects.append(effect)
        self.effects = flattened_effects
    def printer(self, indent="  "):
        print "%sand" % (indent)
        for eff in self.effects:
            eff.printer(indent + "  ")
    def normalize(self):
        new_effects = []
        for effect in self.effects:
            new_effects.append(effect.normalize())
        return ConjunctiveEffect(new_effects)
    def extract_cost(self):
        new_effects = []
        cost_effect = None
        for effect in self.effects:
            if isinstance(effect, CostEffect):
                cost_effect = effect
            else:
                new_effects.append(effect)
        return cost_effect, ConjunctiveEffect(new_effects)

class SimpleEffect(object):
    def __init__(self, effect):
        self.effect = effect
    def printer(self, indent="  "):
        print "%s%s" % (indent, self.effect)
    def normalize(self):
        return self
    def extract_cost(self):
        return None, self

class TypedObject(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def __hash__(self):
        return hash((self.name, self.type))
    def __eq__(self, other):
        return self.name == other.name and self.type == other.type
    def __ne__(self, other):
        return not self == other
    def __str__(self):
        return "%s: %s" % (self.name, self.type)
        
class Predicate(object):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments
    def parse(alist):
        name = alist[0]
        arguments = parse_typed_list(alist[1:], only_variables=True)
        return Predicate(name, arguments)
    parse = staticmethod(parse)
    def __str__(self):
        return "%s(%s)" % (self.name, ", ".join(map(str, self.arguments)))

class Action(object):
    def __init__(self, name, parameters, precondition, effects):
        self.name = name
        self.parameters = parameters
        self.precondition = precondition
        self.effects = effects
    def __repr__(self):
        return "<Action %r>" % (self.name, id(self))
    def parse(alist):
        iterator = iter(alist)
        if iterator.next() == ":action":
            pass
        else:
            raise SystemExit("Error! The typed STRIPS PDDL file should include actions!")
        name = iterator.next()
        parameters_tag_opt = iterator.next()
        if parameters_tag_opt == ":parameters":
            parameters = parse_typed_list(iterator.next(),
                                                     only_variables=True)
            precondition_tag_opt = iterator.next()
        else:
            parameters = []
            precondition_tag_opt = parameters_tag_opt
        if precondition_tag_opt == ":precondition":
            precondition = parse_condition(iterator.next())
            effect_tag = iterator.next()
        else:
            precondition = Conjunction([])
            effect_tag = precondition_tag_opt
        if effect_tag == ":effect":
            pass
        else:
            raise SystemExit("Error! The action should include the effect properly.")
        effect_list = iterator.next()
        eff = []
        parse_effects(effect_list, eff)
        for rest in iterator:
            assert False, rest
        return Action(name, parameters, precondition, eff)
    parse = staticmethod(parse)
    def printer(self):
        print "%s(%s)" % (self.name, ", ".join(map(str, self.parameters)))
        print "Precondition:"
        self.precondition.printer()
        print "Effects:"
        for eff in self.effects:
            eff.printer()
    def instantiate(self, var_mapping, init_facts, fluent_facts):
        arg_list = [var_mapping[par.name] for par in self.parameters]
        name = "(%s %s)" % (self.name, " ".join(arg_list))

        precondition = []
        try:
            self.precondition.instantiate(var_mapping, init_facts,
                                          fluent_facts, precondition)
        except UnreachableError:
            return None
        effects = []
        for eff in self.effects:
            eff.instantiate(var_mapping, init_facts, fluent_facts,
                             effects)
        if effects:
            return PropositionalAction(name, precondition, effects)
        else:
            return None

class PropositionalAction:
    def __init__(self, name, precondition, effects):
        self.name = name
        self.precondition = precondition
        self.add_effects = []
        self.del_effects = []
        for condition, effect in effects:
            if not effect.negated:
                self.add_effects.append((condition, effect))
        for condition, effect in effects:
            if effect.negated and (condition, effect.negate()) not in self.add_effects:
                self.del_effects.append((condition, effect.negate()))
    def __repr__(self):
            return "<Action: %s>" %(self.name)
            
class Domain:
    def __init__(self, domain_name,  requirements,  typing,  constants,  predicates,  actions):
        self.domain_name = domain_name
        self.requirements = requirements
        self.types = typing
        self.constants = constants
        self.predicates = predicates
        self.actions = actions

    def get_instance(typed_strips_domain_file):
        domain_file = parse_pddl('domain', typed_strips_domain_file) 
        domain_name, requirements, types, constants, predicates, actions \
        = parse_domain(domain_file)
        
        return Domain(domain_name, requirements, types, constants, predicates, actions)
    get_instance = staticmethod(get_instance)

    def printer(self):
        print "Domain %s: [%s]" % (self.domain_name, self.requirements)

        print "Types:"
        for type_ in self.types:
            print "  %s" % type_

        print "Constants:"
        for const in self.constants:
            print "  %s" % const
        print "Predicates:"
        for pred in self.predicates:
            print "  %s" % pred

        print "Actions:"
        for action in self.actions:
            action.printer()


class Problem:
    def __init__(self, problem_name, domain_name, requirements, objects, init, goal):
        self.problem_name = problem_name
        self.domain_name = domain_name
        self.requirements = requirements
        self.objects = objects
        self.init = init
        self.goal = goal

    def get_instance(typed_strips_problem_file):
        problem_pddl= parse_pddl('problem', typed_strips_problem_file) 
        problem_name, domain_name, requirements,  objects, init, goal = parse_problem(problem_pddl)
        return Problem(problem_name, domain_name, requirements, objects, init, goal)
    get_instance = staticmethod(get_instance)

    def printer(self):
        print "Problem %s: %s [%s]" % (self.problem_name, self.domain_name, self.requirements)
        print "Objects:"
        for obj in self.objects:
            print "  %s" % obj
        print "Init:"
        for init_ in self.init:
            print "  %s" % init_
        print "Goals:"
        print self.goal.printer()

class State:
    def __init__(self, domain, problem):
        assert(domain.domain_name == problem.domain_name)
        self.domain = domain
        self.problem = problem
        self.goal = problem.goal
        self.objects = domain.constants+problem.objects

class Task(search.Problem):
    def __init__(self, domain,  problem):
        self.initial = State(domain, problem)
        self.goal = self.initial.goal
        search.Problem.__init__(self, self.initial, self.initial.goal)
        
    def successor(self, state):
        return self.get_successors(self.get_actions(state),  state)
        
    def get_successors(self, actions,  state):
        successors =[]
        for action_ in actions:
            successor = self.successor_assist(action_, state)
            successors.append(successor)
        return successors
        
    def successor_assist(self, action, state):
         new_facts =[]
         new_state = copy.deepcopy(state)
         for fact in state.problem.init:
            if fact not in action.del_effects:
                new_facts.append(fact)
         new_state.problem.init = new_facts
         new_state.problem.init += action.add_effects
         return (action,  new_state)
         
    def get_fluent_facts(self,para_mapping,action):
        fluent_facts = []
        for effect in action.effects:
            args =[]
            for argument in effect.literal.args:
                new_arg =para_mapping.get(argument, argument)
                args.append(new_arg)
            if  effect.literal.negated:
                atom = NegatedAtom(effect.literal.predicate,args)
            else:
                atom =Atom(effect.literal.predicate,args)
            fluent_facts.append(atom)
        return fluent_facts
        
    #To get all the possible actions
    def get_actions(self, state):
        actions =[]
        for action in state.domain.actions:
            actions += self.get_new_action(action, state)
        return actions
        
    def get_new_action(self, action,  state):
        actions_result = [] 
        pairs = []
        parameters = action.parameters
        parameter_types = [parameter.type for parameter in parameters]
        for parameter_type in parameter_types:
            all_objects = self.get_objects(parameter_type,state.objects)
            pairs.append(all_objects)
        para_combinators= [list(comb) for comb in itertools.product(*pairs)]
        for combinator in para_combinators:
            var_mapping = dict([param.name,cob.name] for param,cob in zip(parameters,combinator))
            #To get the fluent_facts based on the var_mapping
            fluent_facts = self.get_fluent_facts(var_mapping,action)
            #To get all the actions based on the generated vara_mapping and fluent_facts
            new_action = action.instantiate(var_mapping,state.problem.init,fluent_facts)
            if new_action:
                actions_result.append(new_action)
        return actions_result
        
    def get_objects(self,parameters_type,objects):
    #To get the objects which meet the type of the parameter
        return [obj for obj in objects if obj.type == parameters_type]
    
 # To parse the conditions   
def parse_condition(alist):
    condition = parse_condition_aux(alist, False)
    return condition
    
def parse_condition_aux(alist, negated):
    tag = alist[0]
    if tag in ("and", "or", "not"):
        args = alist[1:]
        if tag == "not":
            assert len(args) == 1
            return parse_condition_aux(args[0], not negated)
    elif negated:
        return NegatedAtom(alist[0], alist[1:])
    else:
        return Atom(alist[0], alist[1:])
    parts = [parse_condition_aux(part, negated) for part in args]

    if tag == "and" and not negated or tag == "or" and negated:
        return Conjunction(parts)
    elif tag == "or" and not negated or tag == "and" and negated:
        return Disjunction(parts)
        
# To parse the literals
def parse_literal(alist):
    if alist[0] == "not":
        assert len(alist) == 2
        alist = alist[1]
        return NegatedAtom(alist[0], alist[1:])
    else:
        return Atom(alist[0], alist[1:])
# To parse the terms

def parse_term(term):
    if isinstance(term, list): 
        return FunctionTerm(term[0],[parse_term(t) for t in term[1:]])
    elif term.startswith("?"):
        return Variable(term)
    else:
        return ObjectTerm(term)

def transitive_closure(pairs):
    result = set(pairs)
    nodes = set(u for (u, v) in pairs) | set(v for (u, v) in pairs)
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if (i, j) not in result and (i, k) in result and (k, j) in result:
                    result.add((i, j))
    return sorted(result)
    
def set_uppertypes(type_list):
    typename_to_type = {}
    child_types = []
    for type in type_list:
        type.supertype_names = []
        typename_to_type[type.name] = type
        if type.basetype_name:
            child_types.append((type.name, type.basetype_name))
    for (desc_name, anc_name) in transitive_closure(child_types):
        typename_to_type[desc_name].supertype_names.append(anc_name)
        
# To parse the effects
def parse_effects(alist, result):
    tmp_effect = parse_effect(alist)
    normalized = tmp_effect.normalize()
    cost_eff, rest_effect = normalized.extract_cost()
    add_effect(rest_effect, result)
    if cost_eff:
        return cost_eff.effect
    else:
        return None

def add_effect(tmp_effect, result):
    if isinstance(tmp_effect, ConjunctiveEffect):
        for effect in tmp_effect.effects:
            add_effect(effect, result)
        return
    else:
        parameters = []
        condition = Truth()
        assert isinstance(tmp_effect, SimpleEffect)
        effect = tmp_effect.effect
        assert isinstance(effect, Literal)
        # Check for contradictory effects
        new_effect = Effect(parameters, condition, effect)
        contradiction = Effect(parameters, condition, effect.negate())
        if not contradiction in result:
            result.append(new_effect)
        else:
            if isinstance(contradiction.literal, NegatedAtom):
                result.remove(contradiction)
                result.append(new_effect)

def parse_effect(alist):
    tag = alist[0]
    if tag == "and":
        return ConjunctiveEffect([parse_effect(eff) for eff in alist[1:]])
    else:
        return SimpleEffect(parse_literal(alist))

def parse_typed_list(alist, only_variables=False, constructor=TypedObject, functions=False):
    result = []
    while alist:
        try:
            separator_position = alist.index("-")
        except ValueError:
            items = alist
            if functions:
                _type = "number"
            else:
                _type = "object"
            alist = []
        else:
            items = alist[:separator_position]
            _type = alist[separator_position + 1]
            alist = alist[separator_position + 2:]
        for item in items:
            assert not only_variables or item.startswith("?")
            entry = constructor(item, _type)
            result.append(entry)
    return result

# To parse the nested list
def parse_nested_list(input_file):
    # tokenize the input file
    tokens = tokenize(input_file)
    next_token = tokens.next()
    if next_token != "(":
        raise  SystemExit("Expected '(', got %s." % next_token)
    result = list(parse_list_assist(tokens))
    # Check that generator is exhausted.
    for tok in tokens:  
        raise SystemExit("Unexpected token: %s." % tok)
    return result

def tokenize(input):
    for line in input:
        line = line.split(";", 1)[0]  # Strip comments.
        # Add space
        line = line.replace("(", " ( ").replace(")", " ) ").replace("?", " ?") 
        for token in line.split():
            yield token.lower()

# To parse the tokenstream without the pair of the parenthese
def parse_list_assist(tokenstream):
    # Leading "(" has already been swallowed.
    while True:
        try:
            token = tokenstream.next()
        except StopIteration:
            raise ParseError()
        if token == ")":
            return
        elif token == "(":
            yield list(parse_list_assist(tokenstream))
        else:
            yield token

# To parse a pddl file: domain or problem
def parse_pddl(type, filename):
    try:
        return parse_nested_list(file(filename))
    except IOError, e:
        raise SystemExit("Error: Can not read file: %s\nReason: %s." %
                         (e.filename, e))
    except ParseError, e:
        raise SystemExit("Error: Can not parse %s file: %s\n" % (type, filename))

# Parse the domain pddl
def parse_domain(domain_pddl):
    iterator = iter(domain_pddl)
    
    # To assure that the file is a domain file
    if iterator.next() == "define":
         pass
    else:
         raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should begin with the keyword: define")
    domain_name = iterator.next()
    
    # To get the domain name
    if domain_name[0] == "domain" and len(domain_name) == 2:
        yield domain_name[1]
    else:
        raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should begin with include the definition of domain")

    requirements_option = iterator.next()
    # To get the requirements
    if  requirements_option[0]==":requirements" and len(requirements_option)==2:
        yield requirements_option[1]
    else:
        raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include only one requirement!")
        
    types_option = iterator.next()
    # To get the types or typing
    if  types_option[0]==':typing' or types_option[0]==':type':
        types_result = [Type("object")] # Add object to the types
        types_result.extend(parse_typed_list(types_option[1:], constructor=Type))
        set_uppertypes(types_result)
        yield types_result
    else:
        raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include at least one type")

    constants_option = iterator.next()
    # To get the constants if any
    if constants_option[0] == ":constants":
        yield parse_typed_list(constants_option[1:])
        pred = iterator.next()
    else:
        yield []
        pred = constants_option

    # To get  predicates
    if pred[0] == ":predicates":
        yield ([Predicate.parse(entry) for entry in pred[1:]] +
           [Predicate("=",
                                 [TypedObject("?x", "object"),
                                 TypedObject("?y", "object")])])
    else:
        raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include predicates")
                                  
    first_action = iterator.next()
    entries = [first_action] + [entry for entry in iterator]
    the_actions = []
    for entry in entries:
        action = Action.parse(entry)
        the_actions.append(action)
    yield the_actions
# To Parse the problem pddl
def parse_problem(problem_pddl):
    iterator = iter(problem_pddl)
    if iterator.next() == "define":
        pass
    else:
        raise SystemExit("Error! This problem PDDL file is not a standard typed STRIPS PDDL file. It should begin with the keyword: define")
    problem_line = iterator.next()
    if problem_line[0] == "problem" and len(problem_line) == 2:
        yield problem_line[1]
    else:
         raise SystemExit("Error! This problem PDDL file is not a standard typed STRIPS PDDL file. It should include name of the problem")

    domain_line = iterator.next()
    assert domain_line[0] == ":domain" and len(domain_line) == 2
    yield domain_line[1]
    requirements_line = iterator.next()

    if  requirements_line[0] ==":requirements" and len(requirements_line) == 2:
        yield requirements_line[1]
    else:
        raise SystemExit("Error! This problem PDDL file is not a standard typed STRIPS PDDL file. It should include only one requirement!")

    objects_opt = iterator.next()
    if objects_opt[0] == ":objects":
        yield parse_typed_list(objects_opt[1:])
        init = iterator.next()
    else:
        yield []
        init = objects_opt

    if init[0] == ":init":
        initial = []
        for fact in init[1:]:
            initial.append(Atom(fact[0], fact[1:]))
        yield initial
    else:
        raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include inits")
    goal = iterator.next()
    if goal[0] == ":goal" and len(goal) == 2:
        yield parse_condition(goal[1])
    else:
        raise SystemExit("Error! This domain PDDL file is not a standard typed STRIPS PDDL file. It should include goals")
    
    for entry in iterator:
        assert False, entry

def loadIntoProblem(domainFile=None, problemFile=None):
    domain= Domain.get_instance(domainFile)
    problem= Problem.get_instance(problemFile)
    return Task(domain, problem)
    
# For Start, remove it if necessary
if __name__ == "__main__":
    # Please change the domainFile and problemFile if necessary, these two files should be in the working directory.
    domainFile ="domain1.pddl"
    problemFile ="problem1.pddl"
    
    task= loadIntoProblem(domainFile,problemFile)
    domain= Domain.get_instance(domainFile)
    problem= Problem.get_instance(problemFile)
    # Test the parser
    domain.printer()
    problem.printer()
    task_state = State(domain,problem )
    successor = task.successor(task_state)
    # Test the successor
    print successor
   
  
