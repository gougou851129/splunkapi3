from splunkapi3.rest import Rest
from splunkapi3.search.alert import Alert
from splunkapi3.search.command import Command
from splunkapi3.search.saved import Saved


class Search(Rest):

    _alert = None
    _command = None
    _saved = None

    @property
    def alert(self):
        if not self._alert:
            self._alert = Alert(self.connection)
        return self._alert

    @property
    def command(self):
        if not self._command:
            self._command = Command(self.connection)
        return self._command

    @property
    def saved(self):
        if not self._saved:
            self._saved = Saved(self.connection)
        return self._saved
