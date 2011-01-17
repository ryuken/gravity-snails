
from scenes.mainmenu import MainMenu
from scenes.scenemanager import SceneManager
mySceneManager = SceneManager()
mySceneManager.setScene(MainMenu())
mySceneManager.run()