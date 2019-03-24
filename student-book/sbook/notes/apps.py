from django.apps import AppConfig


class NotesConfig(AppConfig):
    name = "notes"

    def ready(self):
        from notes import signals
