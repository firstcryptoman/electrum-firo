from electrum_dash.i18n import _

fullname = _('LabelSync')
description = ' '.join([
    _("Save your wallet labels on a remote server, and synchronize them across multiple devices where you use Electrum-DASH."),
    _("Labels, transactions IDs and addresses are encrypted before they are sent to the remote server.")
])
available_for = ['qt', 'kivy']

