#批量梗概目录下的文件名称

import os
from multiprocessing import Pool

def shorten(n):
  os.rename(n, n[0:-5])
base = '/media/zzx/DATA1/segmentation/'


if __name__ == "__main__":
  types = ['ApplyEyeMakeup','ApplyLipstick','Archery','BabyCrawling','BalanceBeam','BandMarching','BaseballPitch','Basketball','BasketballDunk',
'BenchPress','Biking','Billiards','BlowDryHair','BlowingCandles','BodyWeightSquats','Bowling','BoxingPunchingBag','BoxingSpeedBag','BreastStroke','BrushingTeeth',
'CleanAndJerk','CliffDiving','CricketBowling','CricketShot','CuttingInKitchen','Diving','Drumming','Fencing','FieldHockeyPenalty','FloorGymnastics','FrisbeeCatch',
'FrontCrawl','GolfSwing','Haircut','Hammering','HammerThrow','HandstandPushups','HandstandWalking','HeadMassage','HighJump','HorseRace','HorseRiding','HulaHoop',
'IceDancing','JavelinThrow','JugglingBalls','JumpingJack','JumpRope','Kayaking','Knitting','LongJump','Lunges','MilitaryParade','Mixing','MoppingFloor','Nunchucks',
'ParallelBars','PizzaTossing','PlayingCello','PlayingDaf','PlayingDhol','PlayingFlute','PlayingGuitar','PlayingPiano']
  for t in types:
    dir_type = base +t +'/'
    names = os.listdir(dir_type)

    for i in range(len(names)):
      names[i] = dir_type+names[i]

    p = Pool(8)
    p.map(shorten, names)
    p.close()
    p.join()

