import HalfLifeCalculator as hlc
import MotionEquationsCalculator as mec
import BindingEnergy as be

k = input(
    'Equations of motions (em) or Distance and speed equations (ds) or Half Life Equation (hl) or Binding Energy/Mass Defect (be)? ')

if k == 'em':
    answer = mec.main(k)
    print(answer)
elif k == 'ds':
    answer = mec.main(k)
    print(answer)
elif k == 'hl':
    answer = hlc.main(k)
    print(answer)
elif k == 'be':
    answer = be.main(k)
    print(answer)