def calc(expense, requested, max_amount, used):
    if expense <= 0:
        return 0
    else:
        if requested <= 0:
            return 0
        else:
            if used >= max_amount:
                return 0
            else:
                left = max_amount - used
                if requested > left:
                    if left > expense:
                        return expense
                    return left
                else:
                    if requested > expense:
                        return expense
                    return requested