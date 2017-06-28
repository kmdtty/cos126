"""
Gambler's ruin

Reference:
http://mathworld.wolfram.com/GamblersRuin.html

"""
import sys
import  random
def gambler(stake, goal, trials):
  wins = 0.0
  trial = 0.0
  while(stake > 0 and stake <goal and trial < trials):
    trial += 1.0
    # (01)
    r = random.random()
    if r >= 0.5:
      wins += 1
      stake += 1
    else:
      stake -= 1
  print('wins(%s)/trial(%s) = %s' % (wins, trial, str(wins/trial)))
  print('stake = %d' % stake)

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print('USAGE:\n python gambler.py <stake> <goal> <trials>')
    exit(-1)
  stake = int(sys.argv[1])
  goal = int(sys.argv[2])
  trials = int(sys.argv[3])
  gambler(stake, goal, trials)
