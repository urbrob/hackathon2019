from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

class UserMenu(Menu):
    def get_nodes(self, request):
            return [
                NavigationNode(_("Profile"), reverse(profile), 1, attr={'visible_for_anonymous': False}),
                NavigationNode(_("Log in"), reverse(login), 3, attr={'visible_for_authenticated': False}),
                NavigationNode(_("Sign up"), reverse(logout), 4, attr={'visible_for_authenticated': False}),
                NavigationNode(_("Log out"), reverse(logout), 2, attr={'visible_for_anonymous': False}),
            ]
