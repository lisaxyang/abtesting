from scipy import stats
from scipy.stats import t as t_dist
from scipy.stats import chi2    

from abtesting_test import *

# You can comment out these lines! They are just here to help follow along to the tutorial.
# print(t_dist.cdf(-2, 20)) # should print .02963
# print(t_dist.cdf(2, 20)) # positive t-score (bad), should print .97036 (= 1 - .2963)

# print(chi2.cdf(23.6, 12)) # prints 0.976
# print(1 - chi2.cdf(23.6, 12)) # prints 1 - 0.976 = 0.023 (yay!)

# TODO: Fill in the following functions! Be sure to delete "pass" when you want to use/run a function!
# NOTE: You should not be using any outside libraries or functions other than the simple operators (+, **, etc)
# and the specifically mentioned functions (i.e. round, cdf functions...)

def slice_2D(list_2D, start_row, end_row, start_col, end_col):
    '''
    Splices a the 2D list via start_row:end_row and start_col:end_col
    :param list: list of list of numbers
    :param nums: start_row, end_row, start_col, end_col
    :return: the spliced 2D list (ending indices are exclsive)
    '''
    to_append = []
    for l in range(start_row, end_row):
        to_append.append(list_2D[l][start_col:end_col])

    return to_append

def get_avg(nums):
    '''
    Helper function for calculating the average of a sample.
    :param nums: list of numbers
    :return: average of list
    '''
    #TODO: fill me in!
    # pass

    # my_sum = 0
    list_length = len(nums)
    # for number in nums:
    #     my_sum = my_sum + number
    my_sum = sum(nums)
    # print("I am returning ", my_sum, " divided by ", list_length)
    # print("value is ", my_sum / list_length)
    return (my_sum / list_length)

def get_stdev(nums):
    '''
    Helper function for calculating the standard deviation of a sample.
    :param nums: list of numbers
    :return: standard deviation of list
    '''
    #TODO: fill me in!
    # pass

    #gets numerator of fraction
    #avg of the list of numbers
    avg = get_avg(nums)
    new_nums = []
    for i in nums:
        i = (i-avg)**2
        new_nums.append(i)

    my_sum = sum(new_nums)

    # gets n-1 for denominator
    denom = len(nums) - 1

    fraction = my_sum / denom

    return fraction**(1/2)


def get_standard_error(a, b):
    '''
    Helper function for calculating the standard error, given two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: standard error of a and b (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    # pass

    std_asq = get_stdev(a)**2
    n_a = len(a)
    std_bsq = get_stdev(b)**2
    n_b = len(b)

    frac_a = std_asq / n_a
    frac_b = std_bsq / n_b
    
    frac_sum = frac_a + frac_b

    return frac_sum**(1/2)

def get_2_sample_df(a, b):
    '''
    Calculates the combined degrees of freedom between two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: integer representing the degrees of freedom between a and b (see studio 6 guide for this equation!)
    HINT: you can use Math.round() to help you round!
    '''
    #TODO: fill me in!
    # pass

    #standard error between two lists
    se_4 = get_standard_error(a,b)**4

    #standard deviation squared and size of both lists
    std_asq = get_stdev(a)**2
    n_a = len(a)
    std_bsq = get_stdev(b)**2
    n_b = len(b)

    de_frac_a = ((std_asq/n_a)**2) / (n_a - 1)
    de_frac_b = ((std_bsq/n_b)**2) / (n_b - 1)

    denom = de_frac_a + de_frac_b

    frac = se_4 / denom

    return round(frac)


def get_t_score(a, b):
    '''
    Calculates the t-score, given two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: number representing the t-score given lists a and b (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    # pass

    difference = get_avg(a) - get_avg(b)

    return difference / (get_standard_error(a,b))


def perform_2_sample_t_test(a, b):
    '''
    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)
    Calculates a p-value by performing a 2-sample t-test, given two lists of numbers.
    :param a: list of numbers
    :param b: list of numbers
    :return: calculated p-value
    HINT: the t_dist.cdf() function might come in handy!
    '''
    #TODO: fill me in!
    # pass

    neg_t_val = -abs(get_t_score(a,b))
    p_val = t_dist.cdf(neg_t_val, get_2_sample_df(a,b))
    return p_val


# [OPTIONAL] Some helper functions that might be helpful in get_expected_grid().
def row_sum(observed_grid, ele_row):
    row_length = len(observed_grid)
    col_length = len(observed_grid[0])
    spliced_row = slice_2D(observed_grid, ele_row, ele_row+1, 
        0, col_length)
    # print(spliced_row)
    # sum = 0
    # for i in range(0, row_length):
    #     sum = sum + spliced_row[0][i]
    # return sum
    return sum(sum(spliced_row,[]))

def col_sum(observed_grid, ele_col):
    # print('ele_col is ' + str(ele_col))
    row_length = len(observed_grid)
    col_length = len(observed_grid[0])
    spliced_col = slice_2D(observed_grid, 0, row_length, 
        ele_col, ele_col+1)
    # print(spliced_col)
    # sum = 0
    # for i in range(0, col_length):
    #     sum = sum + spliced_col[i][0]
    #     # print("sum is "+ str(sum))
    # return sum
    return sum(sum(spliced_col,[]))

def total_sum(observed_grid):
    return sum(sum(observed_grid,[]))


def calculate_expected(row_sum, col_sum, tot_sum):
    numerator = row_sum*col_sum
    return (numerator/tot_sum)

def get_expected_grid(observed_grid):
    '''
    Calculates the expected counts, given the observed counts.
    ** DO NOT modify the parameter, observed_grid. **
    :param observed_grid: 2D list of observed counts
    :return: 2D list of expected counts
    HINT: To clean up this calculation, consider filling in the optional helper functions below!
    '''
    #TODO: fill me in!
    # pass

    num_rows = len(observed_grid)
    num_cols = len(observed_grid[0])
    expected_grid = [[0 for x in range(num_cols)] for y in range(num_rows)]
    tot_sum = total_sum(observed_grid)
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            expected_ij = calculate_expected(row_sum(observed_grid,i),
                col_sum(observed_grid,j), tot_sum)
            expected_grid[i][j] = expected_ij

    return expected_grid
        
# print(get_expected_grid([[207,282],[231,242]]))

def df_chi2(observed_grid):
    '''
    Calculates the degrees of freedom of the expected counts.
    :param observed_grid: 2D list of observed counts
    :return: degrees of freedom of expected counts (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    # pass
    num_rows = len(observed_grid)
    num_cols = len(observed_grid[0])
    return (num_rows-1)*(num_cols-1)

def chi2_value(observed_grid):
    '''
    Calculates the chi^2 value of the expected counts.
    :param observed_grid: 2D list of observed counts
    :return: associated chi^2 value of expected counts (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    # pass
    expected_grid = get_expected_grid(observed_grid)

    num_rows = len(observed_grid)
    num_cols = len(observed_grid[0])
    chi_grid = [[0 for x in range(num_cols)] for y in range(num_rows)]

    for i in range(0, num_rows):
        for j in range(0, num_cols):
            numerator = (observed_grid[i][j] - expected_grid[i][j])**2
            chi = numerator / (expected_grid[i][j])
            chi_grid[i][j] = chi

    return sum(sum(chi_grid,[]))


def perform_chi2_homogeneity_test(observed_grid):
    '''
    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)
    Calculates the p-value by performing a chi^2 test, given a list of observed counts
    :param observed_grid: 2D list of observed counts
    :return: calculated p-value
    HINT: the chi2.cdf() function might come in handy!
    '''
    #TODO: fill me in!
    # pass

    chi_2 = chi2_value(observed_grid)
    df = df_chi2(observed_grid)

    return (1-chi2.cdf(chi_2, df))

# These commented out lines are for testing your main functions. 
# Please uncomment them when finished with your implementation and confirm you get the same values :)
def data_to_num_list(s):
  '''
    Takes a copy and pasted row/col from a spreadsheet and produces a usable list of nums. 
    This will be useful when you need to run your tests on your cleaned log data!
    :param str: string holding data
    :return: the spliced list of numbers
    '''
  return list(map(float, s.split()))


# print(get_avg([1,2,3,43,54]))
# print(get_stdev([4, 5, 8, 9, 10]))
# a_t1_list = [3,3,3,12,15,16,17,19,23,24,32]
# b_t1_list = [20,13,13,20,29,32,23,20,25,15,30]
# print(get_t_score(a_t1_list, b_t1_list)) 
# print(perform_2_sample_t_test(a_t1_list, b_t1_list)) 

# a_t2_list = data_to_num_list(a2) 
# b_t2_list = data_to_num_list(b2)
# print('average of a:\t' + str(get_avg(a_t2_list)))
# print('std of a:\t' + str(get_stdev(a_t2_list)))
# print('se of a,b:\t' + str(get_standard_error(a_t2_list, b_t2_list)))
# print('df of a,b :\t' + str(get_2_sample_df(a_t2_list, b_t2_list)))
# print(get_t_score(a_t2_list, b_t2_list))
# print(perform_2_sample_t_test(a_t2_list, b_t2_list))


""""""
# t_test 1:
a_t1_list = data_to_num_list(a1) 
b_t1_list = data_to_num_list(b1)
print(get_t_score(a_t1_list, b_t1_list)) # this should be -129.500
print(perform_2_sample_t_test(a_t1_list, b_t1_list)) # this should be 0.0000
# why do you think this is? Take a peek at a1 and b1 in abtesting_test.py :)

# t_test 2:
a_t2_list = data_to_num_list(a2) 
b_t2_list = data_to_num_list(b2)
print(get_t_score(a_t2_list, b_t2_list)) # this should be -1.48834
print(perform_2_sample_t_test(a_t2_list, b_t2_list)) # this should be .082379

# t_test 3:
a_t3_list = data_to_num_list(a3) 
b_t3_list = data_to_num_list(b3)
print(get_t_score(a_t3_list, b_t3_list)) # this should be -2.88969
print(perform_2_sample_t_test(a_t3_list, b_t3_list)) # this should be .005091
"""

"""
# chi2_test 1:
a_c1_list = data_to_num_list(a_count_1) 
b_c1_list = data_to_num_list(b_count_1)
c1_observed_grid = [a_c1_list, b_c1_list]
print(chi2_value(c1_observed_grid)) # this should be 4.103536
print(perform_chi2_homogeneity_test(c1_observed_grid)) # this should be .0427939

# chi2_test 2:
a_c2_list = data_to_num_list(a_count_2) 
b_c2_list = data_to_num_list(b_count_2)
c2_observed_grid = [a_c2_list, b_c2_list]
print(chi2_value(c2_observed_grid)) # this should be 33.86444
print(perform_chi2_homogeneity_test(c2_observed_grid)) # this should be 0.0000
# Again, why do you think this is? Take a peek at a_count_2 and b_count_2 in abtesting_test.py :)

# chi2_test 3:
a_c3_list = data_to_num_list(a_count_3) 
b_c3_list = data_to_num_list(b_count_3)
c3_observed_grid = [a_c3_list, b_c3_list]
print(chi2_value(c3_observed_grid)) # this should be .3119402
print(perform_chi2_homogeneity_test(c3_observed_grid)) # this should be .57649202
""""""


