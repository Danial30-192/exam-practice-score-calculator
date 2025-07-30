from colorama import init, Fore, Style





def restart_app():
    try:
     all_tests_number = int(input(Fore.LIGHTWHITE_EX + "Enter the total number of tests: " + Style.RESET_ALL))
     correct_answers = int(input(Fore.GREEN + "Enter the number of correct answers: " + Style.RESET_ALL))
     wrong_answers = int(input(Fore.RED+ "Enter the number of wrong answers: " + Style.RESET_ALL))
    except ValueError:
     print(Fore.RED + "Error: Please enter only numbers!" + Style.RESET_ALL)

     return
    if correct_answers + wrong_answers > all_tests_number:
        print(Fore.LIGHTRED_EX +"Error: The sum of correct and wrong answers can't be more than total tests." + Style.RESET_ALL )
        return  

    final_test_score_of_100 = ((correct_answers * 3 - wrong_answers) / (all_tests_number * 3) * 100)
    final_test_score_of_20 = ((correct_answers * 3 - wrong_answers) / (all_tests_number * 3) * 20)
    final_test_score_without_wrong_answers_count_of_20 = ((20 / all_tests_number) * correct_answers)
    final_test_score_without_wrong_answers_count_of_100 = ((100 / all_tests_number) * correct_answers)

    print(Fore.LIGHTWHITE_EX +"________________________________________________________________________________________________" + Style.RESET_ALL)
    print(Fore.CYAN + f"Your final test score (out of 100%) is: {final_test_score_of_100:.2f}" , "%" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX +"________________________________________________________________________________________________"+ Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "Your final test score (out of 20) is:" + Style.RESET_ALL , round(final_test_score_of_20, 2))
    print(Fore.LIGHTWHITE_EX +"________________________________________________________________________________________________"+ Style.RESET_ALL)
    print(Fore.GREEN +"Your score without penalty (100%) is:" + Style.RESET_ALL, round(final_test_score_without_wrong_answers_count_of_100, 2) , "%" )
    print(Fore.LIGHTWHITE_EX +"________________________________________________________________________________________________"+ Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "Your score without penalty (20) is:" + Style.RESET_ALL , round(final_test_score_without_wrong_answers_count_of_20, 2))
    print(Fore.LIGHTWHITE_EX +"________________________________________________________________________________________________"+ Style.RESET_ALL)
    if final_test_score_of_100 >= 50:
     print(Fore.LIGHTMAGENTA_EX + "Congratulations!!! You scored above the passing mark! Keep up the good work." + Style.RESET_ALL)

    elif 20 <= final_test_score_of_100 < 50:
        print(Fore.LIGHTWHITE_EX + "It doesn't look so good... but you can do better! I believe in you!" + Style.RESET_ALL)

    else:
        print(Fore.MAGENTA + "Bro it's bad... hey what are you doing with your life? Come on, you can be better than that!" + Style.RESET_ALL)
    


while True:
    restart_app()
    input(Fore.LIGHTWHITE_EX + "Press Enter to restart the app..." + Style.RESET_ALL)
