import email_service as es
import gui as GUI


gui = GUI.Gui()
emailService = es.EmailService()


def main():
    GUI.guiObj = gui
    emailService.start()
    gui.createGui()


if __name__ == "__main__":
    main()