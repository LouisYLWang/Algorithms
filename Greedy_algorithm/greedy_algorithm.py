#minimizing the weighted sum of completion times

def scoring(weight, length, score_method):
    if score_method == 'diff':
      return weight - length
    elif score_method == 'div':
      return weight/length

def run(score_method):
  file = open('jobs.txt')
  lines = file.readlines()
  jobs_ls = list()

  for line in lines[1:]:
    job_weight = int(line.split()[0])
    job_length = int(line.split()[1])
    job_score = scoring(job_weight, job_length, score_method)
    jobs_ls.append([job_score, job_weight, job_length])

  jobs_ls_sorted = sorted(jobs_ls, key = lambda _: (-_[0],-_[1]))
  res = 0
  complition_time = 0

  for job in jobs_ls_sorted:
    complition_time += job[2]
    res += job[1] * complition_time

  print('result of scoring method ' + str(score_method) + ' is ' + str(res))
  return res

run('diff')
run('div')