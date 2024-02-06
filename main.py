import time
from kivy.uix.popup import Popup
import ast
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
kv = Builder.load_file("cal.kv")


class MyLayout(Widget):
    history = []

    def clear(self):
        self.ids.Text_in.text = ""

    def numbers(self, numbers):
        result = self.ids.Text_in.text
        if "Error" in result:
            result = ""
        elif "arshiamoshgin0@gmail.com" in result:
            result = ""
        elif result == "0":
            self.ids.Text_in.text = ""
            result = self.ids.Text_in.text

        result = f"{result}{numbers}"
        self.ids.Text_in.text = result

    def buttons(self, button):
        signs = ["+", "-", "/", "%", "*"]
        result = self.ids.Text_in.text
        if result == "":
            pass
        elif result[-1] in signs:
            result = result.replace(result[-1], button)
            self.ids.Text_in.text = result
        else:
            result = f"{result}{button}"
            self.ids.Text_in.text = result

    def dot(self, dot):
        result = self.ids.Text_in.text
        num_list = result.split("+")
        if "+" in result and "." not in num_list[-1]:
            result = f"{result}{dot}"
            self.ids.Text_in.text = result
        elif "." in result:
            pass
        else:
            result = f"{result}{dot}"
            self.ids.Text_in.text = result

    def equal(self):
        result = self.ids.Text_in.text

        try:
            # answer = eval(result)
            # self.ids.Text_in.text = str(answer)
            node = ast.parse(result, mode="eval")
            answer = eval(compile(node, "<string>", "eval"))
            self.ids.Text_in.text = str(answer)
            self.history.append(answer)
        except:
            self.ids.Text_in.text = "Error"

    def remove(self):
        result = self.ids.Text_in.text
        result = result[:-1]
        self.ids.Text_in.text = result

    def emailshow(self):
        self.ids.Text_in.text = "arshiamoshgin0@gmail.com"


class MyPopup(Popup):
    def history_show(self):
        last_history = ""
        for i in MyLayout().history:
            last_history = f"{last_history}\n{i}"
        print(last_history)
        return last_history

    def history_clear(self):
        MyLayout().history.clear()
        self.ids.History.text = ""


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
