# since question is specific for 7 day period, solution is easier
def optimalFreelancing(jobs):
    # sort jobs by payment
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    days_assigned = 0
    assigned = set()
    total_payment = 0
    
    for job in jobs:
        if days_assigned == 7:
            break
        # try to fit the highest paying job as late as possible based on deadline
        try_day = job["deadline"]
        while try_day > 0:
            if try_day not in assigned:
                assigned.add(try_day)
                total_payment += job["payment"]
                days_assigned += 1         
                break
            try_day -= 1
           
    return total_payment
        
