from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')

def get_socket_stream(name):
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    socket = None
    for device in paired_devices:
        if device.getName() == name:
            socket = device.createInsecureRfcommSocket(25)
            recv_stream = socket.getInputStream()
            send_stream = socket.getOutputStream()
            break
    socket.connect()
    return recv_stream, send_stream

if __name__ == '__main__':
#    kv = '''

    from kivy.lang import Builder
    Builder.load_string('''
<mainscreen>
    output: text_output
    BoxLayout:
        orientation: 'vertical'
        ToggleButton:
            id: b1
            text: '1'
            on_release: app.send(self.text)
        ToggleButton:
            id: b2
            text: '2'
            on_release: app.send(self.text)
        ToggleButton:
            id: b3
            text: '3'
            on_release: app.send(self.text)
        ToggleButton:
            id: b4
            text: '4'
            on_release: app.send(self.text)
        ToggleButton:
            id: b5
            text: '5'
            on_release: app.send(self.text)
        Label:
            id: text_output
            text: 'initial'
    ''')
    
    from kivy.app import App
    from kivy.app import ObjectProperty
    import threading
    import time
    from kivy.uix.screenmanager import Screen
    
    class mainscreen(Screen):
        def update_text(self,text):
            self.output.text = text

    class Bluetooth(App):

        def build(self):
            self.mainscree = mainscreen()
            self.recv_stream, self.send_stream = get_socket_stream('DMachine')
            rcv = threading.Thread(target=self.recv)
            rcv.start()
            return self.mainscree#Builder.load_string(kv)

        def send(self, cmd):
            self.send_stream.write(('{}\n'.format(cmd)).encode())
            self.send_stream.flush()

        def recv(self):
            while True:
                #self.text_output.text = "second"
                print("python in rceive")
                #if self.recv_stream.readable():
                #self.text_output.text = self.recv_stream.read()
                self.mainscree.update_text(self.recv_stream.read())
                # else:
                #     time.sleep(1)

        def reset(self, btns):
            for btn in btns:
                btn.state = 'normal'
            self.send('0\n')

    Bluetooth().run()

