from graph import Node  # import Node class from graph file

from utils import cost_function, heuristic  # import cost and heuristic functions


def evaluate_loan(income, credit_score, dti, loans, loan_amount):  # main AO* evaluation function

    explanation = []  # list to store explanation steps

    root = Node("Loan", "AND")  # create root node representing loan application

    income_node = Node("Income Check", "AND")  # create node for income condition

    credit_node = Node("Credit Check", "AND")  # create node for credit score condition

    dti_node = Node("DTI Check", "AND")  # create node for DTI condition

    decision_node = Node("Decision", "OR")  # create OR node for decision making

    approve = Node("Approve", "OR")  # create node for approve decision

    review = Node("Review", "OR")  # create node for review decision

    reject = Node("Reject", "OR")  # create node for reject decision

    root.add_child(income_node)  # connect income check to root

    root.add_child(credit_node)  # connect credit check to root

    root.add_child(dti_node)  # connect DTI check to root

    root.add_child(decision_node)  # connect decision node to root

    decision_node.add_child(approve)  # add approve option under decision node

    decision_node.add_child(review)  # add review option

    decision_node.add_child(reject)  # add reject option

    base_cost = cost_function(income, credit_score, dti, loans)  # compute base cost using inputs

    approve.cost = base_cost  # assign base cost to approve decision

    review.cost = base_cost + 3  # assign slightly higher cost to review

    reject.cost = base_cost + 6  # assign highest cost to reject

    approve.heuristic = heuristic(approve.cost)  # compute heuristic for approve

    review.heuristic = heuristic(review.cost)  # compute heuristic for review

    reject.heuristic = heuristic(reject.cost)  # compute heuristic for reject

    decisions = [approve, review, reject]  # create list of decision nodes

    best = min(decisions, key=lambda x: x.cost + x.heuristic)  # select node with minimum total cost

    explanation.append(f"Income = {income}")  # add income info to explanation

    explanation.append(f"Credit Score = {credit_score}")  # add credit score info

    explanation.append(f"DTI = {dti}")  # add DTI info

    explanation.append(f"Loans = {loans}")  # add loan count info

    explanation.append(f"Base Cost = {base_cost}")  # show base cost

    explanation.append("AO* selected node with minimum (cost + heuristic)")  # explain selection logic

    explanation.append(f"Selected Decision = {best.name}")  # show chosen decision

    return best.name, best.cost, explanation  # return final decision, cost, explanation