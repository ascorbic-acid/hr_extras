from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Recruitment"),
			"items": [
				{
					"type": "doctype",
					"name": "Custody Issuance Form",
					"description": _("Custody Issuance Form for you."),
				},
			]
		}
	]
