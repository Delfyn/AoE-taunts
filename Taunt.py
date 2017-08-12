import os
import time
import playsound # pip install playsound


class Taunts:
    """Main method to run"""

    path = "C:/Program Files (x86)/Steam/steamapps/common/Age2HD/resources/en/sound/taunt" # Windows
    name = "..." # Chat name

    def main(self):
        """Running mathod"""
        self.check_installation()
        self.play_sound()

    def check_installation(self):
        """Check if folder is correct"""
        print("Name nick : ", end='')
        self.name = input()

        if os.path.isdir(self.path) and os.path.exists(self.path + "/01 yes.mp3"): # Works only on Windows, Linux u must add path
            print("AoE folder loaded")
            print(os.listdir(self.path))
            print(os.path.isdir(self.path))
        else:
            print("Paste AoE/resources/en/sound/taunt folder -> ")
            print("Default path (steam): {}".format(
                "C:/Program Files (x86)/Steam/steamapps/common/Age2HD/resources/en/sound/taunt"))
            self.path = input()
            self.check_installation()

    def play_sound(self, repeat=.2):
        """Play sound"""
        path_list = os.listdir(self.path)
        my_list = []
        for i in range(0, len(path_list)):
            if path_list[i][0] == "0":
                my_list.insert(i, path_list[i][1])
            else:
                my_list.insert(i, path_list[i][0:2])

        while True:
            print(self.name, end=' : ')
            try:
                value = input()
                sound_to_play = value

                if '*' in sound_to_play: # Double list check, bad AF, but it works so .. :P
                    sound_to_play = value[0:value.index('*')]
                    multiply = value[value.index('*') + 1:]
                    for i in range(int(multiply)):
                        if int(sound_to_play) > 0 and int(sound_to_play) < len(my_list) + 1:
                            index = my_list.index(sound_to_play)
                            playsound.playsound(
                                "{}/{}".format(self.path, path_list[index]), False) # pip install playsound
                            time.sleep(repeat)
                else:
                    if int(sound_to_play) > 0 and int(sound_to_play) < len(my_list) + 1:
                        index = my_list.index(sound_to_play)
                        playsound.playsound(
                            "{}/{}".format(self.path, path_list[index]), False)
            except ValueError:
                pass


if __name__ == '__main__':
    taunt = Taunts()
    taunt.main()
