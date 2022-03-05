import pyautogui as auto
import time 
x=0

while x<100000:
    auto.moveTo(822,631, duration=3, tween=auto.easeInOutQuad)
    auto.click(822,631) 
    auto.moveTo(849,681, duration=1, tween=auto.easeInOutQuad)
    auto.click(849,681)
    auto.moveTo(894, 759, duration=1, tween=auto.easeInOutQuad)
    auto.click(894, 759)
    auto.moveTo(903,689, duration=1, tween=auto.easeInOutQuad)
    auto.click(903,689)
    auto.moveTo(920,690, duration=1, tween=auto.easeInOutQuad)
    auto.click(920,690)
    print(x)
    x+=1