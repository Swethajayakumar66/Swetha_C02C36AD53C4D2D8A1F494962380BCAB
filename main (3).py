class player:
    def play(self):
        print("The player is playing cricket.")


class Batsman(player):
  def play(self):
    print("The batsman is batting.")
class Bowler(player):
   def play(self):
     print("the Bowler is bowling.")
batsman= Batsman()
bowler= Bowler()

batsman.play()
Bowler.play()