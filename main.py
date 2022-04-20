import helper

def run():
    welcome = print("********* Rock Paper Scissors *******")
    q1 = helper.yes_or_no()
    q2 = helper.selection()
    pc = helper.pc_select()
    outcome = helper.who_wins(q2, pc)
    print(outcome)

run()