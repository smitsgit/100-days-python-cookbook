from queue import Queue
from threading import Thread, Event, current_thread


class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self.mail_box = Queue()

    def send(self, msg):
        self.mail_box.put(msg)

    def recv(self):
        msg = self.mail_box.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def start(self):
        self._terminated = Event()
        Thread(target=self._bootstrap, daemon=True).start()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            print("Hello Det")
            msg = self.recv()
            print("Got ", msg)


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print(f"{current_thread().name}: Got ###", msg)


def main():
    print(current_thread().name)
    actor = PrintActor()
    actor.start()
    actor.send("Hello")
    actor.close()
    actor.join()


if __name__ == '__main__':
    main()
