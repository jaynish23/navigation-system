import os
import time
import threading
import services.voice_service as vs
import services.ui_service as ui
import services.commands_service as cs

vsObj = vs.voice_assistant()
uiObj = ui.UI()
csObj = cs.commands()

def main():
        global query_display, output_display
        vsObj.assistant_active = False
        os.system("start /B start cmd.exe @cmd /k python C:\\Users\\nikun\\Desktop\\nsvi\\nsvi\\objectDetection.py")
        while True:
            query = None
            query = vsObj.listen(1,1)
            if query != None and query != '':
                query_list = query.split()
                for str in query_list:
                    if(str == "hello"):
                        print("Assistant Activated")
                        vsObj.speak("Assistant Activated")
                        vsObj.assistant_active = True
                        break
            if vsObj.assistant_active:
                count = 3
                while(count):
                    count-=1
                    print(f"test input command {count}")
                    query = vsObj.listen(2,7)
                    if query != None and query != '':
                        print(query)
                        uiObj.query_display = query
                        query_list = query.split()
                        for str in query_list:
                            if(str in csObj.commands):
                                if(str == 'start'):
                                    output = csObj.commands[str]()
                                else:
                                    output = csObj.commands[str]()
                                uiObj.output_display = output
                                uiObj.update_text()
                                print(output)
                                vsObj.speak(output)
                                vsObj.assistant_active = False
                                count = 0
                                break
            with open('state.txt', 'r') as file:
                data = file.read().strip()
            file.close()
            if(data == 'true'):
                with open('voice.txt', 'r') as file:
                    cmd = file.read().strip()
                file.close()
                vsObj.speak(cmd)
                time.sleep(0.5)
                
            
                           
                        



loop_thread = threading.Thread(target=main)
loop_thread.daemon = True
loop_thread.start()
uiObj.root.mainloop()