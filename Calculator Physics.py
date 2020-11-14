import HalfLifeCalculator as hlc
import MotionEquationsCalculator as mec

k = input(
    'Equations of motions (em) or Distance and speed equations (ds) or Half Life Equation (hl)? ')

if k == 'em':
    answer = mec.main(k)
    print(answer)
elif k == 'ds':
    answer = mec.main(k)
    print(answer)
elif k == 'hl':
    answer = hlc.main(k)
    print(answer)