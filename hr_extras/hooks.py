# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hr_extras"
app_title = "Hr Extras"
app_publisher = "Ebkar Technology & Management Solutions"
app_description = "App That Extend the hr doctypes"
app_icon = "octicon octicon-flame"
app_color = "red"
app_email = "support@ebkarco.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_extras/css/hr_extras.css"
# app_include_js = "/assets/hr_extras/js/hr_extras.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_extras/css/hr_extras.css"
# web_include_js = "/assets/hr_extras/js/hr_extras.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hr_extras.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hr_extras.install.before_install"
# after_install = "hr_extras.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_extras.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hr_extras.tasks.all"
# 	],
# 	"daily": [
# 		"hr_extras.tasks.daily"
# 	],
# 	"hourly": [
# 		"hr_extras.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hr_extras.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hr_extras.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hr_extras.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hr_extras.event.get_events"
# }

