import testapi as t

t.get_games()
t.get_player()



t.Postgamemove("7","2","1","1")
t.get_gamestatus()
t.Postgamemove("7","1","1","2")
t.get_gamestatus()
t.Postgamemove("7","2","1","3")
t.get_gamestatus()
t.Postgamemove("7","1","2","1")
t.get_gamestatus()
t.Postgamemove("7","2","2","2")
t.get_gamestatus()
t.Postgamemove("7","1","2","3")
t.get_gamestatus()
t.Postgamemove("7","2","3","3")
t.get_gamestatus()
t.Postgamemove("7","1","3","1")
t.get_gamestatus()
t.Postgamemove("7","2","3","2")

t.get_games()
t.get_player()
t.get_gamestatus()




