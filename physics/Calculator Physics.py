import HalfLifeCalculator as hlc
import MotionEquationsCalculator as mec
import BindingEnergy as be
import gravity_motion_calculator as gmc

k = input(
    "Equations of motions (em) or Distance and speed equations (ds) or Half Life Equation (hl) or Binding Energy/Mass Defect (be) or Gravity and Motion (gmc)? "
)

if k == "em":
    answer = mec.main(k)
    print(answer)
elif k == "ds":
    answer = mec.main(k)
    print(answer)
elif k == "hl":
    answer = hlc.main()
    print(answer)
elif k == "be":
    answer = be.main()
elif k == "gmc":
    answer = gmc.main()
