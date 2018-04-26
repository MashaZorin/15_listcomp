#True if password satisfies requirements
def min_pass_req(password):
    lower_case = [char for char in password if char.islower()]
    upper_case = [char for char in password if char.isupper()]
    nums = [char for char in password if char.isdigit()]

    if not(lower_case == [] or upper_case == [] or nums == []):
        return True
    else:
        return False

#returns the strenght of the password from 1 - 10
def pass_stren(password):
    lower_case = [char for char in password if char.islower()]
    upper_case = [char for char in password if char.isupper()]
    nums = [char for char in password if char.isdigit()]
    special = [char for char in password if char not in lower_case and char not in upper_case and char not in nums]

    score = 1

    if len(lower_case) > 2:
        score += 1
    if len(lower_case) > 5:
        score += 1
    if len(lower_case) > 10:
        score += 1
    if len(upper_case) > 0:
        score += 1
    if len(upper_case) > 2:
        score += 1
    if len(nums) > 0:
        score += 1
    if len(nums) > 2:
        score += 1
    if len(special) > 0:
        score += 1
    if len(special) > 1:
        score += 1

    return score


if __name__ == '__main__':
    pass1 = 'hi'
    pass2 = 'Hello1'
    pass3 = 'HelloMyFriends!1!1!1!'

    print (min_pass_req(pass1), ' is False')
    print (min_pass_req(pass2), ' is True')
    print (min_pass_req(pass3), ' is True')
    
    print (pass_stren(pass1), ' is 1')
    print (pass_stren(pass2), ' is 4')
    print (pass_stren(pass3), ' is 10')
