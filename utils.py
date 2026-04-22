def cost_function(income, credit_score, dti, loans):  # define function to compute cost based on inputs

    cost = 0  # initialize total cost to zero

    if income < 3000:  # check if income is very low
        cost += 5  # add high cost (high risk)
    elif income < 6000:  # check if income is medium
        cost += 3  # add medium cost
    else:  # income is high
        cost += 1  # add low cost (low risk)

    if credit_score < 600:  # check if credit score is poor
        cost += 6  # add high cost
    elif credit_score < 700:  # check if credit score is average
        cost += 3  # add medium cost
    else:  # credit score is good
        cost += 1  # add low cost

    if dti > 40:  # check if DTI ratio is high
        cost += 5  # add high cost
    elif dti > 30:  # check if DTI is moderate
        cost += 3  # add medium cost
    else:  # DTI is low
        cost += 1  # add low cost

    cost += loans  # add cost based on number of existing loans

    return cost  # return final computed cost


def heuristic(cost):  # define heuristic function (estimate of future cost)

    return cost * 0.5  # return estimated cost (simple proportional heuristic)