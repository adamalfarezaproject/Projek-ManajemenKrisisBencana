from chatbot.state import State


class FSM:

    def __init__(self):

        self.current_state = State.IDLE

    def transition(self, intent):

        # ==========================
        # GLOBAL COMMAND
        # ==========================

        if intent in ["RESET", "MENU"]:

            self.current_state = State.IDLE

            return self.current_state

        # ==========================
        # MENU UTAMA
        # ==========================

        if self.current_state == State.IDLE:

            if intent == "BANJIR":

                self.current_state = State.BANJIR_MENU

            elif intent == "GEMPA":

                self.current_state = State.GEMPA_MENU

            elif intent == "LONGSOR":

                self.current_state = State.LONGSOR_MENU

            elif intent == "KEBAKARAN":

                self.current_state = State.KEBAKARAN_MENU

            elif intent == "TSUNAMI":

                self.current_state = State.TSUNAMI_MENU

            elif intent == "STATUS":

                self.current_state = State.INPUT_ID

        # ==========================
        # MENU BENCANA
        # ==========================

        elif self.current_state in [

            State.BANJIR_MENU,
            State.GEMPA_MENU,
            State.LONGSOR_MENU,
            State.KEBAKARAN_MENU,
            State.TSUNAMI_MENU

        ]:

            if intent == "LAPOR":

                self.current_state = State.INPUT_NAMA

        return self.current_state